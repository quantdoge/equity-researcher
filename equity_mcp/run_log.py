"""
Per-run activity log and incremental report dump.

A research run takes tens of minutes and, until this module existed, produced
nothing on disk until every stage had succeeded.  A timeout at the memo threw
away eleven specialist reports that had been finished for half an hour, and a
run whose stdout went somewhere unread left no trace that it had happened.

So each run gets a directory::

    runs/<SYMBOL>_<TIMESTAMP>/
        run.log          # timestamped events, appended as they happen
        reports/         # one <role>.md per agent, written the moment it lands
        result.json      # the full result dict, at the end

The reports are the point.  They are written from the ``on_agent_complete``
callback ``run_research`` already accepts, so a run that dies at step three
still leaves everything steps one and two produced.

Deliberately *not* a copy of the dev branch's progress.py: live narration of
tool calls needs an AgentMiddleware attached to every agent spec, whereas
durability needs only the callback that already exists.  This is the half that
earns its keep without touching the agent wiring.

Nothing here may raise.  Logging exists to make failures survivable, so a full
disk or a read-only path degrades to a one-line warning rather than taking down
the run it was meant to record.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

_STAMP_FORMAT = "%Y%m%dT%H%M%S"


def stamp() -> str:
    """Run identifier: the format the existing runs/ and outputs/ names use."""
    return datetime.now().strftime(_STAMP_FORMAT)


class RunLog:
    """
    The on-disk record of one run.

    An instance rather than a module-level global: the dev branch needs a
    process-global run directory because its `fmp_call` and `run_python` are
    plain MCP tool functions with no run context to thread an id through.
    Nothing on this branch has that problem, so the orchestrator just holds the
    instance and passes it where it is needed.
    """

    def __init__(self, root: Path | str, symbol: str, run_stamp: str | None = None) -> None:
        self.stamp = run_stamp or stamp()
        self.name = f"{symbol.upper()}_{self.stamp}"
        self.dir = Path(root) / self.name
        self.reports_dir = self.dir / "reports"
        self._warned = False

        try:
            self.reports_dir.mkdir(parents=True, exist_ok=True)
        except OSError as exc:
            self._warn(f"could not create run directory {self.dir}: {exc}")

    # ── Events ────────────────────────────────────────────────────────────────

    def event(self, message: str) -> None:
        """Append one timestamped line to run.log."""
        line = f"{datetime.now().isoformat(timespec='seconds')}  {message}\n"
        try:
            with (self.dir / "run.log").open("a", encoding="utf-8") as fh:
                fh.write(line)
        except OSError as exc:
            self._warn(f"could not write run.log: {exc}")

    # ── Artifacts ─────────────────────────────────────────────────────────────

    def report(self, result: dict[str, Any]) -> None:
        """
        Persist one agent's report and record that it finished.

        Takes the dict `_run_one_agent` returns, so callers can hand the
        on_agent_complete payload straight through.
        """
        role = result.get("agent_role", "unknown")
        elapsed = result.get("elapsed_seconds", 0)
        error = result.get("error")

        if error:
            self.event(f"FAIL   {role}  {elapsed}s  {error}")
        else:
            self.event(f"DONE   {role}  {elapsed}s")

        header = [f"# {role.replace('_', ' ').title()}", ""]
        header.append(f"- Symbol: {result.get('symbol', '')}")
        header.append(f"- Elapsed: {elapsed}s")
        if error:
            header.append(f"- Error: {error}")
        header += ["", "---", ""]

        body = result.get("output") or (f"_No output. {error}_" if error else "_No output._")
        self._write(self.reports_dir / f"{role}.md", "\n".join(header) + body + "\n")

    def finish(self, result: dict[str, Any]) -> None:
        """Write the full result dict into the run directory."""
        try:
            payload = json.dumps(result, indent=2, default=str)
        except (TypeError, ValueError) as exc:
            self._warn(f"could not serialise result: {exc}")
            return
        self._write(self.dir / "result.json", payload)

    # ── Internals ─────────────────────────────────────────────────────────────

    def _write(self, path: Path, text: str) -> None:
        # utf-8 explicitly: agent output routinely carries em-dashes and
        # currency symbols that the Windows default (cp1252) cannot encode,
        # and a UnicodeEncodeError here would lose the report entirely.
        try:
            path.write_text(text, encoding="utf-8")
        except OSError as exc:
            self._warn(f"could not write {path.name}: {exc}")

    def _warn(self, message: str) -> None:
        """Warn once per run — a broken log should not also spam the console."""
        if self._warned:
            return
        self._warned = True
        print(f"  [run-log] {message}", file=sys.stderr, flush=True)
