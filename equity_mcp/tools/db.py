"""
Supabase / PostgreSQL query tools, with Financial Modeling Prep as a fallback.

All functions connect using DATABASE_URL from the environment and return plain
dicts / lists so they are easily JSON-serialised by FastMCP.

Every ``get_*`` tool tries Supabase first. If the connection or query raises, or
if the query succeeds but returns nothing, it falls through to the same-named
function in ``fmp_mcp``, which sources the data from FMP's official remote MCP
server and re-shapes it into the identical row shape. Callers cannot tell which
path served a given response; failures are logged, never raised, so a dead
database degrades an agent's data rather than crashing its tool loop.
"""

from __future__ import annotations

import functools
import logging
import os
from contextlib import contextmanager
from datetime import date, datetime
from typing import Any, Callable

import psycopg
from psycopg.rows import dict_row

from equity_mcp.tools import fmp_mcp

_log = logging.getLogger(__name__)

# Tools already warned about a subscription limit. A plan denial is a standing
# account fact, not an incident, and a 12-agent run would otherwise repeat the
# same warning hundreds of times.
_plan_warned: set[str] = set()


@contextmanager
def _conn():
    url = os.environ["DATABASE_URL"]
    with psycopg.connect(url, row_factory=dict_row) as conn:
        yield conn


def _serialize(rows: list[dict]) -> list[dict]:
    """Convert date/datetime objects to ISO strings for JSON serialisation."""
    out = []
    for row in rows:
        out.append(
            {
                k: v.isoformat() if isinstance(v, (date, datetime)) else v
                for k, v in row.items()
            }
        )
    return out


def _fmp_fallback(fmp_fn: Callable[..., Any], on_failure: Callable[[], Any] = list):
    """
    Route a SQL query through FMP's MCP server when the database can't serve it.

    ``fmp_fn`` must accept the same arguments as the decorated function and
    return the same row shape. An empty result counts as a miss — a symbol the
    ingestion pipeline hasn't backfilled is worth fetching from FMP, same as an
    unreachable host. If FMP fails too, ``on_failure`` supplies the neutral
    return value (``[]``, or ``None`` for the single-row lookups).

    Two FMP outcomes are logged apart from a genuine failure, because reading
    either as a bug sends you chasing the wrong thing: a subscription limit is a
    standing account fact, and a shutdown race is benign teardown noise.
    """

    def decorate(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                result = fn(*args, **kwargs)
                if result:
                    return result
                _log.info("%s: no rows in database, falling back to FMP", fn.__name__)
            except Exception as exc:
                _log.warning(
                    "%s: database query failed (%s), falling back to FMP",
                    fn.__name__,
                    exc,
                )

            try:
                return fmp_fn(*args, **kwargs)
            except fmp_mcp.FmpPlanDenied as exc:
                if fn.__name__ not in _plan_warned:
                    _plan_warned.add(fn.__name__)
                    _log.warning(
                        "%s: FMP subscription does not cover this data (%s). "
                        "Returning empty — upgrade the FMP plan or backfill the "
                        "database to populate it.",
                        fn.__name__,
                        exc,
                    )
                return on_failure()
            except fmp_mcp.FmpShuttingDown:
                _log.info(
                    "%s: skipped FMP fallback, interpreter is shutting down",
                    fn.__name__,
                )
                return on_failure()
            except Exception as exc:
                _log.error("%s: FMP fallback failed: %s", fn.__name__, exc)
                return on_failure()

        return wrapper

    return decorate


# ── Universe / Reference ──────────────────────────────────────────────────────


@_fmp_fallback(fmp_mcp.get_research_universe)
def get_research_universe() -> list[dict]:
    """Return all actively trading symbols from the reference schema."""
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT symbol, name, exchange, asset_type, currency, country "
                "FROM ref.symbol WHERE is_active = true ORDER BY symbol"
            )
            return _serialize(cur.fetchall())


@_fmp_fallback(fmp_mcp.get_company_profile, on_failure=lambda: None)
def get_company_profile(symbol: str) -> dict | None:
    """
    Return company profile including sector, industry, geography and description.
    Joins ref.symbol and ref.company.
    """
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT s.symbol, s.name, s.exchange, s.asset_type, s.currency,
                       s.country,
                       c.cik, c.isin, c.cusip, c.sector, c.industry,
                       c.ipo_date, c.description, c.website
                FROM ref.symbol s
                LEFT JOIN ref.company c USING (symbol)
                WHERE s.symbol = %s
                """,
                (symbol.upper(),),
            )
            row = cur.fetchone()
            return _serialize([row])[0] if row else None


@_fmp_fallback(fmp_mcp.get_sector_peers)
def get_sector_peers(symbol: str) -> list[dict]:
    """Return all tickers in the same sector as the given symbol."""
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT sector FROM ref.company WHERE symbol = %s", (symbol.upper(),)
            )
            row = cur.fetchone()
            if not row or not row["sector"]:
                return []
            cur.execute(
                """
                SELECT s.symbol, s.name, s.exchange, c.sector, c.industry
                FROM ref.company c
                JOIN ref.symbol s USING (symbol)
                WHERE c.sector = %s AND s.symbol != %s AND s.is_active = true
                ORDER BY s.symbol
                """,
                (row["sector"], symbol.upper()),
            )
            return _serialize(cur.fetchall())


# ── Price Data ────────────────────────────────────────────────────────────────


@_fmp_fallback(fmp_mcp.get_price_history)
def get_price_history(symbol: str, from_date: str, to_date: str) -> list[dict]:
    """
    Return daily OHLCV + adj_close rows for symbol between from_date and to_date.
    Dates should be ISO format strings: YYYY-MM-DD.
    """
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT date, open, high, low, close, adj_close, volume
                FROM core.price_daily
                WHERE symbol = %s AND date BETWEEN %s AND %s
                ORDER BY date
                """,
                (symbol.upper(), from_date, to_date),
            )
            return _serialize(cur.fetchall())


# ── Fundamental Data ──────────────────────────────────────────────────────────


@_fmp_fallback(fmp_mcp.get_income_statement)
def get_income_statement(
    symbol: str, period_type: str = "annual", n_periods: int = 8
) -> list[dict]:
    """
    Return income statement rows ordered newest first.
    period_type: 'annual' | 'quarter'
    """
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT period_end, period_type, reported_currency, filing_date,
                       revenue, gross_profit, operating_income, net_income,
                       eps, eps_diluted
                FROM core.income_statement
                WHERE symbol = %s AND period_type = %s
                ORDER BY period_end DESC
                LIMIT %s
                """,
                (symbol.upper(), period_type, n_periods),
            )
            return _serialize(cur.fetchall())


@_fmp_fallback(fmp_mcp.get_balance_sheet)
def get_balance_sheet(
    symbol: str, period_type: str = "annual", n_periods: int = 8
) -> list[dict]:
    """Return balance sheet rows ordered newest first."""
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT period_end, period_type, reported_currency, filing_date,
                       total_assets, total_liabilities, total_equity,
                       cash_and_short_term_investments, total_debt
                FROM core.balance_sheet
                WHERE symbol = %s AND period_type = %s
                ORDER BY period_end DESC
                LIMIT %s
                """,
                (symbol.upper(), period_type, n_periods),
            )
            return _serialize(cur.fetchall())


@_fmp_fallback(fmp_mcp.get_cash_flow)
def get_cash_flow(
    symbol: str, period_type: str = "annual", n_periods: int = 8
) -> list[dict]:
    """Return cash flow rows ordered newest first."""
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT period_end, period_type, reported_currency, filing_date,
                       operating_cash_flow, capital_expenditure, free_cash_flow
                FROM core.cash_flow
                WHERE symbol = %s AND period_type = %s
                ORDER BY period_end DESC
                LIMIT %s
                """,
                (symbol.upper(), period_type, n_periods),
            )
            return _serialize(cur.fetchall())


# ── Events & Analyst Data ─────────────────────────────────────────────────────


@_fmp_fallback(fmp_mcp.get_earnings_calendar)
def get_earnings_calendar(symbol: str, n_events: int = 12) -> list[dict]:
    """Return earnings events ordered newest first, including EPS/revenue vs estimates."""
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT event_date, time_of_day, eps_estimate, eps_actual,
                       revenue_estimate, revenue_actual
                FROM core.earnings_calendar
                WHERE symbol = %s
                ORDER BY event_date DESC
                LIMIT %s
                """,
                (symbol.upper(), n_events),
            )
            return _serialize(cur.fetchall())


@_fmp_fallback(fmp_mcp.get_dividends)
def get_dividends(symbol: str, n_years: int = 10) -> list[dict]:
    """Return dividend history for the past n_years."""
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT ex_date, payment_date, declaration_date,
                       dividend, adjusted_dividend, frequency
                FROM core.dividends
                WHERE symbol = %s
                  AND ex_date >= (CURRENT_DATE - make_interval(years => %s))
                ORDER BY ex_date DESC
                """,
                (symbol.upper(), n_years),
            )
            return _serialize(cur.fetchall())


@_fmp_fallback(fmp_mcp.get_analyst_estimates)
def get_analyst_estimates(
    symbol: str, period_type: str = "annual", n_periods: int = 4
) -> list[dict]:
    """Return analyst consensus EPS and revenue estimates, newest first."""
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT period_end, period_type, eps_estimate,
                       revenue_estimate, num_analysts
                FROM core.analyst_estimates
                WHERE symbol = %s AND period_type = %s
                ORDER BY period_end DESC
                LIMIT %s
                """,
                (symbol.upper(), period_type, n_periods),
            )
            return _serialize(cur.fetchall())


@_fmp_fallback(fmp_mcp.get_price_targets)
def get_price_targets(symbol: str, n_recent: int = 20) -> list[dict]:
    """Return recent analyst price targets and ratings, newest first."""
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT published_date, analyst_name, rating,
                       target_price, previous_target_price, publisher
                FROM core.price_targets
                WHERE symbol = %s
                ORDER BY published_date DESC
                LIMIT %s
                """,
                (symbol.upper(), n_recent),
            )
            return _serialize(cur.fetchall())


@_fmp_fallback(fmp_mcp.get_sector_financials)
def get_sector_financials(sector: str, n_periods: int = 4) -> list[dict]:
    """
    Return aggregated revenue, gross profit and net income across all companies
    in a sector, grouped by period_end (annual).
    """
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT i.period_end,
                       count(distinct i.symbol)        AS company_count,
                       sum(i.revenue)                  AS total_revenue,
                       sum(i.gross_profit)             AS total_gross_profit,
                       avg(i.gross_profit / nullif(i.revenue, 0)) AS avg_gross_margin,
                       sum(i.net_income)               AS total_net_income
                FROM core.income_statement i
                JOIN ref.company c USING (symbol)
                WHERE c.sector = %s AND i.period_type = 'annual'
                GROUP BY i.period_end
                ORDER BY i.period_end DESC
                LIMIT %s
                """,
                (sector, n_periods),
            )
            return _serialize(cur.fetchall())
