"""
Turn validated Jev answers and check results into metric rows and one evaluation.

Three results come out of one evaluation, and they are kept apart on purpose:

1. **Conviction**: the stance, its expected value, the conviction level, and
   the agent's own rating mapped onto the stance scale.
2. **Domain profile**: one 1–5 level per domain metric, or ``not_addressed``.
   It describes the company as the agent saw it, so it is never mixed into a
   quality score.
3. **Alignment composite**: the weighted mean of prompt-adherence metrics.
   - A failed veto metric is listed in ``vetoes``. It is never averaged away.
   - Answers behind a failed gate are ``low_evidence`` and excluded.
   - The composite is NULL when less than 70% of the weight returned usable
     answers, because a mean over a third of the rubric is not the rubric.

Score answers are 0-based expected values (Jev returns the probability-weighted
level). Normalising to 0..1 is ``score / (n - 1)``. A score passes when it
rounds to at least the question's ``pass_level``.
"""

from __future__ import annotations

from equity_mcp.evaluation.schema import ChoiceQ, NoulQ, ScoreQ
from equity_mcp.evaluation.stance import conviction_label, stance_expected

COVERAGE_FLOOR = 0.7


def _num(x: object) -> float | None:
    return float(x) if isinstance(x, (int, float)) and not isinstance(x, bool) else None


def metric_row(
    *,
    question_id: str,
    block: str,
    kind: str,
    rubric_request: str | None = None,
    dimension: str | None = None,
    label: str | None = None,
    weight: float = 0.0,
    veto: bool = False,
    variant: str = "primary",
    status: str = "ok",
    **fields: object,
) -> dict:
    row = {
        "question_id": question_id, "block": block, "variant": variant, "kind": kind,
        "rubric_request": rubric_request, "dimension": dimension, "label": label,
        "weight": weight, "veto": veto,
        "noul_p": None, "choice": None, "score": None, "n_levels": None, "probabilities": None,
        "confidence": None, "deterministic_value": None, "detail": None, "code_extract": None,
        "agreement": None, "normalized": None, "passed": None, "status": status, "error": None,
        "call_ref": None,
    }
    row.update(fields)
    return row


def answer_row(
    qid: str,
    q: NoulQ | ScoreQ | ChoiceQ,
    answer: dict,
    *,
    block: str,
    rubric_request: str,
    variant: str,
    extracts: dict[str, dict],
) -> dict:
    """A metric row from one validated Jev answer."""
    row = metric_row(
        question_id=qid, block=block, kind=q.type, rubric_request=rubric_request,
        dimension=q.dimension, weight=q.weight, veto=q.veto, variant=variant,
    )
    if isinstance(q, NoulQ):
        p = float(answer["noul"])
        good = p if q.good_when else 1.0 - p
        row.update(noul_p=p, normalized=round(good, 4), passed=good >= q.threshold)
    elif isinstance(q, ScoreQ):
        n = len(q.criteria)
        s = float(answer["score"])
        row.update(
            score=s, n_levels=n, probabilities=answer.get("probabilities"), confidence=answer.get("confidence"),
            normalized=round(s / (n - 1), 4), passed=round(s) >= q.pass_level,
        )
    else:
        probs = answer.get("probabilities") or {}
        row.update(choice=answer["choice"], probabilities=probs, confidence=answer.get("confidence"))
        if q.value_map:
            v = sum(q.value_map.get(o, 0.0) * p for o, p in probs.items())
            row.update(normalized=round(v, 4), passed=v >= 0.5)
        if q.cross_check:
            code = extracts.get(q.cross_check, {}).get("value")
            row["code_extract"] = None if code is None else str(code)
            row["agreement"] = (answer["choice"] == str(code)) if code is not None else answer["choice"] == "not_stated"
    return row


def domain_row(mid: str, label: str, answer: dict | None, *, status: str, detail: str | None = None) -> dict:
    row = metric_row(question_id=mid, block="domain", kind="score", dimension="domain", label=label,
                     status=status, detail=detail)
    if answer is not None and status == "ok":
        s = float(answer["score"])
        row.update(score=s, n_levels=5, probabilities=answer.get("probabilities"),
                   confidence=answer.get("confidence"), normalized=round(s / 4, 4))
    return row


def check_row(chk, result: dict) -> dict:
    passed = result["passed"]
    return metric_row(
        question_id=chk.id, block="alignment", kind="deterministic", dimension=chk.dimension,
        weight=chk.weight, veto=chk.veto, status="skipped" if passed is None else "ok",
        deterministic_value=_num(result.get("value")), normalized=_num(result.get("value")),
        passed=passed, detail=(result.get("detail") or "")[:500],
    )


def apply_gate(rows: list[dict], gate_id: str | None) -> bool:
    """Mark a failed gate's siblings ``low_evidence``. True if the gate failed."""
    if gate_id is None:
        return False
    gate = next((r for r in rows if r["question_id"] == gate_id and r["status"] == "ok"), None)
    if gate is None or gate["passed"]:
        return False
    for r in rows:
        if r["question_id"] != gate_id and r["status"] == "ok":
            r["status"] = "low_evidence"
    return True


def summarise(rows: list[dict], *, native: tuple[str | None, str | None], gates_failed: int,
              native_conviction: str | None = None) -> dict:
    """The evaluation-level fields computed from all metric rows."""
    primary = [r for r in rows if r["variant"] == "primary"]
    by_id = {r["question_id"]: r for r in primary}

    # ── conviction ──
    stance_r, gate_r, conv_r = by_id.get("stance"), by_id.get("stance_gate"), by_id.get("conviction_level")
    stance_ok = stance_r is not None and stance_r["status"] in ("ok", "low_evidence")
    stance = stance_r["choice"] if stance_ok else None
    probs = stance_r["probabilities"] if stance_ok else None
    native_rating, native_st = native
    conv_score = conv_r["score"] if conv_r and conv_r["status"] in ("ok", "low_evidence") else None
    out: dict = {
        "stance": stance,
        "stance_probabilities": probs,
        "stance_expected": stance_expected(probs),
        "stance_confidence": stance_r["confidence"] if stance_ok else None,
        "stance_low_evidence": (gate_r is not None and gate_r["status"] == "ok" and not gate_r["passed"])
                               or (stance_r is not None and stance_r["status"] == "low_evidence"),
        "conviction_level": conviction_label(conv_score),
        "conviction_score": conv_score,
        "native_rating": native_rating,
        "native_stance": native_st,
        "stance_agreement": (native_st == stance) if (native_st and stance) else None,
    }
    if conv_r is not None and native_conviction is not None:
        conv_r["code_extract"] = native_conviction
        conv_r["agreement"] = native_conviction.lower() == (out["conviction_level"] or "").lower()

    # ── domain profile ──
    domain = [r for r in primary if r["block"] == "domain"]
    profile = {
        r["question_id"]: {
            "label": r["label"],
            "level": round(r["score"] + 1, 2) if r["score"] is not None else None,
            "confidence": r["confidence"],
            "status": r["status"],
        }
        for r in domain
    }
    levels = [p["level"] for p in profile.values() if p["level"] is not None]
    out.update(
        domain_profile=profile,
        domain_mean=round(sum(levels) / len(levels), 3) if levels else None,
        domain_addressed=len(levels),
        domain_total=len(domain),
    )

    # ── alignment composite ──
    align = [r for r in primary if r["block"] == "alignment" and r["weight"] > 0 and r["status"] != "skipped"]
    usable = [r for r in align if r["status"] == "ok" and r["normalized"] is not None]
    w_all = sum(r["weight"] for r in align)
    w_ok = sum(r["weight"] for r in usable)
    coverage = (w_ok / w_all) if w_all else None
    composite = (sum(r["weight"] * r["normalized"] for r in usable) / w_ok) if w_ok else None
    if coverage is not None and coverage < COVERAGE_FLOOR:
        composite = None
    dims: dict[str, dict] = {}
    for r in usable:
        d = dims.setdefault(r["dimension"] or "general", {"w": 0.0, "s": 0.0, "n": 0})
        d["w"] += r["weight"]
        d["s"] += r["weight"] * r["normalized"]
        d["n"] += 1
    vetoes = sorted({r["question_id"] for r in primary
                     if r["block"] == "alignment" and r["veto"] and r["status"] == "ok" and r["passed"] is False})
    errors = sum(1 for r in rows if r["status"] == "error")
    out.update(
        alignment_composite=round(composite, 4) if composite is not None else None,
        alignment_coverage=round(coverage, 4) if coverage is not None else None,
        alignment_dimensions={k: {"score": round(v["s"] / v["w"], 4), "n": v["n"]} for k, v in dims.items() if v["w"]},
        vetoes=vetoes,
        veto_triggered=bool(vetoes),
        insufficient_evidence=gates_failed > 0,
        n_metrics=len(rows),
        n_errors=errors,
        status="partial" if errors or (w_all and composite is None) else "complete",
    )
    return out
