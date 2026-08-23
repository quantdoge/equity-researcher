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
├── session.py             # SQLite checkpoints + session registry behind --last
├── progress.py            # AgentMiddleware: console status + per-agent reports
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

## Call limits

`roles.py` also carries the per-agent call budgets, attached as LangChain
middleware by `middleware_for_role(role, tool_names)` — passed into each subagent
spec by `_build_subagent` and into `create_deep_agent` for the master. Middleware
given to the master does *not* propagate to subagents, which is why both call
sites exist.

- **Tools** — `DEFAULT_TOOL_RUN_LIMIT` (10) per tool, overridable per tool in
  `TOOL_CALL_LIMITS` and per role in `ROLE_TOOL_CALL_LIMITS`. One
  `ToolCallLimitMiddleware` instance per tool, so the budgets are independent:
  ten `fmp_call` *and* ten `web_search`, not ten between them. `exit_behavior` is
  `"continue"`, so an over-budget call returns an error ToolMessage the agent can
  read and route around.
- **Models** — `DEFAULT_MODEL_RUN_LIMIT` (20) per role, overridable in
  `MODEL_CALL_LIMITS`. `exit_behavior` is `"end"`, not because that is preferable
  but because `ModelCallLimitMiddleware` accepts only `"end"` or `"error"` —
  there is no `"continue"` — and `"error"` raises through the graph, killing a
  whole run over one runaway specialist.

`head_of_research` is uncapped on model calls (`MODEL_CALL_LIMITS` sets it to
`None`, and no middleware is built when a limit resolves to `None`). The master
plans, delegates thirteen times, reads thirteen reports and writes the memo; any
cap tight enough to save tokens ends the run with `"Model call limits exceeded"`
where the Investment Memo should be. Its four data tools are still capped.

Two things are deliberately *not* limited. deepagents' own built-ins — `task`,
`write_todos`, `ls`, `read_file` — never appear in `tool_names`, so they get no
middleware; capping `task` at ten would strand three of the thirteen specialists.
And these are all `run_limit`s, never `thread_limit`s, so a subagent's counters
reset on each delegation: the budget bounds one task, not a specialist's whole
participation in a run.

Middleware names must be unique per agent (`create_agent` asserts on duplicates).
`ToolCallLimitMiddleware.name` embeds the tool name, so per-tool instances are
safe; `ModelCallLimitMiddleware.name` does not, so there is exactly one per agent.
Same for `ModelRetryMiddleware` and `ToolErrorMiddleware` below.

## Model transport

`chat_model_for_role(role)` builds the chat model rather than handing deepagents
the bare `"openrouter:<slug>"` spec, because two `ChatOpenRouter` defaults are
hostile to a run that lasts half an hour.

**`streaming=True`.** The default is `False`, which makes every model call one
POST held open with zero bytes flowing until the completion is finished. Over a
long run OpenRouter's edge closes some of those sockets before the first response
byte, and httpx reports it as `RemoteProtocolError: Server disconnected without
sending a response` — the failure that used to end every run partway through.
Streaming keeps bytes moving so the connection never looks idle. It is a
transport change only: `_agenerate` routes through `_astream` +
`agenerate_from_stream` and still returns one complete `AIMessage`, tool calls
reassembled from the chunks.

**`timeout=REQUEST_TIMEOUT_MS`.** `request_timeout=None` is not "use the
default" — the SDK passes it straight into httpx's `build_request`, where an
explicit `None` means `Timeout(None)`, no ceiling at all, so a stalled call hangs
until the server hangs up. With streaming the explicit value is a between-chunks
read timeout, which is the semantics worth having.

Attribution and `openrouter_provider` are set here too. Passing a model *instance*
bypasses deepagents' `apply_provider_profile`, which would otherwise supply them;
they are only passed when the role actually resolves to OpenRouter, since
`model_for_role` lets a role be pinned to another provider that would reject them.

Models are built one per role and never cached — a module-level cache would
outlive the event loop it first served, and a pooled connection from a dead loop
is a new failure mode. The pools connect lazily, so fourteen cost nothing.

### Surviving a dropped connection anyway

The SDK's own `max_retries` does not cover the disconnect above.
`openrouter.utils.retries` honours `retry_connection_errors` only for
`httpx.ConnectError` and `httpx.TimeoutException`; `RemoteProtocolError` falls to
a catch-all that wraps it as `PermanentError` and re-raises without a retry. So
`middleware_for_role` adds two things:

- **`ModelRetryMiddleware`, every role** — retries `httpx.TransportError` (the
  common base of `RemoteProtocolError`, `ReadTimeout` and `ConnectError`) three
  times with backoff. `on_failure="continue"`, so an exhausted retry becomes an
  `AIMessage` describing the failure and degrades one specialist rather than the
  run. It does not eat into the model budget: `ModelCallLimitMiddleware` counts in
  `before_model`, a graph-node hook, while retries happen inside one
  `wrap_model_call`.
- **`ToolErrorMiddleware`, master only** — subagents reach the master through the
  `task` tool, and LangGraph re-raises anything that is not a `ToolException`, so
  an exception escaping a specialist ends the run. `_transport_error_message`
  returns text (which becomes an error `ToolMessage`) for network faults only, and
  `None` for everything else so an ordinary bug still surfaces as a traceback
  instead of being quietly serialised into the master's context.

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
`fmp_call`), `scripts/` (what `run_python` executed), `reports/` (one `.md` per
agent, written the moment it finishes) and `run.log`. That is the audit trail for
every computed figure in the memo. `orchestrator.py` calls
`workspace.set_run(symbol)` at startup, or `workspace.attach_run(session_id)` when
resuming — `attach_run` raises rather than creating the directory, because a
resume into an empty workspace refetches everything while looking like it worked.

MCP tools are plain functions with no run context, so a process-global run
directory is the only way the spill target and the execution cwd agree.
`$EQ_WORKSPACE` pins an explicit directory for inspecting tools outside a run;
`$EQ_WORKSPACE_ROOT` moves the parent.

**The directory name is the session id.** One string is the LangGraph `thread_id`,
the workspace directory, and the stem of both output files. There is deliberately
no second identifier scheme.

## Session persistence

`session.py` owns `runs/sessions.sqlite` (`$EQ_STATE_DB` moves it), which holds
two unrelated things in one file: LangGraph's own `checkpoints`/`writes` tables,
written by `AsyncSqliteSaver`, and a `sessions`/`agent_events` registry written
here. The registry exists so `--list-sessions` can answer without deserialising
checkpoint blobs, and so a run records *why* it stopped.

`build_master_agent(checkpointer=...)` forwards to `create_deep_agent`, and
`run_research` passes `{"configurable": {"thread_id": session_id}}` plus
`recursion_limit=200`. That limit is not incidental: LangGraph's default is 25
supersteps, which a master that plans, delegates thirteen times and synthesises
can plausibly exceed, and a `GraphRecursionError` is indistinguishable from a
crash worth resuming from.

Resume invokes with `None` input, which re-runs the tasks pending in the
checkpoint instead of appending a second copy of the task message. If the thread
has no checkpoint — the first attempt died before its first superstep committed —
`run_research` falls back to the full input.

**Resume granularity is one specialist.** Checkpoints land at master-graph
supersteps, so every finished specialist report survives in the master's message
history. A specialist that died mid-flight reruns from scratch: deepagents
compiles subagent graphs through plain `create_agent` and its `SubAgent`
TypedDict has no `checkpointer` field, so there is nowhere to pass one. The
payloads that specialist had already fetched are still in `data/`, so the rerun
is cheaper than the first pass, not free.

### Never write to the registry from the event loop

The registry helpers block, and the checkpointer's `commit()` is an `await`
queued on the same loop. Blocking the loop means the saver cannot release its
write transaction, so the blocking call waits out its entire busy timeout and
fails with `database is locked` — observed as a 30-second stall per agent before
it was routed off the loop. `session.arecord_agent` is the async-safe entry
point; anything else called from async code needs the same `to_thread` wrapper.

## Progress and incremental output

`progress.py` is one `AgentMiddleware` attached to every agent, and it is where
both the console status and the durable per-agent output come from.
`awrap_tool_call` narrates each fetch and delegation; `aafter_agent` writes
`reports/<role>.md`, appends the same section to `outputs/<session>.md`, and
records the `agent_events` row.

**It costs no tokens.** Every hook returns `None` or the handler's result
untouched, so no message, tool or prompt fragment reaches a model. That is the
whole reason this is middleware rather than a "report your progress" instruction
in the prompts.

Middleware rather than `astream` because deepagents invokes subagents *inside*
the `task` tool rather than as graph nodes, so streaming the master's graph
cannot see into a specialist. Only the async hooks are implemented;
`langchain.agents.factory` picks hooks by comparing the class attribute against
`AgentMiddleware`'s and wraps them in `RunnableCallable(sync, async)`, so
async-only is a supported shape.

Two details that are easy to get wrong:

- **Per-invocation counters cannot key on `checkpoint_ns`.** LangGraph writes it
  *per node*, so `abefore_model` and `aafter_agent` in one invocation see
  different values and the counts get dropped. What is stable is the namespace's
  parent prefix — everything before the last `|`. A subagent sees
  `tools:<task-id>|<node>:<node-id>`, so the prefix is the delegating tool call:
  constant for that specialist's run and distinct from any other delegation. The
  master's nodes are unnested, so their prefix is empty. See `progress._scope`.
- **Report files are named by role, not by ordinal.** A resumed run may rerun a
  specialist, and the newer report should replace the older one rather than
  accumulate near-duplicates. True ordering lives in `agent_events` and in the
  append-only master copy.

Console glyphs fall back to ASCII when `sys.stdout.encoding` cannot encode them —
a Windows console codepage raising `UnicodeEncodeError` from a status line must
not be the thing that ends a run.

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

# Sessions: list what ran, resume what did not finish
uv run python -m equity_mcp.orchestrator --list-sessions
uv run python -m equity_mcp.orchestrator --last                       # newest unfinished
uv run python -m equity_mcp.orchestrator --last AAPL_20260801T142233  # a specific one
uv run python -m equity_mcp.orchestrator --last <id> --force          # re-run a completed one

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

Middleware — one instance per tool the role holds, a model limiter for everyone
but the master, a retry and a progress reporter for everyone, and the tool-error
net for the master alone. Expect 9 for `quant_engineer` and 7 for every other
role, including `head_of_research` (which trades the model limiter for
`ToolErrorMiddleware`):

```bash
uv run python -c "
import asyncio
from equity_mcp.langchain_bridge import get_langchain_tools_for_role
from equity_mcp.roles import ALL_ROLES, middleware_for_role
async def main():
    for r in ALL_ROLES:
        t = await get_langchain_tools_for_role(r)
        mw = middleware_for_role(r, [x.name for x in t])
        names = [m.name for m in mw]
        assert len(set(names)) == len(names), (r, names)
        print(f'{r:22} {len(mw)}  {names}')
asyncio.run(main())"
```

Graph assembly — `create_agent` validates middleware at construction, and
deepagents compiles all 13 subagent graphs eagerly, so this catches a bad
`exit_behavior` or a duplicate middleware name without spending a token.
`OPENROUTER_API_KEY` must be set for `init_chat_model`, but no API call is made:

```bash
uv run python -c "
import asyncio
from equity_mcp.deep_agent_factory import build_master_agent
asyncio.run(build_master_agent()); print('master compiled')"
```

The same check against a live checkpointer, which additionally proves the saver
binds to the running loop and that the state DB is writable:

```bash
uv run python -c "
import asyncio
from equity_mcp import session
from equity_mcp.deep_agent_factory import build_master_agent
async def main():
    session.init_db()
    async with session.checkpointer() as cp:
        await build_master_agent(checkpointer=cp)
        print('master compiled with checkpointer')
asyncio.run(main())"
```

Session state — the LangGraph tables and the registry share one file:

```bash
uv run python -c "
import sqlite3
from equity_mcp import session
c = sqlite3.connect(session.state_db_path())
print(sorted(r[0] for r in c.execute(\"select name from sqlite_master where type='table'\")))
for r in c.execute('select session_id,symbol,status,resumed_count from sessions'): print(r)
for r in c.execute('select seq,role,status,tool_calls,model_calls from agent_events'): print(r)"
```

Expect `['agent_events', 'checkpoints', 'sessions', 'writes', ...]`.

End-to-end resume is the acceptance test, and it costs real tokens: start a run,
Ctrl-C after two or three specialists report, then `--last`. The finished
specialists must appear in `runs/<session>/reports/` and in
`outputs/<session>.md` *before* the resume, and must not be re-run by it — no
second `▶` for them in the resumed run's output.

## External APIs

| API | Key Variable | Required | Notes |
|-----|-------------|----------|-------|
| FMP | `FMP_API_KEY` | **Yes** | The only financial data source, via its remote MCP server |
| OpenRouter | `OPENROUTER_API_KEY` | **Yes** | Powers all agents; per-role model set in `roles.py` |
| SerpApi | `SERP_API_KEY` | Optional | Backs `web_search`; no fallback provider |

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

## Web Search

`web_search` runs on SerpApi's `engine=google` and has no fallback provider —
Brave and the DuckDuckGo scrape are gone. The scrape's regex had stopped matching
DDG's markup, so it returned `[]` for every query while looking healthy, which is
the failure mode worth avoiding here: web search is the documented fallback for
the ESG analyst, whose vendor ratings are plan-gated, and an empty list reads to
an agent as "nothing exists" rather than "the tool is broken."

So `web_search` never raises and never returns a bare `[]` on failure. It returns
one marker result tagged `kind` — `not_configured` (no `SERP_API_KEY`),
`unavailable` (transport error), or `search_error` (SerpApi's own message for a
bad key or exhausted quota, passed through verbatim). An empty list now means
exactly one thing: the search ran and found nothing.
