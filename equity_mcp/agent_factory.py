"""
Agent factory: filters the MCP tool list by agent role and runs the
Claude API tool-use loop.

Usage:
    import asyncio
    from equity_mcp.agent_factory import run_agent
    from equity_mcp.roles import ROLE_VALUE

    result = asyncio.run(run_agent(ROLE_VALUE, "AAPL", "Produce a value investment thesis"))
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import anthropic
from fastmcp import Client

from equity_mcp.langchain_bridge import _result_to_text, _tags_of
from equity_mcp.roles import ALL_ROLES
from equity_mcp.server import mcp

_MODEL = "claude-sonnet-4-6"
_MAX_TOKENS = 8096
_MAX_TOOL_ROUNDS = 15  # safety cap on tool-call iterations
_PROMPTS_DIR = Path(__file__).parent / "prompts"


def load_system_prompt(agent_role: str) -> str:
    """Load the system prompt for the given role from prompts/<role>.md."""
    prompt_file = _PROMPTS_DIR / f"{agent_role}.md"
    if prompt_file.exists():
        return prompt_file.read_text()
    return f"You are the {agent_role.replace('_', ' ').title()} agent in an equity research team."


async def _list_agent_tools(agent_role: str) -> list[dict]:
    """
    Connect to the in-process MCP server, list all tools, and return only
    those whose tags include the agent's role OR 'shared'.
    Tools are returned in Anthropic tool format.
    """
    async with Client(mcp) as client:
        all_tools = await client.list_tools()

    agent_tools = [
        t for t in all_tools
        if agent_role in _tags_of(t) or "shared" in _tags_of(t)
    ]

    return [
        {
            "name": t.name,
            "description": t.description or "",
            "input_schema": t.inputSchema if hasattr(t, "inputSchema") else t.parameters,
        }
        for t in agent_tools
    ]


async def _call_mcp_tool(tool_name: str, tool_input: dict) -> str:
    """Execute a single MCP tool call and return the result as a JSON string."""
    async with Client(mcp) as client:
        result = await client.call_tool(tool_name, tool_input)

    return _result_to_text(result)


async def run_agent(
    agent_role: str,
    symbol: str,
    task: str,
    extra_context: str = "",
) -> dict:
    """
    Run a single agent for a given symbol and task.

    Returns:
        {
          "agent_role": str,
          "symbol": str,
          "output": str,       # final text response
          "tool_calls": int,   # number of tool calls made
        }
    """
    if agent_role not in ALL_ROLES:
        raise ValueError(f"Unknown role '{agent_role}'. Valid roles: {ALL_ROLES}")

    anthropic_client = anthropic.AsyncAnthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    tools = await _list_agent_tools(agent_role)
    system_prompt = load_system_prompt(agent_role)

    user_content = f"Symbol: {symbol}\nTask: {task}"
    if extra_context:
        user_content += f"\n\nAdditional context:\n{extra_context}"

    messages: list[dict] = [{"role": "user", "content": user_content}]
    total_tool_calls = 0

    for _ in range(_MAX_TOOL_ROUNDS):
        response = await anthropic_client.messages.create(
            model=_MODEL,
            max_tokens=_MAX_TOKENS,
            system=system_prompt,
            tools=tools,
            messages=messages,
        )

        # Append assistant message
        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason != "tool_use":
            break

        # Execute all tool calls in this round
        tool_results = []
        for block in response.content:
            if block.type != "tool_use":
                continue
            total_tool_calls += 1
            tool_output = await _call_mcp_tool(block.name, block.input)
            tool_results.append(
                {
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": tool_output,
                }
            )

        messages.append({"role": "user", "content": tool_results})

    # Extract final text
    final_text = ""
    for block in response.content:
        if hasattr(block, "text"):
            final_text += block.text

    return {
        "agent_role": agent_role,
        "symbol": symbol,
        "output": final_text.strip(),
        "tool_calls": total_tool_calls,
    }


async def run_agents_parallel(
    agent_roles: list[str],
    symbol: str,
    task_map: dict[str, str] | None = None,
    default_task: str = "Conduct your analysis for this company.",
) -> list[dict]:
    """
    Run multiple agents concurrently for the same symbol.
    task_map optionally maps role -> task string; falls back to default_task.
    """
    import asyncio

    tasks = [
        run_agent(
            role,
            symbol,
            task_map.get(role, default_task) if task_map else default_task,
        )
        for role in agent_roles
    ]
    return await asyncio.gather(*tasks, return_exceptions=False)
