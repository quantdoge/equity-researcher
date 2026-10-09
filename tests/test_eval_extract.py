"""
Guards report parsing, deterministic checks and stance mapping against real outputs.

The fixtures are checked-in outputs, chosen for one awkward property each:
- AVGO_20261003T135110: a clean run, chatter preambles, a hedged memo verdict.
- IBM_20261006T150931: three specialists failed.
- AAPL_20260926T184412: a --skip-synthesis run whose esg "success" is a stub.
- AMD_20260822T152843: a current-style filename with the legacy schema.
- AXP_20261003T140229: a stray "# **HOLD**" heading inside a "##" section.

Runs under pytest, or standalone:  python tests/test_eval_extract.py
"""

from __future__ import annotations

from pathlib import Path

from _eval_fakes import OUTPUTS, load_output, run_tests

from equity_mcp.evaluation.checks import domain_coverage, price_target_consistency, run_check, run_extracts
from equity_mcp.evaluation.extract import Report, load_run, records_from_result, run_extract, section_text
from equity_mcp.evaluation.loader import load_rubric
from equity_mcp.evaluation.schema import DeterministicCheck, DomainMetric, Extract, Section
from equity_mcp.evaluation.stance import conviction_label, native_stance, stance_expected
from equity_mcp.roles import ALL_ROLES


def test_clean_run_has_thirteen_ok_records() -> None:
    records = records_from_result(load_output("AVGO_20261003T135110.json"))
    assert set(records) == set(ALL_ROLES)
    assert all(r["status"] == "ok" for r in records.values())
    stripped = sum(1 for r in records.values() if r["preamble"])
    assert stripped >= 8, f"only {stripped} preambles stripped"
    assert "13 specialist reports" in records["head_of_research"]["preamble"]


def test_failed_specialists_detected() -> None:
    records = records_from_result(load_output("IBM_20261006T150931.json"))
    for role in ("geo_legal_researcher", "value_researcher", "growth_researcher"):
        assert records[role]["status"] == "failed", role


def test_stub_output_is_degenerate_and_synthesis_absent() -> None:
    records = records_from_result(load_output("AAPL_20260926T184412.json"))
    assert records["esg_analyst"]["status"] == "degenerate"
    assert "portfolio_strategist" not in records and "head_of_research" not in records


def test_legacy_schema_classified_by_keys_not_name() -> None:
    run, records = load_run(OUTPUTS / "AMD_20260822T152843.json")
    assert run["schema_kind"] == "legacy" and records == {}
    assert run["skip_reason"]


def test_value_extracts_on_avgo() -> None:
    lr = load_rubric("value_researcher")
    rec = records_from_result(load_output("AVGO_20261003T135110.json"))["value_researcher"]
    ex = run_extracts(rec, lr.rubric.extract, lr.rubric.sections)
    assert ex["moat_rating"]["value"] == "Wide"
    assert ex["fq_score"]["value"] == 8
    assert ex["verdict"]["value"] == "Hold"
    assert native_stance(lr.rubric.conviction, ex) == ("Hold", "HOLD")


def test_stray_top_level_heading_does_not_end_section() -> None:
    lr = load_rubric("value_researcher")
    rec = records_from_result(load_output("AXP_20261003T140229.json"))["value_researcher"]
    sec = section_text(rec, "verdict", lr.rubric.sections)
    assert sec and "HOLD" in sec["text"] and len(sec["body"]) > 100


def test_memo_bold_line_headings_split() -> None:
    memo = load_output("AVGO_20261003T135110.json")["investment_memo"]
    rep = Report(memo)
    sec = rep.find(Section(heading="^verdict"))
    assert sec is not None and "HOLD" in sec["heading"]
    assert rep.find(Section(heading="bull case")) is not None


def test_enum_matching_longest_first_and_hedges() -> None:
    ex = Extract(section="x", values=["Strong Buy", "Buy", "Hold", "Sell", "Strong Sell"])
    sec = {"heading": "## 6. Growth Verdict: **Strong Buy**", "body": "", "text": ""}
    assert run_extract(ex, sec)["value"] == "Strong Buy"
    pre = Extract(section="x", values=["Tracking Above", "In-Line", "Below"], aliases={"Above": "Tracking Above"})
    out = run_extract(pre, {"heading": "## 3. Earnings Preview Signal: **In-Line-to-Above** consensus",
                            "body": "", "text": ""})
    assert out["value"] == "In-Line" and out["hedged"]


def test_price_target_band_arithmetic() -> None:
    ok = "**Price Target**: Fair-entry band **$240–300** (−16% to −32% from $355.14); bear $210"
    assert price_target_consistency(ok)["passed"] is True
    bad = "**Price Target**: $400 (+40% upside from current $355.14)"
    assert price_target_consistency(bad)["passed"] is False
    narrative = "**Price Target**: Base ~$140 (≈ flat — already at intrinsic)"
    assert price_target_consistency(narrative)["passed"] is None


def test_table_check_columns_and_rows() -> None:
    text = ("## 1. Factor Scores\n| Factor | Score | Sector Rank | Signal |\n|---|---|---|---|\n"
            "| Value | 2 | 4/5 | Neg |\n| Momentum | 3 | 3/5 | Neu |\n")
    rec = {"status": "ok", "full": text, "raw": text, "preamble": "", "report": Report(text)}
    chk = DeterministicCheck(id="t", kind="table_present", section="f", min_rows=2,
                             columns=["Factor", "Sector Rank"], row_labels=["Value", "Momentum"])
    res = run_check(chk, rec, {"f": Section(heading="factor")}, {}, {})
    assert res["passed"], res
    chk2 = chk.model_copy(update={"row_labels": ["Quality"]})
    assert run_check(chk2, rec, {"f": Section(heading="factor")}, {}, {})["passed"] is False


def test_failures_acknowledged_check() -> None:
    text = "## Conviction\n| Value Researcher | **Unavailable** (timeout) |\n"
    rec = {"status": "ok", "full": text, "raw": text, "preamble": "", "report": Report(text)}
    chk = DeterministicCheck(id="f", kind="failures_acknowledged", section="full")
    assert run_check(chk, rec, {}, {}, {"failed_roles": ["value_researcher"]})["passed"]
    assert run_check(chk, rec, {}, {}, {"failed_roles": ["growth_researcher"]})["passed"] is False


def test_domain_coverage_gate() -> None:
    text = "## Financial Quality\nGross margin 68%, operating margin 40%."
    rec = {"status": "ok", "full": text, "raw": text, "preamble": "", "report": Report(text)}
    secs = {"fq": Section(heading="financial quality")}
    liq = DomainMetric(label="Liquidity", section=["fq"], evidence_terms=["current ratio", "working capital"],
                       instructions="Based only on what this research report states, how liquid?",
                       criteria=["a", "b", "c", "d", "e"])
    prof = liq.model_copy(update={"evidence_terms": ["margin"]})
    assert domain_coverage(liq, rec, secs)["addressed"] is False
    assert domain_coverage(prof, rec, secs)["addressed"] is True


def test_stance_maths() -> None:
    assert stance_expected({"HOLD": 0.5, "BUY": 0.5}) == 0.5
    assert stance_expected({"STRONG SELL": 1.0}) == -2
    assert stance_expected(None) is None
    assert conviction_label(1.6) == "High" and conviction_label(0.2) == "Low"


def test_native_maps_for_special_roles() -> None:
    quant = load_rubric("quant_analyst").rubric.conviction
    assert quant.native_to_stance.get("Neutral") == "HOLD"
    short = load_rubric("short_analyst").rubric.conviction
    assert short.native_to_stance.get("Reject Short Thesis") is None
    assert short.native_to_stance.get("Strong Short") == "STRONG SELL"


if __name__ == "__main__":
    run_tests(globals())
