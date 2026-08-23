"""
Orchestrator — entry point for the equity research pipeline.

Delegates to the LangChain deepagents master agent (Head of Research) which
autonomously plans and delegates to its 13 specialist subagents, then
synthesises a final Investment Memo.

Usage:
    python -m equity_mcp.orchestrator --symbol AAPL
    python -m equity_mcp.orchestrator --symbol MSFT --focus "focus on growth and ESG"
    python -m equity_mcp.orchestrator --list-sessions
    python -m equity_mcp.orchestrator --last               # newest unfinished run
    python -m equity_mcp.orchestrator --last AAPL_20260801T142233

Each run gets a workspace under runs/ holding the raw FMP payloads the agents
fetched, the Python they ran over them, and one report per specialist — that is
the audit trail for every number in the memo.  The run is checkpointed to
runs/sessions.sqlite as it goes, so a crash half an hour in is resumable rather
than fatal; see session.py for what "resumable" does and does not cover.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
import time
import traceback
from datetime import date
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

from equity_mcp import progress, session, workspace


def _print_sessions(limit: int = 20) -> None:
    session.init_db()
    rows = session.list_sessions(limit)
    if not rows:
        print("No sessions recorded yet.")
        return

    print(f"\n{'SESSION':<30} {'SYMBOL':<8} {'STATUS':<15} {'AGENTS':>6}  STARTED")
    print("-" * 92)
    for row in rows:
        resumed = f" (x{row['resumed_count']})" if row["resumed_count"] else ""
        print(
            f"{row['session_id']:<30} {row['symbol']:<8} "
            f"{row['status'] + resumed:<15} {row['agents_done']:>6}  {row['started_at']}"
        )
    resumable = [r for r in rows if r["status"] in session.RESUMABLE]
    if resumable:
        print(
            f"\nResume the newest unfinished run with:\n"
            f"  python -m equity_mcp.orchestrator --last\n"
            f"or name one:  --last {resumable[0]['session_id']}\n"
        )
    else:
        print("\nNothing unfinished to resume.\n")


def _resolve_resume(requested: str, force: bool) -> dict:
    """
    Find the session ``--last`` refers to and validate that it can be resumed.

    An empty *requested* is the bare ``--last``: the newest run that stopped
    without finishing.
    """
    row = session.get(requested) if requested else session.latest_resumable()

    if row is None:
        if requested:
            raise SystemExit(
                f"No session '{requested}'. See --list-sessions."
            )
        raise SystemExit(
            "No unfinished session to resume. See --list-sessions."
        )

    if row["status"] == session.STATUS_COMPLETED and not force:
        raise SystemExit(
            f"Session {row['session_id']} already completed "
            f"({row['finished_at']}). Re-run it anyway with --force."
        )
    return row


async def _run(args: argparse.Namespace) -> dict:
    from equity_mcp.deep_agent_factory import run_research

    session.init_db()

    resuming = args.last is not None
    if resuming:
        row = _resolve_resume(args.last, args.force)
        session_id = row["session_id"]
        symbol = row["symbol"]
        focus = args.focus or row["focus"]
        run_dir = workspace.attach_run(session_id)
        session.mark_resumed(session_id)
    else:
        symbol = args.symbol.upper()
        focus = args.focus
        run_dir = workspace.set_run(symbol)
        session_id = workspace.session_id()
        session.start_session(session_id, symbol, focus, run_dir)

    output_dir = Path(args.output_dir) if args.output_dir else None
    master_copy = output_dir / f"{session_id}.md" if output_dir else None

    rep = progress.configure(session_id, run_dir, master_copy, args.verbosity)
    progress.setup_logging(args.verbosity)

    rep.banner([
        "equity-researcher  [deepagents]",
        f"Symbol    : {symbol}",
        f"Session   : {session_id}" + ("   (resuming)" if resuming else ""),
        f"Workspace : {run_dir}",
        f"State DB  : {session.state_db_path()}",
        f"Resume    : python -m equity_mcp.orchestrator --last {session_id}",
    ])
    rep.start_master(symbol, focus, resumed=resuming)

    start = time.time()
    try:
        async with session.checkpointer() as saver:
            result = await run_research(
                symbol,
                extra_instructions=focus,
                session_id=session_id,
                checkpointer=saver,
                resume=resuming,
            )
    except BaseException as exc:  # noqa: BLE001 - KeyboardInterrupt included on purpose
        # Ctrl-C is the likeliest way a half-hour run ends early, and it must
        # leave a resumable row behind rather than a session stuck at "running".
        detail = f"{type(exc).__name__}: {exc}".strip().splitlines()[0][:500]
        session.finish_session(session_id, session.STATUS_FAILED, error=detail)
        rep.line("")
        rep.banner([
            f"Run stopped: {detail}",
            f"Finished agents are on disk: {run_dir / 'reports'}",
            f"Resume with: python -m equity_mcp.orchestrator --last {session_id}",
        ])
        if not isinstance(exc, KeyboardInterrupt):
            if args.verbosity >= progress.VERBOSE:
                traceback.print_exc()
        raise

    elapsed = round(time.time() - start, 1)
    result["session_id"] = session_id
    result["date"] = date.today().isoformat()
    result["elapsed_seconds"] = elapsed
    result["workspace"] = str(run_dir)

    out_file = None
    if output_dir:
        output_dir.mkdir(parents=True, exist_ok=True)
        out_file = output_dir / f"{session_id}.json"
        # messages may not be JSON-serialisable directly; store as strings
        serialisable = {
            **result,
            "messages": [
                m.content if hasattr(m, "content") else str(m)
                for m in result.get("messages", [])
            ],
        }
        out_file.write_text(json.dumps(serialisable, indent=2, default=str), encoding="utf-8")

    session.finish_session(
        session_id,
        session.STATUS_COMPLETED,
        memo_path=str(master_copy) if master_copy else None,
    )

    summary = [f"Research complete in {elapsed}s", f"Workspace : {run_dir}"]
    if master_copy:
        summary.append(f"Memo      : {master_copy}")
    if out_file:
        summary.append(f"JSON      : {out_file}")
    rep.line("")
    rep.banner(summary)

    return result


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Multi-agent equity research pipeline"
    )
    parser.add_argument("--symbol", help="Ticker symbol, e.g. AAPL")
    parser.add_argument(
        "--last",
        nargs="?",
        const="",
        default=None,
        metavar="SESSION_ID",
        help="Resume a run. Bare --last takes the newest unfinished session.",
    )
    parser.add_argument(
        "--list-sessions",
        action="store_true",
        help="Show recorded sessions and exit",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Allow --last on a session that already completed",
    )
    parser.add_argument(
        "--focus",
        default="",
        help="Optional extra instructions for the master agent",
    )
    parser.add_argument(
        "--output-dir", default="outputs",
        help="Directory for the memo and JSON output (default: outputs/)",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true",
        help="Also log model turns and tool result previews",
    )
    parser.add_argument(
        "-q", "--quiet", action="store_true",
        help="Only banners and warnings",
    )
    args = parser.parse_args()

    if not args.list_sessions:
        if bool(args.symbol) == (args.last is not None):
            parser.error("give exactly one of --symbol or --last")

    args.verbosity = (
        progress.VERBOSE if args.verbose
        else progress.QUIET if args.quiet
        else progress.NORMAL
    )
    return args


async def _main_async(args: argparse.Namespace) -> None:
    result = await _run(args)

    memo = result.get("investment_memo") or ""
    if memo and args.verbosity > progress.QUIET:
        print("\n" + "=" * 70)
        print("INVESTMENT MEMO")
        print("=" * 70)
        print(memo)


def main() -> None:
    args = _parse_args()

    if args.list_sessions:
        _print_sessions()
        return

    try:
        asyncio.run(_main_async(args))
    except KeyboardInterrupt:
        # _run has already marked the session failed and printed how to resume.
        sys.exit(130)
    except SystemExit:
        raise
    except Exception as exc:  # noqa: BLE001 - top level, message already shown
        print(f"\nRun failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
