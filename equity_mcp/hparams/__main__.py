"""
Hyperparameter snapshots: build, store and verify them.

    python -m equity_mcp.hparams snapshot [--out FILE]        # current code, no database
    python -m equity_mcp.hparams sync --current [--dry-run]   # store today's config
    python -m equity_mcp.hparams sync --from-run-dir runs/AAPL_20261012T101500 ...
    python -m equity_mcp.hparams sync --backfill [--dry-run] [--file outputs/X.json ...]
    python -m equity_mcp.hparams sync --flush-pending
    python -m equity_mcp.hparams verify [--db]

Runs started by the orchestrator capture their own config (runs/<id>/config.json),
and ``evaluate`` links them as it stores the evaluation. ``sync`` exists for
everything else.

Exit codes follow ``evaluate --sync-rubrics``:
- 0: ok.
- 1: error.
- 2: done, but some links are only inferred, or records went to the pending fallback.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
from pathlib import Path

from dotenv import load_dotenv

from equity_mcp.hparams import backfill as bf
from equity_mcp.hparams.capture import git_dirty, git_sha
from equity_mcp.hparams.ingest import REPO_ROOT, load_run_config, payload_from_run_config
from equity_mcp.hparams.snapshot import Snapshot, build_snapshot, config_sha

load_dotenv()


def _print_snapshot(snap: Snapshot) -> None:
    rt = snap.runtime
    print(f"config_sha  {snap.sha}", flush=True)
    print(f"provenance  {snap.provenance}   git={(snap.source_git_sha or '?')[:7]}"
          f"{'+dirty' if snap.source_git_dirty else ''}   gaps={snap.gaps or '-'}", flush=True)
    print(f"runtime     tool_timeout={rt.get('tool_timeout_s')}s threads={rt.get('max_tool_threads')} "
          f"agent_timeout={rt.get('agent_timeout_s')}s concurrency={rt.get('default_max_concurrency')} "
          f"request_timeout={rt.get('request_timeout_ms')}ms advertised={rt.get('advertised_fraction')}", flush=True)
    print(f"tools       {len(snap.tools)} registered, {len(snap.role_tools)} role grants, "
          f"{len(snap.texts)} distinct texts", flush=True)
    print(f"  {'role':<22} {'stage':>5} {'kind':<17} {'model':<34} {'tokens':>6} {'recur':>5} "
          f"{'adv':>9} {'tools':>5}", flush=True)
    for a in snap.agents:
        adv = f"{a['advertised_tool_rounds']}/{a['advertised_write_by']}" if a["advertised_tool_rounds"] else "-"
        print(f"  {a['role']:<22} {a['stage']:>5} {a['agent_kind']:<17} {a['model_slug'] or '-':<34} "
              f"{a['max_tokens'] or '-':>6} {a['recursion_limit'] or '-':>5} {adv:>9} {a['tool_count']:>5}",
              flush=True)


def _store():
    from equity_mcp.evaluation.store import make_store

    store = make_store(False)
    if store.kind != "supabase":
        raise SystemExit("error: needs SUPABASE_EVAL_DB_URL")
    return store


async def _fetch(store, sql: str, params: tuple = ()) -> list[tuple]:
    def _q():
        with store.conn.cursor() as cur:
            cur.execute(sql, params)
            rows = cur.fetchall()
        store.conn.rollback()
        return rows
    return await store._run(_q)


async def _save_all(store, payloads: list[dict]) -> int:
    pending = 0
    for p in payloads:
        where = await store.save_hparams(p)
        cfg = (p.get("snapshot") or {}).get("config", {}).get("config_sha", "")
        runs = ",".join(link["run_id"] for link in p.get("links") or []) or "-"
        print(f"  {where:<9} config={cfg[:12] or '-':<12} runs={runs}", flush=True)
        pending += where != "supabase"
    return pending


# ── commands ──────────────────────────────────────────────────────────────────


def cmd_snapshot(args: argparse.Namespace) -> int:
    snap = asyncio.run(build_snapshot(provenance="reconstructed_from_git", source_git_sha=git_sha(),
                                      source_git_dirty=git_dirty()))
    _print_snapshot(snap)
    if args.out:
        Path(args.out).write_text(json.dumps(snap.to_record(), indent=1, ensure_ascii=False), encoding="utf-8")
        print(f"written → {args.out}", flush=True)
    problems = snap.problems()
    for p in problems:
        print(f"  ✗ {p}", flush=True)
    return 1 if problems else 0


def cmd_sync(args: argparse.Namespace) -> int:
    if args.flush_pending:
        from equity_mcp.evaluation.store import flush_pending

        saved, failed = asyncio.run(flush_pending())
        print(f"flushed {saved} pending records ({failed} still pending)", flush=True)
        return 2 if failed else 0

    if args.current:
        dirty = git_dirty()
        # Exact for the working tree either way, but only a clean tree can be reproduced from git.
        snap = asyncio.run(build_snapshot(provenance="inferred" if dirty else "reconstructed_from_git",
                                          source_git_sha=git_sha(), source_git_dirty=dirty,
                                          label=args.label))
        _print_snapshot(snap)
        payloads = [{"snapshot": snap.to_record(), "links": []}]
        inferred = False
    elif args.from_run_dir:
        payloads = []
        for d in map(Path, args.from_run_dir):
            cfg = load_run_config(d.name, d.parent)
            if cfg is None:
                print(f"  ✗ {d}: no config.json", file=sys.stderr, flush=True)
                continue
            payloads.append(payload_from_run_config(d.name, cfg))
        inferred = False
    else:  # --backfill
        paths = ([Path(p) for p in args.file] if args.file
                 else sorted((REPO_ROOT / "outputs").glob("*.json")))
        plans = bf.plan(paths)
        if not args.dry_run:
            store = _store()

            async def _ids() -> set[str]:
                async with store:
                    if store.conn is None:
                        raise SystemExit("error: evaluation database unreachable")
                    return {r[0] for r in await _fetch(store, "SELECT run_id FROM eval.runs WHERE skip_reason IS NULL")}
            stored = asyncio.run(_ids())
            for lp in plans:
                if lp.sha and lp.run.run_id not in stored:
                    lp.notes.append("not in eval.runs; evaluate it first")
                    lp.sha = None
        _print_plan(plans)
        if args.dry_run:
            return 0
        payloads, errors = bf.build_payloads(plans)
        for e in errors:
            print(f"  ✗ {e}", file=sys.stderr, flush=True)
        if errors and not payloads:
            return 1
        inferred = any(lp.basis == "inferred" for lp in plans if lp.sha)

    if args.dry_run:
        print("dry run: nothing stored", flush=True)
        return 0

    async def _go() -> int:
        store = _store()
        async with store:
            return await _save_all(store, payloads)
    pending = asyncio.run(_go())
    return 2 if pending or inferred else 0


def _print_plan(plans: list[bf.LinkPlan]) -> None:
    print(f"  {'run':<24} {'kind':<5} {'commit':<8} {'basis':<13} overrides / notes", flush=True)
    for lp in plans:
        ov = ",".join(f"{k.rsplit('.', 1)[-1]}={v:g}" for k, v in lp.overrides.items())
        print(f"  {lp.run.run_id:<24} {lp.run.kind:<5} {(lp.sha or '-')[:7]:<8} {lp.basis or 'unlinked':<13} "
              f"{ov + ' ' if ov else ''}{lp.notes[0] if lp.notes else ''}", flush=True)
    linked = [lp for lp in plans if lp.sha]
    by = {b: sum(lp.basis == b for lp in linked) for b in ("git_checkout", "inferred")}
    print(f"  {len(linked)} linked ({by['git_checkout']} git_checkout, {by['inferred']} inferred), "
          f"{len(plans) - len(linked)} unlinked, {len({lp.key for lp in linked})} distinct configs", flush=True)


def cmd_verify(args: argparse.Namespace) -> int:
    snap = asyncio.run(build_snapshot(provenance="reconstructed_from_git", libs=False))
    problems = [f"live snapshot: {p}" for p in snap.problems()]
    print(f"live snapshot {snap.sha[:12]}: {len(snap.agents)} agents, {len(snap.tools)} tools, "
          f"{len(snap.role_tools)} grants, gaps={snap.gaps or '-'}", flush=True)

    if args.db:
        store = _store()

        async def _db() -> list[str]:
            out: list[str] = []
            async with store:
                if store.conn is None:
                    return ["evaluation database unreachable"]
                for sha, content in await _fetch(store, "SELECT config_sha, content FROM hparams.configs"):
                    if config_sha(content) != sha:
                        out.append(f"config {sha[:12]}: content no longer hashes to its key")
                for row in await _fetch(store, "SELECT issue, config_sha, role, tool_name FROM hparams.v_config_integrity"):
                    out.append(f"integrity: {row[0]} ({row[1][:12]} {row[2] or ''} {row[3] or ''})")
                for (run_id,) in await _fetch(store, """
                        SELECT r.run_id FROM eval.runs r LEFT JOIN hparams.run_configs c USING (run_id)
                        WHERE r.skip_reason IS NULL AND c.run_id IS NULL ORDER BY 1"""):
                    out.append(f"run {run_id} has no config link")
                for row in await _fetch(store, "SELECT issue, schema_name, table_name, column_name "
                                               "FROM datadict.v_coverage_gaps WHERE schema_name = 'hparams'"):
                    out.append(f"datadict: {row[0]} {row[1]}.{row[2]}.{row[3]}")
                n = await _fetch(store, """
                        SELECT count(DISTINCT c.config_sha), count(DISTINCT rc.run_id)
                        FROM hparams.configs c LEFT JOIN hparams.run_configs rc USING (config_sha)""")
                print(f"database: {n[0][0]} configs, {n[0][1]} linked runs", flush=True)
            return out
        problems += asyncio.run(_db())

    for p in problems:
        print(f"  ✗ {p}", flush=True)
    print("OK" if not problems else f"{len(problems)} problem(s)", flush=True)
    return 1 if problems else 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="python -m equity_mcp.hparams", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("snapshot", help="build the current config and print it; no database")
    s.add_argument("--out", help="also write the snapshot record as JSON")
    s.set_defaults(fn=cmd_snapshot)

    s = sub.add_parser("sync", help="store snapshots and run links")
    what = s.add_mutually_exclusive_group(required=True)
    what.add_argument("--current", action="store_true", help="store today's config")
    what.add_argument("--from-run-dir", nargs="+", metavar="DIR", help="ingest runs/<id>/config.json files")
    what.add_argument("--backfill", action="store_true", help="reconstruct configs for runs without one")
    what.add_argument("--flush-pending", action="store_true", help="replay evals/pending*/ into Supabase")
    s.add_argument("--file", nargs="+", help="with --backfill: only these outputs/*.json")
    s.add_argument("--label", help="with --current: a name for the config")
    s.add_argument("--dry-run", action="store_true", help="plan and print only; store nothing")
    s.set_defaults(fn=cmd_sync)

    s = sub.add_parser("verify", help="check snapshot consistency")
    s.add_argument("--db", action="store_true", help="also check what is stored in Supabase")
    s.set_defaults(fn=cmd_verify)

    args = p.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
