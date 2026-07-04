"""
Bridges the FastMCP tool registry to LangChain StructuredTool format.

Uses the in-process FastMCP client to list all registered tools with their
role tags, then wraps each matching tool as a LangChain StructuredTool whose
coroutine calls back into the same in-process MCP server.  This lets deepagents
subagents use exactly the same tool implementations as the original Anthropic
tool-use loop — nothing in equity_mcp/tools/ changes.
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


def _make_async_caller(tool_name: str):
    """
    Return an async function that calls the named MCP tool via the in-process
    FastMCP client.  Each call opens a fresh client context to avoid sharing
    connection state across concurrent subagent executions.
    """
    async def _call(**kwargs: Any) -> str:
        async with Client(mcp) as client:
            result = await client.call_tool(tool_name, kwargs)

        parts: list[str] = []
        for item in result:
            if hasattr(item, "text"):
                parts.append(item.text)
            elif hasattr(item, "model_dump"):
                parts.append(json.dumps(item.model_dump(), default=str))
            else:
                parts.append(str(item))

        return "\n".join(parts) if parts else "No output"

    # Give the coroutine a stable __name__ for LangChain introspection
    _call.__name__ = f"call_{tool_name}"
    return _call


async def get_langchain_tools_for_role(role: str) -> list[StructuredTool]:
    """
    Return LangChain StructuredTool instances for every FastMCP tool whose
    tags include *role* or the universal "shared" tag.

    The tag check mirrors agent_factory._list_agent_tools exactly so both
    execution paths enforce the same access control.
    """
    async with Client(mcp) as client:
        all_tools = await client.list_tools()

    role_tools = [
        t for t in all_tools
        if role in (t.tags or set()) or "shared" in (t.tags or set())
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
