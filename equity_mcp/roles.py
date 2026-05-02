"""
Canonical tag sets for each agent role.

Every tag set includes "shared" so that tools tagged {"shared"} are
automatically visible to all agents.  The agent_factory filters the MCP
tool list by checking whether the agent's role tag OR "shared" appears in
each tool's tags — so a tool tagged SHARED is universally visible while a
tool tagged VALUE is only visible to the value researcher.
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
