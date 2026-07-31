"""
Orchestrator — entry point for the equity research pipeline.

Delegates to the LangChain deepagents master agent (Head of Research) which
autonomously plans and delegates to its 13 specialist subagents, then
synthesises a final Investment Memo.

Usage:
    python -m equity_mcp.orchestrator --symbol AAPL
    python -m equity_mcp.orchestrator --symbol MSFT --focus "focus on growth and ESG"
    python -m equity_mcp.orchestrator --symbol TSLA --output-dir outputs/

Each run gets a workspace under runs/ holding the raw FMP payloads the agents
fetched and the Python they ran over them — that is the audit trail for every
number in the memo.
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

from equity_mcp import workspace


async def _run(symbol: str, focus: str, output_dir: Path | None) -> dict:
    from equity_mcp.deep_agent_factory import run_research

    run_dir = workspace.set_run(symbol)

    print(f"\n{'='*60}")
    print(f"  equity-researcher  [deepagents]")
    print(f"  Symbol    : {symbol}")
    print(f"  Workspace : {run_dir}")
    print(f"{'='*60}\n")

    start = time.time()
    result = await run_research(symbol, extra_instructions=focus)
    elapsed = round(time.time() - start, 1)

    result["date"] = date.today().isoformat()
    result["elapsed_seconds"] = elapsed
    result["workspace"] = str(run_dir)

    print(f"\n{'='*60}")
    print(f"  Research complete in {elapsed}s")
    print(f"  Workspace: {run_dir}")
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


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Multi-agent equity research pipeline"
    )
    parser.add_argument("--symbol", required=True, help="Ticker symbol, e.g. AAPL")
    parser.add_argument(
        "--focus",
        default="",
        help="Optional extra instructions for the master agent",
    )
    parser.add_argument(
        "--output-dir", default="outputs",
        help="Directory to save JSON output (default: outputs/)",
    )
    return parser.parse_args()


async def _main_async(args: argparse.Namespace) -> None:
    result = await _run(args.symbol.upper(), args.focus, Path(args.output_dir))

    print("\n" + "=" * 70)
    print("INVESTMENT MEMO")
    print("=" * 70)
    print(result["investment_memo"])


def main() -> None:
    args = _parse_args()
    asyncio.run(_main_async(args))


if __name__ == "__main__":
    main()
