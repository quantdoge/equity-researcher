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


def _resolve_roles(requested: list[str] | None, valid: list[str]) -> list[str] | None:
    """
    Map CLI role tokens onto canonical role names, accepting unambiguous prefixes.

    So `--agents macro esg` reaches macro_researcher and esg_analyst.  An
    unmatched or ambiguous token is fatal: silently dropping it would run a
    smaller pipeline than asked for, and running zero specialists would look
    like every agent had failed.
    """
    if not requested:
        return None

    resolved: list[str] = []
    for token in requested:
        key = token.lower().replace("-", "_")
        matches = [r for r in valid if r == key] or [r for r in valid if r.startswith(key)]
        if not matches:
            raise SystemExit(
                f"Unknown agent '{token}'. Valid agents: {', '.join(valid)}"
            )
        if len(matches) > 1:
            raise SystemExit(
                f"Ambiguous agent '{token}' — matches {', '.join(matches)}"
            )
        if matches[0] not in resolved:
            resolved.append(matches[0])

    return resolved


async def _run_deepagents(
    symbol: str,
    focus: str,
    output_dir: Path | None,
    max_concurrency: int,
    timeout: float | None,
    agents: list[str] | None = None,
    skip_synthesis: bool = False,
    runs_dir: Path | None = None,
) -> dict:
    from equity_mcp.deep_agent_factory import RESEARCH_ROLES, run_research
    from equity_mcp.run_log import RunLog

    roles = _resolve_roles(agents, RESEARCH_ROLES)
    n_specialists = len(roles) if roles else len(RESEARCH_ROLES)

    run_log = RunLog(runs_dir or Path("runs"), symbol)

    # flush on every print: stdout is block-buffered the moment it is piped or
    # redirected, which is exactly when someone is watching a half-hour run and
    # would otherwise see nothing at all until it ends.
    print(f"\n{'='*60}", flush=True)
    print(f"  equity-researcher  [deepagents]", flush=True)
    print(f"  Symbol : {symbol}", flush=True)
    print(f"  Fan-out: {n_specialists} specialists, {max_concurrency} at a time", flush=True)
    if roles:
        print(f"  Agents : {', '.join(roles)}", flush=True)
    if skip_synthesis:
        print(f"  Synth  : skipped (no portfolio brief, no memo)", flush=True)
    print(f"  Log    : {run_log.dir}", flush=True)
    print(f"{'='*60}\n", flush=True)

    run_log.event(
        f"START  symbol={symbol} agents={','.join(roles) if roles else 'all'} "
        f"concurrency={max_concurrency} skip_synthesis={skip_synthesis} timeout={timeout}"
    )

    start = time.time()

    def _report(r: dict) -> None:
        name = r["agent_role"].replace("_", " ").title()
        mark = "✗" if r.get("error") else "✓"
        line = f"  [{time.time()-start:6.1f}s] {mark} {name:24s} {r['elapsed_seconds']:>6.1f}s"
        if r.get("error"):
            line += f"  — {r['error'][:100]}"
        print(line, flush=True)
        run_log.report(r)

    coro = run_research(
        symbol,
        extra_instructions=focus,
        max_concurrency=max_concurrency,
        on_agent_complete=_report,
        roles=roles,
        skip_synthesis=skip_synthesis,
    )

    # The finally is what makes a timeout or a Ctrl-C legible afterwards: the
    # reports are already on disk by then, and without this the log would simply
    # stop mid-run with no indication of why.
    try:
        result = await (asyncio.wait_for(coro, timeout=timeout) if timeout else coro)
    except asyncio.TimeoutError:
        run_log.event(f"ABORT  timed out after {timeout}s")
        raise
    except BaseException as exc:
        run_log.event(f"ABORT  {type(exc).__name__}: {exc}")
        raise

    elapsed = round(time.time() - start, 1)

    result["date"] = date.today().isoformat()
    result["elapsed_seconds"] = elapsed
    result["run_id"] = run_log.name

    run_log.event(
        f"END    elapsed={elapsed}s failures={','.join(result.get('failures') or []) or 'none'}"
    )
    run_log.finish(result)

    print(f"\n{'='*60}", flush=True)
    print(f"  Research complete in {elapsed}s", flush=True)
    if result.get("failures"):
        print(f"  Failed agents: {', '.join(result['failures'])}", flush=True)
    print(f"  Run log: {run_log.dir}", flush=True)
    print(f"{'='*60}\n", flush=True)

    if output_dir:
        output_dir.mkdir(parents=True, exist_ok=True)
        # Timestamped, not date-only: two runs of the same ticker on one day
        # used to overwrite each other's JSON.  Sharing the run's stamp also
        # ties this file to its run directory.
        out_file = output_dir / f"{symbol}_{run_log.stamp}.json"
        out_file.write_text(json.dumps(result, indent=2, default=str), encoding="utf-8")
        print(f"Output saved → {out_file}\n", flush=True)

    return result


# ── Legacy pipeline (Anthropic SDK direct) ────────────────────────────────────


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
        out_file.write_text(json.dumps(output, indent=2, default=str), encoding="utf-8")
        print(f"\nOutput saved → {out_file}")

    return output


# ── CLI ───────────────────────────────────────────────────────────────────────


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Equity research pipeline — deepagents (default) or legacy Anthropic SDK"
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
        "--runs-dir", default="runs",
        help="Directory for per-run logs and incremental agent reports (default: runs/)",
    )
    parser.add_argument(
        "--legacy", action="store_true",
        help="Use the legacy Anthropic-SDK pipeline instead of deepagents",
    )
    parser.add_argument(
        "--agents", nargs="*",
        help="Subset of agent roles to run; unambiguous prefixes accepted (e.g. macro esg)",
    )
    parser.add_argument(
        "--skip-synthesis", action="store_true",
        help="Stop after the specialists — no portfolio brief, no memo. For smoke tests.",
    )
    parser.add_argument(
        "--max-concurrency", type=int, default=6,
        help="Specialists to run at once (default: 6). Lower this if you hit API rate limits.",
    )
    parser.add_argument(
        "--timeout", type=float, default=None,
        help="Total wall-clock ceiling in seconds for the whole run (default: none)",
    )
    return parser.parse_args()


async def _main_async(args: argparse.Namespace) -> None:
    symbol     = args.symbol.upper()
    output_dir = Path(args.output_dir)

    if args.legacy:
        result = await _run_legacy(symbol, args.agents, output_dir)
    else:
        result = await _run_deepagents(
            symbol, args.focus, output_dir, args.max_concurrency, args.timeout,
            agents=args.agents, skip_synthesis=args.skip_synthesis,
            runs_dir=Path(args.runs_dir),
        )

    if result.get("skipped_synthesis"):
        # Nothing was synthesised, so print the specialist reports instead —
        # otherwise a --skip-synthesis run ends with an empty banner.
        for r in result["agent_results"]:
            print("\n" + "=" * 70)
            print(r["agent_role"].replace("_", " ").upper())
            print("=" * 70)
            print(r["output"] or f"_Unavailable: {r['error']}_")
        return

    print("\n" + "=" * 70)
    print("INVESTMENT MEMO")
    print("=" * 70)
    print(result["investment_memo"])


def main() -> None:
    args = _parse_args()
    asyncio.run(_main_async(args))


if __name__ == "__main__":
    main()
