-- =============================================================================
-- datadict covers a second schema: hparams.
--
-- datadict.tables and datadict.columns were already keyed by schema_name;
-- only the drift guard was hard-wired to 'eval', which would have made every
-- hparams column invisible to it rather than covered by it.
-- Idempotent: safe to re-run.
-- =============================================================================

COMMENT ON SCHEMA datadict IS
    'Data dictionary for the eval schema (Jev evaluation results) and the hparams schema (pipeline hyperparameter snapshots).';

CREATE OR REPLACE VIEW datadict.v_coverage_gaps
WITH (security_invoker = true) AS
WITH live AS (
    SELECT n.nspname AS schema_name, cl.relname AS table_name, a.attname AS column_name,
           format_type(a.atttypid, a.atttypmod) AS data_type
    FROM pg_attribute a
    JOIN pg_class cl     ON cl.oid = a.attrelid
    JOIN pg_namespace n  ON n.oid = cl.relnamespace
    WHERE n.nspname IN ('eval', 'hparams') AND cl.relkind IN ('r', 'v') AND a.attnum > 0 AND NOT a.attisdropped
)
SELECT 'undocumented column' AS issue, l.schema_name, l.table_name, l.column_name, l.data_type AS live_type, NULL AS documented_type
FROM live l LEFT JOIN datadict.columns c USING (schema_name, table_name, column_name)
WHERE c.column_name IS NULL
UNION ALL
SELECT 'documented column no longer exists', c.schema_name, c.table_name, c.column_name, NULL, c.data_type
FROM datadict.columns c LEFT JOIN live l USING (schema_name, table_name, column_name)
WHERE l.column_name IS NULL AND c.schema_name IN ('eval', 'hparams')
UNION ALL
SELECT 'type changed', l.schema_name, l.table_name, l.column_name, l.data_type, c.data_type
FROM live l JOIN datadict.columns c USING (schema_name, table_name, column_name)
WHERE l.data_type <> c.data_type
UNION ALL
SELECT 'derived_from points at nothing', c.schema_name, c.table_name, c.column_name, NULL, c.derived_from
FROM datadict.columns c
WHERE c.derived_from IS NOT NULL
  AND NOT EXISTS (SELECT 1 FROM datadict.columns s
                  WHERE c.derived_from = s.schema_name || '.' || s.table_name || '.' || s.column_name);

COMMENT ON VIEW datadict.v_coverage_gaps IS
    'Drift guard for the dictionary, over the eval and hparams schemas. Must return 0 rows; after any eval or hparams migration, update datadict until it does.';
