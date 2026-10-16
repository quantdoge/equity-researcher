-- =============================================================================
-- datadict seed: documentation for every table, view and column in `hparams`.
--
-- Follows 20261010020100_datadict_eval_seed.sql:
--   - data_type, is_nullable and ordinal_position come from pg_catalog, never
--     from this file.
--   - Pass-through view columns are generated with derived_from pointing at
--     their source column.
--   - Example values come from the snapshot of the code as of 2026-10-11.
-- Idempotent: re-running updates text but never resets created_date.
-- =============================================================================

-- -----------------------------------------------------------------------------
-- 1. Objects
-- -----------------------------------------------------------------------------
INSERT INTO datadict.tables (schema_name, table_name, object_type, description, grain, primary_key, created_date) VALUES
('hparams', 'configs', 'table',
 'One snapshot of the whole research-pipeline configuration (runtime limits, per-agent config, tools and access), keyed by the hash of its canonical JSON. Identical code gives the same row however it was observed; only the observation metadata changes.',
 'one row per distinct configuration', 'config_sha', DATE '2026-10-11'),
('hparams', 'texts', 'table',
 'Every distinct prompt-side text stored once: the raw prompts/<role>.md files, the _execution_budget.md template, each rendered budget block and each composed prompt an agent was built with.',
 'one row per distinct text', 'text_sha', DATE '2026-10-11'),
('hparams', 'config_runtime', 'table',
 'Group 1 of a snapshot: the code-default runtime limits (tool timeout, tool threads, agent timeout, token budgets, recursion limits, concurrency) and the model transport settings.',
 'one row per configuration', 'config_sha', DATE '2026-10-11'),
('hparams', 'config_agents', 'table',
 'Group 2 of a snapshot: how each of the 13 agents is built: its model, its limits as enforced and as told to the model, its task, and which prompt texts it received.',
 'one row per configuration × agent role', 'config_sha, role', DATE '2026-10-11'),
('hparams', 'tool_defs', 'table',
 'Each distinct definition of an MCP tool as an agent sees it (name, description, input schema), plus the module and a hash of the implementing function.',
 'one row per distinct tool definition', 'tool_sha', DATE '2026-10-11'),
('hparams', 'config_tools', 'table',
 'Group 3 of a snapshot: the tools registered in equity_mcp/server.py, which definition each one had and which FastMCP role tags it carried.',
 'one row per configuration × tool', 'config_sha, tool_name', DATE '2026-10-11'),
('hparams', 'config_role_tools', 'table',
 'The resolved access matrix of a snapshot: every tool the bridge handed each role, and whether its own role tag or the shared tag granted it.',
 'one row per configuration × agent role × tool', 'config_sha, role, tool_name', DATE '2026-10-11'),
('hparams', 'run_configs', 'table',
 'Which configuration produced each research run in eval.runs, how that link was established, and the settings that one invocation changed on top of the code defaults.',
 'one row per research run', 'run_id', DATE '2026-10-11'),
('hparams', 'v_config_current', 'view',
 'The configuration in force now: the most recently observed snapshot that is not merely inferred.',
 'zero or one row', NULL, DATE '2026-10-11'),
('hparams', 'v_config_history', 'view',
 'Every snapshot in the order it took effect, with the one before it and how many runs used it. Feed config_sha and previous_config_sha to hparams.config_diff to see what changed.',
 'one row per configuration', NULL, DATE '2026-10-11'),
('hparams', 'v_config_agents', 'view',
 'Per-role configuration of every snapshot with the composed prompt length and when that exact role config first appeared. Filter is_current for today''s agents.',
 'one row per configuration × agent role', NULL, DATE '2026-10-11'),
('hparams', 'v_config_tools', 'view',
 'Every tool of every snapshot with its module, role tags, description, input schema and implementation hash.',
 'one row per configuration × tool', NULL, DATE '2026-10-11'),
('hparams', 'v_config_access_long', 'view',
 'Role × tool access, one row per grant, with the tool''s module and the tag that granted it.',
 'one row per configuration × agent role × tool', NULL, DATE '2026-10-11'),
('hparams', 'v_config_access_wide', 'view',
 'The access matrix laid out as a grid: one row per tool, one true/false column per agent role.',
 'one row per configuration × tool', NULL, DATE '2026-10-11'),
('hparams', 'v_config_access_counts', 'view',
 'How many tools each role holds in each snapshot, split into shared and role-tagged.',
 'one row per configuration × agent role', NULL, DATE '2026-10-11'),
('hparams', 'v_run_configs', 'view',
 'Every run in eval.runs with the configuration it was tied to and the per-run settings, flagging where the run changed the default concurrency. Unlinked runs are kept with config_sha NULL.',
 'one row per research run', NULL, DATE '2026-10-11'),
('hparams', 'v_run_agent_config', 'view',
 'For each linked run and agent: the agent config in force, next to the status and model recorded with that agent''s output. Join eval.evaluations on (run_id, role) to compare scores across configs.',
 'one row per linked run × agent role', NULL, DATE '2026-10-11'),
('hparams', 'v_config_integrity', 'view',
 'Self-consistency guard over the stored snapshots. Must return 0 rows.',
 'one row per problem found', NULL, DATE '2026-10-11')
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
  "portfolio_strategist": "Synthesises the specialists into position size and portfolio action (stage 2)",
  "head_of_research": "Writes the final investment memo (stage 3)"
}'::jsonb),
doc(table_name, column_name, key_role, value_kind, source, definition, example_values, value_range, value_meanings, derived_from) AS (VALUES
-- ── hparams.configs ──────────────────────────────────────────────────────────
('configs', 'config_sha', 'PK', 'hash', 'code',
 'SHA-256 of the canonical JSON in content (sorted keys, compact separators, whole floats written as ints). Any change to a limit, model, task, prompt, budget text, tool definition, tag or watched source file gives a new hash.',
 '22b40e62dabf…', '64 hex characters.', NULL::jsonb, NULL::text),
('configs', 'snapshot_version', NULL, 'ordinal', 'code', 'Version of the snapshot format (equity_mcp/hparams/snapshot.py SNAPSHOT_VERSION). Bumped whenever what is hashed, or how, changes.', '1', 'Integer ≥ 1.', NULL, NULL),
('configs', 'provenance', NULL, 'categorical', 'code', 'How well this configuration is known. Only ever upgraded by a later observation of the same content, never downgraded.', 'captured_at_runtime; reconstructed_from_git', 'captured_at_runtime | reconstructed_from_git | inferred',
 '{"captured_at_runtime": "Read from the live modules by the process that ran the research (runs/<id>/config.json)", "reconstructed_from_git": "Extracted from a committed tree by the git backfill or sync --current; exact for that commit", "inferred": "A committed tree plus overrides deduced from run evidence (e.g. a 600 s timeout in a dirty working tree); best estimate"}', NULL),
('configs', 'effective_at', NULL, 'timestamp', 'code', 'Earliest time this configuration is known to have been in force: the run start for a capture, the commit time for a reconstruction.', '2026-09-27 01:28:23+00', 'UTC timestamp; kept at the earliest observation.', NULL, NULL),
('configs', 'last_seen_at', NULL, 'timestamp', 'code', 'Latest time this configuration is known to have been in force: the latest run that used it, or the latest sync. v_config_current orders by this.', '2026-10-06 15:30:21+00', 'UTC timestamp ≥ effective_at; kept at the latest observation.', NULL, NULL),
('configs', 'source_git_sha', NULL, 'hash', 'code', 'Commit whose tree this configuration was read from (GITHUB_SHA in CI, else git rev-parse HEAD; the chosen commit for a backfill).', 'b33c180a…', '40 hex characters, or NULL if git was unavailable.', NULL, NULL),
('configs', 'source_git_dirty', NULL, 'boolean', 'code', 'Whether equity_mcp/ differed from that commit when the snapshot was taken.', 'false', 'true | false | NULL',
 '{"true": "Uncommitted code changes were in effect; source_git_sha alone does not reproduce it", "false": "The commit reproduces it exactly", "NULL": "Unknown"}', NULL),
('configs', 'gaps', NULL, 'list', 'code', 'What the snapshot could not determine. The matching values are NULL; nothing is guessed.', '{}; {libs_unknown_reconstructed}', 'Empty array = complete. Entries like <module>.<CONSTANT>:missing, builder_failed:<role>:<Error>, libs_unknown_reconstructed, agent_timeout_s_ambiguous.', NULL, NULL),
('configs', 'libs', NULL, 'json', 'code', 'Versions of the agent and MCP libraries installed when the snapshot was taken: deepagents, langgraph, langchain, fastmcp, mcp and others. Not part of the hash. Unknown for reconstructed configs, because CI installs floating versions and uv.lock is not committed.', '{"fastmcp": "4.0.3", "deepagents": "0.7.13", "langgraph": "1.2.11"}', 'Object of package → version (NULL if not installed); NULL when unknown.', NULL, NULL),
('configs', 'content', NULL, 'json', 'code', 'The canonical snapshot that config_sha hashes: {snapshot_version, runtime, agents: {role: {..., tools}}, tools: {name: {tool_sha, tags}}, module_sha256: {file: sha}}. Holds hashes, never text bodies.', '{"runtime": {"tool_timeout_s": 90, "agent_timeout_s": 750, ...}, "agents": {...}, "tools": {...}}', 'JSON object.', NULL, NULL),
('configs', 'label', NULL, 'free_text', 'human', 'Optional human name for the configuration.', 'NULL', 'Free text; nullable.', NULL, NULL),
('configs', 'notes', NULL, 'free_text', 'code', 'How the snapshot was obtained, when that needs saying (e.g. which overrides an inferred config applied).', 'override deep_agent_factory._AGENT_TIMEOUT_S=600 from a TimeoutError at 600.5s', 'Free text; nullable.', NULL, NULL),
('configs', 'created_at', NULL, 'timestamp', 'database', 'When the row was first stored. Not when the config took effect: the backfill stores old configs late.', '2026-10-11 10:00:00+00', 'UTC timestamp; set once.', NULL, NULL),
('configs', 'updated_at', NULL, 'timestamp', 'database', 'When the observation metadata was last changed.', '2026-10-11 10:00:00+00', 'UTC timestamp; maintained by trigger.', NULL, NULL),

-- ── hparams.texts ────────────────────────────────────────────────────────────
('texts', 'text_sha', 'PK', 'hash', 'code', 'SHA-256 of body as UTF-8, enforced by a CHECK. Same convention as loader.prompt_sha256, so a raw prompt''s hash equals eval.rubrics.source_prompt_sha256.', '71c92f6cf7cb…', '64 hex characters.', NULL, NULL),
('texts', 'body', NULL, 'free_text', 'code', 'The text, with line endings normalised to LF.', '# Value Researcher …; \n\n## Your Execution Budget …', 'Roughly 1,500–9,000 characters.', NULL, NULL),
('texts', 'chars', NULL, 'count', 'database', 'Length of body in characters (generated).', '5213', '≥ 1.', NULL, NULL),
('texts', 'created_at', NULL, 'timestamp', 'database', 'When the text was first stored.', '2026-10-11 10:00:00+00', 'UTC timestamp.', NULL, NULL),

-- ── hparams.config_runtime ───────────────────────────────────────────────────
('config_runtime', 'config_sha', 'PK, FK → hparams.configs.config_sha', 'hash', 'code', 'Configuration these limits belong to.', '22b40e62dabf…', 'Must exist in hparams.configs.', NULL, NULL),
('config_runtime', 'tool_timeout_s', NULL, 'continuous', 'code', 'Wall-clock ceiling on one tool call (langchain_bridge._TOOL_TIMEOUT_S). A call past it returns "timed out, proceed without this data" to the agent.', '90', 'Seconds > 0.',
 '{"high": "Slow feeds get more time; a dead API costs the agent more of its own budget", "low": "Slow feeds (FMP news, SEC EDGAR) start returning nothing"}', NULL),
('config_runtime', 'max_tool_threads', NULL, 'count', 'code', 'Size of the worker pool that runs blocking tool calls off the event loop (langchain_bridge._MAX_TOOL_THREADS).', '48', 'Integer > 0.',
 '{"high": "Many specialists can call tools at once", "low": "Concurrent tool calls queue; the parallel fan-out is re-serialised"}', NULL),
('config_runtime', 'specialist_max_tokens', NULL, 'count', 'code', 'Output-token ceiling for the 11 specialists and the portfolio strategist (deep_agent_factory._SPECIALIST_MAX_TOKENS).', '8096', 'Tokens > 0.', NULL, NULL),
('config_runtime', 'memo_max_tokens', NULL, 'count', 'code', 'Output-token ceiling for the head of research memo (_MEMO_MAX_TOKENS).', '16000', 'Tokens > 0.', NULL, NULL),
('config_runtime', 'specialist_recursion_limit', NULL, 'count', 'code', 'LangGraph super-step ceiling for a specialist (_SPECIALIST_RECURSION_LIMIT). R steps allow (R−1)/2 rounds of tool calls.', '30', 'Integer > 0.', NULL, NULL),
('config_runtime', 'master_recursion_limit', NULL, 'count', 'code', 'LangGraph super-step ceiling for the head of research (_MASTER_RECURSION_LIMIT).', '15', 'Integer > 0.', NULL, NULL),
('config_runtime', 'agent_timeout_s', NULL, 'continuous', 'code', 'Wall-clock ceiling on one agent (_AGENT_TIMEOUT_S). An agent past it contributes an empty report.', '750; 900 (before 2026-09-27)', 'Seconds > 0.',
 '{"high": "Agents rarely time out; a hung one holds the run longer", "low": "Thorough agents are cut off and lose their whole report"}', NULL),
('config_runtime', 'default_max_concurrency', NULL, 'count', 'code', 'Specialists run at once unless --max-concurrency says otherwise (_DEFAULT_MAX_CONCURRENCY). The value a run actually used is run_configs.max_concurrency.', '6', 'Integer > 0.', NULL, NULL),
('config_runtime', 'advertised_fraction', NULL, 'continuous', 'code', 'Share of the real step and time ceilings that the execution-budget block quotes to the model, so an agent pacing itself to the quoted limit finishes with margin.', '0.75', '0–1.', NULL, NULL),
('config_runtime', 'request_timeout_ms', NULL, 'count', 'code', 'HTTP timeout passed to the OpenRouter chat model (roles.REQUEST_TIMEOUT_MS).', '600000', 'Milliseconds; NULL if the model was not built through chat_model_for_role.', NULL, NULL),
('config_runtime', 'streaming', NULL, 'boolean', 'code', 'Whether chat models stream. Streaming keeps bytes flowing so OpenRouter''s edge does not drop long-held sockets.', 'true', 'true | false | NULL', '{"true": "Streamed transport", "false": "One long-held POST per completion"}', NULL),
('config_runtime', 'provider_routing', NULL, 'json', 'code', 'OpenRouter provider routing passed with every request (roles._PROVIDER_ROUTING).', '{"ignore": ["azure"]}', 'JSON object; NULL when not routed through OpenRouter.', NULL, NULL),
('config_runtime', 'default_model', NULL, 'categorical', 'code', 'OpenRouter slug every role uses unless overridden (roles.DEFAULT_MODEL).', 'deepseek/deepseek-v4-flash-0731', 'Any OpenRouter model slug.', NULL, NULL),
('config_runtime', 'agent_model_overrides', NULL, 'json', 'code', 'Per-role model overrides (roles.AGENT_MODELS).', '{}', 'Object role → slug; empty = every role on default_model.', NULL, NULL),
('config_runtime', 'budget_template_sha', 'FK → hparams.texts.text_sha', 'hash', 'code', 'The prompts/_execution_budget.md template the budget blocks are rendered from.', 'c740b6e5be54…', '64 hex characters; NULL when the template did not exist.', NULL, NULL),
('config_runtime', 'extra', NULL, 'json', 'code', 'Other limits that shape tool behaviour: the FMP client''s timeout, cache TTL and size, retry attempts, backoff and retried statuses.', '{"fmp._TIMEOUT": 45, "fmp._DEFAULT_TTL": 900, "fmp._CACHE_MAX": 512, "fmp._RETRY_STATUS": [429, 500, 502, 503, 504]}', 'JSON object; keys are <module>.<CONSTANT>.', NULL, NULL),

-- ── hparams.config_agents ────────────────────────────────────────────────────
('config_agents', 'config_sha', 'PK, FK → hparams.configs.config_sha', 'hash', 'code', 'Configuration this agent row belongs to.', '22b40e62dabf…', 'Must exist in hparams.configs.', NULL, NULL),
('config_agents', 'role', 'PK', 'categorical', 'code', 'Agent role.', 'value_researcher', 'One of the 13 agent roles.', (SELECT j FROM roles), NULL),
('config_agents', 'stage', NULL, 'ordinal', 'code', 'Which step of the run the agent belongs to.', '1', '1 | 2 | 3',
 '{"1": "Specialist fan-out, run concurrently", "2": "Portfolio strategist, reads the specialist reports", "3": "Head of research, writes the memo"}', NULL),
('config_agents', 'agent_kind', NULL, 'categorical', 'code', 'Which builder the agent goes through.', 'react_specialist', 'react_specialist | deep_master',
 '{"react_specialist": "LangGraph create_react_agent: one tool loop, no planning tools", "deep_master": "deepagents create_deep_agent with no subagents; deepagents injects planning and filesystem tools that are not in composed_prompt"}', NULL),
('config_agents', 'model_slug', NULL, 'categorical', 'code', 'OpenRouter slug the role runs on (AGENT_MODELS, else DEFAULT_MODEL).', 'deepseek/deepseek-v4-flash-0731', 'Any OpenRouter model slug.', NULL, NULL),
('config_agents', 'model_spec', NULL, 'categorical', 'code', 'The LangChain spec actually passed to init_chat_model.', 'openrouter:deepseek/deepseek-v4-flash-0731', '<provider>:<model>; NULL if not captured.', NULL, NULL),
('config_agents', 'max_tokens', NULL, 'count', 'code', 'Output-token ceiling the model was built with.', '8096; 16000 (head_of_research)', 'Tokens > 0.', NULL, NULL),
('config_agents', 'recursion_limit', NULL, 'count', 'code', 'LangGraph super-step ceiling the agent is invoked with.', '30; 15 (head_of_research)', 'Integer > 0.', NULL, NULL),
('config_agents', 'advertised_recursion_limit', NULL, 'count', 'code', 'The step ceiling the budget block is computed from: max(3, int(recursion_limit × advertised_fraction)).', '22; 11', 'Integer ≥ 3; NULL without a budget block.', NULL, NULL),
('config_agents', 'advertised_tool_rounds', NULL, 'count', 'code', 'Rounds of tool calls the budget block tells the agent it has.', '10; 5', 'Integer ≥ 1; NULL without a budget block.', NULL, NULL),
('config_agents', 'advertised_write_by', NULL, 'count', 'code', 'Round by which the budget block tells the agent to be writing its report.', '8; 3', 'Integer ≥ 1; NULL without a budget block.', NULL, NULL),
('config_agents', 'advertised_timeout_s', NULL, 'continuous', 'code', 'Wall-clock budget the block tells the agent it has (shown to the model rounded to whole seconds).', '562.5', 'Seconds; NULL without a budget block.', NULL, NULL),
('config_agents', 'task', NULL, 'free_text', 'code', 'The task line in the agent''s user message. For head_of_research, a run''s --focus is appended per run (run_configs.extra_instructions).', 'Conduct a thorough value investment analysis.; Produce the final Investment Memo.', 'Free text; NULL if it could not be read.', NULL, NULL),
('config_agents', 'prompt_source', NULL, 'categorical', 'code', 'Where the role prompt came from.', 'file', 'file | fallback',
 '{"file": "prompts/<role>.md", "fallback": "The file was missing, so a one-line generic prompt was used"}', NULL),
('config_agents', 'system_prompt_sha', 'FK → hparams.texts.text_sha', 'hash', 'code', 'The raw role prompt (prompts/<role>.md). Joins to eval.rubrics.source_prompt_sha256.', '71c92f6cf7cb…', '64 hex characters.', NULL, NULL),
('config_agents', 'budget_sha', 'FK → hparams.texts.text_sha', 'hash', 'code', 'The execution-budget block appended to the prompt, as rendered for this role''s limits.', '3f0a…', '64 hex characters; NULL when no block was rendered.', NULL, NULL),
('config_agents', 'composed_prompt_sha', 'FK → hparams.texts.text_sha', 'hash', 'code', 'The exact system prompt the agent was built with, captured from the builder: system prompt + budget block.', '9be1…', '64 hex characters.', NULL, NULL),
('config_agents', 'tool_count', NULL, 'count', 'code', 'Number of tools the role holds.', '22; 6 (head_of_research)', 'Matches tests/test_tool_access.py EXPECTED_COUNTS; 204 across the 13 roles.', NULL, NULL),
('config_agents', 'agent_sha', NULL, 'hash', 'code', 'Hash of this role''s whole config including its tools'' definitions. Equal across configs means the agent itself did not change.', 'e1d2…', '64 hex characters.', NULL, NULL),

-- ── hparams.tool_defs ────────────────────────────────────────────────────────
('tool_defs', 'tool_sha', 'PK', 'hash', 'code', 'SHA-256 of {tool_name, module, description, input_schema, impl_sha256}. Tags are excluded, so retagging a tool reuses its definition.', '5d1c…', '64 hex characters.', NULL, NULL),
('tool_defs', 'tool_name', NULL, 'identifier', 'code', 'MCP tool name.', 'calculate_intrinsic_value_dcf', 'One of the tools registered in server.py.', NULL, NULL),
('tool_defs', 'module', NULL, 'identifier', 'code', 'Python module that implements the tool.', 'equity_mcp.tools.calculations.valuation', 'Dotted module path; NULL if the function was not found.', NULL, NULL),
('tool_defs', 'description', NULL, 'free_text', 'code', 'The description the agent sees (the function docstring as FastMCP renders it).', 'Discounted cash flow intrinsic value …', 'Free text.', NULL, NULL),
('tool_defs', 'input_schema', NULL, 'json', 'code', 'The JSON schema of the tool''s arguments as FastMCP renders it. Rendering depends on the installed FastMCP version (configs.libs).', '{"type": "object", "properties": {"symbol": {"type": "string"}}, "required": ["symbol"]}', 'JSON schema object.', NULL, NULL),
('tool_defs', 'impl_sha256', NULL, 'hash', 'code', 'Hash of the implementing function''s source. Catches behaviour changes the description and schema do not show; helpers it calls are covered by configs.content.module_sha256.', 'a8f0…', '64 hex characters; NULL if the source was unavailable.', NULL, NULL),
('tool_defs', 'created_at', NULL, 'timestamp', 'database', 'When the definition was first stored.', '2026-10-11 10:00:00+00', 'UTC timestamp.', NULL, NULL),

-- ── hparams.config_tools ─────────────────────────────────────────────────────
('config_tools', 'config_sha', 'PK, FK → hparams.configs.config_sha', 'hash', 'code', 'Configuration the tool is registered in.', '22b40e62dabf…', 'Must exist in hparams.configs.', NULL, NULL),
('config_tools', 'tool_name', 'PK', 'identifier', 'code', 'MCP tool name.', 'get_income_statement', '61 tools per configuration as of 2026-10-11.', NULL, NULL),
('config_tools', 'tool_sha', 'FK → hparams.tool_defs.tool_sha', 'hash', 'code', 'Definition the tool had in this configuration.', '5d1c…', 'Must exist in hparams.tool_defs.', NULL, NULL),
('config_tools', 'tags', NULL, 'list', 'code', 'FastMCP tags on the tool: role names, or shared. A role holds the tool if its own name or shared is present.', '{growth_researcher,portfolio_strategist,quant_analyst,value_researcher}; {shared}', 'Sorted array of role names and/or shared.', NULL, NULL),

-- ── hparams.config_role_tools ────────────────────────────────────────────────
('config_role_tools', 'config_sha', 'PK, FK → hparams.config_agents', 'hash', 'code', 'Configuration the grant belongs to.', '22b40e62dabf…', 'Must exist in hparams.config_agents with role.', NULL, NULL),
('config_role_tools', 'role', 'PK', 'categorical', 'code', 'Agent role that holds the tool.', 'quant_analyst', 'One of the 13 agent roles.', (SELECT j FROM roles), NULL),
('config_role_tools', 'tool_name', 'PK, FK → hparams.config_tools', 'identifier', 'code', 'Tool the role holds.', 'rank_universe_by_factor', 'Must exist in hparams.config_tools for the same configuration.', NULL, NULL),
('config_role_tools', 'via', NULL, 'categorical', 'code', 'Which tag granted the tool.', 'role; shared', 'role | shared',
 '{"role": "The tool is tagged with this role''s own name", "shared": "The tool is tagged shared and reaches every role"}', NULL),

-- ── hparams.run_configs ──────────────────────────────────────────────────────
('run_configs', 'run_id', 'PK, FK → eval.runs.run_id', 'identifier', 'pipeline', 'Research run.', 'AVGO_20261003T135110', 'Must exist in eval.runs.', NULL, NULL),
('run_configs', 'config_sha', 'FK → hparams.configs.config_sha', 'hash', 'code', 'Configuration the run used.', '22b40e62dabf…', 'Must exist in hparams.configs.', NULL, NULL),
('run_configs', 'link_basis', NULL, 'categorical', 'code', 'How the run was tied to the config. A link is only ever replaced by one at least as well founded.', 'recorded_in_run; git_checkout; inferred', 'recorded_in_run | prompt_sha_match | git_checkout | inferred',
 '{"recorded_in_run": "The run captured its own config (runs/<id>/config.json): exact", "prompt_sha_match": "Reconstructed from git and confirmed by the prompt hashes the run recorded", "git_checkout": "The run''s commit is unambiguous (CI, or every candidate commit has the same code): exact for committed code", "inferred": "Local run on an uncommitted tree; the nearest commit, adjusted by run evidence such as a timeout at a telling elapsed time"}', NULL),
('run_configs', 'research_git_sha', NULL, 'hash', 'code', 'Commit the run is believed to have run on. Unlike eval.runs.git_sha, which is the commit at evaluation time.', 'b33c180a…', '40 hex characters; NULL if unknown.', NULL, NULL),
('run_configs', 'max_concurrency', NULL, 'count', 'pipeline', 'Specialists the run allowed at once (--max-concurrency, else the default).', '6; 2', 'Integer > 0; NULL if unrecorded.', NULL, NULL),
('run_configs', 'run_timeout_s', NULL, 'continuous', 'pipeline', 'Whole-run ceiling (--timeout).', 'NULL; 900', 'Seconds; NULL = unbounded or unrecorded.', NULL, NULL),
('run_configs', 'agents_requested', NULL, 'list', 'pipeline', 'Specialists requested with --agents.', 'NULL; {macro_researcher,esg_analyst}', 'NULL = all 11 specialists.', NULL, NULL),
('run_configs', 'extra_instructions', NULL, 'free_text', 'pipeline', 'The run''s --focus text, appended to the head of research task.', '''''; NULL', 'Empty string = none given; NULL = not recorded (older local runs).', NULL, NULL),
('run_configs', 'overrides', NULL, 'json', 'code', 'Run-level deviations from the config''s code defaults, when known, e.g. skip_synthesis, or the overrides an inferred config applied.', '{"skip_synthesis": false}; {"deep_agent_factory._AGENT_TIMEOUT_S": 600}', 'JSON object; empty = none.', NULL, NULL),
('run_configs', 'notes', NULL, 'free_text', 'code', 'Evidence behind the link: candidate commits, fingerprints and anything ambiguous.', 'local run; candidates cb0a21f,b33c180 differ; chose b33c180', 'Free text; nullable.', NULL, NULL),
('run_configs', 'linked_at', NULL, 'timestamp', 'database', 'When the run was first linked.', '2026-10-11 10:00:00+00', 'UTC timestamp.', NULL, NULL),
('run_configs', 'updated_at', NULL, 'timestamp', 'database', 'When the link was last replaced.', '2026-10-11 10:00:00+00', 'UTC timestamp; maintained by trigger.', NULL, NULL),

-- ── view-only columns ────────────────────────────────────────────────────────
('v_config_history', 'previous_config_sha', NULL, 'hash', 'view', 'The snapshot that took effect immediately before this one.', 'NULL (first); 22b40e62dabf…', '64 hex characters; NULL for the first.', NULL, NULL),
('v_config_history', 'n_runs', NULL, 'count', 'view', 'Runs linked to this snapshot.', '25', '≥ 0; 0 for a config only ever synced.', NULL, NULL),
('v_config_agents', 'composed_chars', NULL, 'count', 'view', 'Length of the composed prompt.', '6402', '≥ 1.', NULL, NULL),
('v_config_agents', 'agent_unchanged_since', NULL, 'timestamp', 'view', 'Earliest effective_at of any snapshot whose config for this role (agent_sha) is identical: how long the agent has been as it is.', '2026-09-27 01:28:23+00', 'UTC timestamp.', NULL, NULL),
('v_config_access_wide', 'n_roles', NULL, 'count', 'view', 'Roles that hold the tool.', '13 (shared); 1', '0–13.', NULL, NULL),
('v_config_access_counts', 'n_tools', NULL, 'count', 'view', 'Tools the role holds.', '25', '≥ 0.', NULL, NULL),
('v_config_access_counts', 'n_shared', NULL, 'count', 'view', 'Of n_tools, those granted by the shared tag.', '6', '≥ 0.', NULL, NULL),
('v_config_access_counts', 'n_role_tagged', NULL, 'count', 'view', 'Of n_tools, those granted by the role''s own tag.', '19', '≥ 0.', NULL, NULL),
('v_run_configs', 'config_effective_at', NULL, 'timestamp', 'view', 'configs.effective_at of the linked configuration.', '2026-09-27 01:28:23+00', 'UTC timestamp; NULL when unlinked.', NULL, 'hparams.configs.effective_at'),
('v_run_configs', 'concurrency_overridden', NULL, 'boolean', 'view', 'Whether the run''s max_concurrency differs from the config''s default.', 'false', 'true | false',
 '{"true": "The run was started with --max-concurrency other than the default", "false": "Default concurrency, or nothing recorded"}', NULL),
('v_run_agent_config', 'output_agent_model', NULL, 'categorical', 'view', 'eval.agent_outputs.agent_model: the model recorded with the agent''s output (possibly inferred).', 'deepseek/deepseek-v4-flash-0731', 'OpenRouter slug; NULL when the output is absent.', NULL, 'eval.agent_outputs.agent_model'),
('v_run_agent_config', 'model_mismatch', NULL, 'boolean', 'view', 'Whether the output''s recorded model differs from the model the linked config says the role runs on.', 'false', 'true | false',
 '{"true": "The two disagree: check agent_model_inferred and the link_basis", "false": "They agree, or one is unknown"}', NULL),
('v_config_integrity', 'issue', NULL, 'categorical', 'view', 'What is inconsistent.', 'composed prompt is not system prompt + budget block', 'composed prompt is not system prompt + budget block | access row missing for a tag that grants it | access row not justified by the tool''s tags | tool_count differs from access rows | config has no runtime row | config agents differ from content | config tools differ from content', NULL, NULL)
),
live AS (
    SELECT cl.relname AS table_name, a.attname AS column_name, a.attnum AS ordinal_position,
           format_type(a.atttypid, a.atttypmod) AS data_type, NOT a.attnotnull AS is_nullable
    FROM pg_attribute a
    JOIN pg_class cl    ON cl.oid = a.attrelid
    JOIN pg_namespace n ON n.oid = cl.relnamespace
    WHERE n.nspname = 'hparams' AND cl.relkind IN ('r', 'v') AND a.attnum > 0 AND NOT a.attisdropped
)
INSERT INTO datadict.columns (schema_name, table_name, column_name, ordinal_position, data_type, is_nullable,
                              key_role, value_kind, source, definition, example_values, value_range, value_meanings,
                              derived_from, created_date)
SELECT 'hparams', d.table_name, d.column_name, l.ordinal_position, l.data_type, l.is_nullable,
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
-- 3. is_current, on every view that has it, and the 13 role columns of v_config_access_wide
-- -----------------------------------------------------------------------------
INSERT INTO datadict.columns (schema_name, table_name, column_name, ordinal_position, data_type, is_nullable,
                              key_role, value_kind, source, definition, example_values, value_range, value_meanings,
                              derived_from, created_date)
SELECT 'hparams', cl.relname, a.attname, a.attnum, format_type(a.atttypid, a.atttypmod), true,
       NULL, 'boolean', 'view',
       CASE WHEN a.attname = 'is_current'
            THEN 'Whether this row belongs to the configuration in force now (the one hparams.v_config_current picks).'
            ELSE 'Whether the ' || a.attname || ' agent holds this tool in this configuration.' END,
       CASE WHEN a.attname = 'is_current' THEN 'true; false' ELSE 'true (shared tools); false' END,
       'true | false',
       CASE WHEN a.attname = 'is_current'
            THEN '{"true": "Today''s configuration", "false": "A past (or merely inferred) configuration"}'::jsonb
            ELSE '{"true": "The role is given the tool", "false": "The role never sees the tool"}'::jsonb END,
       NULL, DATE '2026-10-11'
FROM pg_attribute a
JOIN pg_class cl    ON cl.oid = a.attrelid
JOIN pg_namespace n ON n.oid = cl.relnamespace
WHERE n.nspname = 'hparams' AND cl.relkind = 'v' AND a.attnum > 0 AND NOT a.attisdropped
  AND (a.attname = 'is_current'
       OR (cl.relname = 'v_config_access_wide'
           AND a.attname IN ('sector_researcher', 'geo_legal_researcher', 'macro_researcher', 'value_researcher',
                             'growth_researcher', 'fin_risk_analyst', 'nonfin_risk_analyst', 'quant_analyst',
                             'short_analyst', 'esg_analyst', 'alt_data_analyst', 'portfolio_strategist',
                             'head_of_research')))
ON CONFLICT (schema_name, table_name, column_name) DO UPDATE SET
    ordinal_position = EXCLUDED.ordinal_position, data_type = EXCLUDED.data_type,
    definition = EXCLUDED.definition, example_values = EXCLUDED.example_values, value_range = EXCLUDED.value_range,
    value_meanings = EXCLUDED.value_meanings;

-- -----------------------------------------------------------------------------
-- 4. Pass-through view columns: derived_from the first listed source that has a
--    column of the same name. They inherit documentation in v_data_dictionary.
-- -----------------------------------------------------------------------------
WITH src(view_name, prio, source_schema, source_table) AS (VALUES
    ('v_config_current',       1, 'hparams', 'configs'),
    ('v_config_history',       1, 'hparams', 'configs'),
    ('v_config_agents',        1, 'hparams', 'config_agents'),     ('v_config_agents',      2, 'hparams', 'configs'),
    ('v_config_tools',         1, 'hparams', 'config_tools'),      ('v_config_tools',       2, 'hparams', 'tool_defs'),
    ('v_config_access_long',   1, 'hparams', 'config_role_tools'), ('v_config_access_long', 2, 'hparams', 'tool_defs'),
    ('v_config_access_wide',   1, 'hparams', 'config_tools'),      ('v_config_access_wide', 2, 'hparams', 'tool_defs'),
    ('v_config_access_counts', 1, 'hparams', 'config_role_tools'),
    ('v_run_configs',          1, 'eval',    'runs'),              ('v_run_configs',        2, 'hparams', 'run_configs'),
    ('v_run_configs',          3, 'hparams', 'configs'),           ('v_run_configs',        4, 'hparams', 'config_runtime'),
    ('v_run_agent_config',     1, 'hparams', 'run_configs'),       ('v_run_agent_config',   2, 'eval',    'runs'),
    ('v_run_agent_config',     3, 'hparams', 'config_agents'),     ('v_run_agent_config',   4, 'eval',    'agent_outputs'),
    ('v_config_integrity',     1, 'hparams', 'config_role_tools')
),
live AS (
    SELECT cl.relname AS table_name, a.attname AS column_name, a.attnum AS ordinal_position,
           format_type(a.atttypid, a.atttypmod) AS data_type
    FROM pg_attribute a
    JOIN pg_class cl    ON cl.oid = a.attrelid
    JOIN pg_namespace n ON n.oid = cl.relnamespace
    WHERE n.nspname = 'hparams' AND cl.relkind = 'v' AND a.attnum > 0 AND NOT a.attisdropped
),
pick AS (
    SELECT DISTINCT ON (l.table_name, l.column_name)
           l.table_name, l.column_name, l.ordinal_position, l.data_type,
           s.value_kind, s.source, src.source_schema || '.' || s.table_name || '.' || s.column_name AS derived_from
    FROM live l
    JOIN src ON src.view_name = l.table_name
    JOIN datadict.columns s ON s.schema_name = src.source_schema AND s.table_name = src.source_table
                           AND s.column_name = l.column_name
    WHERE NOT EXISTS (SELECT 1 FROM datadict.columns x
                      WHERE x.schema_name = 'hparams' AND x.table_name = l.table_name AND x.column_name = l.column_name
                        AND x.definition IS NOT NULL)
    ORDER BY l.table_name, l.column_name, src.prio
)
INSERT INTO datadict.columns (schema_name, table_name, column_name, ordinal_position, data_type, is_nullable,
                              key_role, value_kind, source, derived_from, created_date)
SELECT 'hparams', table_name, column_name, ordinal_position, data_type, true, NULL, value_kind, source, derived_from,
       DATE '2026-10-11'
FROM pick
ON CONFLICT (schema_name, table_name, column_name) DO UPDATE SET
    ordinal_position = EXCLUDED.ordinal_position, data_type = EXCLUDED.data_type,
    value_kind = EXCLUDED.value_kind, source = EXCLUDED.source, derived_from = EXCLUDED.derived_from;
