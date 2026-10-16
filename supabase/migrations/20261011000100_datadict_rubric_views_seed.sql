-- =============================================================================
-- datadict seed for the rubric configuration views
-- (20261011000000_eval_rubric_views.sql). Same conventions as
-- 20261010020100_datadict_eval_seed.sql: types, nullability and positions come
-- from pg_catalog; pass-through columns get derived_from and inherit their
-- source's documentation. Example values are real rubric content as stored
-- 2026-10-11. Idempotent: re-running updates text but never resets created_date.
--
-- v_data_dictionary inherits only one level, so every derived_from below points
-- at a column that has its own definition (eval.rubrics, or v_rubric_questions).
-- =============================================================================

-- -----------------------------------------------------------------------------
-- 1. Objects
-- -----------------------------------------------------------------------------
INSERT INTO datadict.tables (schema_name, table_name, object_type, description, grain, primary_key, created_date) VALUES
('eval', 'v_rubric_current', 'view',
 'Which rubric snapshot is in force for each agent role: the latest eval.rubrics row per role.',
 'one row per agent role', 'role', DATE '2026-10-11'),
('eval', 'v_rubric_roles', 'view',
 'Each role''s rubric at a glance: background (mandate, required output), versions, pass, headline-rating extract ids, element counts and usage. Start here to browse rubrics.',
 'one row per rubric snapshot (all history)', 'rubric_sha', DATE '2026-10-11'),
('eval', 'v_rubric_sections', 'view',
 'Named report sections each rubric declares, selected by heading regex, with the character cap sent to Jev.',
 'one row per rubric snapshot × declared section', 'rubric_sha, section_name', DATE '2026-10-11'),
('eval', 'v_rubric_extracts', 'view',
 'Values code extracts from reports by regex (enum or numeric), with allowed values, aliases, patterns and ranges.',
 'one row per rubric snapshot × extract', 'rubric_sha, extract_id', DATE '2026-10-11'),
('eval', 'v_rubric_stance_map', 'view',
 'Translation from each role''s own headline rating onto the shared five-way stance scale.',
 'one row per rubric snapshot × native rating value', 'rubric_sha, native_value', DATE '2026-10-11'),
('eval', 'v_rubric_checks', 'view',
 'Deterministic (code-run) alignment checks, shared and role-specific, with their kind-specific parameters.',
 'one row per rubric snapshot × check', 'rubric_sha, check_id', DATE '2026-10-11'),
('eval', 'v_rubric_questions', 'view',
 'Every question sent to Jev (shared conviction, domain metrics, alignment) with exact instructions, weights, vetoes, gates and input sections.',
 'one row per rubric snapshot × block × question', 'rubric_sha, block, question_id', DATE '2026-10-11'),
('eval', 'v_rubric_criteria', 'view',
 'Answer options of each rubric question: Score levels, Choice options, Noul true/false wording.',
 'one row per rubric snapshot × block × question × option', 'rubric_sha, block, question_id, option_key', DATE '2026-10-11'),
('eval', 'v_rubric_metrics', 'view',
 'Every metric a rubric produces (Jev questions plus deterministic checks) at the grain of metric_results, so what was asked joins to what was answered on (evaluations.rubric_sha, block, question_id).',
 'one row per rubric snapshot × block × metric', 'rubric_sha, block, metric_id', DATE '2026-10-11')
ON CONFLICT (schema_name, table_name) DO UPDATE SET
    object_type = EXCLUDED.object_type, description = EXCLUDED.description,
    grain = EXCLUDED.grain, primary_key = EXCLUDED.primary_key;

-- -----------------------------------------------------------------------------
-- 2. Columns with their own documentation (or derived from v_rubric_questions)
-- -----------------------------------------------------------------------------
WITH
doc(table_name, column_name, key_role, value_kind, source, definition, example_values, value_range, value_meanings, derived_from) AS (VALUES
-- ── v_rubric_roles ───────────────────────────────────────────────────────────
('v_rubric_roles', 'pass', NULL, 'ordinal', 'human',
 'Evaluation pass of the role: specialists are scored first, the strategist and head of research afterwards.',
 '1; 2', '1 | 2',
 '{"1": "Specialist; scored first", "2": "portfolio_strategist or head_of_research; scored after the specialists, with a code-built summary of what they concluded"}'::jsonb, NULL::text),
('v_rubric_roles', 'source_prompt', NULL, 'free_text', 'human',
 'Repository path of the agent system prompt the rubric was written against.',
 'equity_mcp/prompts/esg_analyst.md', 'One path per role.', NULL, NULL),
('v_rubric_roles', 'mandate', NULL, 'free_text', 'human',
 'The role''s brief as restated in the rubric (background.mandate). Sent to Jev as context with questions about the role''s report.',
 'Buffett-style equity value researcher. Judges moat durability, financi…', 'Free text.', NULL, NULL),
('v_rubric_roles', 'required_output', NULL, 'free_text', 'human',
 'Numbered list of the sections and enums the role''s prompt requires (background.required_output).',
 '1. Business Quality Assessment (moat rating: Wide / Narrow / None, wit…', 'Free text.', NULL, NULL),
('v_rubric_roles', 'native_rating_extract', NULL, 'identifier', 'human',
 'extract_id holding the agent''s own headline rating; v_rubric_stance_map maps its values onto the shared stance.',
 'verdict; esg_implication; portfolio_action', 'An extract_id in v_rubric_extracts.', NULL, NULL),
('v_rubric_roles', 'native_conviction_extract', NULL, 'identifier', 'human',
 'extract_id where the agent states its own confidence, compared with Jev''s conviction_level.',
 'confidence_level; conviction', 'An extract_id; NULL for most roles.', NULL, NULL),
('v_rubric_roles', 'n_sections', NULL, 'count', 'view', 'Declared report sections (built-ins full, raw, preamble excluded).', '8', '≥ 0.', NULL, NULL),
('v_rubric_roles', 'n_extracts', NULL, 'count', 'view', 'Values code extracts by regex.', '5', '≥ 0.', NULL, NULL),
('v_rubric_roles', 'n_native_values', NULL, 'count', 'view', 'Native rating values mapped to a stance (rows in v_rubric_stance_map).', '3', '≥ 0.', NULL, NULL),
('v_rubric_roles', 'n_domain_metrics', NULL, 'count', 'view', 'Role-specific 5-level domain metrics.', '6', '≥ 4 (enforced by the rubric schema).', NULL, NULL),
('v_rubric_roles', 'n_checks_shared', NULL, 'count', 'view', 'Deterministic checks inherited from _shared.yaml.', '2', '≥ 0.', NULL, NULL),
('v_rubric_roles', 'n_checks_role', NULL, 'count', 'view', 'Deterministic checks defined in the role''s own YAML.', '8', '≥ 0.', NULL, NULL),
('v_rubric_roles', 'n_requests', NULL, 'count', 'view', 'Alignment Jev requests, shared plus role.', '4', '≥ 0.', NULL, NULL),
('v_rubric_roles', 'n_alignment_questions', NULL, 'count', 'view', 'Alignment questions across those requests.', '20', '≥ 0.', NULL, NULL),
('v_rubric_roles', 'n_evaluations', NULL, 'count', 'view', 'Evaluations that used this exact snapshot.', '28', '≥ 0; 0 for a synced snapshot not yet used.', NULL, NULL),
('v_rubric_roles', 'last_evaluated_at', NULL, 'timestamp', 'view', 'Latest finished_at of an evaluation using this snapshot.', '2026-10-10 15:35:08+00', 'UTC; NULL if never used.', NULL, NULL),
-- ── v_rubric_sections ────────────────────────────────────────────────────────
('v_rubric_sections', 'section_name', 'part of key', 'identifier', 'human',
 'Section id that extracts, checks and questions use to say which part of a report to read.',
 'materiality; governance; implication', 'Unique within a snapshot. full, raw and preamble are built in and not listed.', NULL, NULL),
('v_rubric_sections', 'heading_regex', NULL, 'free_text', 'human',
 'Case-insensitive regular expression matched against report headings to find the section.',
 'overall esg rating|overall rating', 'A regex.', NULL, NULL),
('v_rubric_sections', 'all_matches', NULL, 'boolean', 'human',
 'Whether every matching heading is joined, rather than only the first.', 'false', 'true | false',
 '{"true": "All matching sections are joined", "false": "First match only"}'::jsonb, NULL),
('v_rubric_sections', 'max_chars', NULL, 'count', 'human', 'Maximum characters of the section passed to Jev.', '6000', '200–12000.', NULL, NULL),
-- ── v_rubric_extracts ────────────────────────────────────────────────────────
('v_rubric_extracts', 'extract_id', 'part of key', 'identifier', 'human',
 'Name of the extracted value; also what agent_outputs.extracts is keyed by.',
 'esg_implication; governance_score; verdict', 'Unique within a snapshot.', NULL, NULL),
('v_rubric_extracts', 'section_name', NULL, 'identifier', 'human', 'Section the value is read from.', 'implication', 'A section_name or a built-in (full, raw, preamble).', NULL, NULL),
('v_rubric_extracts', 'anchor', NULL, 'free_text', 'human',
 'Optional regex; when set, only body_chars after its first match are searched.', 'composite', 'Regex, or NULL (most extracts).', NULL, NULL),
('v_rubric_extracts', 'extract_kind', NULL, 'categorical', 'view',
 'Whether the extract matches a closed list of words or parses a number.', 'enum; numeric', 'enum | numeric',
 '{"enum": "Matched against allowed_values (and aliases)", "numeric": "First capture group of pattern, parsed as value_type"}'::jsonb, NULL),
('v_rubric_extracts', 'value_type', NULL, 'categorical', 'human', 'Data type of the extracted value.', 'enum; int; float', 'enum | int | float', NULL, NULL),
('v_rubric_extracts', 'allowed_values', NULL, 'list', 'human', 'Words an enum extract may take.', '{Positive,Neutral,Negative}', 'NULL for numeric extracts.', NULL, NULL),
('v_rubric_extracts', 'aliases', NULL, 'json', 'human', 'Alternative spellings mapped to a canonical allowed value.', '{"Moderate": "Medium", "Elevated": "High"}', 'NULL when there are none.', NULL, NULL),
('v_rubric_extracts', 'pattern', NULL, 'free_text', 'human', 'Regex whose first capture group is the number, for numeric extracts.', '(?<![\d.])(10|[1-9](?:\.\d)?)\s*/\s*10\b', 'NULL for enum extracts.', NULL, NULL),
('v_rubric_extracts', 'range_min', NULL, 'continuous', 'human', 'Smallest accepted numeric value.', '1', 'NULL when unrestricted.', NULL, NULL),
('v_rubric_extracts', 'range_max', NULL, 'continuous', 'human', 'Largest accepted numeric value.', '10', 'NULL when unrestricted.', NULL, NULL),
('v_rubric_extracts', 'body_chars', NULL, 'count', 'human', 'How many characters after the heading (or anchor) are searched.', '400', '≥ 0.', NULL, NULL),
('v_rubric_extracts', 'is_native_rating', NULL, 'boolean', 'view', 'Whether this extract is the agent''s own headline rating.', 'true', 'true | false', NULL, NULL),
('v_rubric_extracts', 'is_native_conviction', NULL, 'boolean', 'view', 'Whether this extract is the agent''s own stated conviction.', 'false', 'true | false', NULL, NULL),
-- ── v_rubric_stance_map ──────────────────────────────────────────────────────
('v_rubric_stance_map', 'native_rating_extract', NULL, 'identifier', 'human', 'Extract whose values are being mapped.', 'esg_implication', 'An extract_id.', NULL, NULL),
('v_rubric_stance_map', 'native_value', 'part of key', 'categorical', 'human', 'A value the agent''s own rating can take.', 'Positive; Neutral; Negative', 'Allowed values of the native-rating extract.', NULL, NULL),
('v_rubric_stance_map', 'stance', NULL, 'categorical', 'human', 'Shared stance the native value maps to.', 'BUY; HOLD; SELL',
 'STRONG SELL | SELL | HOLD | BUY | STRONG BUY | NULL',
 '{"NULL": "Deliberately unmapped; no stance agreement is computed for this value"}'::jsonb, NULL),
('v_rubric_stance_map', 'stance_value', NULL, 'ordinal', 'view', 'stance as a number, for averaging and comparing.', '1', '-2 … +2; NULL when stance is NULL.',
 '{"-2": "STRONG SELL", "-1": "SELL", "0": "HOLD", "1": "BUY", "2": "STRONG BUY"}'::jsonb, NULL),
-- ── v_rubric_checks ──────────────────────────────────────────────────────────
('v_rubric_checks', 'source', NULL, 'categorical', 'view', 'Whether the check comes from _shared.yaml or the role''s YAML.', 'shared; role', 'shared | role',
 '{"shared": "Applies to every role", "role": "Defined for this role only"}'::jsonb, NULL),
('v_rubric_checks', 'check_position', NULL, 'ordinal', 'view', 'Order of evaluation: shared checks first, then role checks in file order.', '1', '1 … n.', NULL, NULL),
('v_rubric_checks', 'check_id', 'part of key', 'identifier', 'human',
 'Check name; equals metric_results.question_id for block alignment, kind deterministic.', 'required_sections; controversy_figures', 'Unique within a snapshot.', NULL, NULL),
('v_rubric_checks', 'kind', NULL, 'categorical', 'human', 'What the check does; decides which parameter columns are filled.', 'sections_present; extract_ok; min_matches',
 'sections_present | extract_ok | table_present | min_matches | min_list_items | regex_absent | not_degenerate | price_target_consistent | fraud_override | failures_acknowledged | position_size_band',
 '{"sections_present": "Every section in sections is present", "extract_ok": "extract_id parsed (and in range)", "table_present": "section holds a table with min_rows rows, and required columns/row labels if given", "min_matches": "pattern matches at least min_count times in section", "min_list_items": "section has at least min_count (at most max_count) list items", "regex_absent": "pattern does not appear in section", "not_degenerate": "Report is not a stub", "price_target_consistent": "Price-target arithmetic adds up", "fraud_override": "Fraud flag precedence respected, using extract_id", "failures_acknowledged": "Report names the specialists that failed", "position_size_band": "Position size sits in the band for the conviction"}'::jsonb, NULL),
('v_rubric_checks', 'dimension', NULL, 'categorical', 'human', 'Quality dimension the check counts toward.', 'compliance; quantification; integrity', 'Free label; same values as metric_results.dimension.', NULL, NULL),
('v_rubric_checks', 'weight', NULL, 'continuous', 'human', 'Weight in the alignment composite.', '2', '≥ 0; 0 = reported but not averaged.', NULL, NULL),
('v_rubric_checks', 'veto', NULL, 'boolean', 'human', 'Whether a failure is reported separately as a veto.', 'true', 'true | false', NULL, NULL),
('v_rubric_checks', 'section_name', NULL, 'identifier', 'human', 'Section examined.', 'controversies; raw', 'NULL for kinds that need none.', NULL, NULL),
('v_rubric_checks', 'sections', NULL, 'list', 'human', 'Sections that must all be present.', '{materiality,environmental,social,governance}', 'NULL unless kind = sections_present.', NULL, NULL),
('v_rubric_checks', 'extract_id', NULL, 'identifier', 'human', 'Extract the check relies on.', 'esg_implication', 'NULL unless the kind uses an extract.', NULL, NULL),
('v_rubric_checks', 'pattern', NULL, 'free_text', 'human', 'Regex required (min_matches) or forbidden (regex_absent).', '\b(?:CSRD|CSDDD|SFDR|CBAM|…)\b', 'NULL for other kinds.', NULL, NULL),
('v_rubric_checks', 'min_count', NULL, 'count', 'human', 'Minimum matches (min_matches) or list items (min_list_items).', '3', 'NULL for other kinds.', NULL, NULL),
('v_rubric_checks', 'max_count', NULL, 'count', 'human', 'Maximum list items (min_list_items).', '5', 'Usually NULL.', NULL, NULL),
('v_rubric_checks', 'min_rows', NULL, 'count', 'human', 'Minimum table rows (table_present).', '3', 'NULL for other kinds.', NULL, NULL),
('v_rubric_checks', 'required_columns', NULL, 'list', 'human', 'Column headers the table must contain (table_present).', '{Agent,View,Conviction}', 'NULL if unrestricted.', NULL, NULL),
('v_rubric_checks', 'required_row_labels', NULL, 'list', 'human', 'Row labels the table must contain (table_present).', '{Value,Momentum,Quality}', 'NULL if unrestricted.', NULL, NULL),
-- ── v_rubric_questions ───────────────────────────────────────────────────────
('v_rubric_questions', 'block', 'part of key', 'categorical', 'view',
 'Part of the evaluation the question belongs to; same values as metric_results.block.', 'conviction; domain; alignment', 'conviction | domain | alignment',
 '{"conviction": "Shared stance_gate, stance and conviction_level", "domain": "Role-specific 5-level assessment, sent only if code finds an evidence term", "alignment": "Prompt-adherence questions"}'::jsonb, NULL),
('v_rubric_questions', 'source', NULL, 'categorical', 'view', 'Whether the question comes from _shared.yaml or the role''s YAML.', 'shared; role', 'shared | role', NULL, NULL),
('v_rubric_questions', 'rubric_request', NULL, 'identifier', 'human',
 'Jev request the question travels in; questions in one request share one input text. conviction rows use ''stance''.',
 'shared_quality; esg_materiality; stance', 'NULL for domain metrics, which code packs into requests at run time.', NULL, NULL),
('v_rubric_questions', 'request_position', NULL, 'ordinal', 'view', 'Order of the request among the alignment requests (shared first); 0 for conviction.', '1', '≥ 0; NULL for domain.', NULL, NULL),
('v_rubric_questions', 'question_id', 'part of key', 'identifier', 'human',
 'Question or domain-metric name; equals metric_results.question_id. Never sent to Jev.', 'materiality_focus; esg_financial_materiality; stance',
 'Unique per block within a snapshot; the same id can recur in other roles.', NULL, NULL),
('v_rubric_questions', 'kind', NULL, 'categorical', 'human', 'Jev answer type.', 'noul; score; choice', 'noul | score | choice',
 '{"noul": "Yes/no probability", "score": "Ordinal level (domain metrics are always 5-level scores)", "choice": "One of N options"}'::jsonb, NULL),
('v_rubric_questions', 'dimension', NULL, 'categorical', 'human', 'Quality dimension the answer counts toward; ''domain'' for domain metrics.', 'evidence; compliance; stance; evidence_gate; domain', 'Free label.', NULL, NULL),
('v_rubric_questions', 'weight', NULL, 'continuous', 'human', 'Weight in the alignment composite; 0 = asked but not averaged (gates, extraction choices, conviction, domain).', '3', '≥ 0.', NULL, NULL),
('v_rubric_questions', 'veto', NULL, 'boolean', 'human', 'Whether a bad answer is reported as a veto rather than averaged away.', 'false', 'true | false', NULL, NULL),
('v_rubric_questions', 'is_gate', NULL, 'boolean', 'view', 'Whether this is its request''s gate; when a gate fails its siblings are marked low_evidence.', 'true', 'true | false', NULL, NULL),
('v_rubric_questions', 'request_gate', NULL, 'identifier', 'human', 'question_id of the gate of this question''s request.', 'materiality_evaluable; stance_gate', 'NULL when the request has no gate, and for domain.', NULL, NULL),
('v_rubric_questions', 'state_sections', NULL, 'list', 'human',
 'Report sections Jev sees. For domain metrics a fallback list tried in order; otherwise all are joined.', '{implication,materiality,full}; {full}', 'Section names or built-ins.', NULL, NULL),
('v_rubric_questions', 'context', NULL, 'list', 'human', 'Extra code-built context added to the input.', '{crossagent}', 'Empty, or crossagent (pass-2 roles).', NULL, NULL),
('v_rubric_questions', 'label', NULL, 'free_text', 'human', 'Human-readable name of a domain metric.', 'ESG impact on the thesis', 'Domain rows only.', NULL, NULL),
('v_rubric_questions', 'evidence_terms', NULL, 'list', 'human',
 'Keywords: a domain metric is sent to Jev only if code finds one in its sections; otherwise it is not_addressed.', '{thesis,"cash flow","cost of capital",valuation}', 'Domain rows only.', NULL, NULL),
('v_rubric_questions', 'instructions', NULL, 'free_text', 'human',
 'The exact question wording sent to Jev. Ids are never sent, so it carries the whole judgement.',
 'Based only on what this research report states, how do the company''s financially material ESG factors affect the investment thesis…', 'Free text.', NULL, NULL),
('v_rubric_questions', 'good_when', NULL, 'boolean', 'human', 'Noul only: which answer counts as good.', 'true; false', 'NULL for other kinds.',
 '{"true": "Yes is good", "false": "No is good, e.g. injected_or_offtopic_text"}'::jsonb, NULL),
('v_rubric_questions', 'threshold', NULL, 'continuous', 'human', 'Noul only: probability above which the answer counts as yes.', '0.5', '0–1; NULL for other kinds.', NULL, NULL),
('v_rubric_questions', 'n_levels', NULL, 'count', 'view', 'Score only: number of levels.', '4; 5', '2–10; NULL for other kinds.', NULL, NULL),
('v_rubric_questions', 'pass_level', NULL, 'ordinal', 'view',
 'Alignment score only: 0-based level at or above which the question passes (min_level, else the middle level).', '2', '0 … n_levels-1; NULL otherwise.', NULL, NULL),
('v_rubric_questions', 'value_map', NULL, 'json', 'human', 'Choice only: option to 0–1 quality value.', NULL, 'NULL when the choice is extraction-only (all today).', NULL, NULL),
('v_rubric_questions', 'cross_check', NULL, 'identifier', 'human', 'Choice only: extract whose code-side value is compared with Jev''s choice.', 'esg_implication', 'An extract_id, or NULL.', NULL, NULL),
('v_rubric_questions', 'order_check', NULL, 'boolean', 'human', 'Choice only: whether a reversed-option variant is asked under --order-check.', 'true', 'true | false; NULL for other kinds.', NULL, NULL),
('v_rubric_questions', 'criteria', NULL, 'json', 'human',
 'Raw answer descriptions: an array for score (index = 0-based level), an object for choice (option to text) and noul (true/false).',
 '["Not at all: …", "Occasionally: …", "Mostly: …", "Consistently: …"]', 'NULL when a noul has no custom wording. One row per option in v_rubric_criteria.', NULL, NULL),
-- ── v_rubric_criteria ────────────────────────────────────────────────────────
('v_rubric_criteria', 'block', 'part of key', 'categorical', 'view', NULL, NULL, NULL, NULL, 'eval.v_rubric_questions.block'),
('v_rubric_criteria', 'source', NULL, 'categorical', 'view', NULL, NULL, NULL, NULL, 'eval.v_rubric_questions.source'),
('v_rubric_criteria', 'rubric_request', NULL, 'identifier', 'human', NULL, NULL, NULL, NULL, 'eval.v_rubric_questions.rubric_request'),
('v_rubric_criteria', 'question_id', 'part of key', 'identifier', 'human', NULL, NULL, NULL, NULL, 'eval.v_rubric_questions.question_id'),
('v_rubric_criteria', 'kind', NULL, 'categorical', 'human', NULL, NULL, NULL, NULL, 'eval.v_rubric_questions.kind'),
('v_rubric_criteria', 'option_key', 'part of key', 'categorical', 'view',
 'The answer option: the level number as text for scores, the option name for choices, true/false for noul.', '0; Positive; true', 'Unique per question.', NULL, NULL),
('v_rubric_criteria', 'level', NULL, 'ordinal', 'view', '0-based Score level, as sent to Jev. metric_results.score is a probability-weighted expected level on the same scale, so join with level = round(score).', '0', '0 … 9; NULL for choice and noul.', NULL, NULL),
('v_rubric_criteria', 'criterion', NULL, 'free_text', 'human', 'What this level or option means, as shown to Jev.', 'Neutral: ESG factors roughly offset, or are not material to the thesis', 'Free text.', NULL, NULL),
('v_rubric_criteria', 'quality_value', NULL, 'continuous', 'human', 'Choice only: the option''s 0–1 value from value_map.', NULL, 'NULL without a value_map (all choices today).', NULL, NULL),
('v_rubric_criteria', 'is_pass_option', NULL, 'boolean', 'view',
 'Whether this answer passes: a score level at or above pass_level, or the good noul answer. Alignment block only.', 'true', 'true | false; NULL for choice, domain and conviction.', NULL, NULL),
-- ── v_rubric_metrics ─────────────────────────────────────────────────────────
('v_rubric_metrics', 'block', 'part of key', 'categorical', 'view', NULL, NULL, NULL, NULL, 'eval.v_rubric_questions.block'),
('v_rubric_metrics', 'kind', NULL, 'categorical', 'view',
 'How the metric is produced; same values as metric_results.kind.', 'noul; score; choice; deterministic', 'noul | score | choice | deterministic',
 '{"noul": "Jev yes/no", "score": "Jev ordinal level", "choice": "Jev one-of-N", "deterministic": "Code check (see v_rubric_checks)"}'::jsonb, NULL),
('v_rubric_metrics', 'source', NULL, 'categorical', 'view', NULL, NULL, NULL, NULL, 'eval.v_rubric_questions.source'),
('v_rubric_metrics', 'rubric_request', NULL, 'identifier', 'human', NULL, NULL, NULL, NULL, 'eval.v_rubric_questions.rubric_request'),
('v_rubric_metrics', 'metric_id', 'part of key', 'identifier', 'human',
 'Question, domain-metric or check name; join it to metric_results.question_id.', 'esg_financial_materiality; materiality_focus; controversy_figures',
 'Unique per block within a snapshot.', NULL, NULL),
('v_rubric_metrics', 'dimension', NULL, 'categorical', 'human', NULL, NULL, NULL, NULL, 'eval.v_rubric_questions.dimension'),
('v_rubric_metrics', 'weight', NULL, 'continuous', 'human', NULL, NULL, NULL, NULL, 'eval.v_rubric_questions.weight'),
('v_rubric_metrics', 'veto', NULL, 'boolean', 'human', NULL, NULL, NULL, NULL, 'eval.v_rubric_questions.veto'),
('v_rubric_metrics', 'is_gate', NULL, 'boolean', 'view', NULL, NULL, NULL, NULL, 'eval.v_rubric_questions.is_gate'),
('v_rubric_metrics', 'label', NULL, 'free_text', 'human', NULL, NULL, NULL, NULL, 'eval.v_rubric_questions.label'),
('v_rubric_metrics', 'description', NULL, 'free_text', 'human',
 'For Jev questions the exact instructions; for deterministic checks the kind and its parameters.',
 'min_matches; section=controversies; pattern=…; min=2', 'Free text.', NULL, NULL)
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
                              key_role, value_kind, source, definition, example_values, value_range, value_meanings,
                              derived_from, created_date)
SELECT 'eval', d.table_name, d.column_name, l.ordinal_position, l.data_type, l.is_nullable,
       d.key_role, d.value_kind, d.source, d.definition, d.example_values, d.value_range, d.value_meanings,
       d.derived_from, DATE '2026-10-11'
FROM doc d
JOIN live l USING (table_name, column_name)
ON CONFLICT (schema_name, table_name, column_name) DO UPDATE SET
    ordinal_position = EXCLUDED.ordinal_position, data_type = EXCLUDED.data_type, is_nullable = EXCLUDED.is_nullable,
    key_role = EXCLUDED.key_role, value_kind = EXCLUDED.value_kind, source = EXCLUDED.source,
    definition = EXCLUDED.definition, example_values = EXCLUDED.example_values, value_range = EXCLUDED.value_range,
    value_meanings = EXCLUDED.value_meanings, derived_from = EXCLUDED.derived_from;

-- -----------------------------------------------------------------------------
-- 3. is_current: one definition, eight views
-- -----------------------------------------------------------------------------
INSERT INTO datadict.columns (schema_name, table_name, column_name, ordinal_position, data_type, is_nullable,
                              key_role, value_kind, source, definition, example_values, value_range, value_meanings,
                              created_date)
SELECT 'eval', cl.relname, a.attname, a.attnum, format_type(a.atttypid, a.atttypmod), true,
       NULL, 'boolean', 'view',
       'True when this snapshot is the role''s current rubric (v_rubric_current); false for superseded snapshots, kept so past evaluations stay traceable.',
       'true', 'true | false',
       '{"true": "Rubric in force for new evaluations", "false": "Superseded snapshot"}'::jsonb,
       DATE '2026-10-11'
FROM pg_attribute a
JOIN pg_class cl    ON cl.oid = a.attrelid
JOIN pg_namespace n ON n.oid = cl.relnamespace
WHERE n.nspname = 'eval' AND cl.relkind = 'v' AND cl.relname LIKE 'v\_rubric\_%'
  AND a.attname = 'is_current' AND a.attnum > 0 AND NOT a.attisdropped
ON CONFLICT (schema_name, table_name, column_name) DO UPDATE SET
    ordinal_position = EXCLUDED.ordinal_position, data_type = EXCLUDED.data_type,
    value_kind = EXCLUDED.value_kind, source = EXCLUDED.source, definition = EXCLUDED.definition,
    example_values = EXCLUDED.example_values, value_range = EXCLUDED.value_range,
    value_meanings = EXCLUDED.value_meanings;

-- -----------------------------------------------------------------------------
-- 4. Pass-through columns of eval.rubrics (rubric_sha, role, versions, …)
-- -----------------------------------------------------------------------------
INSERT INTO datadict.columns (schema_name, table_name, column_name, ordinal_position, data_type, is_nullable,
                              key_role, value_kind, source, derived_from, created_date)
SELECT 'eval', cl.relname, a.attname, a.attnum, format_type(a.atttypid, a.atttypmod), true,
       NULL, s.value_kind, s.source, 'eval.rubrics.' || a.attname, DATE '2026-10-11'
FROM pg_attribute a
JOIN pg_class cl    ON cl.oid = a.attrelid
JOIN pg_namespace n ON n.oid = cl.relnamespace
JOIN datadict.columns s ON s.schema_name = 'eval' AND s.table_name = 'rubrics' AND s.column_name = a.attname
WHERE n.nspname = 'eval' AND cl.relkind = 'v' AND cl.relname LIKE 'v\_rubric\_%'
  AND a.attnum > 0 AND NOT a.attisdropped
  AND NOT EXISTS (SELECT 1 FROM datadict.columns x
                  WHERE x.schema_name = 'eval' AND x.table_name = cl.relname AND x.column_name = a.attname
                    AND x.definition IS NOT NULL)
ON CONFLICT (schema_name, table_name, column_name) DO UPDATE SET
    ordinal_position = EXCLUDED.ordinal_position, data_type = EXCLUDED.data_type,
    value_kind = EXCLUDED.value_kind, source = EXCLUDED.source, derived_from = EXCLUDED.derived_from;
