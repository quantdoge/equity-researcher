-- =============================================================================
-- eval_writer: least-privilege login role for the Python evaluation writer.
--
-- RUN ONCE BY HAND (NOT a migration), after 20261010000000_eval_schema.sql, as
-- a privileged user (postgres). Never commit a real password:
--
--   psql "$ADMIN_DATABASE_URL" -v eval_writer_password='<choose-a-strong-password>' \
--        -f supabase/sql/eval_writer_role.sql
--
-- Connecting through the Supabase pooler (Supavisor): the username is NOT plain
-- `eval_writer`. Supavisor routes by tenant, so connect as
--     eval_writer.<project_ref>
-- (e.g. eval_writer.abcdefghijklmnopqrst), with the same password. Direct
-- connections use plain `eval_writer`. With the session pooler use
-- prepare_threshold=None in psycopg 3.
--
-- RLS is enabled on every eval table, so eval_writer needs explicit policies;
-- the role is created NOBYPASSRLS on purpose.
-- Re-running is safe: the role is created once (the password is applied only on
-- creation; use ALTER ROLE to rotate it); grants and policies are re-applied.
-- =============================================================================

\set ON_ERROR_STOP on

-- Create the role if missing. psql variables are not expanded inside DO $$ bodies,
-- so build the statement with format() and run it with \gexec.
SELECT format('CREATE ROLE eval_writer LOGIN NOBYPASSRLS NOSUPERUSER NOCREATEDB NOCREATEROLE PASSWORD %L',
              :'eval_writer_password')
WHERE NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'eval_writer')
\gexec

-- An already-existing role must also lack BYPASSRLS / superuser.
ALTER ROLE eval_writer NOBYPASSRLS NOSUPERUSER;

GRANT USAGE ON SCHEMA eval TO eval_writer;

GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA eval TO eval_writer;
-- Re-evaluation replaces metric rows; nothing else is deleted by the writer
-- (FK cascades run with the table owner's rights, not eval_writer's).
GRANT DELETE ON eval.metric_results TO eval_writer;

GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA eval TO eval_writer;

-- Views (already covered by the table grant above; stated explicitly for clarity).
GRANT SELECT ON
    eval.v_latest_evaluations,
    eval.v_stance_matrix,
    eval.v_stance_pivot,
    eval.v_domain_scores,
    eval.v_role_scorecard,
    eval.v_metric_trend,
    eval.v_jev_human_agreement,
    eval.v_pipeline_reliability
TO eval_writer;

-- RLS policies: full access for eval_writer on every table.
DO $$
DECLARE
    t text;
BEGIN
    FOREACH t IN ARRAY ARRAY[
        'runs', 'agent_outputs', 'rubrics', 'jev_calls',
        'evaluations', 'metric_results', 'human_labels'
    ] LOOP
        EXECUTE format('DROP POLICY IF EXISTS eval_writer_all ON eval.%I', t);
        EXECUTE format(
            'CREATE POLICY eval_writer_all ON eval.%I FOR ALL TO eval_writer USING (true) WITH CHECK (true)',
            t
        );
    END LOOP;
END
$$;
