"""
Valuation metric calculations for the Value and Growth researchers.
All functions query the DB internally and return structured dicts.
"""

from __future__ import annotations

from datetime import date, timedelta

from equity_mcp.tools.db import (
    get_balance_sheet,
    get_cash_flow,
    get_company_profile,
    get_dividends,
    get_income_statement,
    get_price_history,
    get_sector_peers,
    get_analyst_estimates,
)


def _latest_price(symbol: str) -> float | None:
    today = date.today().isoformat()
    ninety_days_ago = (date.today() - timedelta(days=90)).isoformat()
    rows = get_price_history(symbol, ninety_days_ago, today)
    return float(rows[-1]["adj_close"]) if rows and rows[-1]["adj_close"] else None


def calculate_valuation_ratios(symbol: str) -> dict:
    """
    Compute key valuation multiples: P/E, P/B, EV/EBITDA, P/FCF, dividend yield.
    Returns latest annual figures plus the current market price used.
    """
    price = _latest_price(symbol)
    income = get_income_statement(symbol, "annual", 1)
    balance = get_balance_sheet(symbol, "annual", 1)
    cf = get_cash_flow(symbol, "annual", 1)
    divs = get_dividends(symbol, 2)

    if not income or not balance:
        return {"symbol": symbol, "error": "Insufficient financial data"}

    inc = income[0]
    bal = balance[0]
    cf0 = cf[0] if cf else {}

    eps = float(inc["eps_diluted"] or 0)
    book_value_per_share = (
        float(bal["total_equity"]) / 1 if bal["total_equity"] else None
    )

    pe = round(price / eps, 2) if price and eps else None

    # Approximate EV = market_cap + total_debt - cash
    # We don't have shares outstanding directly — use net income / EPS as proxy
    shares_approx = (
        float(inc["net_income"]) / eps if inc["net_income"] and eps else None
    )
    market_cap = round(price * shares_approx, 0) if price and shares_approx else None
    debt = float(bal["total_debt"] or 0)
    cash = float(bal["cash_and_short_term_investments"] or 0)
    ev = market_cap + debt - cash if market_cap else None

    # EBITDA approximation: operating_income (D&A not separately stored)
    ebitda_approx = float(inc["operating_income"] or 0)
    ev_ebitda = round(ev / ebitda_approx, 2) if ev and ebitda_approx else None

    fcf = float(cf0.get("free_cash_flow") or 0)
    p_fcf = round(market_cap / fcf, 2) if market_cap and fcf else None

    # Trailing annual dividend
    annual_div = sum(float(d["dividend"] or 0) for d in divs[:4])
    div_yield = round(annual_div / price * 100, 2) if price and annual_div else None

    return {
        "symbol": symbol,
        "price": price,
        "period_end": inc["period_end"],
        "pe_ratio": pe,
        "ev_ebitda": ev_ebitda,
        "price_to_fcf": p_fcf,
        "dividend_yield_pct": div_yield,
        "market_cap_approx": market_cap,
        "enterprise_value_approx": ev,
    }


def calculate_owner_earnings(symbol: str) -> dict:
    """
    Buffett owner earnings = net income + D&A – maintenance capex.
    D&A is approximated as (operating_income - net_income) when not available.
    Returns 4 years of annual owner earnings.
    """
    income = get_income_statement(symbol, "annual", 4)
    cf = get_cash_flow(symbol, "annual", 4)

    rows = []
    cf_map = {r["period_end"]: r for r in cf}
    for inc in income:
        pe = inc["period_end"]
        c = cf_map.get(pe, {})
        net_income = float(inc["net_income"] or 0)
        op_cf = float(c.get("operating_cash_flow") or 0)
        capex = abs(float(c.get("capital_expenditure") or 0))
        # D&A proxy: operating CF - net income (rough)
        da_proxy = op_cf - net_income
        owner_earnings = net_income + da_proxy - capex
        rows.append(
            {
                "period_end": pe,
                "net_income": net_income,
                "da_proxy": round(da_proxy, 0),
                "capex": round(capex, 0),
                "owner_earnings": round(owner_earnings, 0),
            }
        )
    return {"symbol": symbol, "annual_series": rows}


def calculate_return_on_capital(symbol: str) -> dict:
    """Compute ROE, ROIC (approx), and ROCE over the last 4 annual periods."""
    income = get_income_statement(symbol, "annual", 4)
    balance = get_balance_sheet(symbol, "annual", 4)

    rows = []
    bal_map = {r["period_end"]: r for r in balance}
    for inc in income:
        pe = inc["period_end"]
        bal = bal_map.get(pe, {})
        net_income = float(inc["net_income"] or 0)
        equity = float(bal.get("total_equity") or 0)
        assets = float(bal.get("total_assets") or 0)
        debt = float(bal.get("total_debt") or 0)
        op_income = float(inc["operating_income"] or 0)
        invested_capital = equity + debt

        rows.append(
            {
                "period_end": pe,
                "roe_pct": round(net_income / equity * 100, 2) if equity else None,
                "roa_pct": round(net_income / assets * 100, 2) if assets else None,
                "roic_pct": round(op_income / invested_capital * 100, 2) if invested_capital else None,
            }
        )
    return {"symbol": symbol, "annual_series": rows}


def calculate_intrinsic_value_dcf(
    symbol: str,
    wacc: float = 0.09,
    terminal_growth: float = 0.025,
    projection_years: int = 10,
) -> dict:
    """
    Simple DCF using trailing FCF as base, growing at the 3-year historical
    average FCF growth rate, discounted at wacc, with a terminal value.
    """
    cf = get_cash_flow(symbol, "annual", 4)
    if len(cf) < 2:
        return {"symbol": symbol, "error": "Insufficient cash flow history for DCF"}

    fcfs = [float(r["free_cash_flow"] or 0) for r in cf]
    base_fcf = fcfs[0]

    # Historical FCF CAGR over available periods
    years_available = len(fcfs) - 1
    if fcfs[-1] and fcfs[-1] > 0 and base_fcf > 0 and years_available > 0:
        hist_growth = (base_fcf / fcfs[-1]) ** (1 / years_available) - 1
        growth_rate = min(max(hist_growth, 0.0), 0.30)  # cap at 30%
    else:
        growth_rate = 0.05

    # Project FCFs
    projected = []
    pv_sum = 0.0
    for t in range(1, projection_years + 1):
        fcf_t = base_fcf * (1 + growth_rate) ** t
        pv = fcf_t / (1 + wacc) ** t
        projected.append({"year": t, "fcf": round(fcf_t, 0), "pv": round(pv, 0)})
        pv_sum += pv

    # Terminal value
    terminal_fcf = base_fcf * (1 + growth_rate) ** projection_years * (1 + terminal_growth)
    terminal_value = terminal_fcf / (wacc - terminal_growth)
    pv_terminal = terminal_value / (1 + wacc) ** projection_years
    intrinsic_value = pv_sum + pv_terminal

    return {
        "symbol": symbol,
        "base_fcf": round(base_fcf, 0),
        "assumed_growth_rate_pct": round(growth_rate * 100, 2),
        "wacc_pct": round(wacc * 100, 2),
        "terminal_growth_pct": round(terminal_growth * 100, 2),
        "pv_of_projected_fcfs": round(pv_sum, 0),
        "pv_of_terminal_value": round(pv_terminal, 0),
        "intrinsic_value_total": round(intrinsic_value, 0),
        "projected_fcfs": projected,
    }


def calculate_revenue_growth_rates(symbol: str, n_periods: int = 6) -> dict:
    """Return YoY revenue growth rates for the last n annual periods."""
    income = get_income_statement(symbol, "annual", n_periods + 1)
    if len(income) < 2:
        return {"symbol": symbol, "error": "Insufficient data"}

    rows = []
    for i in range(len(income) - 1):
        curr = float(income[i]["revenue"] or 0)
        prev = float(income[i + 1]["revenue"] or 0)
        yoy = round((curr - prev) / prev * 100, 2) if prev else None
        rows.append({"period_end": income[i]["period_end"], "revenue": curr, "yoy_growth_pct": yoy})

    # CAGR
    n = len(income) - 1
    rev_latest = float(income[0]["revenue"] or 0)
    rev_oldest = float(income[-1]["revenue"] or 0)
    cagr = round(((rev_latest / rev_oldest) ** (1 / n) - 1) * 100, 2) if rev_oldest > 0 else None

    return {"symbol": symbol, "cagr_pct": cagr, "annual_series": rows}


def calculate_gross_margin_trend(symbol: str, n_periods: int = 8) -> dict:
    """Return gross and operating margin trend over n annual periods."""
    income = get_income_statement(symbol, "annual", n_periods)
    rows = []
    for inc in income:
        rev = float(inc["revenue"] or 0)
        gp = float(inc["gross_profit"] or 0)
        op = float(inc["operating_income"] or 0)
        rows.append(
            {
                "period_end": inc["period_end"],
                "revenue": rev,
                "gross_margin_pct": round(gp / rev * 100, 2) if rev else None,
                "operating_margin_pct": round(op / rev * 100, 2) if rev else None,
            }
        )
    return {"symbol": symbol, "annual_series": rows}


def calculate_rule_of_40(symbol: str) -> dict:
    """
    Rule of 40 = revenue growth % + FCF margin %.
    Score >= 40 is considered healthy for high-growth companies.
    """
    income = get_income_statement(symbol, "annual", 2)
    cf = get_cash_flow(symbol, "annual", 1)

    if len(income) < 2 or not cf:
        return {"symbol": symbol, "error": "Insufficient data"}

    rev_curr = float(income[0]["revenue"] or 0)
    rev_prev = float(income[1]["revenue"] or 0)
    rev_growth = (rev_curr - rev_prev) / rev_prev * 100 if rev_prev else 0

    fcf = float(cf[0]["free_cash_flow"] or 0)
    fcf_margin = fcf / rev_curr * 100 if rev_curr else 0

    return {
        "symbol": symbol,
        "period_end": income[0]["period_end"],
        "revenue_growth_pct": round(rev_growth, 2),
        "fcf_margin_pct": round(fcf_margin, 2),
        "rule_of_40_score": round(rev_growth + fcf_margin, 2),
    }


def compare_peer_valuations(symbol: str) -> dict:
    """
    Compare the symbol's P/E and revenue growth against sector-peer medians.
    Returns peer statistics alongside the target symbol's own ratios.
    """
    target = calculate_valuation_ratios(symbol)
    peers = get_sector_peers(symbol)

    peer_pes = []
    for peer in peers[:20]:  # cap at 20 peers to avoid long runtime
        try:
            r = calculate_valuation_ratios(peer["symbol"])
            if r.get("pe_ratio"):
                peer_pes.append(r["pe_ratio"])
        except Exception:
            continue

    peer_pes_sorted = sorted(peer_pes)
    n = len(peer_pes_sorted)
    median_pe = peer_pes_sorted[n // 2] if n else None

    return {
        "symbol": symbol,
        "target_pe": target.get("pe_ratio"),
        "peer_median_pe": median_pe,
        "peer_count": n,
        "premium_discount_pct": (
            round((target["pe_ratio"] / median_pe - 1) * 100, 1)
            if target.get("pe_ratio") and median_pe
            else None
        ),
    }
