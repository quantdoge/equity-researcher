"""
Financial Modeling Prep MCP client — the single data source for every agent.

FMP's remote MCP server exposes 28 *category* tools (``statements``, ``chart``,
``company``, ``news``, …), each taking an ``endpoint`` enum that selects one of
roughly 250 underlying REST endpoints:

    https://financialmodelingprep.com/mcp?apikey=<FMP_API_KEY>

See https://site.financialmodelingprep.com/developer/docs/mcp-server

This module publishes exactly two tools rather than a hand-written wrapper per
endpoint, because a wrapper per endpoint is a second copy of FMP's catalog that
drifts the moment FMP adds anything:

- ``fmp_catalog`` — discovery. What categories exist, then what endpoints and
  parameters a given category takes.
- ``fmp_call`` — a generic passthrough. Payloads come back in FMP's own
  camelCase, undisturbed; ``fields`` in the response tells the caller what it
  actually got so no downstream code has to assume a field name.

Large payloads spill to disk. A single ``technicalIndicators`` call returns well
over 100 KB, which is untenable in an LLM context but trivial for ``run_python``
to read back off the workspace — so anything past ``_INLINE_LIMIT`` is written to
``<workspace>/data/`` and only a preview is returned.

``fastmcp.Client`` is async-only, but MCP tools are called synchronously (FastMCP
runs sync tools in worker threads) and ``asyncio.run`` raises if the calling
thread already drives a loop. So this module owns one daemon event loop on a
background thread and marshals every call onto it.

That loop outlives the main thread, which is the one hazard worth knowing about.
CPython sets ``concurrent.futures.thread._shutdown`` the moment the main thread
finishes, and everything downstream of a connect — right down to the
``run_in_executor`` that resolves DNS — refuses to schedule after that. A call
started in that window would otherwise die as an opaque ``cannot schedule new
futures after interpreter shutdown``; ``call_tools`` detects the window and
raises ``FmpShuttingDown``, which ``fmp_call`` reports as the benign teardown
race it is rather than a data failure.
"""

from __future__ import annotations

import asyncio
import atexit
import json
import logging
import os
import threading
from typing import Any, Iterable, Sequence

from equity_mcp import workspace

_log = logging.getLogger(__name__)

_ENDPOINT = "https://financialmodelingprep.com/mcp"

# Per-call budget, plus a smaller allowance for each extra call in a batch,
# since a batch shares one initialised session.
_CALL_TIMEOUT = 90.0
_EXTRA_CALL_TIMEOUT = 15.0
_MAX_BATCH_TIMEOUT = 600.0

# Margin the calling thread allows on top of the loop's own deadline, so the
# in-loop timeout is what normally fires and the session unwinds cleanly.
_TIMEOUT_GRACE = 10.0

# How long exit waits for the loop thread to stop before giving up on it.
_SHUTDOWN_JOIN_TIMEOUT = 2.0

# Serialised payload size past which rows go to a file instead of the response.
_INLINE_LIMIT = 8_000

# FMP reports subscription limits in prose rather than as a status code.
_PLAN_DENIED_MARKERS = ("access denied", "requires a higher plan", "upgrade your")


class FmpError(RuntimeError):
    """The FMP MCP server was unreachable, refused the key, or returned junk."""


class FmpPlanDenied(FmpError):
    """The endpoint exists but the account's FMP subscription doesn't cover it."""


class FmpShuttingDown(FmpError):
    """The interpreter is tearing down; no new FMP work can be scheduled."""


def _is_plan_denied(text: str) -> bool:
    lowered = text.lower()
    return any(marker in lowered for marker in _PLAN_DENIED_MARKERS)


def _is_shutdown_error(exc: BaseException) -> bool:
    """True for the executor's refusal to schedule once the main thread has gone."""
    return "cannot schedule new futures" in str(exc)


def _shutting_down() -> bool:
    """
    True once the main thread has finished.

    ``threading._shutdown`` runs ``concurrent.futures``' exit hook *before* it
    stops the main thread, so this trails the real flag by a hair — the
    ``_is_shutdown_error`` conversion in ``call_tools`` covers that gap. Both are
    public-API checks; the private ``_shutdown`` globals move between versions.
    """
    return _closed or not threading.main_thread().is_alive()


# ── Background event loop ─────────────────────────────────────────────────────

_loop: asyncio.AbstractEventLoop | None = None
_loop_thread: threading.Thread | None = None
_loop_lock = threading.Lock()
_closed = False


def _background_loop() -> asyncio.AbstractEventLoop:
    """Return the module's event loop, starting its daemon thread on first use."""
    global _loop, _loop_thread
    with _loop_lock:
        if _loop is None or _loop.is_closed():
            loop = asyncio.new_event_loop()
            thread = threading.Thread(
                target=loop.run_forever, name="fmp-mcp-loop", daemon=True
            )
            thread.start()
            _loop, _loop_thread = loop, thread
        return _loop


@atexit.register
def _shutdown_loop() -> None:
    """
    Stop the background loop at exit so nothing is left mid-flight.

    Ordering matters here: CPython runs ``threading._shutdown()`` — and with it
    the flag that breaks scheduling — *before* atexit callbacks, so this is
    cleanup rather than prevention. Its real job is cancelling the reconnect
    timers the MCP streamable-HTTP transport arms after a session closes
    ("GET stream disconnected, reconnecting in 1000ms"), which would otherwise
    fire into a half-torn-down interpreter. The join is bounded so a wedged
    session can never hang the process on the way out.
    """
    global _closed
    _closed = True

    with _loop_lock:
        loop, thread = _loop, _loop_thread
    if loop is None or loop.is_closed():
        return

    def _stop() -> None:
        for task in asyncio.all_tasks(loop):
            task.cancel()
        loop.stop()

    try:
        loop.call_soon_threadsafe(_stop)
    except RuntimeError:
        return  # loop already closed underneath us
    if thread is not None:
        thread.join(timeout=_SHUTDOWN_JOIN_TIMEOUT)


def _server_url() -> str:
    key = os.environ.get("FMP_API_KEY", "")
    if not key:
        raise FmpError("FMP_API_KEY not set — cannot reach the FMP MCP server")
    return f"{_ENDPOINT}?apikey={key}"


# ── Call machinery ────────────────────────────────────────────────────────────


def _coerce(value: Any) -> Any:
    """
    Parse an FMP payload that arrived as a JSON string.

    The FMP tools declare a string return type, so their JSON reaches us as text
    either way: as a content block, or — since fastmcp wraps non-dict output
    under a single "result" key — as a string sitting inside structured content.
    Anything already decoded passes through untouched.
    """
    if not isinstance(value, str):
        return value

    text = value.strip()
    if not text:
        raise FmpError("FMP MCP returned an empty payload")
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        # FMP reports auth/plan failures as plain prose, not JSON.
        if _is_plan_denied(text):
            raise FmpPlanDenied(text[:300]) from exc
        raise FmpError(f"FMP MCP returned non-JSON payload: {text[:300]}") from exc


def _unwrap(result: Any) -> Any:
    """Turn a fastmcp CallToolResult (or a bare content list) into Python data."""
    structured = getattr(result, "structured_content", None)
    if isinstance(structured, dict) and structured:
        if len(structured) == 1 and "result" in structured:
            return _coerce(structured["result"])
        return structured

    blocks = getattr(result, "content", None)
    if blocks is None:
        blocks = result if isinstance(result, (list, tuple)) else []

    texts = [t for t in (getattr(b, "text", None) for b in blocks) if t]
    if not texts:
        raise FmpError("FMP MCP returned no text content")

    return _coerce("\n".join(texts))


async def _acall_many(
    calls: Sequence[tuple[str, dict]], skip_errors: bool, timeout: float
) -> list[Any]:
    """
    Run every call over one session, under a deadline the loop itself enforces.

    Holding the timeout here rather than on the calling thread is what makes it
    cancel: ``Future.cancel()`` cannot stop a coroutine that has already started,
    so the old arrangement left ``Client`` sessions open and reconnecting long
    after the caller had given up. An ``asyncio.timeout`` unwinds the ``async
    with`` instead, closing the session on the way out.
    """
    from fastmcp import Client

    results: list[Any] = []
    async with asyncio.timeout(timeout):
        # Connecting is inside the try so a failure here carries the same context
        # as a tool failure, rather than escaping raw to call_tools.
        try:
            async with Client(_server_url()) as client:
                for name, arguments in calls:
                    args = {k: v for k, v in arguments.items() if v is not None}
                    try:
                        results.append(_unwrap(await client.call_tool(name, args)))
                    except FmpError:
                        raise
                    except Exception as exc:
                        if _is_plan_denied(str(exc)):
                            raise FmpPlanDenied(str(exc)) from exc
                        if not skip_errors:
                            raise FmpError(
                                f"FMP MCP tool {name}{args} failed: {exc}"
                            ) from exc
                        _log.warning("FMP MCP tool %s%s failed: %s", name, args, exc)
                        results.append(None)
        except FmpError:
            raise
        except Exception as exc:
            if _is_shutdown_error(exc):
                raise FmpShuttingDown(str(exc)) from exc
            raise FmpError(f"FMP MCP session failed: {exc}") from exc
    return results


def call_tools(
    calls: Iterable[tuple[str, dict]], *, skip_errors: bool = False
) -> list[Any]:
    """
    Run a batch of ``(tool_name, arguments)`` over a single MCP session.

    Returns one decoded payload per call, in order. With ``skip_errors=True`` a
    failing call yields ``None`` instead of aborting the whole batch.

    Raises ``FmpShuttingDown`` rather than attempting a doomed connect once the
    interpreter is on its way out.
    """
    calls = list(calls)
    if not calls:
        return []

    if _shutting_down():
        raise FmpShuttingDown("interpreter is shutting down")

    timeout = min(
        _CALL_TIMEOUT + _EXTRA_CALL_TIMEOUT * (len(calls) - 1), _MAX_BATCH_TIMEOUT
    )
    return _run(_acall_many(calls, skip_errors, timeout), timeout)


def call_tool(name: str, /, **arguments: Any) -> Any:
    """
    Run a single FMP MCP tool call and return its decoded payload.

    ``name`` is positional-only deliberately: several FMP endpoints take an
    argument literally called ``name`` (``economics-indicators``,
    ``search-by-name``, the ``Fundraisers`` searches), which otherwise collides
    with this parameter and raises "got multiple values for argument 'name'".
    """
    return call_tools([(name, arguments)])[0]


def _run(coro: Any, timeout: float) -> Any:
    """Drive *coro* on the background loop, translating teardown into FmpShuttingDown."""
    try:
        future = asyncio.run_coroutine_threadsafe(coro, _background_loop())
    except RuntimeError as exc:
        # The loop shut down between the guard above and scheduling.
        coro.close()
        raise FmpShuttingDown(str(exc)) from exc

    try:
        # The loop's own deadline should fire first; this is only a backstop for
        # a loop that has stopped servicing work altogether.
        return future.result(timeout=timeout + _TIMEOUT_GRACE)
    except FmpError:
        raise
    except TimeoutError as exc:
        future.cancel()
        raise FmpError(f"FMP MCP call exceeded {timeout:g}s") from exc
    except Exception as exc:
        future.cancel()
        if _is_shutdown_error(exc) or _shutting_down():
            raise FmpShuttingDown(str(exc)) from exc
        raise FmpError(f"FMP MCP call failed: {exc}") from exc


# ── Catalog ───────────────────────────────────────────────────────────────────

_catalog_cache: list[dict] | None = None
_catalog_lock = threading.Lock()


async def _alist_tools(timeout: float) -> list[dict]:
    from fastmcp import Client

    async with asyncio.timeout(timeout):
        try:
            async with Client(_server_url()) as client:
                tools = await client.list_tools()
        except Exception as exc:
            if _is_shutdown_error(exc):
                raise FmpShuttingDown(str(exc)) from exc
            raise FmpError(f"FMP MCP list_tools failed: {exc}") from exc

    listing: list[dict] = []
    for t in tools:
        schema = t.inputSchema or {}
        props = schema.get("properties", {}) or {}
        endpoint = props.get("endpoint", {}) or {}
        listing.append(
            {
                "tool": t.name,
                "description": (t.description or "").strip(),
                "params": [k for k in props if k != "endpoint"],
                "endpoints": endpoint.get("enum") or [],
                "required": schema.get("required", []),
            }
        )
    return sorted(listing, key=lambda d: d["tool"].lower())


def _catalog() -> list[dict]:
    """The FMP tool listing, fetched once and cached for the process."""
    global _catalog_cache
    with _catalog_lock:
        if _catalog_cache is None:
            _catalog_cache = _run(_alist_tools(_CALL_TIMEOUT), _CALL_TIMEOUT)
        return _catalog_cache


def _summary(description: str) -> str:
    """
    First paragraph of an FMP tool description.

    FMP appends a full "Endpoints: - name: Title" block to every description.
    That block is the useful part of a drill-down and pure noise in a listing,
    so the compact view cuts at it.
    """
    head = description.split("Endpoints:")[0].strip()
    return " ".join(head.split())


# ── Public tools ──────────────────────────────────────────────────────────────


def fmp_catalog(tool: str | None = None) -> dict:
    """
    Discover what Financial Modeling Prep data is available.

    Call with no arguments for the list of category tools (statements, chart,
    company, news, analyst, economics, …) and what each covers. Then call again
    with one of those names to get its full endpoint list and parameters before
    using fmp_call.

    Args:
        tool: A category tool name from the bare listing. Omit for the overview.

    Returns:
        Overview: {"tools": [{"tool", "summary", "endpoint_count"}, ...]}
        Drill-down: {"tool", "description", "endpoints", "params", "required"}
    """
    try:
        catalog = _catalog()
    except FmpShuttingDown as exc:
        return {"error": str(exc), "kind": "shutting_down"}
    except FmpError as exc:
        return {"error": str(exc), "kind": "unavailable"}

    if tool is None:
        return {
            "tools": [
                {
                    "tool": entry["tool"],
                    "summary": _summary(entry["description"]),
                    "endpoint_count": len(entry["endpoints"]),
                }
                for entry in catalog
            ],
            "usage": (
                "Call fmp_catalog('<tool>') for that tool's endpoints and "
                "parameters, then fmp_call(tool, endpoint, params)."
            ),
        }

    match = next(
        (e for e in catalog if e["tool"].lower() == tool.lower()),
        None,
    )
    if match is None:
        return {
            "error": f"No FMP tool named '{tool}'",
            "kind": "bad_request",
            "available": [e["tool"] for e in catalog],
        }
    return dict(match)


# One WARNING per (tool, endpoint) — a plan-gated endpoint tried by several
# agents in one run should say so once, not once per agent.
_plan_warned: set[tuple[str, str]] = set()


def fmp_call(
    tool: str,
    endpoint: str,
    params: dict | str | None = None,
    save_as: str | None = None,
    preview_rows: int | None = 3,
) -> dict:
    """
    Call one Financial Modeling Prep endpoint and return its data.

    Use fmp_catalog first to find the right tool and endpoint. Data comes back in
    FMP's own field names — read "fields" in the response to see what you got
    rather than assuming names.

    Large responses are written to a JSON file in the run workspace instead of
    being returned inline; you get "fields", a short "preview", and "saved_to".
    Use run_python to compute over the saved file.

    Args:
        tool: Category tool, e.g. "statements", "chart", "company", "news".
        endpoint: Endpoint within that tool, e.g. "income-statement".
        params: Endpoint arguments, e.g. {"symbol": "AAPL", "limit": 8}.
            Two quirks worth knowing: the "news" tool wants "symbols" as a list
            (["AAPL"]), not a string; secFilings search endpoints require
            "from_date" and "to_date".
        save_as: Force the payload to a file with this name, even when small.
        preview_rows: How many rows to show inline when the payload is spilled.

    Returns:
        {"tool", "endpoint", "row_count", "fields", "preview", "rows"?, "saved_to"?}
        or {"error", "kind"} — this never raises.
    """
    # params arrives as a JSON string often enough to be worth handling here as
    # well as in the bridge, since this is a plain function others may call.
    if isinstance(params, str):
        try:
            params = json.loads(params) if params.strip() else {}
        except json.JSONDecodeError:
            return {
                "error": f"params was a string but not valid JSON: {params[:200]}",
                "kind": "bad_request",
            }
    if params is not None and not isinstance(params, dict):
        return {
            "error": f"params must be an object, got {type(params).__name__}",
            "kind": "bad_request",
        }

    args = dict(params or {})
    args["endpoint"] = endpoint

    try:
        # call_tools, not call_tool: args is caller-supplied and may contain any
        # key at all, so it must never be splatted into a Python signature.
        payload = call_tools([(tool, args)])[0]
    except FmpPlanDenied as exc:
        key = (tool, endpoint)
        if key not in _plan_warned:
            _plan_warned.add(key)
            _log.warning(
                "%s/%s: FMP subscription does not cover this endpoint (%s)",
                tool, endpoint, exc,
            )
        return {
            "error": str(exc),
            "kind": "plan_denied",
            "tool": tool,
            "endpoint": endpoint,
        }
    except FmpShuttingDown as exc:
        _log.info("%s/%s: skipped, interpreter is shutting down", tool, endpoint)
        return {"error": str(exc), "kind": "shutting_down"}
    except FmpError as exc:
        message = str(exc)
        kind = "bad_request" if "validation" in message.lower() else "unavailable"
        _log.error("%s/%s: %s", tool, endpoint, message)
        return {"error": message, "kind": kind, "tool": tool, "endpoint": endpoint}

    return _shape(tool, endpoint, payload, save_as, preview_rows)


def _shape(
    tool: str,
    endpoint: str,
    payload: Any,
    save_as: str | None,
    preview_rows: int | None,
) -> dict:
    """Package a decoded payload, spilling to the workspace when it is large."""
    rows = payload if isinstance(payload, list) else [payload]
    rows = [r for r in rows if r is not None]

    fields: list[str] = []
    for row in rows:
        if isinstance(row, dict):
            fields = list(row.keys())
            break

    result: dict[str, Any] = {
        "tool": tool,
        "endpoint": endpoint,
        "row_count": len(rows),
        "fields": fields,
    }
    if not rows:
        result["rows"] = []
        result["note"] = "FMP returned no rows for these arguments."
        return result

    blob = json.dumps(rows, default=str)
    if save_as is None and len(blob) <= _INLINE_LIMIT:
        result["rows"] = rows
        return result

    name = workspace.slug(save_as or f"{tool}_{endpoint}")
    if not name.endswith(".json"):
        name += ".json"
    path = workspace.data_dir() / name
    path.write_text(blob, encoding="utf-8")

    result["saved_to"] = workspace.relative(path)
    result["preview"] = rows[: max(preview_rows if preview_rows is not None else 3, 0)]
    result["note"] = (
        f"{len(rows)} rows ({len(blob):,} bytes) written to "
        f"{result['saved_to']} — load it with run_python rather than "
        "asking for it inline."
    )
    return result
