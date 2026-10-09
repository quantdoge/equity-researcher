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
├── prompts/               # System prompt .md file per agent role
├── metrics/               # Jev evaluation rubric .yaml per agent role + _shared.yaml
└── evaluation/            # Scores outputs/*.json with TypeSafe Jev → Supabase `eval` schema
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
6. Add `metrics/<new_role>.yaml` (see Output Evaluation); `tests/test_eval_rubrics.py` fails until it exists

## Output Evaluation (TypeSafe Jev)

Every agent's report is scored by TypeSafe **Jev**. Jev is a typed "System One"
classifier: it answers Noul (yes/no probability), Score (ordinal level) and
Choice (one of N) questions about a supplied text. The rubric for each agent
lives in `equity_mcp/metrics/<role>.yaml`, one file per role, plus
`_shared.yaml`. The code lives in `equity_mcp/evaluation/`. Results go to a
**separate** Supabase project, schema `eval`
(`supabase/migrations/20261010000000_eval_schema.sql`).

Each evaluation has two blocks that are stored apart and **never averaged together**:

- **conviction**: what the agent concluded.
  - Every agent is placed on the same shared Choice, STRONG SELL / SELL /
    HOLD / BUY / STRONG BUY, with a Low/Medium/High conviction level.
  - The agent's own headline enum is extracted in code and mapped to that
    scale through the YAML's `native_to_stance`. Their agreement is stored.
  - Each role also has 5-level **domain metrics**: profitability, liquidity
    and solvency for value; E, S and G for ESG; and so on.
- **alignment**: whether the output followed its prompt.
  - Deterministic checks in code: sections, enums, tables, counts and
    price-target arithmetic.
  - Jev questions on evidence, balance and consistency.
  - These combine into a weighted composite. Vetoes are listed separately.

```bash
uv run python -m equity_mcp.evaluation.evaluate --validate-rubrics          # offline, also in CI
uv run python -m equity_mcp.evaluation.inspect value_researcher -v          # offline rubric debugger
uv run python -m equity_mcp.evaluation.evaluate --all --dry-run             # request counts, no network
uv run python -m equity_mcp.evaluation.evaluate --file outputs/AVGO_20261003T135110.json
uv run python -m equity_mcp.orchestrator --symbol AAPL --evaluate           # score at the end of a run
uv run python tests/test_eval_rubrics.py && uv run python tests/test_eval_extract.py && uv run python tests/test_eval_jev.py
```

Rules that came from Jev's documented behaviour, not taste:

- **Code does what Jev can't.** Jev reads dates as text, counts badly and
  degrades on long state, so code extracts enums, counts items and checks
  arithmetic. Jev sees only the sections a question needs, capped at 12k chars.
- **Score has no abstain option.** A request's `gate` Noul marks its siblings
  `low_evidence` when it fails. A domain metric is sent only if code finds one
  of its `evidence_terms`; otherwise it is `not_addressed`.
- **Question ids are not sent to the model.** Every `instructions` must stand
  on its own. Score levels are 0-based on the wire.
- **Pin the model** (`JEV_MODEL=jev-1.13.0`). The CLI refuses `jev-latest`
  unless `--allow-floating-model` is passed.
- **The portfolio strategist and head of research are evaluated second.**
  Their fidelity questions get a code-built `specialist_summary` of what the
  specialists concluded and which ones failed.
- **Editing a prompt requires a rubric review.** Each YAML pins
  `source_prompt_sha256`, and `--validate-rubrics` fails on drift. After
  review, update the hash (`--rehash-prompts` prints them). Editing a rubric
  changes its `rubric_sha`, which makes past runs eligible for re-evaluation.
- **Results are advisory until calibrated.** `calibrated: false` sets
  `advisory=true` on every evaluation. Calibration means hand labels in
  `eval.human_labels` and checking agreement in `eval.v_jev_human_agreement`.
- **Evaluation never fails research.**
  - `orchestrator --evaluate` and the CI step swallow every error into one
    `EVAL` line in run.log.
  - An unreachable database parks records in `evals/pending/` (gitignored).
    Replay them with `--flush-pending`.
  - A failed or degenerate agent gets a status and costs no calls, rather than
    a score of zero.

Idempotency: an evaluation is keyed on (run, role, rubric_sha, jev_model). A
rerun skips work that is already stored unless `--force` is passed. Every
successful call is cached in `eval.jev_calls` by state + questions + model, so
`--force` after a one-question rubric edit only pays for the changed request.

**Data dictionary.** Every table, view and column in `eval` is documented in the
`datadict` schema, which has two tables: `datadict.tables` and `datadict.columns`.
For each column it records: type, owner, dates, definition, real example values,
value range, and what each value means. Read it through `datadict.v_data_dictionary`.
In that view, a pass-through view column inherits its source column's text through
`derived_from`.

It is built by `supabase/migrations/20261010020000_datadict_schema.sql` and
`…020100_datadict_eval_seed.sql`. The seed is idempotent, and it copies types
from `pg_catalog`, so types are never written by hand.

**Any migration that changes `eval` must update the seed in the same change.** When
it's done, `SELECT * FROM datadict.v_coverage_gaps` must return 0 rows. That view
lists undocumented columns, dropped columns, type changes and broken `derived_from`
links.

### Rollout status and next session: backfill (written 2026-10-10)

Delete this subsection once the backfill is stored and the paused items are settled.

**State at end of 2026-10-10.** Nothing here is committed yet.
- Supabase project `equity-research-eval` (ref `zpnjlzrgzrtedkqumrph`) has the `eval` and `datadict` schemas applied.
- 3 of the 35 `outputs/*.json` runs are evaluated and stored: `AVGO_20261003T135110`, `IBM_20261006T150931` and `NOW_20261006T153021`. That is 39 evaluations, about 1,380 metric results and 224 cached Jev calls.
- `.env` holds `TYPESAFE_API_KEY` and `SUPABASE_EVAL_DB_URL`, the latter for the `eval_writer` role through the session pooler.

**Backfill the other 32 runs.** This is about 2,140 Jev requests. Idempotency skips the three runs already stored, so `--all` is safe to use.

```bash
# 1. Offline checks. Both must pass before spending anything.
uv run python -m equity_mcp.evaluation.evaluate --validate-rubrics
uv run python -m equity_mcp.evaluation.evaluate --all --dry-run        # request count per run; ignores the store, so includes the 3 done runs

# 2. Smoke test one run end to end, then check it landed.
uv run python -m equity_mcp.evaluation.evaluate --symbol MSFT --latest

# 3. The rest. Run it in the background and log it; rerunning resumes where it stopped.
mkdir -p evals && uv run python -m equity_mcp.evaluation.evaluate --all --concurrency 4 2>&1 | tee evals/backfill.log

# 4. If the database dropped at any point, replay what was parked.
uv run python -m equity_mcp.evaluation.evaluate --flush-pending
```

Things to watch for during the backfill:
- **The oldest files may have a pre-provenance layout.** These are `CMG_2026-07-31_gpt4omini.json`, `CMG_2026-08-01.json` and the August runs. They may be skipped or show more `agent_failed` and `degenerate` statuses. The dry run in step 1 shows which.
- **A 401 or 403 from Jev stops the run** (`FatalJevError`). Check the key rather than retrying.
- **Keep `--concurrency` at 4 or below.** The SDK already retries 429s with backoff.
- **Check the result in SQL afterwards.** Expect 13 rows per complete run, with failed agents as status rows. `datadict.v_coverage_gaps` must still be empty.

```sql
SELECT r.symbol, count(*) AS evals, count(*) FILTER (WHERE e.status = 'complete') AS complete
FROM eval.evaluations e JOIN eval.runs r USING (run_id) GROUP BY 1 ORDER BY 1;
```

**Still paused.** Do not do any of these until the user says so:
- Adding the GitHub DEV secrets (`TYPESAFE_API_KEY`, `SUPABASE_EVAL_DB_URL`) and the variable `JEV_MODEL`.
- Committing. A merge to `main` must carry `[skip ci]`.

**Open decisions.** These were offered but not yet approved:
- **NOW's geo-legal veto fired, probably wrongly.** Its `injected_or_offtopic_text` veto fired at p=0.54. Raising that veto's threshold to about 0.8 would fix it. This changes `rubric_sha`, which makes the stored runs eligible for re-evaluation; the Jev call cache keeps that cheap.
- **`v_stance_pivot.avg_stance_expected` counts low-evidence stances.** The fix is a one-line filter in the view, and the matching dictionary entry should be updated with it.
- **The datadict migrations are missing from Supabase's migration history.** They were applied through the Management API, not `apply_migration`.
- **`SUPABASE_ACCESS_TOKEN` in `.env` should be revoked** in the Supabase dashboard once no more admin SQL is needed.

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
| TypeSafe Jev | `TYPESAFE_API_KEY`, `JEV_MODEL` | Evaluation only | Scores agent outputs; `equity_mcp/evaluation/jev.py` |
| Supabase (eval project) | `SUPABASE_EVAL_DB_URL` | Evaluation only | Separate project, session-pooler URL, `eval_writer` role; unset → `evals/results/` |

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
