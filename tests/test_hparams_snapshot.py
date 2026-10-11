"""
Guards the hyperparameter snapshot (equity_mcp/hparams/snapshot.py).

A snapshot's value is that it describes the pipeline that actually ran. So
these tests check it against the live code it claims to describe:
- tool counts against tests/test_tool_access.py
- prompt hashes against the rubric loader
- composed prompts against a fresh render

They also check that building one leaves no patch behind. Offline: no API key,
no database, no network.

Runs under pytest, or standalone:  python tests/test_hparams_snapshot.py
"""

from __future__ import annotations

import asyncio
import importlib.util
import json
from functools import lru_cache
from pathlib import Path

from _eval_fakes import run_tests

import equity_mcp.deep_agent_factory as daf
from equity_mcp.evaluation.loader import _canonical, prompt_sha256
from equity_mcp.hparams import snapshot as hs
from equity_mcp.hparams.ingest import link_row
from equity_mcp.langchain_bridge import get_langchain_tools_for_role
from equity_mcp.roles import ALL_ROLES

TESTS = Path(__file__).resolve().parent


@lru_cache(maxsize=1)
def _snap() -> hs.Snapshot:
    return asyncio.run(hs.build_snapshot(provenance="reconstructed_from_git", libs=False))


def _expected_counts() -> dict[str, int]:
    spec = importlib.util.spec_from_file_location("_tool_access", TESTS / "test_tool_access.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.EXPECTED_COUNTS


def test_snapshot_is_internally_consistent() -> None:
    snap = _snap()
    assert snap.problems() == [], snap.problems()
    assert snap.gaps == [], snap.gaps
    assert len(snap.agents) == len(ALL_ROLES) == 13
    assert len(snap.tools) == 61


def test_snapshot_is_deterministic() -> None:
    again = asyncio.run(hs.build_snapshot(provenance="captured_at_runtime", libs=True))
    assert again.sha == _snap().sha, "observation metadata must stay outside the hash"


def test_access_matches_tool_access_test() -> None:
    expected = _expected_counts()
    got = {a["role"]: a["tool_count"] for a in _snap().agents}
    assert got == expected, {r: (got.get(r), n) for r, n in expected.items() if got.get(r) != n}
    assert len(_snap().role_tools) == sum(expected.values()) == 204


def test_access_matches_bridge() -> None:
    granted: dict[str, set[str]] = {}
    for rt in _snap().role_tools:
        granted.setdefault(rt["role"], set()).add(rt["tool_name"])
    for role in ALL_ROLES:
        names = {t.name for t in asyncio.run(get_langchain_tools_for_role(role))}
        assert granted[role] == names, role


def test_system_prompt_sha_joins_to_rubrics() -> None:
    for a in _snap().agents:
        assert a["system_prompt_sha"] == prompt_sha256(a["role"]), a["role"]


def test_composed_prompt_is_what_the_builder_renders() -> None:
    texts = _snap().texts
    for a in _snap().agents:
        head = a["role"] == "head_of_research"
        limit = daf._MASTER_RECURSION_LIMIT if head else daf._SPECIALIST_RECURSION_LIMIT
        tokens = daf._MEMO_MAX_TOKENS if head else daf._SPECIALIST_MAX_TOKENS
        expected = daf._load_prompt(a["role"]) + daf._budget_block(limit, daf._AGENT_TIMEOUT_S, tokens, is_master=head)
        assert texts[a["composed_prompt_sha"]] == hs.normalise_text(expected), a["role"]


def test_advertised_values_appear_in_the_rendered_block() -> None:
    texts = _snap().texts
    for a in _snap().agents:
        block = texts[a["budget_sha"]]
        assert f"About {a['advertised_tool_rounds']} rounds" in block, a["role"]
        assert f"by round {a['advertised_write_by']}" in block, a["role"]
        assert f"{a['advertised_timeout_s']:.0f} seconds" in block, a["role"]
    rt = _snap().runtime
    assert rt["advertised_fraction"] == 0.75
    roles = {a["role"]: a for a in _snap().agents}
    assert (roles["value_researcher"]["advertised_tool_rounds"], roles["value_researcher"]["advertised_write_by"]) == (10, 8)
    assert (roles["head_of_research"]["advertised_tool_rounds"], roles["head_of_research"]["advertised_write_by"]) == (5, 3)


def test_runtime_values() -> None:
    rt = _snap().runtime
    assert rt["tool_timeout_s"] == 90 and rt["max_tool_threads"] == 48
    assert rt["agent_timeout_s"] == daf._AGENT_TIMEOUT_S
    assert rt["request_timeout_ms"] == 600_000 and rt["streaming"] is True
    assert rt["provider_routing"] == {"ignore": ["azure"]}
    roles = {a["role"]: a for a in _snap().agents}
    assert roles["portfolio_strategist"]["agent_kind"] == "react_specialist"
    assert roles["portfolio_strategist"]["max_tokens"] == daf._SPECIALIST_MAX_TOKENS
    assert roles["head_of_research"]["agent_kind"] == "deep_master"
    assert roles["head_of_research"]["task"] == "Produce the final Investment Memo."
    assert roles["portfolio_strategist"]["task"].startswith("Review all specialist reports")


def test_build_leaves_no_patch_behind() -> None:
    import langchain.chat_models as lcm
    from deepagents import create_deep_agent
    from langchain.chat_models import base
    from langgraph.prebuilt import create_react_agent

    _snap()
    assert daf.create_react_agent is create_react_agent
    assert daf.create_deep_agent is create_deep_agent
    assert lcm.init_chat_model is base.init_chat_model
    assert daf._BUDGET_TEMPLATE.name == "_execution_budget.md"


def test_override_makes_a_distinct_config_and_is_undone() -> None:
    before = daf._AGENT_TIMEOUT_S
    snap = asyncio.run(hs.build_snapshot(provenance="inferred", libs=False,
                                         overrides={"deep_agent_factory._AGENT_TIMEOUT_S": 600.0}))
    assert daf._AGENT_TIMEOUT_S == before
    assert snap.sha != _snap().sha
    assert snap.runtime["agent_timeout_s"] == 600.0
    assert {a["advertised_timeout_s"] for a in snap.agents} == {450.0}


def test_canonical_json_agrees_with_rubric_hashing() -> None:
    payload = {"b": ["x", {"z": True, "a": None}], "a": "—café"}
    assert hs.canonical_json(payload) == _canonical(payload)


def test_whole_floats_hash_as_ints() -> None:
    assert hs.sha256_json({"t": 750.0}) == hs.sha256_json({"t": 750})
    assert hs.sha256_json({"t": 750.5}) != hs.sha256_json({"t": 750})
    assert hs.sha256_json({"tags": {"b", "a"}}) == hs.sha256_json({"tags": ["a", "b"]})


def test_crlf_hashes_like_lf() -> None:
    assert hs.sha256_text("a\r\nb\rc\n") == hs.sha256_text("a\nb\nc\n")


def test_utf8_survives() -> None:
    bodies = list(_snap().texts.values())
    assert any("—" in b for b in bodies), "prompts carry em dashes"
    assert not any("â€" in b for b in bodies), "cp1252 mojibake in a stored prompt"


def test_record_round_trips() -> None:
    rec = json.loads(json.dumps(_snap().to_record()))
    back = hs.Snapshot.from_record(rec)
    assert back.sha == _snap().sha and back.problems() == []


def test_tampering_is_detected() -> None:
    rec = json.loads(json.dumps(_snap().to_record()))
    sha = next(iter(rec["texts"]))
    rec["texts"][sha] += " edited"
    assert hs.Snapshot.from_record(rec).problems()


def test_link_row_from_run_params() -> None:
    row = link_row("AAPL_X", "a" * 64, "recorded_in_run",
                   {"max_concurrency": 2, "timeout_s": 600, "agents_requested": ["macro_researcher"],
                    "focus": "", "skip_synthesis": True})
    assert row["max_concurrency"] == 2 and row["run_timeout_s"] == 600
    assert row["extra_instructions"] == "" and row["overrides"] == {"skip_synthesis": True}


if __name__ == "__main__":
    run_tests(globals())
