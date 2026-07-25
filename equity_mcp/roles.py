"""
Canonical tag sets and model assignments for each agent role.

Every tag set includes "shared" so that tools tagged {"shared"} are
automatically visible to all agents.  The agent_factory filters the MCP
tool list by checking whether the agent's role tag OR "shared" appears in
each tool's tags — so a tool tagged SHARED is universally visible while a
tool tagged VALUE is only visible to the value researcher.

This module is also the single source of truth for which model each agent
runs on — see DEFAULT_MODEL, AGENT_MODELS and model_for_role at the bottom.
"""

SHARED: set[str] = {"shared"}

HEAD_OF_RESEARCH: set[str]    = {"head_of_research",    "shared"}
SECTOR:           set[str]    = {"sector_researcher",    "shared"}
GEO_LEGAL:        set[str]    = {"geo_legal_researcher", "shared"}
MACRO:            set[str]    = {"macro_researcher",     "shared"}
VALUE:            set[str]    = {"value_researcher",     "shared"}
GROWTH:           set[str]    = {"growth_researcher",    "shared"}
FIN_RISK:         set[str]    = {"fin_risk_analyst",     "shared"}
NONFIN_RISK:      set[str]    = {"nonfin_risk_analyst",  "shared"}
QUANT:            set[str]    = {"quant_analyst",        "shared"}
SHORT:            set[str]    = {"short_analyst",        "shared"}
ESG:              set[str]    = {"esg_analyst",          "shared"}
ALT_DATA:         set[str]    = {"alt_data_analyst",     "shared"}
PORTFOLIO:        set[str]    = {"portfolio_strategist", "shared"}

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
# Every agent runs on OpenRouter.  DEFAULT_MODEL applies to any role with no
# entry in AGENT_MODELS.  Values are bare OpenRouter slugs; model_for_role()
# adds the "openrouter:" provider prefix that LangChain's init_chat_model wants.

DEFAULT_MODEL: str = "anthropic/claude-sonnet-5"

# Per-agent overrides.  role string -> OpenRouter slug.  Empty by default —
# uncomment or add entries to point individual specialists at cheaper or
# stronger models without touching any other file.
AGENT_MODELS: dict[str, str] = {
    # ROLE_QUANT:    "openai/gpt-5.1",
    # ROLE_ALT_DATA: "google/gemini-2.5-flash",
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
