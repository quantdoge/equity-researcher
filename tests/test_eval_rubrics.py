"""
Guards the metrics/*.yaml rubrics: completeness, schema, prompt fidelity and limits.

A rubric is a reading of one prompt. These tests fail when:
- a role has no rubric;
- a rubric stops matching the Jev contract (the shared stance must be exactly
  STRONG SELL / SELL / HOLD / BUY / STRONG BUY; a Score has 2–10 levels);
- a prompt changes without its rubric being reviewed (the hash drift guard);
- an enum the rubric extracts no longer appears in the prompt.

Runs under pytest, or standalone:  python tests/test_eval_rubrics.py
Offline: no API key, no database.
"""

from __future__ import annotations

import json
import re

from _eval_fakes import load_output, run_tests

from equity_mcp.evaluation.checks import run_extracts
from equity_mcp.evaluation.evaluate import BLOCKS, plan_role
from equity_mcp.evaluation.extract import records_from_result, run_from_result
from equity_mcp.evaluation.jev import MAX_STATE_CHARS
from equity_mcp.evaluation.loader import PROMPTS_DIR, load_all, load_rubric, load_shared, validate_all
from equity_mcp.evaluation.schema import MAX_QUESTIONS_PER_REQUEST, STANCES
from equity_mcp.roles import ALL_ROLES


def test_every_role_has_one_valid_rubric() -> None:
    problems = validate_all()
    assert not problems, "\n".join(problems)


def test_shared_stance_is_exactly_five_way() -> None:
    shared = load_shared()
    assert tuple(shared.conviction.stance.criteria) == STANCES
    assert len(shared.conviction.conviction_level.criteria) == 3


def test_conviction_blocks_complete() -> None:
    for role, lr in load_all().items():
        c = lr.rubric.conviction
        assert len(c.domain_metrics) >= 4, f"{role}: fewer than 4 domain metrics"
        for mid, m in c.domain_metrics.items():
            assert len(m.criteria) == 5, f"{role}.{mid}: needs 5 levels"
            assert m.evidence_terms, f"{role}.{mid}: no evidence terms"
        if c.native_rating:
            values = set(lr.rubric.extract[c.native_rating].values or [])
            assert values <= set(c.native_to_stance), f"{role}: native_to_stance incomplete"


def test_enum_values_appear_verbatim_in_prompt() -> None:
    for role, lr in load_all().items():
        prompt = (PROMPTS_DIR / f"{role}.md").read_text(encoding="utf-8").lower()
        prompt = re.sub(r"[\s\-]+", " ", prompt)
        for eid, ex in lr.rubric.extract.items():
            for v in ex.values or []:
                needle = re.sub(r"[\s\-]+", " ", v.lower())
                assert needle in prompt, f"{role}.{eid}: '{v}' not in prompts/{role}.md"


def test_requests_respect_jev_limits_on_real_output() -> None:
    result = load_output("AVGO_20261003T135110.json")
    run = run_from_result(result, None)
    records = records_from_result(result)
    for role, lr in load_all().items():
        rec = records[role]
        ex = run_extracts(rec, lr.rubric.extract, lr.rubric.sections)
        summary = {"completed_specialists": 11} if lr.pass_ == 2 else None
        requests, _ = plan_role(lr, rec, run, ex, blocks=BLOCKS, order_check=True, summary=summary,
                                ctx={"failed_roles": []})
        assert requests, f"{role}: no Jev requests planned"
        for r in requests:
            assert len(r["questions"]) <= MAX_QUESTIONS_PER_REQUEST, f"{role}/{r['rubric_request']}: too many"
            size = len(json.dumps(r["state"], ensure_ascii=False, separators=(",", ":")))
            assert size <= MAX_STATE_CHARS + 200, f"{role}/{r['rubric_request']}: state {size} chars"


def test_instructions_do_not_lean_on_question_ids() -> None:
    """Jev never sees ids, so an instruction that names one ("see moat_rating") is unreadable to it.

    Only snake_case ids are checked: a one-word id such as ``stance`` or
    ``liquidity`` is an ordinary word in a sentence, not a reference.
    """
    for role, lr in load_all().items():
        questions = {qid: q for req in lr.alignment.requests for qid, q in req.questions.items()}
        questions.update(lr.rubric.conviction.domain_metrics)
        ids = {qid for qid in questions if "_" in qid} | {eid for eid in lr.rubric.extract if "_" in eid}
        for qid, q in questions.items():
            leaked = [i for i in ids if i in q.instructions]
            assert not leaked, f"{role}.{qid}: instructions mention ids {leaked}"


def test_prompt_drift_is_detected() -> None:
    lr = load_rubric("value_researcher")
    assert lr.prompt_drift() is None
    lr.rubric.source_prompt_sha256 = "0" * 64
    assert lr.prompt_drift() is not None


def test_rubric_sha_is_stable() -> None:
    assert load_rubric("value_researcher").sha == load_rubric("value_researcher").sha


if __name__ == "__main__":
    run_tests(globals())
