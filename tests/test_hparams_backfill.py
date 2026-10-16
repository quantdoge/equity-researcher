"""
Guards the git backfill's run classification (equity_mcp/hparams/backfill.py).

It works on the real repository history and the checked-in outputs/ and runs/,
so it pins down the reconstruction stored on 2026-10-11:
- 29 linkable runs: 25 CI runs on their trigger commit, and 4 local runs
  inferred from an uncommitted tree.
- JPM ran with a 600 s agent timeout that was never committed.

Offline: it reads git, but runs no extraction and uses no database.

Runs under pytest, or standalone:  python tests/test_hparams_backfill.py
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from _eval_fakes import OUTPUTS, run_tests

from equity_mcp.hparams import backfill as bf


@lru_cache(maxsize=1)
def _plans() -> dict[str, bf.LinkPlan]:
    return {lp.run.run_id: lp for lp in bf.plan(sorted(OUTPUTS.glob("*.json")))}


def test_start_line_parser() -> None:
    line = "2026-09-26T23:52:24  START  symbol=JPM agents=all concurrency=6 skip_synthesis=False timeout=None"
    assert bf.parse_start_line(line) == {"max_concurrency": 6, "timeout_s": None, "agents_requested": None,
                                         "skip_synthesis": False}
    sub = "START  symbol=AAPL agents=macro_researcher,esg_analyst concurrency=2 skip_synthesis=True timeout=600.0"
    assert bf.parse_start_line(sub)["agents_requested"] == ["macro_researcher", "esg_analyst"]
    assert bf.parse_start_line("no start here") is None


def test_legacy_runs_are_not_planned() -> None:
    plans = _plans()
    assert len(plans) == 29
    assert not any(r.startswith(("CMG_2026-0", "LIME_", "LTH_", "AMD_20260822")) for r in plans)


def test_every_linkable_run_is_linked() -> None:
    plans = _plans()
    assert all(lp.sha for lp in plans.values()), [r for r, lp in plans.items() if not lp.sha]
    bases = [lp.basis for lp in plans.values()]
    assert bases.count("git_checkout") == 25 and bases.count("inferred") == 4


def test_ci_runs_use_their_trigger_commit() -> None:
    lp = _plans()["AVGO_20261003T135110"]
    assert lp.run.kind == "ci" and lp.basis == "git_checkout"
    assert lp.sha.startswith("7836fa9")
    assert lp.run.run_params == {"max_concurrency": 6, "timeout_s": None, "agents_requested": None,
                                 "skip_synthesis": False, "focus": ""}


def test_jpm_timeout_fingerprint() -> None:
    lp = _plans()["JPM_20260926T235224"]
    assert lp.run.kind == "local" and lp.basis == "inferred"
    assert lp.sha.startswith("cb0a21f")
    assert lp.overrides == {"deep_agent_factory._AGENT_TIMEOUT_S": 600.0}


def test_run_log_rules_out_a_tree_without_run_log() -> None:
    lp = _plans()["AAPL_20260926T184412"]
    assert lp.sha.startswith("cb0a21f")
    assert any("no run_log.py" in n for n in lp.notes)


def test_ambiguous_local_run_says_so() -> None:
    lp = _plans()["XOM_20260927T085803"]
    assert lp.basis == "inferred" and lp.sha.startswith("b33c180")
    assert "also fits" in lp.notes[0]


def test_subset_run_records_its_params() -> None:
    params = _plans()["AAPL_20260926T222057"].run.run_params
    assert params["agents_requested"] is not None and params["timeout_s"] is not None
    assert params["focus"] is None  # local runs never recorded --focus


def test_fit_rejects_a_run_longer_than_the_timeout() -> None:
    run = _plans()["AVGO_20261003T135110"].run
    long = bf.RunEvidence(**{**run.__dict__, "max_elapsed": 5000.0, "timeouts": []})
    ok, _, why = bf._fit(long, _plans()["AVGO_20261003T135110"].sha)
    assert not ok and "past its" in why


def test_watched_paths_exist() -> None:
    root = Path(bf.REPO_ROOT)
    for p in bf.WATCHED:
        assert (root / p).exists(), p


if __name__ == "__main__":
    run_tests(globals())
