"""
deepagents-based agent factory.

Runs the 12 specialists as independent LangGraph agents fanned out
concurrently, then hands their reports to a master Head of Research deep agent
for synthesis.

Each specialist receives only the LangChain tools whose FastMCP tags include
its role — the same access-control logic as the Anthropic-SDK agent_factory.

Why the fan-out is explicit rather than model-driven: the master used to be
given all 12 specialists as ``subagents`` and asked, in prose, to cover every
dimension.  Claude issues those delegation calls one at a time, so a run was
~14 agent executions end to end.  Ordering them here instead puts 11 research
specialists on one ``asyncio.gather`` and leaves 3 steps on the critical path.
Nothing is lost by doing so: the specialists never read each other's output.

Usage:
    import asyncio
    from equity_mcp.deep_agent_factory import run_research

    output = asyncio.run(run_research("AAPL"))
    print(output["investment_memo"])
"""

from __future__ import annotations

import asyncio
import time
from pathlib import Path
from typing import Any, Callable

from deepagents import create_deep_agent
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langgraph.prebuilt import create_react_agent

from equity_mcp.langchain_bridge import get_langchain_tools_for_role
from equity_mcp.roles import (
    ALL_ROLES,
    ROLE_HEAD_OF_RESEARCH,
    ROLE_PORTFOLIO,
)

load_dotenv()

_MODEL = "claude-sonnet-4-6"

# Set explicitly rather than left to the provider default, which is the full
# 128k output window — enough for a single runaway specialist to spend minutes
# generating, and large enough to risk an HTTP timeout on a non-streaming call.
_SPECIALIST_MAX_TOKENS = 8096
_MEMO_MAX_TOKENS       = 16000

# LangGraph super-step ceilings.  A specialist is one tool loop; the master no
# longer delegates, so it needs far fewer steps than the default 25.
_SPECIALIST_RECURSION_LIMIT = 20
_MASTER_RECURSION_LIMIT     = 15

# Per-agent wall-clock ceiling.  A hung specialist used to hang the whole CLI.
_AGENT_TIMEOUT_S = 900.0

# Concurrent specialists.  Nothing in this repo retries or backs off, and the
# tools hit rate-limited third parties (SEC EDGAR allows 10 req/s), so an
# unthrottled 11-way fan-out trades one bottleneck for another.
_DEFAULT_MAX_CONCURRENCY = 6

_PROMPTS = Path(__file__).parent / "prompts"

# The specialists that do primary research.  The portfolio strategist is a
# synthesiser — it reads the others — so it runs after them, not alongside.
RESEARCH_ROLES: list[str] = [
    r for r in ALL_ROLES if r not in (ROLE_HEAD_OF_RESEARCH, ROLE_PORTFOLIO)
]

# Task given to each specialist.  Mirrors DEFAULT_TASKS in the legacy pipeline.
_TASKS: dict[str, str] = {
    "sector_researcher":    "Analyse the sector, tailwinds/headwinds, and peer benchmarking.",
    "geo_legal_researcher": "Identify geographic exposures, geopolitical risks, and regulatory risk.",
    "macro_researcher":     "Assess the macroeconomic environment and its impact on this company.",
    "value_researcher":     "Conduct a thorough value investment analysis.",
    "growth_researcher":    "Conduct a thorough growth investment analysis.",
    "fin_risk_analyst":     "Conduct a complete financial risk assessment.",
    "nonfin_risk_analyst":  "Conduct a complete non-financial risk assessment.",
    "quant_analyst":        "Compute all quantitative factor scores, alpha/beta, and Sharpe/Sortino ratios.",
    "short_analyst":        "Conduct a forensic short-seller analysis.",
    "esg_analyst":          "Conduct a full ESG analysis.",
    "alt_data_analyst":     "Gather and interpret all available alternative data signals.",
}


def _load_prompt(role: str) -> str:
    p = _PROMPTS / f"{role}.md"
    return p.read_text() if p.exists() else (
        f"You are the {role.replace('_', ' ').title()} agent in an elite equity research team."
    )


def _build_model(max_tokens: int) -> ChatAnthropic:
    return ChatAnthropic(model=_MODEL, max_tokens=max_tokens, timeout=_AGENT_TIMEOUT_S)


def _final_text(result: dict[str, Any]) -> str:
    messages = result.get("messages", [])
    if not messages:
        return ""
    last = messages[-1]
    content = last.content if hasattr(last, "content") else str(last)
    if isinstance(content, list):
        # Anthropic content blocks — keep the text parts.
        return "\n".join(
            b.get("text", "") if isinstance(b, dict) else str(b) for b in content
        ).strip()
    return str(content).strip()


async def build_specialist_agent(role: str, max_tokens: int = _SPECIALIST_MAX_TOKENS):
    """
    Build one standalone research agent for *role*, holding only that role's tools.

    Uses a plain react agent rather than create_deep_agent: a leaf researcher
    has nothing to delegate to and no use for deepagents' injected planning and
    virtual-filesystem tools, which would only add per-turn tokens and turns.
    """
    tools = await get_langchain_tools_for_role(role)
    return create_react_agent(
        _build_model(max_tokens),
        tools,
        prompt=_load_prompt(role),
        name=role,
    )


async def _run_one_agent(
    role: str,
    symbol: str,
    task: str,
    extra_context: str = "",
    recursion_limit: int = _SPECIALIST_RECURSION_LIMIT,
    max_tokens: int = _SPECIALIST_MAX_TOKENS,
) -> dict[str, Any]:
    """Run a single agent to completion, capturing timing and any failure."""
    started = time.time()

    user_content = f"Symbol: {symbol}\nTask: {task}"
    if extra_context:
        user_content += f"\n\nAdditional context:\n{extra_context}"

    try:
        if role == ROLE_HEAD_OF_RESEARCH:
            agent = await build_head_agent()
        else:
            agent = await build_specialist_agent(role, max_tokens=max_tokens)

        result = await asyncio.wait_for(
            agent.ainvoke(
                {"messages": [{"role": "user", "content": user_content}]},
                config={"recursion_limit": recursion_limit},
            ),
            timeout=_AGENT_TIMEOUT_S,
        )
        return {
            "agent_role":      role,
            "symbol":          symbol,
            "output":          _final_text(result),
            "elapsed_seconds": round(time.time() - started, 1),
            "error":           None,
        }
    except Exception as exc:
        # One dead specialist must not take the run down with it — the memo is
        # still worth producing from the other ten.
        return {
            "agent_role":      role,
            "symbol":          symbol,
            "output":          "",
            "elapsed_seconds": round(time.time() - started, 1),
            "error":           f"{type(exc).__name__}: {exc}",
        }


async def run_specialists(
    symbol: str,
    roles: list[str] | None = None,
    max_concurrency: int = _DEFAULT_MAX_CONCURRENCY,
    on_complete: Callable[[dict[str, Any]], None] | None = None,
) -> list[dict[str, Any]]:
    """
    Run the research specialists concurrently and return their reports.

    *on_complete* is invoked with each result as it lands, so callers can show
    progress instead of staring at a silent multi-minute run.
    """
    roles = roles or RESEARCH_ROLES
    semaphore = asyncio.Semaphore(max_concurrency)

    async def _guarded(role: str) -> dict[str, Any]:
        async with semaphore:
            result = await _run_one_agent(
                role, symbol, _TASKS.get(role, "Conduct your analysis for this company.")
            )
        if on_complete:
            on_complete(result)
        return result

    pending = [asyncio.create_task(_guarded(role)) for role in roles]
    return list(await asyncio.gather(*pending))


async def build_head_agent():
    """
    Build the master Head of Research agent.

    Keeps create_deep_agent — its planning tools still earn their place when
    structuring a long memo — but with no subagents: delegation is now the
    orchestrator's job, done concurrently.
    """
    master_tools = await get_langchain_tools_for_role(ROLE_HEAD_OF_RESEARCH)
    return create_deep_agent(
        model=_build_model(_MEMO_MAX_TOKENS),
        system_prompt=_load_prompt(ROLE_HEAD_OF_RESEARCH),
        tools=master_tools,
        subagents=[],
    )


def format_reports(results: list[dict[str, Any]]) -> str:
    """Render specialist reports as the context block passed to later stages."""
    blocks = []
    for r in results:
        title = r["agent_role"].replace("_", " ").title()
        if r.get("error"):
            blocks.append(f"## {title}\n\n_Unavailable: {r['error']}_")
        else:
            blocks.append(f"## {title}\n\n{r['output']}")
    return "\n---\n\n".join(blocks)


async def run_research(
    symbol: str,
    extra_instructions: str = "",
    max_concurrency: int = _DEFAULT_MAX_CONCURRENCY,
    on_agent_complete: Callable[[dict[str, Any]], None] | None = None,
) -> dict[str, Any]:
    """
    Run the full equity research pipeline for a ticker symbol.

    Three steps on the critical path:
      1. the 11 research specialists, concurrently
      2. the portfolio strategist, over their reports
      3. the Head of Research, over everything, producing the Investment Memo

    Returns:
        {
          "symbol":            str,
          "investment_memo":   str,
          "portfolio_brief":   str,
          "agent_results":     list[dict],   # per specialist, with timings
          "per_agent_timings": dict[str, float],
        }
    """
    specialist_results = await run_specialists(
        symbol, max_concurrency=max_concurrency, on_complete=on_agent_complete
    )
    context = format_reports(specialist_results)

    portfolio = await _run_one_agent(
        ROLE_PORTFOLIO,
        symbol,
        "Review all specialist reports and produce a portfolio construction recommendation.",
        extra_context=context,
    )
    if on_agent_complete:
        on_agent_complete(portfolio)

    memo_task = "Produce the final Investment Memo."
    if extra_instructions:
        memo_task += f"\n\nAdditional instructions: {extra_instructions}"

    memo = await _run_one_agent(
        ROLE_HEAD_OF_RESEARCH,
        symbol,
        memo_task,
        extra_context=(
            context
            + "\n---\n\n## Portfolio Strategist\n\n"
            + (portfolio["output"] or f"_Unavailable: {portfolio['error']}_")
        ),
        recursion_limit=_MASTER_RECURSION_LIMIT,
        max_tokens=_MEMO_MAX_TOKENS,
    )
    if on_agent_complete:
        on_agent_complete(memo)

    all_results = specialist_results + [portfolio, memo]

    return {
        "symbol":            symbol,
        "investment_memo":   memo["output"],
        "portfolio_brief":   portfolio["output"],
        "agent_results":     specialist_results,
        "per_agent_timings": {r["agent_role"]: r["elapsed_seconds"] for r in all_results},
        "failures":          [r["agent_role"] for r in all_results if r.get("error")],
    }
