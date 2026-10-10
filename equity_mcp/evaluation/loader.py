"""
Load and validate the metrics/*.yaml rubrics.

Each rubric is merged with _shared.yaml and hashed. ``rubric_sha`` is part of
the idempotency key stored in Supabase, so editing a single instruction makes
every past run eligible for re-evaluation under the new wording, and leaves the
old answers alone.

The prompt-drift guard exists because a rubric is a reading of one prompt. When
``prompts/<role>.md`` changes, the enums and required sections the rubric checks
for may no longer exist. Prompts are hashed with line endings normalised, so a
Windows checkout with autocrlf hashes the same as CI.
"""

from __future__ import annotations

import hashlib
import json
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

from equity_mcp.evaluation.schema import Alignment, Rubric, SharedRubric
from equity_mcp.roles import ALL_ROLES

PACKAGE_DIR = Path(__file__).resolve().parent.parent
METRICS_DIR = PACKAGE_DIR / "metrics"
PROMPTS_DIR = PACKAGE_DIR / "prompts"
REPO_ROOT = PACKAGE_DIR.parent


class RubricError(Exception):
    """A rubric file is missing, malformed or inconsistent. Always fatal: nothing is sent."""


def prompt_sha256(role: str) -> str:
    text = (PROMPTS_DIR / f"{role}.md").read_text(encoding="utf-8")
    return hashlib.sha256(text.replace("\r\n", "\n").encode("utf-8")).hexdigest()


def _canonical(obj: Any) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_json(obj: Any) -> str:
    return hashlib.sha256(_canonical(obj).encode("utf-8")).hexdigest()


def _read_yaml(path: Path) -> dict:
    if not path.exists():
        raise RubricError(f"missing rubric file: {path}")
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise RubricError(f"{path.name}: invalid YAML: {exc}") from exc
    if not isinstance(data, dict):
        raise RubricError(f"{path.name}: top level must be a mapping")
    return data


@lru_cache(maxsize=1)
def load_shared() -> SharedRubric:
    path = METRICS_DIR / "_shared.yaml"
    try:
        return SharedRubric.model_validate(_read_yaml(path))
    except ValueError as exc:  # pydantic.ValidationError subclasses ValueError
        raise RubricError(f"{path.name}: {exc}") from exc


class LoadedRubric:
    """A role rubric merged with _shared.yaml, ready to evaluate with."""

    def __init__(self, rubric: Rubric, shared: SharedRubric) -> None:
        self.rubric = rubric
        self.shared = shared
        self.role = rubric.role
        self.alignment = Alignment(
            deterministic_checks=[*shared.alignment.deterministic_checks, *rubric.alignment.deterministic_checks],
            requests=[*shared.alignment.requests, *rubric.alignment.requests],
        )
        self._check_unique_ids()
        self.content: dict = {
            "role": rubric.model_dump(mode="json", by_alias=True),
            "shared": shared.model_dump(mode="json", by_alias=True),
        }
        self.sha = sha256_json(self.content)

    def _check_unique_ids(self) -> None:
        seen: dict[str, str] = {}
        reserved = {"stance", "stance_gate", "conviction_level"}
        ids: list[tuple[str, str]] = [(c.id, "check") for c in self.alignment.deterministic_checks]
        for req in self.alignment.requests:
            ids += [(qid, f"request {req.id}") for qid in req.questions]
        ids += [(mid, "domain metric") for mid in self.rubric.conviction.domain_metrics]
        for qid, where in ids:
            if qid in reserved:
                raise RubricError(f"{self.role}: id '{qid}' ({where}) is reserved for the shared conviction block")
            if qid in seen:
                raise RubricError(f"{self.role}: duplicate id '{qid}' in {where} and {seen[qid]}")
            seen[qid] = where
        req_ids = [r.id for r in self.alignment.requests]
        if len(req_ids) != len(set(req_ids)):
            raise RubricError(f"{self.role}: duplicate request ids {req_ids}")

    @property
    def pass_(self) -> int:
        return self.rubric.pass_

    def snapshot_row(self) -> dict:
        """The eval.rubrics row for this rubric (read back by the eval.v_rubric_* views)."""
        return {
            "rubric_sha": self.sha, "role": self.role, "rubric_version": self.rubric.rubric_version,
            "shared_version": self.shared.shared_version, "source_prompt_sha256": self.rubric.source_prompt_sha256,
            "calibrated": self.rubric.calibrated, "content": self.content,
        }

    def prompt_drift(self) -> str | None:
        """A message if the prompt changed since the rubric was written, else None."""
        current = prompt_sha256(self.role)
        if self.rubric.source_prompt_sha256 != current:
            return (
                f"{self.role}: prompts/{self.role}.md changed since this rubric was written "
                f"(rubric {self.rubric.source_prompt_sha256[:12]}…, prompt {current[:12]}…). "
                f"Review metrics/{self.role}.yaml, then update source_prompt_sha256."
            )
        return None


def load_rubric(role: str) -> LoadedRubric:
    path = METRICS_DIR / f"{role}.yaml"
    try:
        rubric = Rubric.model_validate(_read_yaml(path))
    except ValueError as exc:
        raise RubricError(f"{path.name}: {exc}") from exc
    if rubric.role != role:
        raise RubricError(f"{path.name}: declares role '{rubric.role}'")
    if rubric.includes != ["_shared"]:
        raise RubricError(f"{path.name}: includes must be [_shared]")
    return LoadedRubric(rubric, load_shared())


def load_all(roles: list[str] | None = None) -> dict[str, LoadedRubric]:
    return {role: load_rubric(role) for role in (roles or ALL_ROLES)}


def validate_all() -> list[str]:
    """Every problem across all rubrics, one string each. Empty means valid."""
    problems: list[str] = []
    expected = {f"{r}.yaml" for r in ALL_ROLES} | {"_shared.yaml"}
    present = {p.name for p in METRICS_DIR.glob("*.yaml")}
    problems += [f"missing rubric file: {n}" for n in sorted(expected - present)]
    problems += [f"unexpected file in metrics/: {n}" for n in sorted(present - expected)]
    try:
        load_shared()
    except RubricError as exc:
        return problems + [str(exc)]
    for role in ALL_ROLES:
        if f"{role}.yaml" not in present:
            continue
        try:
            loaded = load_rubric(role)
        except RubricError as exc:
            problems.append(str(exc))
            continue
        drift = loaded.prompt_drift()
        if drift:
            problems.append(drift)
    return problems
