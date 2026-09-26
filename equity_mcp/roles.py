"""
Canonical tag sets for each agent role.

Each per-role constant holds exactly one tag: that role's own name.  The
universal SHARED tag is separate and must be combined explicitly.  Filtering
(langchain_bridge._tags_of + get_langchain_tools_for_role) admits a tool when
the agent's role tag OR "shared" appears in the tool's tags — so a tool tagged
SHARED is universally visible while one tagged VALUE reaches only the value
researcher, and VALUE | SHARED reaches everyone.

These constants must NOT bundle "shared" into themselves.  They previously did,
which silently tagged all 61 tools as shared and handed every agent the entire
tool surface — defeating the access model and putting ~61 tool schemas in every
agent's context on every turn.
"""

import os
from typing import Any

SHARED: set[str] = {"shared"}

HEAD_OF_RESEARCH: set[str]    = {"head_of_research"}
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

# Canonical role name strings — used as the agent_role key in agent_factory
ROLE_HEAD_OF_RESEARCH    = "head_of_research"
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
# Every agent runs on OpenRouter, authenticated with OPENROUTER_API_KEY from the
# environment.  DEFAULT_MODEL applies to any role with no entry in AGENT_MODELS.
# Values are bare OpenRouter slugs; model_for_role() adds the "openrouter:"
# provider prefix that LangChain's init_chat_model wants.

DEFAULT_MODEL: str = "deepseek/deepseek-v4-flash-0731"

# Per-agent overrides.  role string -> OpenRouter slug.  Empty by default, so
# all 13 agents run DEFAULT_MODEL — add an entry to point one specialist at a
# cheaper or stronger model without touching any other file.
AGENT_MODELS: dict[str, str] = {
    # ROLE_HEAD_OF_RESEARCH: "deepseek/deepseek-v4-pro-0813",
}


def model_for_role(role: str) -> str:
    """
    Return the LangChain model spec for *role*.

    Looks up AGENT_MODELS, falling back to DEFAULT_MODEL, then prefixes the slug
    with the "openrouter:" provider so init_chat_model routes it through
    ChatOpenRouter.  A value that already carries a "<provider>:" prefix is
    passed through untouched, so a role can be pinned to a non-OpenRouter
    provider when needed.
    """
    if role not in ALL_ROLES:
        raise ValueError(f"Unknown role '{role}'. Valid roles: {ALL_ROLES}")

    slug = AGENT_MODELS.get(role, DEFAULT_MODEL)

    # A provider name never contains "/", but OpenRouter variant suffixes
    # ("...:free", "...:nitro") always come after one — that is how the two
    # meanings of ":" are told apart.
    head, sep, _ = slug.partition(":")
    if sep and "/" not in head:
        return slug
    return f"openrouter:{slug}"


# ── Model transport ───────────────────────────────────────────────────────────
# chat_model_for_role builds the chat model itself rather than handing
# deep_agent_factory a bare spec string, because two of ChatOpenRouter's
# defaults are hostile to a run that lasts half an hour.
#
# streaming=False means one POST held open with zero bytes flowing until the
# model has finished the whole completion.  Over a long run OpenRouter's edge
# closes some of those sockets before the first response byte, which surfaces as
# `httpx.RemoteProtocolError: Server disconnected without sending a response`.
# Streaming keeps bytes moving, so the connection never looks idle.  It is a
# transport change only: _agenerate routes through _astream and still returns
# one complete AIMessage, with tool calls reassembled from the chunks.
#
# request_timeout=None is not "use the default" — the SDK passes it straight
# into httpx's build_request, where an explicit None means no ceiling at all, so
# a stalled call would hang until the server hung up.
#
# Attribution and provider routing are ChatOpenRouter's alone, so they are only
# passed when the role actually resolves to OpenRouter.  ChatOpenRouter reads
# OPENROUTER_APP_URL / OPENROUTER_APP_TITLE from the environment, so those are
# left alone when the user has set them.

REQUEST_TIMEOUT_MS: int = 600_000

_APP_URL   = "https://github.com/quantdoge/equity-researcher"
_APP_TITLE = "equity-researcher"

_PROVIDER_ROUTING: dict[str, list[str]] = {"ignore": ["azure"]}


def chat_model_for_role(role: str, max_tokens: int | None = None) -> Any:
    """
    Build the chat model *role* runs on, configured for a long multi-agent run.

    One instance per call, deliberately uncached: a module-level cache would
    outlive the event loop it first served, and a pooled connection left over
    from a dead loop is a new failure mode.  The pools connect lazily, so
    thirteen of them cost nothing.
    """
    # Imported here, not at module scope, so that a bare `fastmcp run
    # equity_mcp/server.py` does not drag the whole LangChain stack in.
    from langchain.chat_models import init_chat_model

    spec = model_for_role(role)

    kwargs: dict[str, Any] = {
        "streaming": True,
        "timeout":   REQUEST_TIMEOUT_MS,
    }
    if max_tokens is not None:
        kwargs["max_tokens"] = max_tokens

    if spec.startswith("openrouter:"):
        kwargs["openrouter_provider"] = _PROVIDER_ROUTING
        if not os.getenv("OPENROUTER_APP_URL"):
            kwargs["app_url"] = _APP_URL
        if not os.getenv("OPENROUTER_APP_TITLE"):
            kwargs["app_title"] = _APP_TITLE

    return init_chat_model(spec, **kwargs)
