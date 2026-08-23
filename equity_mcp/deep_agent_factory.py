"""
deepagents-based agent factory.

Builds 13 specialist subagents (one per role) and wraps them under a master
Head of Research agent using LangChain's create_deep_agent.

Each subagent receives only the LangChain tools whose FastMCP tags include its
role.  In practice that means the twelve analysts all get the same fmp_catalog /
fmp_call pair, while quant_engineer additionally gets run_python — it is the one
agent that executes code, and everything computed in a run is computed there.

Each subagent also runs on the model roles.chat_model_for_role assigns to it, so
specialists can be pointed at different OpenRouter models independently of the
master.  The master agent uses deepagents' built-in planning loop to autonomously
decide which specialists to delegate to and synthesise a final Investment Memo.

One structural constraint worth knowing: deepagents compiles each subagent spec
through plain create_agent with only its own tools, so subagents have no `task`
tool and cannot delegate to each other.  An analyst that needs a computed metric
says so in its report and the Head of Research routes it to quant_engineer.

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
from equity_mcp.roles import (
    ALL_ROLES,
    ROLE_HEAD_OF_RESEARCH,
    chat_model_for_role,
    middleware_for_role,
)

load_dotenv()

_PROMPTS    = Path(__file__).parent / "prompts"

# One-line capability description shown to the master agent for each subagent.
# These inform the Head of Research when and why to delegate to each specialist.
_DESCRIPTIONS: dict[str, str] = {
    "quant_engineer":       "Runs financial computations — finds the right FMP endpoints, pulls the series, and writes and executes Python over them. Delegate any number no FMP endpoint returns directly: custom factor scores, correlation matrices, regressions, cross-sectional ranks, multi-symbol aggregates, forensic ratios",
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
    """
    Role prompt plus the shared toolkit appendix.

    Every agent reaches data the same way, so the catalog/fetch/delegate workflow
    lives once in _toolkit.md rather than being copied into each role file.  The
    role prompt stays what it should be — how this analyst thinks — and adding an
    agent means writing only that.
    """
    p = _PROMPTS / f"{role}.md"
    role_prompt = p.read_text(encoding="utf-8") if p.exists() else (
        f"You are the {role.replace('_', ' ').title()} agent in an elite equity research team."
    )

    toolkit = _PROMPTS / "_toolkit.md"
    if toolkit.exists():
        return f"{role_prompt.rstrip()}\n\n{toolkit.read_text(encoding='utf-8')}"
    return role_prompt


async def _build_subagent(role: str) -> dict[str, Any]:
    """
    Construct a single subagent dict for create_deep_agent.

    The middleware entry carries this role's call budgets.  It is built from the
    names of the tools the role actually received, so only those are capped —
    deepagents' own built-ins stay uncapped by design.  deepagents applies this
    list after its default stack.
    """
    tools = await get_langchain_tools_for_role(role)
    return {
        "name":          role,
        "description":   _DESCRIPTIONS.get(role, role),
        "system_prompt": _load_prompt(role),
        "tools":         tools,
        "model":         chat_model_for_role(role),
        "middleware":    middleware_for_role(role, [t.name for t in tools]),
    }


async def build_master_agent(checkpointer: Any | None = None):
    """
    Construct the master Head of Research deep agent.

    All 13 specialist subagents are built concurrently (their tool lists are
    fetched in parallel from the in-process FastMCP server), then passed to
    create_deep_agent as the subagents roster.

    The master gets its own middleware because middleware passed here does not
    propagate to subagents — each subagent spec carries its own, set in
    _build_subagent.  The master's model calls are uncapped (see MODEL_CALL_LIMITS
    in roles.py); only its four data tools are.

    ``checkpointer`` persists the master graph so a failed run can be resumed;
    it goes only to the master because the SubAgent spec has nowhere to put one,
    which is what bounds resume granularity to a whole specialist (see
    session.py).  ``None`` builds an unpersisted graph, which is what the compile
    checks and any ad-hoc use want.
    """
    specialist_roles = [r for r in ALL_ROLES if r != ROLE_HEAD_OF_RESEARCH]

    subagents = await asyncio.gather(*[
        _build_subagent(role) for role in specialist_roles
    ])

    master_tools = await get_langchain_tools_for_role(ROLE_HEAD_OF_RESEARCH)

    master = create_deep_agent(
        model=chat_model_for_role(ROLE_HEAD_OF_RESEARCH),
        system_prompt=_load_prompt(ROLE_HEAD_OF_RESEARCH),
        tools=master_tools,
        subagents=list(subagents),
        middleware=middleware_for_role(
            ROLE_HEAD_OF_RESEARCH, [t.name for t in master_tools]
        ),
        checkpointer=checkpointer,
    )
    return master


# One superstep per model turn and per tool batch, and the master plans,
# delegates thirteen times and synthesises.  LangGraph's default of 25 is thin
# enough that a long-but-healthy run can trip it, and a GraphRecursionError is
# indistinguishable from a crash worth resuming from.
RECURSION_LIMIT = 200


async def run_research(
    symbol: str,
    extra_instructions: str = "",
    *,
    session_id: str | None = None,
    checkpointer: Any | None = None,
    resume: bool = False,
) -> dict[str, Any]:
    """
    Run the full equity research pipeline for a ticker symbol.

    The master agent autonomously decides which specialists to delegate to and
    synthesises their outputs into a final Investment Memo.  Unlike the
    hard-coded 6-stage pipeline in orchestrator.py this is model-driven:
    the Head of Research plans its own task breakdown via deepagents'
    built-in write_todos planning tool.

    ``session_id`` becomes the LangGraph thread id, so it must be the same
    string across a run and its resumes — orchestrator.py uses the workspace
    directory name.  With ``resume=True`` the graph is invoked with ``None``
    input, which re-runs the pending tasks recorded in the checkpoint instead of
    appending a second copy of the task message.

    Returns:
        {
          "symbol":           str,
          "investment_memo":  str,   # final text output
          "messages":         list,  # full LangGraph message history
        }
    """
    master = await build_master_agent(checkpointer=checkpointer)

    config: dict[str, Any] = {"recursion_limit": RECURSION_LIMIT}
    if session_id:
        config["configurable"] = {"thread_id": session_id}

    task = (
        f"Conduct a complete institutional-quality equity research on ticker: {symbol}.\n\n"
        "Delegate to your specialist subagents to cover ALL dimensions:\n"
        "  • Alternative data signals (alt_data_analyst)\n"
        "  • Any metric that needs computing rather than fetching (quant_engineer)\n"
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
        "in the structured format defined in your system prompt.\n\n"
        "Specialists cannot call each other. When one reports that it needs a "
        "figure computed — a factor score, a correlation, a forensic ratio, a "
        "cross-sectional rank — delegate that to quant_engineer yourself and "
        "feed the result back into the memo.\n"
    )
    if extra_instructions:
        task += f"\nAdditional instructions: {extra_instructions}"

    payload: Any = {"messages": task}
    if resume:
        # Resuming means "carry on from the checkpoint", which LangGraph spells
        # as a None input.  If there is no checkpoint to carry on from — the
        # first run died before its first superstep committed — that would be an
        # empty invocation, so fall back to starting the task properly.
        state = await master.aget_state(config)
        if state is not None and state.values.get("messages"):
            payload = None

    result = await master.ainvoke(payload, config)

    messages = result.get("messages", [])
    final_text = ""
    if messages:
        last = messages[-1]
        # .text flattens block-list content, which non-Anthropic providers on
        # OpenRouter are more likely to return than a plain string.
        final_text = str(last.text) if hasattr(last, "text") else str(last)

    return {
        "symbol":          symbol,
        "investment_memo": final_text,
        "messages":        messages,
    }
