"""
Offline stand-ins for the evaluation tests: a deterministic Jev and an in-memory store.

The fake Jev answers every question with a schema-valid answer derived from the
question itself. Tests therefore exercise the real planning, validation,
gating and aggregation code with no API key and no network.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

REPO = Path(__file__).resolve().parent.parent
OUTPUTS = REPO / "outputs"


def load_output(name: str) -> dict:
    return json.loads((OUTPUTS / name).read_text(encoding="utf-8"))


def fake_answer(wire: dict, *, noul: float = 0.8, level_from_top: int = 1, choice_index: int = 2) -> dict:
    if wire["type"] == "noul":
        return {"type": "noul", "noul": noul}
    if wire["type"] == "choice":
        keys = list(wire["criteria"])
        pick = keys[min(choice_index, len(keys) - 1)]
        probs = {k: 0.0 for k in keys}
        probs[pick] = 0.75
        probs[keys[0] if pick != keys[0] else keys[-1]] = 0.25
        return {"type": "choice", "choice": pick, "probabilities": probs, "confidence": 0.75}
    n = len(wire["criteria"])
    level = max(0, n - 1 - level_from_top)
    probs = {str(i): 0.0 for i in range(n)}
    probs[str(level)] = 1.0
    return {"type": "score", "score": float(level), "probabilities": probs, "confidence": 0.9,
            "legend": {str(i): c for i, c in enumerate(wire["criteria"])}}


class FakeRunner:
    """Quacks like JevRunner. ``fail_requests`` makes calls whose question ids intersect it fail."""

    def __init__(self, fail_requests: set[str] | None = None, **answer_kw) -> None:
        self.calls: list[tuple[dict, dict]] = []
        self.fail_requests = fail_requests or set()
        self.answer_kw = answer_kw

    async def __aenter__(self) -> FakeRunner:
        return self

    async def __aexit__(self, *exc) -> None:
        return None

    async def call(self, state: dict, questions: dict, truncated: bool = False) -> dict:
        self.calls.append((state, questions))
        base = {"cache_key": f"fake{len(self.calls)}", "state_sha256": "s", "questions_sha256": "q",
                "jev_model_requested": "jev-test", "jev_model_returned": "jev-test", "request_id": None,
                "http_status": 200, "latency_ms": 1, "input_tokens": 10, "output_tokens": 1,
                "state_chars": len(json.dumps(state)), "state_truncated": truncated, "cached": False,
                "store_id": None}
        if self.fail_requests & set(questions):
            return {**base, "http_status": 529, "answers": None, "error": "http 529: overloaded"}
        return {**base, "answers": {qid: fake_answer(w, **self.answer_kw) for qid, w in questions.items()},
                "error": None}


class CaptureStore:
    """Quacks like LocalStore/SupabaseStore, keeping saved records in memory."""

    kind = "capture"
    fallbacks = 0

    def __init__(self, already: set[tuple[str, str]] | None = None) -> None:
        self.records: list[dict] = []
        self.already = already or set()

    async def __aenter__(self) -> CaptureStore:
        return self

    async def __aexit__(self, *exc) -> None:
        return None

    async def already_evaluated(self, run_id: str, role: str, rubric_sha: str, model: str) -> bool:
        return (run_id, role) in self.already

    async def cached_call(self, cache_key: str) -> None:
        return None

    async def save(self, record: dict) -> str:
        self.records.append(record)
        return "capture"


def run_tests(namespace: dict) -> None:
    """The standalone runner shared by every test_eval_* module."""
    failures = 0
    for name, fn in sorted(namespace.items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"  PASS  {name}")
            except Exception as exc:  # noqa: BLE001 - report and continue
                failures += 1
                print(f"  FAIL  {name}: {type(exc).__name__}: {exc}")
    print("\nall passed" if not failures else f"\n{failures} failure(s)")
    sys.exit(1 if failures else 0)
