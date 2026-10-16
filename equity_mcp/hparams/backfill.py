"""
Reconstruct hyperparameter snapshots for runs that predate runtime capture.

No stored run recorded its config, ``prompt_sha256`` or ``models``: those
arrived after the last of them. So the config each run used is recovered from
git, with the run's own evidence as a check:

1. **Which runs.** Every ``outputs/*.json`` with ``agent_results``. Legacy
   layouts are skipped; they ran a different pipeline. Without ``--dry-run``,
   only runs present in ``eval.runs`` are linked, because the link references
   them.
2. **CI or local.** A run whose output was added by a ``research:`` commit ran
   in CI. Its stamp is the runner's UTC clock, and it ran the commit that
   triggered the job: the latest code commit before the stamp. Any other run ran
   on a developer machine, stamped in that commit's timezone, possibly on an
   uncommitted tree.
3. **Candidates.** For a local run, the last code commit before the stamp
   (C0) and the first one after it (C1). C1 is preferred, because work in
   progress lands in the next commit. A tree is rejected when the run used
   something it lacks, e.g. a run.log needs a tree with ``run_log.py``.
4. **Fingerprints.**
   - An agent that died with ``TimeoutError`` after *e* seconds ran under an
     agent timeout of about *e*. If that disagrees with the candidate's
     ``_AGENT_TIMEOUT_S``, the candidate is used with an override, which makes a
     distinct, ``inferred`` config.
   - An agent that ran longer than the timeout rules the candidate out.
5. **Basis.** CI runs, and local runs whose candidates have identical code,
   are ``git_checkout``. Every other local run is ``inferred``. The notes
   explain each choice.
6. **Extraction.**
   - ``git archive`` writes the chosen tree to a temp directory outside the
     repo, and a subprocess runs the *current* snapshot.py against it.
   - Nothing is checked out, and no worktree is created.
   - The installed libraries are today's, so a reconstructed config has
     ``libs = NULL`` and the gap ``libs_unknown_reconstructed``.
"""

from __future__ import annotations

import ast
import io
import json
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from equity_mcp.hparams.ingest import link_row
from equity_mcp.hparams.snapshot import Snapshot

REPO_ROOT = Path(__file__).resolve().parents[2]
SNAPSHOT_PY = Path(__file__).resolve().parent / "snapshot.py"

# The code a snapshot reads. Two commits equal on these give the same config.
WATCHED = ("equity_mcp/prompts", "equity_mcp/roles.py", "equity_mcp/deep_agent_factory.py",
           "equity_mcp/langchain_bridge.py", "equity_mcp/server.py", "equity_mcp/tools")

_STAMP = re.compile(r"_(\d{8}T\d{6})$")
_TOLERANCE_S = 5.0
_TIMEOUT_KEY = "deep_agent_factory._AGENT_TIMEOUT_S"

_EXTRACT_STUB = r"""
import asyncio, importlib.util, json, sys
from pathlib import Path
tree, snapshot_py, out, kwargs = sys.argv[1:5]
sys.path.insert(0, tree)
spec = importlib.util.spec_from_file_location("hparams_snapshot", snapshot_py)
mod = importlib.util.module_from_spec(spec)
sys.modules["hparams_snapshot"] = mod
spec.loader.exec_module(mod)
import equity_mcp
loaded = Path(equity_mcp.__file__).resolve()
if not loaded.is_relative_to(Path(tree).resolve()):
    sys.exit(f"equity_mcp resolved to {loaded}, not the extracted tree: the editable install shadows it")
snap = asyncio.run(mod.build_snapshot(**json.loads(kwargs)))
Path(out).write_text(json.dumps(snap.to_record(), ensure_ascii=False), encoding="utf-8")
"""


# ── git ───────────────────────────────────────────────────────────────────────


def git(*args: str, binary: bool = False) -> Any:
    out = subprocess.run(["git", *args], cwd=REPO_ROOT, capture_output=True, timeout=60)
    if out.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {out.stderr.decode('utf-8', 'replace').strip()}")
    return out.stdout if binary else out.stdout.decode("utf-8").strip()


@dataclass(frozen=True)
class Commit:
    sha: str
    at: datetime
    subject: str


def code_commits() -> list[Commit]:
    """Every ancestor of HEAD except the CI's own ``research:`` result commits, oldest first."""
    rows = []
    for line in git("log", "--date-order", "--format=%H%x09%cI%x09%s", "HEAD").splitlines():
        sha, at, subject = line.split("\t", 2)
        if not subject.startswith("research:"):
            rows.append(Commit(sha, datetime.fromisoformat(at), subject))
    return sorted(rows, key=lambda c: c.at)


def same_code(a: str, b: str) -> bool:
    return subprocess.run(["git", "diff", "--quiet", a, b, "--", *WATCHED], cwd=REPO_ROOT).returncode == 0


def has_path(sha: str, path: str) -> bool:
    return subprocess.run(["git", "cat-file", "-e", f"{sha}:{path}"], cwd=REPO_ROOT,
                          capture_output=True).returncode == 0


def agent_timeout_at(sha: str) -> float | None:
    """``_AGENT_TIMEOUT_S`` in that tree, read statically. Used to choose a candidate, never stored."""
    try:
        src = git("show", f"{sha}:equity_mcp/deep_agent_factory.py")
    except RuntimeError:
        return None
    for node in ast.parse(src).body:
        if (isinstance(node, (ast.Assign, ast.AnnAssign)) and isinstance(node.value, ast.Constant)
                and any(getattr(t, "id", None) == "_AGENT_TIMEOUT_S"
                        for t in (node.targets if isinstance(node, ast.Assign) else [node.target]))):
            return float(node.value.value)
    return None


# ── Run evidence ──────────────────────────────────────────────────────────────


@dataclass
class RunEvidence:
    run_id: str
    path: Path
    kind: str                   # "ci" | "local"
    start: datetime
    end: datetime
    run_params: dict | None
    timeouts: list[tuple[str, float]]
    max_elapsed: float
    has_run_log: bool


def parse_start_line(text: str) -> dict | None:
    """``run_params`` from a run.log START line, in the shape capture.py records."""
    m = re.search(r"START\s+(.*)", text)
    if not m:
        return None
    kv = dict(tok.split("=", 1) for tok in m.group(1).split() if "=" in tok)
    out: dict[str, Any] = {}
    if "concurrency" in kv:
        out["max_concurrency"] = int(kv["concurrency"])
    if "timeout" in kv:
        out["timeout_s"] = None if kv["timeout"] == "None" else float(kv["timeout"])
    if "agents" in kv:
        out["agents_requested"] = None if kv["agents"] == "all" else kv["agents"].split(",")
    if "skip_synthesis" in kv:
        out["skip_synthesis"] = kv["skip_synthesis"] == "True"
    return out


def evidence(path: Path) -> RunEvidence | None:
    result = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(result.get("agent_results"), list):
        return None  # legacy layout
    run_id = result.get("run_id") or path.stem
    m = _STAMP.search(run_id)
    if not m:
        return None
    stamp = datetime.strptime(m.group(1), "%Y%m%dT%H%M%S")

    added = git("log", "--diff-filter=A", "--format=%aI%x09%s", "--", f"outputs/{path.name}").splitlines()
    first = added[-1].split("\t", 1) if added else None
    if first and first[1].startswith("research:"):
        kind, tz = "ci", timezone.utc
    else:
        kind = "local"
        tz = datetime.fromisoformat(first[0]).tzinfo if first else datetime.now().astimezone().tzinfo
    start = stamp.replace(tzinfo=tz)

    timings = dict(result.get("per_agent_timings") or {})
    for r in result["agent_results"]:
        timings.setdefault(r["agent_role"], r.get("elapsed_seconds") or 0.0)
    timeouts = [(r["agent_role"], float(r["elapsed_seconds"])) for r in result["agent_results"]
                if (r.get("error") or "").startswith("TimeoutError")]
    timed_out = {role for role, _ in timeouts}
    finished = [float(v) for k, v in timings.items() if k not in timed_out and v is not None]

    log = REPO_ROOT / "runs" / run_id / "run.log"
    params = parse_start_line(log.read_text(encoding="utf-8")) if log.exists() else None
    if params is not None:
        # The CI workflow passes no --focus; a local run's focus was never recorded.
        params["focus"] = "" if kind == "ci" else None
    return RunEvidence(
        run_id=run_id, path=path, kind=kind, start=start,
        end=start + timedelta(seconds=float(result.get("elapsed_seconds") or 0.0)),
        run_params=params, timeouts=timeouts, max_elapsed=max(finished, default=0.0), has_run_log=log.exists(),
    )


# ── Planning ──────────────────────────────────────────────────────────────────


@dataclass
class LinkPlan:
    run: RunEvidence
    sha: str | None = None
    overrides: dict = field(default_factory=dict)
    basis: str | None = None
    notes: list[str] = field(default_factory=list)

    @property
    def key(self) -> tuple[str, str]:
        return (self.sha or "", json.dumps(self.overrides, sort_keys=True))


def _fit(run: RunEvidence, sha: str) -> tuple[bool, dict, str]:
    """Whether *run* could have run on *sha*, the overrides that would take, and why."""
    if run.has_run_log and not has_path(sha, "equity_mcp/run_log.py"):
        return False, {}, f"{sha[:7]} has no run_log.py but the run wrote run.log"
    if not has_path(sha, "equity_mcp/deep_agent_factory.py"):
        return False, {}, f"{sha[:7]} predates deep_agent_factory.py"
    t = agent_timeout_at(sha)
    if t is None:
        return False, {}, f"{sha[:7]}: _AGENT_TIMEOUT_S unreadable"
    overrides: dict = {}
    why = f"{sha[:7]} timeout {t:g}s"
    if run.timeouts:
        seen = sorted({5 * round(e / 5) for _, e in run.timeouts})
        if len(seen) > 1 or abs(run.timeouts[0][1] - seen[0]) > _TOLERANCE_S:
            return False, {}, f"timeouts at {[e for _, e in run.timeouts]} disagree"
        if abs(seen[0] - t) > _TOLERANCE_S:
            overrides[_TIMEOUT_KEY] = float(seen[0])
            why += f"; TimeoutError at {run.timeouts[0][1]}s implies {seen[0]}s"
            t = float(seen[0])
    if run.max_elapsed > t + _TOLERANCE_S:
        return False, {}, f"{sha[:7]}: an agent ran {run.max_elapsed}s, past its {t:g}s timeout"
    return True, overrides, why


def plan(paths: list[Path], commits: list[Commit] | None = None) -> list[LinkPlan]:
    commits = commits if commits is not None else code_commits()
    plans: list[LinkPlan] = []
    for path in paths:
        run = evidence(path)
        if run is None:
            continue
        lp = LinkPlan(run)
        plans.append(lp)
        before = [c for c in commits if c.at <= run.start]
        after = [c for c in commits if c.at > run.start]
        c0 = before[-1] if before else None
        c1 = after[0] if after else None

        if run.kind == "ci":
            candidates = [c0] if c0 else []
        else:
            candidates = [c for c in (c1, c0) if c]
        fits = []
        for c in candidates:
            ok, overrides, why = _fit(run, c.sha)
            lp.notes.append(("ok " if ok else "rejected ") + why)
            if ok:
                fits.append((c, overrides))
        if not fits:
            lp.notes.append("no candidate commit fits; left unlinked")
            continue
        chosen, overrides = fits[0]
        lp.sha, lp.overrides = chosen.sha, overrides
        if run.kind == "ci":
            lp.basis = "inferred" if overrides else "git_checkout"
            lp.notes.insert(0, f"CI run; ran the trigger commit {chosen.sha[:7]}")
        else:
            others = [c for c in candidates if c.sha != chosen.sha]
            if not overrides and all(same_code(chosen.sha, c.sha) for c in others):
                lp.basis = "git_checkout"
                lp.notes.insert(0, f"local run; candidates have identical code; {chosen.sha[:7]}")
            else:
                lp.basis = "inferred"
                ambiguous = len(fits) > 1 and not same_code(fits[0][0].sha, fits[1][0].sha)
                lp.notes.insert(0, f"local run on an uncommitted tree; chose {chosen.sha[:7]}"
                                   + (f" over {fits[1][0].sha[:7]}, which also fits" if ambiguous else ""))
    return plans


# ── Extraction ────────────────────────────────────────────────────────────────


def extract_at(sha: str, *, provenance: str, overrides: dict | None = None,
               effective_at: str | None = None, notes: str | None = None, timeout_s: float = 300) -> Snapshot:
    """Snapshot the tree at *sha* by running the current snapshot.py against it in a subprocess."""
    tmp = Path(tempfile.mkdtemp(prefix="hparams_tree_"))
    try:
        data = git("archive", "--format=tar", sha, "equity_mcp", binary=True)
        with tarfile.open(fileobj=io.BytesIO(data)) as tar:
            tar.extractall(tmp, filter="data")
        out = tmp / "snapshot.json"
        kwargs = {"provenance": provenance, "overrides": overrides or {}, "effective_at": effective_at,
                  "source_git_sha": sha, "source_git_dirty": bool(overrides), "libs": False, "notes": notes}
        proc = subprocess.run(
            [sys.executable, "-I", "-X", "utf8", "-c", _EXTRACT_STUB, str(tmp), str(SNAPSHOT_PY), str(out),
             json.dumps(kwargs)],
            cwd=tmp, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout_s,
        )
        if proc.returncode != 0 or not out.exists():
            tail = (proc.stderr or proc.stdout).strip().splitlines()[-3:]
            raise RuntimeError(f"extracting {sha[:7]} failed: {' | '.join(tail)}")
        return Snapshot.from_record(json.loads(out.read_text(encoding="utf-8")))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def build_payloads(plans: list[LinkPlan], commits: list[Commit] | None = None) -> tuple[list[dict], list[str]]:
    """One payload per distinct (commit, overrides), carrying its run links. Returns (payloads, errors)."""
    commits = commits if commits is not None else code_commits()
    when = {c.sha: c.at for c in commits}
    groups: dict[tuple[str, str], list[LinkPlan]] = {}
    for lp in plans:
        if lp.sha:
            groups.setdefault(lp.key, []).append(lp)

    payloads, errors = [], []
    for (sha, _), members in groups.items():
        overrides = members[0].overrides
        starts = [m.run.start for m in members]
        effective = min([when[sha], *starts]).astimezone(timezone.utc)
        last_seen = max([when[sha], *starts]).astimezone(timezone.utc)
        note = ("override " + ", ".join(f"{k}={v:g}" for k, v in overrides.items()) +
                " (from run evidence; the run's working tree was uncommitted)") if overrides else None
        try:
            snap = extract_at(sha, provenance="inferred" if overrides else "reconstructed_from_git",
                              overrides=overrides, effective_at=effective.isoformat(timespec="seconds"),
                              notes=note)
        except Exception as exc:  # noqa: BLE001 - one bad tree leaves its runs unlinked, not the backfill dead
            errors.append(f"{sha[:7]}: {exc}")
            continue
        snap.last_seen_at = last_seen.isoformat(timespec="seconds")
        snap.gaps = sorted({*snap.gaps, "libs_unknown_reconstructed",
                            *(["working_tree_uncommitted_at_run"] if overrides else [])})
        links = [link_row(m.run.run_id, snap.sha, m.basis, m.run.run_params, research_git_sha=sha,
                          overrides=overrides, notes="; ".join(m.notes)) for m in members]
        payloads.append({"snapshot": snap.to_record(), "links": links})
    return payloads, errors
