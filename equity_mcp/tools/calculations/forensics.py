"""
Forensic accounting tools for the Short / Contrarian Analyst.
Detects earnings quality issues, manipulation signals, and red flags.
"""

from __future__ import annotations

from equity_mcp.tools.db import (
    get_balance_sheet,
    get_cash_flow,
    get_income_statement,
)


def calculate_beneish_m_score(symbol: str) -> dict:
    """
    Beneish M-Score earnings manipulation model.
    Score > -1.78 suggests possible manipulation.
    Score > -2.22 is a softer warning threshold.

    Uses 8 financial ratios derived from two consecutive annual periods.
    """
    income = get_income_statement(symbol, "annual", 2)
    balance = get_balance_sheet(symbol, "annual", 2)
    cf = get_cash_flow(symbol, "annual", 2)

    if len(income) < 2 or len(balance) < 2:
        return {"symbol": symbol, "error": "Need 2 years of data for Beneish M-Score"}

    inc1, inc2 = income[0], income[1]   # current, prior year
    bal1, bal2 = balance[0], balance[1]
    cf1 = cf[0] if cf else {}

    def f(x): return float(x or 0)

    # Current year
    rev1       = f(inc1["revenue"]) or 1
    gp1        = f(inc1["gross_profit"])
    ar1        = f(bal1["net_receivables"])
    assets1    = f(bal1["total_assets"]) or 1
    liab1      = f(bal1["total_liabilities"])
    ni1        = f(inc1["net_income"])
    op_cf1     = f(cf1.get("operating_cash_flow") or 0)
    ppe1       = f(bal1["ppe_net"])
    dep1       = f(inc1["depreciation_and_amortization"])
    sga1       = f(inc1["sga"])

    # Prior year
    rev2       = f(inc2["revenue"]) or 1
    gp2        = f(inc2["gross_profit"])
    ar2        = f(bal2["net_receivables"])
    assets2    = f(bal2["total_assets"]) or 1
    ppe2       = f(bal2["ppe_net"])
    dep2       = f(inc2["depreciation_and_amortization"])
    sga2       = f(inc2["sga"])

    def _dep_rate(dep: float, ppe: float) -> float:
        """Depreciation rate = D&A / (D&A + net PPE)."""
        base = dep + ppe
        return dep / base if base else 0.0

    dep_rate1 = _dep_rate(dep1, ppe1)
    dep_rate2 = _dep_rate(dep2, ppe2)

    # M-score indices.  AQI is the share of assets that is neither current nor
    # PPE — i.e. soft/capitalised assets — so it needs real current assets and
    # real PPE to mean anything.
    soft1 = 1 - (f(bal1["total_current_assets"]) + ppe1) / assets1
    soft2 = 1 - (f(bal2["total_current_assets"]) + ppe2) / assets2

    dsri  = (ar1 / rev1)  / (ar2 / rev2) if ar2 and rev2 else 1         # Days Sales in Receivables
    gmi   = (gp2 / rev2)  / (gp1 / rev1) if gp1 > 0 else 1             # Gross Margin
    aqi   = soft1 / soft2 if soft2 else 1                               # Asset Quality
    sgi   = rev1 / rev2                                                   # Sales Growth
    depi  = dep_rate2 / dep_rate1 if dep_rate1 else 1                    # Depreciation
    sgai  = (sga1 / rev1) / (sga2 / rev2) if sga2 and rev2 else 1        # SG&A
    lvgi  = (liab1 / assets1) / (f(bal2["total_liabilities"]) / assets2) if assets2 > 0 else 1  # Leverage
    tata  = (ni1 - op_cf1) / assets1                                     # Total Accruals

    m_score = (
        -4.84
        + 0.920 * dsri
        + 0.528 * gmi
        + 0.404 * aqi
        + 0.892 * sgi
        + 0.115 * depi
        - 0.172 * sgai
        + 4.679 * tata
        - 0.327 * lvgi
    )

    if m_score > -1.78:
        signal = "HIGH RISK — likely manipulator"
    elif m_score > -2.22:
        signal = "MODERATE RISK — possible manipulator"
    else:
        signal = "Low risk"

    return {
        "symbol": symbol,
        "period_end": inc1["period_end"],
        "m_score": round(m_score, 3),
        "signal": signal,
        "threshold_high": -1.78,
        "threshold_moderate": -2.22,
        "indices": {
            "dsri": round(dsri, 3), "gmi": round(gmi, 3), "aqi": round(aqi, 3),
            "sgi": round(sgi, 3), "depi": round(depi, 3), "sgai": round(sgai, 3),
            "lvgi": round(lvgi, 3), "tata": round(tata, 4),
        },
        "note": "Computed from reported receivables, PPE, D&A and SG&A line items",
    }


def calculate_accruals_ratio(symbol: str) -> dict:
    """
    Balance-sheet accruals ratio = (net income – operating CF) / avg total assets.
    High positive accruals (> 0.05) signal lower earnings quality.
    """
    income = get_income_statement(symbol, "annual", 4)
    balance = get_balance_sheet(symbol, "annual", 4)
    cf = get_cash_flow(symbol, "annual", 4)

    rows = []
    bal_map = {r["period_end"]: r for r in balance}
    cf_map = {r["period_end"]: r for r in cf}

    for inc in income:
        pe = inc["period_end"]
        bal = bal_map.get(pe, {})
        c = cf_map.get(pe, {})
        ni = float(inc["net_income"] or 0)
        op_cf = float(c.get("operating_cash_flow") or 0)
        assets = float(bal.get("total_assets") or 1)
        accruals = (ni - op_cf) / assets
        rows.append({
            "period_end": pe,
            "net_income": round(ni, 0),
            "operating_cash_flow": round(op_cf, 0),
            "accruals_ratio": round(accruals, 4),
            "signal": "warning" if accruals > 0.05 else "ok",
        })

    return {"symbol": symbol, "annual_series": rows}


def calculate_earnings_quality_score(symbol: str) -> dict:
    """
    Composite earnings quality: combines accruals ratio, cash conversion
    (operating CF / net income), and FCF conversion (FCF / net income).
    Returns a 0–100 score where higher = better quality.
    """
    income = get_income_statement(symbol, "annual", 1)
    cf = get_cash_flow(symbol, "annual", 1)

    if not income or not cf:
        return {"symbol": symbol, "error": "Insufficient data"}

    ni = float(income[0]["net_income"] or 0)
    op_cf = float(cf[0]["operating_cash_flow"] or 0)
    fcf = float(cf[0]["free_cash_flow"] or 0)
    assets = 1  # normalised

    cash_conversion = op_cf / ni if ni != 0 else None
    fcf_conversion = fcf / ni if ni != 0 else None
    accruals = (ni - op_cf) / float(income[0].get("revenue") or 1)

    # Score: penalise low cash conversion and high accruals
    score = 50
    if cash_conversion is not None:
        score += min(max((cash_conversion - 1) * 20, -30), 30)
    if accruals < -0.05:
        score -= 20
    elif accruals > 0.05:
        score -= 10

    return {
        "symbol": symbol,
        "period_end": income[0]["period_end"],
        "cash_conversion_ratio": round(cash_conversion, 3) if cash_conversion else None,
        "fcf_conversion_ratio": round(fcf_conversion, 3) if fcf_conversion else None,
        "accruals_to_revenue": round(accruals, 4),
        "quality_score_0_100": min(max(round(score), 0), 100),
    }


def detect_revenue_deceleration(symbol: str, n_quarters: int = 8) -> dict:
    """
    Detect whether the YoY revenue growth rate is accelerating or decelerating
    over the last n quarters. A decelerating trend is a bearish signal.
    """
    income = get_income_statement(symbol, "quarter", n_quarters + 4)
    if len(income) < 5:
        return {"symbol": symbol, "error": "Insufficient quarterly data"}

    inc_map = {r["period_end"]: float(r["revenue"] or 0) for r in income}
    periods = sorted(inc_map.keys(), reverse=True)

    yoy_rates = []
    for i, pe in enumerate(periods):
        # Find same quarter prior year
        pe_date = pe  # already ISO string YYYY-MM-DD
        # Prior year same period — use period 4 positions back (quarterly)
        if i + 4 < len(periods):
            prior_pe = periods[i + 4]
            curr_rev = inc_map[pe]
            prior_rev = inc_map[prior_pe]
            if prior_rev:
                yoy = (curr_rev - prior_rev) / prior_rev * 100
                yoy_rates.append({"period_end": pe, "revenue": curr_rev, "yoy_growth_pct": round(yoy, 2)})

    # Check trend direction (simple linear slope of YoY rates)
    if len(yoy_rates) >= 3:
        rates = [r["yoy_growth_pct"] for r in yoy_rates[:6]]
        n = len(rates)
        slope = (rates[0] - rates[-1]) / (n - 1)  # newest first
        trend = "decelerating" if slope < -1 else ("accelerating" if slope > 1 else "stable")
    else:
        trend = "insufficient data"

    return {
        "symbol": symbol,
        "trend": trend,
        "quarterly_yoy_series": yoy_rates[:8],
    }


def calculate_receivables_growth_vs_revenue(symbol: str) -> dict:
    """
    Red flag: receivables growing faster than revenue suggests channel stuffing
    or aggressive revenue recognition.
    """
    income = get_income_statement(symbol, "annual", 4)
    balance = get_balance_sheet(symbol, "annual", 4)

    rows = []
    bal_map = {r["period_end"]: r for r in balance}

    for i, inc in enumerate(income[:-1]):
        pe_curr = inc["period_end"]
        pe_prev = income[i + 1]["period_end"]
        bal_curr = bal_map.get(pe_curr, {})
        bal_prev = bal_map.get(pe_prev, {})

        rev_curr = float(inc["revenue"] or 0)
        rev_prev = float(income[i + 1]["revenue"] or 0)
        ar_curr = float(bal_curr.get("net_receivables") or 0)
        ar_prev = float(bal_prev.get("net_receivables") or 0)

        rev_growth = (rev_curr - rev_prev) / rev_prev * 100 if rev_prev else None
        ar_growth = (ar_curr - ar_prev) / ar_prev * 100 if ar_prev else None
        flag = ar_growth is not None and rev_growth is not None and ar_growth > rev_growth + 5

        rows.append({
            "period_end": pe_curr,
            "revenue_growth_pct": round(rev_growth, 2) if rev_growth else None,
            "ar_growth_pct": round(ar_growth, 2) if ar_growth else None,
            "red_flag": flag,
        })

    return {
        "symbol": symbol,
        "annual_series": rows,
        "note": "Computed from reported net receivables",
    }


def calculate_inventory_days_trend(symbol: str) -> dict:
    """
    Inventory days = inventory / (COGS / 365).
    Rising inventory days may signal weakening demand.

    Returns nulls for a company that carries no inventory (most software and
    services businesses) rather than implying a number for it.
    """
    income = get_income_statement(symbol, "annual", 4)
    balance = get_balance_sheet(symbol, "annual", 4)
    bal_map = {r["period_end"]: r for r in balance}

    rows = []
    for inc in income:
        rev = float(inc["revenue"] or 0)
        cogs = float(inc["cost_of_revenue"] or 0) or (rev - float(inc["gross_profit"] or 0))
        bal = bal_map.get(inc["period_end"], {})
        inventory = float(bal.get("inventory") or 0)
        inventory_days = (
            round(inventory / (cogs / 365), 1) if cogs > 0 and inventory else None
        )
        rows.append({
            "period_end": inc["period_end"],
            "revenue": rev,
            "cogs": round(cogs, 0),
            "inventory": round(inventory, 0),
            "inventory_days": inventory_days,
        })

    # Signal: is the most recent year higher than 2 years ago?
    signal = "rising" if (
        len(rows) >= 3
        and rows[0]["inventory_days"]
        and rows[2]["inventory_days"]
        and rows[0]["inventory_days"] > rows[2]["inventory_days"] * 1.1
    ) else "stable_or_falling"

    return {
        "symbol": symbol,
        "trend_signal": signal,
        "annual_series": rows,
        "note": "Computed from reported inventory and cost of revenue; null where the company carries no inventory",
    }
