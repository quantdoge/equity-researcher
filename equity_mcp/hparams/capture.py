"""
Capture the config a research run starts with, into runs/<id>/config.json.

Called once by the orchestrator, after START and before the fan-out. It must
take place before ``run_research``: the snapshot briefly stubs the agent
builders (see snapshot.py), which is only safe while no agent is being built.

Like RunLog, it never raises. A snapshot is a measurement of the run, so a
failure costs one ``CONFIG FAILED`` line in run.log, never the run. The file
carries the text bodies, so ingestion later needs nothing but the file. It
lands in runs/, which the research workflow already commits.
"""

from __future__ import annotations

import asyncio
import os
import subprocess
from pathlib import Path
from typing import Any

from equity_mcp.hparams.snapshot import SNAPSHOT_VERSION, build_snapshot

_REPO_ROOT = Path(__file__).resolve().parents[2]


def _git(*args: str) -> str | None:
    try:
        out = subprocess.run(["git", *args], cwd=_REPO_ROOT, capture_output=True, text=True, timeout=5)
    except Exception:
        return None
    return out.stdout.strip() if out.returncode == 0 else None


def git_sha() -> str | None:
    return os.getenv("GITHUB_SHA") or _git("rev-parse", "HEAD") or None


def git_dirty() -> bool | None:
    """Whether the code a snapshot reads differs from HEAD. Outputs, runs and docs don't count."""
    out = _git("status", "--porcelain", "--", "equity_mcp")
    return None if out is None else bool(out)


async def capture_config(run_log: Any, run_params: dict, *, timeout_s: float = 30.0) -> dict | None:
    """
    Snapshot the live config, write it beside the run's reports, and return the payload.

    Returns None on any failure. ``CancelledError`` still propagates, because a
    Ctrl-C must stop the run.
    """
    try:
        sha, dirty = await asyncio.to_thread(lambda: (git_sha(), git_dirty()))
        snap = await asyncio.wait_for(
            build_snapshot(provenance="captured_at_runtime", source_git_sha=sha, source_git_dirty=dirty),
            timeout=timeout_s,
        )
    except Exception as exc:  # noqa: BLE001 - includes the TimeoutError from wait_for
        run_log.event(f"CONFIG FAILED {type(exc).__name__}: {exc}"[:300])
        return None

    payload = {"snapshot_version": SNAPSHOT_VERSION, "config_sha": snap.sha, "run_params": run_params,
               "snapshot": snap.to_record()}
    run_log.config(payload)
    git = (snap.source_git_sha or "?")[:7] + ("+dirty" if snap.source_git_dirty else "")
    run_log.event(f"CONFIG sha={snap.sha[:12]} git={git} gaps={len(snap.gaps)}")
    return payload
