# equity-researcher — CLAUDE.md

## Project Overview

A multi-agent equity research system built on a shared FastMCP server.
14 AI agents (each on its own OpenRouter model) collaborate to produce
institutional-quality investment memos. All financial data comes from Financial
Modeling Prep's remote MCP server; anything that has to be *computed* rather than
fetched is computed by a single agent that writes and runs Python.

## Development Branch

Always develop on `claude/multi-agent-equity-research-DOiTR`.

## Architecture

```
equity_mcp/
├── server.py              # FastMCP app — 6 tools registered here with role tags
├── roles.py               # Canonical tag sets + model assignment per agent role
├── workspace.py           # Per-run scratch dir shared by the FMP and code tools
├── langchain_bridge.py    # Bridges FastMCP tools → LangChain StructuredTool (by role)
├── deep_agent_factory.py  # Builds 13 subagents + master via create_deep_agent
├── orchestrator.py        # CLI entry point
├── tools/
│   ├── fmp.py             # FMP MCP client — fmp_catalog + fmp_call
│   ├── code_exec.py       # run_python + list_workspace
│   └── web.py             # web_search + fetch_page
└── prompts/               # System prompt .md per role, plus _toolkit.md
```

## The Data Model: catalog → fetch → compute

There are no per-metric tools. There used to be ~40 `calculate_*` functions that
hard-coded the column names of a Postgres schema; they were deleted because the
database never existed (`DATABASE_URL` was a placeholder, so every query fell
through to FMP) and because a thin schema had forced them onto invented proxies —
A/R as 8% of assets, PPE as 30%, Piotroski's dilution criterion hard-coded to
pass. Those numbers were wrong by construction.

The replacement is three steps, described to the agents in `prompts/_toolkit.md`:

1. **`fmp_catalog()`** — the 28 FMP category tools and what they cover.
   `fmp_catalog("statements")` drills into one tool's endpoints and parameters.
   Fetched once per process and cached.
2. **`fmp_call(tool, endpoint, params)`** — a generic passthrough. Data arrives in
   FMP's own camelCase and is *not* reshaped; the response carries a `fields` list
   so the caller reads the schema instead of assuming it.
3. **`run_python(code)`** — for anything FMP doesn't return directly.

Deliberately no wrapper-per-endpoint: ~250 endpoints wrapped by hand is a second
copy of FMP's catalog that goes stale the moment FMP ships anything.

**Check FMP before computing.** It already returns much of what the old
calculation layer approximated: `statements/financial-scores` (real Altman Z and
Piotroski), `key-metrics`, `metrics-ratios`, `owner-earnings`,
`financial-statement-growth`, `discountedCashFlow/*`, `technicalIndicators/*`,
`economics/treasury-rates`.

### Payload spilling

`fmp_call` writes any response over `_INLINE_LIMIT` (8 KB) to
`<workspace>/data/<name>.json` and returns only `fields`, a short `preview`, and
`saved_to`. This is load-bearing, not an optimisation: one
`technicalIndicators/relative-strength-index` call returns 1,255 rows / ~179 KB,
which is untenable in an LLM context but trivial for `run_python` to read off
disk. That call comes back as an 834-byte response.

### Failure contract

`fmp_call` never raises. It returns `{"error", "kind"}` where `kind` is one of:

- `plan_denied` — the endpoint exists but the subscription doesn't cover it. FMP
  reports this in prose (`ACCESS DENIED: … requires a higher plan`), not as a
  status code, so it is detected by sniffing for `_PLAN_DENIED_MARKERS`. Logged
  WARNING once per `(tool, endpoint)` per process, since several agents will
  otherwise each rediscover the same gate.
- `shutting_down` — the call started after the main thread finished, when
  `concurrent.futures` refuses to schedule. Benign teardown noise; logged INFO.
- `bad_request` / `unavailable` — everything else. FMP's validation errors list
  the valid enum values, and that text is passed through to the agent verbatim so
  it can correct itself.

### The background event loop

`fastmcp.Client` is async-only, but MCP tools are called synchronously (FastMCP
runs sync tools in worker threads) and `asyncio.run` raises if the calling thread
already drives a loop. So `fmp.py` owns one daemon event loop on a background
thread and marshals every call onto it with `run_coroutine_threadsafe`.

That loop outlives the main thread, which is the one hazard worth knowing about.
CPython sets `concurrent.futures.thread._shutdown` the moment the main thread
finishes, and everything downstream of a connect — down to the `run_in_executor`
that resolves DNS — refuses to schedule after that. `call_tools` guards on
`threading.main_thread().is_alive()` *and* converts the executor's RuntimeError,
because CPython trips the flag just before stopping the main thread and neither
signal alone covers the gap.

The per-batch timeout lives *inside* the loop as `asyncio.timeout`, so expiry
cancels the coroutine and closes the session. `Future.cancel()` cannot stop a
coroutine that has already started, which used to leak reconnecting sessions.

## Orchestration

The Head of Research is a `create_deep_agent` master with 13 specialist
subagents. It plans its own task breakdown via deepagents' `write_todos` and
delegates. Each subagent gets only the FastMCP tools tagged for its role.

```
Master: Head of Research  (create_deep_agent)
  └── subagents (13 specialists):
        quant_engineer     ← the only agent that can execute code
        sector_researcher  |  geo_legal_researcher  |  macro_researcher
        value_researcher   |  growth_researcher     |  fin_risk_analyst
        nonfin_risk_analyst|  quant_analyst          |  short_analyst
        esg_analyst        |  alt_data_analyst       |  portfolio_strategist
```

**Subagents cannot delegate to each other.** `deepagents.middleware.subagents.create_sub_agent`
compiles each spec through plain `create_agent` with only its own `tools`, so no
subagent has a `task` tool. An analyst needing a computed figure says so in its
report; the Head of Research routes it to `quant_engineer`. Both the master's
prompt and its task instruction say this explicitly, because it is not something
the model can infer from its tool list.

## Code Execution

`run_python` shells out to `sys.executable` with the run workspace as cwd, a
600-second timeout ceiling, and — importantly — a scrubbed environment. Only
`PATH`, `SYSTEMROOT`, `WINDIR`, `TEMP`, `TMP`, `HOME`, `LANG` and
`PYTHONIOENCODING` pass through. Generated code computes over JSON already on
disk; it has no business holding `FMP_API_KEY` or `OPENROUTER_API_KEY`, and
withholding them means it cannot fetch anything on its own either.

**This is not a sandbox.** The child runs as the same user with the same
filesystem and network access. The scrub limits credential exposure, not reach.

`numpy` and `pandas` are project dependencies specifically so scripts can use
them — they reach the child through `sys.executable`, so they must be real deps
rather than something incidentally installed.

## Workspace

Each run gets `runs/<SYMBOL>_<TIMESTAMP>/` with `data/` (payloads spilled by
`fmp_call`) and `scripts/` (what `run_python` executed). That is the audit trail
for every computed figure in the memo. `orchestrator.py` calls
`workspace.set_run(symbol)` at startup.

MCP tools are plain functions with no run context, so a process-global run
directory is the only way the spill target and the execution cwd agree.
`$EQ_WORKSPACE` pins an explicit directory for inspecting tools outside a run;
`$EQ_WORKSPACE_ROOT` moves the parent.

## Tool tags = role sets

Tags are `set[str]` in `roles.py`, filtered in `langchain_bridge.get_langchain_tools_for_role`
by `{role, "shared"} & tool.tags`.

**A role constant holds only its own role — never `"shared"`.** They used to
carry it, which silently defeated the whole mechanism: every union mentioning any
role also carried `"shared"` and so matched all roles, making supposedly-gated
tools universal. Since data access is now uniform, `QUANT_ENGINEER` is the only
tag that gates anything, so this correctness matters more than it used to, not
less. Verify with the loop in "Verifying" below.

## Environment Setup

Dependencies are managed with [uv](https://docs.astral.sh/uv/). `uv.lock` is
committed and is the source of truth for versions.

```bash
uv sync
cp .env.example .env
# Fill in FMP_API_KEY and OPENROUTER_API_KEY (both required)
```

Prefix commands with `uv run`, or activate the environment
(`.venv\Scripts\activate` on Windows). Add dependencies with `uv add <pkg>` so
pyproject and the lockfile stay in step.

## Running

```bash
# Full pipeline for a single ticker
uv run python -m equity_mcp.orchestrator --symbol AAPL

# Steer the master agent
uv run python -m equity_mcp.orchestrator --symbol MSFT --focus "weight ESG and growth"

# Inspect all registered MCP tools and their tags
uv run fastmcp inspect equity_mcp/server.py

# Run MCP server standalone (for testing tools directly)
uv run fastmcp run equity_mcp/server.py
```

## Verifying

Per-role tool gating — `quant_engineer` should show 6 tools, every other role 4:

```bash
uv run python -c "
import asyncio
from equity_mcp.langchain_bridge import get_langchain_tools_for_role
from equity_mcp.roles import ALL_ROLES
async def main():
    for r in ALL_ROLES:
        t = await get_langchain_tools_for_role(r)
        print(f'{r:22} {len(t)}  {sorted(x.name for x in t)}')
asyncio.run(main())"
```

## External APIs

| API | Key Variable | Required | Notes |
|-----|-------------|----------|-------|
| FMP | `FMP_API_KEY` | **Yes** | The only financial data source, via its remote MCP server |
| OpenRouter | `OPENROUTER_API_KEY` | **Yes** | Powers all agents; per-role model set in `roles.py` |
| Brave Search | `BRAVE_API_KEY` | Optional | Backs `web_search`; falls back to DuckDuckGo |

### FMP plan gating

This account is on **Starter**. Available: `statements`, `chart`, `quote`,
`company`, `analyst`, `calendar`, `news`, `economics`, `insiderTrades`, `senate`,
`secFilings`, `search`, `directory`, `technicalIndicators`, `discountedCashFlow`,
`indexes`, `etfAndMutualFunds`, `forex`, `crypto`, `commodity`.

Gated: `ESG` and `earningsTranscript` (Ultimate+), `form13F` and
`commitmentOfTraders` (Premium+), parts of `marketPerformance`, `tipranks`
(separate add-on). These return `kind="plan_denied"`. The `esg_analyst`,
`sector_researcher`, and `alt_data_analyst` prompts name their specific gaps and
what to use instead, so agents don't burn turns rediscovering them.

## Adding a New Tool

1. Implement the function in the appropriate `tools/` module
2. Import it in `server.py`
3. Register with `mcp.tool(tags=<ROLE_SET>)(<function>)`
4. The bridge picks it up automatically

Think twice before adding an FMP wrapper — if FMP has an endpoint for it, agents
can already reach it through `fmp_call`, and a wrapper is one more thing to drift.

## Adding a New Agent

1. Add a role constant and tag set to `roles.py`, and the role to `ALL_ROLES`
2. Add a system prompt at `prompts/<new_role>.md` — describe how the analyst
   thinks; the data workflow is appended automatically from `_toolkit.md`
3. Add a one-line capability description to `_DESCRIPTIONS` in
   `deep_agent_factory.py` so the master knows when to delegate to it
4. Optionally pin it to a model via `AGENT_MODELS` in `roles.py`

## Known Issues

`web_search` returns `[]` for every query — the DuckDuckGo scrape in
`tools/web.py` is broken. Setting `BRAVE_API_KEY` sidesteps it without code
changes. This matters more than it looks: web search is the documented fallback
for the ESG analyst, whose vendor ratings are plan-gated.
