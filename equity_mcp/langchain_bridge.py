"""
Bridges the FastMCP tool registry to LangChain StructuredTool format.

Lists all registered tools with their role tags once, caches that listing, and
wraps each matching tool as a LangChain StructuredTool whose coroutine calls
back into the same in-process MCP server.  This lets deepagents subagents use
exactly the same tool implementations as the original Anthropic tool-use loop —
nothing in equity_mcp/tools/ changes.

Two properties matter for the parallel orchestrator:

* **Off-loop execution.**  Every tool in equity_mcp/tools/ is a plain sync
  function doing blocking psycopg / requests I/O.  FastMCP 3.x dispatches sync
  tools to worker threads, but 2.x calls them inline on the event loop — where
  a single 20 s SEC EDGAR fetch stalls every other specialist running
  concurrently.  Each call is therefore dispatched to a dedicated thread pool
  regardless of FastMCP version.  Measured overhead of the extra hop is ~1 ms
  against tool calls that take 100 ms – 20 s.

* **Version-tolerant introspection.**  Where the tag metadata and the call
  result live has moved between FastMCP releases; see _tags_of and
  _result_to_text.
"""

from __future__ import annotations

import asyncio
import json
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Optional

from fastmcp import Client
from langchain_core.tools import StructuredTool
from pydantic import Field, create_model

from equity_mcp.server import mcp

# Wall-clock ceiling for a single tool call.  Nothing in equity_mcp/tools/
# retries or backs off, and several external APIs (SEC EDGAR, PatentsView,
# pytrends) can hang until their own 20-30 s timeouts.  Bounding it here means
# one dead API degrades a single specialist instead of the whole run.
_TOOL_TIMEOUT_S = 90.0

# Sized for ~12 specialists making overlapping tool calls.  The default
# asyncio.to_thread executor (min(32, cpu+4)) is too small and would silently
# re-serialize the fan-out on a small container.
_MAX_TOOL_THREADS = 48

_EXECUTOR = ThreadPoolExecutor(
    max_workers=_MAX_TOOL_THREADS, thread_name_prefix="mcp-tool"
)

_TYPE_MAP: dict[str, type] = {
    "string":  str,
    "integer": int,
    "number":  float,
    "boolean": bool,
    "array":   list,
    "object":  dict,
}

# Populated once by _list_tools_once; 13 roles filter the same listing.
_TOOL_CACHE: list[Any] | None = None
_TOOL_CACHE_LOCK = asyncio.Lock()


def _tags_of(tool: Any) -> set[str]:
    """
    Return a tool's FastMCP tags, whichever way this FastMCP version exposes them.

    The tags are the entire access-control mechanism, so this must not silently
    return an empty set on an unrecognised layout — a role would then see only
    its own explicitly-tagged tools and lose everything tagged SHARED.

    Known layouts:
      * older FastMCP  — ``tool.tags`` (a set) on FastMCP's own Tool type
      * FastMCP 2.14.x — ``tool.meta["_fastmcp"]["tags"]`` (mcp.types.Tool)
      * FastMCP 3.x    — ``tool.meta["fastmcp"]["tags"]``  (mcp.types.Tool)
    """
    direct = getattr(tool, "tags", None)
    if direct:
        return set(direct)

    meta = getattr(tool, "meta", None) or {}
    for namespace in ("_fastmcp", "fastmcp"):
        section = meta.get(namespace) or {}
        tags = section.get("tags")
        if tags:
            return set(tags)

    raise RuntimeError(
        f"Could not read FastMCP tags for tool {getattr(tool, 'name', tool)!r}. "
        "Role-based tool access cannot be enforced — check whether this FastMCP "
        "version changed where tool metadata is exposed."
    )


def _result_to_text(result: Any) -> str:
    """
    Flatten a FastMCP call result to the text an LLM sees.

    Modern FastMCP returns a CallToolResult (not iterable, carries .content and
    .data); older releases returned a bare list of content blocks.
    """
    content = getattr(result, "content", None)
    if content is None and not isinstance(result, (list, tuple)):
        # Structured-only result with no content blocks.
        data = getattr(result, "data", None)
        return json.dumps(data, default=str) if data is not None else "No output"

    items = content if content is not None else result

    parts: list[str] = []
    for item in items:
        if hasattr(item, "text"):
            parts.append(item.text)
        elif hasattr(item, "model_dump"):
            parts.append(json.dumps(item.model_dump(), default=str))
        else:
            parts.append(str(item))

    return "\n".join(parts) if parts else "No output"


def _schema_to_pydantic(schema: dict, tool_name: str):
    """
    Convert an MCP JSON Schema input definition to a Pydantic model class
    suitable for use as a LangChain StructuredTool args_schema.
    Returns None when the schema has no properties (no-arg tools).
    """
    props    = schema.get("properties", {})
    required = set(schema.get("required", []))

    if not props:
        return None

    fields: dict[str, Any] = {}
    for name, prop in props.items():
        py_type  = _TYPE_MAP.get(prop.get("type", "string"), str)
        desc     = prop.get("description", "")
        if name in required:
            fields[name] = (py_type, Field(..., description=desc))
        else:
            fields[name] = (Optional[py_type], Field(None, description=desc))

    return create_model(f"{tool_name}_input", **fields)


def _blocking_call(tool_name: str, kwargs: dict[str, Any]) -> str:
    """
    Run one MCP tool call to completion on a worker thread.

    Owns its own event loop and its own in-process client, so the blocking
    psycopg / requests work inside the tool body cannot touch the orchestrator's
    event loop.  Opening a fresh in-process client costs ~1 ms.
    """
    async def _inner() -> str:
        async with Client(mcp) as client:
            return _result_to_text(await client.call_tool(tool_name, kwargs))

    return asyncio.run(_inner())


def _make_async_caller(tool_name: str):
    """Return an async function that calls the named MCP tool off the event loop."""
    async def _call(**kwargs: Any) -> str:
        # LangChain materialises every optional field, so unsupplied arguments
        # arrive as None.  Forwarding those would override the tool's own
        # defaults (e.g. n_periods=8 becoming LIMIT NULL); drop them instead.
        supplied = {k: v for k, v in kwargs.items() if v is not None}

        loop = asyncio.get_running_loop()
        future = loop.run_in_executor(_EXECUTOR, _blocking_call, tool_name, supplied)
        try:
            return await asyncio.wait_for(future, timeout=_TOOL_TIMEOUT_S)
        except asyncio.TimeoutError:
            return (
                f"Tool '{tool_name}' timed out after {_TOOL_TIMEOUT_S:.0f}s. "
                "Proceed without this data and note the gap in your analysis."
            )
        except Exception as exc:  # surface as text, don't kill the specialist
            return f"Tool '{tool_name}' failed: {type(exc).__name__}: {exc}"

    # Give the coroutine a stable __name__ for LangChain introspection
    _call.__name__ = f"call_{tool_name}"
    return _call


async def _list_tools_once() -> list[Any]:
    """
    List the MCP tool registry once per process and cache it.

    Previously each of the 13 roles opened its own client and re-serialised all
    61 tools at startup.
    """
    global _TOOL_CACHE
    if _TOOL_CACHE is not None:
        return _TOOL_CACHE

    async with _TOOL_CACHE_LOCK:
        if _TOOL_CACHE is None:
            async with Client(mcp) as client:
                _TOOL_CACHE = await client.list_tools()
    return _TOOL_CACHE


async def get_langchain_tools_for_role(role: str) -> list[StructuredTool]:
    """
    Return LangChain StructuredTool instances for every FastMCP tool whose
    tags include *role* or the universal "shared" tag.

    The tag check mirrors agent_factory._list_agent_tools exactly so both
    execution paths enforce the same access control.
    """
    all_tools = await _list_tools_once()

    role_tools = [
        t for t in all_tools
        if role in _tags_of(t) or "shared" in _tags_of(t)
    ]

    lc_tools: list[StructuredTool] = []
    for t in role_tools:
        args_schema = _schema_to_pydantic(t.inputSchema or {}, t.name)

        lc_tools.append(
            StructuredTool(
                name=t.name,
                description=t.description or "",
                coroutine=_make_async_caller(t.name),
                args_schema=args_schema,
            )
        )

    return lc_tools
