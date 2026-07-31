"""
Bridges the FastMCP tool registry to LangChain StructuredTool format.

Uses the in-process FastMCP client to list all registered tools with their
role tags, then wraps each matching tool as a LangChain StructuredTool whose
coroutine calls back into the same in-process MCP server.  The deepagents
subagents consume this list, so they run on the same tool implementations the
MCP server exposes — nothing in equity_mcp/tools/ changes.
"""

from __future__ import annotations

import json
from typing import Any, Optional

from fastmcp import Client
from langchain_core.tools import StructuredTool
from pydantic import Field, create_model

from equity_mcp.server import mcp

_TYPE_MAP: dict[str, type] = {
    "string":  str,
    "integer": int,
    "number":  float,
    "boolean": bool,
    "array":   list,
    "object":  dict,
}


def _py_type(prop: dict) -> Any:
    """
    Best Python type for one JSON Schema property.

    A union ("anyOf"/"oneOf", which is how a `dict | str` annotation reaches us)
    resolves to Any rather than to one arm — narrowing it would reject the other.
    An unrecognised schema also resolves to Any: guessing `str` is what made
    `params: dict | str` reject the dicts it was widened to accept.
    """
    kind = prop.get("type")
    if isinstance(kind, str):
        return _TYPE_MAP.get(kind, Any)
    if isinstance(kind, list):  # e.g. ["integer", "null"]
        concrete = [k for k in kind if k != "null"]
        return _TYPE_MAP.get(concrete[0], Any) if len(concrete) == 1 else Any
    return Any


def _schema_to_pydantic(schema: dict, tool_name: str):
    """
    Convert an MCP JSON Schema input definition to a Pydantic model class
    suitable for use as a LangChain StructuredTool args_schema.
    Returns None when the schema has no properties (no-arg tools).

    Optional fields keep the schema's own default rather than being forced to
    None.  That distinction is load-bearing: FastMCP validates the *server*
    signature, where `preview_rows: int = 3` will not accept null, so advertising
    the parameter as nullable invites the model to send a null that the server
    then rejects — and a validation error aborts the whole graph rather than
    coming back as feedback.
    """
    props    = schema.get("properties", {})
    required = set(schema.get("required", []))

    if not props:
        return None

    fields: dict[str, Any] = {}
    for name, prop in props.items():
        py_type  = _py_type(prop)
        desc     = prop.get("description", "")
        if name in required:
            fields[name] = (py_type, Field(..., description=desc))
        else:
            fields[name] = (
                Optional[py_type],
                Field(prop.get("default"), description=desc),
            )

    return create_model(f"{tool_name}_input", **fields)


def _maybe_json(value: str) -> Any:
    """
    Decode *value* if it is a JSON object or array, else None.

    Deliberately narrow: only text that starts with "{" or "[" is a candidate, so
    a genuine string argument that happens to be valid JSON — a bare number, a
    quoted ticker — is never silently retyped.
    """
    text = value.strip()
    if not text or text[0] not in "{[":
        return None
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None


def _tool_tags(tool: Any) -> set[str]:
    """
    Extract the FastMCP role tags from a tool returned by client.list_tools().

    The MCP wire type (mcp.types.Tool) has no .tags attribute — FastMCP carries
    them through as meta["fastmcp"]["tags"].  Older FastMCP versions exposed a
    .tags attribute directly, so that is checked as a fallback.
    """
    meta = getattr(tool, "meta", None) or {}
    tags = (meta.get("fastmcp") or {}).get("tags")
    if tags is None:
        tags = getattr(tool, "tags", None) or ()
    return set(tags)


def _render(result: Any) -> str:
    """
    Flatten a fastmcp CallToolResult into the string LangChain expects.

    Prefer structured content — our tools return dicts, and their JSON survives
    the round trip better than the text rendering — then fall back to the text
    content blocks.  CallToolResult is not iterable in current fastmcp, so this
    goes through .structured_content / .content explicitly.
    """
    structured = getattr(result, "structured_content", None)
    if isinstance(structured, dict) and structured:
        # fastmcp wraps non-dict returns under a single "result" key.
        payload = (
            structured["result"]
            if len(structured) == 1 and "result" in structured
            else structured
        )
        return json.dumps(payload, default=str)

    blocks = getattr(result, "content", None)
    if blocks is None:
        blocks = result if isinstance(result, (list, tuple)) else []

    parts: list[str] = []
    for item in blocks:
        if getattr(item, "text", None):
            parts.append(item.text)
        elif hasattr(item, "model_dump"):
            parts.append(json.dumps(item.model_dump(), default=str))
        else:
            parts.append(str(item))

    return "\n".join(parts) if parts else "No output"


def _make_async_caller(tool_name: str):
    """
    Return an async function that calls the named MCP tool via the in-process
    FastMCP client.  Each call opens a fresh client context to avoid sharing
    connection state across concurrent subagent executions.

    Two accommodations for how models actually emit tool calls:

    - Unset optional arguments are dropped rather than sent as null, so the
      server applies its own defaults.
    - A JSON *string* where an object or array is expected is decoded first.
      Models serialise nested arguments this way routinely, and the MCP schema
      gives them little to go on — `_TYPE_MAP` flattens "object" to a bare dict
      with no properties.

    Errors come back as text instead of propagating.  A raised tool error is not
    recoverable in LangGraph — it aborts the whole run — whereas a message the
    agent can read lets it correct the call and continue.
    """
    async def _call(**kwargs: Any) -> str:
        args = {k: v for k, v in kwargs.items() if v is not None}
        for key, value in list(args.items()):
            if isinstance(value, str):
                decoded = _maybe_json(value)
                if decoded is not None:
                    args[key] = decoded

        try:
            async with Client(mcp) as client:
                result = await client.call_tool(tool_name, args)
        except Exception as exc:
            return f"Tool {tool_name} failed: {exc}"

        return _render(result)

    # Give the coroutine a stable __name__ for LangChain introspection
    _call.__name__ = f"call_{tool_name}"
    return _call


async def get_langchain_tools_for_role(role: str) -> list[StructuredTool]:
    """
    Return LangChain StructuredTool instances for every FastMCP tool whose
    tags include *role* or the universal "shared" tag.

    This is the single enforcement point for per-agent tool access.  Note it
    depends on role constants in roles.py NOT containing "shared" — a role set
    that carries it matches every role and silently makes the tool universal.
    """
    async with Client(mcp) as client:
        all_tools = await client.list_tools()

    role_tools = [
        t for t in all_tools
        if {role, "shared"} & _tool_tags(t)
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
