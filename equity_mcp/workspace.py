"""
Per-run scratch directory shared by the FMP tools and the code executor.

MCP tools are plain functions invoked with no run context, so there is nowhere
to thread a run identifier through: ``fmp_call`` needs somewhere to spill large
payloads, and ``run_python`` needs a working directory to find them in again.
A process-global run directory is what makes those two land in the same place.

Layout::

    runs/<SYMBOL>_<TIMESTAMP>/
        data/       # JSON payloads spilled by fmp_call
        scripts/    # Python written by the quant_engineer subagent
        reports/    # one .md per specialist, written as each finishes

``orchestrator.py`` calls ``set_run(symbol)`` before the agent starts. Anything
that touches the workspace without one — a bare ``fastmcp run``, a REPL — gets a
lazily created ``runs/adhoc_<TIMESTAMP>/`` instead of an error, so the tools stay
usable standalone.

The directory name doubles as the session id (see ``session.py``): resuming a
failed run calls ``attach_run(session_id)`` instead of ``set_run``, so the second
pass spills into the same directory and can read what the first pass fetched.
"""

from __future__ import annotations

import os
import re
from datetime import datetime
from pathlib import Path

_DATA = "data"
_SCRIPTS = "scripts"
_REPORTS = "reports"

_SUBDIRS = (_DATA, _SCRIPTS, _REPORTS)

_run_dir: Path | None = None


def _stamp() -> str:
    return datetime.now().strftime("%Y%m%dT%H%M%S")


def slug(text: str) -> str:
    """Reduce *text* to something safe for a directory or file name."""
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "_", text).strip("._-")
    return cleaned or "unnamed"


def set_run(symbol: str, root: str | Path | None = None) -> Path:
    """
    Start a new run workspace for *symbol* and make it the process-wide default.

    ``root`` defaults to ``$EQ_WORKSPACE_ROOT`` or ``./runs``.
    """
    global _run_dir

    base = Path(root or os.environ.get("EQ_WORKSPACE_ROOT") or "runs")
    _run_dir = (base / f"{slug(symbol).upper()}_{_stamp()}").resolve()
    for sub in _SUBDIRS:
        (_run_dir / sub).mkdir(parents=True, exist_ok=True)
    return _run_dir


def attach_run(session_id: str, root: str | Path | None = None) -> Path:
    """
    Re-enter the existing workspace named *session_id* — the resume counterpart
    to ``set_run``.

    Raises ``FileNotFoundError`` rather than creating the directory: a resume
    against a workspace that is not there would silently refetch everything into
    an empty one, which looks like a working resume and is not.  Missing
    *subdirectories* are recreated, since an untouched run may never have had a
    reason to make ``scripts/``.
    """
    global _run_dir

    base = Path(root or os.environ.get("EQ_WORKSPACE_ROOT") or "runs")
    candidate = (base / session_id).resolve()
    if not candidate.is_dir():
        raise FileNotFoundError(f"No run workspace at {candidate}")

    _run_dir = candidate
    for sub in _SUBDIRS:
        (_run_dir / sub).mkdir(parents=True, exist_ok=True)
    return _run_dir


def session_id() -> str:
    """The active run's identifier — its directory name."""
    return workspace_dir().name


def workspace_dir() -> Path:
    """
    Return the active run workspace, creating an ad-hoc one if none was set.

    ``$EQ_WORKSPACE`` pins an explicit directory and wins over both the run set
    by ``set_run`` and the ad-hoc fallback — that is the hook for pointing a
    test or a manual session at a known location.
    """
    global _run_dir

    pinned = os.environ.get("EQ_WORKSPACE")
    if pinned:
        path = Path(pinned).resolve()
        for sub in _SUBDIRS:
            (path / sub).mkdir(parents=True, exist_ok=True)
        return path

    if _run_dir is None:
        set_run("adhoc")
    assert _run_dir is not None  # set_run always assigns
    return _run_dir


def data_dir() -> Path:
    return workspace_dir() / _DATA


def scripts_dir() -> Path:
    return workspace_dir() / _SCRIPTS


def reports_dir() -> Path:
    return workspace_dir() / _REPORTS


def relative(path: Path) -> str:
    """Path as the agent should refer to it — relative to the workspace root."""
    try:
        return path.resolve().relative_to(workspace_dir()).as_posix()
    except ValueError:
        return path.as_posix()
