-- =============================================================================
-- hparams views: reading the hyperparameter snapshots.
--
-- All views are security_invoker, so they run with the caller's privileges and
-- RLS. Each has an is_current column: true for the snapshot
-- hparams.v_config_current picks.
--
-- "Current" is the most recently observed config, by last_seen_at, never by
-- created_at. The git backfill inserts old configs after newer ones, so insert
-- order says nothing about which config is in force.
-- Idempotent: safe to re-run.
-- =============================================================================

-- 1. The config in force now.
CREATE OR REPLACE VIEW hparams.v_config_current
WITH (security_invoker = true) AS
SELECT c.config_sha, c.provenance, c.effective_at, c.last_seen_at, c.source_git_sha
FROM hparams.configs AS c
WHERE c.provenance <> 'inferred'
ORDER BY c.last_seen_at DESC, c.created_at DESC, c.config_sha
LIMIT 1;

COMMENT ON VIEW hparams.v_config_current IS
    'The configuration in force now: the non-inferred snapshot observed most recently (last_seen_at, not insert time). One row, or none before the first ingest.';

-- 2. Every snapshot in order, with its predecessor.
CREATE OR REPLACE VIEW hparams.v_config_history
WITH (security_invoker = true) AS
SELECT
    c.config_sha,
    COALESCE(c.config_sha = (SELECT config_sha FROM hparams.v_config_current), false)  AS is_current,
    c.provenance,
    c.effective_at,
    c.last_seen_at,
    c.source_git_sha,
    c.source_git_dirty,
    c.gaps,
    lag(c.config_sha) OVER (ORDER BY c.effective_at, c.config_sha)                       AS previous_config_sha,
    (SELECT count(*) FROM hparams.run_configs AS rc WHERE rc.config_sha = c.config_sha)::integer AS n_runs
FROM hparams.configs AS c;

COMMENT ON VIEW hparams.v_config_history IS
    'Every snapshot in effective order, with the one before it (pass both to hparams.config_diff) and how many runs used it.';

-- 3. Per-role configuration.
CREATE OR REPLACE VIEW hparams.v_config_agents
WITH (security_invoker = true) AS
SELECT
    g.config_sha,
    COALESCE(g.config_sha = (SELECT config_sha FROM hparams.v_config_current), false)  AS is_current,
    c.provenance,
    c.effective_at,
    g.role,
    g.stage,
    g.agent_kind,
    g.model_slug,
    g.model_spec,
    g.max_tokens,
    g.recursion_limit,
    g.advertised_recursion_limit,
    g.advertised_tool_rounds,
    g.advertised_write_by,
    g.advertised_timeout_s,
    g.task,
    g.prompt_source,
    g.system_prompt_sha,
    g.budget_sha,
    g.composed_prompt_sha,
    tc.chars                                                                           AS composed_chars,
    g.tool_count,
    g.agent_sha,
    (SELECT min(c2.effective_at)
       FROM hparams.config_agents AS g2
       JOIN hparams.configs       AS c2 ON c2.config_sha = g2.config_sha
      WHERE g2.role = g.role AND g2.agent_sha = g.agent_sha)                            AS agent_unchanged_since
FROM hparams.config_agents AS g
JOIN hparams.configs       AS c  ON c.config_sha = g.config_sha
LEFT JOIN hparams.texts    AS tc ON tc.text_sha  = g.composed_prompt_sha;

COMMENT ON VIEW hparams.v_config_agents IS
    'Per-role configuration of every snapshot (filter is_current for today), with the composed prompt length and when this exact role config first appeared.';

-- 4. Tools of every snapshot.
CREATE OR REPLACE VIEW hparams.v_config_tools
WITH (security_invoker = true) AS
SELECT
    t.config_sha,
    COALESCE(t.config_sha = (SELECT config_sha FROM hparams.v_config_current), false)  AS is_current,
    t.tool_name,
    d.module,
    t.tags,
    d.description,
    d.input_schema,
    d.impl_sha256,
    t.tool_sha
FROM hparams.config_tools AS t
JOIN hparams.tool_defs    AS d ON d.tool_sha = t.tool_sha;

COMMENT ON VIEW hparams.v_config_tools IS
    'Every tool of every snapshot with its module, role tags, description, input schema and implementation hash.';

-- 5. Access, one row per grant.
CREATE OR REPLACE VIEW hparams.v_config_access_long
WITH (security_invoker = true) AS
SELECT
    a.config_sha,
    COALESCE(a.config_sha = (SELECT config_sha FROM hparams.v_config_current), false)  AS is_current,
    a.role,
    a.tool_name,
    d.module,
    a.via
FROM hparams.config_role_tools AS a
JOIN hparams.config_tools      AS t ON t.config_sha = a.config_sha AND t.tool_name = a.tool_name
JOIN hparams.tool_defs         AS d ON d.tool_sha   = t.tool_sha;

COMMENT ON VIEW hparams.v_config_access_long IS
    'Role x tool access, one row per grant, with the tag that granted it.';

-- 6. Access as a tool x role matrix (same role order as eval.v_stance_pivot).
CREATE OR REPLACE VIEW hparams.v_config_access_wide
WITH (security_invoker = true) AS
SELECT
    t.config_sha,
    COALESCE(t.config_sha = (SELECT config_sha FROM hparams.v_config_current), false)  AS is_current,
    t.tool_name,
    d.module,
    t.tags,
    bool_or(a.role = 'sector_researcher')     IS TRUE AS sector_researcher,
    bool_or(a.role = 'geo_legal_researcher')  IS TRUE AS geo_legal_researcher,
    bool_or(a.role = 'macro_researcher')      IS TRUE AS macro_researcher,
    bool_or(a.role = 'value_researcher')      IS TRUE AS value_researcher,
    bool_or(a.role = 'growth_researcher')     IS TRUE AS growth_researcher,
    bool_or(a.role = 'fin_risk_analyst')      IS TRUE AS fin_risk_analyst,
    bool_or(a.role = 'nonfin_risk_analyst')   IS TRUE AS nonfin_risk_analyst,
    bool_or(a.role = 'quant_analyst')         IS TRUE AS quant_analyst,
    bool_or(a.role = 'short_analyst')         IS TRUE AS short_analyst,
    bool_or(a.role = 'esg_analyst')           IS TRUE AS esg_analyst,
    bool_or(a.role = 'alt_data_analyst')      IS TRUE AS alt_data_analyst,
    bool_or(a.role = 'portfolio_strategist')  IS TRUE AS portfolio_strategist,
    bool_or(a.role = 'head_of_research')      IS TRUE AS head_of_research,
    count(a.role)::integer                            AS n_roles
FROM hparams.config_tools           AS t
JOIN hparams.tool_defs              AS d ON d.tool_sha = t.tool_sha
LEFT JOIN hparams.config_role_tools AS a ON a.config_sha = t.config_sha AND a.tool_name = t.tool_name
GROUP BY t.config_sha, t.tool_name, d.module, t.tags;

COMMENT ON VIEW hparams.v_config_access_wide IS
    'Tool x role access matrix per snapshot: one row per tool, one boolean column per role (same order as eval.v_stance_pivot).';

-- 7. Tools per role.
CREATE OR REPLACE VIEW hparams.v_config_access_counts
WITH (security_invoker = true) AS
SELECT
    a.config_sha,
    COALESCE(a.config_sha = (SELECT config_sha FROM hparams.v_config_current), false)  AS is_current,
    a.role,
    count(*)::integer                                  AS n_tools,
    count(*) FILTER (WHERE a.via = 'shared')::integer  AS n_shared,
    count(*) FILTER (WHERE a.via = 'role')::integer    AS n_role_tagged
FROM hparams.config_role_tools AS a
GROUP BY a.config_sha, a.role;

COMMENT ON VIEW hparams.v_config_access_counts IS
    'Tools per role per snapshot; compare with EXPECTED_COUNTS in tests/test_tool_access.py (head_of_research 6 ... quant_analyst 25).';

-- 8. Runs and the config each one used.
CREATE OR REPLACE VIEW hparams.v_run_configs
WITH (security_invoker = true) AS
SELECT
    r.run_id,
    r.symbol,
    r.run_date,
    r.skip_reason,
    rc.config_sha,
    rc.link_basis,
    c.provenance,
    c.effective_at                                                   AS config_effective_at,
    rc.research_git_sha,
    rt.default_max_concurrency,
    rc.max_concurrency,
    rc.max_concurrency IS DISTINCT FROM rt.default_max_concurrency   AS concurrency_overridden,
    rt.agent_timeout_s,
    rc.run_timeout_s,
    rc.agents_requested,
    rc.extra_instructions,
    rc.overrides,
    rc.notes
FROM eval.runs                    AS r
LEFT JOIN hparams.run_configs     AS rc ON rc.run_id     = r.run_id
LEFT JOIN hparams.configs         AS c  ON c.config_sha  = rc.config_sha
LEFT JOIN hparams.config_runtime  AS rt ON rt.config_sha = rc.config_sha;

COMMENT ON VIEW hparams.v_run_configs IS
    'Every run in eval.runs with the config it was tied to and its per-run settings. Unlinked runs (config_sha NULL) are kept: legacy runs never link.';

-- 9. Run x role: the agent config in force, next to what the output recorded.
CREATE OR REPLACE VIEW hparams.v_run_agent_config
WITH (security_invoker = true) AS
SELECT
    rc.run_id,
    r.symbol,
    r.run_date,
    g.role,
    rc.config_sha,
    rc.link_basis,
    g.agent_sha,
    g.model_slug,
    g.max_tokens,
    g.recursion_limit,
    g.system_prompt_sha,
    g.composed_prompt_sha,
    o.status,
    o.agent_model                                                       AS output_agent_model,
    o.agent_model_inferred,
    (o.agent_model IS NOT NULL AND g.model_slug IS NOT NULL
     AND o.agent_model <> g.model_slug)                                 AS model_mismatch
FROM hparams.run_configs        AS rc
JOIN eval.runs                  AS r ON r.run_id     = rc.run_id
JOIN hparams.config_agents      AS g ON g.config_sha = rc.config_sha
LEFT JOIN eval.agent_outputs    AS o ON o.run_id = rc.run_id AND o.role = g.role;

COMMENT ON VIEW hparams.v_run_agent_config IS
    'Run x role: the agent config in force plus the model recorded with the output, flagging disagreement. Join eval.evaluations on (run_id, role) to compare scores across configs.';

-- 10. Self-consistency guard. Must return 0 rows.
CREATE OR REPLACE VIEW hparams.v_config_integrity
WITH (security_invoker = true) AS
SELECT 'composed prompt is not system prompt + budget block' AS issue, g.config_sha, g.role, NULL::text AS tool_name
FROM hparams.config_agents AS g
JOIN hparams.texts AS cp ON cp.text_sha = g.composed_prompt_sha
JOIN hparams.texts AS sp ON sp.text_sha = g.system_prompt_sha
LEFT JOIN hparams.texts AS bd ON bd.text_sha = g.budget_sha
WHERE g.prompt_source = 'file' AND cp.body <> sp.body || COALESCE(bd.body, '')
UNION ALL
SELECT 'access row missing for a tag that grants it', g.config_sha, g.role, t.tool_name
FROM hparams.config_agents AS g
JOIN hparams.config_tools  AS t ON t.config_sha = g.config_sha
WHERE (g.role = ANY (t.tags) OR 'shared' = ANY (t.tags))
  AND NOT EXISTS (SELECT 1 FROM hparams.config_role_tools AS a
                  WHERE a.config_sha = g.config_sha AND a.role = g.role AND a.tool_name = t.tool_name)
UNION ALL
SELECT 'access row not justified by the tool''s tags', a.config_sha, a.role, a.tool_name
FROM hparams.config_role_tools AS a
JOIN hparams.config_tools      AS t ON t.config_sha = a.config_sha AND t.tool_name = a.tool_name
WHERE NOT (a.role = ANY (t.tags) OR 'shared' = ANY (t.tags))
UNION ALL
SELECT 'tool_count differs from access rows', g.config_sha, g.role, NULL
FROM hparams.config_agents AS g
WHERE g.tool_count IS DISTINCT FROM
      (SELECT count(*) FROM hparams.config_role_tools AS a WHERE a.config_sha = g.config_sha AND a.role = g.role)
UNION ALL
SELECT 'config has no runtime row', c.config_sha, NULL, NULL
FROM hparams.configs AS c
WHERE NOT EXISTS (SELECT 1 FROM hparams.config_runtime AS rt WHERE rt.config_sha = c.config_sha)
UNION ALL
SELECT 'config agents differ from content', c.config_sha, NULL, NULL
FROM hparams.configs AS c
WHERE (SELECT count(*) FROM hparams.config_agents AS g WHERE g.config_sha = c.config_sha)
      <> (SELECT count(*) FROM jsonb_object_keys(c.content -> 'agents'))
UNION ALL
SELECT 'config tools differ from content', c.config_sha, NULL, NULL
FROM hparams.configs AS c
WHERE (SELECT count(*) FROM hparams.config_tools AS t WHERE t.config_sha = c.config_sha)
      <> (SELECT count(*) FROM jsonb_object_keys(c.content -> 'tools'));

COMMENT ON VIEW hparams.v_config_integrity IS
    'Self-consistency of stored snapshots: composed prompt = system prompt + budget block, access rows = the tag rule, child rows = content. Must return 0 rows.';

-- -----------------------------------------------------------------------------
-- Field-level diff of two configs. Rows exist only where something differs.
-- -----------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION hparams.config_diff(cfg_a text, cfg_b text)
RETURNS TABLE (facet text, item text, field text, a_value jsonb, b_value jsonb)
LANGUAGE sql STABLE
SET search_path = pg_catalog
AS $$
WITH items AS (
    SELECT r.config_sha, 'runtime'::text AS facet, ''::text AS item, to_jsonb(r) - 'config_sha' AS doc
      FROM hparams.config_runtime AS r WHERE r.config_sha IN (cfg_a, cfg_b)
    UNION ALL
    SELECT g.config_sha, 'agent', g.role, to_jsonb(g) - 'config_sha' - 'role' - 'agent_sha'
      FROM hparams.config_agents AS g WHERE g.config_sha IN (cfg_a, cfg_b)
    UNION ALL
    SELECT t.config_sha, 'tool', t.tool_name,
           jsonb_build_object('tags', to_jsonb(t.tags), 'module', d.module, 'description', d.description,
                              'input_schema', d.input_schema, 'impl_sha256', d.impl_sha256)
      FROM hparams.config_tools AS t JOIN hparams.tool_defs AS d ON d.tool_sha = t.tool_sha
     WHERE t.config_sha IN (cfg_a, cfg_b)
    UNION ALL
    SELECT a.config_sha, 'access', a.role || '/' || a.tool_name, jsonb_build_object('via', a.via)
      FROM hparams.config_role_tools AS a WHERE a.config_sha IN (cfg_a, cfg_b)
    UNION ALL
    SELECT c.config_sha, 'module', m.key, jsonb_build_object('sha256', m.value)
      FROM hparams.configs AS c CROSS JOIN LATERAL jsonb_each(c.content -> 'module_sha256') AS m
     WHERE c.config_sha IN (cfg_a, cfg_b)
), x AS (SELECT * FROM items WHERE config_sha = cfg_a),
   y AS (SELECT * FROM items WHERE config_sha = cfg_b)
SELECT COALESCE(x.facet, y.facet), COALESCE(x.item, y.item), k.field, x.doc -> k.field, y.doc -> k.field
FROM x FULL JOIN y ON x.facet = y.facet AND x.item = y.item
CROSS JOIN LATERAL jsonb_object_keys(COALESCE(x.doc, '{}'::jsonb) || COALESCE(y.doc, '{}'::jsonb)) AS k(field)
WHERE (x.doc -> k.field) IS DISTINCT FROM (y.doc -> k.field)
ORDER BY 1, 2, 3
$$;

COMMENT ON FUNCTION hparams.config_diff(text, text) IS
    'Field-level diff of two config_shas across the runtime, agent, tool, access and module facets. A prompt edit shows as a changed *_prompt_sha; join hparams.texts for the bodies.';

-- -----------------------------------------------------------------------------
-- Keep the new views and function private too.
-- -----------------------------------------------------------------------------
DO $$
DECLARE
    r text;
BEGIN
    REVOKE ALL ON ALL TABLES    IN SCHEMA hparams FROM PUBLIC;
    REVOKE ALL ON ALL FUNCTIONS IN SCHEMA hparams FROM PUBLIC;
    FOREACH r IN ARRAY ARRAY['anon', 'authenticated'] LOOP
        IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = r) THEN
            EXECUTE format('REVOKE ALL ON ALL TABLES    IN SCHEMA hparams FROM %I', r);
            EXECUTE format('REVOKE ALL ON ALL FUNCTIONS IN SCHEMA hparams FROM %I', r);
        END IF;
    END LOOP;
END
$$;
