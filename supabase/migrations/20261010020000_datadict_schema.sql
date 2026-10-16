-- =============================================================================
-- datadict schema: a queryable data dictionary for the `eval` schema.
--
-- datadict.tables      one row per documented table/view
-- datadict.columns     one row per field: type, owner, dates, definition,
--                      examples, value range and what each value means
-- datadict.v_data_dictionary   the reading view (view columns inherit their
--                      source column's documentation through derived_from)
-- datadict.v_coverage_gaps     drift guard: must return 0 rows
--
-- Types are never typed by hand: the seed copies them from pg_catalog, and
-- v_coverage_gaps flags any column added, dropped or retyped since.
-- Idempotent: safe to re-run.
-- =============================================================================

CREATE SCHEMA IF NOT EXISTS datadict;
COMMENT ON SCHEMA datadict IS 'Data dictionary for the eval schema (Jev evaluation results).';

CREATE OR REPLACE FUNCTION datadict.touch_updated_at()
RETURNS trigger
LANGUAGE plpgsql
SET search_path = pg_catalog
AS $$
BEGIN
    NEW.updated_at := now();
    RETURN NEW;
END;
$$;

-- -----------------------------------------------------------------------------
-- datadict.tables
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS datadict.tables (
    schema_name   text NOT NULL,
    table_name    text NOT NULL,
    object_type   text NOT NULL CHECK (object_type IN ('table', 'view')),
    description   text NOT NULL,
    grain         text NOT NULL,
    primary_key   text,
    data_owner    text NOT NULL DEFAULT 'Jason Lim (quantdoge)',
    created_date  date NOT NULL DEFAULT DATE '2026-10-10',
    updated_at    timestamptz NOT NULL DEFAULT now(),
    PRIMARY KEY (schema_name, table_name)
);
COMMENT ON TABLE datadict.tables IS
    'One row per documented table or view: what it holds, its grain (what one row is), its key and owner.';

-- -----------------------------------------------------------------------------
-- datadict.columns
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS datadict.columns (
    schema_name       text NOT NULL,
    table_name        text NOT NULL,
    column_name       text NOT NULL,
    ordinal_position  integer NOT NULL,
    data_type         text NOT NULL,
    is_nullable       boolean NOT NULL,
    key_role          text,
    value_kind        text NOT NULL CHECK (value_kind IN
                          ('identifier', 'categorical', 'ordinal', 'continuous', 'boolean', 'count',
                           'timestamp', 'date', 'free_text', 'json', 'hash', 'list')),
    source            text NOT NULL CHECK (source IN ('jev', 'code', 'pipeline', 'database', 'human', 'view')),
    definition        text,
    example_values    text,
    value_range       text,
    value_meanings    jsonb,
    derived_from      text,
    data_owner        text NOT NULL DEFAULT 'Jason Lim (quantdoge)',
    created_date      date NOT NULL DEFAULT DATE '2026-10-10',
    updated_at        timestamptz NOT NULL DEFAULT now(),
    PRIMARY KEY (schema_name, table_name, column_name),
    FOREIGN KEY (schema_name, table_name) REFERENCES datadict.tables (schema_name, table_name) ON DELETE CASCADE,
    CHECK (definition IS NOT NULL OR derived_from IS NOT NULL)
);
COMMENT ON TABLE datadict.columns IS
    'One row per field. source says who produces the value: jev = a TypeSafe Jev answer, code = computed by equity_mcp/evaluation, '
    'pipeline = copied from the research output JSON, database = a default or trigger, human = typed by a person, '
    'view = computed inside a view. A view column with derived_from and no definition inherits its source column''s documentation.';

COMMENT ON COLUMN datadict.columns.value_meanings IS
    'What values mean. Categorical: {"value": "meaning"}. Ordinal: {"0 Low": "..."}. Continuous: {"high": "...", "low": "..."}.';

DROP TRIGGER IF EXISTS tables_touch_updated_at ON datadict.tables;
CREATE TRIGGER tables_touch_updated_at BEFORE UPDATE ON datadict.tables
    FOR EACH ROW EXECUTE FUNCTION datadict.touch_updated_at();
DROP TRIGGER IF EXISTS columns_touch_updated_at ON datadict.columns;
CREATE TRIGGER columns_touch_updated_at BEFORE UPDATE ON datadict.columns
    FOR EACH ROW EXECUTE FUNCTION datadict.touch_updated_at();

-- -----------------------------------------------------------------------------
-- Reading view: view columns inherit documentation from their source column.
-- -----------------------------------------------------------------------------
CREATE OR REPLACE VIEW datadict.v_data_dictionary
WITH (security_invoker = true) AS
SELECT
    c.schema_name,
    c.table_name,
    t.object_type,
    c.column_name,
    c.ordinal_position,
    c.data_type,
    c.is_nullable,
    c.key_role,
    COALESCE(c.value_kind, s.value_kind)          AS value_kind,
    CASE WHEN c.definition IS NULL THEN s.source ELSE c.source END AS source,
    COALESCE(c.definition, s.definition)          AS definition,
    COALESCE(c.example_values, s.example_values)  AS example_values,
    COALESCE(c.value_range, s.value_range)        AS value_range,
    COALESCE(c.value_meanings, s.value_meanings)  AS value_meanings,
    c.derived_from,
    c.data_owner,
    c.created_date,
    GREATEST(c.updated_at, s.updated_at)          AS updated_at
FROM datadict.columns AS c
JOIN datadict.tables  AS t USING (schema_name, table_name)
LEFT JOIN datadict.columns AS s
       ON c.derived_from = s.schema_name || '.' || s.table_name || '.' || s.column_name;

COMMENT ON VIEW datadict.v_data_dictionary IS
    'The data dictionary to read: every documented field with its type, owner, dates, definition, examples, range and value meanings. '
    'View columns show their source column''s documentation unless they override it.';

-- -----------------------------------------------------------------------------
-- Drift guard: columns that exist but are undocumented, documented columns that
-- no longer exist, and type changes. Must return 0 rows.
-- -----------------------------------------------------------------------------
CREATE OR REPLACE VIEW datadict.v_coverage_gaps
WITH (security_invoker = true) AS
WITH live AS (
    SELECT n.nspname AS schema_name, cl.relname AS table_name, a.attname AS column_name,
           format_type(a.atttypid, a.atttypmod) AS data_type
    FROM pg_attribute a
    JOIN pg_class cl     ON cl.oid = a.attrelid
    JOIN pg_namespace n  ON n.oid = cl.relnamespace
    WHERE n.nspname = 'eval' AND cl.relkind IN ('r', 'v') AND a.attnum > 0 AND NOT a.attisdropped
)
SELECT 'undocumented column' AS issue, l.schema_name, l.table_name, l.column_name, l.data_type AS live_type, NULL AS documented_type
FROM live l LEFT JOIN datadict.columns c USING (schema_name, table_name, column_name)
WHERE c.column_name IS NULL
UNION ALL
SELECT 'documented column no longer exists', c.schema_name, c.table_name, c.column_name, NULL, c.data_type
FROM datadict.columns c LEFT JOIN live l USING (schema_name, table_name, column_name)
WHERE l.column_name IS NULL AND c.schema_name = 'eval'
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
    'Drift guard for the dictionary. Must return 0 rows; after any eval migration, update datadict until it does.';

-- -----------------------------------------------------------------------------
-- Security: same model as eval. RLS on; anon/authenticated get nothing;
-- eval_writer (if it exists) may read, not write.
-- -----------------------------------------------------------------------------
ALTER TABLE datadict.tables  ENABLE ROW LEVEL SECURITY;
ALTER TABLE datadict.columns ENABLE ROW LEVEL SECURITY;

DO $$
DECLARE
    r text;
    t text;
BEGIN
    REVOKE ALL ON SCHEMA datadict FROM PUBLIC;
    REVOKE ALL ON ALL TABLES    IN SCHEMA datadict FROM PUBLIC;
    REVOKE ALL ON ALL FUNCTIONS IN SCHEMA datadict FROM PUBLIC;
    FOREACH r IN ARRAY ARRAY['anon', 'authenticated'] LOOP
        IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = r) THEN
            EXECUTE format('REVOKE ALL ON SCHEMA datadict FROM %I', r);
            EXECUTE format('REVOKE ALL ON ALL TABLES IN SCHEMA datadict FROM %I', r);
            EXECUTE format('ALTER DEFAULT PRIVILEGES IN SCHEMA datadict REVOKE ALL ON TABLES FROM %I', r);
        END IF;
    END LOOP;
    IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'eval_writer') THEN
        GRANT USAGE ON SCHEMA datadict TO eval_writer;
        GRANT SELECT ON ALL TABLES IN SCHEMA datadict TO eval_writer;
        FOREACH t IN ARRAY ARRAY['tables', 'columns'] LOOP
            EXECUTE format('DROP POLICY IF EXISTS eval_writer_read ON datadict.%I', t);
            EXECUTE format('CREATE POLICY eval_writer_read ON datadict.%I FOR SELECT TO eval_writer USING (true)', t);
        END LOOP;
    END IF;
END
$$;
