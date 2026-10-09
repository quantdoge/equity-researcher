"""
Guards the Jev boundary and the end-to-end evaluation pipeline, offline.

The response validator is the line between "Jev said something" and "we
store a score", so it is tested against every malformed shape. The pipeline is
run on real outputs with a fake Jev (tests/_eval_fakes.py), which exercises the
real planning, gating, two-pass and aggregation code.

Runs under pytest, or standalone:  python tests/test_eval_jev.py
"""

from __future__ import annotations

import asyncio

from _eval_fakes import CaptureStore, FakeRunner, load_output, run_tests

from equity_mcp.evaluation import aggregate as agg
from equity_mcp.evaluation.evaluate import evaluate_result, exit_code
from equity_mcp.evaluation.jev import JevRunner, validate_answer, wire_question
from equity_mcp.evaluation.schema import STANCES, ChoiceQ

SCORE = {"type": "score", "instructions": "x" * 20, "criteria": ["a", "b", "c", "d"]}
CHOICE = {"type": "choice", "instructions": "x" * 20, "criteria": {"A": "a", "B": "b"}}
NOUL = {"type": "noul", "instructions": "x" * 20}


def test_validator_accepts_good_answers() -> None:
    assert validate_answer(NOUL, {"type": "noul", "noul": 0.3}) is None
    assert validate_answer(CHOICE, {"type": "choice", "choice": "A", "confidence": 0.6,
                                    "probabilities": {"A": 0.6, "B": 0.4}}) is None
    assert validate_answer(SCORE, {"type": "score", "score": 2.4, "confidence": 0.5,
                                   "probabilities": {"0": 0, "1": 0.1, "2": 0.4, "3": 0.5}}) is None


def test_validator_rejects_bad_answers() -> None:
    assert validate_answer(NOUL, None) == "missing answer"
    assert validate_answer(NOUL, {"type": "noul", "noul": 1.3})
    assert validate_answer(NOUL, {"type": "score", "score": 1})
    assert validate_answer(CHOICE, {"type": "choice", "choice": "C", "confidence": 0.6,
                                    "probabilities": {"A": 0.6, "B": 0.4}})
    assert validate_answer(CHOICE, {"type": "choice", "choice": "A", "confidence": 0.6,
                                    "probabilities": {"A": 0.9, "B": 0.4}})
    assert validate_answer(SCORE, {"type": "score", "score": 3.5, "confidence": 0.5,
                                   "probabilities": {"3": 1.0}})
    assert validate_answer(SCORE, {"type": "score", "score": float("nan"), "confidence": 0.5,
                                   "probabilities": {"3": 1.0}})


def test_reversed_choice_keeps_options_but_flips_order() -> None:
    q = ChoiceQ(type="choice", instructions="Which stance does the report support?", weight=0,
                criteria={s: s.lower() for s in STANCES})
    fwd, rev = wire_question(q), wire_question(q, reversed_options=True)
    assert list(rev["criteria"]) == list(reversed(list(fwd["criteria"])))


def test_cache_key_independent_of_key_order() -> None:
    async def keys() -> tuple[str, str]:
        r = JevRunner(model="jev-1.13.0", dry_run=True)
        a = await r.call({"a": 1, "b": 2}, {"q": NOUL})
        b = await r.call({"b": 2, "a": 1}, {"q": NOUL})
        return a["cache_key"], b["cache_key"]

    a, b = asyncio.run(keys())
    assert a == b


def _evaluate(name: str, runner: FakeRunner, **kw) -> tuple[dict, CaptureStore]:
    store = CaptureStore(kw.pop("already", None))
    out = asyncio.run(evaluate_result(load_output(name), None, model="jev-1.13.0", store=store,
                                      runner=runner, quiet=True, **kw))
    return out, store


def test_end_to_end_clean_run() -> None:
    runner = FakeRunner()
    out, store = _evaluate("AVGO_20261003T135110.json", runner)
    assert len(out["roles"]) == 13
    by_role = {r["evaluation"]["role"]: r["evaluation"] for r in store.records}
    for role, ev in by_role.items():
        assert ev["stance"] in STANCES, role
        assert ev["status"] == "complete", (role, ev["status"])
        assert ev["domain_total"] >= 4, role
    # pass 2 sees the specialists, pass 1 does not
    with_summary = [s for s, _ in runner.calls if "specialist_summary" in s]
    assert with_summary and all(s["evaluation_context"]["agent_role"] in ("Portfolio Strategist", "Head Of Research")
                                for s in with_summary)
    assert exit_code([out]) == 0


def test_failed_agents_cost_nothing() -> None:
    runner = FakeRunner()
    out, store = _evaluate("IBM_20261006T150931.json", runner)
    failed = {r["evaluation"]["role"]: r for r in store.records if r["evaluation"]["status"] == "agent_failed"}
    assert set(failed) == {"geo_legal_researcher", "value_researcher", "growth_researcher"}
    assert all(not r["calls"] and not r["metrics"] for r in failed.values())
    hor = [s for s, _ in runner.calls if s["evaluation_context"]["agent_role"] == "Head Of Research"
           and "specialist_summary" in s]
    assert hor and len(hor[0]["specialist_summary"]["failed_or_missing_specialists"]) == 3


def test_call_errors_make_partial_not_guessed() -> None:
    runner = FakeRunner(fail_requests={"stance"})
    out, store = _evaluate("AVGO_20261003T135110.json", runner, roles=["value_researcher"])
    ev = store.records[0]["evaluation"]
    assert ev["stance"] is None and ev["status"] == "partial" and ev["n_errors"] >= 3
    assert exit_code([out]) == 2


def test_already_evaluated_is_skipped() -> None:
    runner = FakeRunner()
    out, store = _evaluate("AVGO_20261003T135110.json", runner, roles=["value_researcher"],
                           already={("AVGO_20261003T135110", "value_researcher")})
    assert out["roles"][0]["status"] == "already_evaluated" and not runner.calls and not store.records


def test_dry_run_sends_nothing() -> None:
    runner = JevRunner(model="jev-1.13.0", dry_run=True)
    out, store = _evaluate("AVGO_20261003T135110.json", runner, dry_run=True)
    assert not store.records
    assert all(r["status"] == "dry_run" and r["requests"] > 0 for r in out["roles"])


def test_veto_is_never_averaged_away() -> None:
    rows = [
        agg.metric_row(question_id="a", block="alignment", kind="noul", weight=3, normalized=1.0, passed=True),
        agg.metric_row(question_id="v", block="alignment", kind="noul", weight=0, veto=True,
                       normalized=0.0, passed=False),
    ]
    s = agg.summarise(rows, native=(None, None), gates_failed=0)
    assert s["alignment_composite"] == 1.0 and s["vetoes"] == ["v"] and s["veto_triggered"]


def test_gate_and_coverage_floor() -> None:
    rows = [
        agg.metric_row(question_id="g", block="alignment", kind="noul", weight=0, normalized=0.1, passed=False),
        agg.metric_row(question_id="x", block="alignment", kind="score", weight=3, normalized=0.9, passed=True),
        agg.metric_row(question_id="y", block="alignment", kind="noul", weight=1, normalized=0.9, passed=True,
                       rubric_request="other"),
    ]
    assert agg.apply_gate(rows[:2], "g") is True
    assert rows[1]["status"] == "low_evidence"
    s = agg.summarise(rows, native=(None, None), gates_failed=1)
    assert s["alignment_composite"] is None  # 1/4 of the weight usable < 70%
    assert s["insufficient_evidence"]


if __name__ == "__main__":
    run_tests(globals())
