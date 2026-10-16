# Equity Research Eval Dashboard — Agents & Tools Plan

**Status:** final draft for review · nothing built yet for Agents / Tools
**Dashboard:** Equity research rubric explorer (Claude Dashboard artifact)
**Data source:** Supabase project `equity-research-eval` (`zpnjlzrgzrtedkqumrph`), schemas `eval` and `hparams`
**Prepared:** 16 Oct 2026

---

## 1. Purpose

Extend the existing dashboard so a reader can go from **what the agents produced and how they were graded** (Results, Evals) to **how each agent is configured** (Agents) and **what each agent can call** (Tools). Only the **current** configuration is shown; older config snapshots are ignored.

---

## 2. Dashboard after this change

| Tab | Status | Purpose |
|---|---|---|
| **Results** | Live | Per ticker / run: head-of-research verdict, all roles table, stance chart, selected role's cards, agent memo, judge answers |
| **Evals** | Live | Rubric explorer: section → dimension → question type → question, with answer criteria |
| **Agents** | **New** | Team structure, selected agent's model, limits, task, system instruction, tools; all-agents table |
| **Tools** | **New** | Access matrix and tool catalogue with descriptions and input schemas |

**Shared controls**

- **Role picker** (top of page) drives Results, Evals **and Agents**.
- **Tools** starts on **All agents**; an opt-in "Follow role picker" option narrows it to the selected agent.
- Tab order: **Results | Evals | Agents | Tools**.

---

## 3. `hparams` data model (what was studied)

### 3.1 Tables

| Table | Grain | Key fields used |
|---|---|---|
| `configs` | one row per config snapshot (3 today) | `config_sha`, `provenance`, `effective_at`, `last_seen_at`, `source_git_sha`, `content` |
| `config_agents` | config × agent | `role`, `stage`, `agent_kind`, `model_slug`, `model_spec`, `max_tokens`, `recursion_limit`, `advertised_*`, `task`, `system_prompt_sha`, `budget_sha`, `composed_prompt_sha`, `tool_count` |
| `config_runtime` | one per config | `agent_timeout_s`, `tool_timeout_s`, `specialist_max_tokens`, `memo_max_tokens`, `specialist_recursion_limit`, `master_recursion_limit`, `advertised_fraction`, `provider_routing`, `default_model`, `agent_model_overrides` |
| `config_tools` | config × tool | `tool_name`, `tool_sha`, `tags` |
| `config_role_tools` | config × agent × tool | `via` (`shared` or `role`) |
| `tool_defs` | one per tool version | `tool_name`, `module`, `description`, `input_schema`, `impl_sha256` |
| `texts` | content-addressed text | `text_sha`, `body`, `chars` (system prompts, budget blocks, composed prompts) |
| `run_configs` | run → config link | `run_id`, `config_sha` |

### 3.2 Views used

| View | Use |
|---|---|
| `v_config_current` | Defines **current**: latest non-`inferred` config by `last_seen_at` |
| `v_config_agents` | Agents with `is_current`, `composed_chars`, `agent_unchanged_since` |
| `v_config_tools` | Tools with `is_current`, module, tags, description, input schema |
| `v_config_access_long` | Agent → tool access rows with `via` |
| `v_config_access_wide` | Tool × role booleans and `n_roles` |
| `v_config_integrity` | Consistency checks (0 issues on current config) |

### 3.3 Current configuration (as of 16 Oct 2026)

- Config `22b40e6…`, provenance `reconstructed_from_git`, effective **27 Sep 2026**, last seen **6 Oct 2026**, git `5b45296`.
- 26 of 29 evaluated runs used this config; the other 3 used 26 Sep snapshots whose system prompts are identical. The Agents tab therefore describes what produced almost every memo in Results.
- **0** integrity issues.

### 3.4 Agents (13 current)

| Stage | Agent(s) | Kind | Tools |
|---|---|---|---|
| 1 | 11 specialists: alt_data, esg, fin_risk, geo_legal, growth, macro, nonfin_risk, quant, sector, short, value | `react_specialist` | 9–25 each |
| 2 | portfolio_strategist | `react_specialist` | 25 |
| 3 | head_of_research (main deep agent) | `deep_master` | 6 (shared only) |

**Flow (confirmed):** every Stage 1 specialist → portfolio strategist **and** head of research; portfolio strategist → head of research.

**Note:** the head of research also has deep-agent built-ins (`write_todos`, filesystem tools) mentioned in its budget text but **not stored** in `hparams`. Its card will say so.

### 3.5 Tools (61 current)

- 10 modules under `equity_mcp.tools.*`: `calculations.forensics`, `calculations.quant`, `calculations.risk`, `calculations.valuation`, `db`, `web`, `external.alt_data`, `external.fred`, `external.news`, `external.sec_edgar`.
- **6 shared** with all 13 agents; **21 used by one agent only**; none unused.
- Access is granted by `tags` (`shared` or a role name); `via` records which.
- 112 input parameters in total; types `string`, `integer`, `number`, `array`; **no parameter descriptions or enums** in the schemas.

---

## 4. Field mapping — Agents tab

| Requested | Hard limit (enforced) | Told to agent (in prompt) | Source |
|---|---|---|---|
| **System prompt** (shown as *System instruction*) | — | — | `texts.body` via `system_prompt_sha` (markdown, 1.5–2.3K chars) |
| Execution budget block | — | full text | `texts.body` via `budget_sha` (appended to the prompt; the agent sees instruction + budget, 2.8–3.6K chars) |
| **Task** | — | — | `config_agents.task` |
| **Token budget** | `max_tokens`: 8,096 specialists / 16,000 head of research | stated in budget block | `config_agents.max_tokens` |
| **Recursion limit** | `recursion_limit`: 30 / 15 | `advertised_recursion_limit` 22 / 11 · `advertised_tool_rounds` ≈10 / ≈5 · `advertised_write_by` round 8 / 3 | `config_agents` |
| **Timeout** | `agent_timeout_s` 750 s per agent | `advertised_timeout_s` 562.5 s · `tool_timeout_s` 90 s per tool call | `config_runtime`, `config_agents` |
| **Model** | `model_slug` `deepseek/deepseek-v4-flash-0731` | — | `model_spec` prefix `openrouter:` → provider; `provider_routing` (Azure excluded); `agent_model_overrides` (none) |
| Context | stage, `agent_kind`, `tool_count`, `agent_unchanged_since` | — | `v_config_agents` |

Told-to-agent values are 75% of the hard limits (`advertised_fraction` = 0.75) — a deliberate safety margin, so both are shown.

## 5. Field mapping — Tools tab

| Requested | Source |
|---|---|
| **Tool name** | `v_config_tools.tool_name` |
| **Module** | `v_config_tools.module` |
| **Agents with access** | `v_config_access_long` (`role`, `via`) |
| **Description** | `v_config_tools.description` |
| **Input schema** | `v_config_tools.input_schema` (JSON Schema: `properties`, `type`, `items.type`, `required`, `default`) |

---

## 6. Agents tab — specification

### 6.1 Header line
"Configuration in force since 27 Sep 2026 · last used 6 Oct · git 5b45296 · 0 integrity issues"

### 6.2 Team structure diagram (top of tab)
- Inline SVG, three columns: **Stage 1** (11 specialist nodes) → **Stage 2** portfolio strategist → **Stage 3** head of research (labelled *deep agent*).
- Arrows: every specialist → portfolio strategist and → head of research; portfolio strategist → head of research. Specialist arrows bundled so the diagram stays readable.
- Each node shows its role name and tool count.
- The role from the picker is highlighted; clicking a node sets the role picker (which also updates Results and Evals).
- Narrow screens (~400 px): stages stack vertically.

### 6.3 Selected agent
1. **Four cards**, hard limit large, told-to-agent value beneath:

| Card | Large value | Beneath |
|---|---|---|
| Model | DeepSeek V4 Flash | via OpenRouter · Azure excluded · raw slug |
| Token budget | 8,096 output tokens | as stated in the budget block |
| Recursion limit | 30 steps | told 22 steps · ≈10 tool rounds · write by round 8 |
| Timeout | 750 s per agent | told 562 s · 90 s per tool call |

2. **Task** — highlighted line, with stage, agent kind and "Last changed <date>".
3. **System instruction** — rendered markdown (same safe renderer as the Results memo).
4. **Execution budget** — collapsible block beneath, noting the agent receives instruction + budget together.
5. **Tools this agent can use** — chips grouped by module, marked *shared* or *role-specific*; clicking a chip opens the tool in the Tools tab. Head of research shows the note about deep-agent built-ins.

### 6.4 All agents at a glance
Sortable table of 13 agents: role, stage, kind, model, token budget, recursion (hard / told), timeout (hard / told), tool count. Row click selects that agent.

---

## 7. Tools tab — specification

### 7.1 Header line
"61 tools across 10 modules · 6 shared with every agent · 21 used by one agent only"

### 7.2 Filters
- **Search** — tool name or description.
- **Module** — all or one of the 10.
- **Agent** — default **All agents**; options for each agent, plus **Follow role picker** (opt-in).
- **Access** — all / shared / one agent only.
- Filters apply to both the matrix and the tool list. "Clear filters" resets.

### 7.3 Access matrix
- Rows: tools grouped by module (shared tools first in each module); columns: 13 agents in stage order.
- Filled cell = access; shared access in a muted tint; one-agent-only tools flagged in the row label.
- The role picker's agent column is highlighted.
- Hover tooltip: tool · agent · granted via shared / role tag. Clicking a row scrolls to that tool's card.
- Scrolls horizontally on narrow screens, with the tool name column sticky.

### 7.4 Tool cards (grouped by module)
- Tool name, full module path.
- Description (line breaks kept).
- **Who can use it:** "All 13 agents (shared)" or one chip per agent; chips link to that agent in the Agents tab.
- **Input schema table:** Parameter · Type (array shows item type) · Required · Default.
- **View raw JSON** toggle showing the full schema.

---

## 8. New live queries (Supabase `execute_sql`)

All are filtered to the current configuration, take no filters, and return about 60 KB combined. All four were run against the live data on 16 Oct 2026 and gave the expected row counts.

### 8.1 `cfg_current` — header (1 row)
```sql
SELECT c.config_sha, c.provenance, c.effective_at, c.last_seen_at,
       left(c.source_git_sha, 7) AS git_sha,
       rt.agent_timeout_s, rt.tool_timeout_s, rt.default_model,
       rt.provider_routing, rt.agent_model_overrides, rt.advertised_fraction,
       (SELECT count(*) FROM hparams.v_config_integrity i
         WHERE i.config_sha = c.config_sha)::int AS integrity_issues
FROM hparams.v_config_current c
LEFT JOIN hparams.config_runtime rt ON rt.config_sha = c.config_sha
```

### 8.2 `cfg_agents` — agents with prompt and limits (13 rows)
```sql
SELECT a.role, a.stage, a.agent_kind, a.model_slug, a.model_spec,
       a.max_tokens, a.recursion_limit, a.advertised_recursion_limit,
       a.advertised_tool_rounds, a.advertised_write_by, a.advertised_timeout_s,
       rt.agent_timeout_s, rt.tool_timeout_s,
       a.task, a.tool_count, a.composed_chars, a.agent_unchanged_since,
       sp.body AS system_prompt, bd.body AS budget_block
FROM hparams.v_config_agents a
JOIN hparams.config_runtime rt ON rt.config_sha = a.config_sha
LEFT JOIN hparams.texts sp ON sp.text_sha = a.system_prompt_sha
LEFT JOIN hparams.texts bd ON bd.text_sha = a.budget_sha
WHERE a.is_current
ORDER BY a.stage, a.role
```

### 8.3 `cfg_access` — agent → tool (204 rows)
```sql
SELECT role, tool_name, module, via
FROM hparams.v_config_access_long
WHERE is_current
ORDER BY role, module, tool_name
```

### 8.4 `cfg_tools` — tool definitions (61 rows)
```sql
SELECT t.tool_name, t.module, t.tags,
       ('shared' = ANY (t.tags)) AS is_shared, w.n_roles,
       t.description, t.input_schema
FROM hparams.v_config_tools t
JOIN hparams.v_config_access_wide w
  ON w.config_sha = t.config_sha AND w.tool_name = t.tool_name
WHERE t.is_current
ORDER BY t.module, t.tool_name
```

**Existing queries** (unchanged): `roles`, `questions`, `criteria` (Evals); `runs`, `run_roles`, `role_dims`, `role_domain`, `role_stance`, `role_answers`, `role_output` (Results).

---

## 9. Implementation notes

- **Rendering:** the system instruction and budget block reuse the memo's markdown renderer, which builds page elements and never inserts raw HTML. Only `http(s)` links are clickable.
- **Loaders:** the four new sources use the existing Supabase answer loader.
- **Shared state:** the role picker (`role`) selects the agent; clicking a diagram node or table row sets it. The Tools filter state is held on the page only and is not a query input.
- **Cross-tab links:** tool chip → Tools tab, scrolled to the card; agent chip → Agents tab with that role selected.
- **Labels:** stage names ("Specialist", "Synthesis", "Deep agent"), the plain section names already in use, and the raw ids kept in grey.
- **Layout:** cards in an auto-fit grid; the diagram is sized from its container; the matrix scrolls horizontally; everything works at ~400 px wide beside the chat.
- **Loading states:** skeletons while loading, "Failed to load" lines on error, and an explicit message where data is missing.

---

## 10. Verification before handover

1. Run each new query as stored; confirm row counts (1 / 13 / 204 / 61).
2. Run the page against mock data in a headless test: diagram renders, role switching updates the cards and prompt, matrix and filters work, schema tables and raw JSON toggle work, cross-tab links work.
3. Write to the dashboard; read its runs/check documents for load or script errors; fix and re-check if any.

---

## 11. Decisions log

| # | Decision | Choice |
|---|---|---|
| 1 | Agent selection | Reuse shared role picker |
| 2 | Limits | Show hard and told-to-agent values |
| 3 | Access matrix | Include in Tools tab |
| 4 | Team structure diagram | Include at top of Agents |
| 5 | Diagram flow | All specialists → portfolio strategist and head of research; portfolio strategist → head of research |
| 6 | Tools default | Start on All agents; "Follow role picker" opt-in |
| 7 | Scope | Current config only (`is_current`); older snapshots ignored |

### Earlier dashboard decisions (for reference)
- Rubric views are spelled `v_rubric_*`; score scale shown as the range found in criteria; `n_levels` counts levels.
- Metrics tab removed; Questions and Criteria merged into **Evals**.
- Plain-language names: Follows the brief / Investment view / Company assessment; Rating / Pick one / Yes-No.
- Company assessment shown on the 0–4 scale.
- Head of research verdict shown as a separate tag above the all-roles table.
- Agent memo shown beneath the role cards, with the preamble shown as a muted "Agent's note".
- Judge answers table: sortable, with Show / Question / Type filters and a confidence range slider.

---

## 12. Deferred (not in this build)

1. Results → Agents "View this agent's setup" link.
2. Agents → Results "How this agent scored" strip.
3. Tool coverage warning (tools available vs tool rounds allowed).
4. Prompt length vs token budget chart.
5. Deep links (`#agents`, `#tools`) — note: the page already supports `#results` / `#evals`; extending to the new tabs is trivial if wanted later.
6. Trend over time per ticker (skipped earlier; few repeat runs).
