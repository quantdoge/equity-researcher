"""
Agent factory: resolves the model and tool set for an agent role and runs a
tool-use loop against it.

Tools come from the shared FastMCP server via langchain_bridge, filtered by
role tag.  The model comes from roles.model_for_role, so each agent can run on
its own OpenRouter model.

Usage:
    import asyncio
    from equity_mcp.agent_factory import run_agent
    from equity_mcp.roles import ROLE_VALUE

    result = asyncio.run(run_agent(ROLE_VALUE, "AAPL", "Produce a value investment thesis"))
"""

from __future__ import annotations

import asyncio
from pathlib import Path

from langchain.chat_models import init_chat_model
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage, ToolMessage

from equity_mcp.langchain_bridge import get_langchain_tools_for_role
from equity_mcp.roles import ALL_ROLES, model_for_role

_MAX_TOKENS = 8096
_MAX_TOOL_ROUNDS = 15  # safety cap on tool-call iterations
_PROMPTS_DIR = Path(__file__).parent / "prompts"


def load_system_prompt(agent_role: str) -> str:
    """Load the system prompt for the given role from prompts/<role>.md."""
    prompt_file = _PROMPTS_DIR / f"{agent_role}.md"
    if prompt_file.exists():
        return prompt_file.read_text()
    return f"You are the {agent_role.replace('_', ' ').title()} agent in an equity research team."


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

    tools = await get_langchain_tools_for_role(agent_role)
    tools_by_name = {t.name: t for t in tools}

    llm = init_chat_model(
        model_for_role(agent_role),
        max_tokens=_MAX_TOKENS,
    ).bind_tools(tools)

    user_content = f"Symbol: {symbol}\nTask: {task}"
    if extra_context:
        user_content += f"\n\nAdditional context:\n{extra_context}"

    messages: list[BaseMessage] = [
        SystemMessage(load_system_prompt(agent_role)),
        HumanMessage(user_content),
    ]
    total_tool_calls = 0

    for _ in range(_MAX_TOOL_ROUNDS):
        ai = await llm.ainvoke(messages)
        messages.append(ai)

        if not ai.tool_calls:
            break

        for call in ai.tool_calls:
            total_tool_calls += 1
            tool = tools_by_name.get(call["name"])
            if tool is None:
                output = f"Error: unknown tool '{call['name']}'"
            else:
                try:
                    output = await tool.ainvoke(call["args"])
                except Exception as exc:  # a bad tool call degrades, never crashes
                    output = f"Tool error: {exc}"
            messages.append(
                ToolMessage(
                    content=str(output),
                    tool_call_id=call["id"],
                    name=call["name"],
                )
            )

    return {
        "agent_role": agent_role,
        "symbol": symbol,
        "output": str(ai.text).strip(),
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
    tasks = [
        run_agent(
            role,
            symbol,
            task_map.get(role, default_task) if task_map else default_task,
        )
        for role in agent_roles
    ]
    return await asyncio.gather(*tasks, return_exceptions=False)
