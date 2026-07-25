"""
Financial Modeling Prep MCP client — fallback data source for ``tools/db.py``.

Every ``get_*`` function in ``db.py`` queries Supabase first. When the database
is unreachable, the query errors, or the table simply has no rows for that
symbol, it falls through to the same-named function in this module, which
sources the data from FMP's official remote MCP server:

    https://financialmodelingprep.com/mcp?apikey=<FMP_API_KEY>

See https://site.financialmodelingprep.com/developer/docs/mcp-server

The server exposes 28 category tools (``statements``, ``chart``, ``company``,
…), each taking an ``endpoint`` enum that selects the underlying FMP REST
endpoint. Payloads come back as JSON text content in FMP's camelCase field
names, so each function here re-shapes them into the exact snake_case row shape
``db.py`` returns from SQL — callers cannot tell which path served the data.

``fastmcp.Client`` is async-only, but every ``db.py`` function is synchronous
(FastMCP runs sync tools in worker threads). ``asyncio.run`` is not safe here —
it raises if the calling thread already drives a loop — so this module owns one
daemon event loop on a background thread and marshals every call onto it.

That loop outlives the main thread, which is the one hazard worth knowing about.
CPython sets ``concurrent.futures.thread._shutdown`` the moment the main thread
finishes, and everything downstream of a connect — right down to the
``run_in_executor`` that resolves DNS — refuses to schedule after that. A call
started in that window used to die as an opaque ``cannot schedule new futures
after interpreter shutdown``; ``call_tools`` now detects the window and raises
``FmpShuttingDown`` instead, which ``db.py`` logs as the benign teardown race it
is rather than a data failure.
"""

from __future__ import annotations

import asyncio
import atexit
import json
import logging
import os
import threading
from datetime import date, datetime, timedelta
from typing import Any, Iterable, Sequence

_log = logging.getLogger(__name__)

_ENDPOINT = "https://financialmodelingprep.com/mcp"

# Per-call budget, plus a smaller allowance for each extra call in a batch,
# since a batch shares one initialised session.
_CALL_TIMEOUT = 90.0
_EXTRA_CALL_TIMEOUT = 15.0
_MAX_BATCH_TIMEOUT = 600.0

# Margin the calling thread allows on top of the loop's own deadline, so the
# in-loop timeout is what normally fires and the session unwinds cleanly.
_TIMEOUT_GRACE = 10.0

# How long exit waits for the loop thread to stop before giving up on it.
_SHUTDOWN_JOIN_TIMEOUT = 2.0

# Screener page size when enumerating a sector, and how many of those
# constituents (largest first) get aggregated by get_sector_financials.
_SCREENER_LIMIT = 1000
_SECTOR_SAMPLE = 25

# FMP reports subscription limits in prose rather than as a status code.
_PLAN_DENIED_MARKERS = ("access denied", "requires a higher plan", "upgrade your")


class FmpError(RuntimeError):
    """The FMP MCP server was unreachable, refused the key, or returned junk."""


class FmpPlanDenied(FmpError):
    """The endpoint exists but the account's FMP subscription doesn't cover it."""


class FmpShuttingDown(FmpError):
    """The interpreter is tearing down; no new FMP work can be scheduled."""


def _is_plan_denied(text: str) -> bool:
    lowered = text.lower()
    return any(marker in lowered for marker in _PLAN_DENIED_MARKERS)


def _is_shutdown_error(exc: BaseException) -> bool:
    """True for the executor's refusal to schedule once the main thread has gone."""
    return "cannot schedule new futures" in str(exc)


def _shutting_down() -> bool:
    """
    True once the main thread has finished.

    ``threading._shutdown`` runs ``concurrent.futures``' exit hook *before* it
    stops the main thread, so this trails the real flag by a hair — the
    ``_is_shutdown_error`` conversion in ``call_tools`` covers that gap. Both are
    public-API checks; the private ``_shutdown`` globals move between versions.
    """
    return _closed or not threading.main_thread().is_alive()


# ── Background event loop ─────────────────────────────────────────────────────

_loop: asyncio.AbstractEventLoop | None = None
_loop_thread: threading.Thread | None = None
_loop_lock = threading.Lock()
_closed = False


def _background_loop() -> asyncio.AbstractEventLoop:
    """Return the module's event loop, starting its daemon thread on first use."""
    global _loop, _loop_thread
    with _loop_lock:
        if _loop is None or _loop.is_closed():
            loop = asyncio.new_event_loop()
            thread = threading.Thread(
                target=loop.run_forever, name="fmp-mcp-loop", daemon=True
            )
            thread.start()
            _loop, _loop_thread = loop, thread
        return _loop


@atexit.register
def _shutdown_loop() -> None:
    """
    Stop the background loop at exit so nothing is left mid-flight.

    Ordering matters here: CPython runs ``threading._shutdown()`` — and with it
    the flag that breaks scheduling — *before* atexit callbacks, so this is
    cleanup rather than prevention. Its real job is cancelling the reconnect
    timers the MCP streamable-HTTP transport arms after a session closes
    ("GET stream disconnected, reconnecting in 1000ms"), which would otherwise
    fire into a half-torn-down interpreter. The join is bounded so a wedged
    session can never hang the process on the way out.
    """
    global _closed
    _closed = True

    with _loop_lock:
        loop, thread = _loop, _loop_thread
    if loop is None or loop.is_closed():
        return

    def _stop() -> None:
        for task in asyncio.all_tasks(loop):
            task.cancel()
        loop.stop()

    try:
        loop.call_soon_threadsafe(_stop)
    except RuntimeError:
        return  # loop already closed underneath us
    if thread is not None:
        thread.join(timeout=_SHUTDOWN_JOIN_TIMEOUT)


def _server_url() -> str:
    key = os.environ.get("FMP_API_KEY", "")
    if not key:
        raise FmpError("FMP_API_KEY not set — cannot reach the FMP MCP server")
    return f"{_ENDPOINT}?apikey={key}"


# ── Call machinery ────────────────────────────────────────────────────────────


def _coerce(value: Any) -> Any:
    """
    Parse an FMP payload that arrived as a JSON string.

    The FMP tools declare a string return type, so their JSON reaches us as text
    either way: as a content block, or — since fastmcp wraps non-dict output
    under a single "result" key — as a string sitting inside structured content.
    Anything already decoded passes through untouched.
    """
    if not isinstance(value, str):
        return value

    text = value.strip()
    if not text:
        raise FmpError("FMP MCP returned an empty payload")
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        # FMP reports auth/plan failures as plain prose, not JSON.
        if _is_plan_denied(text):
            raise FmpPlanDenied(text[:200]) from exc
        raise FmpError(f"FMP MCP returned non-JSON payload: {text[:200]}") from exc


def _unwrap(result: Any) -> Any:
    """Turn a fastmcp CallToolResult (or a bare content list) into Python data."""
    structured = getattr(result, "structured_content", None)
    if isinstance(structured, dict) and structured:
        if len(structured) == 1 and "result" in structured:
            return _coerce(structured["result"])
        return structured

    blocks = getattr(result, "content", None)
    if blocks is None:
        blocks = result if isinstance(result, (list, tuple)) else []

    texts = [t for t in (getattr(b, "text", None) for b in blocks) if t]
    if not texts:
        raise FmpError("FMP MCP returned no text content")

    return _coerce("\n".join(texts))


async def _acall_many(
    calls: Sequence[tuple[str, dict]], skip_errors: bool, timeout: float
) -> list[Any]:
    """
    Run every call over one session, under a deadline the loop itself enforces.

    Holding the timeout here rather than on the calling thread is what makes it
    cancel: ``Future.cancel()`` cannot stop a coroutine that has already started,
    so the old arrangement left ``Client`` sessions open and reconnecting long
    after the caller had given up. An ``asyncio.timeout`` unwinds the ``async
    with`` instead, closing the session on the way out.
    """
    from fastmcp import Client

    results: list[Any] = []
    async with asyncio.timeout(timeout):
        # Connecting is inside the try so a failure here carries the same context
        # as a tool failure, rather than escaping raw to call_tools.
        try:
            async with Client(_server_url()) as client:
                for name, arguments in calls:
                    args = {k: v for k, v in arguments.items() if v is not None}
                    try:
                        results.append(_unwrap(await client.call_tool(name, args)))
                    except FmpError:
                        raise
                    except Exception as exc:
                        if _is_plan_denied(str(exc)):
                            raise FmpPlanDenied(str(exc)) from exc
                        if not skip_errors:
                            raise FmpError(
                                f"FMP MCP tool {name}{args} failed: {exc}"
                            ) from exc
                        _log.warning("FMP MCP tool %s%s failed: %s", name, args, exc)
                        results.append(None)
        except FmpError:
            raise
        except Exception as exc:
            if _is_shutdown_error(exc):
                raise FmpShuttingDown(str(exc)) from exc
            raise FmpError(f"FMP MCP session failed: {exc}") from exc
    return results


def call_tools(
    calls: Iterable[tuple[str, dict]], *, skip_errors: bool = False
) -> list[Any]:
    """
    Run a batch of ``(tool_name, arguments)`` over a single MCP session.

    Returns one decoded payload per call, in order. With ``skip_errors=True`` a
    failing call yields ``None`` instead of aborting the whole batch — used by
    the fan-out in get_sector_financials, where a few unavailable symbols
    shouldn't sink the aggregate.

    Raises ``FmpShuttingDown`` rather than attempting a doomed connect once the
    interpreter is on its way out.
    """
    calls = list(calls)
    if not calls:
        return []

    if _shutting_down():
        raise FmpShuttingDown("interpreter is shutting down")

    timeout = min(
        _CALL_TIMEOUT + _EXTRA_CALL_TIMEOUT * (len(calls) - 1), _MAX_BATCH_TIMEOUT
    )
    try:
        future = asyncio.run_coroutine_threadsafe(
            _acall_many(calls, skip_errors, timeout), _background_loop()
        )
    except RuntimeError as exc:
        # The loop shut down between the guard above and scheduling.
        raise FmpShuttingDown(str(exc)) from exc

    try:
        # The loop's own deadline should fire first; this is only a backstop for
        # a loop that has stopped servicing work altogether.
        return future.result(timeout=timeout + _TIMEOUT_GRACE)
    except FmpError:
        raise
    except TimeoutError as exc:
        future.cancel()
        raise FmpError(f"FMP MCP call exceeded {timeout:g}s") from exc
    except Exception as exc:
        future.cancel()
        if _is_shutdown_error(exc) or _shutting_down():
            raise FmpShuttingDown(str(exc)) from exc
        raise FmpError(f"FMP MCP call failed: {exc}") from exc


def call_tool(name: str, **arguments: Any) -> Any:
    """Run a single FMP MCP tool call and return its decoded payload."""
    return call_tools([(name, arguments)])[0]


# ── Payload normalisation ─────────────────────────────────────────────────────


def _rows(payload: Any) -> list[dict]:
    """Normalise an FMP payload to a list of dicts, raising on error envelopes."""
    if payload is None:
        return []
    if isinstance(payload, dict):
        for key in ("Error Message", "error"):
            if key in payload:
                raise FmpError(str(payload[key]))
        return [payload]
    if isinstance(payload, list):
        return [r for r in payload if isinstance(r, dict)]
    raise FmpError(f"unexpected FMP payload type: {type(payload).__name__}")


def _iso_date(value: Any) -> str | None:
    """Coerce an FMP date (str or datetime) to a YYYY-MM-DD string."""
    if isinstance(value, datetime):
        return value.date().isoformat()
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, str) and value:
        return value[:10]
    return None


def _pick(row: dict, *keys: str) -> Any:
    """Return the first non-null value among ``keys`` — FMP renames fields between plans."""
    for key in keys:
        value = row.get(key)
        if value is not None:
            return value
    return None


def _asset_type(row: dict) -> str | None:
    if "isEtf" not in row and "isFund" not in row:
        return None
    if row.get("isEtf"):
        return "etf"
    if row.get("isFund"):
        return "fund"
    return "stock"


# ── Universe / Reference ──────────────────────────────────────────────────────


def get_research_universe() -> list[dict]:
    """FMP fallback for db.get_research_universe — directory/actively-trading-list."""
    rows = _rows(call_tool("directory", endpoint="actively-trading-list"))
    return [
        {
            "symbol": r.get("symbol"),
            "name": _pick(r, "name", "companyName"),
            "exchange": _pick(r, "exchange", "exchangeShortName"),
            "asset_type": _asset_type(r),
            "currency": r.get("currency"),
            "country": r.get("country"),
        }
        for r in rows
        if r.get("symbol")
    ]


def get_company_profile(symbol: str) -> dict | None:
    """FMP fallback for db.get_company_profile — company/profile-symbol."""
    rows = _rows(call_tool("company", endpoint="profile-symbol", symbol=symbol.upper()))
    if not rows:
        return None
    r = rows[0]
    return {
        "symbol": r.get("symbol"),
        "name": r.get("companyName"),
        "exchange": _pick(r, "exchange", "exchangeFullName"),
        "asset_type": _asset_type(r),
        "currency": r.get("currency"),
        "country": r.get("country"),
        "cik": r.get("cik"),
        "isin": r.get("isin"),
        "cusip": r.get("cusip"),
        "sector": r.get("sector"),
        "industry": r.get("industry"),
        "ipo_date": _iso_date(r.get("ipoDate")),
        "description": r.get("description"),
        "website": r.get("website"),
    }


def get_sector_peers(symbol: str) -> list[dict]:
    """
    FMP fallback for db.get_sector_peers.

    Resolves the symbol's sector via company/profile-symbol, then enumerates the
    sector with search/search-company-screener — matching the SQL, which returns
    every actively-trading name in the sector rather than a curated peer list.
    """
    symbol = symbol.upper()
    profile = _rows(call_tool("company", endpoint="profile-symbol", symbol=symbol))
    sector = profile[0].get("sector") if profile else None
    if not sector:
        return []

    rows = _rows(
        call_tool(
            "search",
            endpoint="search-company-screener",
            sector=sector,
            isActivelyTrading=True,
            limit=_SCREENER_LIMIT,
        )
    )
    peers = [
        {
            "symbol": r.get("symbol"),
            "name": _pick(r, "companyName", "name"),
            "exchange": _pick(r, "exchangeShortName", "exchange"),
            "sector": r.get("sector"),
            "industry": r.get("industry"),
        }
        for r in rows
        if r.get("symbol") and r.get("symbol") != symbol
    ]
    return sorted(peers, key=lambda r: r["symbol"] or "")


# ── Price Data ────────────────────────────────────────────────────────────────


def get_price_history(symbol: str, from_date: str, to_date: str) -> list[dict]:
    """
    FMP fallback for db.get_price_history — chart/historical-price-eod-full.

    The full EOD series carries raw OHLCV but no adjusted close, so the
    dividend-adjusted series is merged in on date. That endpoint is plan-gated,
    so it is best-effort: adj_close stays null rather than failing the call.
    """
    symbol = symbol.upper()
    bars = _rows(
        call_tool(
            "chart",
            endpoint="historical-price-eod-full",
            symbol=symbol,
            from_date=from_date,
            to_date=to_date,
        )
    )

    adjusted: dict[str, Any] = {}
    try:
        for r in _rows(
            call_tool(
                "chart",
                endpoint="historical-price-eod-dividend-adjusted",
                symbol=symbol,
                from_date=from_date,
                to_date=to_date,
            )
        ):
            day = _iso_date(r.get("date"))
            if day:
                adjusted[day] = _pick(r, "adjClose", "adjustedClose", "close")
    except FmpError as exc:
        _log.info("dividend-adjusted series unavailable for %s: %s", symbol, exc)

    out = []
    for r in bars:
        day = _iso_date(r.get("date"))
        if not day:
            continue
        out.append(
            {
                "date": day,
                "open": r.get("open"),
                "high": r.get("high"),
                "low": r.get("low"),
                "close": r.get("close"),
                "adj_close": adjusted.get(day, _pick(r, "adjClose")),
                "volume": r.get("volume"),
            }
        )
    # FMP returns newest-first; the SQL orders ascending.
    return sorted(out, key=lambda r: r["date"])


# ── Fundamental Data ──────────────────────────────────────────────────────────


def _statement_head(row: dict, period_type: str) -> dict:
    """The five identifying columns every core.*_statement row shares."""
    return {
        "period_end": _iso_date(row.get("date")),
        "period_type": period_type,
        "reported_currency": row.get("reportedCurrency"),
        "filing_date": _iso_date(row.get("filingDate")),
    }


def get_income_statement(
    symbol: str, period_type: str = "annual", n_periods: int = 8
) -> list[dict]:
    """FMP fallback for db.get_income_statement — statements/income-statement."""
    rows = _rows(
        call_tool(
            "statements",
            endpoint="income-statement",
            symbol=symbol.upper(),
            period=period_type,
            limit=n_periods,
        )
    )
    return [
        {
            **_statement_head(r, period_type),
            "revenue": r.get("revenue"),
            "gross_profit": r.get("grossProfit"),
            "operating_income": r.get("operatingIncome"),
            "net_income": r.get("netIncome"),
            "eps": r.get("eps"),
            "eps_diluted": _pick(r, "epsDiluted", "epsdiluted"),
        }
        for r in rows
    ]


def get_balance_sheet(
    symbol: str, period_type: str = "annual", n_periods: int = 8
) -> list[dict]:
    """FMP fallback for db.get_balance_sheet — statements/balance-sheet-statement."""
    rows = _rows(
        call_tool(
            "statements",
            endpoint="balance-sheet-statement",
            symbol=symbol.upper(),
            period=period_type,
            limit=n_periods,
        )
    )
    return [
        {
            **_statement_head(r, period_type),
            "total_assets": r.get("totalAssets"),
            "total_liabilities": r.get("totalLiabilities"),
            "total_equity": _pick(r, "totalEquity", "totalStockholdersEquity"),
            "cash_and_short_term_investments": r.get("cashAndShortTermInvestments"),
            "total_debt": r.get("totalDebt"),
        }
        for r in rows
    ]


def get_cash_flow(
    symbol: str, period_type: str = "annual", n_periods: int = 8
) -> list[dict]:
    """FMP fallback for db.get_cash_flow — statements/cashflow-statement."""
    rows = _rows(
        call_tool(
            "statements",
            endpoint="cashflow-statement",
            symbol=symbol.upper(),
            period=period_type,
            limit=n_periods,
        )
    )
    return [
        {
            **_statement_head(r, period_type),
            "operating_cash_flow": _pick(
                r, "operatingCashFlow", "netCashProvidedByOperatingActivities"
            ),
            "capital_expenditure": r.get("capitalExpenditure"),
            "free_cash_flow": r.get("freeCashFlow"),
        }
        for r in rows
    ]


# ── Events & Analyst Data ─────────────────────────────────────────────────────


def get_earnings_calendar(symbol: str, n_events: int = 12) -> list[dict]:
    """FMP fallback for db.get_earnings_calendar — calendar/earnings-company."""
    rows = _rows(
        call_tool(
            "calendar",
            endpoint="earnings-company",
            symbol=symbol.upper(),
            limit=n_events,
        )
    )
    events = [
        {
            "event_date": _iso_date(r.get("date")),
            "time_of_day": _pick(r, "time", "timeOfDay"),
            "eps_estimate": _pick(r, "epsEstimated", "epsEstimate"),
            "eps_actual": _pick(r, "epsActual", "eps"),
            "revenue_estimate": _pick(r, "revenueEstimated", "revenueEstimate"),
            "revenue_actual": _pick(r, "revenueActual", "revenue"),
        }
        for r in rows
        if r.get("date")
    ]
    events.sort(key=lambda r: r["event_date"] or "", reverse=True)
    return events[:n_events]


def get_dividends(symbol: str, n_years: int = 10) -> list[dict]:
    """
    FMP fallback for db.get_dividends — calendar/dividends-company.

    FMP caps by row count rather than by date, so this over-fetches (allowing
    for monthly payers) and applies the n_years cutoff client-side.
    """
    rows = _rows(
        call_tool(
            "calendar",
            endpoint="dividends-company",
            symbol=symbol.upper(),
            limit=n_years * 12 + 4,
        )
    )
    cutoff = (date.today() - timedelta(days=int(n_years * 365.25))).isoformat()

    dividends = []
    for r in rows:
        ex_date = _iso_date(r.get("date"))
        if not ex_date or ex_date < cutoff:
            continue
        dividends.append(
            {
                "ex_date": ex_date,
                "payment_date": _iso_date(r.get("paymentDate")),
                "declaration_date": _iso_date(r.get("declarationDate")),
                "dividend": r.get("dividend"),
                "adjusted_dividend": _pick(r, "adjDividend", "adjustedDividend"),
                "frequency": r.get("frequency"),
            }
        )
    dividends.sort(key=lambda r: r["ex_date"], reverse=True)
    return dividends


def get_analyst_estimates(
    symbol: str, period_type: str = "annual", n_periods: int = 4
) -> list[dict]:
    """FMP fallback for db.get_analyst_estimates — analyst/financial-estimates."""
    rows = _rows(
        call_tool(
            "analyst",
            endpoint="financial-estimates",
            symbol=symbol.upper(),
            period=period_type,
            limit=n_periods,
        )
    )
    estimates = [
        {
            "period_end": _iso_date(r.get("date")),
            "period_type": period_type,
            "eps_estimate": _pick(r, "epsAvg", "estimatedEpsAvg"),
            "revenue_estimate": _pick(r, "revenueAvg", "estimatedRevenueAvg"),
            "num_analysts": _pick(r, "numAnalystsEps", "numAnalystsRevenue"),
        }
        for r in rows
        if r.get("date")
    ]
    estimates.sort(key=lambda r: r["period_end"] or "", reverse=True)
    return estimates[:n_periods]


def get_price_targets(symbol: str, n_recent: int = 20) -> list[dict]:
    """
    FMP fallback for db.get_price_targets — analyst/grades.

    The MCP server exposes only consensus price targets, not the per-analyst
    target rows core.price_targets stores. analyst/grades is the closest match:
    dated rating changes attributed to the issuing firm. The row shape is
    preserved, but target_price and previous_target_price are always null.
    """
    rows = _rows(
        call_tool("analyst", endpoint="grades", symbol=symbol.upper(), limit=n_recent)
    )
    targets = [
        {
            "published_date": _iso_date(r.get("date")),
            "analyst_name": _pick(r, "gradingCompany", "analystName"),
            "rating": _pick(r, "newGrade", "rating"),
            "target_price": None,
            "previous_target_price": None,
            "publisher": _pick(r, "gradingCompany", "publisher"),
        }
        for r in rows
        if r.get("date")
    ]
    targets.sort(key=lambda r: r["published_date"] or "", reverse=True)
    return targets[:n_recent]


def get_sector_financials(sector: str, n_periods: int = 4) -> list[dict]:
    """
    FMP fallback for db.get_sector_financials.

    FMP has no sector-level financial aggregate, so this rebuilds one: screen the
    sector, take the largest _SECTOR_SAMPLE constituents by market cap, pull each
    annual income statement, and sum in Python.

    Two deliberate deviations from the SQL, both unavoidable:
      * only the top _SECTOR_SAMPLE names are summed, not the full sector, to
        keep the fan-out bounded — treat the totals as an index, not a census;
      * rows are bucketed by fiscal year rather than exact period_end, since
        constituents have staggered fiscal year ends and grouping on the raw
        date would shatter each year into single-company buckets. The reported
        period_end is the latest date in the bucket.
    """
    constituents = _rows(
        call_tool(
            "search",
            endpoint="search-company-screener",
            sector=sector,
            isActivelyTrading=True,
            limit=_SCREENER_LIMIT,
        )
    )
    constituents.sort(key=lambda r: r.get("marketCap") or 0, reverse=True)
    symbols = [r["symbol"] for r in constituents[:_SECTOR_SAMPLE] if r.get("symbol")]
    if not symbols:
        return []

    payloads = call_tools(
        [
            (
                "statements",
                {
                    "endpoint": "income-statement",
                    "symbol": symbol,
                    "period": "annual",
                    "limit": n_periods,
                },
            )
            for symbol in symbols
        ],
        skip_errors=True,
    )

    buckets: dict[int, dict[str, Any]] = {}
    for payload in payloads:
        try:
            statements = _rows(payload)
        except FmpError as exc:
            _log.warning("skipping sector constituent: %s", exc)
            continue

        for r in statements:
            period_end = _iso_date(r.get("date"))
            if not period_end:
                continue
            fiscal_year = r.get("fiscalYear") or int(period_end[:4])
            symbol = r.get("symbol")

            bucket = buckets.setdefault(
                int(fiscal_year),
                {
                    "period_end": period_end,
                    "symbols": set(),
                    "revenue": 0.0,
                    "gross_profit": 0.0,
                    "net_income": 0.0,
                    "margins": [],
                },
            )
            if symbol in bucket["symbols"]:
                continue
            bucket["symbols"].add(symbol)
            bucket["period_end"] = max(bucket["period_end"], period_end)

            revenue = float(r.get("revenue") or 0)
            gross_profit = float(r.get("grossProfit") or 0)
            bucket["revenue"] += revenue
            bucket["gross_profit"] += gross_profit
            bucket["net_income"] += float(r.get("netIncome") or 0)
            if revenue:
                bucket["margins"].append(gross_profit / revenue)

    out = []
    for fiscal_year in sorted(buckets, reverse=True)[:n_periods]:
        bucket = buckets[fiscal_year]
        margins = bucket["margins"]
        out.append(
            {
                "period_end": bucket["period_end"],
                "company_count": len(bucket["symbols"]),
                "total_revenue": bucket["revenue"],
                "total_gross_profit": bucket["gross_profit"],
                "avg_gross_margin": sum(margins) / len(margins) if margins else None,
                "total_net_income": bucket["net_income"],
            }
        )
    return out
