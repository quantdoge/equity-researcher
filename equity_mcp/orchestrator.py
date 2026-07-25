"""
Orchestrator — entry point for the equity research pipeline.

Delegates to the LangChain deepagents master agent (Head of Research) which
autonomously plans and delegates to its 12 specialist subagents, then
synthesises a final Investment Memo.

Usage:
    python -m equity_mcp.orchestrator --symbol AAPL
    python -m equity_mcp.orchestrator --symbol MSFT --focus "focus on growth and ESG"
    python -m equity_mcp.orchestrator --symbol TSLA --output-dir outputs/

The previous hard-coded 6-stage pipeline (agent_factory.py) is preserved as a
fallback; run with --legacy to use it instead.
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


# ── deepagents pipeline (default) ─────────────────────────────────────────────


async def _run_deepagents(symbol: str, focus: str, output_dir: Path | None) -> dict:
    from equity_mcp.deep_agent_factory import run_research

    print(f"\n{'='*60}")
    print(f"  equity-researcher  [deepagents]")
    print(f"  Symbol : {symbol}")
    print(f"{'='*60}\n")

    start = time.time()
    result = await run_research(symbol, extra_instructions=focus)
    elapsed = round(time.time() - start, 1)

    result["date"] = date.today().isoformat()
    result["elapsed_seconds"] = elapsed

    print(f"\n{'='*60}")
    print(f"  Research complete in {elapsed}s")
    print(f"{'='*60}\n")

    if output_dir:
        output_dir.mkdir(parents=True, exist_ok=True)
        out_file = output_dir / f"{symbol}_{date.today().isoformat()}.json"
        # messages may not be JSON-serialisable directly; store as strings
        serialisable = {
            **result,
            "messages": [
                m.content if hasattr(m, "content") else str(m)
                for m in result.get("messages", [])
            ],
        }
        out_file.write_text(json.dumps(serialisable, indent=2, default=str))
        print(f"Output saved → {out_file}\n")

    return result


# ── Legacy pipeline (hard-coded stages) ───────────────────────────────────────


async def _run_legacy(symbol: str, agents: list[str] | None, output_dir: Path | None) -> dict:
    from equity_mcp.agent_factory import run_agents_parallel, run_agent
    from equity_mcp.roles import (
        ROLE_ALT_DATA, ROLE_ESG, ROLE_FIN_RISK, ROLE_GEO_LEGAL,
        ROLE_GROWTH, ROLE_HEAD_OF_RESEARCH, ROLE_MACRO, ROLE_NONFIN_RISK,
        ROLE_PORTFOLIO, ROLE_QUANT, ROLE_SECTOR, ROLE_SHORT, ROLE_VALUE,
    )

    PIPELINE_STAGES: list[tuple[str, list[str]]] = [
        ("Stage 1 — Fast signals",    [ROLE_ALT_DATA, ROLE_QUANT]),
        ("Stage 2 — Context layer",   [ROLE_SECTOR, ROLE_GEO_LEGAL, ROLE_MACRO]),
        ("Stage 3 — Company analysis",[ROLE_VALUE, ROLE_GROWTH, ROLE_SHORT, ROLE_ESG]),
        ("Stage 4 — Risk overlay",    [ROLE_FIN_RISK, ROLE_NONFIN_RISK]),
    ]
    DEFAULT_TASKS: dict[str, str] = {
        ROLE_ALT_DATA:    "Gather and interpret all available alternative data signals.",
        ROLE_QUANT:       "Compute all quantitative factor scores, alpha/beta, and Sharpe/Sortino ratios.",
        ROLE_SECTOR:      "Analyse the sector, tailwinds/headwinds, and peer benchmarking.",
        ROLE_GEO_LEGAL:   "Identify geographic exposures, geopolitical risks, and regulatory risk.",
        ROLE_MACRO:       "Assess the macroeconomic environment and its impact on this company.",
        ROLE_VALUE:       "Conduct a thorough value investment analysis.",
        ROLE_GROWTH:      "Conduct a thorough growth investment analysis.",
        ROLE_SHORT:       "Conduct a forensic short-seller analysis.",
        ROLE_ESG:         "Conduct a full ESG analysis.",
        ROLE_FIN_RISK:    "Conduct a complete financial risk assessment.",
        ROLE_NONFIN_RISK: "Conduct a complete non-financial risk assessment.",
    }

    stages = PIPELINE_STAGES
    if agents:
        requested = set(agents)
        stages = [
            (name, [r for r in roles if r in requested or r.replace("_", "") in requested])
            for name, roles in stages
        ]
        stages = [(n, r) for n, r in stages if r]

    all_results: list[dict] = []
    start = time.time()

    for stage_name, roles in stages:
        print(f"\n{'='*60}\n  {stage_name}\n{'='*60}")
        stage_results = await run_agents_parallel(
            agent_roles=roles, symbol=symbol, task_map=DEFAULT_TASKS,
        )
        all_results.extend(stage_results)
        for r in stage_results:
            print(f"  ✓ {r['agent_role'].replace('_',' ').title()} — {r['tool_calls']} tool calls")

    def _format(results):
        return "\n---\n\n".join(
            f"## {r['agent_role'].replace('_',' ').title()}\n\n{r['output']}"
            for r in results
        )

    context = _format(all_results)

    portfolio_result = await run_agent(
        ROLE_PORTFOLIO, symbol,
        "Review all specialist reports and produce a portfolio construction recommendation.",
        extra_context=context,
    )
    memo_result = await run_agent(
        ROLE_HEAD_OF_RESEARCH, symbol,
        "Produce the final Investment Memo.",
        extra_context=context + "\n\n---\n\n## Portfolio Strategist\n\n" + portfolio_result["output"],
    )

    elapsed = round(time.time() - start, 1)
    output = {
        "symbol": symbol,
        "date": date.today().isoformat(),
        "elapsed_seconds": elapsed,
        "agent_results": all_results,
        "portfolio_brief": portfolio_result["output"],
        "investment_memo": memo_result["output"],
    }

    if output_dir:
        output_dir.mkdir(parents=True, exist_ok=True)
        out_file = output_dir / f"{symbol}_{date.today().isoformat()}_legacy.json"
        out_file.write_text(json.dumps(output, indent=2, default=str))
        print(f"\nOutput saved → {out_file}")

    return output


# ── CLI ───────────────────────────────────────────────────────────────────────


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Equity research pipeline — deepagents (default) or legacy staged pipeline"
    )
    parser.add_argument("--symbol", required=True, help="Ticker symbol, e.g. AAPL")
    parser.add_argument(
        "--focus",
        default="",
        help="Optional extra instructions for the master agent (deepagents mode only)",
    )
    parser.add_argument(
        "--output-dir", default="outputs",
        help="Directory to save JSON output (default: outputs/)",
    )
    parser.add_argument(
        "--legacy", action="store_true",
        help="Use the legacy hard-coded staged pipeline instead of deepagents",
    )
    parser.add_argument(
        "--agents", nargs="*",
        help="(Legacy mode only) Subset of agent roles to run",
    )
    return parser.parse_args()


async def _main_async(args: argparse.Namespace) -> None:
    symbol     = args.symbol.upper()
    output_dir = Path(args.output_dir)

    if args.legacy:
        result = await _run_legacy(symbol, args.agents, output_dir)
    else:
        result = await _run_deepagents(symbol, args.focus, output_dir)

    print("\n" + "=" * 70)
    print("INVESTMENT MEMO")
    print("=" * 70)
    print(result["investment_memo"])


def main() -> None:
    args = _parse_args()
    asyncio.run(_main_async(args))


if __name__ == "__main__":
    main()
