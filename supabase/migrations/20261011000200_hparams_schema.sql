-- =============================================================================
-- hparams schema: versioned, content-addressed snapshots of the research
-- pipeline's hyperparameters, and which snapshot each run in eval.runs used.
-- Target: Supabase / PostgreSQL 17.
--
-- A snapshot is three groups of settings:
--   1. Runtime limits: tool timeout and thread pool, agent timeout, token
--      budgets, recursion limits, concurrency, model transport.
--   2. Per-agent config for all 13 roles: model, limits as enforced and as told
--      to the model, task, and the exact prompt texts.
--   3. Tools: definitions, FastMCP role tags, and the resolved role x tool
--      access matrix.
--
-- Written by equity_mcp/hparams (ingest.py), via the `eval_writer` role.
-- Grants and policies: supabase/sql/eval_writer_role.sql.
-- Locked down like eval: RLS on, no policies here, nothing for anon or
-- authenticated, and not exposed to the Data API.
-- Idempotent: safe to re-run.
-- =============================================================================

CREATE SCHEMA IF NOT EXISTS hparams;

COMMENT ON SCHEMA hparams IS
    'Hyperparameter snapshots (runtime limits, per-agent config, tools and access) tied to eval.runs through hparams.run_configs.';

-- -----------------------------------------------------------------------------
-- Functions
-- -----------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION hparams.touch_updated_at()
RETURNS trigger
LANGUAGE plpgsql
SET search_path = pg_catalog
AS $$
BEGIN
    NEW.updated_at := now();
    RETURN NEW;
END;
$$;

COMMENT ON FUNCTION hparams.touch_updated_at() IS
    'BEFORE UPDATE trigger: stamps updated_at with now().';

-- A stored config's provenance may be upgraded by a better observation, never downgraded.
CREATE OR REPLACE FUNCTION hparams.provenance_rank(p text)
RETURNS integer
LANGUAGE sql IMMUTABLE PARALLEL SAFE
SET search_path = pg_catalog
AS $$
    SELECT CASE p WHEN 'inferred' THEN 1 WHEN 'reconstructed_from_git' THEN 2 WHEN 'captured_at_runtime' THEN 3 END
$$;

COMMENT ON FUNCTION hparams.provenance_rank(text) IS
    'Rank of a configs.provenance value: inferred 1 < reconstructed_from_git 2 < captured_at_runtime 3.';

-- A run's link may be replaced by one at least as well founded, never by a weaker one.
CREATE OR REPLACE FUNCTION hparams.link_basis_rank(b text)
RETURNS integer
LANGUAGE sql IMMUTABLE PARALLEL SAFE
SET search_path = pg_catalog
AS $$
    SELECT CASE b WHEN 'inferred' THEN 1 WHEN 'git_checkout' THEN 2
                  WHEN 'prompt_sha_match' THEN 3 WHEN 'recorded_in_run' THEN 4 END
$$;

COMMENT ON FUNCTION hparams.link_basis_rank(text) IS
    'Rank of a run_configs.link_basis value: inferred 1 < git_checkout 2 < prompt_sha_match 3 < recorded_in_run 4.';

-- -----------------------------------------------------------------------------
-- hparams.configs : one row per distinct configuration
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS hparams.configs (
    config_sha        text PRIMARY KEY CHECK (config_sha ~ '^[0-9a-f]{64}$'),
    snapshot_version  integer NOT NULL,
    provenance        text NOT NULL CHECK (provenance IN
                          ('captured_at_runtime', 'reconstructed_from_git', 'inferred')),
    effective_at      timestamptz NOT NULL,
    last_seen_at      timestamptz NOT NULL,
    source_git_sha    text CHECK (source_git_sha IS NULL OR source_git_sha ~ '^[0-9a-f]{40}$'),
    source_git_dirty  boolean,
    gaps              text[] NOT NULL DEFAULT '{}',
    libs              jsonb,
    content           jsonb NOT NULL,
    label             text,
    notes             text,
    created_at        timestamptz NOT NULL DEFAULT now(),
    updated_at        timestamptz NOT NULL DEFAULT now(),
    CHECK (last_seen_at >= effective_at)
);

COMMENT ON TABLE hparams.configs IS
    'Immutable, content-addressed snapshot of the whole pipeline configuration, keyed by the hash of its canonical JSON content. Only the observation metadata (provenance, dates, git, gaps, libs) may change.';

CREATE INDEX IF NOT EXISTS configs_last_seen_at_idx ON hparams.configs (last_seen_at DESC);

-- -----------------------------------------------------------------------------
-- hparams.texts : every distinct prompt-side text, stored once
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS hparams.texts (
    text_sha    text PRIMARY KEY CHECK (text_sha ~ '^[0-9a-f]{64}$'),
    body        text NOT NULL,
    chars       integer GENERATED ALWAYS AS (char_length(body)) STORED,
    created_at  timestamptz NOT NULL DEFAULT now(),
    -- The writer sends LF-normalised bodies, as loader.prompt_sha256 hashes them.
    CONSTRAINT texts_sha_matches_body CHECK (text_sha = encode(sha256(convert_to(body, 'UTF8')), 'hex'))
);

COMMENT ON TABLE hparams.texts IS
    'Every distinct prompt-side text stored once, keyed by the sha256 of its LF-normalised UTF-8 bytes: raw role prompts, the budget template, rendered budget blocks and composed prompts.';

-- -----------------------------------------------------------------------------
-- hparams.config_runtime : group 1, one row per config
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS hparams.config_runtime (
    config_sha                  text PRIMARY KEY REFERENCES hparams.configs (config_sha),
    tool_timeout_s              double precision CHECK (tool_timeout_s > 0),
    max_tool_threads            integer          CHECK (max_tool_threads > 0),
    specialist_max_tokens       integer,
    memo_max_tokens             integer,
    specialist_recursion_limit  integer,
    master_recursion_limit      integer,
    agent_timeout_s             double precision CHECK (agent_timeout_s > 0),
    default_max_concurrency     integer          CHECK (default_max_concurrency > 0),
    advertised_fraction         numeric,
    request_timeout_ms          integer,
    streaming                   boolean,
    provider_routing            jsonb,
    default_model               text,
    agent_model_overrides       jsonb,
    budget_template_sha         text REFERENCES hparams.texts (text_sha),
    extra                       jsonb NOT NULL DEFAULT '{}'
);

COMMENT ON TABLE hparams.config_runtime IS
    'Group 1: the code-default runtime limits and model transport of a config. The real ceilings only: the values quoted to the model are per agent in config_agents, and CLI overrides are per run in run_configs.';

CREATE INDEX IF NOT EXISTS config_runtime_budget_template_idx ON hparams.config_runtime (budget_template_sha);

-- -----------------------------------------------------------------------------
-- hparams.config_agents : group 2, one row per config x role
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS hparams.config_agents (
    config_sha                  text NOT NULL REFERENCES hparams.configs (config_sha),
    role                        text NOT NULL,
    stage                       smallint CHECK (stage IN (1, 2, 3)),
    agent_kind                  text NOT NULL CHECK (agent_kind IN ('react_specialist', 'deep_master')),
    model_slug                  text,
    model_spec                  text,
    max_tokens                  integer,
    recursion_limit             integer,
    advertised_recursion_limit  integer,
    advertised_tool_rounds      integer,
    advertised_write_by         integer,
    advertised_timeout_s        double precision,
    task                        text,
    prompt_source               text CHECK (prompt_source IN ('file', 'fallback')),
    system_prompt_sha           text REFERENCES hparams.texts (text_sha),
    budget_sha                  text REFERENCES hparams.texts (text_sha),
    composed_prompt_sha         text REFERENCES hparams.texts (text_sha),
    tool_count                  integer,
    agent_sha                   text CHECK (agent_sha ~ '^[0-9a-f]{64}$'),
    PRIMARY KEY (config_sha, role)
);

COMMENT ON TABLE hparams.config_agents IS
    'Group 2: per-role configuration of a snapshot: model, limits as enforced and as advertised to the model, task, and references to the prompt texts. system_prompt_sha joins to eval.rubrics.source_prompt_sha256.';

CREATE INDEX IF NOT EXISTS config_agents_system_prompt_idx ON hparams.config_agents (system_prompt_sha);
CREATE INDEX IF NOT EXISTS config_agents_budget_idx        ON hparams.config_agents (budget_sha);
CREATE INDEX IF NOT EXISTS config_agents_composed_idx      ON hparams.config_agents (composed_prompt_sha);
CREATE INDEX IF NOT EXISTS config_agents_role_agent_sha_idx ON hparams.config_agents (role, agent_sha);

-- -----------------------------------------------------------------------------
-- hparams.tool_defs : one row per distinct tool definition
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS hparams.tool_defs (
    tool_sha      text PRIMARY KEY CHECK (tool_sha ~ '^[0-9a-f]{64}$'),
    tool_name     text NOT NULL,
    module        text,
    description   text,
    input_schema  jsonb,
    impl_sha256   text,
    created_at    timestamptz NOT NULL DEFAULT now()
);

COMMENT ON TABLE hparams.tool_defs IS
    'Content-addressed definition of an MCP tool as an agent sees it (name, module, description, input JSON schema) plus a hash of the implementing function. Tags are per config, in config_tools.';

CREATE INDEX IF NOT EXISTS tool_defs_tool_name_idx ON hparams.tool_defs (tool_name);

-- -----------------------------------------------------------------------------
-- hparams.config_tools : group 3, one row per config x tool
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS hparams.config_tools (
    config_sha  text NOT NULL REFERENCES hparams.configs (config_sha),
    tool_name   text NOT NULL,
    tool_sha    text NOT NULL REFERENCES hparams.tool_defs (tool_sha),
    tags        text[] NOT NULL,
    PRIMARY KEY (config_sha, tool_name)
);

COMMENT ON TABLE hparams.config_tools IS
    'The tools registered in equity_mcp/server.py for a snapshot: which definition, under which FastMCP role tags.';

CREATE INDEX IF NOT EXISTS config_tools_tool_sha_idx ON hparams.config_tools (tool_sha);

-- -----------------------------------------------------------------------------
-- hparams.config_role_tools : resolved access, one row per config x role x tool
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS hparams.config_role_tools (
    config_sha  text NOT NULL,
    role        text NOT NULL,
    tool_name   text NOT NULL,
    via         text NOT NULL CHECK (via IN ('role', 'shared')),
    PRIMARY KEY (config_sha, role, tool_name),
    FOREIGN KEY (config_sha, role)      REFERENCES hparams.config_agents (config_sha, role),
    FOREIGN KEY (config_sha, tool_name) REFERENCES hparams.config_tools (config_sha, tool_name)
);

COMMENT ON TABLE hparams.config_role_tools IS
    'Resolved role x tool access: the tools the bridge actually handed each role (langchain_bridge.get_langchain_tools_for_role). via says which tag granted it.';

CREATE INDEX IF NOT EXISTS config_role_tools_tool_idx ON hparams.config_role_tools (config_sha, tool_name);

-- -----------------------------------------------------------------------------
-- hparams.run_configs : one row per research run
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS hparams.run_configs (
    run_id              text PRIMARY KEY REFERENCES eval.runs (run_id) ON DELETE CASCADE,
    config_sha          text NOT NULL REFERENCES hparams.configs (config_sha),
    link_basis          text NOT NULL CHECK (link_basis IN
                            ('recorded_in_run', 'prompt_sha_match', 'git_checkout', 'inferred')),
    research_git_sha    text CHECK (research_git_sha IS NULL OR research_git_sha ~ '^[0-9a-f]{40}$'),
    max_concurrency     integer CHECK (max_concurrency > 0),
    run_timeout_s       double precision,
    agents_requested    text[],
    extra_instructions  text,
    overrides           jsonb NOT NULL DEFAULT '{}',
    notes               text,
    linked_at           timestamptz NOT NULL DEFAULT now(),
    updated_at          timestamptz NOT NULL DEFAULT now()
);

COMMENT ON TABLE hparams.run_configs IS
    'Ties each research run in eval.runs to the config that produced it, with the per-invocation settings (concurrency, timeout, agents, focus) applied on top of the code defaults.';

CREATE INDEX IF NOT EXISTS run_configs_config_sha_idx ON hparams.run_configs (config_sha);

-- -----------------------------------------------------------------------------
-- updated_at triggers
-- -----------------------------------------------------------------------------
CREATE OR REPLACE TRIGGER configs_touch_updated_at
    BEFORE UPDATE ON hparams.configs
    FOR EACH ROW EXECUTE FUNCTION hparams.touch_updated_at();

CREATE OR REPLACE TRIGGER run_configs_touch_updated_at
    BEFORE UPDATE ON hparams.run_configs
    FOR EACH ROW EXECUTE FUNCTION hparams.touch_updated_at();

-- -----------------------------------------------------------------------------
-- Row level security: enabled everywhere, no policies here.
-- -----------------------------------------------------------------------------
ALTER TABLE hparams.configs            ENABLE ROW LEVEL SECURITY;
ALTER TABLE hparams.texts              ENABLE ROW LEVEL SECURITY;
ALTER TABLE hparams.config_runtime     ENABLE ROW LEVEL SECURITY;
ALTER TABLE hparams.config_agents      ENABLE ROW LEVEL SECURITY;
ALTER TABLE hparams.tool_defs          ENABLE ROW LEVEL SECURITY;
ALTER TABLE hparams.config_tools       ENABLE ROW LEVEL SECURITY;
ALTER TABLE hparams.config_role_tools  ENABLE ROW LEVEL SECURITY;
ALTER TABLE hparams.run_configs        ENABLE ROW LEVEL SECURITY;

-- -----------------------------------------------------------------------------
-- Lock the schema away from PUBLIC and the Supabase API roles
-- -----------------------------------------------------------------------------
DO $$
DECLARE
    r text;
BEGIN
    REVOKE ALL ON SCHEMA hparams FROM PUBLIC;
    REVOKE ALL ON ALL TABLES    IN SCHEMA hparams FROM PUBLIC;
    REVOKE ALL ON ALL SEQUENCES IN SCHEMA hparams FROM PUBLIC;
    REVOKE ALL ON ALL FUNCTIONS IN SCHEMA hparams FROM PUBLIC;

    FOREACH r IN ARRAY ARRAY['anon', 'authenticated'] LOOP
        IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = r) THEN
            EXECUTE format('REVOKE ALL ON SCHEMA hparams FROM %I', r);
            EXECUTE format('REVOKE ALL ON ALL TABLES    IN SCHEMA hparams FROM %I', r);
            EXECUTE format('REVOKE ALL ON ALL SEQUENCES IN SCHEMA hparams FROM %I', r);
            EXECUTE format('REVOKE ALL ON ALL FUNCTIONS IN SCHEMA hparams FROM %I', r);
            EXECUTE format('ALTER DEFAULT PRIVILEGES IN SCHEMA hparams REVOKE ALL ON TABLES    FROM %I', r);
            EXECUTE format('ALTER DEFAULT PRIVILEGES IN SCHEMA hparams REVOKE ALL ON SEQUENCES FROM %I', r);
            EXECUTE format('ALTER DEFAULT PRIVILEGES IN SCHEMA hparams REVOKE ALL ON FUNCTIONS FROM %I', r);
        END IF;
    END LOOP;
END
$$;
