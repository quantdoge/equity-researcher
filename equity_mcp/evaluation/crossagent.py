"""
Pass-2 context: what the specialists actually said, built in code.

The portfolio strategist and head of research are judged partly on fidelity.
Does the strategist's conviction table match the specialists? Does the memo's
verdict follow from them? Are failed agents acknowledged rather than invented?
Jev can only judge that if it sees the specialists' positions, so this module
summarises them. It uses code extracts and the pass-1 Jev stances, never the
raw reports, which would bury the memo in context.

The same facts feed the deterministic pass-2 checks (``failures_acknowledged``,
``fraud_override``) through ``ctx``.
"""

from __future__ import annotations

from equity_mcp.evaluation.extract import PASS2_ROLES, role_label
from equity_mcp.roles import ALL_ROLES

SPECIALIST_ROLES: tuple[str, ...] = tuple(r for r in ALL_ROLES if r not in PASS2_ROLES)


def build(run: dict, records: dict[str, dict], pass1: dict[str, dict], for_role: str) -> tuple[dict, dict]:
    """
    ``(specialist_summary, ctx)``.

    ``pass1[role]`` holds ``{"extracts", "native_rating", "stance", "conviction_level"}``
    for every specialist whose record was parsed. ``stance`` and ``conviction_level``
    are None when Jev was not run for that role in this invocation.
    """
    views, failed = [], []
    for role in SPECIALIST_ROLES:
        rec = records.get(role)
        status = rec["status"] if rec else "missing"
        if status != "ok":
            failed.append(role)
        p = pass1.get(role, {})
        views.append({
            "agent": role_label(role),
            "status": "completed" if status == "ok" else f"no usable report ({status})",
            "native_rating": p.get("native_rating"),
            "stance": p.get("stance"),
            "conviction": p.get("conviction_level"),
        })
    short = pass1.get("short_analyst", {}).get("extracts", {})
    summary: dict = {
        "completed_specialists": len(SPECIALIST_ROLES) - len(failed),
        "failed_or_missing_specialists": [role_label(r) for r in failed],
        "specialist_views": views,
        "short_seller_flags": {
            "earnings_quality": short.get("earnings_quality", {}).get("value"),
            "contrarian_rating": short.get("contrarian_rating", {}).get("value"),
        },
    }
    if for_role == "head_of_research":
        ps = pass1.get("portfolio_strategist", {}).get("extracts", {})
        summary["portfolio_action"] = ps.get("portfolio_action", {}).get("value")
    ctx = {
        "failed_roles": sorted(set(failed) | (set(run.get("failures") or []) & set(SPECIALIST_ROLES))),
        "short_earnings_quality": summary["short_seller_flags"]["earnings_quality"],
    }
    return summary, ctx
