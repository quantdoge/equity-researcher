"""
Guards the Supabase writer against the real `eval` schema: upserts are idempotent.

Skipped unless SUPABASE_EVAL_DB_URL_TEST points at a database with the
migration applied (a Supabase branch or a scratch project, not production).
The rows it writes use a run_id prefixed TEST_ and are deleted afterwards, so
the URL must be an owner/admin login: eval_writer is deliberately not granted
DELETE on eval.runs.

Runs under pytest, or standalone:  python tests/test_eval_store.py
"""

from __future__ import annotations

import asyncio
import os

from _eval_fakes import CaptureStore, FakeRunner, load_output, run_tests

from equity_mcp.evaluation.evaluate import evaluate_result
from equity_mcp.evaluation.store import SupabaseStore

URL = os.getenv("SUPABASE_EVAL_DB_URL_TEST", "").strip()
RUN_ID = "TEST_AVGO_20261003T135110"


async def _counts(store: SupabaseStore) -> tuple[int, int]:
    async with store.conn.cursor() as cur:
        await cur.execute("SELECT count(*) FROM eval.evaluations WHERE run_id=%s", (RUN_ID,))
        (n_eval,) = await cur.fetchone()
        await cur.execute(
            "SELECT count(*) FROM eval.metric_results m JOIN eval.evaluations e ON e.id=m.evaluation_id "
            "WHERE e.run_id=%s", (RUN_ID,))
        (n_metrics,) = await cur.fetchone()
    await store.conn.rollback()
    return n_eval, n_metrics


def test_upserts_are_idempotent() -> None:
    if not URL:
        print("    (skipped: SUPABASE_EVAL_DB_URL_TEST not set)")
        return
    result = load_output("AVGO_20261003T135110.json")
    result["run_id"] = RUN_ID

    async def go() -> None:
        async with SupabaseStore(URL) as store:
            assert store.conn is not None, "could not connect"
            try:
                for _ in range(2):
                    await evaluate_result(result, None, model="jev-1.13.0", roles=["value_researcher", "esg_analyst"],
                                          store=store, runner=FakeRunner(), force=True, quiet=True)
                    counts = await _counts(store)
                assert counts[0] == 2 and counts[1] > 20, counts
                assert store.fallbacks == 0
            finally:
                async with store.conn.cursor() as cur:
                    await cur.execute("DELETE FROM eval.runs WHERE run_id=%s", (RUN_ID,))
                await store.conn.commit()

    asyncio.run(go())


def test_capture_store_contract_matches() -> None:
    """The record shape handed to every store carries all six parts."""
    store = CaptureStore()
    asyncio.run(evaluate_result(load_output("AVGO_20261003T135110.json"), None, model="jev-1.13.0",
                                roles=["value_researcher"], store=store, runner=FakeRunner(), quiet=True))
    rec = store.records[0]
    assert set(rec) == {"run", "agent_output", "rubric", "evaluation", "calls", "metrics"}
    assert all("call_ref" in m for m in rec["metrics"])
    assert {m["block"] for m in rec["metrics"]} == {"conviction", "domain", "alignment"}


if __name__ == "__main__":
    run_tests(globals())
