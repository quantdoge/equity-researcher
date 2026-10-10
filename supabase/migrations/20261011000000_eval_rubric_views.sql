-- =============================================================================
-- Rubric configuration views: what each role's metrics/<role>.yaml (merged with
-- _shared.yaml) asks, unnested from eval.rubrics.content. No new tables.
--
--   v_rubric_current     which snapshot is in force per role
--   v_rubric_roles       background (mandate, required output), versions, counts
--   v_rubric_sections    section name -> heading regex
--   v_rubric_extracts    values code pulls out of a report by regex
--   v_rubric_stance_map  the role's own rating -> shared five-way stance
--   v_rubric_checks      deterministic alignment checks (shared + role)
--   v_rubric_questions   every question sent to Jev: conviction, domain, alignment
--   v_rubric_criteria    one row per answer option of those questions
--   v_rubric_metrics     questions + checks at the grain of eval.metric_results
--
-- Every view but v_rubric_current carries is_current, so history (every
-- rubric_sha ever stored) stays queryable. To see what a past evaluation was
-- asked, join on evaluations.rubric_sha, not is_current:
--   metric_results m JOIN evaluations e ON e.id = m.evaluation_id
--   JOIN v_rubric_metrics rm ON (rm.rubric_sha, rm.block, rm.metric_id) = (e.rubric_sha, m.block, m.question_id)
--
-- jsonb does not keep object-key order, so the YAML order of sections, extracts,
-- domain metrics, questions within a request and choice options is lost. It
-- never affected rubric_sha (hashed with sort_keys). Array order is kept:
-- checks, requests and score levels.
--
-- Rubrics reach eval.rubrics when first evaluated, or via
-- `python -m equity_mcp.evaluation.evaluate --sync-rubrics`.
-- Documented in datadict by 20261011000100_datadict_rubric_views_seed.sql.
-- Idempotent.
-- =============================================================================

CREATE OR REPLACE VIEW eval.v_rubric_current
WITH (security_invoker = true) AS
SELECT DISTINCT ON (r.role)
       r.role,
       r.rubric_sha,
       r.rubric_version,
       r.shared_version,
       r.created_at
FROM eval.rubrics AS r
ORDER BY r.role, r.created_at DESC, r.rubric_sha;

COMMENT ON VIEW eval.v_rubric_current IS
    'The rubric snapshot in force for each role: its most recently created eval.rubrics row. Rubrics land there when first evaluated or synced (evaluate --sync-rubrics).';

-- -----------------------------------------------------------------------------
CREATE OR REPLACE VIEW eval.v_rubric_roles
WITH (security_invoker = true) AS
SELECT r.rubric_sha,
       r.role,
       r.rubric_sha IN (SELECT c.rubric_sha FROM eval.v_rubric_current AS c)   AS is_current,
       r.rubric_version,
       r.shared_version,
       (r.content->'role'->>'pass')::integer                                  AS pass,
       r.calibrated,
       r.content->'role'->>'source_prompt'                                    AS source_prompt,
       r.source_prompt_sha256,
       r.content->'role'->'background'->>'mandate'                            AS mandate,
       r.content->'role'->'background'->>'required_output'                    AS required_output,
       r.content->'role'->'conviction'->>'native_rating'                      AS native_rating_extract,
       r.content->'role'->'conviction'->>'native_conviction'                  AS native_conviction_extract,
       (SELECT count(*) FROM jsonb_object_keys(r.content->'role'->'sections'))::integer                       AS n_sections,
       (SELECT count(*) FROM jsonb_object_keys(r.content->'role'->'extract'))::integer                        AS n_extracts,
       (SELECT count(*) FROM jsonb_object_keys(r.content->'role'->'conviction'->'native_to_stance'))::integer AS n_native_values,
       (SELECT count(*) FROM jsonb_object_keys(r.content->'role'->'conviction'->'domain_metrics'))::integer   AS n_domain_metrics,
       jsonb_array_length(r.content->'shared'->'alignment'->'deterministic_checks')                           AS n_checks_shared,
       jsonb_array_length(r.content->'role'->'alignment'->'deterministic_checks')                             AS n_checks_role,
       jsonb_array_length(r.content->'shared'->'alignment'->'requests')
         + jsonb_array_length(r.content->'role'->'alignment'->'requests')                                     AS n_requests,
       (SELECT count(*)
          FROM jsonb_array_elements((r.content->'shared'->'alignment'->'requests')
                                    || (r.content->'role'->'alignment'->'requests')) AS q(v),
               jsonb_object_keys(q.v->'questions'))::integer                                                  AS n_alignment_questions,
       (SELECT count(*) FROM eval.evaluations AS e WHERE e.rubric_sha = r.rubric_sha)::integer               AS n_evaluations,
       (SELECT max(e.finished_at) FROM eval.evaluations AS e WHERE e.rubric_sha = r.rubric_sha)               AS last_evaluated_at,
       r.created_at
FROM eval.rubrics AS r;

COMMENT ON VIEW eval.v_rubric_roles IS
    'One row per rubric snapshot (all history; filter is_current for today): the role''s background (mandate, required output), versions, pass, headline-rating extract ids, element counts and how often the snapshot has been used. Start here.';

-- -----------------------------------------------------------------------------
CREATE OR REPLACE VIEW eval.v_rubric_sections
WITH (security_invoker = true) AS
SELECT r.rubric_sha,
       r.role,
       r.rubric_sha IN (SELECT c.rubric_sha FROM eval.v_rubric_current AS c) AS is_current,
       s.key                                 AS section_name,
       s.value->>'heading'                   AS heading_regex,
       (s.value->>'all_matches')::boolean    AS all_matches,
       (s.value->>'max_chars')::integer      AS max_chars
FROM eval.rubrics AS r
CROSS JOIN LATERAL jsonb_each(r.content->'role'->'sections') AS s;

COMMENT ON VIEW eval.v_rubric_sections IS
    'Report sections each role''s rubric declares: the case-insensitive heading regex that selects them and the character cap sent to Jev. The built-in sections full, raw and preamble exist for every role and are not listed.';

-- -----------------------------------------------------------------------------
CREATE OR REPLACE VIEW eval.v_rubric_extracts
WITH (security_invoker = true) AS
SELECT r.rubric_sha,
       r.role,
       r.rubric_sha IN (SELECT c.rubric_sha FROM eval.v_rubric_current AS c) AS is_current,
       e.key                                                AS extract_id,
       e.value->>'section'                                  AS section_name,
       e.value->>'anchor'                                   AS anchor,
       CASE WHEN jsonb_typeof(e.value->'values') = 'array' THEN 'enum' ELSE 'numeric' END AS extract_kind,
       e.value->>'type'                                     AS value_type,
       CASE WHEN jsonb_typeof(e.value->'values') = 'array'
            THEN ARRAY(SELECT jsonb_array_elements_text(e.value->'values')) END        AS allowed_values,
       NULLIF(e.value->'aliases', '{}'::jsonb)              AS aliases,
       e.value->>'pattern'                                  AS pattern,
       (e.value->'range'->>0)::numeric                      AS range_min,
       (e.value->'range'->>1)::numeric                      AS range_max,
       (e.value->>'body_chars')::integer                    AS body_chars,
       e.key = COALESCE(r.content->'role'->'conviction'->>'native_rating', '')     AS is_native_rating,
       e.key = COALESCE(r.content->'role'->'conviction'->>'native_conviction', '') AS is_native_conviction
FROM eval.rubrics AS r
CROSS JOIN LATERAL jsonb_each(r.content->'role'->'extract') AS e;

COMMENT ON VIEW eval.v_rubric_extracts IS
    'Values code pulls out of each report by regex, never by the model: enum extracts list allowed values and aliases, numeric extracts a pattern, type and range. Flags the extracts holding the agent''s own rating and conviction.';

-- -----------------------------------------------------------------------------
CREATE OR REPLACE VIEW eval.v_rubric_stance_map
WITH (security_invoker = true) AS
SELECT r.rubric_sha,
       r.role,
       r.rubric_sha IN (SELECT c.rubric_sha FROM eval.v_rubric_current AS c) AS is_current,
       r.content->'role'->'conviction'->>'native_rating'  AS native_rating_extract,
       m.key                                               AS native_value,
       m.value #>> '{}'                                    AS stance,
       CASE m.value #>> '{}'
            WHEN 'STRONG SELL' THEN -2 WHEN 'SELL' THEN -1 WHEN 'HOLD' THEN 0
            WHEN 'BUY' THEN 1 WHEN 'STRONG BUY' THEN 2 END AS stance_value
FROM eval.rubrics AS r
CROSS JOIN LATERAL jsonb_each(r.content->'role'->'conviction'->'native_to_stance') AS m;

COMMENT ON VIEW eval.v_rubric_stance_map IS
    'How each role''s own headline rating (e.g. Positive/Neutral/Negative, Wide/Narrow moat) is translated onto the shared STRONG SELL..STRONG BUY stance. stance is NULL for values deliberately left unmapped.';

-- -----------------------------------------------------------------------------
CREATE OR REPLACE VIEW eval.v_rubric_checks
WITH (security_invoker = true) AS
SELECT r.rubric_sha,
       r.role,
       r.rubric_sha IN (SELECT c.rubric_sha FROM eval.v_rubric_current AS c) AS is_current,
       ck.source,
       row_number() OVER (PARTITION BY r.rubric_sha ORDER BY (ck.source = 'role'), ck.i)::integer AS check_position,
       ck.v->>'id'                      AS check_id,
       ck.v->>'kind'                    AS kind,
       ck.v->>'dimension'               AS dimension,
       (ck.v->>'weight')::numeric       AS weight,
       (ck.v->>'veto')::boolean         AS veto,
       ck.v->>'section'                 AS section_name,
       CASE WHEN jsonb_typeof(ck.v->'sections') = 'array'
            THEN ARRAY(SELECT jsonb_array_elements_text(ck.v->'sections')) END   AS sections,
       ck.v->>'extract'                 AS extract_id,
       ck.v->>'pattern'                 AS pattern,
       (ck.v->>'min')::integer          AS min_count,
       (ck.v->>'max')::integer          AS max_count,
       (ck.v->>'min_rows')::integer     AS min_rows,
       CASE WHEN jsonb_typeof(ck.v->'columns') = 'array'
            THEN ARRAY(SELECT jsonb_array_elements_text(ck.v->'columns')) END    AS required_columns,
       CASE WHEN jsonb_typeof(ck.v->'row_labels') = 'array'
            THEN ARRAY(SELECT jsonb_array_elements_text(ck.v->'row_labels')) END AS required_row_labels
FROM eval.rubrics AS r
CROSS JOIN LATERAL (
    SELECT 'shared'::text AS source, t.v, t.i
    FROM jsonb_array_elements(r.content->'shared'->'alignment'->'deterministic_checks') WITH ORDINALITY AS t(v, i)
    UNION ALL
    SELECT 'role', t.v, t.i
    FROM jsonb_array_elements(r.content->'role'->'alignment'->'deterministic_checks') WITH ORDINALITY AS t(v, i)
) AS ck;

COMMENT ON VIEW eval.v_rubric_checks IS
    'Deterministic (code-run) alignment checks per role: the shared ones from _shared.yaml, then the role''s own, in evaluation order. Which parameter columns are filled depends on kind; unused ones are NULL.';

-- -----------------------------------------------------------------------------
-- Every question asked of Jev: the shared conviction block (stance_gate, stance,
-- conviction_level), the role's domain metrics and the alignment questions.
-- Domain rows carry dimension 'domain', weight 0, veto false: the rubric has no
-- such fields for them, and those are the values evaluate stores in metric_results.
CREATE OR REPLACE VIEW eval.v_rubric_questions
WITH (security_invoker = true) AS
WITH raw AS (
    SELECT r.rubric_sha, r.role, 'conviction'::text AS block, 'shared'::text AS source,
           'stance'::text AS rubric_request, 0 AS request_position,
           k.key AS question_id, k.value AS q,
           ARRAY(SELECT jsonb_array_elements_text(r.content->'shared'->'conviction'->'state')) AS state_sections,
           ARRAY[]::text[] AS context, 'stance_gate'::text AS request_gate,
           NULL::text AS label, NULL::text[] AS evidence_terms
    FROM eval.rubrics AS r
    CROSS JOIN LATERAL jsonb_each((r.content->'shared'->'conviction') - 'state'::text) AS k
    UNION ALL
    SELECT r.rubric_sha, r.role, 'domain', 'role', NULL, NULL, m.key,
           m.value || '{"type": "score", "dimension": "domain", "weight": 0, "veto": false}'::jsonb,
           ARRAY(SELECT jsonb_array_elements_text(m.value->'section')),
           ARRAY[]::text[], NULL, m.value->>'label',
           ARRAY(SELECT jsonb_array_elements_text(m.value->'evidence_terms'))
    FROM eval.rubrics AS r
    CROSS JOIN LATERAL jsonb_each(r.content->'role'->'conviction'->'domain_metrics') AS m
    UNION ALL
    SELECT r.rubric_sha, r.role, 'alignment', rq.source, rq.v->>'id',
           rq.i + CASE WHEN rq.source = 'role'
                       THEN jsonb_array_length(r.content->'shared'->'alignment'->'requests') ELSE 0 END,
           qq.key, qq.value,
           ARRAY(SELECT jsonb_array_elements_text(rq.v->'state')),
           ARRAY(SELECT jsonb_array_elements_text(rq.v->'context')),
           rq.v->>'gate', NULL, NULL
    FROM eval.rubrics AS r
    CROSS JOIN LATERAL (
        SELECT 'shared'::text AS source, t.v, t.i::integer AS i
        FROM jsonb_array_elements(r.content->'shared'->'alignment'->'requests') WITH ORDINALITY AS t(v, i)
        UNION ALL
        SELECT 'role', t.v, t.i::integer
        FROM jsonb_array_elements(r.content->'role'->'alignment'->'requests') WITH ORDINALITY AS t(v, i)
    ) AS rq
    CROSS JOIN LATERAL jsonb_each(rq.v->'questions') AS qq
),
typed AS (
    SELECT raw.*,
           raw.q->>'type'                             AS kind,
           NULLIF(raw.q->'criteria', 'null'::jsonb)   AS criteria
    FROM raw
)
SELECT t.rubric_sha,
       t.role,
       t.rubric_sha IN (SELECT c.rubric_sha FROM eval.v_rubric_current AS c) AS is_current,
       t.block,
       t.source,
       t.rubric_request,
       t.request_position,
       t.question_id,
       t.kind,
       t.q->>'dimension'                AS dimension,
       (t.q->>'weight')::numeric        AS weight,
       (t.q->>'veto')::boolean          AS veto,
       (t.request_gate IS NOT NULL AND t.question_id = t.request_gate) AS is_gate,
       t.request_gate,
       t.state_sections,
       t.context,
       t.label,
       t.evidence_terms,
       t.q->>'instructions'             AS instructions,
       (t.q->>'good_when')::boolean     AS good_when,
       (t.q->>'threshold')::numeric     AS threshold,
       CASE WHEN jsonb_typeof(t.criteria) = 'array' THEN jsonb_array_length(t.criteria) END AS n_levels,
       CASE WHEN t.kind = 'score' AND t.block = 'alignment'
            THEN COALESCE((t.q->>'min_level')::integer, jsonb_array_length(t.criteria) / 2) END AS pass_level,
       NULLIF(t.q->'value_map', 'null'::jsonb) AS value_map,
       t.q->>'cross_check'              AS cross_check,
       (t.q->>'order_check')::boolean   AS order_check,
       t.criteria
FROM typed AS t;

COMMENT ON VIEW eval.v_rubric_questions IS
    'Every question the rubric sends to Jev, per role snapshot: the shared conviction questions, the role''s domain metrics and its alignment questions, with exact instructions, weights, vetoes, gates and the report sections each one sees. Answer options are in v_rubric_criteria.';

-- -----------------------------------------------------------------------------
CREATE OR REPLACE VIEW eval.v_rubric_criteria
WITH (security_invoker = true) AS
SELECT q.rubric_sha,
       q.role,
       q.is_current,
       q.block,
       q.source,
       q.rubric_request,
       q.question_id,
       q.kind,
       x.option_key,
       x.level,
       x.criterion,
       x.quality_value,
       x.is_pass_option
FROM eval.v_rubric_questions AS q
CROSS JOIN LATERAL (
    SELECT (a.i - 1)::text            AS option_key,
           (a.i - 1)::integer         AS level,
           a.v #>> '{}'               AS criterion,
           NULL::numeric              AS quality_value,
           CASE WHEN q.pass_level IS NOT NULL THEN (a.i - 1) >= q.pass_level END AS is_pass_option
    FROM jsonb_array_elements(CASE WHEN jsonb_typeof(q.criteria) = 'array' THEN q.criteria ELSE '[]'::jsonb END)
         WITH ORDINALITY AS a(v, i)
    UNION ALL
    SELECT o.key,
           NULL::integer,
           o.value #>> '{}',
           (q.value_map ->> o.key)::numeric,
           CASE WHEN q.kind = 'noul' AND q.block = 'alignment' THEN o.key = q.good_when::text END
    FROM jsonb_each(CASE WHEN jsonb_typeof(q.criteria) = 'object' THEN q.criteria ELSE '{}'::jsonb END) AS o
) AS x;

COMMENT ON VIEW eval.v_rubric_criteria IS
    'The answer options of each rubric question, one row each: Score levels (0-based, as sent to Jev), Choice options and Noul true/false descriptions. Noul questions with no custom wording have no rows.';

-- -----------------------------------------------------------------------------
-- One list of everything that produces a metric_results row: Jev questions and
-- deterministic checks. Joins 1:1 to metric_results on
-- (evaluations.rubric_sha, block, question_id = metric_id).
CREATE OR REPLACE VIEW eval.v_rubric_metrics
WITH (security_invoker = true) AS
SELECT q.rubric_sha,
       q.role,
       q.is_current,
       q.block,
       q.kind,
       q.source,
       q.rubric_request,
       q.question_id       AS metric_id,
       q.dimension,
       q.weight,
       q.veto,
       q.is_gate,
       q.label,
       q.instructions      AS description
FROM eval.v_rubric_questions AS q
UNION ALL
SELECT c.rubric_sha,
       c.role,
       c.is_current,
       'alignment',
       'deterministic',
       c.source,
       NULL,
       c.check_id,
       c.dimension,
       c.weight,
       c.veto,
       false,
       NULL,
       concat_ws('; ', c.kind,
                 'section=' || c.section_name,
                 'sections=' || array_to_string(c.sections, ','),
                 'extract=' || c.extract_id,
                 'pattern=' || c.pattern,
                 'min=' || c.min_count,
                 'max=' || c.max_count,
                 'min_rows=' || c.min_rows,
                 'columns=' || array_to_string(c.required_columns, ','),
                 'row_labels=' || array_to_string(c.required_row_labels, ','))
FROM eval.v_rubric_checks AS c;

COMMENT ON VIEW eval.v_rubric_metrics IS
    'Every metric a rubric produces, at the grain of eval.metric_results: Jev questions (conviction, domain, alignment) plus deterministic checks (block alignment, kind deterministic). description is the Jev instruction, or the check''s kind and parameters. Join to metric_results via evaluations.rubric_sha, block and question_id = metric_id.';

-- -----------------------------------------------------------------------------
-- Grants: eval stays closed to the API roles. eval_writer's SELECT came from a
-- one-off GRANT ... ON ALL TABLES, which does not cover views created later.
-- -----------------------------------------------------------------------------
DO $$
DECLARE
    v text;
    r text;
BEGIN
    FOREACH v IN ARRAY ARRAY['v_rubric_current', 'v_rubric_roles', 'v_rubric_sections', 'v_rubric_extracts',
                             'v_rubric_stance_map', 'v_rubric_checks', 'v_rubric_questions', 'v_rubric_criteria',
                             'v_rubric_metrics']
    LOOP
        EXECUTE format('REVOKE ALL ON eval.%I FROM PUBLIC', v);
        FOREACH r IN ARRAY ARRAY['anon', 'authenticated'] LOOP
            IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = r) THEN
                EXECUTE format('REVOKE ALL ON eval.%I FROM %I', v, r);
            END IF;
        END LOOP;
        IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'eval_writer') THEN
            EXECUTE format('GRANT SELECT ON eval.%I TO eval_writer', v);
        END IF;
    END LOOP;
END
$$;
