"""
TypeSafe Jev client wrapper: state building, wire questions, response validation, caching.

Jev's own documented limits shape this module:

- **Context rot.** Accuracy drops as state fills with unrelated text, so the
  state is an object holding only the sections a question needs. A long report
  is capped at MAX_STATE_CHARS, and the truncation is recorded.
- **No confident default.** A transport failure, a 422 or a malformed answer
  becomes an ``error`` on the affected metrics, never a guessed value. A 401 or
  403 is fatal for the whole invocation, because every later call would fail
  the same way and each failure would look like a data problem.
- **A pinned model.** ``jev-latest`` is a moving alias, so results under it
  could not be compared across runs. The CLI refuses it unless told otherwise.

Retries belong to the SDK's ``RetryPolicy``, which already covers 408, 429,
5xx and 529 and honours ``Retry-After``. The default policy has a 30-second
*total* budget, which a 12k-character request under load can exceed, so it is
widened here.
"""

from __future__ import annotations

import asyncio
import hashlib
import json
import math
import time
from typing import Any

from equity_mcp.evaluation.schema import ChoiceQ, DomainMetric, NoulQ, ScoreQ

MAX_STATE_CHARS = 12000
DEFAULT_MODEL = "jev-1.13.0"


class FatalJevError(Exception):
    """Authentication, permission or configuration failure. Stops the invocation."""


def _canonical(obj: Any) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _sha(obj: Any) -> str:
    return hashlib.sha256(_canonical(obj).encode("utf-8")).hexdigest()


# ── Wire format ───────────────────────────────────────────────────────────────


def wire_question(q: NoulQ | ScoreQ | ChoiceQ | DomainMetric, *, reversed_options: bool = False) -> dict:
    """The JSON body for one question. Question ids are not part of it."""
    if isinstance(q, DomainMetric):
        return {"type": "score", "instructions": q.instructions.strip(), "criteria": list(q.criteria)}
    if isinstance(q, NoulQ):
        out: dict[str, Any] = {"type": "noul", "instructions": q.instructions.strip()}
        if q.criteria is not None:
            out["criteria"] = {"true": q.criteria.true, "false": q.criteria.false}
        return out
    if isinstance(q, ScoreQ):
        return {"type": "score", "instructions": q.instructions.strip(), "criteria": list(q.criteria)}
    items = list(q.criteria.items())
    if reversed_options:
        items.reverse()
    return {"type": "choice", "instructions": q.instructions.strip(), "criteria": dict(items)}


def build_state(
    *,
    role_label: str,
    mandate: str,
    required_output: str | None,
    run: dict,
    texts: list[str],
    specialist_summary: dict | None = None,
) -> tuple[dict, bool]:
    """``(state, truncated)``. ``report_section`` gets whatever budget the rest leaves."""
    state: dict[str, Any] = {
        "evaluation_context": {
            "agent_role": role_label,
            "agent_mandate": " ".join(mandate.split()),
        },
        "run": {
            "symbol": run.get("symbol"),
            "report_date": run.get("run_date"),
        },
    }
    if required_output:
        state["evaluation_context"]["required_output"] = required_output.strip()
    if specialist_summary is not None:
        state["specialist_summary"] = specialist_summary
    budget = MAX_STATE_CHARS - len(_canonical(state))
    report = "\n\n---\n\n".join(t.strip() for t in texts if t and t.strip())
    truncated = len(report) > budget
    state["report_section"] = report[: max(budget, 1000)]
    return state, truncated


# ── Response validation ───────────────────────────────────────────────────────


def _finite01(x: Any) -> bool:
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x) and -1e-9 <= x <= 1 + 1e-9


def _dist_ok(probs: Any, keys: set[str]) -> bool:
    if not isinstance(probs, dict) or not probs:
        return False
    if not set(map(str, probs)) <= keys:
        return False
    if not all(_finite01(v) for v in probs.values()):
        return False
    return abs(sum(probs.values()) - 1.0) <= 0.02


def validate_answer(wire: dict, answer: Any) -> str | None:
    """None if the answer fits its question, else the reason it does not."""
    if not isinstance(answer, dict):
        return "missing answer"
    if answer.get("type") != wire["type"]:
        return f"type {answer.get('type')!r} != {wire['type']!r}"
    if wire["type"] == "noul":
        return None if _finite01(answer.get("noul")) else f"noul out of range: {answer.get('noul')!r}"
    if wire["type"] == "choice":
        options = set(wire["criteria"])
        if answer.get("choice") not in options:
            return f"choice {answer.get('choice')!r} not among options"
        if not _finite01(answer.get("confidence")):
            return "confidence out of range"
        if not _dist_ok(answer.get("probabilities"), options):
            return "invalid probability distribution"
        return None
    n = len(wire["criteria"])
    score = answer.get("score")
    if not isinstance(score, (int, float)) or not math.isfinite(score) or not -1e-6 <= score <= n - 1 + 1e-6:
        return f"score {score!r} outside 0..{n - 1}"
    if not _finite01(answer.get("confidence")):
        return "confidence out of range"
    if not _dist_ok(answer.get("probabilities"), {str(i) for i in range(n)}):
        return "invalid probability distribution"
    return None


# ── Runner ────────────────────────────────────────────────────────────────────


class JevRunner:
    """
    Sends planned requests with bounded concurrency, through a two-level cache.

    The cache is in-memory first, then the store's ``jev_calls`` table. A hit
    costs nothing, which is what makes ``--force`` re-evaluations and rubric
    edits that touch one request cheap.
    """

    def __init__(
        self,
        *,
        model: str,
        concurrency: int = 4,
        dry_run: bool = False,
        store: Any = None,
        timeout_s: float = 120.0,
    ) -> None:
        self.model = model
        self.dry_run = dry_run
        self.store = store
        self._sem = asyncio.Semaphore(max(1, concurrency))
        self._memo: dict[str, dict] = {}
        self._client = None
        self._timeout_s = timeout_s

    async def __aenter__(self) -> JevRunner:
        if not self.dry_run:
            try:
                from typesafe_sdk import AsyncTypeSafeClient, RetryPolicy
            except ImportError as exc:
                raise FatalJevError("typesafe-sdk is not installed (pip install -e .)") from exc
            try:
                self._client = AsyncTypeSafeClient(
                    model=self.model,
                    retry=RetryPolicy(max_retries=4, backoff_initial=1.0, backoff_max=20.0, timeout=240.0),
                    timeout=self._timeout_s,
                )
            except Exception as exc:  # missing/invalid TYPESAFE_API_KEY is raised here
                raise FatalJevError(f"could not create Jev client: {exc}") from exc
            await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc: Any) -> None:
        if self._client is not None:
            await self._client.__aexit__(*exc)

    async def list_models(self) -> list[str]:
        if self._client is None:
            return []
        resp = await self._client.models.list()
        return [m.name for m in resp.models]

    async def call(self, state: dict, questions: dict[str, dict], truncated: bool = False) -> dict:
        """
        One System One request. Returns a jev_calls-shaped dict with ``answers``
        (raw wire answers keyed by question id) or ``error``. ``fatal`` is True
        only for auth or permission failures; the caller stops on those.
        """
        state_sha = _sha(state)
        questions_sha = _sha(questions)
        cache_key = _sha({"model": self.model, "state": state_sha, "questions": questions_sha})
        base = {
            "cache_key": cache_key,
            "state_sha256": state_sha,
            "questions_sha256": questions_sha,
            "jev_model_requested": self.model,
            "jev_model_returned": None,
            "request_id": None,
            "http_status": None,
            "latency_ms": None,
            "input_tokens": None,
            "output_tokens": None,
            "state_chars": len(_canonical(state)),
            "state_truncated": truncated,
            "answers": None,
            "error": None,
            "cached": False,
            "store_id": None,
        }
        if self.dry_run:
            return {**base, "error": "dry_run", "dry_run": True}

        if cache_key in self._memo:
            return {**self._memo[cache_key], "cached": True}
        if self.store is not None:
            hit = await self.store.cached_call(cache_key)
            if hit is not None:
                out = {**base, **hit, "cached": True}
                self._memo[cache_key] = out
                return out

        from typesafe_sdk import (
            TypeSafeAPIConnectionError,
            TypeSafeAPIError,
            TypeSafeAPIResponseValidationError,
            TypeSafeAuthenticationError,
            TypeSafeError,
            TypeSafePermissionDeniedError,
        )

        async with self._sem:
            t0 = time.monotonic()
            try:
                resp = await self._client.system_one(state, questions, model=self.model)
            except (TypeSafeAuthenticationError, TypeSafePermissionDeniedError) as exc:
                raise FatalJevError(f"Jev rejected the API key: {exc}") from exc
            except TypeSafeAPIResponseValidationError as exc:
                return {**base, "http_status": exc.status, "request_id": exc.request_id,
                        "error": f"invalid_response: {exc}"[:500]}
            except TypeSafeAPIError as exc:
                return {**base, "http_status": exc.status, "request_id": exc.request_id,
                        "error": f"http {exc.status}: {exc}"[:500]}
            except TypeSafeAPIConnectionError as exc:
                return {**base, "error": f"connection: {type(exc).__name__}: {exc}"[:500]}
            except TypeSafeError as exc:
                return {**base, "error": f"client: {exc}"[:500]}
            latency = int((time.monotonic() - t0) * 1000)

        raw = resp.raw_http_response.json()
        usage = raw.get("usage") or {}
        try:
            request_id = resp.request_id
        except Exception:
            request_id = None
        out = {
            **base,
            "jev_model_returned": raw.get("model"),
            "request_id": request_id,
            "http_status": resp.raw_http_response.status_code,
            "latency_ms": latency,
            "input_tokens": usage.get("input_tokens"),
            "output_tokens": usage.get("output_tokens"),
            "answers": raw.get("answers") or {},
        }
        self._memo[cache_key] = out
        return out
