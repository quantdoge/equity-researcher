"""
Live run status and incremental output.

Two problems, one mechanism.  A run is silent for half an hour and produces
nothing until it finishes, so a failure at specialist eleven shows no sign of
trouble beforehand and leaves nothing behind afterwards.  Both are fixed by a
single ``AgentMiddleware`` attached to every agent:

* ``awrap_tool_call`` narrates each fetch and each delegation as it happens.
* ``aafter_agent`` writes the finished agent's report to
  ``runs/<session>/reports/<role>.md``, appends it to the master copy at
  ``outputs/<session>.md``, and records the event in the session registry.

**None of this costs tokens.**  Every hook here either returns ``None`` or the
handler's result untouched, so no message, tool or prompt fragment reaches a
model.  The status lines are ordinary ``print``; the durability is ordinary
file I/O.  That is the whole reason this is middleware rather than an extra
"report your progress" instruction in the prompts.

Middleware, not ``astream``: deepagents invokes subagents *inside* the ``task``
tool rather than as graph nodes, so streaming the master's graph cannot see into
a specialist.  Middleware attached to each subagent spec can.

Only the async hooks are implemented.  ``langchain.agents.factory`` picks hooks
by comparing the class attribute against ``AgentMiddleware``'s and wraps them in
a ``RunnableCallable(sync, async)``, so async-only is a supported shape — and the
whole pipeline runs under ``ainvoke``.
"""

from __future__ import annotations

import logging
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Awaitable, Callable

from equity_mcp import session as session_registry
from equity_mcp import workspace

QUIET = 0
NORMAL = 1
VERBOSE = 2

# Windows consoles still default to a codepage that cannot encode any of this,
# and a UnicodeEncodeError raised from a status line would kill a run that was
# otherwise fine.  _pick_symbols falls back to ASCII when stdout says it cannot
# cope; nothing downstream depends on which set is in use.
_UNICODE_SYMBOLS = {
    "start": "▶", "delegate": "→", "done": "✓", "fail": "✗",
    "tool": "🔧", "note": "·", "memo": "★",
}
_ASCII_SYMBOLS = {
    "start": ">", "delegate": "->", "done": "[ok]", "fail": "[!!]",
    "tool": "*", "note": "-", "memo": "##",
}

_MAX_ARG_CHARS = 72


def _pick_symbols() -> dict[str, str]:
    encoding = getattr(sys.stdout, "encoding", None) or "ascii"
    try:
        "".join(_UNICODE_SYMBOLS.values()).encode(encoding)
    except (UnicodeEncodeError, LookupError):
        return _ASCII_SYMBOLS
    return _UNICODE_SYMBOLS


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _text_of(message: Any) -> str:
    """
    Flatten a message's content to text.

    ``.text`` handles the block-list content that non-Anthropic models on
    OpenRouter are more likely to return than a plain string — the same reason
    ``deep_agent_factory`` uses it for the final memo.
    """
    if message is None:
        return ""
    text = getattr(message, "text", None)
    # A property in current langchain-core, a method in older ones — and the
    # property's return value is still callable for compatibility, so test for
    # a string before testing for callable or every read warns.
    if isinstance(text, str):
        return text
    if callable(text):
        return str(text())
    return str(getattr(message, "content", message))


def _summarise_args(tool_name: str, args: Any) -> str:
    """One short, human-readable line describing what a tool call is asking for."""
    if not isinstance(args, dict):
        return str(args)[:_MAX_ARG_CHARS]

    if tool_name == "fmp_call":
        parts = [str(args.get("tool") or "?"), str(args.get("endpoint") or "?")]
        label = "/".join(parts)
        params = args.get("params")
        if isinstance(params, dict) and params:
            label += "  " + " ".join(f"{k}={v}" for k, v in list(params.items())[:3])
        return label[:_MAX_ARG_CHARS]

    if tool_name == "task":
        return str(args.get("subagent_type") or args.get("name") or "?")

    if tool_name == "web_search":
        return f'"{args.get("query", "")}"'[:_MAX_ARG_CHARS]

    if tool_name == "fetch_page":
        return str(args.get("url", ""))[:_MAX_ARG_CHARS]

    if tool_name == "run_python":
        code = str(args.get("code", ""))
        first = next((ln for ln in code.splitlines() if ln.strip()), "")
        lines = len(code.splitlines())
        return f"{lines} lines  {first.strip()[:40]}"

    for value in args.values():
        if isinstance(value, str) and value:
            return value[:_MAX_ARG_CHARS]
    return ""


class Reporter:
    """
    The console and the on-disk output for one run.

    Every write goes through ``_lock``: the master can emit parallel ``task``
    calls, and the FMP tools run in worker threads, so neither the console nor
    the appended master copy is single-writer.
    """

    def __init__(
        self,
        session_id: str,
        run_dir: Path,
        master_copy: Path | None,
        verbosity: int = NORMAL,
    ) -> None:
        self.session_id = session_id
        self.run_dir = run_dir
        self.master_copy = master_copy
        self.verbosity = verbosity
        self.started = time.time()
        self.symbols = _pick_symbols()
        self._lock = threading.Lock()
        self._log_file = run_dir / "run.log"

    # -- console ---------------------------------------------------------
    def line(self, text: str, indent: int = 0, level: int = NORMAL) -> None:
        if self.verbosity < level:
            return
        elapsed = time.time() - self.started
        stamp = f"[{int(elapsed // 60):02d}:{int(elapsed % 60):02d}]"
        rendered = f"{stamp} {'  ' * indent}{text}"
        with self._lock:
            try:
                print(rendered, flush=True)
            except UnicodeEncodeError:  # pragma: no cover - console codepage
                print(rendered.encode("ascii", "replace").decode(), flush=True)
            try:
                with self._log_file.open("a", encoding="utf-8") as fh:
                    fh.write(rendered + "\n")
            except OSError:
                pass  # a status line must never be the thing that ends a run

    def banner(self, lines: list[str]) -> None:
        """A framed block — used for the run header and the closing summary."""
        bar = "=" * 62
        self.line(bar, level=QUIET)
        for text in lines:
            self.line(f"  {text}", level=QUIET)
        self.line(bar, level=QUIET)

    # -- durable output --------------------------------------------------
    def append_master(self, section: str) -> None:
        if not self.master_copy:
            return
        with self._lock:
            self.master_copy.parent.mkdir(parents=True, exist_ok=True)
            with self.master_copy.open("a", encoding="utf-8") as fh:
                fh.write(section)

    def start_master(self, symbol: str, focus: str, resumed: bool) -> None:
        """
        Write the master copy's header, or a resume marker if it already exists.

        Appending rather than truncating is the point: the reports written
        before a crash are the reason the file is worth having.
        """
        if not self.master_copy:
            return
        if self.master_copy.exists():
            self.append_master(
                f"\n\n---\n\n*Resumed {_now()}*\n"
            )
            return
        header = (
            f"# Equity Research — {symbol}\n\n"
            f"- **Session**: `{self.session_id}`\n"
            f"- **Started**: {_now()}\n"
            f"- **Workspace**: `{self.run_dir}`\n"
        )
        if focus:
            header += f"- **Focus**: {focus}\n"
        header += "\n> Sections are appended as each agent finishes.\n"
        self.append_master(header)

    def write_report(self, role: str, body: str) -> Path:
        """
        Persist one agent's report.

        Named by role alone, not by an ordinal: a resumed run may rerun a
        specialist, and the newer report should replace the older one rather than
        accumulate near-duplicates.  True ordering lives in ``agent_events`` and
        in the append-only master copy.
        """
        path = workspace.reports_dir() / f"{workspace.slug(role)}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"# {role}\n\n_{_now()}_\n\n{body}\n", encoding="utf-8")
        return path


_reporter: Reporter | None = None


def configure(
    session_id: str,
    run_dir: Path,
    master_copy: Path | None,
    verbosity: int = NORMAL,
) -> Reporter:
    """Install the reporter for this process. Called once by the orchestrator."""
    global _reporter
    _reporter = Reporter(session_id, run_dir, master_copy, verbosity)
    return _reporter


def reporter() -> Reporter | None:
    """
    The active reporter, or ``None`` when nothing configured one.

    Building an agent outside a run — the compile check in CLAUDE.md, a REPL —
    is a legitimate thing to do, and it should not need a session.  Every hook
    below no-ops in that case.
    """
    return _reporter


class _ReporterHandler(logging.Handler):
    """Sends log records through the reporter, so they land in run.log too."""

    def emit(self, record: logging.LogRecord) -> None:
        rep = reporter()
        if rep is None:
            return
        symbol = rep.symbols["fail" if record.levelno >= logging.ERROR else "note"]
        rep.line(f"{symbol} {record.getMessage()}", indent=1, level=QUIET)


def setup_logging(verbosity: int = NORMAL) -> None:
    """
    Route the library loggers into the same stream as the status lines.

    ``logging.basicConfig`` is never called anywhere else in this project, so
    the plan-denied warnings ``tools/fmp.py`` already emits have until now gone
    nowhere.  They are exactly the kind of thing worth seeing mid-run.

    ``_ReporterHandler`` is a module-level class rather than a local one so the
    de-duplication below actually works: a class defined inside this function
    would be a *different* class on every call, and a second call would leave two
    handlers attached and print every warning twice.
    """
    level = logging.WARNING if verbosity <= QUIET else logging.INFO

    root = logging.getLogger()
    root.setLevel(level)
    for existing in list(root.handlers):
        if isinstance(existing, _ReporterHandler):
            root.removeHandler(existing)
    root.addHandler(_ReporterHandler())

    # Third-party chatter would drown the run at INFO.
    for noisy in ("httpx", "httpcore", "openai", "urllib3", "aiosqlite", "fastmcp", "mcp"):
        logging.getLogger(noisy).setLevel(logging.WARNING)


def _scope(role: str) -> str:
    """
    A key identifying one *invocation* of an agent, for per-invocation counters.

    A middleware instance is reused across every invocation of its agent, so the
    counters cannot live on ``self``.  The obvious key, ``checkpoint_ns``, is
    the wrong one: LangGraph writes it **per node**, so ``abefore_model`` and
    ``aafter_agent`` in the same invocation see different values and the
    accumulated counts would be dropped on the floor::

        m_SUB.before_model:5e6535...      <- one node
        m_SUB.after_agent:e05bf5...       <- the next

    What *is* stable across an invocation is the namespace's parent prefix —
    everything before the last ``|``.  A subagent invoked through the ``task``
    tool sees ``tools:<task-id>|<node>:<node-id>``, so the prefix is the
    delegating tool call: constant for that specialist's whole run, and distinct
    from any other delegation.  The master's own nodes are unnested, so their
    prefix is empty and the thread alone identifies them.
    """
    try:
        from langchain_core.runnables.config import ensure_config

        conf = (ensure_config() or {}).get("configurable") or {}
        ns = str(conf.get("checkpoint_ns") or "")
        parent = ns.rsplit("|", 1)[0] if "|" in ns else ""
        return f"{role}@{conf.get('thread_id') or ''}:{parent}"
    except Exception:
        return role


def build_middleware(role: str) -> Any:
    """
    Construct the progress middleware for *role*.

    The class is defined inside the function for the same reason
    ``roles.middleware_for_role`` imports its middleware lazily: ``server.py``
    imports that module, and a bare ``fastmcp run`` should not drag in the whole
    LangChain agent stack to serve six tools.
    """
    from langchain.agents.middleware import AgentMiddleware

    class ProgressMiddleware(AgentMiddleware):
        """Narrates one agent and persists its report when it finishes."""

        def __init__(self, role: str) -> None:
            super().__init__()
            self.role = role
            self.is_master = role == "head_of_research"
            self._runs: dict[str, dict[str, Any]] = {}

        @property
        def name(self) -> str:
            # Unique per agent — create_agent asserts on duplicate names, and
            # every agent gets one of these.
            return f"progress_{self.role}"

        def _counters(self) -> dict[str, Any]:
            key = _scope(self.role)
            state = self._runs.get(key)
            if state is None:
                state = {
                    "tools": 0,
                    "models": 0,
                    "t0": time.time(),
                    "started_at": _now(),
                }
                self._runs[key] = state
            return state

        async def abefore_agent(self, state, runtime):  # noqa: ANN001, ARG002
            rep = reporter()
            self._counters()  # start the clock even if nothing is watching
            if rep and not self.is_master:
                rep.line(f"{rep.symbols['start']} {self.role}", indent=1)
            return None

        async def abefore_model(self, state, runtime):  # noqa: ANN001, ARG002
            self._counters()["models"] += 1
            return None

        async def awrap_tool_call(
            self,
            request: Any,
            handler: Callable[[Any], Awaitable[Any]],
        ) -> Any:
            rep = reporter()
            call = getattr(request, "tool_call", None) or {}
            tool_name = str(call.get("name") or "?")
            counters = self._counters()
            counters["tools"] += 1

            if rep:
                summary = _summarise_args(tool_name, call.get("args"))
                if tool_name == "task":
                    rep.line(f"{rep.symbols['delegate']} delegate  {summary}")
                else:
                    indent = 1 if self.is_master else 2
                    rep.line(f"{rep.symbols['tool']} {tool_name}  {summary}", indent=indent)

            result = await handler(request)

            # Observation only — the handler's result is returned untouched, so
            # nothing here reaches a model.
            if rep and rep.verbosity >= VERBOSE:
                preview = _text_of(result).strip().replace("\n", " ")[:110]
                if preview:
                    rep.line(f"{rep.symbols['note']} {preview}", indent=3, level=VERBOSE)
            return result

        async def aafter_agent(self, state, runtime):  # noqa: ANN001, ARG002
            rep = reporter()
            key = _scope(self.role)
            counters = self._runs.pop(key, None) or {
                "tools": 0, "models": 0, "t0": time.time(), "started_at": _now(),
            }
            elapsed = round(time.time() - counters["t0"], 1)

            messages = (state or {}).get("messages") or []
            body = _text_of(messages[-1]).strip() if messages else ""

            report_path: str | None = None
            if body and rep:
                try:
                    path = rep.write_report(self.role, body)
                    report_path = workspace.relative(path)
                    heading = (
                        f"{rep.symbols['memo']} Investment Memo"
                        if self.is_master else self.role
                    )
                    rep.append_master(
                        f"\n\n---\n\n## {heading}\n\n"
                        f"<sub>{counters['tools']} tool calls · "
                        f"{counters['models']} model calls · {elapsed}s</sub>\n\n"
                        f"{body}\n"
                    )
                except OSError as exc:  # pragma: no cover - disk trouble only
                    logging.getLogger(__name__).warning(
                        "could not persist %s report: %s", self.role, exc
                    )

            if rep:
                try:
                    # Off the event loop: a blocking sqlite write here would
                    # stall the checkpointer's pending commit and deadlock until
                    # the busy timeout expires.  See session.py's docstring.
                    await session_registry.arecord_agent(
                        rep.session_id,
                        self.role,
                        status="completed",
                        started_at=counters["started_at"],
                        elapsed_s=elapsed,
                        tool_calls=counters["tools"],
                        model_calls=counters["models"],
                        report_path=report_path,
                        chars=len(body),
                    )
                except Exception as exc:  # pragma: no cover - bookkeeping only
                    logging.getLogger(__name__).warning(
                        "could not record %s event: %s", self.role, exc
                    )

                if not self.is_master:
                    rep.line(
                        f"{rep.symbols['done']} {self.role} done  "
                        f"({counters['tools']} tools, {counters['models']} model calls, "
                        f"{elapsed}s)",
                        indent=1,
                    )
                    if report_path:
                        rep.line(f"{rep.symbols['note']} saved {report_path}", indent=2)
            return None

    return ProgressMiddleware(role)
