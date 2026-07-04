"""
deepagents-based agent factory.

Builds 12 specialist subagents (one per role) and wraps them under a master
Head of Research agent using LangChain's create_deep_agent.

Each subagent receives only the LangChain tools whose FastMCP tags include
its role — the same access-control logic as the Anthropic-SDK agent_factory.
The master agent uses deepagents' built-in planning loop to autonomously
decide which specialists to delegate to and synthesise a final Investment Memo.

Usage:
    import asyncio
    from equity_mcp.deep_agent_factory import run_research

    output = asyncio.run(run_research("AAPL"))
    print(output["investment_memo"])
"""

from __future__ import annotations

import asyncio
import json
from pathlib import Path
from typing import Any

from deepagents import create_deep_agent
from dotenv import load_dotenv

from equity_mcp.langchain_bridge import get_langchain_tools_for_role
from equity_mcp.roles import ALL_ROLES, ROLE_HEAD_OF_RESEARCH

load_dotenv()

_MODEL      = "anthropic:claude-sonnet-4-6"
_PROMPTS    = Path(__file__).parent / "prompts"

# One-line capability description shown to the master agent for each subagent.
# These inform the Head of Research when and why to delegate to each specialist.
_DESCRIPTIONS: dict[str, str] = {
    "sector_researcher":    "Sector dynamics, industry tailwinds/headwinds, and peer benchmarking on revenue and margins",
    "geo_legal_researcher": "Geopolitical risk, sanctions exposure, active litigation, and regulatory risk by jurisdiction",
    "macro_researcher":     "Macroeconomic environment (rates, inflation, GDP, yield curve) and impact on the company",
    "value_researcher":     "Economic moat, financial quality, intrinsic value via DCF/owner earnings — Warren Buffett style",
    "growth_researcher":    "Revenue growth trajectory, TAM, analyst estimate momentum, and upcoming catalysts — Cathie Wood style",
    "fin_risk_analyst":     "Credit risk, liquidity risk, market risk — Altman Z-Score, Piotroski F-Score, VaR, leverage ratios",
    "nonfin_risk_analyst":  "Governance quality, SEC enforcement, insider trading, operational and reputational risk",
    "quant_analyst":        "Factor scores (momentum, value, quality, low-vol), alpha/beta, Sharpe/Sortino, cross-sectional rankings",
    "short_analyst":        "Beneish M-Score, accruals, receivables red flags, competitive moat erosion — Jim Chanos style",
    "esg_analyst":          "Material E/S/G factors, controversies, board governance, climate transition and regulatory ESG exposure",
    "alt_data_analyst":     "Google Trends, patent filings, job postings, news sentiment, earnings surprise history",
    "portfolio_strategist": "Aggregate conviction scores, position sizing, portfolio-level correlation and factor exposure",
}


def _load_prompt(role: str) -> str:
    p = _PROMPTS / f"{role}.md"
    return p.read_text() if p.exists() else (
        f"You are the {role.replace('_', ' ').title()} agent in an elite equity research team."
    )


async def _build_subagent(role: str) -> dict[str, Any]:
    """Construct a single subagent dict for create_deep_agent."""
    tools = await get_langchain_tools_for_role(role)
    return {
        "name":          role,
        "description":   _DESCRIPTIONS.get(role, role),
        "system_prompt": _load_prompt(role),
        "tools":         tools,
        "model":         _MODEL,
    }


async def build_master_agent():
    """
    Construct the master Head of Research deep agent.

    All 12 specialist subagents are built concurrently (their tool lists are
    fetched in parallel from the in-process FastMCP server), then passed to
    create_deep_agent as the subagents roster.
    """
    specialist_roles = [r for r in ALL_ROLES if r != ROLE_HEAD_OF_RESEARCH]

    subagents = await asyncio.gather(*[
        _build_subagent(role) for role in specialist_roles
    ])

    master_tools = await get_langchain_tools_for_role(ROLE_HEAD_OF_RESEARCH)

    master = create_deep_agent(
        model=_MODEL,
        system_prompt=_load_prompt(ROLE_HEAD_OF_RESEARCH),
        tools=master_tools,
        subagents=list(subagents),
    )
    return master


async def run_research(symbol: str, extra_instructions: str = "") -> dict[str, Any]:
    """
    Run the full equity research pipeline for a ticker symbol.

    The master agent autonomously decides which specialists to delegate to and
    synthesises their outputs into a final Investment Memo.  Unlike the
    hard-coded 6-stage pipeline in orchestrator.py this is model-driven:
    the Head of Research plans its own task breakdown via deepagents'
    built-in write_todos planning tool.

    Returns:
        {
          "symbol":           str,
          "investment_memo":  str,   # final text output
          "messages":         list,  # full LangGraph message history
        }
    """
    master = await build_master_agent()

    task = (
        f"Conduct a complete institutional-quality equity research on ticker: {symbol}.\n\n"
        "Delegate to your specialist subagents to cover ALL dimensions:\n"
        "  • Alternative data signals (alt_data_analyst)\n"
        "  • Quantitative factor analysis (quant_analyst)\n"
        "  • Sector dynamics and peer benchmarking (sector_researcher)\n"
        "  • Geopolitical and legal risk (geo_legal_researcher)\n"
        "  • Macroeconomic environment (macro_researcher)\n"
        "  • Value investment analysis (value_researcher)\n"
        "  • Growth investment analysis (growth_researcher)\n"
        "  • Short / contrarian forensic analysis (short_analyst)\n"
        "  • ESG and sustainability (esg_analyst)\n"
        "  • Financial risk metrics (fin_risk_analyst)\n"
        "  • Non-financial and governance risk (nonfin_risk_analyst)\n"
        "  • Portfolio construction recommendation (portfolio_strategist)\n\n"
        "After collecting all specialist reports, produce a final Investment Memo "
        "in the structured format defined in your system prompt.\n"
    )
    if extra_instructions:
        task += f"\nAdditional instructions: {extra_instructions}"

    result = await master.ainvoke({"messages": task})

    messages = result.get("messages", [])
    final_text = ""
    if messages:
        last = messages[-1]
        final_text = last.content if hasattr(last, "content") else str(last)

    return {
        "symbol":          symbol,
        "investment_memo": final_text,
        "messages":        messages,
    }
