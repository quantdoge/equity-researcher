"""
A content-addressed snapshot of the research pipeline's hyperparameters.

Everything is read from live module state in the process that builds it,
never re-implemented:

- An agent's prompt is the one ``build_specialist_agent`` / ``build_head_agent``
  actually pass to ``create_react_agent`` / ``create_deep_agent``. Those two
  are swapped for capturing stubs while the builders run.
- Its tools are the ones the bridge hands that role.
- Its model and transport are whatever ``chat_model_for_role`` passes to
  ``init_chat_model``.

A snapshot therefore cannot describe a pipeline other than the one that ran.

This file is self-contained on purpose: it uses only the stdlib at import time,
and ``equity_mcp`` is imported lazily inside ``build_snapshot``. The git
backfill (backfill.py) runs *this* file against old trees that predate
``equity_mcp.hparams``, so nothing may be imported from the rest of the
package at module level.

The hashing conventions match ``equity_mcp/evaluation/loader.py``. Text is
hashed as LF-normalised UTF-8, like ``prompt_sha256``, so ``system_prompt_sha``
joins to ``eval.rubrics.source_prompt_sha256``. JSON is canonicalised the way
``sha256_json`` does it, except that whole floats are written as ints: 750.0
and 750 must not give two configs.
"""

from __future__ import annotations

import ast
import contextlib
import hashlib
import importlib
import inspect
import json
import math
import tempfile
import textwrap
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator

SNAPSHOT_VERSION = 1

# Ascending rank: a later observation may upgrade a stored config, never downgrade it.
PROVENANCES = ("inferred", "reconstructed_from_git", "captured_at_runtime")

LIBS = ("deepagents", "langgraph", "langchain", "langchain-core", "langchain-openrouter",
        "fastmcp", "mcp", "httpx", "pydantic")

# Files whose bytes decide behaviour that the extracted values cannot show.
# Examples are the FMP caps written inline as literals, retry logic and
# _schema_to_pydantic. Prompts are covered separately through texts.
_MODULE_FILES = ("roles.py", "deep_agent_factory.py", "langchain_bridge.py", "server.py")

_FMP_CONSTANTS = ("_TIMEOUT", "_DEFAULT_TTL", "_CACHE_MAX", "_FAST_FAIL_ATTEMPTS", "_TIMEOUT_ATTEMPTS", "_BACKOFF")

_PROBE_TEMPLATE = "{tool_rounds}|{timeout_s}|{max_tokens}|{write_by}"


class UnsupportedLayout(RuntimeError):
    """The tree predates the parallel deepagents pipeline; there is nothing comparable to snapshot."""


# ── Hashing ───────────────────────────────────────────────────────────────────


def normalise_text(s: str) -> str:
    """CRLF and lone CR to LF: what read_text's universal newlines already does to a file."""
    return s.replace("\r\n", "\n").replace("\r", "\n")


def sha256_text(s: str) -> str:
    return hashlib.sha256(normalise_text(s).encode("utf-8")).hexdigest()


def _canon(obj: Any) -> Any:
    if obj is None or isinstance(obj, (bool, str, int)):
        return obj
    if isinstance(obj, float):
        if not math.isfinite(obj):
            raise ValueError(f"non-finite number in snapshot: {obj!r}")
        return int(obj) if obj.is_integer() else obj
    if isinstance(obj, dict):
        return {str(k): _canon(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_canon(v) for v in obj]
    if isinstance(obj, (set, frozenset)):
        return sorted(_canon(v) for v in obj)
    raise TypeError(f"not JSON-canonicalisable: {type(obj).__name__}")


def canonical_json(obj: Any) -> str:
    return json.dumps(_canon(obj), sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)


def sha256_json(obj: Any) -> str:
    return hashlib.sha256(canonical_json(obj).encode("utf-8")).hexdigest()


def config_sha(content: dict) -> str:
    return sha256_json(content)


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


# ── The snapshot ──────────────────────────────────────────────────────────────


@dataclass
class Snapshot:
    """
    One config, already split into the rows of the hparams tables.

    ``content`` is what ``sha`` hashes. It holds text and tool hashes, never
    bodies. ``provenance``, ``effective_at``, ``gaps``, ``libs`` and the git
    fields describe how the snapshot was observed, so they are outside the hash.
    A reconstructed config and a runtime-captured one with identical code
    therefore collide, as they should.
    """

    sha: str
    content: dict
    provenance: str
    effective_at: str
    last_seen_at: str | None = None
    source_git_sha: str | None = None
    source_git_dirty: bool | None = None
    gaps: list[str] = field(default_factory=list)
    libs: dict | None = None
    label: str | None = None
    notes: str | None = None
    texts: dict[str, str] = field(default_factory=dict)
    tool_defs: list[dict] = field(default_factory=list)
    runtime: dict = field(default_factory=dict)
    agents: list[dict] = field(default_factory=list)
    tools: list[dict] = field(default_factory=list)
    role_tools: list[dict] = field(default_factory=list)

    def config_row(self) -> dict:
        return {
            "config_sha": self.sha, "snapshot_version": self.content.get("snapshot_version"),
            "provenance": self.provenance, "effective_at": self.effective_at,
            "last_seen_at": self.last_seen_at or self.effective_at,
            "source_git_sha": self.source_git_sha, "source_git_dirty": self.source_git_dirty,
            "gaps": list(self.gaps), "libs": self.libs, "content": self.content,
            "label": self.label, "notes": self.notes,
        }

    def to_record(self) -> dict:
        """JSON-safe and self-contained (it carries the text bodies), as written to runs/<id>/config.json."""
        return {
            "snapshot_version": SNAPSHOT_VERSION, "config": self.config_row(), "texts": self.texts,
            "tool_defs": self.tool_defs, "runtime": self.runtime, "agents": self.agents,
            "tools": self.tools, "role_tools": self.role_tools,
        }

    @classmethod
    def from_record(cls, rec: dict) -> Snapshot:
        cfg = rec["config"]
        return cls(
            sha=cfg["config_sha"], content=cfg["content"], provenance=cfg["provenance"],
            effective_at=cfg["effective_at"], last_seen_at=cfg.get("last_seen_at"),
            source_git_sha=cfg.get("source_git_sha"),
            source_git_dirty=cfg.get("source_git_dirty"), gaps=list(cfg.get("gaps") or []),
            libs=cfg.get("libs"), label=cfg.get("label"), notes=cfg.get("notes"),
            texts=dict(rec.get("texts") or {}), tool_defs=list(rec.get("tool_defs") or []),
            runtime=dict(rec.get("runtime") or {}), agents=list(rec.get("agents") or []),
            tools=list(rec.get("tools") or []), role_tools=list(rec.get("role_tools") or []),
        )

    def problems(self) -> list[str]:
        """Internal-consistency failures, one string each. Empty means the snapshot is sound."""
        out: list[str] = []
        if config_sha(self.content) != self.sha:
            out.append("config_sha does not match content")
        for sha, body in self.texts.items():
            if sha256_text(body) != sha or normalise_text(body) != body:
                out.append(f"text {sha[:12]} does not hash to its key (or is not LF-normalised)")
            if "\x00" in body:
                out.append(f"text {sha[:12]} contains NUL, which Postgres text cannot store")
        defs = {d["tool_sha"] for d in self.tool_defs}
        tags = {t["tool_name"]: set(t["tags"]) for t in self.tools}
        for t in self.tools:
            if t["tool_sha"] not in defs:
                out.append(f"tool {t['tool_name']} references a missing definition")
        granted: dict[str, set[str]] = {}
        for rt in self.role_tools:
            granted.setdefault(rt["role"], set()).add(rt["tool_name"])
        for a in self.agents:
            role = a["role"]
            for col in ("system_prompt_sha", "budget_sha", "composed_prompt_sha"):
                if a.get(col) and a[col] not in self.texts:
                    out.append(f"{role}.{col} references a missing text")
            sp, bd, cp = (self.texts.get(a.get(c) or "") for c in ("system_prompt_sha", "budget_sha", "composed_prompt_sha"))
            if a.get("prompt_source") == "file" and sp is not None and cp is not None and cp != sp + (bd or ""):
                out.append(f"{role}: composed prompt is not system prompt + budget block")
            rule = {n for n, tg in tags.items() if role in tg or "shared" in tg}
            if granted.get(role, set()) != rule:
                out.append(f"{role}: access rows differ from the tag rule "
                           f"(+{sorted(granted.get(role, set()) - rule)} -{sorted(rule - granted.get(role, set()))})")
            if a.get("tool_count") != len(granted.get(role, set())):
                out.append(f"{role}: tool_count {a.get('tool_count')} != {len(granted.get(role, set()))} access rows")
        return out


def collect_libs() -> dict[str, str | None]:
    from importlib import metadata

    out: dict[str, str | None] = {}
    for name in LIBS:
        try:
            out[name] = metadata.version(name)
        except metadata.PackageNotFoundError:
            out[name] = None
    return out


# ── Extraction helpers ────────────────────────────────────────────────────────


class _Gaps(list):
    def get(self, mod: Any, name: str, label: str) -> Any:
        if hasattr(mod, name):
            return getattr(mod, name)
        self.append(f"{label}.{name}:missing")
        return None


@contextlib.contextmanager
def _patched(target: Any, name: str, value: Any) -> Iterator[None]:
    missing = object()
    old = getattr(target, name, missing)
    setattr(target, name, value)
    try:
        yield
    finally:
        if old is missing:
            delattr(target, name)
        else:
            setattr(target, name, old)


@contextlib.contextmanager
def _overrides(overrides: dict[str, Any]) -> Iterator[None]:
    """Apply ``{"deep_agent_factory._AGENT_TIMEOUT_S": 600}``-style overrides for the duration."""
    with contextlib.ExitStack() as stack:
        for key, value in overrides.items():
            mod_name, _, attr = key.rpartition(".")
            mod = importlib.import_module(f"equity_mcp.{mod_name}")
            if not hasattr(mod, attr):
                raise UnsupportedLayout(f"override target {key} does not exist in this tree")
            stack.enter_context(_patched(mod, attr, value))
        yield


class _ModelStub:
    """What the capturing init_chat_model returns: the spec and kwargs, no client."""

    def __init__(self, spec: Any, kwargs: dict) -> None:
        self.spec = spec
        self.kwargs = kwargs


def _capture_build(captured: dict, kind: str):
    def _stub(*args: Any, **kwargs: Any) -> object:
        captured["kind"] = kind
        captured["model"] = kwargs.get("model", args[0] if args else None)
        captured["tools"] = kwargs.get("tools", args[1] if len(args) > 1 else None)
        captured["prompt"] = kwargs.get("prompt", kwargs.get("system_prompt"))
        return object()
    return _stub


def _stage_tasks(daf: Any, gaps: _Gaps) -> dict[str, str | None]:
    """
    The portfolio and head tasks. They are literals inside ``run_research``, not entries in ``_TASKS``.

    They are read out of the function's own source with ``ast``, so a reworded
    task shows up here without anyone remembering to mirror it.
    """
    out: dict[str, str | None] = {"portfolio_strategist": None, "head_of_research": None}
    try:
        tree = ast.parse(textwrap.dedent(inspect.getsource(daf.run_research)))
    except (OSError, TypeError, SyntaxError, AttributeError):
        gaps.append("task_literal_unparsed")
        return out
    for node in ast.walk(tree):
        if (isinstance(node, ast.Call) and getattr(node.func, "id", None) == "_run_one_agent"
                and node.args and getattr(node.args[0], "id", None) == "ROLE_PORTFOLIO"
                and len(node.args) >= 3 and isinstance(node.args[2], ast.Constant)):
            out["portfolio_strategist"] = node.args[2].value
        if (isinstance(node, ast.Assign) and any(getattr(t, "id", None) == "memo_task" for t in node.targets)
                and isinstance(node.value, ast.Constant)):
            out["head_of_research"] = node.value.value
    for role, task in out.items():
        if task is None:
            gaps.append(f"task_literal_unparsed:{role}")
    return out


def _probe_budget(daf: Any, recursion_limit: int, timeout_s: float, max_tokens: int,
                  is_master: bool) -> tuple[str, dict | None]:
    """
    ``(rendered_block, advertised_values)``, both from the real ``_budget_block``.

    The advertised values are obtained without re-implementing the 75% rule. A
    second render swaps ``_BUDGET_TEMPLATE`` for a template of bare
    placeholders, which yields the numbers the model is told. The swap is
    synchronous inside try/finally, so nothing else can render a prompt
    meanwhile.
    """
    def _render() -> str:
        try:
            return daf._budget_block(recursion_limit, timeout_s, max_tokens, is_master=is_master)
        except TypeError:  # older _budget_block without is_master
            return daf._budget_block(recursion_limit, timeout_s, max_tokens)

    block = _render()
    if not block:
        return block, None
    with tempfile.TemporaryDirectory() as tmp:
        probe = Path(tmp) / "probe.md"
        probe.write_text(_PROBE_TEMPLATE, encoding="utf-8")
        with _patched(daf, "_BUDGET_TEMPLATE", probe):
            raw = _render()
    first = raw.strip().splitlines()[0] if raw.strip() else ""
    parts = first.split("|")
    if len(parts) != 4:
        return block, None
    rounds, adv_timeout, _, write_by = parts
    return block, {"tool_rounds": int(rounds), "timeout_s": float(adv_timeout), "write_by": int(write_by)}


def _module_hashes(pkg: Path) -> dict[str, str]:
    files = [pkg / f for f in _MODULE_FILES] + sorted((pkg / "tools").rglob("*.py"))
    return {p.relative_to(pkg).as_posix(): sha256_text(p.read_text(encoding="utf-8")) for p in files if p.exists()}


async def _list_tools(lb: Any, server: Any) -> list[Any]:
    if hasattr(lb, "_list_tools_once"):
        return list(await lb._list_tools_once())
    from fastmcp import Client  # trees before the listing cache

    async with Client(server.mcp) as client:
        return list(await client.list_tools())


# ── Build ─────────────────────────────────────────────────────────────────────


async def build_snapshot(
    *,
    provenance: str = "captured_at_runtime",
    overrides: dict[str, Any] | None = None,
    effective_at: str | None = None,
    source_git_sha: str | None = None,
    source_git_dirty: bool | None = None,
    libs: bool = True,
    label: str | None = None,
    notes: str | None = None,
) -> Snapshot:
    """
    Snapshot the pipeline as the current interpreter has it imported.

    It is called once at run start in the orchestrator (capture.py), and by the
    backfill in a subprocess whose ``sys.path`` puts an old tree first.
    *overrides* reproduces a run whose working tree differed from any commit in
    a known way, e.g. ``{"deep_agent_factory._AGENT_TIMEOUT_S": 600.0}``.
    Such a snapshot is a different config, and is marked ``inferred``.
    """
    if provenance not in PROVENANCES:
        raise ValueError(f"provenance must be one of {PROVENANCES}")
    gaps = _Gaps()

    try:
        daf = importlib.import_module("equity_mcp.deep_agent_factory")
    except ImportError as exc:
        raise UnsupportedLayout(f"no deep_agent_factory: {exc}") from exc
    if not hasattr(daf, "run_specialists") or not hasattr(daf, "build_specialist_agent"):
        raise UnsupportedLayout("deep_agent_factory has no parallel specialist fan-out")
    lb = importlib.import_module("equity_mcp.langchain_bridge")
    roles = importlib.import_module("equity_mcp.roles")
    server = importlib.import_module("equity_mcp.server")
    try:
        fmp = importlib.import_module("equity_mcp.tools.external.fmp")
    except ImportError:
        fmp = None
        gaps.append("fmp:missing")

    texts: dict[str, str] = {}

    def keep(body: str | None) -> str | None:
        if not body:
            return None
        body = normalise_text(body)
        sha = sha256_text(body)
        texts[sha] = body
        return sha

    with _overrides(overrides or {}):
        # 1. Tools: definitions and tags, straight from the registry the bridge filters.
        listed = sorted(await _list_tools(lb, server), key=lambda t: t.name)
        tool_defs: list[dict] = []
        tools: list[dict] = []
        tags_of: dict[str, list[str]] = {}
        for t in listed:
            fn = getattr(server, t.name, None)
            impl = module = None
            if fn is None:
                gaps.append(f"tool_impl_not_found:{t.name}")
            else:
                module = getattr(fn, "__module__", None)
                try:
                    impl = sha256_text(inspect.getsource(inspect.unwrap(fn)))
                except (OSError, TypeError):
                    gaps.append(f"tool_source_unavailable:{t.name}")
            # MCP SDK v2 renamed inputSchema; the old spelling still works there but warns.
            schema = getattr(t, "input_schema", None)
            if schema is None:
                schema = getattr(t, "inputSchema", None)
            d = {"tool_name": t.name, "module": module, "description": t.description or "",
                 "input_schema": schema or {}, "impl_sha256": impl}
            d["tool_sha"] = sha256_json({k: d[k] for k in ("tool_name", "module", "description",
                                                           "input_schema", "impl_sha256")})
            tool_defs.append(d)
            tags_of[t.name] = sorted(lb._tags_of(t))
            tools.append({"tool_name": t.name, "tool_sha": d["tool_sha"], "tags": tags_of[t.name]})
        tool_sha_of = {t["tool_name"]: t["tool_sha"] for t in tools}

        # 2. Agents. The limits each role really runs under are the ones _run_one_agent receives:
        #    its own defaults for the fan-out and the strategist, explicit master values for the memo.
        g = gaps.get
        params = inspect.signature(daf._run_one_agent).parameters
        spec_limit = params["recursion_limit"].default if "recursion_limit" in params else None
        spec_tokens = params["max_tokens"].default if "max_tokens" in params else None
        master_limit = g(daf, "_MASTER_RECURSION_LIMIT", "deep_agent_factory")
        memo_tokens = g(daf, "_MEMO_MAX_TOKENS", "deep_agent_factory")
        agent_timeout = g(daf, "_AGENT_TIMEOUT_S", "deep_agent_factory")
        tasks = dict(getattr(daf, "_TASKS", {}) or {})
        stage_tasks = _stage_tasks(daf, gaps)
        portfolio = getattr(roles, "ROLE_PORTFOLIO", "portfolio_strategist")
        head = getattr(roles, "ROLE_HEAD_OF_RESEARCH", "head_of_research")
        default_model = g(roles, "DEFAULT_MODEL", "roles")
        overrides_map = dict(g(roles, "AGENT_MODELS", "roles") or {})

        model_calls: list[tuple[Any, dict]] = []

        def _init_stub(spec: Any, **kwargs: Any) -> _ModelStub:
            model_calls.append((spec, kwargs))
            return _ModelStub(spec, kwargs)

        import langchain.chat_models as lcm

        agents: list[dict] = []
        role_tools: list[dict] = []
        advertised_fraction: float | None = None
        transport: dict = {}
        with _patched(lcm, "init_chat_model", _init_stub):
            for role in roles.ALL_ROLES:
                is_head = role == head
                limit, tokens = (master_limit, memo_tokens) if is_head else (spec_limit, spec_tokens)
                captured: dict = {}
                try:
                    with _patched(daf, "create_react_agent", _capture_build(captured, "react_specialist")), \
                         _patched(daf, "create_deep_agent", _capture_build(captured, "deep_master")):
                        if is_head:
                            await daf.build_head_agent(max_tokens=tokens, recursion_limit=limit)
                        else:
                            await daf.build_specialist_agent(role, max_tokens=tokens, recursion_limit=limit)
                except Exception as exc:  # noqa: BLE001 - a builder that cannot run is a gap, not a crash
                    gaps.append(f"builder_failed:{role}:{type(exc).__name__}")

                system = daf._load_prompt(role)
                prompt_source = "file" if (Path(daf._PROMPTS) / f"{role}.md").exists() else "fallback"
                block, adv = _probe_budget(daf, limit, agent_timeout, tokens, is_head)
                if captured.get("prompt") is not None:
                    composed = captured["prompt"]
                else:
                    composed = system + block
                    gaps.append(f"composed_prompt_not_captured:{role}")

                model = captured.get("model")
                spec, kwargs = (model.spec, model.kwargs) if isinstance(model, _ModelStub) else (None, {})
                if spec is None:
                    gaps.append(f"model_not_captured:{role}")
                if not transport and kwargs:
                    transport = kwargs

                names = sorted(t.name for t in (captured.get("tools") or []))
                for name in names:
                    role_tools.append({"role": role, "tool_name": name,
                                       "via": "role" if role in tags_of.get(name, ()) else "shared"})

                if adv is not None and agent_timeout:
                    advertised_fraction = round(adv["timeout_s"] / agent_timeout, 6)
                row = {
                    "role": role,
                    "stage": 3 if is_head else 2 if role == portfolio else 1,
                    "agent_kind": captured.get("kind") or ("deep_master" if is_head else "react_specialist"),
                    "model_slug": overrides_map.get(role, default_model),
                    "model_spec": spec,
                    "max_tokens": kwargs.get("max_tokens", tokens),
                    "recursion_limit": limit,
                    "advertised_recursion_limit": (max(3, int(limit * advertised_fraction))
                                                   if adv and limit and advertised_fraction else None),
                    "advertised_tool_rounds": adv["tool_rounds"] if adv else None,
                    "advertised_write_by": adv["write_by"] if adv else None,
                    "advertised_timeout_s": adv["timeout_s"] if adv else None,
                    "task": stage_tasks.get(role) if role in stage_tasks else
                            tasks.get(role, "Conduct your analysis for this company."),
                    "prompt_source": prompt_source,
                    "system_prompt_sha": keep(system),
                    "budget_sha": keep(block),
                    "composed_prompt_sha": keep(composed),
                    "tool_count": len(names),
                }
                agents.append(row)

        # 3. Runtime: code defaults only. What one invocation overrode goes in run_configs.
        template = Path(daf._BUDGET_TEMPLATE) if hasattr(daf, "_BUDGET_TEMPLATE") else None
        runtime = {
            "tool_timeout_s": g(lb, "_TOOL_TIMEOUT_S", "langchain_bridge"),
            "max_tool_threads": g(lb, "_MAX_TOOL_THREADS", "langchain_bridge"),
            "specialist_max_tokens": g(daf, "_SPECIALIST_MAX_TOKENS", "deep_agent_factory"),
            "memo_max_tokens": memo_tokens,
            "specialist_recursion_limit": g(daf, "_SPECIALIST_RECURSION_LIMIT", "deep_agent_factory"),
            "master_recursion_limit": master_limit,
            "agent_timeout_s": agent_timeout,
            "default_max_concurrency": g(daf, "_DEFAULT_MAX_CONCURRENCY", "deep_agent_factory"),
            "advertised_fraction": advertised_fraction,
            "request_timeout_ms": transport.get("timeout"),
            "streaming": transport.get("streaming"),
            "provider_routing": transport.get("openrouter_provider"),
            "default_model": default_model,
            "agent_model_overrides": overrides_map,
            "budget_template_sha": keep(template.read_text(encoding="utf-8"))
                                   if template is not None and template.exists() else None,
            "extra": {f"fmp.{n}": (sorted(v) if isinstance(v, (set, frozenset)) else v)
                      for n in _FMP_CONSTANTS + ("_RETRY_STATUS",)
                      if fmp is not None and (v := getattr(fmp, n, None)) is not None},
        }
        if advertised_fraction is None:
            gaps.append("budget_block:not_rendered")

    module_sha = _module_hashes(Path(daf.__file__).resolve().parent)
    agent_content = {a["role"]: {**{k: v for k, v in a.items() if k != "role"},
                                 "tools": [rt["tool_name"] for rt in role_tools if rt["role"] == a["role"]]}
                     for a in agents}
    for a in agents:
        a["agent_sha"] = sha256_json({**agent_content[a["role"]],
                                      "tools": [[n, tool_sha_of[n]] for n in agent_content[a["role"]]["tools"]]})
    content = {
        "snapshot_version": SNAPSHOT_VERSION,
        "runtime": runtime,
        "agents": agent_content,
        "tools": {t["tool_name"]: {"tool_sha": t["tool_sha"], "tags": t["tags"]} for t in tools},
        "module_sha256": module_sha,
    }
    return Snapshot(
        sha=config_sha(content), content=_canon(content), provenance=provenance,
        effective_at=effective_at or _now(), source_git_sha=source_git_sha, source_git_dirty=source_git_dirty,
        gaps=sorted(set(gaps)), libs=collect_libs() if libs else None, label=label, notes=notes,
        texts=texts, tool_defs=tool_defs, runtime=runtime, agents=agents, tools=tools, role_tools=role_tools,
    )
