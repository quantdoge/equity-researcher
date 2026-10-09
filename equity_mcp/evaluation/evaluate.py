"""
Score research outputs against the metrics/<role>.yaml rubrics with TypeSafe Jev.

    python -m equity_mcp.evaluation.evaluate --file outputs/AVGO_20261003T135110.json
    python -m equity_mcp.evaluation.evaluate --all --dry-run
    python -m equity_mcp.evaluation.evaluate --symbol NOW --latest --roles value head
    python -m equity_mcp.evaluation.evaluate --validate-rubrics

For each agent in a run it:
1. Parses the report and runs the deterministic checks.
2. Asks Jev the shared stance, conviction and domain questions (block
   ``conviction``) and the prompt-adherence questions (block ``alignment``).
3. Stores everything in Supabase (``SUPABASE_EVAL_DB_URL``), or locally in
   evals/results/ when no database is configured or ``--no-store`` is given.

Specialists go first. The portfolio strategist and head of research go second,
because their fidelity questions need to know what the specialists concluded.

The run is idempotent: an evaluation already stored for the same run, role,
rubric hash and Jev model is skipped unless ``--force``, and every successful
Jev call is cached by state + questions + model.

Exit codes:
- 0: everything evaluated, or skipped with a reason.
- 1: configuration error (rubric invalid, API key rejected, no files).
- 2: finished with partial errors, or results went to the pending fallback.
"""

from __future__ import annotations

import argparse
import asyncio
import glob
import hashlib
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

from equity_mcp.evaluation import aggregate as agg
from equity_mcp.evaluation import crossagent
from equity_mcp.evaluation.checks import domain_coverage, run_check, run_extracts
from equity_mcp.evaluation.extract import PASS2_ROLES, records_from_result, role_label, run_from_result, section_text
from equity_mcp.evaluation.jev import DEFAULT_MODEL, FatalJevError, JevRunner, build_state, validate_answer, wire_question
from equity_mcp.evaluation.loader import REPO_ROOT, LoadedRubric, RubricError, load_all, prompt_sha256, validate_all
from equity_mcp.evaluation.schema import MAX_QUESTIONS_PER_REQUEST, ChoiceQ
from equity_mcp.evaluation.stance import conviction_label, native_stance
from equity_mcp.evaluation.store import flush_pending, make_store
from equity_mcp.roles import AGENT_MODELS, ALL_ROLES
from equity_mcp.roles import DEFAULT_MODEL as AGENT_DEFAULT_MODEL

load_dotenv()

EVALUATOR_VERSION = "1"
BLOCKS = ("conviction", "alignment")
_STAMP = re.compile(r"_(\d{8}T\d{6})$")


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _git_sha() -> str | None:
    if os.getenv("GITHUB_SHA"):
        return os.environ["GITHUB_SHA"]
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, capture_output=True,
                              text=True, timeout=5).stdout.strip() or None
    except Exception:
        return None


def resolve_model(model: str | None, allow_floating: bool = False) -> str:
    chosen = (model or os.getenv("JEV_MODEL") or DEFAULT_MODEL).strip()
    if chosen.endswith("latest") and not allow_floating:
        raise SystemExit(
            f"Refusing floating model alias '{chosen}': results would not be comparable across runs. "
            "Pin a version (e.g. jev-1.13.0) or pass --allow-floating-model."
        )
    return chosen


# ── Planning ──────────────────────────────────────────────────────────────────


def _texts(record: dict, sids: list[str], loaded: LoadedRubric) -> list[str]:
    out = []
    for sid in sids:
        sec = section_text(record, sid, loaded.rubric.sections)
        if sec and sec["text"].strip():
            out.append(sec["text"])
    return out


def plan_role(
    loaded: LoadedRubric,
    record: dict,
    run: dict,
    extracts: dict[str, dict],
    *,
    blocks: tuple[str, ...],
    order_check: bool,
    summary: dict | None,
    ctx: dict,
) -> tuple[list[dict], list[dict]]:
    """``(requests, rows)``: Jev requests to send, and rows already decided in code."""
    rb, shared = loaded.rubric, loaded.shared
    label = role_label(loaded.role)
    requests: list[dict] = []
    rows: list[dict] = []

    def add(block: str, rid: str, texts: list[str], qobjs: dict, *, gate: str | None = None,
            variant: str = "primary", required_output: bool = False, with_summary: bool = False) -> None:
        state, truncated = build_state(
            role_label=label, mandate=rb.background.mandate,
            required_output=rb.background.required_output if required_output else None,
            run=run, texts=texts, specialist_summary=summary if with_summary else None,
        )
        wire = {qid: wire_question(q, reversed_options=(variant == "reversed")) for qid, q in qobjs.items()}
        requests.append({"block": block, "rubric_request": rid, "state": state, "truncated": truncated,
                         "questions": wire, "qobjs": qobjs, "gate": gate, "variant": variant})

    if "conviction" in blocks:
        sc = shared.conviction
        texts = _texts(record, sc.state, loaded)
        qobjs = {"stance_gate": sc.stance_gate, "stance": sc.stance, "conviction_level": sc.conviction_level}
        add("conviction", "stance", texts, qobjs, gate="stance_gate")
        if order_check:
            add("conviction", "stance", texts, {"stance": sc.stance}, variant="reversed")

        # Pack addressed metrics ≤6 per request. Each request's state is only the
        # sections its metrics drew evidence from, so packing saves calls without
        # sending the whole report. "full" swallows the rest, so it stands alone.
        addressed: list[tuple[str, Any, str]] = []
        for mid, metric in rb.conviction.domain_metrics.items():
            cov = domain_coverage(metric, record, rb.sections)
            if not cov["addressed"]:
                rows.append(agg.domain_row(mid, metric.label, None, status="not_addressed",
                                           detail=f"no evidence terms in {cov['section'] or 'any listed section'}"))
                continue
            addressed.append((mid, metric, cov["section"]))
        addressed.sort(key=lambda t: t[2] == "full")
        for i in range(0, len(addressed), MAX_QUESTIONS_PER_REQUEST):
            chunk = addressed[i: i + MAX_QUESTIONS_PER_REQUEST]
            sids = list(dict.fromkeys(sid for _, _, sid in chunk))
            if "full" in sids:
                sids = ["full"]
            add("domain", "domain:" + "+".join(sids), _texts(record, sids, loaded),
                {mid: metric for mid, metric, _ in chunk})

    if "alignment" in blocks:
        for chk in loaded.alignment.deterministic_checks:
            rows.append(agg.check_row(chk, run_check(chk, record, rb.sections, extracts, ctx)))
        for req in loaded.alignment.requests:
            texts = _texts(record, req.state, loaded)
            with_summary = "crossagent" in req.context
            if not texts:
                for qid, q in req.questions.items():
                    rows.append(agg.metric_row(question_id=qid, block="alignment", kind=q.type,
                                               rubric_request=req.id, dimension=q.dimension, weight=q.weight,
                                               veto=q.veto, status="skipped",
                                               detail=f"sections {req.state} not found"))
                continue
            add("alignment", req.id, texts, dict(req.questions), gate=req.gate,
                required_output=True, with_summary=with_summary)
            if order_check:
                rev = {qid: q for qid, q in req.questions.items() if isinstance(q, ChoiceQ) and q.order_check}
                if rev:
                    add("alignment", req.id, texts, rev, variant="reversed",
                        required_output=True, with_summary=with_summary)
    return requests, rows


# ── Execution ─────────────────────────────────────────────────────────────────


def _rows_from_call(req: dict, call: dict, extracts: dict, ref: int | None) -> list[dict]:
    rows = []
    answers = call.get("answers") or {}
    for qid, q in req["qobjs"].items():
        wire = req["questions"][qid]
        if req["block"] == "domain":
            err = call.get("error") or validate_answer(wire, answers.get(qid))
            row = agg.domain_row(qid, q.label, None if err else answers[qid], status="error" if err else "ok")
            row["error"] = err
        else:
            common = dict(question_id=qid, block=req["block"], kind=q.type, rubric_request=req["rubric_request"],
                          dimension=q.dimension, weight=q.weight, veto=q.veto, variant=req["variant"])
            err = call.get("error") or validate_answer(wire, answers.get(qid))
            if err:
                row = agg.metric_row(**common, status="error", error=err)
            else:
                row = agg.answer_row(qid, q, answers[qid], block=req["block"],
                                     rubric_request=req["rubric_request"], variant=req["variant"],
                                     extracts=extracts)
        row["call_ref"] = ref
        rows.append(row)
    return rows


def _agent_model(run: dict, role: str) -> tuple[str, bool]:
    recorded = (run.get("agent_models") or {}).get(role)
    if recorded:
        return recorded, False
    return AGENT_MODELS.get(role, AGENT_DEFAULT_MODEL), True


def _jsonable_extracts(extracts: dict[str, dict]) -> dict:
    return {k: {"value": v["value"], "hedged": v["hedged"]} for k, v in extracts.items()}


async def evaluate_role(
    role: str,
    loaded: LoadedRubric,
    record: dict,
    run: dict,
    extracts: dict[str, dict],
    *,
    runner: JevRunner,
    store: Any,
    model: str,
    blocks: tuple[str, ...],
    order_check: bool,
    force: bool,
    dry_run: bool,
    summary: dict | None,
    ctx: dict,
) -> dict:
    """Evaluate one agent's report. Returns a short result dict for printing and exit codes."""
    if not dry_run and not force and await store.already_evaluated(run["run_id"], role, loaded.sha, model):
        return {"role": role, "status": "already_evaluated"}

    started = _now()
    agent_model, inferred = _agent_model(run, role)
    report = record.get("report")
    output_row = {
        "run_id": run["run_id"], "role": role, "status": record["status"], "error": record["error"],
        "output_text": record["raw"], "output_sha256": record["output_sha256"], "chars": len(record["raw"]),
        "preamble_chars": len(record["preamble"]), "section_names": report.heading_names if report else [],
        "agent_model": agent_model, "agent_model_inferred": inferred,
        "elapsed_seconds": record["elapsed_seconds"], "extracts": _jsonable_extracts(extracts),
    }
    rubric_row = {
        "rubric_sha": loaded.sha, "role": role, "rubric_version": loaded.rubric.rubric_version,
        "shared_version": loaded.shared.shared_version, "source_prompt_sha256": loaded.rubric.source_prompt_sha256,
        "calibrated": loaded.rubric.calibrated, "content": loaded.content,
    }
    evaluation: dict[str, Any] = {
        "run_id": run["run_id"], "role": role, "rubric_sha": loaded.sha, "jev_model": model,
        "evaluator_version": EVALUATOR_VERSION, "pass": loaded.pass_, "advisory": not loaded.rubric.calibrated,
        "started_at": started,
    }

    if record["status"] != "ok":
        evaluation.update(status="agent_failed" if record["status"] == "failed" else record["status"],
                          n_metrics=0, n_errors=0, n_calls=0, n_cached=0, finished_at=_now(),
                          vetoes=[], veto_triggered=False, insufficient_evidence=False)
        if not dry_run:
            await store.save({"run": run, "agent_output": output_row, "rubric": rubric_row,
                              "evaluation": evaluation, "calls": [], "metrics": []})
        return {"role": role, "status": evaluation["status"], "calls": 0}

    requests, rows = plan_role(loaded, record, run, extracts, blocks=blocks, order_check=order_check,
                               summary=summary, ctx=ctx)

    if dry_run:
        chars = sum(len(str(r["state"])) for r in requests)
        return {"role": role, "status": "dry_run", "requests": len(requests),
                "questions": sum(len(r["questions"]) for r in requests), "state_chars": chars,
                "domain_not_addressed": sum(1 for r in rows if r["status"] == "not_addressed")}

    results = await asyncio.gather(*(runner.call(r["state"], r["questions"], r["truncated"]) for r in requests))
    calls = []
    gates_failed = 0
    for ref, (req, call) in enumerate(zip(requests, results)):
        calls.append({**call, "ref": ref})
        req_rows = _rows_from_call(req, call, extracts, ref)
        if req["variant"] == "primary" and req["block"] == "alignment" and agg.apply_gate(req_rows, req["gate"]):
            gates_failed += 1
        if req["block"] == "conviction" and req["variant"] == "primary":
            agg.apply_gate([r for r in req_rows if r["question_id"] != "conviction_level"], req["gate"])
        rows.extend(req_rows)

    conv = loaded.rubric.conviction
    native = native_stance(conv, extracts)
    native_conv = None
    if conv.native_conviction:
        v = extracts.get(conv.native_conviction, {}).get("value")
        native_conv = str(v) if v is not None else None
    s = agg.summarise(rows, native=native, gates_failed=gates_failed, native_conviction=native_conv)
    evaluation.update(s)
    evaluation.update(
        n_calls=len(calls), n_cached=sum(1 for c in calls if c.get("cached")),
        input_tokens=sum(c.get("input_tokens") or 0 for c in calls if not c.get("cached")),
        output_tokens=sum(c.get("output_tokens") or 0 for c in calls if not c.get("cached")),
        finished_at=_now(),
    )
    where = await store.save({"run": run, "agent_output": output_row, "rubric": rubric_row,
                              "evaluation": evaluation, "calls": calls, "metrics": rows})
    return {"role": role, "status": evaluation["status"], "evaluation": evaluation, "calls": len(calls),
            "cached": evaluation["n_cached"], "stored": where}


async def evaluate_result(
    result: dict,
    source_path: Path | None = None,
    *,
    roles: list[str] | None = None,
    model: str | None = None,
    blocks: tuple[str, ...] = BLOCKS,
    force: bool = False,
    dry_run: bool = False,
    order_check: bool = False,
    concurrency: int = 4,
    no_store: bool = False,
    quiet: bool = False,
    store: Any = None,
    runner: JevRunner | None = None,
) -> dict:
    """
    Evaluate one research result dict, as written to outputs/*.json.

    Library entry point, used by the CLI and by ``orchestrator --evaluate``.
    It raises only for configuration problems (``RubricError``,
    ``FatalJevError``). Per-metric failures are recorded and reported in the
    returned summary.
    """
    model = resolve_model(model, allow_floating=True) if model else resolve_model(None)
    run = run_from_result(result, source_path)
    if source_path is not None and source_path.exists():
        run["source_sha256"] = hashlib.sha256(source_path.read_bytes()).hexdigest()
    run["git_sha"] = _git_sha()

    out: dict[str, Any] = {"run_id": run["run_id"], "roles": [], "skipped": None}
    own_store = store is None
    store = store or make_store(no_store or dry_run)

    if run["schema_kind"] != "agent_results_v1":
        out["skipped"] = run["skip_reason"]
        if not dry_run:
            async with store:
                await store.save({"run": run, "agent_output": None})
        return out

    records = records_from_result(result)
    rubrics = load_all()
    extracts = {
        role: run_extracts(rec, rubrics[role].rubric.extract, rubrics[role].rubric.sections)
        if rec["status"] == "ok" else {}
        for role, rec in records.items() if role in rubrics
    }
    targets = [r for r in ALL_ROLES if r in records and (roles is None or r in roles)]

    own_runner = runner is None
    runner = runner or JevRunner(model=model, concurrency=concurrency, dry_run=dry_run,
                                 store=None if dry_run else store)

    async def _go() -> None:
        common = dict(runner=runner, store=store, model=model, blocks=blocks, order_check=order_check,
                      force=force, dry_run=dry_run)
        pass1 = [r for r in targets if r not in PASS2_ROLES]
        base_ctx = {"failed_roles": run["failures"], "short_earnings_quality": None}
        res1 = await asyncio.gather(*(
            evaluate_role(r, rubrics[r], records[r], run, extracts.get(r, {}), summary=None, ctx=base_ctx, **common)
            for r in pass1
        ))
        out["roles"].extend(res1)

        info: dict[str, dict] = {}
        by_role = {r["role"]: r for r in res1}
        for role, rec in records.items():
            if role not in rubrics:
                continue
            ev = by_role.get(role, {}).get("evaluation") or {}
            native = native_stance(rubrics[role].rubric.conviction, extracts.get(role, {}))
            info[role] = {"extracts": extracts.get(role, {}), "native_rating": native[0],
                          "stance": ev.get("stance") or native[1],
                          "conviction_level": ev.get("conviction_level")}
        for role in [r for r in PASS2_ROLES if r in targets]:  # strategist, then memo
            summary, ctx = crossagent.build(run, records, info, role)
            res = await evaluate_role(role, rubrics[role], records[role], run, extracts.get(role, {}),
                                      summary=summary, ctx=ctx, **common)
            out["roles"].append(res)

    if own_runner and own_store:
        async with store, runner:
            await _go()
    elif own_runner:
        async with runner:
            await _go()
    elif own_store:
        async with store:
            await _go()
    else:
        await _go()

    out["fallbacks"] = getattr(store, "fallbacks", 0)
    if not quiet:
        print_summary(out)
    return out


# ── Reporting ─────────────────────────────────────────────────────────────────


def _fmt(x: Any, spec: str = ".2f") -> str:
    return "-" if x is None else format(x, spec)


def print_summary(out: dict) -> None:
    print(f"\n[eval] {out['run_id']}", flush=True)
    if out.get("skipped"):
        print(f"  skipped: {out['skipped']}", flush=True)
        return
    for r in out["roles"]:
        role, status = r["role"], r["status"]
        if status == "dry_run":
            print(f"  {role:<22} dry-run  requests={r['requests']:<3} questions={r['questions']:<3} "
                  f"state≈{r['state_chars'] // 1000}k chars (~{r['state_chars'] // 4 // 1000}k tokens)  "
                  f"domain not addressed={r['domain_not_addressed']}", flush=True)
            continue
        ev = r.get("evaluation")
        if not ev:
            print(f"  {role:<22} {status}", flush=True)
            continue
        stance = f"{ev['stance'] or '-'} ({_fmt(ev['stance_confidence'])})"
        if ev.get("stance_low_evidence"):
            stance += "*"
        dom = f"{_fmt(ev['domain_mean'], '.1f')} ({ev['domain_addressed']}/{ev['domain_total']})"
        vetoes = ",".join(ev["vetoes"]) or "-"
        print(f"  {role:<22} {status:<8} stance={stance:<18} conv={ev['conviction_level'] or '-':<6} "
              f"native={ev['native_rating'] or '-':<12} domain={dom:<10} align={_fmt(ev['alignment_composite'])} "
              f"vetoes={vetoes}  calls={r['calls']} ({r.get('cached', 0)} cached) → {r.get('stored')}", flush=True)


def exit_code(outs: list[dict]) -> int:
    for out in outs:
        if out.get("fallbacks"):
            return 2
        for r in out.get("roles", []):
            ev = r.get("evaluation") or {}
            if r["status"] == "partial" or ev.get("n_errors"):
                return 2
    return 0


# ── CLI ───────────────────────────────────────────────────────────────────────


def _stamp_of(path: Path) -> str:
    m = _STAMP.search(path.stem)
    return m.group(1) if m else ""


def select_files(args: argparse.Namespace) -> list[Path]:
    outputs = REPO_ROOT / "outputs"
    if args.file:
        files = [Path(p) for pat in args.file for p in (glob.glob(pat) or [pat])]
    elif args.symbol:
        files = sorted(outputs.glob(f"{args.symbol.upper()}_*.json"), key=_stamp_of)
        if args.latest and files:
            files = [files[-1]]
    else:
        files = sorted(outputs.glob("*.json"))
    if args.since:
        since = args.since.replace("-", "")
        files = [f for f in files if (_stamp_of(f) or "99999999")[:8] >= since]
    if args.require_newer_than:
        files = [f for f in files if _stamp_of(f) > args.require_newer_than]
    return files


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="python -m equity_mcp.evaluation.evaluate", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sel = p.add_mutually_exclusive_group()
    sel.add_argument("--file", nargs="+", help="output JSON files or globs")
    sel.add_argument("--all", action="store_true", help="every outputs/*.json")
    sel.add_argument("--symbol", help="outputs for one ticker")
    p.add_argument("--latest", action="store_true", help="with --symbol: only the newest run")
    p.add_argument("--since", help="only runs on or after YYYY-MM-DD")
    p.add_argument("--require-newer-than", metavar="STAMP", help="only runs stamped after YYYYmmddTHHMMSS")
    p.add_argument("--roles", nargs="+", help="agent names or unambiguous prefixes")
    p.add_argument("--model", help=f"Jev model (default $JEV_MODEL or {DEFAULT_MODEL})")
    p.add_argument("--allow-floating-model", action="store_true")
    p.add_argument("--blocks", nargs="+", choices=BLOCKS, default=list(BLOCKS))
    p.add_argument("--concurrency", type=int, default=4, help="Jev requests in flight")
    p.add_argument("--force", action="store_true", help="re-evaluate even if already stored")
    p.add_argument("--dry-run", action="store_true", help="plan only: no network, no storage")
    p.add_argument("--order-check", action="store_true", help="also ask reversed-option variants of choices")
    p.add_argument("--no-store", action="store_true", help="write results to evals/results/ instead of Supabase")
    p.add_argument("--flush-pending", action="store_true", help="replay evals/pending/ into Supabase and exit")
    p.add_argument("--validate-rubrics", action="store_true", help="validate metrics/*.yaml and exit")
    p.add_argument("--rehash-prompts", action="store_true", help="print each prompt's sha256 and exit")
    p.add_argument("--list-models", action="store_true", help="list Jev models available to the key and exit")
    args = p.parse_args(argv)

    if args.validate_rubrics:
        problems = validate_all()
        for prob in problems:
            print(f"  ✗ {prob}", flush=True)
        print(f"{'OK' if not problems else 'INVALID'}: {len(ALL_ROLES)} rubrics + _shared.yaml", flush=True)
        return 1 if problems else 0
    if args.rehash_prompts:
        for role in ALL_ROLES:
            print(f"{role:<24} source_prompt_sha256: \"{prompt_sha256(role)}\"")
        return 0
    if args.flush_pending:
        saved, failed = asyncio.run(flush_pending())
        print(f"flushed {saved} pending records ({failed} still pending)", flush=True)
        return 2 if failed else 0
    if args.list_models:
        async def _models() -> list[str]:
            async with JevRunner(model=resolve_model(args.model, True)) as r:
                return await r.list_models()
        try:
            print("\n".join(asyncio.run(_models())))
        except FatalJevError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 1
        return 0

    if not (args.file or args.all or args.symbol):
        p.error("choose --file, --all or --symbol")
    model = resolve_model(args.model, args.allow_floating_model)
    roles = None
    if args.roles:
        from equity_mcp.orchestrator import _resolve_roles
        roles = _resolve_roles(args.roles, ALL_ROLES)
    try:
        problems = validate_all()
    except RubricError as exc:
        problems = [str(exc)]
    if problems:
        for prob in problems:
            print(f"  ✗ {prob}", file=sys.stderr)
        print("Rubrics invalid: fix them or run --validate-rubrics.", file=sys.stderr)
        return 1

    files = select_files(args)
    if not files:
        print("[eval] no matching output files: nothing to evaluate", flush=True)
        return 0
    print(f"[eval] {len(files)} file(s), model {model}, blocks {' '.join(args.blocks)}"
          f"{', DRY RUN' if args.dry_run else ''}", flush=True)

    async def _run_all() -> list[dict]:
        import json

        store = make_store(args.no_store or args.dry_run)
        runner = JevRunner(model=model, concurrency=args.concurrency, dry_run=args.dry_run,
                           store=None if (args.dry_run or args.no_store) else store)
        outs = []
        async with store, runner:
            for path in files:
                result = json.loads(path.read_text(encoding="utf-8"))
                outs.append(await evaluate_result(
                    result, path, roles=roles, model=model, blocks=tuple(args.blocks), force=args.force,
                    dry_run=args.dry_run, order_check=args.order_check, store=store, runner=runner,
                ))
            for out in outs:
                out["fallbacks"] = getattr(store, "fallbacks", 0)
        return outs

    try:
        outs = asyncio.run(_run_all())
    except FatalJevError as exc:
        print(f"[eval] fatal: {exc}", file=sys.stderr, flush=True)
        return 1
    except OSError as exc:  # database unreachable at connect
        print(f"[eval] fatal: could not connect to the evaluation database: {exc}", file=sys.stderr, flush=True)
        return 1

    if args.dry_run:
        n_req = sum(r.get("requests", 0) for o in outs for r in o["roles"])
        chars = sum(r.get("state_chars", 0) for o in outs for r in o["roles"])
        skipped = sum(1 for o in outs if o.get("skipped"))
        print(f"\n[eval] DRY RUN: {len(outs) - skipped} runs to evaluate, {skipped} skipped, "
              f"{n_req} Jev requests, ~{chars // 4:,} input tokens", flush=True)
    return exit_code(outs)


if __name__ == "__main__":
    sys.exit(main())
