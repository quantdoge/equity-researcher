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
# Required:    OPENROUTER_API_KEY, FMP_API_KEY
# Recommended: FRED_API_KEY, SEC_USER_AGENT, BRAVE_API_KEY (or SERP_API_KEY)
# Legacy only: ANTHROPIC_API_KEY   (--legacy pipeline)
# Evaluation:  TYPESAFE_API_KEY, JEV_MODEL, SUPABASE_EVAL_DB_URL   (see "Evaluating research output")
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

## Evaluating research output (TypeSafe Jev)

Every research run can be scored, agent by agent, by [TypeSafe Jev](https://docs.typesafe.ai). Jev is a typed classifier that answers yes/no, ordinal-score and multiple-choice questions about a text. Each agent has a rubric in `equity_mcp/metrics/<role>.yaml`, plus `_shared.yaml`, which apply to every agent. Each rubric scores two separate blocks:

- **Conviction** says what the agent concluded. It has three parts:
  - A stance on the same five-way scale for every agent: STRONG SELL / SELL / HOLD / BUY / STRONG BUY.
  - A Low / Medium / High conviction level.
  - Role-specific **domain scores** on a 1–5 scale, such as profitability, liquidity and solvency for value, or E / S / G for ESG.
- **Alignment** says whether the output followed its prompt. It combines code checks with Jev questions:
  - Code checks: required sections, rating labels, tables, item counts, price-target arithmetic.
  - Jev questions: evidence, balance, consistency.

Results go to a separate Supabase project, schema **`eval`**.

### Prerequisites

```bash
# .env
TYPESAFE_API_KEY=apikey_...
JEV_MODEL=jev-1.13.0          # pin it — "jev-latest" moves, so scores wouldn't compare across runs
SUPABASE_EVAL_DB_URL=postgresql://eval_writer.<project_ref>:<password>@aws-0-<region>.pooler.supabase.com:5432/postgres?sslmode=require
```

- **Use the session pooler URL**, from Supabase dashboard → Connect → Session pooler. Direct database hosts are IPv6-only.
- **Without `SUPABASE_EVAL_DB_URL`** the evaluator still runs, but writes results to `evals/results/<run_id>.json` instead of Supabase.
- **One-time database setup:** apply `supabase/migrations/20261010000000_eval_schema.sql`. Then, as an admin, run `supabase/sql/eval_writer_role.sql`. It creates the least-privilege `eval_writer` login the URL above uses.
- **Can't see the tables?** The Supabase Table Editor opens on the `public` schema. Switch the schema dropdown to **`eval`**.

### Option 1: score as part of a research run

```bash
python -m equity_mcp.orchestrator --symbol AAPL --evaluate
EQR_EVALUATE=1 python -m equity_mcp.orchestrator --symbol AAPL   # same, via env
```

Scoring starts once the output JSON is written. It never fails the research run. The outcome is one `EVAL` line in `runs/<id>/run.log`, for example `EVAL roles=13 calls=84 errors=0 stances=…`, or `EVAL FAILED …`.

### Option 2: score a specific run

```bash
python -m equity_mcp.evaluation.evaluate --file outputs/AVGO_20261003T135110.json
python -m equity_mcp.evaluation.evaluate --symbol NOW --latest            # newest run of one ticker
python -m equity_mcp.evaluation.evaluate --symbol NOW --latest --roles value head   # some agents only (prefixes ok)
python -m equity_mcp.evaluation.evaluate --file outputs/IBM_*.json --blocks conviction   # stance/domain only
python -m equity_mcp.evaluation.evaluate --file outputs/AVGO_20261003T135110.json --force  # re-score anyway
python -m equity_mcp.evaluation.evaluate --file outputs/AVGO_20261003T135110.json --no-store  # local JSON only
```

Each agent prints one line:

```
value_researcher   complete stance=HOLD (1.00)  conv=Medium native=Hold  domain=3.9 (7/8)  align=0.92 vetoes=-  calls=7 (0 cached) → supabase
```

Runs are idempotent. A (run, agent, rubric version, Jev model) combination that is already stored is skipped. With `--force`, every unchanged question is answered from the `eval.jev_calls` cache at no cost.

### Option 3: backfill everything

```bash
python -m equity_mcp.evaluation.evaluate --all --dry-run                  # ALWAYS first: request count + token estimate, no network
python -m equity_mcp.evaluation.evaluate --all                            # every outputs/*.json
python -m equity_mcp.evaluation.evaluate --all --since 2026-10-01 --concurrency 6
python -m equity_mcp.evaluation.evaluate --flush-pending                  # replay results parked during a DB outage
```

A full research run costs about 75 Jev requests. Backfilling all the outputs currently in the repo is about 2,200 requests. Old-format output files with no `agent_results` are skipped, with the reason recorded. Failed or stub agents are recorded as such and cost no calls.

### Option 4: GitHub Actions

**Continuously, after every research run.** `.github/workflows/equity-research.yml` has an **"Evaluate outputs (Jev)"** step. For each ticker in the matrix, it scores the output that run just produced. It has three safeguards:
- It runs with `if: always()` and `continue-on-error: true`, so it can never fail the job or block the commit.
- It only scores outputs newer than the job's start (`--require-newer-than`), never an old checked-in file.
- It does nothing until the secrets below exist.

Set these up once, under repo Settings → Environments → `DEV`:

| Kind | Name | Value |
|---|---|---|
| Secret | `TYPESAFE_API_KEY` | your TypeSafe key |
| Secret | `SUPABASE_EVAL_DB_URL` | the session-pooler URL above |
| Variable | `JEV_MODEL` | `jev-1.13.0` |

> Every push to `main` triggers the **full paid research matrix**. Commits that only touch code, docs or workflows should carry `[skip ci]` in the message.

**On demand or backfill.** `.github/workflows/equity-eval.yml` runs from Actions → "Equity eval (backfill)" → **Run workflow**, or from the CLI:

```bash
gh workflow run equity-eval.yml                                    # dry run of everything (default)
gh workflow run equity-eval.yml -f dry_run=false -f symbol=NOW      # live, one ticker
gh workflow run equity-eval.yml -f dry_run=false -f since=2026-10-01 -f roles="value head"
```

| Input | Default | Meaning |
|---|---|---|
| `symbol` | *(empty = all)* | one ticker |
| `since` | — | only runs on/after `YYYY-MM-DD` |
| `roles` | — | space-separated agent names or prefixes |
| `blocks` | `both` | `both`, `conviction` or `alignment` |
| `force` | `false` | re-score stored evaluations |
| `dry_run` | **`true`** | plan only, no Jev calls |
| `order_check` | `false` | also ask choices with options reversed (bias check; extra cost) |

The workflow validates the rubrics first and never commits anything. It uploads `evals/` as an artifact, and a partial result (exit code 2) shows as a warning rather than a failure.

### Reading the results

The `eval` schema holds the raw tables (`runs`, `agent_outputs`, `evaluations`, `metric_results`, `jev_calls`, `rubrics`, `human_labels`) and these views:

| View | Shows |
|---|---|
| `v_stance_matrix` | one row per run × agent: stance, confidence, conviction, the agent's own rating, agreement |
| `v_stance_pivot` | one row per run, one stance column per agent, plus the specialists' average stance |
| `v_role_scorecard` | alignment composite, vetoes, domain mean per run × agent |
| `v_domain_scores` | every domain score (1–5) per run × agent × metric |
| `v_metric_trend` | weekly pass rate per question |
| `v_pipeline_reliability` | how often each agent fails or returns a stub |
| `v_jev_human_agreement` | your hand labels next to Jev's answers (calibration) |

```sql
SELECT * FROM eval.v_stance_pivot WHERE symbol = 'NOW' ORDER BY run_date DESC;
```

Every column of every `eval` table and view is documented in the **`datadict`** schema. For each column it records the type, owner, dates, definition, real example values, value range, and what each value means.

```sql
SELECT table_name, column_name, data_type, definition, example_values, value_range, value_meanings
FROM datadict.v_data_dictionary WHERE table_name = 'evaluations' ORDER BY ordinal_position;
```

What the main `evaluations` fields mean:

| Field | Source | Meaning |
|---|---|---|
| `stance` | Jev | most likely of STRONG SELL…STRONG BUY for the whole report |
| `stance_probabilities` | Jev | its probability for each of the five options |
| `stance_confidence` | Jev | how concentrated those probabilities are (not accuracy) |
| `stance_expected` | code | probability-weighted stance on −2 (STRONG SELL) … +2 (STRONG BUY) |
| `stance_low_evidence` | code | the report doesn't clearly take a view on owning the stock; treat the stance as unreliable |
| `conviction_score` / `conviction_level` | Jev / code | 0–2 commitment score, rounded to Low / Medium / High |
| `native_rating` | code | the agent's own headline label, e.g. "Pass", "Neutral", "Strong Short" |
| `native_stance` | code | that label mapped to the five-way scale (NULL for risk-only ratings) |
| `stance_agreement` | code | the agent's label and Jev's reading land on the same stance |
| `domain_mean` | code | mean of the agent's 1–5 domain scores |
| `alignment_composite` | code | 0–1 prompt-adherence score; `vetoes` lists hard failures separately |

All results are flagged **advisory** (`advisory = true`) until calibrated, meaning until Jev's answers have been checked against your own labels in `eval.human_labels`.

### Maintaining the rubrics

```bash
python -m equity_mcp.evaluation.evaluate --validate-rubrics     # schema + prompt-drift check (offline; also runs in CI)
python -m equity_mcp.evaluation.inspect value_researcher -v      # offline: how a rubric parses every real output
python -m equity_mcp.evaluation.evaluate --rehash-prompts        # current prompt hashes, after reviewing a rubric
python -m equity_mcp.evaluation.evaluate --list-models           # Jev models your key can use
python tests/test_eval_rubrics.py && python tests/test_eval_extract.py && python tests/test_eval_jev.py
```

Editing `equity_mcp/prompts/<role>.md` makes `--validate-rubrics` fail until the matching rubric has been reviewed and its `source_prompt_sha256` updated. That's deliberate: a rubric checks for the sections and labels a prompt asks for. Editing a rubric changes its version hash, so past runs become eligible for re-scoring under the new wording.

### Exit codes and troubleshooting

| Exit | Meaning |
|---|---|
| `0` | everything scored, or skipped with a reason |
| `1` | configuration error: invalid rubric, missing or rejected API key, floating model alias |
| `2` | finished, but some questions errored or results went to `evals/pending/` |

- **"Refusing floating model alias"**: set `JEV_MODEL=jev-1.13.0`, or pass `--allow-floating-model` if you really want `jev-latest`.
- **"evaluation database unreachable"**: results were parked in `evals/pending/`. Fix the URL, then run `--flush-pending`.
- **Tables not visible in Supabase**: switch the Table Editor's schema dropdown to `eval`.

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
├── prompts/               # System prompt .md file per agent role
├── metrics/               # Jev evaluation rubric .yaml per agent role + _shared.yaml
└── evaluation/            # Scores outputs/*.json with Jev → Supabase `eval` schema (CLI: evaluate, inspect)
supabase/
├── migrations/            # eval schema (tables, views, row-level security)
└── sql/eval_writer_role.sql   # one-time least-privilege login for the evaluator
.github/workflows/
├── equity-research.yml    # research matrix (+ Jev evaluation step)
└── equity-eval.yml        # on-demand / backfill evaluation
```

## FMP → Supabase Data Pipeline

A production-ready continuous ingestion pipeline lives on the `dev` branch:

- **Script**: `scripts/fmp_pipeline.py`
- **Config**: `pipeline/endpoints.yaml`
- **Schema**: `supabase/migrations/20260425_000001_init_fmp_pipeline.sql`
- **CI/CD**: `.github/workflows/daily-fmp-pipeline.yml`

See the `dev` branch for full documentation.
