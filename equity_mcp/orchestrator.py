"""
Orchestrator — Head of Research coordination loop.

Runs all specialist agents in the correct pipeline order, collects their
outputs, then runs the Head of Research and Portfolio Strategist to produce
the final investment memo.

Usage:
    python -m equity_mcp.orchestrator --symbol AAPL
    python -m equity_mcp.orchestrator --symbol AAPL --agents value quant fin_risk
"""

from __future__ import annotations

import argparse
import asyncio
import json
import time
from datetime import date
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

from equity_mcp.agent_factory import run_agent, run_agents_parallel
from equity_mcp.roles import (
    ROLE_ALT_DATA,
    ROLE_ESG,
    ROLE_FIN_RISK,
    ROLE_GEO_LEGAL,
    ROLE_GROWTH,
    ROLE_HEAD_OF_RESEARCH,
    ROLE_MACRO,
    ROLE_NONFIN_RISK,
    ROLE_PORTFOLIO,
    ROLE_QUANT,
    ROLE_SECTOR,
    ROLE_SHORT,
    ROLE_VALUE,
)

# ── Pipeline stage definitions ────────────────────────────────────────────────
# Agents within the same stage run in parallel; stages run sequentially.

PIPELINE_STAGES: list[tuple[str, list[str]]] = [
    (
        "Stage 1 — Fast signals",
        [ROLE_ALT_DATA, ROLE_QUANT],
    ),
    (
        "Stage 2 — Context layer",
        [ROLE_SECTOR, ROLE_GEO_LEGAL, ROLE_MACRO],
    ),
    (
        "Stage 3 — Company analysis",
        [ROLE_VALUE, ROLE_GROWTH, ROLE_SHORT, ROLE_ESG],
    ),
    (
        "Stage 4 — Risk overlay",
        [ROLE_FIN_RISK, ROLE_NONFIN_RISK],
    ),
]

DEFAULT_TASKS: dict[str, str] = {
    ROLE_ALT_DATA:   "Gather and interpret all available alternative data signals for this company. Focus on Google Trends, job postings, patent trends, news sentiment, and earnings surprise history.",
    ROLE_QUANT:      "Compute all quantitative factor scores (momentum, value, quality, low-vol, earnings revision), alpha/beta, and Sharpe/Sortino ratios. Rank the stock within its sector.",
    ROLE_SECTOR:     "Analyse the sector this company operates in. Cover sector dynamics, tailwinds/headwinds, and peer benchmarking on revenue growth and margins.",
    ROLE_GEO_LEGAL:  "Identify all geographic exposures, geopolitical risks, active litigation, and regulatory risks for this company.",
    ROLE_MACRO:      "Assess the current macroeconomic environment and its specific impact on this company's business model, valuation, and risk profile.",
    ROLE_VALUE:      "Conduct a thorough value investment analysis. Assess the economic moat, financial quality, intrinsic value, and management quality.",
    ROLE_GROWTH:     "Conduct a thorough growth investment analysis. Assess the TAM, revenue growth trajectory, upcoming catalysts, and analyst estimate momentum.",
    ROLE_SHORT:      "Conduct a forensic short-seller analysis. Assess earnings quality, run the Beneish M-Score, identify accounting red flags, and evaluate the bear case.",
    ROLE_ESG:        "Conduct a full ESG analysis. Assess material E, S, and G factors, controversies, governance quality, and regulatory ESG exposure.",
    ROLE_FIN_RISK:   "Conduct a complete financial risk assessment covering credit risk, liquidity risk, and market risk. Compute Altman Z-Score, Piotroski F-Score, and VaR.",
    ROLE_NONFIN_RISK: "Conduct a complete non-financial risk assessment covering governance, regulatory actions, insider activity, operational risks, and reputational risks.",
}


def _format_agent_outputs(results: list[dict]) -> str:
    """Format all agent outputs into a structured context block for the Head of Research."""
    sections = []
    for r in results:
        role = r["agent_role"].replace("_", " ").title()
        sections.append(f"## {role}\n\n{r['output']}\n")
    return "\n---\n\n".join(sections)


async def run_full_pipeline(
    symbol: str,
    stages: list[tuple[str, list[str]]] | None = None,
    tasks: dict[str, str] | None = None,
    output_dir: Path | None = None,
) -> dict:
    """
    Execute the full multi-agent research pipeline for a symbol.

    Returns a dict with:
        - symbol
        - date
        - agent_results: list of per-agent outputs
        - portfolio_brief: portfolio strategist output
        - investment_memo: head of research final memo
    """
    if stages is None:
        stages = PIPELINE_STAGES
    if tasks is None:
        tasks = DEFAULT_TASKS

    all_results: list[dict] = []
    total_start = time.time()

    # Run pipeline stages sequentially; agents within each stage run in parallel
    for stage_name, roles in stages:
        print(f"\n{'='*60}")
        print(f"  {stage_name}")
        print(f"  Agents: {', '.join(r.replace('_', ' ') for r in roles)}")
        print(f"{'='*60}")
        stage_start = time.time()

        stage_results = await run_agents_parallel(
            agent_roles=roles,
            symbol=symbol,
            task_map=tasks,
        )
        all_results.extend(stage_results)

        for r in stage_results:
            role_label = r["agent_role"].replace("_", " ").title()
            print(f"  ✓ {role_label} — {r['tool_calls']} tool calls")

        print(f"  Stage time: {time.time() - stage_start:.1f}s")

    # Aggregate context for synthesis agents
    context = _format_agent_outputs(all_results)

    # Portfolio Strategist synthesis
    print(f"\n{'='*60}")
    print("  Stage 5 — Portfolio Strategist synthesis")
    print(f"{'='*60}")
    portfolio_result = await run_agent(
        agent_role=ROLE_PORTFOLIO,
        symbol=symbol,
        task=(
            "Review all specialist agent reports below and produce a portfolio "
            "construction recommendation with position sizing, risk management rules, "
            "and a final action (Initiate / Add / Hold / Reduce / Exit / Pass)."
        ),
        extra_context=context,
    )
    print(f"  ✓ Portfolio Strategist — {portfolio_result['tool_calls']} tool calls")

    # Head of Research final memo
    print(f"\n{'='*60}")
    print("  Stage 6 — Head of Research final memo")
    print(f"{'='*60}")
    full_context = context + "\n\n---\n\n## Portfolio Strategist\n\n" + portfolio_result["output"]
    memo_result = await run_agent(
        agent_role=ROLE_HEAD_OF_RESEARCH,
        symbol=symbol,
        task=(
            "Review all specialist and portfolio agent reports below. "
            "Produce the final Investment Memo as specified in your instructions."
        ),
        extra_context=full_context,
    )
    print(f"  ✓ Head of Research — {memo_result['tool_calls']} tool calls")

    total_time = time.time() - total_start
    print(f"\n{'='*60}")
    print(f"  Pipeline complete in {total_time:.1f}s")
    print(f"{'='*60}\n")

    output = {
        "symbol": symbol,
        "date": date.today().isoformat(),
        "total_elapsed_seconds": round(total_time, 1),
        "agent_results": all_results,
        "portfolio_brief": portfolio_result["output"],
        "investment_memo": memo_result["output"],
    }

    # Optionally persist outputs
    if output_dir:
        output_dir.mkdir(parents=True, exist_ok=True)
        out_file = output_dir / f"{symbol}_{date.today().isoformat()}.json"
        out_file.write_text(json.dumps(output, indent=2, default=str))
        print(f"Output saved to {out_file}")

    return output


# ── CLI entry point ───────────────────────────────────────────────────────────


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the equity research pipeline")
    parser.add_argument("--symbol", required=True, help="Stock ticker symbol (e.g. AAPL)")
    parser.add_argument(
        "--agents",
        nargs="*",
        help="Subset of agent roles to run (default: all). E.g. --agents value quant fin_risk",
    )
    parser.add_argument(
        "--output-dir",
        default="outputs",
        help="Directory to save JSON output (default: outputs/)",
    )
    return parser.parse_args()


async def _main_async(args: argparse.Namespace) -> None:
    symbol = args.symbol.upper()

    # Build stage list, optionally filtered to requested agents
    if args.agents:
        requested = set(args.agents)
        stages = [
            (name, [r for r in roles if r in requested or r.replace("_", "") in requested])
            for name, roles in PIPELINE_STAGES
        ]
        stages = [(n, r) for n, r in stages if r]  # drop empty stages
    else:
        stages = None  # run full pipeline

    result = await run_full_pipeline(
        symbol=symbol,
        stages=stages,
        output_dir=Path(args.output_dir),
    )

    print("\n" + "=" * 70)
    print("INVESTMENT MEMO")
    print("=" * 70)
    print(result["investment_memo"])


def main() -> None:
    args = _parse_args()
    asyncio.run(_main_async(args))


if __name__ == "__main__":
    main()
