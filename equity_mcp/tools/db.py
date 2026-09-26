"""
Market and fundamental data tools, sourced from Financial Modeling Prep.

These twelve tools were originally SQL queries against a Supabase schema
(``ref.symbol``, ``core.income_statement``, …) that has not been provisioned, so
every one of them failed. They now fetch the same figures from FMP via
``tools.external.fmp.fmp_cached``, keeping their original names, signatures and —
the part that matters — their original return-key names: ``tools/calculations/*``
reads those keys directly off the rows and joins the three statements on
``period_end``.

Two ordering invariants are load-bearing, and one of them is the opposite of
FMP's own:

- ``get_price_history`` returns rows **oldest first** (the old ``ORDER BY date``).
  FMP returns newest first, so it is reversed here. Callers index from the end
  (``rows[-1]`` is the latest price) and walk forward from ``rows[0]`` for max
  drawdown, so getting this backwards silently inverts both.
- Everything else returns **newest first** (the old ``ORDER BY … DESC``). FMP
  already does this for statements, dividends and earnings; ``analyst-estimates``
  does not, so it is sorted explicitly.

Fields arrive in FMP's camelCase and are renamed here. Alongside every original
key, the statements now carry the real line items the old schema never stored —
``net_receivables``, ``ppe_net``, ``depreciation_and_amortization``, ``ebitda``,
``weighted_average_shares_diluted``, ``inventory``, ``retained_earnings``,
``total_current_assets`` / ``total_current_liabilities`` — which replaced the
fixed-fraction proxies that used to stand in for them in ``calculations/``. The
additions are purely additive: nothing reading an old key needs to change.

``DATABASE_URL`` is unused while this is in place.
"""

from __future__ import annotations

from datetime import date, timedelta
from typing import Any

from equity_mcp.tools.external.fmp import fmp_cached

# Screener page size when a caller wants "the universe". The full FMP symbol
# list is ~40,000 rows, which is neither useful to an agent nor affordable to
# iterate over, so the universe is the largest N by market cap.
_UNIVERSE_LIMIT = 500

# Peers returned by get_sector_peers, largest first. compare_peer_valuations
# slices this further — every peer it keeps costs five HTTP requests.
_PEER_LIMIT = 50

# Companies aggregated by get_sector_financials. Each one is a separate income
# statement request, so this is the knob that decides that tool's runtime.
_SECTOR_SAMPLE = 15


# ── Shaping helpers ───────────────────────────────────────────────────────────


def _rows(payload: Any) -> list[dict]:
    """Normalise an FMP payload to a list of dict rows."""
    if isinstance(payload, list):
        return [r for r in payload if isinstance(r, dict)]
    if isinstance(payload, dict):
        return [payload]
    return []


def _pick(row: dict, mapping: dict[str, str]) -> dict:
    """Project an FMP row onto our field names. A field FMP omits becomes None."""
    return {ours: row.get(theirs) for ours, theirs in mapping.items()}


def _newest_first(rows: list[dict], key: str) -> list[dict]:
    return sorted(rows, key=lambda r: r.get(key) or "", reverse=True)


_PERIOD_ALIASES = {
    "annual": "annual",
    "annually": "annual",
    "fy": "annual",
    "year": "annual",
    "quarter": "quarter",
    "quarterly": "quarter",
    "q": "quarter",
}


def _fmp_period(period_type: str) -> str:
    """Map our period_type onto FMP's `period` parameter."""
    key = (period_type or "annual").strip().lower()
    if key not in _PERIOD_ALIASES:
        raise ValueError(
            f"period_type must be 'annual' or 'quarter', got {period_type!r}"
        )
    return _PERIOD_ALIASES[key]


def _period_type_of(row: dict, requested: str) -> str:
    """
    Report the period a row actually covers.

    FMP labels rows "FY" or "Q1".."Q4"; the old schema stored the same two values
    this function returns. Falls back to what the caller asked for.
    """
    period = str(row.get("period") or "").upper()
    if period == "FY":
        return "annual"
    if period.startswith("Q"):
        return "quarter"
    return requested


def _asset_type(row: dict) -> str:
    if row.get("isEtf"):
        return "etf"
    if row.get("isFund"):
        return "fund"
    return "stock"


# ── Universe / Reference ──────────────────────────────────────────────────────

_PROFILE = {
    "symbol": "symbol",
    "name": "companyName",
    "exchange": "exchangeShortName",
    "currency": "currency",
    "country": "country",
    "cik": "cik",
    "isin": "isin",
    "cusip": "cusip",
    "sector": "sector",
    "industry": "industry",
    "ipo_date": "ipoDate",
    "description": "description",
    "website": "website",
    # Not in the old schema, cheap to pass along, useful to an analyst.
    "price": "price",
    "market_cap": "marketCap",
    "beta": "beta",
    "ceo": "ceo",
    "full_time_employees": "fullTimeEmployees",
    "is_actively_trading": "isActivelyTrading",
}

_SCREENER = {
    "symbol": "symbol",
    "name": "companyName",
    "exchange": "exchangeShortName",
    "country": "country",
    "sector": "sector",
    "industry": "industry",
    "market_cap": "marketCap",
}


def _screen(limit: int, **filters: Any) -> list[dict]:
    """Run the FMP company screener and return rows largest-market-cap first."""
    payload = fmp_cached(
        "company-screener",
        limit=max(int(limit), 1),
        isActivelyTrading="true",
        **filters,
    )
    rows = []
    for row in _rows(payload):
        mapped = _pick(row, _SCREENER)
        mapped["asset_type"] = _asset_type(row)
        # The old ref.symbol carried a currency; the screener does not expose one.
        mapped.setdefault("currency", None)
        rows.append(mapped)
    rows.sort(key=lambda r: r.get("market_cap") or 0, reverse=True)
    return rows


def get_research_universe(limit: int = _UNIVERSE_LIMIT) -> list[dict]:
    """
    Return actively trading symbols, largest market cap first.

    FMP lists roughly 40,000 symbols, so this is the top `limit` by market cap
    rather than every listing — a bounded, ranked universe is what the factor
    screens actually want.
    """
    return _screen(limit)


def get_company_profile(symbol: str) -> dict | None:
    """
    Return company profile including sector, industry, geography and description.
    """
    rows = _rows(fmp_cached("profile", symbol=symbol.upper()))
    if not rows:
        return None
    profile = _pick(rows[0], _PROFILE)
    profile["asset_type"] = _asset_type(rows[0])
    return profile


def get_sector_peers(symbol: str, limit: int = _PEER_LIMIT) -> list[dict]:
    """
    Return other tickers in the same sector, largest market cap first.

    Ordered by size deliberately: callers cap the list, and the largest names are
    the more informative comparables.
    """
    profile = get_company_profile(symbol)
    sector = (profile or {}).get("sector")
    if not sector:
        return []

    target = symbol.upper()
    peers = _screen(limit + 1, sector=sector)
    return [row for row in peers if row.get("symbol") != target][:limit]


# ── Price Data ────────────────────────────────────────────────────────────────


def get_price_history(symbol: str, from_date: str, to_date: str) -> list[dict]:
    """
    Return daily OHLCV + adj_close rows for symbol between from_date and to_date,
    oldest first. Dates should be ISO format strings: YYYY-MM-DD.
    """
    payload = fmp_cached(
        "historical-price-eod/dividend-adjusted",
        symbol=symbol.upper(),
        # "from" is a Python keyword, so it cannot be passed as a bare kwarg.
        **{"from": from_date, "to": to_date},
    )

    rows = []
    for row in _rows(payload):
        close = row.get("adjClose")
        rows.append(
            {
                "date": row.get("date"),
                "open": row.get("adjOpen"),
                "high": row.get("adjHigh"),
                "low": row.get("adjLow"),
                # This endpoint reports dividend-adjusted prices only; the /full
                # variant carries a raw close but no adjClose at all.
                "close": close,
                "adj_close": close,
                "volume": row.get("volume"),
            }
        )

    # Ascending — callers read rows[-1] as the latest bar and walk forward.
    rows.sort(key=lambda r: r.get("date") or "")
    return rows


# ── Fundamental Data ──────────────────────────────────────────────────────────

_INCOME = {
    "period_end": "date",
    "reported_currency": "reportedCurrency",
    "filing_date": "filingDate",
    "fiscal_year": "fiscalYear",
    "revenue": "revenue",
    "cost_of_revenue": "costOfRevenue",
    "gross_profit": "grossProfit",
    "operating_income": "operatingIncome",
    "net_income": "netIncome",
    "eps": "eps",
    "eps_diluted": "epsDiluted",
    # Line items the old schema lacked; these replaced proxies in calculations/.
    "ebitda": "ebitda",
    "ebit": "ebit",
    "depreciation_and_amortization": "depreciationAndAmortization",
    "sga": "sellingGeneralAndAdministrativeExpenses",
    "interest_expense": "interestExpense",
    "weighted_average_shares": "weightedAverageShsOut",
    "weighted_average_shares_diluted": "weightedAverageShsOutDil",
}

_BALANCE = {
    "period_end": "date",
    "reported_currency": "reportedCurrency",
    "filing_date": "filingDate",
    "fiscal_year": "fiscalYear",
    "total_assets": "totalAssets",
    "total_liabilities": "totalLiabilities",
    "total_equity": "totalEquity",
    "cash_and_short_term_investments": "cashAndShortTermInvestments",
    "total_debt": "totalDebt",
    # Line items the old schema lacked.
    "net_receivables": "netReceivables",
    "inventory": "inventory",
    "ppe_net": "propertyPlantEquipmentNet",
    "goodwill_and_intangibles": "goodwillAndIntangibleAssets",
    "total_current_assets": "totalCurrentAssets",
    "total_current_liabilities": "totalCurrentLiabilities",
    "retained_earnings": "retainedEarnings",
    "short_term_debt": "shortTermDebt",
    "long_term_debt": "longTermDebt",
    "net_debt": "netDebt",
}

_CASH_FLOW = {
    "period_end": "date",
    "reported_currency": "reportedCurrency",
    "filing_date": "filingDate",
    "fiscal_year": "fiscalYear",
    "operating_cash_flow": "operatingCashFlow",
    "capital_expenditure": "capitalExpenditure",
    "free_cash_flow": "freeCashFlow",
    # Line items the old schema lacked.
    "net_income": "netIncome",
    "depreciation_and_amortization": "depreciationAndAmortization",
    "stock_based_compensation": "stockBasedCompensation",
    "change_in_working_capital": "changeInWorkingCapital",
    "dividends_paid": "netDividendsPaid",
    "share_repurchase": "commonStockRepurchased",
}


def _statement(
    path: str,
    mapping: dict[str, str],
    symbol: str,
    period_type: str,
    n_periods: int,
) -> list[dict]:
    """Fetch one financial statement, newest period first."""
    period = _fmp_period(period_type)
    payload = fmp_cached(
        path,
        symbol=symbol.upper(),
        period=period,
        limit=max(int(n_periods), 1),
    )

    rows = []
    for row in _rows(payload):
        mapped = _pick(row, mapping)
        mapped["period_type"] = _period_type_of(row, period)
        rows.append(mapped)

    return _newest_first(rows, "period_end")[: max(int(n_periods), 1)]


def get_income_statement(
    symbol: str, period_type: str = "annual", n_periods: int = 8
) -> list[dict]:
    """
    Return income statement rows ordered newest first.
    period_type: 'annual' | 'quarter'
    """
    return _statement("income-statement", _INCOME, symbol, period_type, n_periods)


def get_balance_sheet(
    symbol: str, period_type: str = "annual", n_periods: int = 8
) -> list[dict]:
    """Return balance sheet rows ordered newest first."""
    return _statement(
        "balance-sheet-statement", _BALANCE, symbol, period_type, n_periods
    )


def get_cash_flow(
    symbol: str, period_type: str = "annual", n_periods: int = 8
) -> list[dict]:
    """Return cash flow rows ordered newest first."""
    return _statement("cash-flow-statement", _CASH_FLOW, symbol, period_type, n_periods)


# ── Events & Analyst Data ─────────────────────────────────────────────────────

_EARNINGS = {
    "event_date": "date",
    "eps_estimate": "epsEstimated",
    "eps_actual": "epsActual",
    "revenue_estimate": "revenueEstimated",
    "revenue_actual": "revenueActual",
}

_DIVIDENDS = {
    "ex_date": "date",
    "payment_date": "paymentDate",
    "declaration_date": "declarationDate",
    "record_date": "recordDate",
    "dividend": "dividend",
    "adjusted_dividend": "adjDividend",
    "frequency": "frequency",
    "dividend_yield": "yield",
}

_ESTIMATES = {
    "period_end": "date",
    "eps_estimate": "epsAvg",
    "eps_low": "epsLow",
    "eps_high": "epsHigh",
    "revenue_estimate": "revenueAvg",
    "revenue_low": "revenueLow",
    "revenue_high": "revenueHigh",
    "ebitda_estimate": "ebitdaAvg",
    "net_income_estimate": "netIncomeAvg",
    "num_analysts": "numAnalystsEps",
    "num_analysts_revenue": "numAnalystsRevenue",
}

_PRICE_TARGETS = {
    "published_date": "publishedDate",
    "analyst_name": "analystName",
    "target_price": "priceTarget",
    "adjusted_target_price": "adjPriceTarget",
    "price_when_posted": "priceWhenPosted",
    "publisher": "newsPublisher",
    "analyst_company": "analystCompany",
    "news_title": "newsTitle",
    "news_url": "newsURL",
}


def get_earnings_calendar(symbol: str, n_events: int = 12) -> list[dict]:
    """
    Return earnings events ordered newest first, including EPS/revenue vs estimates.
    Upcoming events appear first and carry null actuals.
    """
    payload = fmp_cached(
        "earnings", symbol=symbol.upper(), limit=max(int(n_events), 1)
    )

    rows = []
    for row in _rows(payload):
        mapped = _pick(row, _EARNINGS)
        # The old schema stored a BMO/AMC marker; FMP does not report one here.
        mapped["time_of_day"] = None
        rows.append(mapped)

    return _newest_first(rows, "event_date")[: max(int(n_events), 1)]


def get_dividends(symbol: str, n_years: int = 10) -> list[dict]:
    """Return dividend history for the past n_years, most recent first."""
    years = max(int(n_years), 1)
    # This endpoint takes no date range, only a row limit — so over-fetch with
    # headroom for monthly payers and trim by date below.
    payload = fmp_cached(
        "dividends", symbol=symbol.upper(), limit=min(years * 12 + 4, 400)
    )

    cutoff = (date.today() - timedelta(days=round(365.25 * years))).isoformat()
    rows = [
        mapped
        for mapped in (_pick(row, _DIVIDENDS) for row in _rows(payload))
        if (mapped.get("ex_date") or "") >= cutoff
    ]
    return _newest_first(rows, "ex_date")


def get_analyst_estimates(
    symbol: str, period_type: str = "annual", n_periods: int = 4
) -> list[dict]:
    """Return analyst consensus EPS and revenue estimates, newest first."""
    period = _fmp_period(period_type)
    # `period` is mandatory on this endpoint — omitting it is an HTTP 400.
    payload = fmp_cached(
        "analyst-estimates",
        symbol=symbol.upper(),
        period=period,
        limit=max(int(n_periods), 1),
    )

    rows = []
    for row in _rows(payload):
        mapped = _pick(row, _ESTIMATES)
        mapped["period_type"] = period
        rows.append(mapped)

    # Sorted explicitly: this endpoint returns ascending dates, and callers treat
    # index 0 as the most recent estimate.
    return _newest_first(rows, "period_end")[: max(int(n_periods), 1)]


def get_price_targets(symbol: str, n_recent: int = 20) -> list[dict]:
    """
    Return recent analyst price targets, newest first.

    FMP publishes the target alongside the note that announced it, which carries
    no rating or prior target — both keys are present and None so the shape is
    unchanged. Use fetch_analyst_grades-style sources for ratings.
    """
    payload = fmp_cached(
        "price-target-news", symbol=symbol.upper(), limit=max(int(n_recent), 1)
    )

    rows = []
    for row in _rows(payload):
        mapped = _pick(row, _PRICE_TARGETS)
        mapped["rating"] = None
        mapped["previous_target_price"] = None
        rows.append(mapped)

    return _newest_first(rows, "published_date")[: max(int(n_recent), 1)]


def get_sector_financials(
    sector: str, n_periods: int = 4, n_companies: int = _SECTOR_SAMPLE
) -> list[dict]:
    """
    Return aggregated revenue, gross profit and net income for a sector, by
    annual period.

    FMP has no sector-aggregate endpoint, so this sums the `n_companies` largest
    companies in the sector rather than every listing — a size-weighted sample of
    the sector, not a census. `company_count` reports how many actually
    contributed to each period.
    """
    peers = _screen(max(int(n_companies), 1), sector=sector)
    if not peers:
        return []

    periods: dict[str, dict] = {}
    for peer in peers:
        symbol = peer.get("symbol")
        if not symbol:
            continue
        try:
            statements = get_income_statement(symbol, "annual", n_periods)
        except Exception:
            # One unavailable company must not sink the whole aggregate.
            continue

        for row in statements:
            period_end = row.get("period_end")
            if not period_end:
                continue
            bucket = periods.setdefault(
                period_end,
                {
                    "period_end": period_end,
                    "company_count": 0,
                    "total_revenue": 0.0,
                    "total_gross_profit": 0.0,
                    "total_net_income": 0.0,
                    "_margins": [],
                },
            )
            revenue = float(row.get("revenue") or 0)
            gross_profit = float(row.get("gross_profit") or 0)
            bucket["company_count"] += 1
            bucket["total_revenue"] += revenue
            bucket["total_gross_profit"] += gross_profit
            bucket["total_net_income"] += float(row.get("net_income") or 0)
            if revenue:
                bucket["_margins"].append(gross_profit / revenue)

    rows = []
    for bucket in periods.values():
        margins = bucket.pop("_margins")
        bucket["avg_gross_margin"] = (
            round(sum(margins) / len(margins), 4) if margins else None
        )
        rows.append(bucket)

    return _newest_first(rows, "period_end")[: max(int(n_periods), 1)]
