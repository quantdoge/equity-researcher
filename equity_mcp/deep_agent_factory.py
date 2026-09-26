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
import sys
import time
from pathlib import Path
from typing import Any, Callable

from deepagents import create_deep_agent
from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent

from equity_mcp.langchain_bridge import get_langchain_tools_for_role
from equity_mcp.roles import (
    ALL_ROLES,
    ROLE_HEAD_OF_RESEARCH,
    ROLE_PORTFOLIO,
    chat_model_for_role,
)

load_dotenv()

# Which OpenRouter model each agent runs on lives in roles.py — DEFAULT_MODEL
# plus the per-role overrides in AGENT_MODELS — so one specialist can be
# repointed at a different model without touching this file.

# Set explicitly rather than left to the provider default, which is the full
# output window — enough for a single runaway specialist to spend minutes
# generating, and large enough to risk an HTTP timeout.
_SPECIALIST_MAX_TOKENS = 8096
_MEMO_MAX_TOKENS       = 16000

# LangGraph super-step ceilings.  A specialist is one tool loop; the master no
# longer delegates, so it needs far fewer steps than the default 25.
_SPECIALIST_RECURSION_LIMIT = 30
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
    # encoding is explicit because read_text() defaults to the locale's, which on
    # Windows is cp1252: every em dash and curly quote in these prompts then
    # reaches the model as mojibake ("â€”").  It round-trips invisibly through a
    # UTF-8 terminal, so it will not show up in a print.
    p = _PROMPTS / f"{role}.md"
    return p.read_text(encoding="utf-8") if p.exists() else (
        f"You are the {role.replace('_', ' ').title()} agent in an elite equity research team."
    )


# The ceilings above are enforced on the graph, not communicated to the model: an
# agent's context is its role prompt plus "Symbol / Task", so it cannot pace
# itself and gets no warning as it approaches one.  Crossing either the step or
# the time ceiling raises out of ainvoke into _run_one_agent's except, which
# returns an *empty* report — nine minutes of gathered data discarded.  So tell
# each agent what it is working within, rendered from the same numbers the
# runtime is given.
_BUDGET_TEMPLATE = _PROMPTS / "_execution_budget.md"

# create_deep_agent injects planning and virtual-filesystem tools, which spend
# rounds from the master's budget like any other tool call — and its budget is
# the smaller one.
_MASTER_BUDGET_NOTE = """
Your planning and filesystem tools draw on this same budget — one `write_todos`
plus two reads is nearly half of it. Every specialist report is already in your
context; you are synthesising, not gathering. Prefer writing directly.
"""


def _budget_block(
    recursion_limit: int,
    timeout_s: float,
    max_tokens: int,
    is_master: bool = False,
) -> str:
    """
    Render the execution-budget block for the ceilings this agent actually runs under.

    A react agent alternates model node / tool node, so a recursion limit of R
    super-steps allows T rounds of tool calls where 2T + 1 <= R (the +1 being the
    final turn that writes the report).  30 -> 14 rounds, 15 -> 7.

    Degrades to "" on a missing or unformattable template, with a warning: like
    _load_prompt's own fallback, a prompt addition must not be the thing that
    fails a run.  An unescaped "{" added to the template later would otherwise
    raise here and take down every agent build.
    """
    if not _BUDGET_TEMPLATE.exists():
        return ""

    # Advertise 75% of the real ceilings.  An agent that paces itself to the
    # true limit finishes *at* it, which is the one place a run has nothing
    # left for the report; quoting a quarter less buys that margin back.
    recursion_limit = max(3, int(recursion_limit * 0.75))
    timeout_s = timeout_s * 0.75

    tool_rounds = max(1, (recursion_limit - 1) // 2)
    try:
        block = _BUDGET_TEMPLATE.read_text(encoding="utf-8").format(
            tool_rounds=tool_rounds,
            timeout_s=timeout_s,
            max_tokens=max_tokens,
            # Leave headroom so the report is written *before* the last round, not
            # in the round that trips the limit.
            write_by=max(1, tool_rounds - 2),
        )
    except (KeyError, IndexError, ValueError) as exc:
        print(
            f"warning: {_BUDGET_TEMPLATE.name} could not be rendered "
            f"({type(exc).__name__}: {exc}); agents run without a budget block. "
            "Literal braces in that file must be doubled.",
            file=sys.stderr,
            flush=True,
        )
        return ""
    if is_master:
        block += _MASTER_BUDGET_NOTE
    return f"\n\n{block}"


def _build_model(role: str, max_tokens: int):
    """Build the chat model *role* runs on, per the OpenRouter config in roles.py."""
    return chat_model_for_role(role, max_tokens=max_tokens)


def _final_text(result: dict[str, Any]) -> str:
    messages = result.get("messages", [])
    if not messages:
        return ""
    last = messages[-1]
    content = last.content if hasattr(last, "content") else str(last)
    if isinstance(content, list):
        # Structured content blocks — keep the text parts.
        return "\n".join(
            b.get("text", "") if isinstance(b, dict) else str(b) for b in content
        ).strip()
    return str(content).strip()


async def build_specialist_agent(
    role: str,
    max_tokens: int = _SPECIALIST_MAX_TOKENS,
    recursion_limit: int = _SPECIALIST_RECURSION_LIMIT,
):
    """
    Build one standalone research agent for *role*, holding only that role's tools.

    Uses a plain react agent rather than create_deep_agent: a leaf researcher
    has nothing to delegate to and no use for deepagents' injected planning and
    virtual-filesystem tools, which would only add per-turn tokens and turns.

    *recursion_limit* is not enforced here — the caller passes it to ainvoke — but
    it is what the budget block quotes, so both must come from one value.
    """
    tools = await get_langchain_tools_for_role(role)
    return create_react_agent(
        _build_model(role, max_tokens),
        tools,
        prompt=_load_prompt(role) + _budget_block(recursion_limit, _AGENT_TIMEOUT_S, max_tokens),
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
        # Both builders are handed the same recursion_limit that goes into the
        # ainvoke config below, so the budget the agent is told is the budget it
        # is actually held to.
        if role == ROLE_HEAD_OF_RESEARCH:
            agent = await build_head_agent(
                max_tokens=max_tokens, recursion_limit=recursion_limit
            )
        else:
            agent = await build_specialist_agent(
                role, max_tokens=max_tokens, recursion_limit=recursion_limit
            )

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


async def build_head_agent(
    max_tokens: int = _MEMO_MAX_TOKENS,
    recursion_limit: int = _MASTER_RECURSION_LIMIT,
):
    """
    Build the master Head of Research agent.

    Keeps create_deep_agent — its planning tools still earn their place when
    structuring a long memo — but with no subagents: delegation is now the
    orchestrator's job, done concurrently.
    """
    master_tools = await get_langchain_tools_for_role(ROLE_HEAD_OF_RESEARCH)
    return create_deep_agent(
        model=_build_model(ROLE_HEAD_OF_RESEARCH, max_tokens),
        system_prompt=(
            _load_prompt(ROLE_HEAD_OF_RESEARCH)
            + _budget_block(recursion_limit, _AGENT_TIMEOUT_S, max_tokens, is_master=True)
        ),
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
    roles: list[str] | None = None,
    skip_synthesis: bool = False,
) -> dict[str, Any]:
    """
    Run the full equity research pipeline for a ticker symbol.

    Three steps on the critical path:
      1. the 11 research specialists, concurrently
      2. the portfolio strategist, over their reports
      3. the Head of Research, over everything, producing the Investment Memo

    *roles* narrows step 1 to a subset of RESEARCH_ROLES; *skip_synthesis* stops
    after it.  Both exist for smoke-testing — a subset of two specialists with no
    synthesis is two agent runs instead of thirteen — and are not meant for a
    real research run, where the memo is the product.

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
        symbol, roles=roles, max_concurrency=max_concurrency, on_complete=on_agent_complete
    )
    context = format_reports(specialist_results)

    if skip_synthesis:
        return {
            "symbol":            symbol,
            "investment_memo":   "",
            "portfolio_brief":   "",
            "agent_results":     specialist_results,
            "per_agent_timings": {
                r["agent_role"]: r["elapsed_seconds"] for r in specialist_results
            },
            "failures":          [r["agent_role"] for r in specialist_results if r.get("error")],
            "skipped_synthesis": True,
        }

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
