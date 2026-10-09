"""
Persist evaluations to the `eval` schema of the evaluation Supabase project.

Connection: ``SUPABASE_EVAL_DB_URL``, a *session pooler* URL
(``postgresql://eval_writer.<ref>:<pw>@aws-0-<region>.pooler.supabase.com:5432/postgres``).
Supabase direct hosts are IPv6-only and GitHub runners have no IPv6. Prepared
statements are switched off with ``prepare_threshold=None``, because psycopg
auto-prepares after five executions and the transaction pooler cannot hold a
prepared statement across transactions. Doing it unconditionally means
pointing the URL at either pooler mode just works.

Writes are idempotent:
- Each (run, role) evaluation goes in one transaction.
- Upserts use the natural keys.
- A re-evaluation replaces its metric rows wholesale.

A failed Jev call is logged but never becomes a cache entry; the partial
unique index on ``jev_calls`` is ``WHERE error IS NULL``.

When the database is unreachable, records go to ``evals/pending/<run_id>.jsonl``
instead of being lost, and ``--flush-pending`` replays them. Like RunLog,
evaluation must not take down the run it is attached to.
"""

from __future__ import annotations

import asyncio
import json
import os
import sys
from pathlib import Path
from typing import Any

from equity_mcp.evaluation.loader import REPO_ROOT

PENDING_DIR = REPO_ROOT / "evals" / "pending"
RESULTS_DIR = REPO_ROOT / "evals" / "results"

_RUN_COLS = ("run_id", "symbol", "run_date", "source_path", "source_sha256", "schema_kind",
             "skipped_synthesis", "failures", "elapsed_seconds", "git_sha", "skip_reason")
_OUTPUT_COLS = ("run_id", "role", "status", "error", "output_text", "output_sha256", "chars", "preamble_chars",
                "section_names", "agent_model", "agent_model_inferred", "elapsed_seconds", "extracts")
_RUBRIC_COLS = ("rubric_sha", "role", "rubric_version", "shared_version", "source_prompt_sha256", "calibrated",
                "content")
_CALL_COLS = ("cache_key", "state_sha256", "questions_sha256", "jev_model_requested", "jev_model_returned",
              "request_id", "http_status", "latency_ms", "input_tokens", "output_tokens", "state_chars",
              "state_truncated", "answers", "error")
_EVAL_COLS = ("run_id", "role", "agent_output_id", "rubric_sha", "jev_model", "evaluator_version", "pass",
              "status", "stance", "stance_probabilities", "stance_expected", "stance_confidence",
              "stance_low_evidence", "conviction_level", "conviction_score", "native_rating", "native_stance",
              "stance_agreement", "domain_profile", "domain_mean", "domain_addressed", "domain_total",
              "alignment_composite", "alignment_dimensions", "alignment_coverage", "veto_triggered", "vetoes",
              "insufficient_evidence", "advisory", "n_metrics", "n_errors", "n_calls", "n_cached",
              "input_tokens", "output_tokens", "started_at", "finished_at")
_METRIC_COLS = ("evaluation_id", "question_id", "block", "variant", "kind", "rubric_request", "dimension", "label",
                "weight", "veto", "noul_p", "choice", "score", "n_levels", "probabilities", "confidence",
                "deterministic_value", "detail", "code_extract", "agreement", "normalized", "passed", "status",
                "error", "jev_call_id")
_JSONB = {"extracts", "content", "answers", "stance_probabilities", "domain_profile", "alignment_dimensions",
          "probabilities"}


def _jsonable(record: dict) -> str:
    return json.dumps(record, default=str, ensure_ascii=False)


class LocalStore:
    """No database: writes each record to evals/results/<run_id>.json for inspection."""

    kind = "local"

    async def __aenter__(self) -> LocalStore:
        return self

    async def __aexit__(self, *exc: Any) -> None:
        return None

    async def already_evaluated(self, run_id: str, role: str, rubric_sha: str, model: str) -> bool:
        return False

    async def cached_call(self, cache_key: str) -> dict | None:
        return None

    async def save(self, record: dict) -> str:
        try:
            RESULTS_DIR.mkdir(parents=True, exist_ok=True)
            path = RESULTS_DIR / f"{record['run']['run_id']}.json"
            existing = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
            existing[record["evaluation"]["role"]] = record
            path.write_text(json.dumps(existing, default=str, ensure_ascii=False, indent=1), encoding="utf-8")
            return "local"
        except OSError as exc:
            print(f"[eval] warning: could not write local result: {exc}", file=sys.stderr, flush=True)
            return "dropped"


def write_pending(record: dict) -> None:
    try:
        PENDING_DIR.mkdir(parents=True, exist_ok=True)
        with (PENDING_DIR / f"{record['run']['run_id']}.jsonl").open("a", encoding="utf-8") as fh:
            fh.write(_jsonable(record) + "\n")
    except OSError as exc:
        print(f"[eval] warning: could not write pending record: {exc}", file=sys.stderr, flush=True)


class SupabaseStore:
    """psycopg async writer for the eval schema. Falls back to pending JSONL on DB errors."""

    kind = "supabase"

    def __init__(self, url: str) -> None:
        self.url = url
        self.conn = None
        self.fallbacks = 0
        self._lock = asyncio.Lock()

    async def __aenter__(self) -> SupabaseStore:
        import psycopg

        try:
            self.conn = await psycopg.AsyncConnection.connect(
                self.url, prepare_threshold=None, autocommit=False, connect_timeout=20
            )
        except Exception as exc:
            # Unreachable database: keep evaluating, park every record in evals/pending/.
            print(f"[eval] warning: evaluation database unreachable ({type(exc).__name__}: {exc}); "
                  f"results go to {PENDING_DIR} — replay with --flush-pending", file=sys.stderr, flush=True)
            self.conn = None
        return self

    async def __aexit__(self, *exc: Any) -> None:
        if self.conn is not None:
            await self.conn.close()

    def _adapt(self, col: str, value: Any) -> Any:
        if col in _JSONB and value is not None:
            from psycopg.types.json import Jsonb

            return Jsonb(value)
        return value

    async def already_evaluated(self, run_id: str, role: str, rubric_sha: str, model: str) -> bool:
        if self.conn is None:
            return False
        async with self._lock:
            try:
                async with self.conn.cursor() as cur:
                    await cur.execute(
                        "SELECT 1 FROM eval.evaluations WHERE run_id=%s AND role=%s AND rubric_sha=%s "
                        "AND jev_model=%s AND status IN ('complete','agent_failed','degenerate','missing')",
                        (run_id, role, rubric_sha, model),
                    )
                    row = await cur.fetchone()
                await self.conn.rollback()
                return row is not None
            except Exception as exc:
                await self._reset(exc)
                return False

    async def cached_call(self, cache_key: str) -> dict | None:
        if self.conn is None:
            return None
        async with self._lock:
            try:
                async with self.conn.cursor() as cur:
                    await cur.execute(
                        "SELECT id, answers, jev_model_returned, request_id, input_tokens, output_tokens "
                        "FROM eval.jev_calls WHERE cache_key=%s AND error IS NULL",
                        (cache_key,),
                    )
                    row = await cur.fetchone()
                await self.conn.rollback()
            except Exception as exc:
                await self._reset(exc)
                return None
        if row is None:
            return None
        return {"store_id": row[0], "answers": row[1], "jev_model_returned": row[2], "request_id": row[3],
                "input_tokens": row[4], "output_tokens": row[5], "error": None}

    async def _reset(self, exc: Exception) -> None:
        print(f"[eval] database error: {type(exc).__name__}: {exc}", file=sys.stderr, flush=True)
        try:
            await self.conn.rollback()
        except Exception:
            pass

    async def _upsert(self, cur, table: str, cols: tuple[str, ...], row: dict, conflict: str,
                      update: bool = True, returning: str | None = None):
        values = [self._adapt(c, row.get(c)) for c in cols]
        placeholders = ", ".join(["%s"] * len(cols))
        if update:
            sets = ", ".join(f"{c}=EXCLUDED.{c}" for c in cols)
            action = f"DO UPDATE SET {sets}"
        else:
            action = "DO NOTHING"
        sql = f"INSERT INTO {table} ({', '.join(cols)}) VALUES ({placeholders}) ON CONFLICT {conflict} {action}"
        if returning:
            sql += f" RETURNING {returning}"
        await cur.execute(sql, values)
        return await cur.fetchone() if returning else None

    async def save(self, record: dict) -> str:
        if self.conn is None:
            self.fallbacks += 1
            write_pending(record)
            return "pending"
        async with self._lock:
            try:
                await self._save(record)
                return "supabase"
            except Exception as exc:
                await self._reset(exc)
                self.fallbacks += 1
                write_pending(record)
                return "pending"

    async def _save(self, record: dict) -> None:
        async with self.conn.transaction():
            async with self.conn.cursor() as cur:
                run = record["run"]
                await self._upsert(cur, "eval.runs", _RUN_COLS, run, "(run_id)")
                if record.get("agent_output") is None:
                    return
                await cur.execute("UPDATE eval.runs SET updated_at = now() WHERE run_id=%s", (run["run_id"],))
                (output_id,) = await self._upsert(
                    cur, "eval.agent_outputs", _OUTPUT_COLS, record["agent_output"], "(run_id, role)",
                    returning="id",
                )
                await self._upsert(cur, "eval.rubrics", _RUBRIC_COLS, record["rubric"], "(rubric_sha)", update=False)

                call_ids: dict[int, int] = {}
                for call in record.get("calls", []):
                    if call.get("store_id"):
                        call_ids[call["ref"]] = call["store_id"]
                        continue
                    if call.get("error") is None:
                        (cid,) = await self._upsert(
                            cur, "eval.jev_calls", _CALL_COLS, call, "(cache_key) WHERE error IS NULL",
                            returning="id",
                        )
                    else:
                        cols = ", ".join(_CALL_COLS)
                        await cur.execute(
                            f"INSERT INTO eval.jev_calls ({cols}) VALUES ({', '.join(['%s'] * len(_CALL_COLS))}) "
                            "RETURNING id",
                            [self._adapt(c, call.get(c)) for c in _CALL_COLS],
                        )
                        (cid,) = await cur.fetchone()
                    call_ids[call["ref"]] = cid

                ev = {**record["evaluation"], "agent_output_id": output_id}
                (eval_id,) = await self._upsert(
                    cur, "eval.evaluations", _EVAL_COLS, ev, "(run_id, role, rubric_sha, jev_model)",
                    returning="id",
                )
                await cur.execute("DELETE FROM eval.metric_results WHERE evaluation_id=%s", (eval_id,))
                rows = []
                for m in record.get("metrics", []):
                    m = {**m, "evaluation_id": eval_id, "jev_call_id": call_ids.get(m.get("call_ref"))}
                    rows.append([self._adapt(c, m.get(c)) for c in _METRIC_COLS])
                if rows:
                    await cur.executemany(
                        f"INSERT INTO eval.metric_results ({', '.join(_METRIC_COLS)}) "
                        f"VALUES ({', '.join(['%s'] * len(_METRIC_COLS))})",
                        rows,
                    )


def make_store(no_store: bool) -> LocalStore | SupabaseStore:
    url = os.getenv("SUPABASE_EVAL_DB_URL", "").strip()
    if no_store or not url:
        return LocalStore()
    return SupabaseStore(url)


async def flush_pending() -> tuple[int, int]:
    """Replay evals/pending/*.jsonl into Supabase. Returns (saved, failed)."""
    url = os.getenv("SUPABASE_EVAL_DB_URL", "").strip()
    if not url:
        raise SystemExit("SUPABASE_EVAL_DB_URL is not set")
    saved = failed = 0
    files = sorted(PENDING_DIR.glob("*.jsonl")) if PENDING_DIR.exists() else []
    async with SupabaseStore(url) as store:
        for path in files:
            remaining = []
            for line in path.read_text(encoding="utf-8").splitlines():
                if not line.strip():
                    continue
                record = json.loads(line)
                try:
                    await store._save(record)
                    saved += 1
                except Exception as exc:
                    await store._reset(exc)
                    remaining.append(line)
                    failed += 1
            if remaining:
                path.write_text("\n".join(remaining) + "\n", encoding="utf-8")
            else:
                path.unlink()
    return saved, failed
