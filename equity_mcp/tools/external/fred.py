"""
FRED (Federal Reserve Economic Data) API tools for the Macro Researcher.
Free API key available at https://fred.stlouisfed.org/docs/api/api_key.html
"""

from __future__ import annotations

import os
from datetime import date, timedelta

import requests

_BASE = "https://api.stlouisfed.org/fred"
_TIMEOUT = 15

# Common series IDs for quick reference
COMMON_SERIES = {
    "gdp":            "GDP",        # US GDP (quarterly, billions $)
    "cpi":            "CPIAUCSL",   # CPI All Urban Consumers
    "fed_funds":      "FEDFUNDS",   # Federal Funds Rate
    "unemployment":   "UNRATE",     # Unemployment Rate
    "10y_treasury":   "GS10",       # 10-Year Treasury Constant Maturity
    "2y_treasury":    "GS2",        # 2-Year Treasury
    "30y_mortgage":   "MORTGAGE30US",
    "pce":            "PCE",        # Personal Consumption Expenditures
    "industrial_prod":"INDPRO",     # Industrial Production Index
    "retail_sales":   "RSXFS",      # Retail Sales ex Food Services
    "m2":             "M2SL",       # M2 Money Stock
    "vix":            "VIXCLS",     # CBOE Volatility Index
}


def fetch_macro_series(series_id: str, from_date: str | None = None) -> dict:
    """
    Fetch a FRED data series by series_id.
    series_id can be a FRED ID (e.g. 'FEDFUNDS') or a shorthand from COMMON_SERIES.
    from_date: ISO date string YYYY-MM-DD (defaults to 2 years ago).
    Returns: {series_id, title, units, frequency, observations: [{date, value}]}.
    """
    api_key = os.environ.get("FRED_API_KEY", "")
    if not api_key:
        return {"error": "FRED_API_KEY not set. Get a free key at fred.stlouisfed.org"}

    resolved_id = COMMON_SERIES.get(series_id.lower(), series_id)
    if from_date is None:
        from_date = (date.today() - timedelta(days=730)).isoformat()

    # Fetch series metadata
    meta_resp = requests.get(
        f"{_BASE}/series",
        params={"series_id": resolved_id, "api_key": api_key, "file_type": "json"},
        timeout=_TIMEOUT,
    )
    meta_resp.raise_for_status()
    meta = meta_resp.json().get("seriess", [{}])[0]

    # Fetch observations
    obs_resp = requests.get(
        f"{_BASE}/series/observations",
        params={
            "series_id": resolved_id,
            "api_key": api_key,
            "file_type": "json",
            "observation_start": from_date,
            "sort_order": "desc",
        },
        timeout=_TIMEOUT,
    )
    obs_resp.raise_for_status()
    observations = [
        {"date": o["date"], "value": None if o["value"] == "." else float(o["value"])}
        for o in obs_resp.json().get("observations", [])
    ]

    return {
        "series_id": resolved_id,
        "title": meta.get("title", ""),
        "units": meta.get("units", ""),
        "frequency": meta.get("frequency", ""),
        "last_updated": meta.get("last_updated", ""),
        "observations": observations[:120],  # cap at ~10 years of monthly data
    }


def fetch_yield_curve() -> dict:
    """
    Fetch the current US Treasury yield curve (2Y, 5Y, 10Y, 30Y) and
    the 2Y-10Y spread as an inversion signal.
    """
    api_key = os.environ.get("FRED_API_KEY", "")
    if not api_key:
        return {"error": "FRED_API_KEY not set"}

    tenors = {"2Y": "GS2", "5Y": "GS5", "10Y": "GS10", "30Y": "GS30"}
    from_date = (date.today() - timedelta(days=30)).isoformat()
    yields: dict[str, float | None] = {}

    for label, sid in tenors.items():
        resp = requests.get(
            f"{_BASE}/series/observations",
            params={
                "series_id": sid, "api_key": api_key, "file_type": "json",
                "observation_start": from_date, "sort_order": "desc", "limit": 1,
            },
            timeout=_TIMEOUT,
        )
        resp.raise_for_status()
        obs = resp.json().get("observations", [])
        yields[label] = float(obs[0]["value"]) if obs and obs[0]["value"] != "." else None

    spread_2_10 = (
        round(yields["10Y"] - yields["2Y"], 3)
        if yields.get("10Y") and yields.get("2Y")
        else None
    )

    return {
        "as_of": date.today().isoformat(),
        "yields": yields,
        "spread_2y_10y": spread_2_10,
        "inversion": spread_2_10 is not None and spread_2_10 < 0,
    }


def fetch_inflation_data(country: str = "US") -> dict:
    """
    Return recent CPI and PCE data for the US (country parameter reserved for
    future multi-country support via World Bank API).
    """
    from_date = (date.today() - timedelta(days=730)).isoformat()
    cpi = fetch_macro_series("CPIAUCSL", from_date)
    pce = fetch_macro_series("PCE", from_date)

    # Calculate YoY CPI change from last two observations 12 months apart
    yoy_cpi = None
    obs = cpi.get("observations", [])
    if len(obs) >= 12:
        latest = obs[0]["value"]
        year_ago = obs[11]["value"]
        if latest and year_ago:
            yoy_cpi = round((latest / year_ago - 1) * 100, 2)

    return {
        "country": country,
        "cpi_yoy_pct": yoy_cpi,
        "cpi_series": cpi.get("observations", [])[:24],
        "pce_series": pce.get("observations", [])[:24],
    }
