"""
Quantitative / factor analysis tools for the Quant Analyst.
"""

from __future__ import annotations

import math
import statistics
from datetime import date, timedelta

from equity_mcp.tools.db import (
    get_analyst_estimates,
    get_balance_sheet,
    get_cash_flow,
    get_income_statement,
    get_price_history,
    get_research_universe,
    get_sector_peers,
)


def _adj_closes(symbol: str, days: int) -> list[float]:
    to_d = date.today().isoformat()
    from_d = (date.today() - timedelta(days=days + 10)).isoformat()
    rows = get_price_history(symbol, from_d, to_d)
    return [float(r["adj_close"]) for r in rows if r["adj_close"]]


def _daily_returns(closes: list[float]) -> list[float]:
    return [(closes[i] / closes[i - 1]) - 1 for i in range(1, len(closes))]


def calculate_momentum_score(
    symbol: str, lookback_days: int = 252
) -> dict:
    """
    Price momentum: total return over lookback_days excluding the most recent
    21 trading days (standard 12-1 momentum to avoid short-term reversal).
    """
    closes = _adj_closes(symbol, lookback_days + 30)
    if len(closes) < lookback_days // 5:
        return {"symbol": symbol, "error": "Insufficient price history"}

    # Skip last ~21 trading days
    skip = min(21, len(closes) - 1)
    start_price = closes[-(lookback_days // 5 + skip)] if len(closes) > lookback_days // 5 + skip else closes[0]
    end_price = closes[-skip]

    momentum = round((end_price / start_price - 1) * 100, 2)
    return {
        "symbol": symbol,
        "lookback_days": lookback_days,
        "momentum_return_pct": momentum,
        "signal": "positive" if momentum > 0 else "negative",
    }


def calculate_value_factor_score(symbol: str) -> dict:
    """
    Composite value factor: combines P/E, P/B proxy, and FCF yield.
    Returns raw values; cross-sectional z-score requires rank_universe_by_factor.
    """
    from equity_mcp.tools.calculations.valuation import calculate_valuation_ratios, calculate_return_on_capital
    ratios = calculate_valuation_ratios(symbol)
    roc = calculate_return_on_capital(symbol)

    return {
        "symbol": symbol,
        "pe_ratio": ratios.get("pe_ratio"),
        "ev_ebitda": ratios.get("ev_ebitda"),
        "price_to_fcf": ratios.get("price_to_fcf"),
        "roe_pct": roc["annual_series"][0]["roe_pct"] if roc.get("annual_series") else None,
    }


def calculate_quality_factor_score(symbol: str) -> dict:
    """
    Quality factor: ROE, gross profit/assets (Novy-Marx), and accruals ratio.
    High quality = high ROE, high gross profit/assets, low accruals.
    """
    income = get_income_statement(symbol, "annual", 1)
    balance = get_balance_sheet(symbol, "annual", 1)
    cf = get_cash_flow(symbol, "annual", 1)

    if not income or not balance:
        return {"symbol": symbol, "error": "Insufficient data"}

    inc = income[0]
    bal = balance[0]
    cf0 = cf[0] if cf else {}

    net_income = float(inc["net_income"] or 0)
    equity = float(bal["total_equity"] or 1)
    assets = float(bal["total_assets"] or 1)
    gross_profit = float(inc["gross_profit"] or 0)
    op_cf = float(cf0.get("operating_cash_flow") or 0)

    roe = net_income / equity
    gross_profit_to_assets = gross_profit / assets
    # Accruals: positive means earnings > cash (lower quality)
    accruals = (net_income - op_cf) / assets

    return {
        "symbol": symbol,
        "period_end": inc["period_end"],
        "roe_pct": round(roe * 100, 2),
        "gross_profit_to_assets": round(gross_profit_to_assets, 4),
        "accruals_ratio": round(accruals, 4),
        "quality_signal": "high" if roe > 0.15 and gross_profit_to_assets > 0.3 and accruals < 0.05 else "low",
    }


def calculate_low_vol_score(symbol: str) -> dict:
    """
    Low-volatility factor: annualised historical vol and beta vs SPY.
    Lower volatility stocks tend to generate risk-adjusted outperformance.
    """
    from equity_mcp.tools.calculations.risk import calculate_price_volatility
    return calculate_price_volatility(symbol, window_days=252)


def calculate_earnings_revision_score(symbol: str) -> dict:
    """
    Estimate revision momentum: compares the most recent consensus EPS estimate
    against the estimate from 3 months prior for the same forward period.
    Positive revision = bullish signal.
    """
    estimates = get_analyst_estimates(symbol, "annual", 6)
    if len(estimates) < 2:
        return {"symbol": symbol, "error": "Insufficient analyst estimate history"}

    latest = estimates[0]
    prior = estimates[1] if len(estimates) > 1 else None

    latest_eps = float(latest["eps_estimate"] or 0)
    prior_eps = float(prior["eps_estimate"] or 0) if prior else None

    revision = None
    if prior_eps:
        revision = round((latest_eps - prior_eps) / abs(prior_eps) * 100, 2)

    return {
        "symbol": symbol,
        "forward_period": latest["period_end"],
        "current_eps_estimate": latest_eps,
        "prior_eps_estimate": prior_eps,
        "revision_pct": revision,
        "signal": "upgrade" if revision and revision > 0 else ("downgrade" if revision and revision < 0 else "flat"),
    }


def calculate_alpha_beta(
    symbol: str, benchmark_symbol: str = "SPY", window_days: int = 252
) -> dict:
    """
    OLS regression of symbol returns on benchmark returns.
    Returns alpha (annualised), beta, and R-squared.
    """
    to_d = date.today().isoformat()
    from_d = (date.today() - timedelta(days=window_days + 30)).isoformat()

    sym_prices = get_price_history(symbol, from_d, to_d)
    bm_prices = get_price_history(benchmark_symbol, from_d, to_d)

    if len(sym_prices) < 60 or len(bm_prices) < 60:
        return {"symbol": symbol, "error": "Insufficient price data"}

    sym_rets = _daily_returns([float(r["adj_close"]) for r in sym_prices if r["adj_close"]])
    bm_rets = _daily_returns([float(r["adj_close"]) for r in bm_prices if r["adj_close"]])

    n = min(len(sym_rets), len(bm_rets))
    y = sym_rets[-n:]
    x = bm_rets[-n:]

    x_mean = sum(x) / n
    y_mean = sum(y) / n
    cov = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(n)) / n
    var_x = sum((x[i] - x_mean) ** 2 for i in range(n)) / n

    beta = cov / var_x if var_x else None
    alpha_daily = y_mean - (beta * x_mean if beta else 0)
    alpha_ann = alpha_daily * 252

    ss_res = sum((y[i] - (alpha_daily + (beta or 0) * x[i])) ** 2 for i in range(n))
    ss_tot = sum((y[i] - y_mean) ** 2 for i in range(n))
    r_squared = 1 - ss_res / ss_tot if ss_tot else None

    return {
        "symbol": symbol,
        "benchmark": benchmark_symbol,
        "window_days": window_days,
        "alpha_annualised_pct": round(alpha_ann * 100, 3),
        "beta": round(beta, 3) if beta else None,
        "r_squared": round(r_squared, 4) if r_squared else None,
    }


def calculate_sharpe_sortino(symbol: str, window_days: int = 252) -> dict:
    """Compute Sharpe and Sortino ratios (assuming 0% risk-free rate)."""
    closes = _adj_closes(symbol, window_days + 10)
    if len(closes) < 30:
        return {"symbol": symbol, "error": "Insufficient price data"}

    rets = _daily_returns(closes)
    mean = sum(rets) / len(rets)
    std = statistics.stdev(rets)
    downside = [r for r in rets if r < 0]
    downside_std = statistics.stdev(downside) if len(downside) > 1 else std

    sharpe = round(mean / std * math.sqrt(252), 3) if std else None
    sortino = round(mean / downside_std * math.sqrt(252), 3) if downside_std else None

    return {
        "symbol": symbol,
        "window_days": window_days,
        "sharpe_ratio": sharpe,
        "sortino_ratio": sortino,
        "annualised_return_pct": round(mean * 252 * 100, 2),
        "annualised_vol_pct": round(std * math.sqrt(252) * 100, 2),
    }


def calculate_correlation_matrix(symbols: list[str], window_days: int = 252) -> dict:
    """
    Compute the pairwise return correlation matrix for a list of symbols.
    Returns a nested dict: {symbol_a: {symbol_b: correlation}}.
    """
    to_d = date.today().isoformat()
    from_d = (date.today() - timedelta(days=window_days + 30)).isoformat()

    all_rets: dict[str, list[float]] = {}
    for sym in symbols:
        rows = get_price_history(sym, from_d, to_d)
        closes = [float(r["adj_close"]) for r in rows if r["adj_close"]]
        if len(closes) > 10:
            all_rets[sym] = _daily_returns(closes)

    if len(all_rets) < 2:
        return {"error": "Need at least 2 symbols with price data"}

    matrix: dict[str, dict[str, float]] = {}
    syms = list(all_rets.keys())
    for i, a in enumerate(syms):
        matrix[a] = {}
        for b in syms:
            if a == b:
                matrix[a][b] = 1.0
                continue
            n = min(len(all_rets[a]), len(all_rets[b]))
            ra = all_rets[a][-n:]
            rb = all_rets[b][-n:]
            mean_a = sum(ra) / n
            mean_b = sum(rb) / n
            cov = sum((ra[k] - mean_a) * (rb[k] - mean_b) for k in range(n)) / n
            std_a = statistics.stdev(ra) or 1e-10
            std_b = statistics.stdev(rb) or 1e-10
            matrix[a][b] = round(cov / (std_a * std_b), 4)

    return {"symbols": syms, "window_days": window_days, "correlations": matrix}


def rank_universe_by_factor(
    factor_name: str,
    universe: list[str] | None = None,
    top_n: int = 20,
) -> dict:
    """
    Rank symbols in the universe by a named factor and return the top_n.
    Supported factor_name values: 'momentum', 'quality', 'value'.
    universe defaults to all active symbols if not provided.
    """
    if universe is None:
        rows = get_research_universe()
        universe = [r["symbol"] for r in rows[:100]]  # cap for performance

    factor_fn = {
        "momentum": lambda s: calculate_momentum_score(s).get("momentum_return_pct"),
        "quality": lambda s: calculate_quality_factor_score(s).get("roe_pct"),
        "value": lambda s: (
            -calculate_value_factor_score(s).get("pe_ratio", 9999) or 0
        ),
    }.get(factor_name)

    if not factor_fn:
        return {"error": f"Unknown factor '{factor_name}'. Choose: momentum, quality, value"}

    results = []
    for sym in universe:
        try:
            score = factor_fn(sym)
            if score is not None:
                results.append({"symbol": sym, "score": score})
        except Exception:
            continue

    results.sort(key=lambda x: x["score"], reverse=True)
    return {
        "factor": factor_name,
        "universe_size": len(universe),
        "top_n": top_n,
        "ranked": results[:top_n],
    }
