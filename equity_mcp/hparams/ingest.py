"""
Store hyperparameter snapshots and run links in the `hparams` schema.

The SQL lives here, but it runs through ``evaluation.store.SupabaseStore``, so
it shares that store's connection, lock, reconnect-and-retry and pending
fallback. The store calls ``write`` inside one transaction per payload::

    {"snapshot": <Snapshot.to_record()> | None, "links": [<link_row>, ...]}

Order of writes:
- configs (upsert; see below), then, only when the config is new: texts,
  tool_defs, config_runtime, config_agents, config_tools and config_role_tools.
  Content-addressed rows use ON CONFLICT DO NOTHING.
- run_configs last. The eval.runs row it references is written by the
  evaluation itself, earlier.

A config's ``content`` never changes. Observing it again can widen
effective_at / last_seen_at, and can upgrade provenance (inferred <
reconstructed_from_git < captured_at_runtime), along with the git fields, gaps
and libs that came with the better observation. A run link is replaced only by
one whose link_basis ranks at least as high, so a later backfill guess can never
overwrite a link the run recorded itself.

Evaluation must not fail because of any of this. ``ingest_run`` swallows every
error into a warning, and the store parks the payload in
evals/pending_hparams/ when the database is down.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Callable

from equity_mcp.hparams.snapshot import Snapshot

REPO_ROOT = Path(__file__).resolve().parents[2]
RUNS_DIR = REPO_ROOT / "runs"

LINK_BASES = ("inferred", "git_checkout", "prompt_sha_match", "recorded_in_run")  # ascending rank

CONFIG_COLS = ("config_sha", "snapshot_version", "provenance", "effective_at", "last_seen_at", "source_git_sha",
               "source_git_dirty", "gaps", "libs", "content", "label", "notes")
RUNTIME_COLS = ("config_sha", "tool_timeout_s", "max_tool_threads", "specialist_max_tokens", "memo_max_tokens",
                "specialist_recursion_limit", "master_recursion_limit", "agent_timeout_s", "default_max_concurrency",
                "advertised_fraction", "request_timeout_ms", "streaming", "provider_routing", "default_model",
                "agent_model_overrides", "budget_template_sha", "extra")
AGENT_COLS = ("config_sha", "role", "stage", "agent_kind", "model_slug", "model_spec", "max_tokens",
              "recursion_limit", "advertised_recursion_limit", "advertised_tool_rounds", "advertised_write_by",
              "advertised_timeout_s", "task", "prompt_source", "system_prompt_sha", "budget_sha",
              "composed_prompt_sha", "tool_count", "agent_sha")
TOOL_DEF_COLS = ("tool_sha", "tool_name", "module", "description", "input_schema", "impl_sha256")
TOOL_COLS = ("config_sha", "tool_name", "tool_sha", "tags")
ROLE_TOOL_COLS = ("config_sha", "role", "tool_name", "via")
LINK_COLS = ("run_id", "config_sha", "link_basis", "research_git_sha", "max_concurrency", "run_timeout_s",
             "agents_requested", "extra_instructions", "overrides", "notes")

# Columns store._adapt must wrap as jsonb.
JSONB_COLS = {"libs", "content", "provider_routing", "agent_model_overrides", "extra", "input_schema", "overrides"}

_CONFIG_UPSERT = f"""
INSERT INTO hparams.configs AS c ({', '.join(CONFIG_COLS)}) VALUES ({', '.join(['%s'] * len(CONFIG_COLS))})
ON CONFLICT (config_sha) DO UPDATE SET
    effective_at = LEAST(c.effective_at, EXCLUDED.effective_at),
    last_seen_at = GREATEST(c.last_seen_at, EXCLUDED.last_seen_at),
    provenance   = CASE WHEN {{better}} THEN EXCLUDED.provenance       ELSE c.provenance END,
    source_git_sha   = CASE WHEN {{better}} THEN EXCLUDED.source_git_sha   ELSE c.source_git_sha END,
    source_git_dirty = CASE WHEN {{better}} THEN EXCLUDED.source_git_dirty ELSE c.source_git_dirty END,
    gaps         = CASE WHEN {{better}} THEN EXCLUDED.gaps ELSE c.gaps END,
    libs         = CASE WHEN {{better}} THEN COALESCE(EXCLUDED.libs, c.libs)
                        ELSE COALESCE(c.libs, EXCLUDED.libs) END,
    label        = COALESCE(c.label, EXCLUDED.label),
    notes        = COALESCE(c.notes, EXCLUDED.notes)
RETURNING (xmax = 0) AS inserted
""".replace(
    "{better}",
    "hparams.provenance_rank(EXCLUDED.provenance) > hparams.provenance_rank(c.provenance)",
)

_LINK_UPSERT = f"""
INSERT INTO hparams.run_configs AS rc ({', '.join(LINK_COLS)}) VALUES ({', '.join(['%s'] * len(LINK_COLS))})
ON CONFLICT (run_id) DO UPDATE SET {', '.join(f'{c} = EXCLUDED.{c}' for c in LINK_COLS if c != 'run_id')}
WHERE hparams.link_basis_rank(EXCLUDED.link_basis) >= hparams.link_basis_rank(rc.link_basis)
RETURNING run_id
"""


def _insert_many(cur, table: str, cols: tuple[str, ...], rows: list[dict], conflict: str,
                 adapt: Callable[[str, Any], Any]) -> None:
    if not rows:
        return
    cur.executemany(
        f"INSERT INTO {table} ({', '.join(cols)}) VALUES ({', '.join(['%s'] * len(cols))}) "
        f"ON CONFLICT {conflict} DO NOTHING",
        [[adapt(c, r.get(c)) for c in cols] for r in rows],
    )


def write(cur, payload: dict, adapt: Callable[[str, Any], Any]) -> dict:
    """Write one payload with *cur*, inside the caller's transaction. Returns what happened."""
    out = {"config": None, "config_new": False, "links": 0, "links_kept": 0}
    rec = payload.get("snapshot")
    if rec:
        snap = Snapshot.from_record(rec)
        problems = snap.problems()
        if problems:
            raise ValueError(f"refusing inconsistent snapshot {snap.sha[:12]}: {problems[:3]}")
        row = rec["config"]
        cur.execute(_CONFIG_UPSERT, [adapt(c, row.get(c)) for c in CONFIG_COLS])
        (new,) = cur.fetchone()
        out.update(config=snap.sha, config_new=bool(new))
        if new:
            sha = snap.sha
            _insert_many(cur, "hparams.texts", ("text_sha", "body"),
                         [{"text_sha": k, "body": v} for k, v in snap.texts.items()], "(text_sha)", adapt)
            _insert_many(cur, "hparams.tool_defs", TOOL_DEF_COLS, snap.tool_defs, "(tool_sha)", adapt)
            _insert_many(cur, "hparams.config_runtime", RUNTIME_COLS, [{**snap.runtime, "config_sha": sha}],
                         "(config_sha)", adapt)
            _insert_many(cur, "hparams.config_agents", AGENT_COLS, [{**a, "config_sha": sha} for a in snap.agents],
                         "(config_sha, role)", adapt)
            _insert_many(cur, "hparams.config_tools", TOOL_COLS, [{**t, "config_sha": sha} for t in snap.tools],
                         "(config_sha, tool_name)", adapt)
            _insert_many(cur, "hparams.config_role_tools", ROLE_TOOL_COLS,
                         [{**rt, "config_sha": sha} for rt in snap.role_tools], "(config_sha, role, tool_name)", adapt)
    for link in payload.get("links") or []:
        if link.get("link_basis") not in LINK_BASES:
            raise ValueError(f"bad link_basis {link.get('link_basis')!r} for {link.get('run_id')}")
        cur.execute(_LINK_UPSERT, [adapt(c, link.get(c)) for c in LINK_COLS])
        if cur.fetchone() is None:
            out["links_kept"] += 1  # a better-founded link was already stored
        else:
            out["links"] += 1
    return out


def link_row(run_id: str, config_sha: str, link_basis: str, run_params: dict | None, *,
             research_git_sha: str | None = None, overrides: dict | None = None, notes: str | None = None) -> dict:
    """A run_configs row from the run_params dict the orchestrator records (capture.py)."""
    p = run_params or {}
    extra = dict(overrides or {})
    if p.get("skip_synthesis") is not None:
        extra.setdefault("skip_synthesis", bool(p["skip_synthesis"]))
    return {
        "run_id": run_id, "config_sha": config_sha, "link_basis": link_basis, "research_git_sha": research_git_sha,
        "max_concurrency": p.get("max_concurrency"), "run_timeout_s": p.get("timeout_s"),
        "agents_requested": p.get("agents_requested"), "extra_instructions": p.get("focus"),
        "overrides": extra, "notes": notes,
    }


def load_run_config(run_id: str, runs_dir: Path = RUNS_DIR) -> dict | None:
    """The payload capture.py wrote for *run_id*, or None if there is none."""
    path = runs_dir / run_id / "config.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def payload_from_run_config(run_id: str, cfg: dict) -> dict:
    snap = cfg["snapshot"]
    link = link_row(run_id, cfg["config_sha"], "recorded_in_run", cfg.get("run_params"),
                    research_git_sha=snap["config"].get("source_git_sha"))
    return {"snapshot": snap, "links": [link]}


async def ingest_run(store: Any, result: dict, runs_dir: Path = RUNS_DIR) -> str | None:
    """
    Link one evaluated run to the config it captured. Never raises.

    It does nothing when the run captured no config.json. Older runs are linked
    by the explicit backfill, which is the only path allowed to guess.
    """
    try:
        run_id = result.get("run_id")
        if not run_id or not hasattr(store, "save_hparams"):
            return None
        cfg = load_run_config(run_id, runs_dir)
        if cfg is None:
            return None
        return await store.save_hparams(payload_from_run_config(run_id, cfg))
    except Exception as exc:  # noqa: BLE001 - evaluation must never fail because of hparams
        print(f"[hparams] warning: could not link {result.get('run_id')}: {type(exc).__name__}: {exc}",
              file=sys.stderr, flush=True)
        return None
