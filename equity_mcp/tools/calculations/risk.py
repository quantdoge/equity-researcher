"""
Financial risk metric calculations for the Financial Risk Analyst.
Covers Altman Z-score, Piotroski F-score, leverage/liquidity ratios, VaR.
"""

from __future__ import annotations

import math
import statistics
from datetime import date, timedelta

from equity_mcp.tools.db import (
    get_balance_sheet,
    get_cash_flow,
    get_income_statement,
    get_price_history,
)


def calculate_leverage_ratios(symbol: str) -> dict:
    """
    Compute debt/equity, net debt/EBITDA, interest coverage, and debt/assets
    for the most recent annual period.
    """
    income = get_income_statement(symbol, "annual", 1)
    balance = get_balance_sheet(symbol, "annual", 1)

    if not income or not balance:
        return {"symbol": symbol, "error": "Insufficient data"}

    inc = income[0]
    bal = balance[0]

    debt = float(bal["total_debt"] or 0)
    equity = float(bal["total_equity"] or 0)
    assets = float(bal["total_assets"] or 0)
    cash = float(bal["cash_and_short_term_investments"] or 0)
    op_income = float(inc["operating_income"] or 0)
    revenue = float(inc["revenue"] or 0)
    ebitda = float(inc["ebitda"] or 0)

    return {
        "symbol": symbol,
        "period_end": bal["period_end"],
        "debt_to_equity": round(debt / equity, 2) if equity else None,
        "debt_to_assets": round(debt / assets, 2) if assets else None,
        "net_debt": round(debt - cash, 0),
        "net_debt_to_ebitda": round((debt - cash) / ebitda, 2) if ebitda else None,
        "interest_coverage": (
            round(op_income / abs(float(inc["interest_expense"])), 2)
            if inc["interest_expense"]
            else None
        ),
        "operating_margin_pct": round(op_income / revenue * 100, 2) if revenue else None,
    }


def calculate_liquidity_ratios(symbol: str) -> dict:
    """
    Compute current ratio, quick ratio, cash ratio and working capital, plus
    whole-balance-sheet solvency ratios.
    """
    balance = get_balance_sheet(symbol, "annual", 1)
    if not balance:
        return {"symbol": symbol, "error": "No balance sheet data"}

    bal = balance[0]
    assets = float(bal["total_assets"] or 0)
    liabilities = float(bal["total_liabilities"] or 0)
    cash = float(bal["cash_and_short_term_investments"] or 0)
    equity = float(bal["total_equity"] or 0)
    current_assets = float(bal["total_current_assets"] or 0)
    current_liabilities = float(bal["total_current_liabilities"] or 0)
    inventory = float(bal["inventory"] or 0)

    return {
        "symbol": symbol,
        "period_end": bal["period_end"],
        "current_ratio": (
            round(current_assets / current_liabilities, 2)
            if current_liabilities
            else None
        ),
        "quick_ratio": (
            round((current_assets - inventory) / current_liabilities, 2)
            if current_liabilities
            else None
        ),
        "cash_ratio": (
            round(cash / current_liabilities, 2) if current_liabilities else None
        ),
        "working_capital": round(current_assets - current_liabilities, 0),
        "assets_to_liabilities": round(assets / liabilities, 2) if liabilities else None,
        "cash_to_liabilities": round(cash / liabilities, 2) if liabilities else None,
        "equity_to_assets": round(equity / assets, 2) if assets else None,
        "cash": cash,
    }


def calculate_altman_z_score(symbol: str) -> dict:
    """
    Altman Z-Score (public company version).
    Z > 2.99: safe zone.  1.81–2.99: grey zone.  < 1.81: distress zone.

    x4 uses book equity rather than market capitalisation, so the score is
    indicative rather than a literal Altman reading.
    """
    income = get_income_statement(symbol, "annual", 1)
    balance = get_balance_sheet(symbol, "annual", 1)

    if not income or not balance:
        return {"symbol": symbol, "error": "Insufficient data for Z-score"}

    inc = income[0]
    bal = balance[0]

    assets = float(bal["total_assets"] or 1)
    liabilities = float(bal["total_liabilities"] or 0)
    equity = float(bal["total_equity"] or 0)
    revenue = float(inc["revenue"] or 0)
    # EBIT proper, not operating income standing in for it.
    ebit = float(inc["ebit"] or inc["operating_income"] or 0)
    retained_earnings = float(bal["retained_earnings"] or 0)

    working_capital = float(bal["total_current_assets"] or 0) - float(
        bal["total_current_liabilities"] or 0
    )

    x1 = working_capital / assets                     # Working capital / Total assets
    x2 = retained_earnings / assets                   # Retained earnings / Total assets
    x3 = ebit / assets                                # EBIT / Total assets
    x4 = equity / liabilities if liabilities else 0   # Market value equity / Total liabilities
    x5 = revenue / assets                             # Sales / Total assets

    z = 1.2 * x1 + 1.4 * x2 + 3.3 * x3 + 0.6 * x4 + 1.0 * x5

    if z > 2.99:
        zone = "Safe"
    elif z > 1.81:
        zone = "Grey"
    else:
        zone = "Distress"

    return {
        "symbol": symbol,
        "period_end": bal["period_end"],
        "z_score": round(z, 3),
        "zone": zone,
        "components": {"x1": round(x1, 4), "x2": round(x2, 4), "x3": round(x3, 4), "x4": round(x4, 4), "x5": round(x5, 4)},
        "note": "x4 uses book equity (not market cap) — treat as indicative only",
    }


def calculate_piotroski_f_score(symbol: str) -> dict:
    """
    Piotroski F-Score (0–9).  8–9: strong.  0–2: weak.
    Evaluates profitability (4 pts), leverage/liquidity (3 pts), operating efficiency (2 pts).
    """
    income = get_income_statement(symbol, "annual", 2)
    balance = get_balance_sheet(symbol, "annual", 2)
    cf = get_cash_flow(symbol, "annual", 2)

    if len(income) < 2 or len(balance) < 2:
        return {"symbol": symbol, "error": "Need 2 years of data for F-score"}

    inc0, inc1 = income[0], income[1]
    bal0, bal1 = balance[0], balance[1]
    cf0 = cf[0] if cf else {}

    assets0 = float(bal0["total_assets"] or 1)
    assets1 = float(bal1["total_assets"] or 1)
    net_income = float(inc0["net_income"] or 0)
    op_cf = float(cf0.get("operating_cash_flow") or 0)
    liabilities0 = float(bal0["total_liabilities"] or 0)
    liabilities1 = float(bal1["total_liabilities"] or 0)
    revenue0 = float(inc0["revenue"] or 1)
    revenue1 = float(inc1["revenue"] or 1)
    gross0 = float(inc0["gross_profit"] or 0)
    gross1 = float(inc1["gross_profit"] or 0)
    shares0 = float(inc0["weighted_average_shares_diluted"] or 0)
    shares1 = float(inc1["weighted_average_shares_diluted"] or 0)

    roa0 = net_income / assets0
    roa1 = float(inc1["net_income"] or 0) / assets1
    leverage0 = liabilities0 / assets0
    leverage1 = liabilities1 / assets1
    gross_margin0 = gross0 / revenue0
    gross_margin1 = gross1 / revenue1
    asset_turnover0 = float(inc0["revenue"] or 0) / assets0
    asset_turnover1 = float(inc1["revenue"] or 0) / assets1

    scores = {
        "F1_positive_roa": int(roa0 > 0),
        "F2_positive_op_cf": int(op_cf > 0),
        "F3_roa_improvement": int(roa0 > roa1),
        "F4_accruals_quality": int(op_cf / assets0 > roa0),
        "F5_lower_leverage": int(leverage0 < leverage1),
        "F6_positive_equity_change": int(float(bal0["total_equity"] or 0) > float(bal1["total_equity"] or 0)),
        # Diluted share count fell or held flat — buybacks score, issuance does not.
        # Scores 1 when the count is unavailable rather than penalising a gap.
        "F7_no_dilution": int(shares0 <= shares1 if shares0 and shares1 else 1),
        "F8_gross_margin_improvement": int(gross_margin0 > gross_margin1),
        "F9_asset_turnover_improvement": int(asset_turnover0 > asset_turnover1),
    }

    total = sum(scores.values())
    strength = "Strong" if total >= 8 else ("Moderate" if total >= 5 else "Weak")

    return {
        "symbol": symbol,
        "period_end": bal0["period_end"],
        "f_score": total,
        "strength": strength,
        "component_scores": scores,
    }


def calculate_price_volatility(
    symbol: str, window_days: int = 252, benchmark_symbol: str = "SPY"
) -> dict:
    """
    Compute annualised historical volatility, beta vs benchmark, max drawdown,
    and Sharpe ratio (assumes 0% risk-free rate for simplicity).
    """
    to_d = date.today().isoformat()
    from_d = (date.today() - timedelta(days=window_days + 30)).isoformat()

    prices = get_price_history(symbol, from_d, to_d)
    bench = get_price_history(benchmark_symbol, from_d, to_d)

    if len(prices) < 30:
        return {"symbol": symbol, "error": "Insufficient price history"}

    def daily_returns(rows):
        closes = [float(r["adj_close"]) for r in rows if r["adj_close"]]
        return [(closes[i] / closes[i - 1]) - 1 for i in range(1, len(closes))]

    rets = daily_returns(prices)
    ann_vol = statistics.stdev(rets) * math.sqrt(252) if len(rets) > 1 else None
    avg_ret = sum(rets) / len(rets)
    sharpe = round(avg_ret / statistics.stdev(rets) * math.sqrt(252), 3) if len(rets) > 1 else None

    # Max drawdown
    closes = [float(r["adj_close"]) for r in prices if r["adj_close"]]
    peak = closes[0]
    max_dd = 0.0
    for c in closes:
        if c > peak:
            peak = c
        dd = (peak - c) / peak
        if dd > max_dd:
            max_dd = dd

    # Beta vs benchmark
    beta = None
    if bench and len(bench) > 30:
        bench_rets = daily_returns(bench)
        min_len = min(len(rets), len(bench_rets))
        r = rets[-min_len:]
        b = bench_rets[-min_len:]
        cov = sum((r[i] - avg_ret) * (b[i] - sum(b) / len(b)) for i in range(min_len)) / min_len
        bench_var = statistics.variance(b)
        beta = round(cov / bench_var, 3) if bench_var else None

    return {
        "symbol": symbol,
        "window_days": window_days,
        "annualised_volatility_pct": round(ann_vol * 100, 2) if ann_vol else None,
        "beta_vs_benchmark": beta,
        "benchmark": benchmark_symbol,
        "max_drawdown_pct": round(max_dd * 100, 2),
        "sharpe_ratio_approx": sharpe,
    }


def calculate_fcf_yield(symbol: str) -> dict:
    """Compute trailing FCF yield = FCF / market cap."""
    from equity_mcp.tools.calculations.valuation import _latest_price
    income = get_income_statement(symbol, "annual", 1)
    cf = get_cash_flow(symbol, "annual", 1)
    if not income or not cf:
        return {"symbol": symbol, "error": "Insufficient data"}

    inc = income[0]
    price = _latest_price(symbol)
    fcf = float(cf[0]["free_cash_flow"] or 0)
    shares = float(inc["weighted_average_shares_diluted"] or 0) or None
    market_cap = price * shares if price and shares else None
    fcf_yield = round(fcf / market_cap * 100, 2) if market_cap and market_cap > 0 else None

    return {
        "symbol": symbol,
        "period_end": inc["period_end"],
        "free_cash_flow": round(fcf, 0),
        "market_cap_approx": round(market_cap, 0) if market_cap else None,
        "fcf_yield_pct": fcf_yield,
    }
