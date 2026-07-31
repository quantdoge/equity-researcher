"""
Python execution over data already fetched into the run workspace.

The analysis layer used to be ~40 hand-written ``calculate_*`` functions, each
hard-coding the field names of a database schema that no longer exists. This
replaces all of them: an agent pulls the series it needs with ``fmp_call``,
reads the ``fields`` list off the response so it knows what it actually got, and
writes the arithmetic itself.

Execution is a plain subprocess rather than ``exec`` in-process, for two reasons
that both matter: a runaway script can be killed on a timeout, and the child gets
a scrubbed environment. Generated code computes over JSON sitting on disk — it
has no business holding ``FMP_API_KEY`` or ``OPENROUTER_API_KEY``, so
``_ALLOWED_ENV`` passes through only what the interpreter needs to start.

This is not a security sandbox. The child runs as the same user with the same
filesystem and network access; the scrub limits credential exposure, not reach.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import uuid
from pathlib import Path

from equity_mcp import workspace

# Enough for CPython to start and for stdout to survive non-ASCII on Windows.
# Everything else — including every API key — is withheld from the child.
_ALLOWED_ENV = ("PATH", "SYSTEMROOT", "WINDIR", "TEMP", "TMP", "HOME", "LANG")

_MAX_STREAM = 16_000
_DEFAULT_TIMEOUT = 120
_MAX_TIMEOUT = 600


def _scrubbed_env() -> dict[str, str]:
    env = {k: os.environ[k] for k in _ALLOWED_ENV if k in os.environ}
    env["PYTHONIOENCODING"] = "utf-8"
    return env


def _clip(text: str) -> str:
    if len(text) <= _MAX_STREAM:
        return text
    return text[:_MAX_STREAM] + f"\n… [clipped, {len(text):,} bytes total]"


def run_python(code: str, timeout_s: int = _DEFAULT_TIMEOUT) -> dict:
    """
    Run Python and return what it printed.

    The script runs with the run workspace as its working directory, so data
    saved by fmp_call is at "data/<name>.json" — load it with a relative path.
    Print your results (JSON is easiest to read back); nothing else is captured.

    The standard library is available, as are any packages installed in this
    project's environment. No API keys are visible to the script, so it cannot
    fetch data itself — pull what you need with fmp_call first.

    Args:
        code: Python source to execute.
        timeout_s: Seconds before the script is killed (capped at 600).

    Returns:
        {"stdout", "stderr", "exit_code", "script"} — or {"error", ...} if the
        script timed out or could not be started. This never raises.
    """
    timeout = max(1, min(int(timeout_s), _MAX_TIMEOUT))
    cwd = workspace.workspace_dir()
    script = workspace.scripts_dir() / f"{uuid.uuid4().hex[:12]}.py"
    script.write_text(code, encoding="utf-8")

    rel = workspace.relative(script)
    try:
        proc = subprocess.run(
            [sys.executable, str(script)],
            cwd=str(cwd),
            env=_scrubbed_env(),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
        )
    except subprocess.TimeoutExpired as exc:
        return {
            "error": f"script timed out after {timeout}s",
            "exit_code": None,
            "script": rel,
            "stdout": _clip(exc.stdout or ""),
            "stderr": _clip(exc.stderr or ""),
        }
    except OSError as exc:
        return {"error": f"could not start python: {exc}", "script": rel}

    return {
        "exit_code": proc.returncode,
        "stdout": _clip(proc.stdout),
        "stderr": _clip(proc.stderr),
        "script": rel,
    }


def list_workspace() -> dict:
    """
    List the data files saved in the run workspace by fmp_call.

    Use this to see what has already been fetched — by yourself or by another
    agent in this run — before pulling it again.

    Returns:
        {"workspace": str, "files": [{"path", "size_bytes", "row_count", "fields"}]}
    """
    root = workspace.data_dir()
    files: list[dict] = []

    for path in sorted(root.glob("*.json")):
        entry: dict = {
            "path": workspace.relative(path),
            "size_bytes": path.stat().st_size,
        }
        try:
            rows = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            entry["error"] = f"unreadable: {exc}"
            files.append(entry)
            continue

        if isinstance(rows, list):
            entry["row_count"] = len(rows)
            first = next((r for r in rows if isinstance(r, dict)), None)
            if first is not None:
                entry["fields"] = list(first.keys())
        files.append(entry)

    return {"workspace": str(workspace.workspace_dir()), "files": files}
