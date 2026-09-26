# equity-researcher — CLAUDE.md

## Project Overview

A multi-agent equity research system built on a shared FastMCP server.
13 AI agents (each on an OpenRouter model) collaborate to produce institutional-quality
investment memos. All agents share one MCP tool server; tool access is
enforced per-agent via FastMCP tags.

## Development Branch

Always develop on `claude/multi-agent-equity-research-DOiTR`.

## Architecture

```
equity_mcp/
├── server.py              # FastMCP app — all 61 tools registered here with role tags
├── roles.py               # Canonical tag sets + per-agent OpenRouter model config
├── langchain_bridge.py    # Bridges FastMCP tools → LangChain StructuredTool (by role)
├── deep_agent_factory.py  # Parallel specialist fan-out + create_deep_agent master
├── agent_factory.py       # Legacy: Anthropic-SDK tool-use loop (--legacy fallback)
├── orchestrator.py        # CLI entry — deepagents default, --legacy flag for fallback
├── tools/
│   ├── db.py              # Market + fundamental data, sourced from FMP
│   ├── web.py             # web_search + fetch_page
│   ├── calculations/      # valuation, risk, quant, forensics (these query the DB)
│   └── external/          # fred, sec_edgar, news, alt_data (external APIs)
└── prompts/               # System prompt .md file per agent role
```

## Orchestration: deepagents (default)

Three steps on the critical path. The 11 research specialists run concurrently
as independent LangGraph react agents, each holding only the FastMCP tools
tagged for its role via `langchain_bridge.get_langchain_tools_for_role`. The
portfolio strategist then reads their reports, and the Head of Research — a
`create_deep_agent` master with **no subagents** — writes the memo.

```
1. asyncio.gather, semaphore-capped (default 6 at a time):
     sector_researcher  |  geo_legal_researcher  |  macro_researcher
     value_researcher   |  growth_researcher     |  fin_risk_analyst
     nonfin_risk_analyst|  quant_analyst         |  short_analyst
     esg_analyst        |  alt_data_analyst
2. portfolio_strategist   (reads all 11 reports)
3. head_of_research       (create_deep_agent — synthesis only)
```

The master previously held all 12 as deepagents `subagents` and was asked in
prose to cover every dimension. Claude issues those delegation calls one at a
time, making a run ~14 sequential agent executions. Fanning out here instead is
safe because the specialists never read each other's output. Per-agent timings
land in the output JSON under `per_agent_timings`; a failed specialist is
recorded in `failures` and does not abort the run.

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
# Fill in OPENROUTER_API_KEY and FMP_API_KEY — those two are what a run needs
pip install -e .
```

## Running

```bash
# Full pipeline for a single ticker
uv run python -m equity_mcp.orchestrator --symbol AAPL

# Tune the fan-out (lower if you hit OpenRouter rate limits) and bound the run
uv run python -m equity_mcp.orchestrator --symbol AAPL --max-concurrency 4 --timeout 1800

# Verify role-based tool access after touching roles.py / server.py tags
uv run python tests/test_tool_access.py

# Run a subset of agents — unambiguous prefixes are accepted
uv run python -m equity_mcp.orchestrator --symbol MSFT --agents value quant fin_risk

# Inspect all registered MCP tools and their tags
uv run fastmcp inspect equity_mcp/server.py

# Run MCP server standalone (for testing tools directly)
uv run fastmcp run equity_mcp/server.py
```

## No Database Required

**`db.py` no longer touches Postgres.** All 12 of its tools source their data
from FMP via `tools/external/fmp.py`, so every role works with only
`FMP_API_KEY` set and `DATABASE_URL` is currently unused. The Supabase schema it
used to query (`ref.symbol`, `core.income_statement`, …) was never provisioned,
which had left `value_researcher`, `quant_analyst`, `short_analyst`,
`fin_risk_analyst` and `portfolio_strategist` with nothing to analyse.

An FMP outage still degrades rather than dying: `langchain_bridge`
`._make_async_caller` converts every tool exception to text, so a failed fetch
reaches the agent as `Tool '...' failed:` and the run continues.

```bash
# Cheapest smoke test: two specialists, no synthesis — 2 agent runs, not 13
uv run python -m equity_mcp.orchestrator --symbol AAPL \
  --agents macro esg --skip-synthesis --max-concurrency 2 --timeout 600

# The five roles that were previously blocked on the database
uv run python -m equity_mcp.orchestrator --symbol AAPL \
  --agents value quant short fin_risk --max-concurrency 4 --timeout 1800
```

`--skip-synthesis` stops after the specialist fan-out and prints their reports
instead of a memo. Both flags are for testing; a real run wants the memo.

## Run Logs

Every deepagents run writes a directory as it goes (`--runs-dir`, default
`runs/`, gitignored):

```
runs/<SYMBOL>_<YYYYmmddTHHMMSS>/
    run.log          # START, one DONE/FAIL per agent, END or ABORT
    reports/         # <role>.md, written the moment that agent finishes
    result.json      # the full result dict, at the end
```

`equity_mcp/run_log.py` owns this. Reports are written from the
`on_agent_complete` callback `run_research()` already accepts, so **a run that
times out or is interrupted still leaves every finished agent's work on disk** —
previously a failure at the memo discarded eleven completed specialist reports.
`tail -f runs/<id>/run.log` to watch a run in progress.

Two related properties worth not regressing:

- Progress prints pass `flush=True`. Without it stdout is block-buffered the
  moment it is piped or redirected, and a half-hour run shows nothing at all
  until it exits — which also means a broken pipe discards the entire run.
- `outputs/` filenames carry the run's timestamp, not just a date, so two runs
  of one ticker on the same day no longer overwrite each other. The stamp is
  shared with the run directory, so a JSON and its run can be matched up.

`RunLog` never raises: an unwritable path degrades to a single stderr warning.
Logging exists to make failures survivable and must not become one.

## Key Design Decisions

**Single shared MCP server** — all tools live in `server.py`. Add a tool once,
tag it with the appropriate role sets from `roles.py`, and it's immediately
available to the right agents. No duplication across agent files.

**Enforcement by omission** — `agent_factory.py` filters the full tool list to
only those tagged with the agent's role before passing to Claude API. Claude
literally cannot see or call tools it isn't given.

**Tool tags = role sets** — tags are Python `set[str]` defined in `roles.py`.
Each per-role constant holds exactly one tag: that role's own name. `SHARED` is
separate. So `VALUE` reaches only the value researcher, `SHARED` reaches
everyone, and `VALUE | SHARED` reaches everyone.

Never bundle `"shared"` into a per-role constant. Doing so tags every tool as
shared, which hands all 13 agents the entire 61-tool surface — defeating the
access model and putting every tool schema in every agent's context on every
turn. `tests/test_tool_access.py` asserts the per-role counts to catch this.

## Model Selection

Every deepagents agent runs on OpenRouter, keyed by `OPENROUTER_API_KEY`.
`roles.py` owns the choice:

- `DEFAULT_MODEL` — the slug every role uses unless overridden
  (currently `deepseek/deepseek-v4-flash-0731`).
- `AGENT_MODELS` — `role -> OpenRouter slug` overrides; empty by default.
- `model_for_role(role)` — resolves the two into a LangChain spec, adding the
  `openrouter:` provider prefix. A value that already carries a `<provider>:`
  prefix passes through, so a role can be pinned to another provider.
- `chat_model_for_role(role, max_tokens)` — builds the `ChatOpenRouter`
  instance `deep_agent_factory` uses, with `streaming=True` and an explicit
  `timeout` (see the comments there for why both defaults are unusable on a
  half-hour run), plus OpenRouter app attribution and provider routing.

To repoint one specialist, add a line to `AGENT_MODELS` — nothing else changes.
The legacy `--legacy` pipeline still calls the Anthropic SDK directly and is
unaffected by any of this.

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
| Supabase/PostgreSQL | `DATABASE_URL` | No | **Currently unused** — `db.py` reads from FMP instead |
| OpenRouter | `OPENROUTER_API_KEY` | Yes | Powers all deepagents agents; per-role model in `roles.py` |
| Anthropic | `ANTHROPIC_API_KEY` | Legacy only | Used by the `--legacy` pipeline in `agent_factory.py` |
| FRED | `FRED_API_KEY` | Recommended | Free at fred.stlouisfed.org |
| SEC EDGAR | `SEC_USER_AGENT` | Recommended | No key; just set a user-agent |
| FMP | `FMP_API_KEY` | Yes | **All 12 `db.py` tools**, plus every tool in `tools/external/news.py` |
| Brave Search | `BRAVE_API_KEY` | One of these two | Preferred `web_search` provider |
| SerpAPI | `SERP_API_KEY` | One of these two | Used when Brave is unset |

### FMP caching — use `fmp_cached`, not `fmp_get`

`tools/external/fmp.py` exposes two entry points. **New tools should call
`fmp_cached`**; `fmp_get` is the uncached path, appropriate only for calls whose
parameters already carry a timestamp (the news feeds).

The cache is a process-wide TTL dict (15 min, 512 entries, FIFO eviction) keyed
on path + params, and it is what makes the fan-out affordable. The 13 agents run
concurrently with overlapping tool sets — seven of them can request the same
symbol's income statement in one run — and two calculation tools iterate over
peers or a universe. Measured cold: `compare_peer_valuations` is 47 requests /
17s, and a repeat is 0 requests / 0.0s. Empty results are cached too (a symbol
FMP has no data for would otherwise be re-fetched by every agent); exceptions
never are.

Two caps exist for the same reason and are tuned against
`langchain_bridge._TOOL_TIMEOUT_S` (90s), not chosen for taste — raising either
is the first thing that will push a tool into a timeout, which returns *nothing*:

- `compare_peer_valuations` — 8 peers, at 5 requests each.
- `rank_universe_by_factor` — 25 symbols, at 1–3 requests each (~30s cold).

Retries cover transient faults only: connection errors and `{429, 500, 502, 503,
504}` get up to 3 attempts, a read timeout gets 2 (it has already spent 45s).
**HTTP 402 is never retried** — it is a plan ceiling, permanent for the life of
the subscription.

### News

News comes from FMP, the only news source the project pays for. On the plans in
use it is **symbol-scoped with no keyword search**, so `fetch_esg_controversy_news`
and friends pull a symbol's recent coverage and filter it client-side, topping up
from `web_search` when too little is on-topic. Topped-up articles carry
`source: "web search"` so an agent can weigh a search snippet differently from a
published article.

`fmp_get` raises `FMPPlanDenied` on HTTP 402 — a plan ceiling, permanent for the
life of the subscription. Never retry one or debug it as an auth fault; the news
helpers catch it and fall back. `news/press-releases` is above the Starter plan;
`news/stock`, `news/general-latest` and `news/stock-latest` are not.

FMP's news feeds are slow and highly variable (a 250-row request measured 5s
once and 32s the next), hence the 45s timeout in `tools/external/fmp.py`. A tight
timeout there is worse than useless: it is indistinguishable from an empty
result, so it silently drops real data.

## Data Proxies — removed

The calculation tools used to substitute fixed fractions of `total_assets` for
line items the old schema never stored. FMP reports all of them, so the proxies
are gone and `db.py` returns the real fields alongside the original keys:

| Was | Now |
|-----|-----|
| A/R → 8% of total assets | `net_receivables` |
| PPE → 30% of total assets | `ppe_net` |
| D&A → operating CF – net income | `depreciation_and_amortization` |
| Inventory → 15% of COGS | `inventory` |
| EBITDA → operating income | `ebitda` |
| Shares → net income / diluted EPS | `weighted_average_shares_diluted` |
| Retained earnings → total equity | `retained_earnings` |
| Current ratio → total assets / total liabilities | `total_current_assets` / `total_current_liabilities` |
| SG&A → revenue – gross profit – operating income | `sga` |

Do not reintroduce a proportional-to-assets proxy. Two of them were not merely
imprecise but **degenerate**: because A/R and PPE were both fixed fractions of
the same denominator, the Beneish `aqi` and `depi` indices evaluated to exactly
1.0 for every company, and `inventory_days` was the constant 54.8 — so
`trend_signal` could never fire. A proxy that varies with nothing measures
nothing.

Book value per share was also literally `total_equity / 1`.

What is still approximate, and honestly labelled: `market_cap_approx` uses
weighted-average diluted shares rather than current shares outstanding, and the
Altman `x4` uses book equity rather than market capitalisation.
