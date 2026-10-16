"""
The five-way stance every agent is placed on, and the agent's own rating mapped onto it.

Jev answers one shared Choice per report: STRONG SELL / SELL / HOLD / BUY /
STRONG BUY. Independently, code reads the agent's own headline enum ("Neutral",
"Short", "Pass", …) and maps it through the rubric's ``native_to_stance``.
The two are stored side by side, and their agreement is a signal in itself.
An agent whose stated rating disagrees with the stance its own analysis
supports has written an internally inconsistent report.

Some native ratings have no buy/sell meaning. A risk level or "Reject Short
Thesis" maps to ``None`` and is recorded without agreement.
"""

from __future__ import annotations

from equity_mcp.evaluation.schema import STANCE_VALUES, Conviction

CONVICTION_LABELS: tuple[str, ...] = ("Low", "Medium", "High")


def stance_expected(probabilities: dict[str, float] | None) -> float | None:
    """Probability-weighted stance on −2 (STRONG SELL) … +2 (STRONG BUY)."""
    if not probabilities:
        return None
    total = sum(p for s, p in probabilities.items() if s in STANCE_VALUES)
    if total <= 0:
        return None
    return round(sum(STANCE_VALUES[s] * p for s, p in probabilities.items() if s in STANCE_VALUES) / total, 4)


def conviction_label(score: float | None) -> str | None:
    """The 0-based conviction Score (0..2) as Low/Medium/High."""
    if score is None:
        return None
    idx = min(max(int(round(score)), 0), len(CONVICTION_LABELS) - 1)
    return CONVICTION_LABELS[idx]


def native_stance(conviction: Conviction, extracts: dict[str, dict]) -> tuple[str | None, str | None]:
    """``(native_rating, native_stance)`` from the code-side extract, either possibly None."""
    if conviction.native_rating is None:
        return None, None
    rating = extracts.get(conviction.native_rating, {}).get("value")
    if rating is None:
        return None, None
    return str(rating), conviction.native_to_stance.get(str(rating))
