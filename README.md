# equity-researcher

An AI-powered equity research team — 13 specialist agents backed by a shared FastMCP tool server — that collaborates to produce institutional-quality investment memos for any publicly traded company.

## Agents

| # | Agent | Style / Analogy |
|---|-------|----------------|
| 1 | Head of Research | Master orchestrator |
| 2 | Sector Economy Researcher | Industry dynamics |
| 3 | Geopolitical & Legal Researcher | Country risk, litigation |
| 4 | Macroeconomy Researcher | Monetary/fiscal policy |
| 5 | Equity Value Researcher | Warren Buffett |
| 6 | Equity Growth Researcher | Cathie Wood |
| 7 | Financial Risk Analyst | Credit/market/liquidity risk |
| 8 | Non-Financial Risk Analyst | Governance/fraud/regulatory |
| 9 | Quantitative Analyst | AQR / D.E. Shaw factor models |
| 10 | Short / Contrarian Analyst | Jim Chanos / Hindenburg Research |
| 11 | ESG / Sustainability Analyst | Climate, governance, social |
| 12 | Alternative Data Analyst | Google Trends, patents, sentiment |
| 13 | Portfolio Strategist | Position sizing, portfolio construction |

## Architecture

A single **FastMCP server** registers all ~70 tools. Each tool is tagged with the agent roles that may use it. The **agent factory** filters the tool list per role before each Claude API call — agents literally cannot see tools they shouldn't use.

```
FastMCP Server (all tools)
        ↓
filter_tools_for_role("value_researcher")   ← ~15 tools
        ↓
Claude API call with filtered tool list
```

## Pipeline

Stages run sequentially; agents within each stage run in parallel:

```
Stage 1: Alt Data + Quant          (fast signals — run first)
Stage 2: Sector + Geo + Macro      (context layer)
Stage 3: Value + Growth + Short + ESG  (company analysis)
Stage 4: Financial Risk + Non-Financial Risk  (risk overlay)
Stage 5: Portfolio Strategist      (synthesis)
Stage 6: Head of Research          (final investment memo)
```

## Data Sources

**Already ingested (Supabase/PostgreSQL via FMP pipeline):**
- Daily OHLCV prices
- Income statements, balance sheets, cash flow statements
- Analyst estimates and price targets
- Earnings calendar, dividends, splits

**External APIs used by agents:**
- FRED (macro data — free)
- SEC EDGAR (10-K/10-Q text, Form 4 insiders — free)
- NewsAPI (news sentiment — freemium)
- USPTO (patent filings — free)
- Google Trends via pytrends (free)
- Brave Search (web search — freemium)

## Setup

```bash
# 1. Clone and install
pip install -e .

# 2. Configure environment
cp .env.example .env
# Fill in DATABASE_URL, ANTHROPIC_API_KEY, and optional API keys

# 3. Apply Supabase migration (if not already done)
# See supabase/migrations/ on the dev branch
```

## Usage

```bash
# Full 13-agent pipeline for one ticker
python -m equity_mcp.orchestrator --symbol AAPL

# Run a subset of agents
python -m equity_mcp.orchestrator --symbol MSFT --agents value quant fin_risk

# Inspect all registered tools and their agent tags
fastmcp inspect equity_mcp/server.py

# Run the MCP server standalone (test tools directly)
fastmcp run equity_mcp/server.py
```

## FMP → Supabase Data Pipeline

A production-ready continuous ingestion pipeline lives on the `dev` branch:

- **Script**: `scripts/fmp_pipeline.py`
- **Config**: `pipeline/endpoints.yaml`
- **Schema**: `supabase/migrations/20260425_000001_init_fmp_pipeline.sql`
- **CI/CD**: `.github/workflows/daily-fmp-pipeline.yml`

See the `dev` branch for full documentation.

## Project Structure

```
equity_mcp/
├── server.py          # FastMCP app — all tools registered with role tags
├── roles.py           # Tag sets per agent role
├── agent_factory.py   # Tool filtering + Claude API tool-use loop
├── orchestrator.py    # 6-stage pipeline runner
├── tools/
│   ├── db.py          # Supabase query wrappers
│   ├── web.py         # Web search + page fetch
│   ├── calculations/  # Valuation, risk, quant, forensics
│   └── external/      # FRED, SEC EDGAR, News, Alt Data
└── prompts/           # System prompt per agent role
```
