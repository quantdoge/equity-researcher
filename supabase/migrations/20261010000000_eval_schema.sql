-- =============================================================================
-- eval schema: LLM-evaluation results store (Jev classifier over agent output)
-- Target: Supabase / PostgreSQL 17.
--
-- Written to by a Python process (psycopg 3 via the Supavisor session pooler)
-- using the least-privilege `eval_writer` role (see supabase/sql/eval_writer_role.sql).
-- The schema is deliberately NOT exposed to the Supabase Data API: anon and
-- authenticated get nothing, RLS is on, and this migration defines no policies.
-- Idempotent: safe to re-run.
-- =============================================================================

CREATE SCHEMA IF NOT EXISTS eval;

-- -----------------------------------------------------------------------------
-- updated_at trigger function
-- -----------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION eval.touch_updated_at()
RETURNS trigger
LANGUAGE plpgsql
SET search_path = pg_catalog
AS $$
BEGIN
    NEW.updated_at := now();
    RETURN NEW;
END;
$$;

COMMENT ON FUNCTION eval.touch_updated_at() IS
    'BEFORE UPDATE trigger: stamps updated_at with now().';

-- -----------------------------------------------------------------------------
-- eval.runs : one row per research output file
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS eval.runs (
    run_id             text PRIMARY KEY,
    symbol             text NOT NULL,
    run_date           date,
    source_path        text,
    source_sha256      text,
    schema_kind        text NOT NULL CHECK (schema_kind IN ('agent_results_v1', 'legacy')),
    skipped_synthesis  boolean NOT NULL DEFAULT false,
    failures           text[] NOT NULL DEFAULT '{}',
    elapsed_seconds    double precision,
    git_sha            text,
    skip_reason        text,
    ingested_at        timestamptz NOT NULL DEFAULT now(),
    updated_at         timestamptz NOT NULL DEFAULT now()
);

COMMENT ON TABLE eval.runs IS
    'One row per ingested research output file (one pipeline run for one symbol). Parent of agent outputs, evaluations and human labels.';

CREATE INDEX IF NOT EXISTS runs_symbol_run_date_idx ON eval.runs (symbol, run_date);

-- -----------------------------------------------------------------------------
-- eval.agent_outputs : one row per run x role
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS eval.agent_outputs (
    id                    bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    run_id                text NOT NULL REFERENCES eval.runs (run_id) ON DELETE CASCADE,
    role                  text NOT NULL,
    status                text NOT NULL CHECK (status IN ('ok', 'failed', 'degenerate', 'missing')),
    error                 text,
    output_text           text,
    output_sha256         text,
    chars                 integer,
    preamble_chars        integer,
    section_names         text[],
    agent_model           text,
    agent_model_inferred  boolean,
    elapsed_seconds       double precision,
    extracts              jsonb NOT NULL DEFAULT '{}',
    created_at            timestamptz NOT NULL DEFAULT now(),
    updated_at            timestamptz NOT NULL DEFAULT now(),
    UNIQUE (run_id, role)
);

COMMENT ON TABLE eval.agent_outputs IS
    'The text (and basic stats) each research agent produced in a run, with its pipeline status. One row per run and role.';

CREATE INDEX IF NOT EXISTS agent_outputs_role_idx ON eval.agent_outputs (role);

-- -----------------------------------------------------------------------------
-- eval.rubrics : versioned rubric snapshots, content-addressed
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS eval.rubrics (
    rubric_sha            text PRIMARY KEY,
    role                  text NOT NULL,
    rubric_version        integer NOT NULL,
    shared_version        integer NOT NULL,
    source_prompt_sha256  text,
    calibrated            boolean NOT NULL DEFAULT false,
    content               jsonb NOT NULL,
    created_at            timestamptz NOT NULL DEFAULT now()
);

COMMENT ON TABLE eval.rubrics IS
    'Immutable, content-addressed snapshots of the per-role evaluation rubric (keyed by hash) so every evaluation can be traced to the exact questions asked.';

CREATE INDEX IF NOT EXISTS rubrics_role_idx ON eval.rubrics (role);

-- -----------------------------------------------------------------------------
-- eval.jev_calls : call log + cache of successful classifier calls
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS eval.jev_calls (
    id                   bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    cache_key            text NOT NULL,
    state_sha256         text,
    questions_sha256     text,
    jev_model_requested  text NOT NULL,
    jev_model_returned   text,
    request_id           text,
    http_status          integer,
    latency_ms           integer,
    input_tokens         integer,
    output_tokens        integer,
    state_chars          integer,
    state_truncated      boolean NOT NULL DEFAULT false,
    answers              jsonb,
    error                text,
    created_at           timestamptz NOT NULL DEFAULT now()
);

COMMENT ON TABLE eval.jev_calls IS
    'Log of every Jev classifier call. Successful calls (error IS NULL) are unique per cache_key and act as a cache; failed calls are only logged and may repeat.';

CREATE UNIQUE INDEX IF NOT EXISTS jev_calls_cache_key_ok
    ON eval.jev_calls (cache_key)
    WHERE error IS NULL;

-- -----------------------------------------------------------------------------
-- eval.evaluations : one per run x role x rubric x Jev model
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS eval.evaluations (
    id                    bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    run_id                text NOT NULL REFERENCES eval.runs (run_id) ON DELETE CASCADE,
    role                  text NOT NULL,
    agent_output_id       bigint REFERENCES eval.agent_outputs (id) ON DELETE CASCADE,
    rubric_sha            text NOT NULL REFERENCES eval.rubrics (rubric_sha),
    jev_model             text NOT NULL,
    evaluator_version     text,
    pass                  smallint NOT NULL CHECK (pass IN (1, 2)),
    status                text NOT NULL CHECK (status IN
                              ('complete', 'partial', 'agent_failed', 'degenerate', 'missing', 'error')),
    stance                text CHECK (stance IS NULL OR stance IN
                              ('STRONG SELL', 'SELL', 'HOLD', 'BUY', 'STRONG BUY')),
    stance_probabilities  jsonb,
    stance_expected       numeric CHECK (stance_expected BETWEEN -2 AND 2),
    stance_confidence     numeric,
    stance_low_evidence   boolean,
    conviction_level      text CHECK (conviction_level IS NULL OR conviction_level IN ('Low', 'Medium', 'High')),
    conviction_score      numeric,
    native_rating         text,
    native_stance         text,
    stance_agreement      boolean,
    domain_profile        jsonb,
    domain_mean           numeric,
    domain_addressed      integer,
    domain_total          integer,
    alignment_composite   numeric,
    alignment_dimensions  jsonb,
    alignment_coverage    numeric,
    veto_triggered        boolean NOT NULL DEFAULT false,
    vetoes                text[] NOT NULL DEFAULT '{}',
    insufficient_evidence boolean NOT NULL DEFAULT false,
    advisory              boolean NOT NULL DEFAULT true,
    n_metrics             integer,
    n_errors              integer,
    n_calls               integer,
    n_cached              integer,
    input_tokens          integer,
    output_tokens         integer,
    started_at            timestamptz,
    finished_at           timestamptz,
    created_at            timestamptz NOT NULL DEFAULT now(),
    UNIQUE (run_id, role, rubric_sha, jev_model)
);

COMMENT ON TABLE eval.evaluations IS
    'Headline result of evaluating one agent output with one rubric and one Jev model: stance, conviction, domain and alignment summaries, vetoes and cost counters.';

CREATE INDEX IF NOT EXISTS evaluations_role_finished_at_idx ON eval.evaluations (role, finished_at);
CREATE INDEX IF NOT EXISTS evaluations_run_id_idx           ON eval.evaluations (run_id);

-- -----------------------------------------------------------------------------
-- eval.metric_results : one row per evaluation x question x variant
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS eval.metric_results (
    id                   bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    evaluation_id        bigint NOT NULL REFERENCES eval.evaluations (id) ON DELETE CASCADE,
    question_id          text NOT NULL,
    block                text NOT NULL CHECK (block IN ('conviction', 'domain', 'alignment')),
    variant              text NOT NULL DEFAULT 'primary' CHECK (variant IN ('primary', 'reversed')),
    kind                 text NOT NULL CHECK (kind IN ('noul', 'score', 'choice', 'deterministic')),
    rubric_request       text,
    dimension            text,
    label                text,
    weight               numeric,
    veto                 boolean NOT NULL DEFAULT false,
    noul_p               numeric,
    choice               text,
    score                numeric,
    n_levels             smallint,
    probabilities        jsonb,
    confidence           numeric,
    deterministic_value  numeric,
    detail               text,
    code_extract         text,
    agreement            boolean,
    normalized           numeric,
    passed               boolean,
    status               text NOT NULL CHECK (status IN
                             ('ok', 'error', 'skipped', 'low_evidence', 'not_addressed')),
    error                text,
    jev_call_id          bigint REFERENCES eval.jev_calls (id) ON DELETE SET NULL,
    created_at           timestamptz NOT NULL DEFAULT now(),
    UNIQUE (evaluation_id, question_id, variant)
);

COMMENT ON TABLE eval.metric_results IS
    'Per-question results behind an evaluation (conviction, domain and alignment blocks), including the raw classifier readout and the normalized score. Replaced wholesale on re-evaluation.';

CREATE INDEX IF NOT EXISTS metric_results_question_id_idx ON eval.metric_results (question_id);
CREATE INDEX IF NOT EXISTS metric_results_block_idx       ON eval.metric_results (block);
-- Supports the ON DELETE SET NULL action from jev_calls and call-to-metric lookups.
CREATE INDEX IF NOT EXISTS metric_results_jev_call_id_idx ON eval.metric_results (jev_call_id);

-- -----------------------------------------------------------------------------
-- eval.human_labels : human ground truth for calibrating Jev
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS eval.human_labels (
    id           bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    run_id       text NOT NULL REFERENCES eval.runs (run_id) ON DELETE CASCADE,
    role         text NOT NULL,
    question_id  text NOT NULL,
    labeler      text NOT NULL,
    label        jsonb NOT NULL,
    notes        text,
    created_at   timestamptz NOT NULL DEFAULT now(),
    UNIQUE (run_id, role, question_id, labeler)
);

COMMENT ON TABLE eval.human_labels IS
    'Human judgments for individual rubric questions on a run and role, used to measure and calibrate agreement with Jev.';

-- -----------------------------------------------------------------------------
-- updated_at triggers
-- -----------------------------------------------------------------------------
CREATE OR REPLACE TRIGGER runs_touch_updated_at
    BEFORE UPDATE ON eval.runs
    FOR EACH ROW EXECUTE FUNCTION eval.touch_updated_at();

CREATE OR REPLACE TRIGGER agent_outputs_touch_updated_at
    BEFORE UPDATE ON eval.agent_outputs
    FOR EACH ROW EXECUTE FUNCTION eval.touch_updated_at();

-- -----------------------------------------------------------------------------
-- Row level security: enabled everywhere, no policies here.
-- Policies for the writer role live in supabase/sql/eval_writer_role.sql.
-- -----------------------------------------------------------------------------
ALTER TABLE eval.runs            ENABLE ROW LEVEL SECURITY;
ALTER TABLE eval.agent_outputs   ENABLE ROW LEVEL SECURITY;
ALTER TABLE eval.rubrics         ENABLE ROW LEVEL SECURITY;
ALTER TABLE eval.jev_calls       ENABLE ROW LEVEL SECURITY;
ALTER TABLE eval.evaluations     ENABLE ROW LEVEL SECURITY;
ALTER TABLE eval.metric_results  ENABLE ROW LEVEL SECURITY;
ALTER TABLE eval.human_labels    ENABLE ROW LEVEL SECURITY;

-- -----------------------------------------------------------------------------
-- Views (all security_invoker so they run with the caller's privileges + RLS)
-- -----------------------------------------------------------------------------

-- 1. Latest evaluation per (run_id, role), joined with run metadata.
CREATE OR REPLACE VIEW eval.v_latest_evaluations
WITH (security_invoker = true) AS
SELECT
    r.symbol,
    r.run_date,
    le.*
FROM (
    SELECT DISTINCT ON (e.run_id, e.role) e.*
    FROM eval.evaluations AS e
    ORDER BY e.run_id, e.role, e.finished_at DESC NULLS LAST, e.id DESC
) AS le
JOIN eval.runs AS r ON r.run_id = le.run_id;

COMMENT ON VIEW eval.v_latest_evaluations IS
    'Most recent evaluation per run and role (finished_at, then id), with the run symbol and date. Base for the other reporting views.';

-- 2. Long-format stance matrix.
CREATE OR REPLACE VIEW eval.v_stance_matrix
WITH (security_invoker = true) AS
SELECT
    symbol,
    run_date,
    run_id,
    role,
    stance,
    stance_expected,
    stance_confidence,
    conviction_level,
    native_rating,
    native_stance,
    stance_agreement,
    stance_low_evidence,
    status
FROM eval.v_latest_evaluations;

COMMENT ON VIEW eval.v_stance_matrix IS
    'One row per run and role with Jev stance, conviction and agreement with the agent''s own rating.';

-- 3. Wide stance pivot, one row per run.
CREATE OR REPLACE VIEW eval.v_stance_pivot
WITH (security_invoker = true) AS
SELECT
    symbol,
    run_date,
    run_id,
    max(stance) FILTER (WHERE role = 'sector_researcher')      AS sector_researcher,
    max(stance) FILTER (WHERE role = 'geo_legal_researcher')   AS geo_legal_researcher,
    max(stance) FILTER (WHERE role = 'macro_researcher')       AS macro_researcher,
    max(stance) FILTER (WHERE role = 'value_researcher')       AS value_researcher,
    max(stance) FILTER (WHERE role = 'growth_researcher')      AS growth_researcher,
    max(stance) FILTER (WHERE role = 'fin_risk_analyst')       AS fin_risk_analyst,
    max(stance) FILTER (WHERE role = 'nonfin_risk_analyst')    AS nonfin_risk_analyst,
    max(stance) FILTER (WHERE role = 'quant_analyst')          AS quant_analyst,
    max(stance) FILTER (WHERE role = 'short_analyst')          AS short_analyst,
    max(stance) FILTER (WHERE role = 'esg_analyst')            AS esg_analyst,
    max(stance) FILTER (WHERE role = 'alt_data_analyst')       AS alt_data_analyst,
    max(stance) FILTER (WHERE role = 'portfolio_strategist')   AS portfolio_strategist,
    max(stance) FILTER (WHERE role = 'head_of_research')       AS head_of_research,
    avg(stance_expected) FILTER (WHERE role IN (
        'sector_researcher', 'geo_legal_researcher', 'macro_researcher',
        'value_researcher', 'growth_researcher', 'fin_risk_analyst',
        'nonfin_risk_analyst', 'quant_analyst', 'short_analyst',
        'esg_analyst', 'alt_data_analyst'
    ))                                                         AS avg_stance_expected
FROM eval.v_latest_evaluations
GROUP BY symbol, run_date, run_id;

COMMENT ON VIEW eval.v_stance_pivot IS
    'One row per run with a stance column per role; avg_stance_expected averages the 11 specialists only (not strategist or head of research).';

-- 4. Domain metric scores for the latest evaluations.
CREATE OR REPLACE VIEW eval.v_domain_scores
WITH (security_invoker = true) AS
SELECT
    le.symbol,
    le.run_date,
    le.run_id,
    le.role,
    m.question_id        AS metric,
    m.variant,
    m.label,
    m.score,
    m.score + 1          AS level,       -- 0-based score shown on a 1-5 scale
    m.normalized,
    m.confidence,
    m.status
FROM eval.v_latest_evaluations AS le
JOIN eval.metric_results       AS m ON m.evaluation_id = le.id
WHERE m.block = 'domain';

COMMENT ON VIEW eval.v_domain_scores IS
    'Domain-block metric results for the latest evaluation of each run and role; level is score + 1 for a 1-5 display scale.';

-- 5. Per-role scorecard.
CREATE OR REPLACE VIEW eval.v_role_scorecard
WITH (security_invoker = true) AS
SELECT
    symbol,
    run_date,
    run_id,
    role,
    status,
    alignment_composite,
    alignment_coverage,
    alignment_dimensions,
    veto_triggered,
    vetoes,
    insufficient_evidence,
    advisory,
    domain_mean,
    domain_addressed,
    domain_total,
    stance,
    conviction_level
FROM eval.v_latest_evaluations;

COMMENT ON VIEW eval.v_role_scorecard IS
    'Headline scorecard per run and role from the latest evaluation: alignment, vetoes, domain coverage, stance and conviction.';

-- 6. Weekly metric trend (primary variant only; reversed items are consistency probes).
CREATE OR REPLACE VIEW eval.v_metric_trend
WITH (security_invoker = true) AS
SELECT
    le.role,
    m.question_id,
    m.block,
    date_trunc('week', le.run_date)::date                   AS week,
    count(*)                                                AS n,
    avg(m.passed::int) FILTER (WHERE m.status = 'ok')       AS pass_rate,
    avg(m.normalized)                                       AS avg_normalized
FROM eval.v_latest_evaluations AS le
JOIN eval.metric_results       AS m ON m.evaluation_id = le.id
WHERE m.variant = 'primary'
GROUP BY le.role, m.question_id, m.block, date_trunc('week', le.run_date);

COMMENT ON VIEW eval.v_metric_trend IS
    'Weekly trend per role, question and block over latest evaluations (primary variant): count, pass rate over status=ok rows, and mean normalized score.';

-- 7. Jev vs human agreement.
CREATE OR REPLACE VIEW eval.v_jev_human_agreement
WITH (security_invoker = true) AS
SELECT
    h.run_id,
    h.role,
    h.question_id,
    h.labeler,
    h.label,
    h.notes,
    le.symbol,
    le.run_date,
    m.block,
    m.noul_p,
    m.choice,
    m.score,
    m.passed,
    m.status
FROM eval.human_labels         AS h
JOIN eval.v_latest_evaluations AS le
  ON le.run_id = h.run_id AND le.role = h.role
JOIN eval.metric_results       AS m
  ON m.evaluation_id = le.id
 AND m.question_id   = h.question_id
 AND m.variant       = 'primary';

COMMENT ON VIEW eval.v_jev_human_agreement IS
    'Each human label next to Jev''s primary-variant readout (noul_p, choice, score, passed) from the latest evaluation of the same run, role and question.';

-- 8. Pipeline reliability per role.
CREATE OR REPLACE VIEW eval.v_pipeline_reliability
WITH (security_invoker = true) AS
SELECT
    role,
    count(*)                                               AS n,
    count(*) FILTER (WHERE status = 'ok')                  AS n_ok,
    count(*) FILTER (WHERE status = 'failed')              AS n_failed,
    count(*) FILTER (WHERE status = 'degenerate')          AS n_degenerate,
    count(*) FILTER (WHERE status = 'missing')             AS n_missing,
    (count(*) FILTER (WHERE status = 'ok'))::numeric
        / NULLIF(count(*), 0)                              AS ok_rate
FROM eval.agent_outputs
GROUP BY role;

COMMENT ON VIEW eval.v_pipeline_reliability IS
    'Share of runs in which each agent role produced a usable output, broken down by failure type.';

-- -----------------------------------------------------------------------------
-- Lock the schema away from PUBLIC and the Supabase API roles
-- (guarded: local/non-Supabase databases may lack anon/authenticated)
-- -----------------------------------------------------------------------------
DO $$
DECLARE
    r text;
BEGIN
    REVOKE ALL ON SCHEMA eval FROM PUBLIC;
    REVOKE ALL ON ALL TABLES    IN SCHEMA eval FROM PUBLIC;
    REVOKE ALL ON ALL SEQUENCES IN SCHEMA eval FROM PUBLIC;
    REVOKE ALL ON ALL FUNCTIONS IN SCHEMA eval FROM PUBLIC;

    FOREACH r IN ARRAY ARRAY['anon', 'authenticated'] LOOP
        IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = r) THEN
            EXECUTE format('REVOKE ALL ON SCHEMA eval FROM %I', r);
            EXECUTE format('REVOKE ALL ON ALL TABLES    IN SCHEMA eval FROM %I', r);
            EXECUTE format('REVOKE ALL ON ALL SEQUENCES IN SCHEMA eval FROM %I', r);
            EXECUTE format('REVOKE ALL ON ALL FUNCTIONS IN SCHEMA eval FROM %I', r);
            -- Keep future objects created by the migration owner private too.
            EXECUTE format('ALTER DEFAULT PRIVILEGES IN SCHEMA eval REVOKE ALL ON TABLES    FROM %I', r);
            EXECUTE format('ALTER DEFAULT PRIVILEGES IN SCHEMA eval REVOKE ALL ON SEQUENCES FROM %I', r);
            EXECUTE format('ALTER DEFAULT PRIVILEGES IN SCHEMA eval REVOKE ALL ON FUNCTIONS FROM %I', r);
        END IF;
    END LOOP;
END
$$;
