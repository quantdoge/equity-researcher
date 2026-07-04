# equity-researcher

An AI-powered equity research team — 13 specialist agents backed by a shared FastMCP tool server — that collaborates to produce institutional-quality investment memos for any publicly traded company.

The orchestration layer is built on [deepagents](https://pypi.org/project/deepagents/) (LangChain / LangGraph): a **Head of Research** master agent autonomously plans its own task breakdown, delegates to 12 specialist subagents, and synthesises their outputs into a final Investment Memo.

## Agents

| # | Agent | Focus |
|---|-------|-------|
| 1 | Head of Research | Master orchestrator — plans, delegates, synthesises |
| 2 | Sector Economy Researcher | Industry dynamics, tailwinds/headwinds, peer benchmarking |
| 3 | Geopolitical & Legal Researcher | Country risk, sanctions, litigation, regulation |
| 4 | Macroeconomy Researcher | Rates, inflation, GDP, yield curve |
| 5 | Equity Value Researcher | Economic moat, DCF / owner earnings — Buffett style |
| 6 | Equity Growth Researcher | Revenue trajectory, TAM, catalysts — Cathie Wood style |
| 7 | Financial Risk Analyst | Credit/market/liquidity — Altman Z, Piotroski F |
| 8 | Non-Financial Risk Analyst | Governance, SEC enforcement, insider trading |
| 9 | Quantitative Analyst | Factor scores, alpha/beta, Sharpe/Sortino |
| 10 | Short / Contrarian Analyst | Beneish M-Score, accruals, bear case — Jim Chanos style |
| 11 | ESG / Sustainability Analyst | Material E/S/G factors, controversies, governance |
| 12 | Alternative Data Analyst | Google Trends, patents, job postings, sentiment |
| 13 | Portfolio Strategist | Position sizing, correlation, portfolio construction |

## Architecture

### Orchestration: deepagents (default)

```
orchestrator.py  (CLI entry)
       ↓
deep_agent_factory.run_research(symbol)
       ↓
create_deep_agent(
    model = claude-sonnet-4-6
    system_prompt = head_of_research.md
    subagents = [
        { name: sector_researcher,    tools: role-filtered LangChain tools },
        { name: value_researcher,     tools: role-filtered LangChain tools },
        { name: quant_analyst,        tools: role-filtered LangChain tools },
        ... 9 more specialists
    ]
)
       ↓  master agent autonomously plans which subagents to invoke
LangGraph runtime
  ├── delegate → sector_researcher  → calls FastMCP tools in-process
  ├── delegate → value_researcher   → calls FastMCP tools in-process
  ├── delegate → quant_analyst      → calls FastMCP tools in-process
  └── synthesise → final Investment Memo
```

The master agent uses deepagents' built-in `write_todos` planning tool to decompose the research task. Each subagent runs in an isolated context window and receives only the tools tagged for its role.

### FastMCP → LangChain Tool Bridge

A single **FastMCP server** (`server.py`) registers all ~70 tools, each tagged with the set of agent roles that may use it. The `langchain_bridge` module connects to the in-process FastMCP server, filters tools by role tag, and wraps each as a LangChain `StructuredTool` — so both the deepagents path and the legacy Anthropic SDK path enforce identical access control via the same tag system.

```
FastMCP Server (all ~70 tools, role-tagged)
        ↓  langchain_bridge.get_langchain_tools_for_role("value_researcher")
LangChain StructuredTool list (~15 tools)  →  passed to value_researcher subagent
```

### Legacy Pipeline (--legacy flag)

The original hard-coded 6-stage pipeline using the raw Anthropic SDK is preserved in `agent_factory.py`. Stages run sequentially; agents within each stage run in parallel:

```
Stage 1: Alt Data + Quant              (fast signals)
Stage 2: Sector + Geo/Legal + Macro    (context layer)
Stage 3: Value + Growth + Short + ESG  (company analysis)
Stage 4: Financial Risk + Non-Financial Risk  (risk overlay)
Stage 5: Portfolio Strategist          (synthesis)
Stage 6: Head of Research              (final memo)
```

## Data Sources

**Already ingested (Supabase/PostgreSQL via FMP pipeline):**
- Daily OHLCV prices
- Income statements, balance sheets, cash flow statements
- Analyst estimates and price targets
- Earnings calendar, dividends, splits

**External APIs called live by agents:**
- FRED (macro series — free)
- SEC EDGAR (10-K/10-Q filings, Form 4 insiders — free)
- NewsAPI (news sentiment — freemium)
- USPTO (patent filing trends — free)
- Google Trends via pytrends (free)
- Brave Search / DuckDuckGo fallback (web search)

## Setup

```bash
# 1. Clone and install
pip install -e .

# 2. Configure environment
cp .env.example .env
# Required: DATABASE_URL, ANTHROPIC_API_KEY
# Recommended: FRED_API_KEY, SEC_USER_AGENT
# Optional: NEWS_API_KEY, BRAVE_API_KEY
```

## Usage

```bash
# Full pipeline for one ticker (deepagents — default)
python -m equity_mcp.orchestrator --symbol AAPL

# Add optional research focus instructions
python -m equity_mcp.orchestrator --symbol MSFT --focus "focus on cloud growth and AI competition"

# Save JSON output to a directory
python -m equity_mcp.orchestrator --symbol TSLA --output-dir outputs/

# Use the legacy 6-stage Anthropic SDK pipeline
python -m equity_mcp.orchestrator --symbol AAPL --legacy

# Legacy mode — run only specific agents
python -m equity_mcp.orchestrator --symbol MSFT --legacy --agents value quant fin_risk

# Inspect all registered tools and their role tags
fastmcp inspect equity_mcp/server.py

# Run the MCP server standalone (for testing tools directly)
fastmcp run equity_mcp/server.py
```

## Project Structure

```
equity_mcp/
├── server.py              # FastMCP app — all ~70 tools registered with role tags
├── roles.py               # Canonical tag sets per agent role
├── langchain_bridge.py    # Bridges FastMCP tools → LangChain StructuredTool (by role)
├── deep_agent_factory.py  # Builds 12 subagents + master via create_deep_agent
├── agent_factory.py       # Legacy: Anthropic-SDK tool-use loop (--legacy fallback)
├── orchestrator.py        # CLI entry — deepagents default, --legacy flag available
├── tools/
│   ├── db.py              # Supabase query wrappers
│   ├── web.py             # Web search + page fetch
│   ├── calculations/      # Valuation, risk, quant, forensics (pure Python)
│   └── external/          # FRED, SEC EDGAR, News, Alt Data
└── prompts/               # System prompt .md file per agent role
```

## FMP → Supabase Data Pipeline

A production-ready continuous ingestion pipeline lives on the `dev` branch:

- **Script**: `scripts/fmp_pipeline.py`
- **Config**: `pipeline/endpoints.yaml`
- **Schema**: `supabase/migrations/20260425_000001_init_fmp_pipeline.sql`
- **CI/CD**: `.github/workflows/daily-fmp-pipeline.yml`

See the `dev` branch for full documentation.
