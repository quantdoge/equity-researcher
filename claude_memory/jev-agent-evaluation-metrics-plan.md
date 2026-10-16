# Plan: Per-agent JEV evaluation metrics → Supabase

## Context
Each research run produces 13 agent outputs, saved in `outputs/<SYM>_<stamp>.json`: 11 specialists, `portfolio_strategist` and `head_of_research`. Today nothing measures either:
- what each agent concluded about the company, or
- whether the output followed its prompt in `equity_mcp/prompts/`.

We will add:
- **`equity_mcp/metrics/`** with one YAML file per agent. Each file defines two scored blocks:
  1. **Conviction.** What the agent concluded about the stock:
     - a mandatory **Choice of STRONG SELL / SELL / HOLD / BUY / STRONG BUY**,
     - a conviction level,
     - that agent's own **domain metric scores**, for example profitability, liquidity and solvency for value, or E, S and G for ESG.
  2. **Prompt alignment.** How well the output followed its prompt: required sections and enums, evidence, quantification, balance, consistency.
- **An evaluator** that sends curated background plus the relevant report text to TypeSafe **Jev** (`POST https://api.typesafe.ai/v1/systemone`), validates the typed answers, and stores everything in a **new, separate Supabase project**.

Decisions already made:
- Rubric files are YAML.
- Three triggers: manual CLI backfill, an opt-in orchestrator `--evaluate` flag, and a GitHub Action.
- A separate Supabase project.

### Constraints that shape the design
These come from the live Jev docs, the system-one skill and a repo audit.

**Jev limits**
- Context rot: send only the relevant sections, capped at 12k characters.
- Not a calculator or counter: section presence, enum extraction, tables, keyword coverage and price-target arithmetic are done **in code**.
- Score levels are weakly calibrated: use them as thresholds and profiles, not exact magnitudes.
- Choice leans toward the first option: run a reversed-order check on the calibration set.
- Question IDs are not sent to the model: every instruction must stand alone.
- Score has no way to abstain: abstention comes from gate Nouls or code coverage checks.

**Output data**
- `agent_results` holds only the 11 specialists. The portfolio strategist and head of research live in the `portfolio_brief` and `investment_memo` fields.
- Reports start with chatter.
- Native enums are hedged or upper-case (`In-Line-to-Above`, `HOLD / PASS`).
- The memo uses `**bold-line**` pseudo-headings.
- 6 of the 35 outputs use a legacy schema.
- Some outputs that count as successes are degenerate stubs (`"Sorry, need more steps…"` with `error: None`).

**CI and Supabase**
- Research commits carry `[skip ci]`, so the eval step has to run inside the research job.
- A normal push to `main` starts the 6-ticker research matrix, so infrastructure merges need `[skip ci]`.
- Supabase direct hosts are IPv6-only, so use the **session pooler** with psycopg `prepare_threshold=None`.
- Pin `typesafe-sdk` 0.7.4 to model `jev-1.13.0`, never `jev-latest`. Its `RetryPolicy` already retries 408, 429, 5xx and 529.

## Layout
```
equity_mcp/metrics/              # data only (user's requested layout)
  _shared.yaml                   # identical for all 13 roles: stance Choice + its gate, conviction_level,
                                 #   shared alignment items (honest gaps, sourcing, rating-vs-body consistency,
                                 #   other side considered, injected text veto, not_degenerate veto)
  sector_researcher.yaml … head_of_research.yaml   (13 files = roles.ALL_ROLES)
equity_mcp/evaluation/
  schema.py     pydantic models for the YAML (conviction + alignment blocks; discriminated Question union)
  loader.py     load + merge _shared, rubric_sha, prompt-drift check (source_prompt_sha256)
  extract.py    outputs json → 13 role records (ok|failed|degenerate|missing|skipped_synthesis); strip chatter;
                section splitter (##/###/**bold-line**); classify files by keys (legacy → skip w/ reason)
  checks.py     deterministic checks + keyword-coverage gates for domain metrics + native-enum regex extraction
  jev.py        AsyncTypeSafeClient wrapper; object state {evaluation_context, required_output, run, report_section};
                ≤6 questions/request; MAX_STATE_CHARS=12000; response validation; cache key; reversed-option pass
  stance.py     native enum → 5-point stance mapping, expected stance (−2..+2), conviction derivation
  crossagent.py pass-2 state: specialist stances/conviction/domain profile + failures + short-seller flags
  aggregate.py  alignment composite (weighted, vetoes separate, low_evidence excluded) + domain profile (not averaged in)
  store.py      psycopg async upserts (one txn per run×role), cached-call lookup, JSONL fallback evals/pending/
  evaluate.py   CLI + evaluate_result(result, path, …) library entry
supabase/migrations/20261010000000_eval_schema.sql
.github/workflows/equity-eval.yml   (workflow_dispatch backfill)
tests/test_eval_{rubrics,extract,checks,stance,jev,aggregate,store}.py
```

## Block A: Conviction (every agent)

### A1. Stance Choice: mandatory, identical wording across all 13 agents
The question is defined once in `_shared.yaml`, so stances are comparable across agents.
- **Instruction:** "Taking the report as a whole, which investment stance on this stock does it support for a long-only investor over the next 12 months?"
- **Criteria:** exactly `STRONG SELL`, `SELL`, `HOLD`, `BUY`, `STRONG BUY`, each with a one-line description. For example, `HOLD` reads: "balanced or neutral view; neither adding nor exiting is justified".
- **Abstention lane:** a sibling gate Noul, `stance_inferable`: "Does the report express or clearly imply a view on whether the stock is attractive to own?" This keeps the Choice at exactly five options. When the gate fails, for example on a macro report with no company view, the stance is stored with `low_evidence=true` and excluded from aggregates.

What is stored from the answer:
- `stance` (argmax), `stance_probabilities`, `stance_confidence`.
- `stance_expected = Σ p·v`, where v runs from −2 for STRONG SELL to +2 for STRONG BUY, computed in code.

### A2. Native-rating cross-check
Each role's YAML carries a `native_to_stance` map from that agent's own enum to the 5-point scale. Code extracts the native rating with regex and records `stance_agreement` against the Jev stance. A null entry means "no mapping", for example a risk rating that is not a buy/sell call.

| Role | Native enum → stance |
|---|---|
| value, growth | Strong Buy/Buy/Hold/Sell/Strong Sell → same |
| quant | Strong Buy/Buy/**Neutral→HOLD**/Sell/Strong Sell |
| short | Strong Short→STRONG SELL, Short→SELL, No Edge→HOLD, Reject Short Thesis→null (only says "not a short") |
| head_of_research | BUY/HOLD/SELL → same |
| portfolio_strategist | Initiate/Add→BUY, Hold/Pass→HOLD, Reduce→SELL, Exit→STRONG SELL |
| alt_data | Bullish→BUY, Neutral→HOLD, Bearish→SELL |
| esg (implication) | Positive→BUY, Neutral→HOLD, Negative→SELL |
| sector | Attractive→BUY, Neutral→HOLD, Unattractive→SELL |
| macro | Favourable→BUY, Neutral→HOLD, Unfavourable→SELL |
| geo_legal, fin_risk, nonfin_risk | null; their risk ratings feed domain metrics instead |

### A3. Conviction level (every agent)
A shared Score: "How strongly and unequivocally does the report commit to its stance?" Levels are Low / Medium / High, with concrete descriptions such as hedging language, conflicting signals, or explicit caveats.
- The portfolio strategist's `Conviction` column is checked against this in pass 2.
- For alt_data, the native `Confidence Level` enum is cross-checked as well.

### A4. Domain metric scores (role-specific)
**Scale.** Every domain metric is a 5-level Score oriented as *favourability to a long investor*: 1 = very unfavourable, 5 = very favourable. Each level has a description specific to that dimension. Risk dimensions read "very high risk" at 1 and "very low risk" at 5. Because the orientation is shared, profiles can be compared and charted across agents.

**What each metric declares:**
- `section`: which part of the report goes in the state.
- `evidence_terms`: a keyword list such as `[current ratio, quick ratio, cash, working capital]` for liquidity.

**Coverage gate.** Before any Jev call, code checks that the selected text mentions at least one evidence term.
- No match: the metric is `not_addressed`, it is not sent, and it costs nothing. This is the abstention lane Score itself lacks.
- Match: the Score is sent. Each result stores `score`, `probabilities` and `confidence`.

These scores record **the agent's assessment as written in its report**, not ground truth.

| Agent | Domain metrics (each a 5-level Score) |
|---|---|
| value_researcher | profitability, liquidity, solvency/leverage, cash-flow quality (FCF conversion), returns on capital (ROIC vs WACC), moat durability, valuation / margin of safety, management & capital allocation |
| growth_researcher | revenue growth, growth durability/visibility, TAM & penetration runway, gross-margin trajectory/unit economics, Rule of 40, estimate-revision momentum, stock price momentum, valuation vs growth (P/S, PEG) |
| esg_analyst | environmental, social, governance, controversy severity, regulatory ESG exposure, financial materiality of ESG factors |
| sector_researcher | sector growth, competitive intensity, barriers to entry, cycle position, company competitive position vs peers, relative margins/pricing power |
| geo_legal_researcher | geographic concentration risk, regulatory risk, litigation & enforcement risk, sanctions/export-control exposure, political & trade/tariff risk |
| macro_researcher | interest-rate sensitivity, economic growth/demand sensitivity, inflation & input-cost exposure, FX exposure, trade/tariff exposure, overall macro tailwind |
| fin_risk_analyst | leverage, interest coverage, liquidity, refinancing/maturity risk, FCF sustainability, market risk (volatility/drawdown), downside-scenario resilience |
| nonfin_risk_analyst | governance quality, insider-activity signal, regulatory exposure, operational concentration (supplier/customer), cyber & key-person risk, reputational risk |
| quant_analyst | value factor, momentum factor, quality factor, low-volatility factor, earnings-revision factor, risk-adjusted return (alpha/Sharpe) |
| short_analyst | earnings quality, accounting red flags (accruals/Beneish), working-capital red flags (receivables/inventory), moat erosion/competitive threat, management & governance red flags, bear-thesis credibility |
| alt_data_analyst | consumer demand trend, business activity (hiring/patents), digital traction (web/app), news sentiment, social sentiment, earnings preview vs consensus, data quality/recency |
| portfolio_strategist | consensus strength, risk/reward asymmetry, position-sizing appropriateness, portfolio fit/diversification, risk-management specificity, entry timing |
| head_of_research | business quality, valuation attractiveness, overall risk level, catalyst visibility, thesis balance (bull vs bear), price-target upside |

## Block B: Prompt alignment (every agent)
This block is kept from the earlier design.

**Deterministic checks in code**
- Required sections are present.
- Native enums are parseable; the main rating is a veto.
- Required tables and columns exist, for example quant's `Factor|Score|Sector Rank|Signal` with 5 rows, or the strategist's `Agent|View|Conviction|Key Finding`.
- Bullet counts are met, for example 3 tailwinds and 3 headwinds, or 3–5 catalysts.
- Numeric density meets the minimum.
- Price-target arithmetic adds up.

**Jev questions, grouped into requests of at most 6, each request with a gate Noul `section_evaluable`**
- Role-specific prompt rules, such as value's margin-of-safety rule, short's "present the other side", macro's "precise numbers and dates", alt_data's "note data limitations and lag", and ESG's "not solely self-reported scores".
- Shared items: honest data gaps, sourcing specificity, rating supported by the body, other side considered, and injected or off-topic text (veto).

**Pass 2: cross-agent checks for the strategist and head of research.** The state is built in code from the pass-1 stances, conviction levels, domain profiles and failures.
- Portfolio strategist:
  - Its conviction table matches the specialists' stances and conviction.
  - Fraud override veto: a short-analyst "Fraudulent Risk" combined with Initiate or Add.
  - The position size falls inside its band.
  - Failed agents are acknowledged.
- Head of research:
  - The verdict agrees with the balance of specialist stances, or justifies departing from it.
  - Value, risk and macro inputs are used.
  - Disagreements are flagged.
  - Team claims match reality. For example, the AVGO memo says "13 specialist reports" when there were 11.

## YAML shape (`value_researcher.yaml`, abridged)
```yaml
role: value_researcher
rubric_version: 1
pass: 1
includes: [_shared]                     # brings stance Choice + stance_inferable gate + conviction_level + shared alignment
source_prompt: equity_mcp/prompts/value_researcher.md
source_prompt_sha256: "<set by --rehash-prompts; test fails on drift>"
calibrated: false
background:
  mandate: >  Buffett-style value researcher … requires a 20–30% discount to intrinsic value …
  required_output: |  1. Business Quality (moat Wide/Narrow/None) … 5. Verdict Strong Buy…Strong Sell …
sections:
  moat: {heading: 'business quality|moat'}
  fin_quality: {heading: 'financial quality'}
  valuation: {heading: 'valuation|intrinsic'}
  management: {heading: 'management'}
  verdict: {heading: 'verdict'}
  risks: {heading: 'risk'}
  full: {whole_report: true, max_chars: 12000}

conviction:
  native_rating: {section: verdict, values: [Strong Buy, Buy, Hold, Sell, Strong Sell]}
  native_to_stance: {Strong Buy: STRONG BUY, Buy: BUY, Hold: HOLD, Sell: SELL, Strong Sell: STRONG SELL}
  domain_metrics:
    profitability:
      section: fin_quality
      evidence_terms: [margin, ROE, ROIC, net income, operating income, EBITDA]
      instructions: >
        Based only on the evidence in this report section, how strong is the company's profitability?
      criteria:
        - "Very weak: loss-making or margins far below peers and deteriorating"
        - "Weak: thin or declining margins"
        - "Average: margins in line with peers, stable"
        - "Strong: margins above peers and stable or rising"
        - "Very strong: sector-leading margins sustained over several years"
    liquidity:
      section: fin_quality
      evidence_terms: [current ratio, quick ratio, cash, working capital, liquidity]
      instructions: >
        Based only on the evidence in this report section, how strong is the company's
        short-term liquidity position?
      criteria: [ … 5 levels … ]
    solvency: { section: fin_quality, evidence_terms: [debt, leverage, net debt, interest coverage, Altman], … }
    cash_flow_quality: { … }
    returns_on_capital: { … }
    moat_durability: { section: moat, … }
    valuation_margin_of_safety: { section: valuation, … }
    capital_allocation: { section: management, … }

alignment:
  deterministic_checks:
    - {id: required_sections, kind: sections_present, sections: [moat, fin_quality, valuation, management, verdict, risks], weight: 2}
    - {id: verdict_parseable, kind: extract_ok, extract: native_rating, weight: 2, veto: true}
    - {id: fq_score_in_range, kind: extract_ok, extract: fq_score, weight: 1}
    - {id: valuation_numbers, kind: min_matches, section: valuation, pattern: '\$\s?\d[\d,.]*', min: 3, weight: 1}
    - {id: risk_items, kind: min_list_items, section: risks, min: 3, weight: 1}
  requests:
    - id: valuation_discipline
      state: [valuation, verdict]
      gate: section_evaluable
      questions:
        section_evaluable: {type: noul, weight: 0, instructions: "Does the section contain a substantive valuation …?"}
        margin_of_safety_applied: {type: score, dimension: consistency, weight: 3, criteria: [4 levels …]}
        intrinsic_value_method_explicit: {type: noul, dimension: evidence, weight: 2}
        implied_growth_addressed: {type: noul, dimension: evidence, weight: 1}
    - id: moat
      state: [moat]
      questions: { moat_evidence_strength: {type: score, …}, moat_trend_addressed: {type: noul, …} }
```

## Aggregation (`aggregate.py`, `stance.py`)
Each evaluation produces three things that are kept **separate** and never averaged together:
1. **Conviction:** `stance`, `stance_expected`, `stance_confidence`, `conviction_level`, `native_rating`, `native_stance`, `stance_agreement`.
2. **Domain profile:** `{metric: score | not_addressed}`, plus `domain_mean` over the addressed metrics only.
3. **Alignment composite:** a weighted mean of the normalised alignment metrics.
   - Vetoes are kept separate.
   - `low_evidence` answers are excluded.
   - The composite is NULL when less than 70% of the weight returned ok.

All composites stay `advisory=true` until calibrated.

## Supabase schema (`eval`; RLS on, no policies; `eval_writer` role via pooler)
| Table | Key columns | Unique |
|---|---|---|
| runs | run_id, symbol, run_date, source_path/sha256, schema_kind, skipped_synthesis, failures[], git_sha, skip_reason | PK run_id |
| agent_outputs | run_id, role, status, error, output_text/sha, chars, section_names[], agent_model(+inferred), extracts jsonb | (run_id, role) |
| rubrics | rubric_sha, role, rubric_version, source_prompt_sha256, content jsonb | PK rubric_sha |
| evaluations | run_id, role, rubric_sha, jev_model, pass, status, **stance, stance_probabilities, stance_expected, stance_confidence, stance_low_evidence, conviction_level, native_rating, native_stance, stance_agreement, domain_profile jsonb, domain_mean**, alignment_composite, alignment_dimensions jsonb, veto_triggered, vetoes[], insufficient_evidence, advisory | (run_id, role, rubric_sha, jev_model) |
| metric_results | evaluation_id, question_id, **block (conviction/domain/alignment)**, variant, kind, dimension, weight, noul_p/choice/score/probabilities/confidence, deterministic_value, code_extract, agreement, normalized, passed, status (ok/error/skipped/low_evidence/not_addressed) | (evaluation_id, question_id, variant) |
| jev_calls | cache_key, state/questions sha, model requested/returned, request_id, http_status, latency, tokens, answers, error | partial unique cache_key WHERE error IS NULL |
| human_labels | run_id, role, question_id, labeler, label | (run_id, role, question_id, labeler) |

The migration also creates these views:
- `v_stance_matrix`: run × role stances. Shows at a glance how the 13 agents voted on each ticker.
- `v_domain_scores`: long format, role × metric over time.
- `v_role_scorecard`: alignment results.
- `v_metric_trend`.
- `v_jev_human_agreement`.
- `v_pipeline_reliability`.

## CLI
```
python -m equity_mcp.evaluation.evaluate (--file P… | --all | --symbol SYM [--latest])
  [--since D] [--require-newer-than STAMP] [--roles value quant …] [--model jev-1.13.0]
  [--blocks conviction alignment] [--concurrency 4] [--force] [--dry-run] [--order-check]
  [--no-store | --flush-pending] [--validate-rubrics] [--rehash-prompts]
```
- **Idempotent:** a (run, role, rubric_sha, model) that has already been evaluated is skipped, and a `jev_calls` cache hit costs nothing.
- **Exit codes:** 0 ok; 1 for a config error, invalid YAML or a 401; 2 for partial errors or the DB fallback.
- **Output:** one line per role, for example `value_researcher  stance=HOLD (0.62) conv=Medium  domain=3.4 (8/8)  align=0.71  vetoes=-  calls=5`.

## Step-by-step execution (subagent assignment; ‖ = parallel)
**Phase 0: setup (main agent, needs you)**
1. Create branch `feat/llm-eval`. Confirm whether CLAUDE.md's `claude/multi-agent-equity-research-DOiTR` rule still applies.
2. Create Supabase project `equity-research-eval` in the Stocksight.AI org via the Supabase MCP: get_cost → you confirm → create_project. It would be the org's second active project.
3. Get the session-pooler URL and create the `eval_writer` role via `execute_sql`. The password stays out of git.
4. Add DEV secrets `TYPESAFE_API_KEY` and `SUPABASE_EVAL_DB_URL`, and the variable `JEV_MODEL=jev-1.13.0`.
5. Jev smoke test: `models.list()` and one call with stance Choice + Score + Noul on an AVGO section. Save the response as `tests/fixtures/jev_response_sample.json`.

**Phase 1: contracts**
- 1.0 **python-pro**: `schema.py` (conviction + alignment blocks). This blocks the rest of Phase 1.
- Then three tracks in parallel:
  - 1.1 **ai-engineer**: `_shared.yaml` (stance Choice, gate, conviction_level, shared alignment) and the exemplar `value_researcher.yaml`. After that, three ai-engineer instances in parallel, each writing the domain metrics (with 5 described levels and `evidence_terms`), the `native_to_stance` map and the alignment block:
    - 1.2: sector, geo_legal, macro, growth
    - 1.3: fin_risk, nonfin_risk, quant, short
    - 1.4: esg, alt_data, portfolio_strategist, head_of_research
  - ‖ 1.5 **python-pro**: `loader.py`, `extract.py`, `checks.py`, `stance.py`. Fixtures: AVGO, IBM, ZS, AAPL_184412, AMD_20260822.
  - ‖ 1.6 **sql-pro**: migration SQL with the new stance and domain columns, views and RLS.

**Phase 2: engine** (2.1 ‖ 2.2 ‖ 2.3)
- 2.1 **ai-engineer**: `jev.py`, with `RetryPolicy(max_retries=4, backoff_max=20, timeout=180)` and an explicit model.
- 2.2 **data-engineer**: `store.py`, using `psycopg.AsyncConnection.connect(url, prepare_threshold=None)`.
- 2.3 **python-pro**: `aggregate.py` and `crossagent.py`.

**Phase 3: entry points** (3.1 ‖ 3.2 ‖ 3.3)
- 3.1 **cli-developer**: `evaluate.py`.
- 3.2 **python-pro**: `orchestrator.py`.
  - Add a `--evaluate` flag, also switchable with `EQR_EVALUATE=1`.
  - After the outputs JSON is written (around line 156), lazily import the evaluator and run `asyncio.wait_for(evaluate_result(...), 900)` in a `try/except`, then log `run_log.event("EVAL …")`. It must never fail the run.
  - Also record `result["models"]` and `result["prompt_sha256"]`.
- 3.3 **python-pro**: `pyproject.toml`.
  - Add `typesafe-sdk>=0.7.4,<0.8` and `pydantic>=2.12`.
  - Add package-data for `metrics/*.yaml` and `prompts/*.md`.
  - Update `uv.lock` and `requirements.txt`, and add `evals/` to `.gitignore`.

**Phase 4: delivery** (4.1 ‖ 4.2 ‖ 4.3 ‖ 4.4)
- 4.1 **agents-infrastructure-operations:deployment-engineer**: add an eval step to `equity-research.yml` between the pipeline and the commit step. It uses `if: always()`, `continue-on-error: true` and `timeout-minutes: 20`, and runs `--symbol ${{ matrix.ticker }} --latest --require-newer-than $JOB_START`.
- 4.2 **deployment-engineer**: `equity-eval.yml`, a workflow_dispatch backfill. Inputs: symbol, since, roles, blocks, force, dry_run. It is read-only and never commits.
- 4.3 **python-pro**: `tests/test_eval_*.py`. They run under pytest or standalone, like `tests/test_tool_access.py`.
- 4.4 main agent / `document-writer` skill: an Evaluation section in CLAUDE.md, an External APIs row, and the new `.env.example` variables.

**Phase 5: rollout (main agent + you)**
1. `apply_migration`, then `list_tables`, then `get_advisors(security)`, then grant `eval_writer`.
2. Run `--validate-rubrics`, then `--all --dry-run`. Expect 29 files processed, 6 legacy files skipped, about 70–80 Jev calls per run and about 2.2k for the backfill. **Confirm the cost before going live.**
3. Run one live file (AVGO) and inspect `v_stance_matrix` and `v_domain_scores`. Then run `--all`, and rerun to confirm the rerun makes 0 calls.
4. Calibration, by **data-analyst** with you: label about 25 reports, including each report's stance, 2–3 domain scores per role and key alignment items. Run `--order-check` on the stance Choice to measure lean toward the first option. A question is marked `calibrated: true` only at ≥80% agreement.

## Verification
**Offline tests**
- Rubric files:
  - Every role in `ALL_ROLES` has exactly one YAML file.
  - Each YAML has a `conviction` block containing ≥4 domain metrics, each with 5 levels and non-empty `evidence_terms`, plus a `native_to_stance` map.
  - The shared stance Choice has exactly the 5 options.
  - Every native enum appears verbatim in its prompt.
  - The prompt-hash drift guard catches prompt edits without a rubric review.
  - Requests have ≤6 questions each and stay within 12k characters of state.
- Stance (`stance.py`):
  - Mapping covers quant Neutral→HOLD and short Reject→null.
  - `stance_expected` maths is correct.
- Evidence gate: the AVGO value report gives profitability and liquidity as addressed. A synthetic report without liquidity terms gives `not_addressed` with no call made.
- Extraction: AVGO gives moat=Wide, fq=8, verdict=Hold→HOLD. IBM is detected as failed, AAPL_184412 as degenerate, and AMD_20260822 as legacy.
- Jev validator: rejects a stance outside the 5 options, a score out of range, or an out-of-range noul. A 422 becomes a metric error; a 401 is fatal.
- Aggregation: vetoes are not averaged away, and the domain profile is not mixed into the alignment composite.
- Store: an upsert is idempotent. This test runs only when `SUPABASE_EVAL_DB_URL_TEST` is set.

**Live checks**
- A dry run, then a single live file.
- Orchestrator smoke test: `--symbol AAPL --agents macro esg --skip-synthesis --evaluate --max-concurrency 2 --timeout 600`. Expect an `EVAL` line in `run.log`.
- A dispatch of `equity-eval.yml` with `dry_run=true`.

## Risks
- **What the domain scores mean.** They measure what the agent *claims*, not the truth. An optional later step could anchor a few of them, such as liquidity and solvency, to ratios from the existing FMP calculation tools.
- **Cost.** About 70–80 Jev calls per run. Keep `--order-check` to the calibration set.
- **Bias toward the first option.** The stance options are listed STRONG SELL first, so any first-option lean would push toward bearish answers. Measure it before trusting the stance distribution.
- **Hedged native enums.** Expect a high rate of `not_stated` extracts, and report that as a prompt-compliance finding.
- **Merging to main.** The merge commit must carry `[skip ci]`.
