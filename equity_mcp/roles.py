"""
Canonical tag sets and model assignments for each agent role.

langchain_bridge filters the MCP tool list by checking whether the agent's own
role tag OR "shared" appears in each tool's tags.  A role constant therefore
holds *only* its own role: a tool tagged VALUE reaches the value researcher and
nobody else, while a tool tagged SHARED reaches everyone.

Do not put "shared" back into the role constants.  They used to carry it, which
silently defeated the filter — every union that mentioned any role also carried
"shared" and so matched all roles, making supposedly-gated tools universal.

Since every agent reaches Financial Modeling Prep through the same fmp_catalog /
fmp_call pair, data access no longer varies by role and almost everything is
tagged SHARED.  The one tag that still gates anything is QUANT_ENGINEER, which
holds the code-execution tools.

This module is also the single source of truth for which model each agent
runs on — see DEFAULT_MODEL, AGENT_MODELS and model_for_role below, and
chat_model_for_role, which turns that spec into the configured client the agents
actually run on.
"""

from __future__ import annotations

import os
from collections.abc import Iterable
from typing import Any

SHARED: set[str] = {"shared"}

HEAD_OF_RESEARCH: set[str]    = {"head_of_research"}
QUANT_ENGINEER:   set[str]    = {"quant_engineer"}
SECTOR:           set[str]    = {"sector_researcher"}
GEO_LEGAL:        set[str]    = {"geo_legal_researcher"}
MACRO:            set[str]    = {"macro_researcher"}
VALUE:            set[str]    = {"value_researcher"}
GROWTH:           set[str]    = {"growth_researcher"}
FIN_RISK:         set[str]    = {"fin_risk_analyst"}
NONFIN_RISK:      set[str]    = {"nonfin_risk_analyst"}
QUANT:            set[str]    = {"quant_analyst"}
SHORT:            set[str]    = {"short_analyst"}
ESG:              set[str]    = {"esg_analyst"}
ALT_DATA:         set[str]    = {"alt_data_analyst"}
PORTFOLIO:        set[str]    = {"portfolio_strategist"}

# Canonical role name strings — the subagent names and prompt file stems
ROLE_HEAD_OF_RESEARCH    = "head_of_research"
ROLE_QUANT_ENGINEER      = "quant_engineer"
ROLE_SECTOR              = "sector_researcher"
ROLE_GEO_LEGAL           = "geo_legal_researcher"
ROLE_MACRO               = "macro_researcher"
ROLE_VALUE               = "value_researcher"
ROLE_GROWTH              = "growth_researcher"
ROLE_FIN_RISK            = "fin_risk_analyst"
ROLE_NONFIN_RISK         = "nonfin_risk_analyst"
ROLE_QUANT               = "quant_analyst"
ROLE_SHORT               = "short_analyst"
ROLE_ESG                 = "esg_analyst"
ROLE_ALT_DATA            = "alt_data_analyst"
ROLE_PORTFOLIO           = "portfolio_strategist"

ALL_ROLES: list[str] = [
    ROLE_HEAD_OF_RESEARCH,
    ROLE_QUANT_ENGINEER,
    ROLE_SECTOR,
    ROLE_GEO_LEGAL,
    ROLE_MACRO,
    ROLE_VALUE,
    ROLE_GROWTH,
    ROLE_FIN_RISK,
    ROLE_NONFIN_RISK,
    ROLE_QUANT,
    ROLE_SHORT,
    ROLE_ESG,
    ROLE_ALT_DATA,
    ROLE_PORTFOLIO,
]

# ── Model selection ───────────────────────────────────────────────────────────
# Every agent runs on OpenRouter.  DEFAULT_MODEL applies to any role with no
# entry in AGENT_MODELS.  Values are bare OpenRouter slugs; model_for_role()
# adds the "openrouter:" provider prefix that LangChain's init_chat_model wants.

DEFAULT_MODEL: str = "deepseek/deepseek-v4-flash-0731"

# Per-agent overrides.  role string -> OpenRouter slug.  Empty by default —
# uncomment or add entries to point individual specialists at cheaper or
# stronger models without touching any other file.
AGENT_MODELS: dict[str, str] = {
    ROLE_HEAD_OF_RESEARCH:  "deepseek/deepseek-v4-pro-0813",
    ROLE_QUANT_ENGINEER: "z-ai/glm-5.3",
    ROLE_ALT_DATA: "z-ai/glm-5.3"
}


def model_for_role(role: str) -> str:
    """
    Return the LangChain model spec for *role*.

    Looks up AGENT_MODELS, falling back to DEFAULT_MODEL, then prefixes the
    slug with the "openrouter:" provider so init_chat_model routes it through
    ChatOpenRouter.  A value that already carries a "<provider>:" prefix is
    passed through untouched, so a role can be pinned to a non-OpenRouter
    provider when needed.
    """
    if role not in ALL_ROLES:
        raise ValueError(f"Unknown role '{role}'. Valid roles: {ALL_ROLES}")

    slug = AGENT_MODELS.get(role, DEFAULT_MODEL)

    # A provider name never contains "/", but OpenRouter variant suffixes
    # ("...:free", "...:nitro") always come after one — that's how the two
    # meanings of ":" are told apart.
    head, sep, _ = slug.partition(":")
    if sep and "/" not in head:
        return slug
    return f"openrouter:{slug}"


# ── Model transport ───────────────────────────────────────────────────────────
# chat_model_for_role builds the chat model itself rather than handing
# deep_agent_factory the bare spec string, because two of ChatOpenRouter's
# defaults are actively hostile to a run that lasts half an hour.
#
# streaming=False means one POST held open with zero bytes flowing until the
# model has finished the whole completion.  Over a long run OpenRouter's edge
# closes some of those sockets before the first response byte, which surfaces as
# `httpx.RemoteProtocolError: Server disconnected without sending a response`
# raised from _receive_response_headers.  Streaming keeps bytes moving, so the
# connection never looks idle.  It is a transport change only: _agenerate routes
# through _astream + agenerate_from_stream and still returns one complete
# AIMessage, with tool calls reassembled from the chunks.
#
# request_timeout=None is not "use the default" — the SDK passes it straight into
# httpx's build_request, and an explicit None there means Timeout(None), i.e. no
# ceiling at all.  A stalled call would hang until the server hung up.  With
# streaming the explicit value below is a between-chunks read timeout, which is
# the semantics worth having.
#
# The SDK's own max_retries does *not* cover the disconnect above:
# openrouter.utils.retries honours retry_connection_errors only for
# httpx.ConnectError and httpx.TimeoutException, and classifies everything else —
# RemoteProtocolError included — as permanent.  That gap is covered by the
# ModelRetryMiddleware in middleware_for_role.

REQUEST_TIMEOUT_MS: int = 600_000

# Shown on the OpenRouter activity page.  Passing a model instance bypasses
# deepagents' provider profile, which would otherwise supply attribution and the
# provider routing preference below, so both are set here instead of silently
# lost.  ChatOpenRouter reads OPENROUTER_APP_URL / OPENROUTER_APP_TITLE from the
# environment, so those fields are left alone when the user has set them.
_APP_URL   = "https://github.com/quantdoge/equity-researcher"
_APP_TITLE = "equity-researcher"

_PROVIDER_ROUTING: dict[str, Any] = {"ignore": ["azure"]}


def chat_model_for_role(role: str) -> Any:
    """
    Build the chat model *role* runs on, configured for a long multi-agent run.

    One instance per call, deliberately uncached: a module-level cache would
    outlive the event loop it first served, and a pooled connection left over
    from a dead loop is a new failure mode.  The pools connect lazily, so
    fourteen of them cost nothing.

    streaming and timeout are provider-agnostic and always applied.  The
    attribution and routing kwargs are ChatOpenRouter's alone, so they are only
    passed when the role actually resolves to OpenRouter — model_for_role lets a
    role be pinned elsewhere, and that model would reject them.
    """
    # Imported here for the same reason as the middleware imports below — a
    # top-level import would pull the LangChain stack into a bare `fastmcp run`.
    from langchain.chat_models import init_chat_model

    spec = model_for_role(role)

    kwargs: dict[str, Any] = {
        "streaming": True,
        "timeout":   REQUEST_TIMEOUT_MS,
    }

    if spec.startswith("openrouter:"):
        kwargs["openrouter_provider"] = _PROVIDER_ROUTING
        if not os.getenv("OPENROUTER_APP_URL"):
            kwargs["app_url"] = _APP_URL
        if not os.getenv("OPENROUTER_APP_TITLE"):
            kwargs["app_title"] = _APP_TITLE

    return init_chat_model(spec, **kwargs)


# ── Call limits ───────────────────────────────────────────────────────────────
# Budgets attached as LangChain middleware by middleware_for_role(), which
# deep_agent_factory passes to each subagent spec and to create_deep_agent.
# Both limits are *run* limits: one graph invocation.  A subagent's counters
# therefore reset on every delegation, which is what you want — the budget bounds
# one task, not the specialist's whole participation in a run.

DEFAULT_TOOL_RUN_LIMIT: int | None = 10

# Tool name -> calls per run, applied to every agent that holds the tool.
# Anything absent gets DEFAULT_TOOL_RUN_LIMIT.  None or 0 means uncapped.
TOOL_CALL_LIMITS: dict[str, int | None] = {
    # "fmp_call": 25,
}

# role -> {tool name -> calls per run}.  Wins over TOOL_CALL_LIMITS for that one
# role; tools it does not mention still fall through to the table above.
ROLE_TOOL_CALL_LIMITS: dict[str, dict[str, int | None]] = {
    # ROLE_QUANT_ENGINEER: {"run_python": 30, "fmp_call": 40},
}

DEFAULT_MODEL_RUN_LIMIT: int | None = 20

# role -> model calls per run.  None means uncapped.
MODEL_CALL_LIMITS: dict[str, int | None] = {
    # The master plans, delegates 13 times, reads 13 reports and writes the memo.
    # Any cap low enough to save tokens is low enough to end the run with
    # "Model call limits exceeded" where the Investment Memo should be.
    ROLE_HEAD_OF_RESEARCH: None,
}


def _normalise(limit: int | None) -> int | None:
    """Treat 0 the same as None — both mean "no ceiling", never "no calls"."""
    return limit if limit else None


def tool_run_limit(role: str, tool_name: str) -> int | None:
    """
    Calls per run *role* may make to *tool_name*, or None for uncapped.

    Resolution order: the role's own entry in ROLE_TOOL_CALL_LIMITS, then the
    flat TOOL_CALL_LIMITS table, then DEFAULT_TOOL_RUN_LIMIT.  A key present with
    a None value is distinct from a key absent, so a role can opt one tool out of
    a limit the flat table imposes.
    """
    per_role = ROLE_TOOL_CALL_LIMITS.get(role, {})
    if tool_name in per_role:
        return _normalise(per_role[tool_name])
    if tool_name in TOOL_CALL_LIMITS:
        return _normalise(TOOL_CALL_LIMITS[tool_name])
    return _normalise(DEFAULT_TOOL_RUN_LIMIT)


def model_run_limit(role: str) -> int | None:
    """Model calls per run for *role*, or None for uncapped."""
    return _normalise(MODEL_CALL_LIMITS.get(role, DEFAULT_MODEL_RUN_LIMIT))


def _transport_error_message(exc: Exception, request: Any) -> str | None:
    """
    on_error for the master's ToolErrorMiddleware.

    Returns text — which the library turns into an error ToolMessage — only for
    network faults escaping a `task` call, so a specialist that dies on a dropped
    connection costs one report instead of the whole memo.  Everything else
    returns None and propagates unchanged: an ordinary bug should surface as a
    traceback, not be quietly serialised into the master's context.

    Only the exception type is named.  Transport error messages are not
    especially sensitive, but there is no reason to hand the model a raw string
    from inside httpx when the type is what it needs to decide what to do.
    """
    import httpx

    if isinstance(exc, httpx.TransportError):
        name = getattr(request, "tool_call", {}).get("name", "subagent")
        return (
            f"`{name}` failed with a network error ({type(exc).__name__}) and its "
            "report was not produced. Delegate it again, or continue without it "
            "and say so in the memo."
        )
    return None


def middleware_for_role(role: str, tool_names: Iterable[str]) -> list[Any]:
    """
    Build the middleware stack for *role* — call budgets, plus resilience.

    One ToolCallLimitMiddleware per name in *tool_names* that resolves to a
    limit, plus at most one ModelCallLimitMiddleware.  *tool_names* is a
    parameter rather than a constant here so it can come from the tools the role
    actually received from the bridge — a hardcoded list would be a second copy
    of the registrations in server.py, free to drift.

    Only tools named here are capped.  deepagents' own built-ins (task,
    write_todos, ls, read_file, ...) are deliberately left alone: capping `task`
    at ten would strand three of the thirteen specialists.

    The two exit behaviours differ because the library's options do:

    - Tools use "continue", so an over-budget call comes back as an error
      ToolMessage the agent can read and work around.
    - Models use "end" — ModelCallLimitMiddleware accepts only "end" or "error",
      and "error" raises through the graph, killing the whole run over one
      runaway specialist.  "end" returns whatever the agent has so far.

    Both classes raise ValueError when every limit is None, so an uncapped
    subject gets no instance at all rather than one configured with nothing.

    Every role also gets a ModelRetryMiddleware for transport faults and a
    ProgressMiddleware for status and incremental output, and the master alone
    gets a ToolErrorMiddleware — see the comments at those call sites.
    Middleware names must be unique per agent (create_agent asserts on
    duplicates); the LangChain classes name themselves after their class, so
    there is exactly one instance of each, and ProgressMiddleware embeds the
    role in its name.
    """
    if role not in ALL_ROLES:
        raise ValueError(f"Unknown role '{role}'. Valid roles: {ALL_ROLES}")

    # Imported here, not at module scope: server.py imports this module, and a
    # top-level import would pull the whole LangChain agent stack into a bare
    # `fastmcp run` / `fastmcp inspect` that never builds an agent.
    import httpx
    from langchain.agents.middleware import (
        ModelCallLimitMiddleware,
        ModelRetryMiddleware,
        ToolCallLimitMiddleware,
        ToolErrorMiddleware,
    )

    middleware: list[Any] = []

    for name in tool_names:
        limit = tool_run_limit(role, name)
        if limit is None:
            continue
        middleware.append(
            ToolCallLimitMiddleware(
                tool_name=name,
                run_limit=limit,
                exit_behavior="continue",
            )
        )

    model_limit = model_run_limit(role)
    if model_limit is not None:
        middleware.append(
            ModelCallLimitMiddleware(run_limit=model_limit, exit_behavior="end")
        )

    # A run lasts long enough that some OpenRouter call will eventually have its
    # connection dropped, and the SDK's own max_retries does not cover it: it
    # honours retry_connection_errors only for ConnectError and TimeoutException
    # and treats RemoteProtocolError as permanent.  Without this, one dropped
    # socket inside one specialist raises through the `task` tool and kills the
    # whole run — thirty minutes of fetched data and finished reports discarded.
    #
    # httpx.TransportError is the common base of RemoteProtocolError, ReadTimeout
    # and ConnectError, so one entry covers the observed fault and its
    # neighbours.  on_failure="continue" turns an exhausted retry into an
    # AIMessage describing the failure, degrading one agent instead of the run.
    #
    # This does not eat into the model budget above: ModelCallLimitMiddleware
    # counts in before_model, a graph-node hook, while retries happen inside a
    # single wrap_model_call.
    middleware.append(
        ModelRetryMiddleware(
            max_retries=3,
            retry_on=(httpx.TransportError,),
            on_failure="continue",
            initial_delay=2.0,
            backoff_factor=2.0,
        )
    )

    # Second layer, master only: subagents reach it through the `task` tool, and
    # LangGraph re-raises anything that is not a ToolException, so an exception
    # escaping a specialist ends the run.  This converts network faults into an
    # error ToolMessage the Head of Research can route around; everything else
    # still propagates (see _transport_error_message).
    if role == ROLE_HEAD_OF_RESEARCH:
        middleware.append(ToolErrorMiddleware(_transport_error_message))

    # Status lines and per-agent report files.  Costs no tokens: its hooks only
    # observe — they return None or the handler's result untouched, so nothing
    # they do reaches a model.  See progress.py.
    from equity_mcp.progress import build_middleware

    middleware.append(build_middleware(role))

    return middleware
