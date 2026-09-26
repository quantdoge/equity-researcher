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
