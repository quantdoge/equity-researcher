"""
Alternative data tools for the Alternative Data Analyst.
Covers Google Trends (pytrends), USPTO patent API, and earnings surprise history.
Social sentiment uses web search as a proxy when dedicated APIs are absent.
"""

from __future__ import annotations

import os
import re
import time
from datetime import date, timedelta

import requests

from equity_mcp.tools.db import get_earnings_calendar


def fetch_google_trends(keyword: str, geo: str = "US", timeframe: str = "today 12-m") -> dict:
    """
    Fetch Google Trends interest-over-time for a keyword.
    timeframe examples: 'today 12-m', 'today 5-y', '2023-01-01 2024-01-01'
    Returns weekly interest values (0–100).
    """
    try:
        from pytrends.request import TrendReq
    except ImportError:
        return {"error": "pytrends not installed. Run: pip install pytrends"}

    try:
        pt = TrendReq(hl="en-US", tz=0, timeout=(10, 30))
        pt.build_payload([keyword], cat=0, timeframe=timeframe, geo=geo, gprop="")
        data = pt.interest_over_time()
        if data.empty:
            return {"keyword": keyword, "geo": geo, "data": []}
        rows = [
            {"date": str(idx.date()), "interest": int(row[keyword])}
            for idx, row in data.iterrows()
            if not row.get("isPartial", False)
        ]
        return {
            "keyword": keyword,
            "geo": geo,
            "timeframe": timeframe,
            "data": rows[-52:],  # last year of weekly data
        }
    except Exception as exc:
        return {"keyword": keyword, "error": str(exc)}


def fetch_patent_filing_trend(company_name: str, n_years: int = 5) -> dict:
    """
    Fetch patent application counts by year from the USPTO PatentsView API.
    Rising patent filings signal increasing R&D investment.
    """
    base_url = "https://api.patentsview.org/patents/query"
    start_year = date.today().year - n_years

    try:
        payload = {
            "q": {"_contains": {"assignee_organization": company_name}},
            "f": ["patent_id", "patent_date", "patent_title"],
            "o": {"per_page": 100, "page": 1},
        }
        resp = requests.post(base_url, json=payload, timeout=20)
        resp.raise_for_status()
        patents = resp.json().get("patents", []) or []

        # Count by year
        yearly: dict[int, int] = {}
        for p in patents:
            yr_str = (p.get("patent_date") or "")[:4]
            if yr_str.isdigit():
                yr = int(yr_str)
                if yr >= start_year:
                    yearly[yr] = yearly.get(yr, 0) + 1

        trend = [{"year": yr, "patent_count": cnt} for yr, cnt in sorted(yearly.items())]
        total = sum(c["patent_count"] for c in trend)

        return {
            "company": company_name,
            "total_patents_found": total,
            "by_year": trend,
            "note": "Counts patents with assignee name containing the query string",
        }
    except Exception as exc:
        return {"company": company_name, "error": str(exc)}


def calculate_earnings_surprise_history(symbol: str, n_quarters: int = 8) -> dict:
    """
    Compute earnings surprise (beat/miss) history from core.earnings_calendar.
    Returns beat rate, average surprise magnitude, and per-quarter detail.
    """
    events = get_earnings_calendar(symbol, n_events=n_quarters)
    rows = []
    beats = 0
    misses = 0
    surprise_pcts = []

    for e in events:
        est = e.get("eps_estimate")
        act = e.get("eps_actual")
        if est is None or act is None:
            rows.append({"event_date": e["event_date"], "result": "no_data"})
            continue

        est_f = float(est)
        act_f = float(act)
        surprise = act_f - est_f
        surprise_pct = (surprise / abs(est_f) * 100) if est_f != 0 else None
        beat = act_f >= est_f

        if beat:
            beats += 1
        else:
            misses += 1
        if surprise_pct is not None:
            surprise_pcts.append(surprise_pct)

        rows.append({
            "event_date": e["event_date"],
            "eps_estimate": est_f,
            "eps_actual": act_f,
            "surprise": round(surprise, 4),
            "surprise_pct": round(surprise_pct, 2) if surprise_pct else None,
            "result": "beat" if beat else "miss",
        })

    total = beats + misses
    return {
        "symbol": symbol,
        "quarters_analysed": total,
        "beat_rate_pct": round(beats / total * 100, 1) if total else None,
        "avg_surprise_pct": round(sum(surprise_pcts) / len(surprise_pcts), 2) if surprise_pcts else None,
        "quarterly_detail": rows,
    }


def fetch_job_postings_trend(company_name: str, role_filter: str = "") -> dict:
    """
    Proxy for job posting trends via a web search on LinkedIn/Indeed.
    Returns search results about hiring activity — a proxy for growth signals.
    """
    from equity_mcp.tools.web import web_search
    query = f'"{company_name}" hiring jobs {role_filter} site:linkedin.com OR site:indeed.com'
    results = web_search(query, n_results=5)
    return {
        "company": company_name,
        "role_filter": role_filter,
        "note": "Job posting data retrieved via web search proxy — integrate Thinknum or LinkedIn API for quantitative counts",
        "results": results,
    }


def fetch_social_sentiment(symbol: str, platform: str = "reddit") -> dict:
    """
    Proxy social sentiment via web search on Reddit / StockTwits.
    Integrate Reddit API or StockTwits API for real-time data.
    """
    from equity_mcp.tools.web import web_search
    if platform == "reddit":
        query = f"{symbol} stock site:reddit.com/r/wallstreetbets OR site:reddit.com/r/investing"
    else:
        query = f"{symbol} stocktwits sentiment cashtag"

    results = web_search(query, n_results=5)
    return {
        "symbol": symbol,
        "platform": platform,
        "note": "Social sentiment retrieved via web search — integrate Reddit or StockTwits API for quantitative sentiment scores",
        "results": results,
    }


def fetch_web_traffic_trend(domain: str) -> dict:
    """
    Proxy web traffic via SimilarWeb public data (no API key required for basic).
    Integrate SimilarWeb API for historical monthly visit data.
    """
    from equity_mcp.tools.web import web_search
    results = web_search(f"site:similarweb.com {domain} traffic monthly visits", n_results=3)
    return {
        "domain": domain,
        "note": "Web traffic estimate retrieved via web search — integrate SimilarWeb API for precise monthly visit data",
        "results": results,
    }
