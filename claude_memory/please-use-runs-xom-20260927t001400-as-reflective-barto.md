# Plan: Per-ticker memory + pre-memo retry of timed-out specialists

## Context

`runs/XOM_20260927T001400` shows the problem. Six specialists (sector, macro, value, growth, fin_risk, nonfin_risk) all failed in the same second with `ReadTimeout` after about 717s. Their reports on disk are empty: `_run_one_agent` catches the exception and returns `output=""`, so twelve minutes of tool calls per agent are lost. Only geo_legal finished (100s). The run then aborted (`CancelledError`) before quant, short, esg and alt_data ever ran.

Nothing carries over between runs of the same ticker. Nothing inside a run retries a failed agent. Every rerun starts from zero, and a transient stall loses an agent's work for good.

Goal:
1. Keep a durable memory per ticker, updated **while** agents run, not only when they finish.
2. Every run of a ticker reads that memory: all 11 specialists, the strategist and the Head of Research.
3. Before synthesis, rerun each specialist that failed on a timeout or a step limit, giving it everything its failed attempt gathered.

Decisions already made with you:
- Retry on timeouts **and** `GraphRecursionError`.
- On a rerun, every specialist runs again and uses memory as a head start. Reports are not reused just because they are fresh.
- Memory is written by automatic tool-result capture plus orchestrator-written reports. There is no LLM note tool, so memory costs no tool rounds.

## Memory layout (new, gitignored)

```
memory/<TICKER>/
    MEMORY.md                 # index: run history, per-role last status, latest memo view, known data gaps
    <role>.md                 # last SUCCESSFUL report for that role (run_id, date, elapsed in header)
    evidence/<role>.jsonl     # one line per tool call: ts, run_id, attempt, tool, args, ok, result (truncated)
```

- The `evidence/*.jsonl` files are appended on every tool call, and each line is opened, written and closed. Anything gathered up to a `ReadTimeout`, a `CancelledError` or a Ctrl-C therefore stays on disk. This is what "updated as the recursion goes" means here.
- A failed attempt never overwrites `<role>.md`. The last good report survives a bad run.

## Flow after the change

```
run start ─ TickerMemory(memory/XOM, run_id)  (trims evidence to last 3 runs)
1. fan-out: 11 specialists           prompt += memory.context_for(role, "prior")
     every tool call ─────────────►  evidence/<role>.jsonl   (auto)
     each finish     ─────────────►  <role>.md + MEMORY.md status row
1b. RETRY PASS (new): failed && retryable → rerun at half concurrency
                                     prompt += memory.context_for(role, "retry")
2. portfolio_strategist              prompt += memory.context_for_master()   (retried once if it times out)
3. head_of_research                  prompt += memory.context_for_master()
     memo done ───────────────────►  MEMORY.md "Latest view" + run-history row
```

The retry sits before the strategist, not just before the Head of Research, because the strategist also reads every report.

## Implementation

### 1. New `equity_mcp/memory.py`: `TickerMemory`
Follow `RunLog`'s contract in [run_log.py](equity_mcp/run_log.py): it never raises, it warns once to stderr, and it writes files with `encoding="utf-8"`.

- `__init__(root, symbol, run_id)`: `mkdir`, then trim each evidence file to its last 3 `run_id`s.
- `record_tool_call(role, attempt, tool, args, text)`: append one JSONL line. Guard it with a `threading.Lock`. Truncate `text` to about 8k characters. Set `ok=False` when the text starts with `Tool '...' failed` or `timed out` (the bridge's error strings).
- `record_result(result)`: on success, write `<role>.md`. In every case, update that role's row in the `MEMORY.md` status table.
- `record_memo(memo, portfolio_brief, run_id)`: write a "Latest view" section and a run-history row to `MEMORY.md`. The view is the memo's first ~3k characters (rating, target, thesis).
- `context_for(role, mode)` renders a character-capped block (~20k total, ~1.5k per evidence entry, newest first, deduplicated on `(tool, args)`):
  - `"prior"`: the role's last report with its age, plus evidence from earlier runs, filtered to a `_DURABLE_TOOLS` allowlist. Examples of durable tools: statements, `get_company_profile`, `get_sector_peers`, `fetch_company_facts`, `fetch_filing_text`, `get_dividends`, `get_sector_financials`, and the statement-based calculators such as Altman, Piotroski and Beneish. It also carries these instructions: reuse durable data under 7 days old without re-fetching; always re-fetch prices, news, estimates and macro data; explain any change from the prior conclusion.
  - `"retry"`: **all** evidence from this run's failed attempt(s), plus a header such as "your previous attempt timed out after 717s; these N calls already succeeded, don't repeat them; fill only the gaps; start writing by round X". Failed tool calls are listed separately so the agent does not hammer a dead tool again.
- `context_for_master()`: the `MEMORY.md` index plus the previous memo's view, so the memo can say what changed since the last view.
- The block is framed as data ("verify before relying"), matching how deepagents' own `MemoryMiddleware` frames memory.

### 2. Capture hook in [langchain_bridge.py](equity_mcp/langchain_bridge.py)
- Add `on_result: Callable[[str, dict, str], None] | None = None` to `get_langchain_tools_for_role` and pass it into `_make_async_caller`.
- In `_call`, invoke `on_result(tool_name, supplied, text)` on every exit path: success, the timeout text and the failure text. Wrap the call in `try/except`, because a memory fault must never fail a tool.
- The bridge stays memory-agnostic, since it only calls a callback. Tool access control is untouched.

### 3. [deep_agent_factory.py](equity_mcp/deep_agent_factory.py)
- `build_specialist_agent` and `build_head_agent` take `on_tool_result` and forward it to `get_langchain_tools_for_role`.
- `_run_one_agent` gains these parameters: `memory: TickerMemory | None`, `memory_context: str`, `attempt: int`, `timeout_s: float = _AGENT_TIMEOUT_S`.
  - `memory_context` goes into the **user message** under its own heading, separate from `extra_context`, and not into the system prompt. That keeps the system prompt identical from run to run.
  - It builds the capture callback as `lambda tool, args, text: memory.record_tool_call(role, attempt, tool, args, text)`.
  - The `except` adds `error_type` and `retryable` (via `_is_retryable(exc)`) and `attempt` to the result dict.
- `_is_retryable(exc)` is an `isinstance` check against `TimeoutError` (asyncio's `wait_for`), `httpx.TimeoutException` (covers ReadTimeout, ConnectTimeout, PoolTimeout and WriteTimeout), `openai.APITimeoutError` if importable, and `langgraph.errors.GraphRecursionError`.
- `run_specialists` accepts a `context_for: Callable[[str], str]` and `memory`, and passes both into `_run_one_agent`.
- New `retry_failed(results, ..., retries=1)`:
  - Select `r for r in results if r["error"] and r.get("retryable")`.
  - Rerun those with `attempt=2`, `memory_context=memory.context_for(role, "retry")` and concurrency `max(1, max_concurrency // 2)`. The XOM failures all landed in one second, which points to a shared stall; hitting it again at full width tends to repeat it.
  - Replace the entries in `results` and fire `on_complete` again, which overwrites `reports/<role>.md`.
- `run_research` takes a `memory` argument and does four things:
  - It calls `memory.record_result` inside the existing completion path, wrapping `on_agent_complete` so the CLI callback is unchanged.
  - It runs the retry pass between step 1 and step 2.
  - It retries the strategist once on a retryable error.
  - It calls `record_memo` after step 3.
- The result dict gains `"retried": [...]` and `"attempts": {role: n}`. `failures` then reflects the state **after** the retry.

### 4. [orchestrator.py](equity_mcp/orchestrator.py)
- New flags:
  - `--memory-dir` (default `memory/`)
  - `--no-memory` (read nothing, write nothing; this is the current behaviour)
  - `--retries` (default 1, and 0 disables the retry pass)
  - `--agent-timeout` (overrides `_AGENT_TIMEOUT_S`, mostly for forcing a timeout in tests)
- Build `TickerMemory(memory_dir, symbol, run_log.name)`, which shares the run's stamp, and pass it to `run_research`.
- Add a `RETRY  <role> attempt=2` event to `run.log` through a small new `RunLog.retry()` helper, and print the banner line with `flush=True` like the existing prints.

### 5. Housekeeping
- Add `memory/` to `.gitignore`.
- Add a "Ticker Memory & Retry" section to `CLAUDE.md` covering the layout, the durable/volatile split and the retry criteria. Also note that memory must never raise, matching the `RunLog` note.
- Do the work on `claude/multi-agent-equity-research-DOiTR`, per `CLAUDE.md`. The current branch is `main`, with an uncommitted change `_AGENT_TIMEOUT_S 900→750`, which this plan leaves alone.

## How XOM_20260927T001400 would play out

The six `ReadTimeout`s are all retryable. Their evidence files already hold every tool result gathered before the stall, so the retries run at concurrency 3. Each retry sees "N calls already done, write the report" and finishes in a few rounds instead of twelve minutes. geo_legal's report goes to `memory/XOM/geo_legal_researcher.md`. The next XOM run starts every specialist with its prior report and durable evidence, so fetches of 10-K text and statements are skipped.

## Out of scope, but related

`REQUEST_TIMEOUT_MS = 600_000` in [roles.py](equity_mcp/roles.py) is the likely reason one stalled stream can eat 600s of a 750s budget. A short `httpx.Timeout(read=...)` would make stalls fail fast, which gives the retry pass room to work. That is worth a separate change once this lands.

## Verification

1. **Unit tests**: new `tests/test_memory.py`, in the plain-`python` style of `tests/test_tool_access.py`. It covers:
   - JSONL append and trimming to 3 runs
   - the `context_for` character cap and dedupe
   - durable filtering in `"prior"` mode
   - an unwritable root that only warns
   - `_is_retryable` for `httpx.ReadTimeout`, `TimeoutError`, `GraphRecursionError` and `ValueError`
   - a `run_research` retry path with `_run_one_agent` monkeypatched to raise `ReadTimeout` once. It asserts that the retry received `"retry"`-mode context and that the result was replaced.
2. **Access control is unchanged**: `uv run python tests/test_tool_access.py`.
3. **Capture smoke test**: `uv run python -m equity_mcp.orchestrator --symbol AAPL --agents macro esg --skip-synthesis --max-concurrency 2 --timeout 600`. Check that `memory/AAPL/` holds `MEMORY.md`, `macro_researcher.md`, `esg_analyst.md` and `evidence/*.jsonl`.
4. **Forced retry**: the same command with `--agent-timeout 90`. `run.log` should show `FAIL … TimeoutError`, then `RETRY … attempt=2`. The attempt-2 lines in the evidence file should show fewer repeated `(tool, args)` pairs.
5. **Rerun reads memory**: repeat step 3. The specialists' prompts should include the prior report. Log the rendered `memory_context` length at debug level to confirm. Durable tools should not be re-called.
6. **Full run**: `--symbol XOM --max-concurrency 4 --timeout 2400`. The memo should reference the prior view, and `MEMORY.md` should gain a run-history row.
