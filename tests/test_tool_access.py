"""
Guards the role-based tool access model.

The tag filtering is the entire enforcement mechanism — an agent simply never
sees a tool it isn't entitled to. A silent regression here (a FastMCP release
moving where tag metadata lives, say) would not raise; it would just hand every
agent the wrong toolset. So assert the per-role counts directly.

Runs under pytest, or standalone:  python tests/test_tool_access.py
Needs no DATABASE_URL or ANTHROPIC_API_KEY — nothing here calls a tool.
"""

from __future__ import annotations

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from equity_mcp.langchain_bridge import (  # noqa: E402
    _list_tools_once,
    _result_to_text,
    _tags_of,
    get_langchain_tools_for_role,
)
from equity_mcp.roles import ALL_ROLES  # noqa: E402

TOTAL_TOOLS = 61

# rank_universe_by_factor is deliberately not in head_of_research's set: one
# call fans out to ~700 sequential DB connections.
EXPECTED_COUNTS: dict[str, int] = {
    "head_of_research":     6,   # the 6 SHARED tools; it delegates, it doesn't research
    "sector_researcher":    11,
    "geo_legal_researcher": 11,
    "macro_researcher":     11,
    "value_researcher":     22,
    "growth_researcher":    20,
    "fin_risk_analyst":     16,
    "nonfin_risk_analyst":  12,
    "quant_analyst":        25,
    "short_analyst":        21,
    "esg_analyst":          9,
    "alt_data_analyst":     15,
    "portfolio_strategist": 25,
}


def test_every_tool_exposes_tags() -> None:
    tools = asyncio.run(_list_tools_once())
    assert len(tools) == TOTAL_TOOLS, f"expected {TOTAL_TOOLS} tools, got {len(tools)}"
    for t in tools:
        assert _tags_of(t), f"{t.name} has no tags"


def test_per_role_tool_counts() -> None:
    for role in ALL_ROLES:
        tools = asyncio.run(get_langchain_tools_for_role(role))
        assert len(tools) == EXPECTED_COUNTS[role], (
            f"{role}: expected {EXPECTED_COUNTS[role]} tools, got {len(tools)}"
        )


def test_head_of_research_cannot_rank_universe() -> None:
    names = {t.name for t in asyncio.run(get_langchain_tools_for_role("head_of_research"))}
    assert "rank_universe_by_factor" not in names
    quant = {t.name for t in asyncio.run(get_langchain_tools_for_role("quant_analyst"))}
    assert "rank_universe_by_factor" in quant


def test_shared_tools_reach_every_role() -> None:
    shared = {"get_price_history", "get_company_profile", "get_sector_peers",
              "web_search", "fetch_page", "get_research_universe"}
    for role in ALL_ROLES:
        names = {t.name for t in asyncio.run(get_langchain_tools_for_role(role))}
        assert shared <= names, f"{role} is missing shared tools: {shared - names}"


def test_result_to_text_handles_both_shapes() -> None:
    class _Text:
        text = "hello"

    class _Modern:
        content = [_Text()]

    assert _result_to_text(_Modern()) == "hello"      # CallToolResult
    assert _result_to_text([_Text()]) == "hello"      # legacy bare list


if __name__ == "__main__":
    failures = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"  PASS  {name}")
            except AssertionError as exc:
                failures += 1
                print(f"  FAIL  {name}: {exc}")
    print("\nall passed" if not failures else f"\n{failures} failure(s)")
    sys.exit(1 if failures else 0)
