# How a config change reaches the `hparams` schema in Supabase

Recorded 2026-10-18. Line numbers are as of commit `e5e7bc7`. If they have moved, search for the function name.

## Short answer
**A commit writes nothing to Supabase.** `hparams` rows are written only when a run is ingested.
This covers changes to prompts, tools, models (`DEFAULT_MODEL` / `AGENT_MODELS` in `roles.py`) and execution budgets.

All four change `config_sha`, the sha256 of a canonical JSON of the config. That JSON covers:
- prompt text,
- tool defs, tags and impl hash,
- role→tool access,
- models,
- `max_tokens`, recursion limits and timeouts,
- the file hashes of `roles.py`, `deep_agent_factory.py`, `langchain_bridge.py`, `server.py` and `tools/**`.

A new `config_sha` produces new rows. An already-stored one only widens `last_seen_at`.

## Ways to get a change into Supabase
`SUPABASE_EVAL_DB_URL` must be set in `.env` for every option.

| Goal | Command | Notes |
|---|---|---|
| Register the config with no run | `python -m equity_mcp.hparams sync --current [--dry-run] [--label "..."]` | No Jev or OpenRouter cost. From a clean tree, provenance is `reconstructed_from_git`; from a dirty tree, `inferred`. Commit first if you can. |
| Register it together with a run | `python -m equity_mcp.orchestrator --symbol X --evaluate` | Also needs `TYPESAFE_API_KEY`. Provenance is `captured_at_runtime`, and the run is linked as `recorded_in_run`. |
| A run that finished without `--evaluate` | `python -m equity_mcp.evaluation.evaluate --symbol X --latest` | Goes the same route as `--evaluate`, from `evaluate_result` on. |
| Replay parked payloads | `python -m equity_mcp.hparams sync --flush-pending` | Replays `evals/pending_hparams/`. |
| Check | `python -m equity_mcp.hparams verify --db` | Or SQL: `SELECT role, model_slug FROM hparams.config_agents WHERE config_sha = '<sha>'`. |

**Trap:** `hparams sync --from-run-dir runs/<id>` fails for a run that was never evaluated.
- `hparams.run_configs.run_id` references `eval.runs` (FK at `supabase/migrations/20261011000200_hparams_schema.sql:228`).
- Only an evaluation creates that `eval.runs` row.
- Without it, the whole transaction rolls back, config row included, and the payload is parked in `evals/pending_hparams/`.

**CI today writes no hparams rows.** A push to `main` runs `.github/workflows/equity-research.yml`.
- Its eval step exits early while `TYPESAFE_API_KEY` is unset. Adding the secret is still on hold.
- With the key but no `SUPABASE_EVAL_DB_URL`, the payload lands in the runner's `evals/`. That folder is not committed, so the payload is lost.

## Option B call chain (`orchestrator --evaluate`)

**Stage 1: run start, no DB**
1. `orchestrator.py:364` defines `--evaluate` (or `EQR_EVALUATE=1`). Line 381 passes it into `run()`.
2. `orchestrator.py:106-112` calls `capture_config(run_log, run_params)`. This happens **before** the fan-out, because the snapshot briefly stubs the agent builders.
3. `hparams/capture.py:45-67` `capture_config` → `build_snapshot(provenance="captured_at_runtime", source_git_sha, source_git_dirty)`.
4. `run_log.py:118-125` `RunLog.config` writes `runs/<id>/config.json`. `orchestrator.py:156` puts `config_sha` in the result.

**Stage 2: after the agents, which is the trigger**

5. `orchestrator.py:181-182`: `if evaluate: await _evaluate_run(result, out_file, run_log)`.
6. `orchestrator.py:206-229` `_evaluate_run` → `evaluate_result(...)` under a **900 s** `wait_for`. Every error becomes one `EVAL FAILED` line in run.log.
7. `evaluation/evaluate.py:338` → `store.py:430-434` `make_store`. The result is a `SupabaseStore` if `SUPABASE_EVAL_DB_URL` is set, else a `LocalStore`.
8. `evaluate.py:401` `async with store, runner:` opens the DB connection (`store.py:172`) and the Jev client.
9. `evaluate.py:370-390` scores each role. `store.py:380` `_save` upserts the `eval.runs` row.
10. `evaluate.py:395-398`: `ingest_run(store, result)` is the hparams trigger. It runs after the roles because of the FK, and outside their transactions.

**Stage 3: hparams write**

11. `hparams/ingest.py:167-185` `ingest_run` → `load_run_config` (line 152) → `payload_from_run_config` (line 160, `link_basis="recorded_in_run"`).
12. `store.py:353-371` `save_hparams` → line 373 `_save_hparams`, **one transaction**.
13. `hparams/ingest.py:100-134` `write`, in order:
    1. `_CONFIG_UPSERT` (line 62) into `hparams.configs`. `RETURNING (xmax = 0)` tells whether the config is new.
    2. Only if new: insert `texts`, `tool_defs`, `config_runtime`, `config_agents`, `config_tools` and `config_role_tools`, all `ON CONFLICT DO NOTHING`.
    3. `_LINK_UPSERT` (line 81) into `hparams.run_configs`. It replaces an existing link only when the new `link_basis` ranks at least as high.

## Dependencies and failure modes

| Dependency | Where | If missing or failing |
|---|---|---|
| `SUPABASE_EVAL_DB_URL` | `store.py:430` | `LocalStore` writes `evals/results/hparams/`. This is **not** the pending folder, so `--flush-pending` won't replay it. |
| DB reachable | `store.py:172-180` | Payload is parked in `evals/pending_hparams/`; replay with `hparams sync --flush-pending`. |
| `TYPESAFE_API_KEY` | `evaluation/jev.py:186` (`FatalJevError`) | Fails at `evaluate.py:401`, before step 10, so no hparams write at all. |
| `eval.runs` row | FK, `hparams_schema.sql:228` | Transaction rolls back, config included. |
| `runs/<id>/config.json` | step 4 | `CONFIG FAILED` in run.log → `ingest_run` returns None. |
| Eval finishes within 900 s | `orchestrator.py:217` | Ingest never runs; recover with `evaluate --symbol X --latest`. |

**The snapshot reflects the code at run start (step 3), not the last commit.** If you edit `roles.py` mid-run, that run still records the old model.
