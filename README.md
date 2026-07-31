# equity-researcher

An AI-powered equity research team — 14 specialist agents backed by a shared FastMCP tool server — that collaborates to produce institutional-quality investment memos for any publicly traded company.

The orchestration layer is built on [deepagents](https://pypi.org/project/deepagents/) (LangChain / LangGraph): a **Head of Research** master agent autonomously plans its own task breakdown, delegates to 13 specialist subagents, and synthesises their outputs into a final Investment Memo.

## Agents

| # | Agent | Focus |
|---|-------|-------|
| 1 | Head of Research | Master orchestrator — plans, delegates, synthesises |
| 2 | Quantitative Engineer | The only agent that executes code; computes everything FMP doesn't return |
| 3 | Sector Economy Researcher | Industry dynamics, tailwinds/headwinds, peer benchmarking |
| 4 | Geopolitical & Legal Researcher | Country risk, sanctions, litigation, regulation |
| 5 | Macroeconomy Researcher | Rates, inflation, GDP, yield curve |
| 6 | Equity Value Researcher | Economic moat, DCF / owner earnings — Buffett style |
| 7 | Equity Growth Researcher | Revenue trajectory, TAM, catalysts — Cathie Wood style |
| 8 | Financial Risk Analyst | Credit/market/liquidity — Altman Z, Piotroski F |
| 9 | Non-Financial Risk Analyst | Governance, SEC enforcement, insider trading |
| 10 | Quantitative Analyst | Factor scores, alpha/beta, Sharpe/Sortino |
| 11 | Short / Contrarian Analyst | Beneish M-Score, accruals, bear case — Jim Chanos style |
| 12 | ESG / Sustainability Analyst | Material E/S/G factors, controversies, governance |
| 13 | Alternative Data Analyst | Insider and congressional trading, sentiment, earnings surprises |
| 14 | Portfolio Strategist | Position sizing, correlation, portfolio construction |

## How it works

```
orchestrator.py  (CLI entry, opens runs/<SYMBOL>_<ts>/)
       ↓
deep_agent_factory.run_research(symbol)
       ↓
create_deep_agent(
    model         = roles.model_for_role("head_of_research"),
    system_prompt = prompts/head_of_research.md + prompts/_toolkit.md,
    subagents     = [ 13 specialists, each with a per-role model
                      and role-filtered tools from the MCP server ]
)
```

The master plans with deepagents' built-in `write_todos`, delegates via `task`,
and writes the memo. Subagents cannot call each other, so when an analyst needs a
figure computed the master routes that request to the Quantitative Engineer.

### Three tools, not forty

There is no tool per metric. Agents work in three steps:

1. **`fmp_catalog()`** — discover what Financial Modeling Prep offers (28 category
   tools, ~250 endpoints). `fmp_catalog("statements")` drills into one.
2. **`fmp_call(tool, endpoint, params)`** — fetch. Data comes back in FMP's own
   field names, with a `fields` list so nothing has to assume a schema. Responses
   over 8 KB are written to `runs/<SYMBOL>_<ts>/data/` and only previewed inline.
3. **`run_python(code)`** — compute, when FMP has no endpoint for it. Restricted to
   the Quantitative Engineer.

Much of what looks like it needs computing does not: `statements/financial-scores`
returns real Altman Z and Piotroski scores, and `key-metrics`, `metrics-ratios`,
`owner-earnings`, `financial-statement-growth`, `discountedCashFlow/*` and
`technicalIndicators/*` cover most standard ratios.

### Audit trail

Every run leaves `runs/<SYMBOL>_<TIMESTAMP>/` containing `data/` — the raw FMP
payloads the agents fetched — and `scripts/` — the Python they ran over them. Any
computed figure in the memo can be traced back to both.

## Setup

Dependencies are managed with [uv](https://docs.astral.sh/uv/); `uv.lock` is
committed.

```bash
uv sync
cp .env.example .env
# Fill in FMP_API_KEY and OPENROUTER_API_KEY — both required
```

| Key | Required | Purpose |
|-----|----------|---------|
| `FMP_API_KEY` | Yes | The only financial data source |
| `OPENROUTER_API_KEY` | Yes | Powers every agent |
| `BRAVE_API_KEY` | Optional | Backs `web_search`; the DuckDuckGo fallback is unreliable |

Endpoint availability follows your FMP plan. A gated endpoint returns
`{"kind": "plan_denied"}` rather than failing the run — on Starter that means no
ESG ratings, earnings transcripts, 13F data, or sector P/E snapshots.

## Running

```bash
# Full pipeline for a single ticker
uv run python -m equity_mcp.orchestrator --symbol AAPL

# Steer the master agent
uv run python -m equity_mcp.orchestrator --symbol MSFT --focus "weight ESG and growth"

# Inspect the registered MCP tools and their role tags
uv run fastmcp inspect equity_mcp/server.py

# Run the MCP server standalone, to exercise tools directly
uv run fastmcp run equity_mcp/server.py
```

The memo is printed to stdout and saved to `outputs/<SYMBOL>_<date>.json`.

## Layout

```
equity_mcp/
├── server.py              # FastMCP app — 6 tools registered with role tags
├── roles.py               # Tag sets + per-role model assignment
├── workspace.py           # Per-run scratch dir
├── langchain_bridge.py    # FastMCP tools → LangChain StructuredTool, by role
├── deep_agent_factory.py  # Builds 13 subagents + master
├── orchestrator.py        # CLI entry point
├── tools/
│   ├── fmp.py             # fmp_catalog + fmp_call
│   ├── code_exec.py       # run_python + list_workspace
│   └── web.py             # web_search + fetch_page
└── prompts/               # One .md per role, plus the shared _toolkit.md
```

See `CLAUDE.md` for design rationale and the details worth knowing before
changing any of it.
