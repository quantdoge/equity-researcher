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
    ar1        = f(bal1["total_assets"]) * 0.08   # proxy: A/R ~ 8% of assets
    assets1    = f(bal1["total_assets"]) or 1
    liab1      = f(bal1["total_liabilities"])
    ni1        = f(inc1["net_income"])
    op_cf1     = f(cf1.get("operating_cash_flow") or 0)
    capex1     = abs(f(cf1.get("capital_expenditure") or 0))
    ppe1       = assets1 * 0.30   # proxy: PPE ~ 30% of assets
    sga1       = rev1 - gp1 - f(inc1["operating_income"])  # rough SG&A proxy

    # Prior year
    rev2       = f(inc2["revenue"]) or 1
    gp2        = f(inc2["gross_profit"])
    ar2        = f(bal2["total_assets"]) * 0.08
    assets2    = f(bal2["total_assets"]) or 1
    ppe2       = assets2 * 0.30
    sga2       = rev2 - gp2 - f(inc2["operating_income"])

    # M-score indices
    dsri  = (ar1 / rev1)  / (ar2 / rev2)                                # Days Sales in Receivables
    gmi   = (gp2 / rev2)  / (gp1 / rev1) if gp1 > 0 else 1             # Gross Margin
    aqi   = (1 - (ppe1 + ar1) / assets1) / (1 - (ppe2 + ar2) / assets2) # Asset Quality
    sgi   = rev1 / rev2                                                   # Sales Growth
    depi  = (ppe2 / (ppe2 + (assets2 - ppe2))) / (ppe1 / (ppe1 + (assets1 - ppe1))) if ppe1 > 0 else 1  # Depreciation
    sgai  = (sga1 / rev1) / (sga2 / rev2) if sga2 != 0 and rev2 != 0 else 1  # SG&A
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
        "note": "A/R and PPE estimated via proxies; obtain actual line items for precision",
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
    Uses accounts receivable proxy (8% of total assets) since A/R is not
    stored as a separate column in the current schema.
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
        ar_curr = float(bal_curr.get("total_assets") or 0) * 0.08
        ar_prev = float(bal_prev.get("total_assets") or 0) * 0.08

        rev_growth = (rev_curr - rev_prev) / rev_prev * 100 if rev_prev else None
        ar_growth = (ar_curr - ar_prev) / ar_prev * 100 if ar_prev else None
        flag = ar_growth is not None and rev_growth is not None and ar_growth > rev_growth + 5

        rows.append({
            "period_end": pe_curr,
            "revenue_growth_pct": round(rev_growth, 2) if rev_growth else None,
            "ar_growth_pct_proxy": round(ar_growth, 2) if ar_growth else None,
            "red_flag": flag,
        })

    return {
        "symbol": symbol,
        "annual_series": rows,
        "note": "A/R approximated as 8% of total assets — replace with actual A/R if available",
    }


def calculate_inventory_days_trend(symbol: str) -> dict:
    """
    Inventory days = inventory / (COGS / 365).
    Rising inventory days may signal weakening demand.
    Inventory is proxied as (revenue - gross_profit) * 0.15 since it is not
    stored as a separate line item.
    """
    income = get_income_statement(symbol, "annual", 4)

    rows = []
    for inc in income:
        rev = float(inc["revenue"] or 0)
        gp = float(inc["gross_profit"] or 0)
        cogs = rev - gp
        inventory_proxy = cogs * 0.15
        inventory_days = round(inventory_proxy / (cogs / 365), 1) if cogs > 0 else None
        rows.append({
            "period_end": inc["period_end"],
            "revenue": rev,
            "cogs_proxy": round(cogs, 0),
            "inventory_days_proxy": inventory_days,
        })

    # Signal: is the most recent year higher than 2 years ago?
    signal = "rising" if (
        len(rows) >= 3
        and rows[0]["inventory_days_proxy"]
        and rows[2]["inventory_days_proxy"]
        and rows[0]["inventory_days_proxy"] > rows[2]["inventory_days_proxy"] * 1.1
    ) else "stable_or_falling"

    return {
        "symbol": symbol,
        "trend_signal": signal,
        "annual_series": rows,
        "note": "Inventory estimated as 15% of COGS — replace with actual inventory if available",
    }
