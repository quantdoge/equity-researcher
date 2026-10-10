"""
Guards the eval.v_rubric_* views and the --sync-rubrics path that feeds them.

- Every rubric view is security_invoker, commented, documented in the datadict
  seed and granted to eval_writer (both in the migration and the role script).
- The sync stores LoadedRubric.snapshot_row(), the same row an evaluation
  stores, and labels each role new / unchanged / stale correctly.

Runs under pytest, or standalone:  python tests/test_eval_rubric_views.py
Offline: no API key, no database.
"""

from __future__ import annotations

import asyncio
import re

from _eval_fakes import run_tests

from equity_mcp.evaluation.evaluate import main, sync_rubrics
from equity_mcp.evaluation.loader import REPO_ROOT, load_all

MIGRATION = REPO_ROOT / "supabase" / "migrations" / "20261011000000_eval_rubric_views.sql"
SEED = REPO_ROOT / "supabase" / "migrations" / "20261011000100_datadict_rubric_views_seed.sql"
WRITER = REPO_ROOT / "supabase" / "sql" / "eval_writer_role.sql"


def _views() -> list[str]:
    return re.findall(r"CREATE OR REPLACE VIEW eval\.(v_rubric_\w+)", MIGRATION.read_text(encoding="utf-8"))


def test_views_are_invoker_commented_documented_and_granted() -> None:
    sql = MIGRATION.read_text(encoding="utf-8")
    seed = SEED.read_text(encoding="utf-8")
    writer = WRITER.read_text(encoding="utf-8")
    views = _views()
    assert len(views) == 9, views
    for v in views:
        body = re.search(rf"CREATE OR REPLACE VIEW eval\.{v}\s+WITH \(security_invoker = true\)", sql)
        assert body, f"{v}: not security_invoker"
        assert f"COMMENT ON VIEW eval.{v} IS" in sql, f"{v}: no COMMENT ON VIEW"
        assert f"('eval', '{v}', 'view'," in seed, f"{v}: no datadict.tables row"
        assert f"'{v}'" in sql.split("DO $$")[-1], f"{v}: missing from the grant block"
        assert f"eval.{v}" in writer, f"{v}: missing from eval_writer_role.sql"


def test_snapshot_row_matches_rubric() -> None:
    for role, lr in load_all().items():
        row = lr.snapshot_row()
        assert row["rubric_sha"] == lr.sha and row["role"] == role
        assert set(row["content"]) == {"role", "shared"}
        assert row["content"]["role"]["pass"] in (1, 2), "views read content->'role'->>'pass'"


class _SyncStore:
    kind = "supabase"

    def __init__(self, stored: set[str], current: dict[str, str]) -> None:
        self.stored, self.current, self.saved = stored, current, []

    async def save_rubrics(self, rows: list[dict]) -> dict[str, bool]:
        self.saved += rows
        out = {r["rubric_sha"]: r["rubric_sha"] not in self.stored for r in rows}
        self.stored |= set(out)
        return out

    async def current_rubrics(self) -> dict[str, str]:
        return self.current


def test_sync_labels_new_unchanged_and_stale() -> None:
    rubrics = load_all(["value_researcher", "esg_analyst", "macro_researcher"])
    value, esg, macro = (rubrics[r].sha for r in ("value_researcher", "esg_analyst", "macro_researcher"))
    store = _SyncStore(stored={value, esg}, current={"value_researcher": value, "esg_analyst": "f" * 64})
    rows = {r["role"]: r["status"] for r in asyncio.run(sync_rubrics(rubrics, store))}
    assert rows == {"value_researcher": "unchanged", "esg_analyst": "stale", "macro_researcher": "new"}, rows
    assert [r["rubric_sha"] for r in store.saved] == [value, esg, macro]


def test_sync_dry_run_writes_nothing() -> None:
    store = _SyncStore(stored=set(), current={})
    rows = asyncio.run(sync_rubrics(load_all(["quant_analyst"]), store, dry_run=True))
    assert rows[0]["status"] == "dry_run" and store.saved == []
    assert main(["--sync-rubrics", "--dry-run", "--roles", "quant"]) == 0


if __name__ == "__main__":
    run_tests(globals())
