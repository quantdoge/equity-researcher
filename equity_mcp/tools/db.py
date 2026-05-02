"""
Supabase / PostgreSQL query tools.

All functions connect using DATABASE_URL from the environment and return plain
dicts / lists so they are easily JSON-serialised by FastMCP.
"""

from __future__ import annotations

import os
from contextlib import contextmanager
from datetime import date, datetime
from typing import Any

import psycopg
from psycopg.rows import dict_row


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


# ── Universe / Reference ──────────────────────────────────────────────────────


def get_research_universe() -> list[dict]:
    """Return all actively trading symbols from the reference schema."""
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT symbol, name, exchange, asset_type, currency, country "
                "FROM ref.symbol WHERE is_active = true ORDER BY symbol"
            )
            return _serialize(cur.fetchall())


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
