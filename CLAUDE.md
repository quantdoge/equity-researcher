# equity-researcher — CLAUDE.md

## Project Overview

A multi-agent equity research system built on a shared FastMCP server.
13 AI agents (powered by Claude) collaborate to produce institutional-quality
investment memos. All agents share one MCP tool server; tool access is
enforced per-agent via FastMCP tags.

## Development Branch

Always develop on `claude/multi-agent-equity-research-DOiTR`.

## Architecture

```
equity_mcp/
├── server.py              # FastMCP app — all ~70 tools registered here with role tags
├── roles.py               # Canonical tag sets per agent role
├── langchain_bridge.py    # Bridges FastMCP tools → LangChain StructuredTool (by role)
├── deep_agent_factory.py  # Builds 12 subagents + master via create_deep_agent
├── agent_factory.py       # Legacy: Anthropic-SDK tool-use loop (--legacy fallback)
├── orchestrator.py        # CLI entry — deepagents default, --legacy flag for fallback
├── tools/
│   ├── db.py              # Supabase query wrappers (falls back to fmp_mcp)
│   ├── fmp_mcp.py         # FMP MCP client — fallback source for every db tool
│   ├── web.py             # web_search + fetch_page
│   ├── calculations/      # valuation, risk, quant, forensics (pure Python)
│   └── external/          # fred, sec_edgar, news, alt_data (external APIs)
└── prompts/               # System prompt .md file per agent role
```

## Orchestration: deepagents (default)

The Head of Research is a `create_deep_agent` master agent with 12 specialist
subagents. It autonomously plans its research task breakdown via deepagents'
built-in `write_todos` planning tool, then delegates to each specialist.
Each subagent receives only the FastMCP tools tagged for its role via
`langchain_bridge.get_langchain_tools_for_role`.

```
Master: Head of Research  (create_deep_agent)
  └── subagents (12 specialists, each with role-filtered tools):
        sector_researcher  |  geo_legal_researcher  |  macro_researcher
        value_researcher   |  growth_researcher     |  fin_risk_analyst
        nonfin_risk_analyst|  quant_analyst          |  short_analyst
        esg_analyst        |  alt_data_analyst       |  portfolio_strategist
```

## Legacy Pipeline (--legacy flag)

The original 6-stage sequential+parallel pipeline using the raw Anthropic SDK
is preserved in `agent_factory.py`:

```bash
python -m equity_mcp.orchestrator --symbol AAPL --legacy
```

## Agent Pipeline Order (legacy)

Stages run sequentially; agents within each stage run in parallel:
1. Alt Data + Quant (fast signals)
2. Sector + Geo/Legal + Macro (context layer)
3. Value + Growth + Short + ESG (company analysis)
4. Financial Risk + Non-Financial Risk (risk overlay)
5. Portfolio Strategist (synthesis)
6. Head of Research (final investment memo)

## Environment Setup

```bash
cp .env.example .env
# Fill in DATABASE_URL, ANTHROPIC_API_KEY, and any optional API keys
pip install -e .
```

## Running

```bash
# Full pipeline for a single ticker
python -m equity_mcp.orchestrator --symbol AAPL

# Run a subset of agents
python -m equity_mcp.orchestrator --symbol MSFT --agents value quant fin_risk

# Inspect all registered MCP tools and their tags
fastmcp inspect equity_mcp/server.py

# Run MCP server standalone (for testing tools directly)
fastmcp run equity_mcp/server.py
```

## Key Design Decisions

**Single shared MCP server** — all tools live in `server.py`. Add a tool once,
tag it with the appropriate role sets from `roles.py`, and it's immediately
available to the right agents. No duplication across agent files.

**Enforcement by omission** — `agent_factory.py` filters the full tool list to
only those tagged with the agent's role before passing to Claude API. Claude
literally cannot see or call tools it isn't given.

**Tool tags = role sets** — tags are Python `set[str]` defined in `roles.py`.
A tool tagged `VALUE | SHARED` is visible to the value researcher AND all
agents (since every agent's tag includes `"shared"`).

**Database-first, FMP-second** — every `get_*` tool in `db.py` queries Supabase,
then falls through to the same-named function in `fmp_mcp.py` if the query
raises *or* returns zero rows (an un-backfilled symbol is treated as a cache
miss, not as "no data"). The fallback calls FMP's official remote MCP server at
`https://financialmodelingprep.com/mcp?apikey=$FMP_API_KEY` and re-shapes the
camelCase response into the exact snake_case row shape the SQL returns, so
callers can't tell which path served them. If both sources fail the tool logs
and returns `[]` / `None` — a dead database degrades an agent, never crashes it.

Wiring is one decorator; the FMP function must mirror the SQL signature and shape:

```python
@_fmp_fallback(fmp_mcp.get_income_statement)
def get_income_statement(symbol, period_type="annual", n_periods=8): ...
```

Two fallbacks are deliberately lossy, since the MCP server has no equivalent:
`get_price_targets` uses `analyst/grades`, so `target_price` is always null;
`get_sector_financials` aggregates the top 25 sector constituents by market cap
and buckets by fiscal year rather than exact `period_end`.

## Adding a New Tool

1. Implement the function in the appropriate `tools/` module
2. Import it in `server.py`
3. Register with `mcp.tool(tags=<ROLE_SET>)(<function>)`
4. That's it — the agent factory picks it up automatically

## Adding a New Agent

1. Add role constants to `roles.py`
2. Add a system prompt to `prompts/<new_role>.md`
3. Add the role to `ALL_ROLES` in `roles.py`
4. Add it to the appropriate pipeline stage in `orchestrator.py`
5. Tag any new tools with the new role set

## External APIs

| API | Key Variable | Required | Notes |
|-----|-------------|----------|-------|
| Supabase/PostgreSQL | `DATABASE_URL` | Yes | Existing pipeline |
| Anthropic | `ANTHROPIC_API_KEY` | Yes | Powers all agents |
| FRED | `FRED_API_KEY` | Recommended | Free at fred.stlouisfed.org |
| SEC EDGAR | `SEC_USER_AGENT` | Recommended | No key; just set a user-agent |
| NewsAPI | `NEWS_API_KEY` | Optional | Falls back to web search |
| Brave Search | `BRAVE_API_KEY` | Optional | Falls back to DuckDuckGo |
| FMP | `FMP_API_KEY` | Recommended | Data pipeline **and** the live fallback for every `db.py` tool |

## Data Proxies

Several calculation tools use proxies because the current schema doesn't store
every financial line item separately (e.g., accounts receivable, D&A, PPE):

- A/R → 8% of total assets
- PPE → 30% of total assets
- D&A → operating CF – net income

Replace these proxies by extending the Supabase schema and FMP ingestion
pipeline to store granular line items as the project matures.
