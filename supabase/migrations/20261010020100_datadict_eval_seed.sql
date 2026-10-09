-- =============================================================================
-- datadict seed: documentation for every table, view and column in `eval`.
--
-- data_type / is_nullable / ordinal_position come from pg_catalog, never from
-- this file. Pass-through view columns are generated: they get derived_from =
-- their source column and inherit its documentation in v_data_dictionary.
-- Example values are real values from the AVGO/IBM/NOW runs stored 2026-10-10.
-- Idempotent: re-running updates text but never resets created_date.
-- =============================================================================

-- -----------------------------------------------------------------------------
-- 1. Objects
-- -----------------------------------------------------------------------------
INSERT INTO datadict.tables (schema_name, table_name, object_type, description, grain, primary_key) VALUES
('eval', 'runs', 'table',
 'One research output file (outputs/<SYMBOL>_<stamp>.json) that was ingested for evaluation. Legacy-format files are recorded here with a skip_reason and nothing else.',
 'one row per research run', 'run_id'),
('eval', 'agent_outputs', 'table',
 'The report each research agent wrote in a run, with its pipeline status and the values code extracted from it.',
 'one row per run × agent role', 'id; unique (run_id, role)'),
('eval', 'rubrics', 'table',
 'Immutable snapshot of each metrics/<role>.yaml rubric merged with _shared.yaml, keyed by its hash, so every evaluation can be traced to the exact questions asked.',
 'one row per distinct rubric content', 'rubric_sha'),
('eval', 'jev_calls', 'table',
 'Log of every request sent to TypeSafe Jev. Successful calls double as a cache: an identical state + questions + model is never paid for twice.',
 'one row per Jev API request', 'id; unique cache_key where error is null'),
('eval', 'evaluations', 'table',
 'Headline result of scoring one agent''s report: its stance and conviction, its domain profile, and its prompt-alignment score with vetoes. The table most people should start from.',
 'one row per run × agent role × rubric version × Jev model', 'id; unique (run_id, role, rubric_sha, jev_model)'),
('eval', 'metric_results', 'table',
 'Every individual answer behind an evaluation: each Jev question (noul/score/choice) and each code check, with raw readout, normalised 0–1 value and pass/fail.',
 'one row per evaluation × question × variant', 'id; unique (evaluation_id, question_id, variant)'),
('eval', 'human_labels', 'table',
 'Hand-made judgments of individual rubric questions, used to check how often Jev agrees with a human before results stop being advisory.',
 'one row per run × agent role × question × labeller', 'id; unique (run_id, role, question_id, labeler)'),
('eval', 'v_latest_evaluations', 'view',
 'evaluations restricted to the most recent evaluation of each run × agent (latest finished_at), with the run''s symbol and date. Base of the other reporting views.',
 'one row per run × agent role', NULL),
('eval', 'v_stance_matrix', 'view',
 'Long-format stance table: what every agent concluded in every run, next to the agent''s own headline rating.',
 'one row per run × agent role', NULL),
('eval', 'v_stance_pivot', 'view',
 'Wide stance table: one row per run with one stance column per agent, plus the specialists'' average expected stance.',
 'one row per run', NULL),
('eval', 'v_domain_scores', 'view',
 'Every domain metric score (profitability, governance, sector growth, …) from the latest evaluations, on a 1–5 scale.',
 'one row per run × agent role × domain metric × variant', NULL),
('eval', 'v_role_scorecard', 'view',
 'Quality scorecard per run × agent: alignment composite and coverage, vetoes, evidence flag, domain mean, stance and conviction.',
 'one row per run × agent role', NULL),
('eval', 'v_metric_trend', 'view',
 'Weekly pass rate and mean normalised score of each question per agent, for spotting rubric questions or agents that drift.',
 'one row per agent role × question × block × week', NULL),
('eval', 'v_jev_human_agreement', 'view',
 'Each human label next to Jev''s answer to the same question, for calibration.',
 'one row per human label (that has a matching Jev answer)', NULL),
('eval', 'v_pipeline_reliability', 'view',
 'How often each research agent produced a usable report, failed, or returned a stub. Measures the research pipeline, not report quality.',
 'one row per agent role', NULL)
ON CONFLICT (schema_name, table_name) DO UPDATE SET
    object_type = EXCLUDED.object_type, description = EXCLUDED.description,
    grain = EXCLUDED.grain, primary_key = EXCLUDED.primary_key;

-- -----------------------------------------------------------------------------
-- 2. Columns with their own documentation
-- -----------------------------------------------------------------------------
WITH
roles(j) AS (SELECT '{
  "sector_researcher": "Industry structure, cycle, tailwinds/headwinds, peer benchmarking",
  "geo_legal_researcher": "Country, regulatory, sanctions and litigation risk",
  "macro_researcher": "Rates, inflation, growth, FX and their effect on the company",
  "value_researcher": "Buffett-style moat, financial quality, intrinsic value vs price",
  "growth_researcher": "TAM, growth durability, catalysts, valuation for growth",
  "fin_risk_analyst": "Credit, liquidity and market risk; downside scenario",
  "nonfin_risk_analyst": "Governance, regulatory, operational, reputational risk; insider activity",
  "quant_analyst": "Factor scores, momentum, risk-adjusted returns",
  "short_analyst": "Forensic short-seller view: earnings quality, red flags, bear case",
  "esg_analyst": "Financially material environmental, social and governance factors",
  "alt_data_analyst": "Search, hiring, web, sentiment and other leading indicators",
  "portfolio_strategist": "Synthesises the specialists into position size and portfolio action (evaluated in pass 2)",
  "head_of_research": "Writes the final investment memo and verdict (evaluated in pass 2)"
}'::jsonb),
stances(j) AS (SELECT '{
  "STRONG SELL": "(-2) Strongly negative: the stock should be avoided or sold; severe downside or dominant risks",
  "SELL": "(-1) Negative: unfavourable findings outweigh favourable ones; reduce or avoid",
  "HOLD": "(0) Balanced or neutral: findings roughly offset; neither adding nor exiting is justified",
  "BUY": "(+1) Positive: favourable findings outweigh unfavourable ones; owning or adding is justified",
  "STRONG BUY": "(+2) Strongly positive: compelling upside with limited risks; high-conviction purchase"
}'::jsonb),
doc(table_name, column_name, key_role, value_kind, source, definition, example_values, value_range, value_meanings, derived_from) AS (VALUES
-- ── eval.runs ────────────────────────────────────────────────────────────────
('runs', 'run_id', 'PK', 'identifier', 'pipeline',
 'Identifier of the research run: <SYMBOL>_<YYYYmmddTHHMMSS> in the research machine''s local clock. Same as the output file name and the runs/<run_id>/ log directory.',
 'IBM_20261006T150931; AVGO_20261003T135110', 'Unique. Legacy files without a run_id use their file name stem (e.g. CMG_2026-08-01).', NULL::jsonb, NULL::text),
('runs', 'symbol', NULL, 'identifier', 'pipeline', 'Ticker researched.', 'IBM; AVGO; NOW', 'Upper-case exchange ticker.', NULL, NULL),
('runs', 'run_date', NULL, 'date', 'pipeline', 'Date the research run was produced.', '2026-10-06', 'Calendar date; NULL only if neither the output nor its name carried one.', NULL, NULL),
('runs', 'source_path', NULL, 'free_text', 'code', 'Repository-relative path of the output JSON that was evaluated.', 'outputs/IBM_20261006T150931.json', 'NULL when evaluated in-process by orchestrator --evaluate without a saved file.', NULL, NULL),
('runs', 'source_sha256', NULL, 'hash', 'code', 'SHA-256 of the output file''s bytes at evaluation time; shows whether the file changed afterwards.', '6655c6cda036…', '64 hex characters, or NULL when evaluated from memory.', NULL, NULL),
('runs', 'schema_kind', NULL, 'categorical', 'code', 'Which output-file format the run uses, decided from its keys rather than its name.', 'agent_results_v1', 'agent_results_v1 | legacy',
 '{"agent_results_v1": "Current format with an agent_results list; evaluated", "legacy": "Old master-agent format (Jul–Aug 2026); recorded with skip_reason, not evaluated"}', NULL),
('runs', 'skipped_synthesis', NULL, 'boolean', 'pipeline', 'Whether the run was a --skip-synthesis smoke test, i.e. had no portfolio brief and no memo.', 'false', 'true | false',
 '{"true": "Specialists only; portfolio_strategist and head_of_research absent", "false": "Full run"}', NULL),
('runs', 'failures', NULL, 'list', 'pipeline', 'Agent roles that failed during the research run itself (errors or timeouts).', '{geo_legal_researcher,value_researcher,growth_researcher}', 'Empty array = no failures; otherwise any of the 13 role names.', NULL, NULL),
('runs', 'elapsed_seconds', NULL, 'continuous', 'pipeline', 'Wall-clock duration of the whole research run.', '695.1', 'Seconds, ≥ 0; full runs take roughly 600–1,100 s.',
 '{"high": "Slow run; agents more likely to have hit timeouts", "low": "Fast run, or a partial/smoke run"}', NULL),
('runs', 'git_sha', NULL, 'hash', 'code', 'Commit of this repository when the evaluation ran (GITHUB_SHA in CI, else git rev-parse HEAD).', '3c7b8691ab…', '40 hex characters, or NULL if git was unavailable.', NULL, NULL),
('runs', 'skip_reason', NULL, 'free_text', 'code', 'Why the run was recorded but not evaluated.', 'legacy schema: no agent_results', 'NULL for evaluated runs.', NULL, NULL),
('runs', 'ingested_at', NULL, 'timestamp', 'database', 'When the run was first stored.', '2026-10-09 18:24:32+00', 'UTC timestamp; set once.', NULL, NULL),
('runs', 'updated_at', NULL, 'timestamp', 'database', 'When the row was last modified (every re-evaluation upserts it).', '2026-10-09 18:24:32+00', 'UTC timestamp; maintained by trigger.', NULL, NULL),

-- ── eval.agent_outputs ───────────────────────────────────────────────────────
('agent_outputs', 'id', 'PK', 'identifier', 'database', 'Surrogate key.', '4', 'Positive integer, generated.', NULL, NULL),
('agent_outputs', 'run_id', 'FK → eval.runs.run_id', 'identifier', 'pipeline', 'Run the report belongs to.', 'AVGO_20261003T135110', 'Must exist in eval.runs.', NULL, NULL),
('agent_outputs', 'role', 'unique with run_id', 'categorical', 'pipeline', 'Which research agent wrote the report.', 'value_researcher', 'One of the 13 agent roles.', (SELECT j FROM roles), NULL),
('agent_outputs', 'status', NULL, 'categorical', 'code', 'Whether the agent produced a report worth evaluating.', 'ok; failed', 'ok | failed | degenerate | missing',
 '{"ok": "Usable report; evaluated", "failed": "Agent errored, timed out or returned nothing; recorded, no Jev calls", "degenerate": "Agent ''succeeded'' but returned a stub such as ''Sorry, need more steps…'' (under ~400 chars or no headings); not evaluated", "missing": "Expected but absent from the output file"}', NULL),
('agent_outputs', 'error', NULL, 'free_text', 'pipeline', 'Error the research pipeline recorded for this agent.', 'ReadError: ; TimeoutError: ', 'NULL when the agent completed.', NULL, NULL),
('agent_outputs', 'output_text', NULL, 'free_text', 'pipeline', 'The full markdown report exactly as the agent wrote it, including any leading chatter.', '# Broadcom Inc. (AVGO) — Value Investment Analysis …', 'Typically 3,800–11,000 characters; empty for failed agents.', NULL, NULL),
('agent_outputs', 'output_sha256', NULL, 'hash', 'code', 'SHA-256 of output_text.', 'a1b2c3…', '64 hex characters; NULL when empty.', NULL, NULL),
('agent_outputs', 'chars', NULL, 'count', 'code', 'Length of output_text in characters.', '8592', '≥ 0; 0 for failed agents.', NULL, NULL),
('agent_outputs', 'preamble_chars', NULL, 'count', 'code', 'Length of the chatter before the report''s first heading (e.g. "All data gathered. Here is the brief."), which is stripped before evaluation.', '0; 96', '≥ 0; 0 = report starts with its heading.', NULL, NULL),
('agent_outputs', 'section_names', NULL, 'list', 'code', 'Headings the section splitter found (markdown ## headings, or **bold-line** pseudo-headings in memos).', '{"1. Business Quality Assessment — Moat: Wide …","2. Financial Quality Score — 8 / 10",…}', 'Array of heading texts; empty when not parsed.', NULL, NULL),
('agent_outputs', 'agent_model', NULL, 'categorical', 'pipeline', 'LLM (OpenRouter slug) that wrote the report.', 'deepseek/deepseek-v4-flash-0731', 'Any OpenRouter model slug.', NULL, NULL),
('agent_outputs', 'agent_model_inferred', NULL, 'boolean', 'code', 'Whether agent_model was recorded in the run or guessed from today''s roles.py.', 'true', 'true | false',
 '{"true": "Run did not record its models; taken from current roles.py (may be wrong for old runs)", "false": "Recorded in the run''s models field"}', NULL),
('agent_outputs', 'elapsed_seconds', NULL, 'continuous', 'pipeline', 'How long the agent itself ran.', '86.2; 750.3 (timeout)', 'Seconds ≥ 0; ~750 s usually means it hit its timeout.',
 '{"high": "Long tool-use loop or a timeout", "low": "Quick run, or an early failure"}', NULL),
('agent_outputs', 'extracts', NULL, 'json', 'code', 'Values code pulled out of the report by regex, as defined in the rubric''s extract block: {extract_id: {value, hedged}}. hedged = the heading named more than one allowed value.', '{"verdict": {"value": "Hold", "hedged": true}, "fq_score": {"value": 8, "hedged": false}, "moat_rating": {"value": "Wide", "hedged": false}}', 'Object; value is NULL when the report did not state a parseable value.', NULL, NULL),
('agent_outputs', 'created_at', NULL, 'timestamp', 'database', 'When the row was first stored.', '2026-10-09 18:09:51+00', 'UTC timestamp.', NULL, NULL),
('agent_outputs', 'updated_at', NULL, 'timestamp', 'database', 'When the row was last modified.', '2026-10-09 18:09:51+00', 'UTC timestamp; maintained by trigger.', NULL, NULL),

-- ── eval.rubrics ─────────────────────────────────────────────────────────────
('rubrics', 'rubric_sha', 'PK', 'hash', 'code', 'SHA-256 of the merged rubric (metrics/<role>.yaml + _shared.yaml). Any wording change gives a new hash, which makes past runs eligible for re-evaluation.', 'e408cc1d8139…', '64 hex characters.', NULL, NULL),
('rubrics', 'role', NULL, 'categorical', 'code', 'Agent role the rubric scores.', 'sector_researcher', 'One of the 13 agent roles.', (SELECT j FROM roles), NULL),
('rubrics', 'rubric_version', NULL, 'ordinal', 'human', 'Version number written in the role''s YAML; bumped by hand on deliberate revisions.', '1', 'Integer ≥ 1; higher = newer revision.', NULL, NULL),
('rubrics', 'shared_version', NULL, 'ordinal', 'human', 'Version of _shared.yaml (the stance, conviction and shared quality questions) included in this rubric.', '1', 'Integer ≥ 1.', NULL, NULL),
('rubrics', 'source_prompt_sha256', NULL, 'hash', 'code', 'Hash of prompts/<role>.md that the rubric was written against; --validate-rubrics fails when the prompt changes.', '71c92f6cf7cb…', '64 hex characters.', NULL, NULL),
('rubrics', 'calibrated', NULL, 'boolean', 'human', 'Whether this rubric''s answers have been validated against human labels.', 'false', 'true | false',
 '{"false": "Results are advisory (evaluations.advisory = true)", "true": "Agreement with human labels was checked and accepted"}', NULL),
('rubrics', 'content', NULL, 'json', 'code', 'The full merged rubric: sections, extracts, domain metrics, checks and every question''s exact wording.', '{"role": {...}, "shared": {...}}', 'JSON object.', NULL, NULL),
('rubrics', 'created_at', NULL, 'timestamp', 'database', 'When this rubric version was first used.', '2026-10-09 18:09:51+00', 'UTC timestamp.', NULL, NULL),

-- ── eval.jev_calls ───────────────────────────────────────────────────────────
('jev_calls', 'id', 'PK', 'identifier', 'database', 'Surrogate key.', '1', 'Positive integer, generated.', NULL, NULL),
('jev_calls', 'cache_key', 'unique where error is null', 'hash', 'code', 'SHA-256 of (model, state hash, questions hash). A successful call with the same key is reused instead of paid for again.', '4443a1c8f20d…', '64 hex characters.', NULL, NULL),
('jev_calls', 'state_sha256', NULL, 'hash', 'code', 'Hash of the JSON state sent (report section + context).', '9f2c…', '64 hex characters.', NULL, NULL),
('jev_calls', 'questions_sha256', NULL, 'hash', 'code', 'Hash of the questions sent.', '1b7e…', '64 hex characters.', NULL, NULL),
('jev_calls', 'jev_model_requested', NULL, 'categorical', 'code', 'Jev model asked for (pinned via JEV_MODEL).', 'jev-1.13.0', 'A Jev model id; floating aliases like jev-latest are refused by default.', NULL, NULL),
('jev_calls', 'jev_model_returned', NULL, 'categorical', 'jev', 'Model that actually answered, as reported by Jev.', 'jev-1.13.0', 'A concrete Jev version; NULL when the call failed.', NULL, NULL),
('jev_calls', 'request_id', NULL, 'identifier', 'jev', 'Jev''s request id (x-typesafe-request-id header), for support tickets.', 'req_01a121da173c7b678c85472928a93bb6', 'NULL when the call never reached Jev.', NULL, NULL),
('jev_calls', 'http_status', NULL, 'categorical', 'jev', 'HTTP status of the final attempt.', '200', '200 | 422 | 429 | 5xx | NULL',
 '{"200": "Answered", "422": "Request rejected as malformed: a rubric bug", "429": "Rate limited after all retries", "5xx/529": "Jev error or overload after all retries", "NULL": "Connection failure; nothing received"}', NULL),
('jev_calls', 'latency_ms', NULL, 'continuous', 'code', 'Time from sending the request to receiving the answer.', '405', 'Milliseconds; observed 233–469.', '{"high": "Slow response (large state or load)", "low": "Fast response"}', NULL),
('jev_calls', 'input_tokens', NULL, 'count', 'jev', 'Input tokens Jev billed for the request.', '2342', 'Observed 638–4,607; the main cost driver.', '{"high": "Large report section sent", "low": "Short state"}', NULL),
('jev_calls', 'output_tokens', NULL, 'count', 'jev', 'Output tokens Jev billed (roughly proportional to the number of questions).', '91', 'Observed ≤ 168.', NULL, NULL),
('jev_calls', 'state_chars', NULL, 'count', 'code', 'Size of the JSON state sent, in characters.', '5513', 'Capped near 12,000; observed 993–11,965.', '{"high": "Near the cap; more context, more context-rot risk", "low": "Narrow, focused state"}', NULL),
('jev_calls', 'state_truncated', NULL, 'boolean', 'code', 'Whether the report text was cut to fit the 12,000-character cap.', 'false', 'true | false', '{"true": "Some report text was not seen by Jev", "false": "Jev saw the full selected sections"}', NULL),
('jev_calls', 'answers', NULL, 'json', 'jev', 'Jev''s raw answers keyed by question id, exactly as returned.', '{"stance": {"type": "choice", "choice": "BUY", "confidence": 0.96, "probabilities": {...}}}', 'JSON object; NULL when the call failed.', NULL, NULL),
('jev_calls', 'error', NULL, 'free_text', 'code', 'Why the call failed. NULL means success; only successful calls are cached.', 'http 529: overloaded; connection: ReadTimeout', 'NULL on success.', NULL, NULL),
('jev_calls', 'created_at', NULL, 'timestamp', 'database', 'When the call was logged.', '2026-10-09 18:09:51+00', 'UTC timestamp.', NULL, NULL),

-- ── eval.evaluations ─────────────────────────────────────────────────────────
('evaluations', 'id', 'PK', 'identifier', 'database', 'Surrogate key.', '4', 'Positive integer, generated.', NULL, NULL),
('evaluations', 'run_id', 'FK → eval.runs.run_id', 'identifier', 'pipeline', 'Run evaluated.', 'AVGO_20261003T135110', 'Must exist in eval.runs.', NULL, NULL),
('evaluations', 'role', NULL, 'categorical', 'pipeline', 'Agent whose report was evaluated.', 'value_researcher', 'One of the 13 agent roles.', (SELECT j FROM roles), NULL),
('evaluations', 'agent_output_id', 'FK → eval.agent_outputs.id', 'identifier', 'database', 'The report evaluated.', '4', 'Must exist in eval.agent_outputs.', NULL, NULL),
('evaluations', 'rubric_sha', 'FK → eval.rubrics.rubric_sha', 'hash', 'code', 'Exact rubric version used.', 'e408cc1d8139…', '64 hex characters.', NULL, NULL),
('evaluations', 'jev_model', NULL, 'categorical', 'code', 'Jev model requested for this evaluation; part of the uniqueness key, so a new model means a new evaluation row.', 'jev-1.13.0', 'A Jev model id.', NULL, NULL),
('evaluations', 'evaluator_version', NULL, 'ordinal', 'code', 'Version of the equity_mcp.evaluation code (EVALUATOR_VERSION).', '1', 'String; bumped when scoring logic changes.', NULL, NULL),
('evaluations', 'pass', NULL, 'ordinal', 'code', 'Which evaluation pass scored this agent.', '1', '1 | 2',
 '{"1": "Specialist; scored first", "2": "portfolio_strategist or head_of_research; scored after the specialists, with a code-built summary of what they concluded"}', NULL),
('evaluations', 'status', NULL, 'categorical', 'code', 'Outcome of the evaluation.', 'complete; agent_failed', 'complete | partial | agent_failed | degenerate | missing | error',
 '{"complete": "All questions answered", "partial": "Some Jev calls or answers failed, or under 70% of alignment weight was usable; scores may be NULL", "agent_failed": "The agent produced no report; nothing scored, no calls", "degenerate": "The agent returned a stub; nothing scored", "missing": "Agent absent from the run", "error": "Evaluation itself failed"}', NULL),
('evaluations', 'stance', NULL, 'categorical', 'jev', 'The investment stance the whole report supports, according to Jev (the most likely of five options in the shared stance question).', 'HOLD; SELL; STRONG BUY', 'STRONG SELL | SELL | HOLD | BUY | STRONG BUY | NULL (call failed)', (SELECT j FROM stances), NULL),
('evaluations', 'stance_probabilities', NULL, 'json', 'jev', 'Jev''s probability for each of the five stances. Sums to 1.', '{"STRONG SELL": 0.03, "SELL": 0.59, "HOLD": 0.37, "BUY": 0.01, "STRONG BUY": 0.0}', 'Each value 0–1; total 1 (±0.02).', NULL, NULL),
('evaluations', 'stance_expected', NULL, 'continuous', 'code', 'Probability-weighted stance: Σ p × value with STRONG SELL = −2 … STRONG BUY = +2. Keeps the uncertainty that stance discards and can be averaged across agents.', '-0.64; 0.00; 1.97', '−2.0 … +2.0; observed −1.94 … 1.97.',
 '{"+2": "Unanimously STRONG BUY", "+1": "BUY-leaning", "0": "Neutral, or split evenly", "-1": "SELL-leaning", "-2": "Unanimously STRONG SELL"}', NULL),
('evaluations', 'stance_confidence', NULL, 'continuous', 'jev', 'How concentrated Jev''s stance probabilities are. Not a measure of correctness.', '0.49; 1.00', '0–1.',
 '{"high (≈1)": "Nearly all probability on one stance", "low (≈0.4–0.5)": "Probability spread across two or more stances, e.g. SELL vs HOLD"}', NULL),
('evaluations', 'stance_low_evidence', NULL, 'boolean', 'code', 'True when the stance gate question (does the report take a view on owning the stock?) came back below 0.5. The stance is stored but should be treated as unreliable.', 'false; true (NOW geo-legal)', 'true | false',
 '{"true": "Report mostly describes conditions without a view on ownership; treat stance with caution", "false": "Report clearly takes a view"}', NULL),
('evaluations', 'conviction_level', NULL, 'ordinal', 'code', 'How firmly the report commits to its view: conviction_score rounded and named.', 'Medium', 'Low | Medium | High | NULL. All evaluations to 2026-10-10 are Medium.',
 '{"Low": "Heavily hedged, conflicting signals unresolved, or data said to be insufficient", "Medium": "Clear view with material caveats, conditions or offsetting risks", "High": "Unequivocal view, consistently supported, few caveats"}', NULL),
('evaluations', 'conviction_score', NULL, 'continuous', 'jev', 'Jev''s probability-weighted conviction level on the 0-based scale 0 = Low, 1 = Medium, 2 = High. More informative than conviction_level, which rounds it.', '1.14; 0.94', '0.0–2.0; observed 0.66–1.40.',
 '{"high (→2)": "Firm, unhedged commitment", "low (→0)": "Hedged or conflicted"}', NULL),
('evaluations', 'native_rating', NULL, 'categorical', 'code', 'The agent''s own headline rating, extracted from its report by regex (no Jev).', 'Pass; Neutral; Strong Short; Moderate', 'The enum its prompt asks for, e.g. Strong Buy…Strong Sell, Attractive/Neutral/Unattractive, Low/Moderate/High/Critical, Initiate…Pass. NULL if not stated.', NULL, NULL),
('evaluations', 'native_stance', NULL, 'categorical', 'code', 'native_rating translated onto the five-way stance through the rubric''s native_to_stance map.', 'HOLD (from Pass or Neutral); STRONG SELL (from Strong Short)', 'Same five stances, or NULL when the rating is not a buy/sell call (risk ratings, "Reject Short Thesis").', (SELECT j FROM stances), NULL),
('evaluations', 'stance_agreement', NULL, 'boolean', 'code', 'Whether the agent''s own rating (native_stance) and Jev''s reading of the whole report (stance) land on the same stance.', 'true; false (NOW strategist: wrote PASS, report reads as SELL)', 'true | false | NULL',
 '{"true": "Headline consistent with the analysis", "false": "Headline and analysis point different ways; inspect the report", "NULL": "No mappable native rating, or no Jev stance"}', NULL),
('evaluations', 'domain_profile', NULL, 'json', 'code', 'The agent''s role-specific domain scores: {metric_id: {label, level 1–5 or null, confidence, status}}. Describes the company as the agent assessed it; never mixed into the quality score.', '{"solvency": {"label": "Solvency / leverage", "level": 3.87, "status": "ok", "confidence": 0.88}, "liquidity": {"level": null, "status": "not_addressed"}}', 'Levels 1–5; status ok | not_addressed | error.', NULL, NULL),
('evaluations', 'domain_mean', NULL, 'continuous', 'code', 'Mean domain level over the metrics the report addressed.', '3.93; 1.77', '1.0–5.0; observed 1.76–4.66.',
 '{"high (→5)": "Agent assessed the company very favourably on its dimensions", "low (→1)": "Very unfavourably (for risk roles: high risk)"}', NULL),
('evaluations', 'domain_addressed', NULL, 'count', 'code', 'How many domain metrics the report actually discussed and were scored.', '7', '0 … domain_total.', NULL, NULL),
('evaluations', 'domain_total', NULL, 'count', 'code', 'How many domain metrics the role''s rubric defines.', '8', '5–8 depending on the role.', NULL, NULL),
('evaluations', 'alignment_composite', NULL, 'continuous', 'code', 'Weighted mean of the normalised prompt-alignment metrics: how well the report followed its prompt. Vetoes are listed separately, never averaged in.', '0.92; 0.68', '0–1; observed 0.68–0.94; NULL when under 70% of the weight was usable.',
 '{"high (→1)": "Followed the prompt closely: sections, evidence, balance, consistency", "low (→0)": "Missing sections, unsupported claims or inconsistencies"}', NULL),
('evaluations', 'alignment_dimensions', NULL, 'json', 'code', 'alignment_composite broken down by dimension: {dimension: {score 0–1, n metrics}}.', '{"balance": {"n": 4, "score": 0.954}, "evidence": {"n": 5, "score": 0.8146}}', 'Scores 0–1.', NULL, NULL),
('evaluations', 'alignment_coverage', NULL, 'continuous', 'code', 'Share of alignment weight that produced a usable answer (not errored or low-evidence).', '1.0', '0–1; below 0.7 the composite is NULL.', '{"1": "Every weighted question answered", "<0.7": "Too much missing for a fair composite"}', NULL),
('evaluations', 'veto_triggered', NULL, 'boolean', 'code', 'Whether any veto metric failed.', 'false', 'true | false', '{"true": "A hard failure occurred; see vetoes", "false": "No veto failed"}', NULL),
('evaluations', 'vetoes', NULL, 'list', 'code', 'Ids of the veto metrics that failed, e.g. injected text, unparseable headline rating, fraud override ignored.', '{}; {injected_or_offtopic_text}', 'Empty array = none.', NULL, NULL),
('evaluations', 'insufficient_evidence', NULL, 'boolean', 'code', 'Whether any alignment request''s gate question failed, so its answers were excluded as low_evidence.', 'false', 'true | false', '{"true": "Part of the rubric could not be judged from the report", "false": "All gates passed"}', NULL),
('evaluations', 'advisory', NULL, 'boolean', 'code', 'True until the rubric is calibrated against human labels.', 'true', 'true | false', '{"true": "Use for monitoring and comparison, not as ground truth", "false": "Rubric calibrated"}', NULL),
('evaluations', 'n_metrics', NULL, 'count', 'code', 'Number of metric_results rows behind this evaluation.', '35', '0 (failed agent) … ~50.', NULL, NULL),
('evaluations', 'n_errors', NULL, 'count', 'code', 'Metric rows that errored.', '0', '≥ 0; > 0 makes status partial.', NULL, NULL),
('evaluations', 'n_calls', NULL, 'count', 'code', 'Jev requests used (including cache hits).', '7', '0 (failed agent) … ~9.', NULL, NULL),
('evaluations', 'n_cached', NULL, 'count', 'code', 'Of n_calls, how many were served from the jev_calls cache at no cost.', '0; 7', '0 … n_calls.', NULL, NULL),
('evaluations', 'input_tokens', NULL, 'count', 'jev', 'Input tokens paid for (cached calls excluded).', '21650; 0', '≥ 0; 0 when every call was cached.', NULL, NULL),
('evaluations', 'output_tokens', NULL, 'count', 'jev', 'Output tokens paid for (cached calls excluded).', '640', '≥ 0.', NULL, NULL),
('evaluations', 'started_at', NULL, 'timestamp', 'code', 'When this evaluation started.', '2026-10-09 18:09:51+00', 'UTC timestamp.', NULL, NULL),
('evaluations', 'finished_at', NULL, 'timestamp', 'code', 'When this evaluation finished; the latest per run × role is what the v_ views show.', '2026-10-09 18:09:51+00', 'UTC timestamp.', NULL, NULL),
('evaluations', 'created_at', NULL, 'timestamp', 'database', 'When the row was first stored.', '2026-10-09 18:09:51+00', 'UTC timestamp.', NULL, NULL),

-- ── eval.metric_results ──────────────────────────────────────────────────────
('metric_results', 'id', 'PK', 'identifier', 'database', 'Surrogate key.', '1', 'Positive integer, generated.', NULL, NULL),
('metric_results', 'evaluation_id', 'FK → eval.evaluations.id', 'identifier', 'database', 'Evaluation this answer belongs to.', '4', 'Must exist in eval.evaluations.', NULL, NULL),
('metric_results', 'question_id', 'unique with evaluation_id, variant', 'identifier', 'code', 'Rubric id of the question, check or domain metric.', 'stance; sourcing_specificity; profitability; verdict_parseable', 'Any id defined in metrics/<role>.yaml or _shared.yaml.', NULL, NULL),
('metric_results', 'block', NULL, 'categorical', 'code', 'Which part of the evaluation the row belongs to.', 'alignment', 'conviction | domain | alignment',
 '{"conviction": "Shared stance, stance gate and conviction level", "domain": "Role-specific 5-level assessment of the company", "alignment": "Prompt-adherence questions and code checks; feeds alignment_composite"}', NULL),
('metric_results', 'variant', 'unique with evaluation_id, question_id', 'categorical', 'code', 'Whether this is the normal answer or an order-check re-ask.', 'primary', 'primary | reversed',
 '{"primary": "Normal question", "reversed": "Same choice question with options in reverse order (--order-check), to measure Jev''s lean toward the first option"}', NULL),
('metric_results', 'kind', NULL, 'categorical', 'code', 'Type of question.', 'noul', 'noul | score | choice | deterministic',
 '{"noul": "Jev yes/no probability", "score": "Jev ordinal level", "choice": "Jev picks one option", "deterministic": "Checked in code (sections, tables, counts, arithmetic)"}', NULL),
('metric_results', 'rubric_request', NULL, 'categorical', 'code', 'Rubric request (group of questions sent in one Jev call) that produced the row.', 'stance; shared_quality; valuation_discipline; domain:fin_quality+moat', 'Request id from the rubric; NULL for code checks.', NULL, NULL),
('metric_results', 'dimension', NULL, 'categorical', 'code', 'What aspect of quality the metric measures; used for alignment_dimensions.', 'evidence', 'compliance | evidence | quantification | balance | consistency | honesty | integrity | fidelity | actionability | extraction | evidence_gate | stance | conviction | domain',
 '{"compliance": "Followed the required output structure", "evidence": "Claims backed by data or sources", "quantification": "Uses concrete numbers", "balance": "Weighs the other side", "consistency": "Conclusions follow from the body", "honesty": "Flags data gaps", "integrity": "No injected or off-topic text", "fidelity": "Pass 2: faithful to what specialists said", "actionability": "Concrete, usable rules or plans", "extraction": "Reads a stated value (weight 0)", "evidence_gate": "Whether a section is judgeable at all (weight 0)", "stance": "Shared stance question", "conviction": "Shared conviction question", "domain": "Domain metric"}', NULL),
('metric_results', 'label', NULL, 'free_text', 'code', 'Human-readable name of a domain metric.', 'Sector growth; Solvency / leverage', 'Set for block = domain; NULL otherwise.', NULL, NULL),
('metric_results', 'weight', NULL, 'continuous', 'code', 'Weight in alignment_composite.', '2; 0', '≥ 0.', '{"0": "Recorded but not scored (gates, extractions, informational vetoes)", "higher": "Counts more in the composite"}', NULL),
('metric_results', 'veto', NULL, 'boolean', 'code', 'Whether failing this metric is a hard failure listed in evaluations.vetoes.', 'false', 'true | false', '{"true": "Failure is a veto", "false": "Ordinary weighted metric"}', NULL),
('metric_results', 'noul_p', NULL, 'continuous', 'jev', 'For kind = noul: Jev''s probability that the answer is yes.', '0.98; 0.06', '0–1; NULL for other kinds.',
 '{"≈1": "Confident yes", "≈0.5": "Uncertain", "≈0": "Confident no (whether yes is good depends on the question; see normalized)"}', NULL),
('metric_results', 'choice', NULL, 'categorical', 'jev', 'For kind = choice: the option Jev picked.', 'Strong; HOLD; not_stated', 'One of the question''s options; NULL for other kinds.', NULL, NULL),
('metric_results', 'score', NULL, 'continuous', 'jev', 'For kind = score: Jev''s probability-weighted level, 0-based (level 0 = first, worst criterion).', '1.13 of 0–3; 4 of 0–4 (domain)', '0 … n_levels − 1; may fall between levels.',
 '{"high": "Closer to the best-described level", "low": "Closer to the worst-described level"}', NULL),
('metric_results', 'n_levels', NULL, 'count', 'code', 'Number of levels in the score question.', '4; 5', '2–10; 5 for domain metrics; NULL for non-score kinds.', NULL, NULL),
('metric_results', 'probabilities', NULL, 'json', 'jev', 'Jev''s probability per option (choice) or per level (score).', '{"0": 0.0, "1": 0.87, "2": 0.12, "3": 0.01}', 'Values 0–1 summing to 1; NULL for noul and code checks.', NULL, NULL),
('metric_results', 'confidence', NULL, 'continuous', 'jev', 'How concentrated Jev''s probabilities are (choice and score).', '0.86', '0–1.', '{"high": "One option or level dominates", "low": "Spread across several"}', NULL),
('metric_results', 'deterministic_value', NULL, 'continuous', 'code', 'For code checks: the measured value, as a fraction met.', '1; 0.83', '0–1.', '{"1": "Fully met (e.g. all sections present)", "0": "Not met"}', NULL),
('metric_results', 'detail', NULL, 'free_text', 'code', 'Explanation of a code check result, or why a metric was not addressed or skipped.', '7 rows; missing [''risks'']; no evidence terms in fin_quality', 'Free text; NULL for most Jev answers.', NULL, NULL),
('metric_results', 'code_extract', NULL, 'categorical', 'code', 'The value code extracted from the report for comparison with Jev''s choice (cross-check), or the agent''s self-reported conviction.', 'Strong; Medium', 'NULL when the metric has no cross-check.', NULL, NULL),
('metric_results', 'agreement', NULL, 'boolean', 'code', 'Whether Jev''s choice matches code_extract.', 'true', 'true | false | NULL', '{"true": "Jev and the regex read the same value", "false": "They differ; check the report", "NULL": "No cross-check"}', NULL),
('metric_results', 'normalized', NULL, 'continuous', 'code', 'The answer on a common 0–1 "goodness" scale: noul → p(yes) or 1 − p(yes) depending on which answer is good; score → score / (n_levels − 1); code check → deterministic_value; domain → score / 4.', '0.98; 0.3767', '0–1; NULL for extraction choices.', '{"1": "Best possible", "0": "Worst possible"}', NULL),
('metric_results', 'passed', NULL, 'boolean', 'code', 'Whether the metric met its threshold (noul: good-side probability ≥ threshold, usually 0.5; score: rounded level ≥ min_level; code: check satisfied).', 'true; false', 'true | false | NULL',
 '{"true": "Met", "false": "Not met", "NULL": "Not a pass/fail metric (domain scores, extraction choices) or check skipped"}', NULL),
('metric_results', 'status', NULL, 'categorical', 'code', 'Whether the row holds a usable answer.', 'ok', 'ok | error | skipped | low_evidence | not_addressed',
 '{"ok": "Usable answer", "error": "Jev call or answer failed; see error", "skipped": "Could not be evaluated (section missing, or a check like price-target arithmetic had nothing parseable)", "low_evidence": "Its request''s gate failed; answer kept but excluded from scores", "not_addressed": "Domain metric the report never discussed; not sent to Jev"}', NULL),
('metric_results', 'error', NULL, 'free_text', 'code', 'Why the answer is missing or invalid.', 'http 529: overloaded; choice ''X'' not among options', 'NULL unless status = error.', NULL, NULL),
('metric_results', 'jev_call_id', 'FK → eval.jev_calls.id', 'identifier', 'database', 'Jev call that produced the answer.', '1', 'NULL for code checks and not_addressed metrics.', NULL, NULL),
('metric_results', 'created_at', NULL, 'timestamp', 'database', 'When the row was stored (rows are replaced on re-evaluation).', '2026-10-09 18:09:51+00', 'UTC timestamp.', NULL, NULL),

-- ── eval.human_labels ────────────────────────────────────────────────────────
('human_labels', 'id', 'PK', 'identifier', 'database', 'Surrogate key.', '1', 'Positive integer, generated.', NULL, NULL),
('human_labels', 'run_id', 'FK → eval.runs.run_id', 'identifier', 'human', 'Run the label is about.', 'AVGO_20261003T135110', 'Must exist in eval.runs.', NULL, NULL),
('human_labels', 'role', NULL, 'categorical', 'human', 'Agent whose report was labelled.', 'head_of_research', 'One of the 13 agent roles.', (SELECT j FROM roles), NULL),
('human_labels', 'question_id', NULL, 'identifier', 'human', 'Rubric question the label answers; matches metric_results.question_id.', 'stance; team_claims_accurate', 'Any rubric question id.', NULL, NULL),
('human_labels', 'labeler', NULL, 'identifier', 'human', 'Who made the label.', 'quantdoge', 'Free identifier; unique per run × role × question.', NULL, NULL),
('human_labels', 'label', NULL, 'json', 'human', 'The human''s answer, in the same terms as the question.', '{"value": "SELL"}; {"passed": false}; {"level": 3}', 'JSON object.', NULL, NULL),
('human_labels', 'notes', NULL, 'free_text', 'human', 'Optional reasoning.', 'Memo claims 13 reports; only 11 specialists exist', 'Free text; nullable.', NULL, NULL),
('human_labels', 'created_at', NULL, 'timestamp', 'database', 'When the label was stored.', '2026-10-10 09:00:00+00', 'UTC timestamp.', NULL, NULL),

-- ── view-only columns ────────────────────────────────────────────────────────
('v_domain_scores', 'metric', NULL, 'identifier', 'view', 'Domain metric id (metric_results.question_id renamed).', 'profitability; governance; sector_growth', 'Ids from conviction.domain_metrics in each role''s rubric.', NULL, 'eval.metric_results.question_id'),
('v_domain_scores', 'level', NULL, 'ordinal', 'view', 'Domain score shown on a 1–5 scale (score + 1).', '4.87; 3.0', '1.0–5.0; may fall between levels; NULL when not addressed.',
 '{"5": "Very favourable to a long investor (risk roles: very low risk)", "4": "Favourable", "3": "Average / neutral", "2": "Unfavourable", "1": "Very unfavourable (risk roles: very high risk)"}', NULL),
('v_metric_trend', 'week', NULL, 'date', 'view', 'Week of the runs (Monday, from run_date).', '2026-09-28', 'Monday dates.', NULL, NULL),
('v_metric_trend', 'n', NULL, 'count', 'view', 'Number of primary answers in the week.', '1', '≥ 1.', NULL, NULL),
('v_metric_trend', 'pass_rate', NULL, 'continuous', 'view', 'Share of usable answers that passed.', '0.75', '0–1; NULL for metrics without pass/fail (domain).', '{"high": "Question usually met by this agent", "low": "Question usually failed: a weak agent behaviour or a harsh question"}', NULL),
('v_metric_trend', 'avg_normalized', NULL, 'continuous', 'view', 'Mean normalised 0–1 value in the week.', '0.385', '0–1.', '{"high": "Good on average", "low": "Poor on average"}', NULL),
('v_pipeline_reliability', 'n', NULL, 'count', 'view', 'Runs in which the agent appears.', '3', '≥ 1.', NULL, NULL),
('v_pipeline_reliability', 'n_ok', NULL, 'count', 'view', 'Runs where it produced a usable report.', '2', '0 … n.', NULL, NULL),
('v_pipeline_reliability', 'n_failed', NULL, 'count', 'view', 'Runs where it errored or timed out.', '1', '0 … n.', NULL, NULL),
('v_pipeline_reliability', 'n_degenerate', NULL, 'count', 'view', 'Runs where it returned a stub.', '0', '0 … n.', NULL, NULL),
('v_pipeline_reliability', 'n_missing', NULL, 'count', 'view', 'Runs where it was absent.', '0', '0 … n.', NULL, NULL),
('v_pipeline_reliability', 'ok_rate', NULL, 'continuous', 'view', 'n_ok / n.', '0.67', '0–1.', '{"1": "Always produced a usable report", "low": "Agent frequently fails or stubs; a research-pipeline problem, not a quality one"}', NULL),
('v_stance_pivot', 'avg_stance_expected', NULL, 'continuous', 'view', 'Mean stance_expected across the 11 specialists (strategist and memo excluded). Note: currently includes low-evidence stances.', '-0.62', '−2 … +2.', '{"+2": "Specialists unanimously strongly bullish", "0": "Neutral or split", "-2": "Unanimously strongly bearish"}', NULL)
),
live AS (
    SELECT cl.relname AS table_name, a.attname AS column_name, a.attnum AS ordinal_position,
           format_type(a.atttypid, a.atttypmod) AS data_type, NOT a.attnotnull AS is_nullable
    FROM pg_attribute a
    JOIN pg_class cl    ON cl.oid = a.attrelid
    JOIN pg_namespace n ON n.oid = cl.relnamespace
    WHERE n.nspname = 'eval' AND cl.relkind IN ('r', 'v') AND a.attnum > 0 AND NOT a.attisdropped
)
INSERT INTO datadict.columns (schema_name, table_name, column_name, ordinal_position, data_type, is_nullable,
                              key_role, value_kind, source, definition, example_values, value_range, value_meanings, derived_from)
SELECT 'eval', d.table_name, d.column_name, l.ordinal_position, l.data_type, l.is_nullable,
       d.key_role, d.value_kind, d.source, d.definition, d.example_values, d.value_range, d.value_meanings, d.derived_from
FROM doc d
JOIN live l USING (table_name, column_name)
ON CONFLICT (schema_name, table_name, column_name) DO UPDATE SET
    ordinal_position = EXCLUDED.ordinal_position, data_type = EXCLUDED.data_type, is_nullable = EXCLUDED.is_nullable,
    key_role = EXCLUDED.key_role, value_kind = EXCLUDED.value_kind, source = EXCLUDED.source,
    definition = EXCLUDED.definition, example_values = EXCLUDED.example_values, value_range = EXCLUDED.value_range,
    value_meanings = EXCLUDED.value_meanings, derived_from = EXCLUDED.derived_from;

-- -----------------------------------------------------------------------------
-- 3. The 13 per-agent stance columns of v_stance_pivot
-- -----------------------------------------------------------------------------
INSERT INTO datadict.columns (schema_name, table_name, column_name, ordinal_position, data_type, is_nullable,
                              key_role, value_kind, source, definition, example_values, value_range, value_meanings, derived_from)
SELECT 'eval', 'v_stance_pivot', cl_col.attname, cl_col.attnum, format_type(cl_col.atttypid, cl_col.atttypmod), true,
       NULL, 'categorical', 'view',
       'Stance (eval.evaluations.stance) of the ' || cl_col.attname || ' agent in this run, from its latest evaluation.',
       'SELL; HOLD; NULL (agent failed)', 'STRONG SELL | SELL | HOLD | BUY | STRONG BUY | NULL (agent failed or not evaluated)',
       '{"STRONG SELL": "(-2) strongly negative", "SELL": "(-1) negative", "HOLD": "(0) neutral", "BUY": "(+1) positive", "STRONG BUY": "(+2) strongly positive"}'::jsonb,
       'eval.evaluations.stance'
FROM pg_attribute cl_col
WHERE cl_col.attrelid = 'eval.v_stance_pivot'::regclass AND cl_col.attnum > 0 AND NOT cl_col.attisdropped
  AND cl_col.attname IN ('sector_researcher', 'geo_legal_researcher', 'macro_researcher', 'value_researcher',
                         'growth_researcher', 'fin_risk_analyst', 'nonfin_risk_analyst', 'quant_analyst',
                         'short_analyst', 'esg_analyst', 'alt_data_analyst', 'portfolio_strategist', 'head_of_research')
ON CONFLICT (schema_name, table_name, column_name) DO UPDATE SET
    ordinal_position = EXCLUDED.ordinal_position, data_type = EXCLUDED.data_type,
    definition = EXCLUDED.definition, example_values = EXCLUDED.example_values, value_range = EXCLUDED.value_range,
    value_meanings = EXCLUDED.value_meanings, derived_from = EXCLUDED.derived_from;

-- -----------------------------------------------------------------------------
-- 4. Pass-through view columns: derived_from the first listed source table that
--    has a column of the same name. They inherit documentation in the view.
-- -----------------------------------------------------------------------------
WITH src(view_name, prio, source_table) AS (VALUES
    ('v_latest_evaluations',   1, 'runs'),           ('v_latest_evaluations',   2, 'evaluations'),
    ('v_stance_matrix',        1, 'runs'),           ('v_stance_matrix',        2, 'evaluations'),
    ('v_role_scorecard',       1, 'runs'),           ('v_role_scorecard',       2, 'evaluations'),
    ('v_stance_pivot',         1, 'runs'),
    ('v_domain_scores',        1, 'runs'),           ('v_domain_scores',        2, 'metric_results'),
    ('v_domain_scores',        3, 'evaluations'),
    ('v_metric_trend',         1, 'metric_results'), ('v_metric_trend',         2, 'evaluations'),
    ('v_jev_human_agreement',  1, 'human_labels'),   ('v_jev_human_agreement',  2, 'runs'),
    ('v_jev_human_agreement',  3, 'metric_results'),
    ('v_pipeline_reliability', 1, 'agent_outputs')
),
live AS (
    SELECT cl.relname AS table_name, a.attname AS column_name, a.attnum AS ordinal_position,
           format_type(a.atttypid, a.atttypmod) AS data_type
    FROM pg_attribute a
    JOIN pg_class cl    ON cl.oid = a.attrelid
    JOIN pg_namespace n ON n.oid = cl.relnamespace
    WHERE n.nspname = 'eval' AND cl.relkind = 'v' AND a.attnum > 0 AND NOT a.attisdropped
),
pick AS (
    SELECT DISTINCT ON (l.table_name, l.column_name)
           l.table_name, l.column_name, l.ordinal_position, l.data_type,
           s.value_kind, s.source, 'eval.' || s.table_name || '.' || s.column_name AS derived_from
    FROM live l
    JOIN src ON src.view_name = l.table_name
    JOIN datadict.columns s ON s.schema_name = 'eval' AND s.table_name = src.source_table AND s.column_name = l.column_name
    WHERE NOT EXISTS (SELECT 1 FROM datadict.columns x
                      WHERE x.schema_name = 'eval' AND x.table_name = l.table_name AND x.column_name = l.column_name
                        AND x.definition IS NOT NULL)
    ORDER BY l.table_name, l.column_name, src.prio
)
INSERT INTO datadict.columns (schema_name, table_name, column_name, ordinal_position, data_type, is_nullable,
                              key_role, value_kind, source, derived_from)
SELECT 'eval', table_name, column_name, ordinal_position, data_type, true, NULL, value_kind, source, derived_from
FROM pick
ON CONFLICT (schema_name, table_name, column_name) DO UPDATE SET
    ordinal_position = EXCLUDED.ordinal_position, data_type = EXCLUDED.data_type,
    value_kind = EXCLUDED.value_kind, source = EXCLUDED.source, derived_from = EXCLUDED.derived_from;
