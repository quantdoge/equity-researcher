# Reading the `hparams` schema

The `hparams` schema records which configuration produced each research run. A configuration covers:
- runtime limits
- each agent's model, budget, task and exact prompts
- tool access

Every view below has an `is_current` column, which is true for the config `hparams.v_config_current` picks.

## Today's configuration

```sql
-- Per-agent settings in force now
SELECT role, stage, agent_kind, model_slug, max_tokens, recursion_limit,
       advertised_tool_rounds, advertised_write_by, advertised_timeout_s, tool_count, task
FROM hparams.v_config_agents WHERE is_current ORDER BY stage, role;

-- Runtime limits in force now
SELECT rt.* FROM hparams.config_runtime rt JOIN hparams.v_config_current c USING (config_sha);

-- Tool access grid
SELECT * FROM hparams.v_config_access_wide WHERE is_current ORDER BY n_roles DESC, tool_name;
```

## A prompt's text

```sql
SELECT g.role, t.chars, t.body
FROM hparams.v_config_agents g JOIN hparams.texts t ON t.text_sha = g.composed_prompt_sha
WHERE g.is_current AND g.role = 'value_researcher';
```

To see only the role prompt, join on `system_prompt_sha`. To see only the execution-budget block, join on `budget_sha`.

## What changed between two configs

```sql
SELECT config_sha, previous_config_sha, effective_at, n_runs FROM hparams.v_config_history ORDER BY effective_at;
SELECT * FROM hparams.config_diff('<previous_config_sha>', '<config_sha>');
```

`config_diff` returns one row per differing field. Its facets are runtime, agent, tool, access and module. A prompt edit shows up as a changed `*_prompt_sha`.

## Scores by configuration

```sql
SELECT rc.config_sha, e.role, count(*) AS n, avg(e.alignment_composite) AS alignment, avg(e.stance_expected) AS stance
FROM hparams.run_configs rc
JOIN eval.v_latest_evaluations e USING (run_id)
GROUP BY 1, 2 ORDER BY 2, 1;
```

## How each run was linked

```sql
SELECT run_id, config_sha, link_basis, research_git_sha, max_concurrency, run_timeout_s,
       agents_requested, concurrency_overridden, notes
FROM hparams.v_run_configs ORDER BY run_id;
```

`link_basis` says how well founded the link is:

| link_basis | Meaning |
|---|---|
| `recorded_in_run` | The run captured its own config. Exact. |
| `git_checkout` | The run is a CI run, or every candidate commit had the same code. Exact for committed code. |
| `inferred` | The run was local, on an uncommitted tree. The link is the nearest commit, adjusted by run evidence. |

## Health checks (all must return 0 rows)

```sql
SELECT * FROM hparams.v_config_integrity;
SELECT * FROM datadict.v_coverage_gaps WHERE schema_name = 'hparams';
SELECT run_id FROM hparams.v_run_configs WHERE config_sha IS NULL AND skip_reason IS NULL;
```
