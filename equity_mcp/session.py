"""
Durable run state — LangGraph checkpoints and the session registry.

A full run is fourteen agents over roughly half an hour, so it is worth being
able to lose the second half of one without losing the first.  Two things live
in ``runs/sessions.sqlite``:

* **LangGraph's own checkpoint tables**, written by ``AsyncSqliteSaver`` at every
  superstep of the master graph.  This is what ``--last`` resumes from.
* **A session registry** — ``sessions`` and ``agent_events`` — written by this
  module.  The checkpoint tables are opaque blobs keyed by ``thread_id``; the
  registry is what makes ``--list-sessions`` answerable without deserialising
  them, and what records *why* a run stopped.

The two share one file on purpose: one path to configure, one file to delete.
They are written through different connections (aiosqlite for the saver, plain
``sqlite3`` here), which SQLite is fine with in WAL mode — see ``_connect``.

**Never call the write helpers here directly from a coroutine.**  They block, and
the checkpointer's ``commit()`` is an ``await`` queued on the same event loop:
blocking the loop means the saver cannot release its write transaction, which
means the blocking call waits out its full busy timeout and fails with "database
is locked", every time.  Observed as a 30-second stall per agent before it was
routed off the loop.  ``arecord_agent`` is the async-safe entry point; add a
``to_thread`` wrapper alongside it for anything else called from async code.

Resume granularity is one specialist, not one tool call.  Checkpoints land at
master-graph supersteps, so every *finished* specialist report is preserved in
the master's message history; a specialist that died mid-flight reruns from
scratch, because deepagents compiles subagent graphs without a checkpointer and
its ``SubAgent`` spec has nowhere to pass one.  The payloads that specialist had
already fetched are still in ``runs/<session>/data/``, so the rerun is cheaper
than the first pass, not free.

Session ids are the run-directory name, ``<SYMBOL>_<TIMESTAMP>`` — the same
string is the LangGraph ``thread_id``, the workspace directory, and the stem of
both output files.  There is deliberately no second identifier scheme.
"""

from __future__ import annotations

import asyncio
import os
import sqlite3
import threading
from contextlib import asynccontextmanager, contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, AsyncIterator, Iterator

STATUS_RUNNING = "running"
STATUS_FAILED = "failed"
STATUS_COMPLETED = "completed"

RESUMABLE = (STATUS_RUNNING, STATUS_FAILED)

# Registry writes are a few per run against a file the checkpointer writes to
# constantly.  WAL lets the two coexist; the busy timeout covers the moments
# they collide anyway.
_BUSY_TIMEOUT_MS = 30_000

# The FMP tools run in worker threads and the progress middleware writes from
# whichever task the graph is in, so registry writes are not single-threaded.
_lock = threading.Lock()

_SCHEMA = """
CREATE TABLE IF NOT EXISTS sessions (
    session_id    TEXT PRIMARY KEY,
    symbol        TEXT NOT NULL,
    focus         TEXT NOT NULL DEFAULT '',
    status        TEXT NOT NULL,
    started_at    TEXT NOT NULL,
    updated_at    TEXT NOT NULL,
    finished_at   TEXT,
    run_dir       TEXT NOT NULL,
    memo_path     TEXT,
    error         TEXT,
    resumed_count INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS agent_events (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id   TEXT NOT NULL,
    seq          INTEGER NOT NULL,
    role         TEXT NOT NULL,
    status       TEXT NOT NULL,
    started_at   TEXT,
    finished_at  TEXT NOT NULL,
    elapsed_s    REAL,
    tool_calls   INTEGER NOT NULL DEFAULT 0,
    model_calls  INTEGER NOT NULL DEFAULT 0,
    report_path  TEXT,
    chars        INTEGER NOT NULL DEFAULT 0
);

CREATE INDEX IF NOT EXISTS agent_events_session
    ON agent_events (session_id, seq);
"""


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def state_db_path() -> Path:
    """
    Where the checkpoints and the registry live.

    ``$EQ_STATE_DB`` pins an explicit file; otherwise it sits beside the run
    workspaces, under ``$EQ_WORKSPACE_ROOT`` if that is set so the whole of a
    run's state stays together when the root is moved.
    """
    pinned = os.environ.get("EQ_STATE_DB")
    if pinned:
        return Path(pinned).resolve()
    root = Path(os.environ.get("EQ_WORKSPACE_ROOT") or "runs")
    return (root / "sessions.sqlite").resolve()


@contextmanager
def _connect() -> Iterator[sqlite3.Connection]:
    """A short-lived registry connection, committed on clean exit."""
    path = state_db_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path, timeout=_BUSY_TIMEOUT_MS / 1000)
    conn.row_factory = sqlite3.Row
    try:
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute(f"PRAGMA busy_timeout={_BUSY_TIMEOUT_MS}")
        yield conn
        conn.commit()
    finally:
        conn.close()


def init_db() -> None:
    """Create the registry tables. Idempotent; safe to call on every start."""
    with _lock, _connect() as conn:
        conn.executescript(_SCHEMA)


@asynccontextmanager
async def checkpointer() -> AsyncIterator[Any]:
    """
    Yield an ``AsyncSqliteSaver`` over the state DB.

    Must wrap *both* the graph build and the invoke: the saver holds an open
    aiosqlite connection and binds to the running loop at construction, so a
    graph compiled against a closed one is a graph that cannot checkpoint.
    """
    from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver

    path = state_db_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    async with AsyncSqliteSaver.from_conn_string(str(path)) as saver:
        await saver.setup()
        yield saver


# --------------------------------------------------------------------------
# sessions
# --------------------------------------------------------------------------

def start_session(session_id: str, symbol: str, focus: str, run_dir: Path) -> None:
    """Register a new run as ``running``."""
    now = _now()
    with _lock, _connect() as conn:
        conn.execute(
            """
            INSERT OR REPLACE INTO sessions
                (session_id, symbol, focus, status, started_at, updated_at, run_dir)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (session_id, symbol, focus, STATUS_RUNNING, now, now, str(run_dir)),
        )


def mark_resumed(session_id: str) -> None:
    """Flip a session back to ``running`` and count the resume."""
    with _lock, _connect() as conn:
        conn.execute(
            """
            UPDATE sessions
               SET status = ?, updated_at = ?, finished_at = NULL, error = NULL,
                   resumed_count = resumed_count + 1
             WHERE session_id = ?
            """,
            (STATUS_RUNNING, _now(), session_id),
        )


def finish_session(
    session_id: str,
    status: str,
    error: str | None = None,
    memo_path: str | None = None,
) -> None:
    """Record the terminal state. Called from a ``finally``, so never raises."""
    now = _now()
    try:
        with _lock, _connect() as conn:
            conn.execute(
                """
                UPDATE sessions
                   SET status = ?, updated_at = ?, finished_at = ?,
                       error = ?, memo_path = COALESCE(?, memo_path)
                 WHERE session_id = ?
                """,
                (status, now, now, error, memo_path, session_id),
            )
    except sqlite3.Error:  # pragma: no cover - a bookkeeping write, not the run
        pass


def get(session_id: str) -> dict[str, Any] | None:
    with _lock, _connect() as conn:
        row = conn.execute(
            "SELECT * FROM sessions WHERE session_id = ?", (session_id,)
        ).fetchone()
    return dict(row) if row else None


def latest_resumable() -> dict[str, Any] | None:
    """The newest session that stopped without finishing — what bare ``--last`` means."""
    placeholders = ",".join("?" * len(RESUMABLE))
    with _lock, _connect() as conn:
        row = conn.execute(
            f"""
            SELECT * FROM sessions
             WHERE status IN ({placeholders})
             ORDER BY started_at DESC
             LIMIT 1
            """,
            RESUMABLE,
        ).fetchone()
    return dict(row) if row else None


def list_sessions(limit: int = 20) -> list[dict[str, Any]]:
    with _lock, _connect() as conn:
        rows = conn.execute(
            """
            SELECT s.*, (
                SELECT COUNT(*) FROM agent_events e
                 WHERE e.session_id = s.session_id
            ) AS agents_done
              FROM sessions s
             ORDER BY s.started_at DESC
             LIMIT ?
            """,
            (limit,),
        ).fetchall()
    return [dict(r) for r in rows]


# --------------------------------------------------------------------------
# agent_events
# --------------------------------------------------------------------------

def record_agent(
    session_id: str,
    role: str,
    *,
    status: str,
    started_at: str | None,
    elapsed_s: float | None,
    tool_calls: int,
    model_calls: int,
    report_path: str | None,
    chars: int,
) -> int:
    """
    Append one finished-agent event and return its sequence number.

    The sequence is allocated here under the same lock as the insert, so two
    specialists finishing concurrently — which happens whenever the master emits
    parallel ``task`` calls — cannot claim the same number.
    """
    with _lock, _connect() as conn:
        row = conn.execute(
            "SELECT COALESCE(MAX(seq), 0) AS n FROM agent_events WHERE session_id = ?",
            (session_id,),
        ).fetchone()
        seq = int(row["n"]) + 1
        conn.execute(
            """
            INSERT INTO agent_events
                (session_id, seq, role, status, started_at, finished_at,
                 elapsed_s, tool_calls, model_calls, report_path, chars)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                session_id, seq, role, status, started_at, _now(),
                elapsed_s, tool_calls, model_calls, report_path, chars,
            ),
        )
    return seq


async def arecord_agent(*args: Any, **kwargs: Any) -> int:
    """
    ``record_agent`` from a coroutine, off the event loop.

    The progress middleware runs inside the graph, so this is the only safe way
    to call it there — see the module docstring on why a blocking write from the
    loop deadlocks against the checkpointer.
    """
    return await asyncio.to_thread(lambda: record_agent(*args, **kwargs))


def agent_events(session_id: str) -> list[dict[str, Any]]:
    with _lock, _connect() as conn:
        rows = conn.execute(
            "SELECT * FROM agent_events WHERE session_id = ? ORDER BY seq",
            (session_id,),
        ).fetchall()
    return [dict(r) for r in rows]
