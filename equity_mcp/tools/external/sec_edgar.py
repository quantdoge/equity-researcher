"""
SEC EDGAR API tools.
No API key required — EDGAR is a free public service.
Set SEC_USER_AGENT env var to a descriptive string per EDGAR fair-use policy.
"""

from __future__ import annotations

import os

import requests

_EDGAR_BASE = "https://data.sec.gov"
_EFTS_BASE = "https://efts.sec.gov"
_TIMEOUT = 20


def _headers() -> dict:
    agent = os.environ.get(
        "SEC_USER_AGENT", "equity-researcher/0.1 contact@example.com"
    )
    return {"User-Agent": agent, "Accept": "application/json"}


def fetch_company_facts(symbol: str) -> dict:
    """
    Return SEC filing metadata for the company — CIK lookup and available
    submission types.  Useful for finding 10-K and 10-Q filings.
    """
    # Map ticker to CIK via EDGAR company search
    search_resp = requests.get(
        f"https://efts.sec.gov/LATEST/search-index?q=%22{symbol}%22&dateRange=custom"
        f"&startdt=2020-01-01&forms=10-K",
        headers=_headers(),
        timeout=_TIMEOUT,
    )
    # Fallback: use company tickers JSON
    tickers_resp = requests.get(
        "https://www.sec.gov/files/company_tickers.json",
        headers=_headers(),
        timeout=_TIMEOUT,
    )
    tickers_resp.raise_for_status()
    tickers = tickers_resp.json()

    cik = None
    company_name = None
    for entry in tickers.values():
        if entry.get("ticker", "").upper() == symbol.upper():
            cik = str(entry["cik_str"]).zfill(10)
            company_name = entry.get("title", "")
            break

    if not cik:
        return {"symbol": symbol, "error": f"CIK not found for {symbol}"}

    # Fetch submissions
    subs_resp = requests.get(
        f"{_EDGAR_BASE}/submissions/CIK{cik}.json",
        headers=_headers(),
        timeout=_TIMEOUT,
    )
    subs_resp.raise_for_status()
    subs = subs_resp.json()

    recent = subs.get("filings", {}).get("recent", {})
    forms = recent.get("form", [])
    dates = recent.get("filingDate", [])
    accessions = recent.get("accessionNumber", [])

    filings = [
        {"form": forms[i], "filing_date": dates[i], "accession_number": accessions[i]}
        for i in range(min(len(forms), 20))
        if forms[i] in ("10-K", "10-Q", "20-F", "DEF 14A", "4", "8-K")
    ]

    return {
        "symbol": symbol,
        "cik": cik,
        "company_name": company_name,
        "recent_filings": filings,
    }


def fetch_insider_trading_filings(symbol: str, n_filings: int = 20) -> dict:
    """
    Return recent SEC Form 4 filings (insider buy/sell transactions).
    """
    facts = fetch_company_facts(symbol)
    if "error" in facts:
        return facts

    cik = facts["cik"]
    subs_resp = requests.get(
        f"{_EDGAR_BASE}/submissions/CIK{cik}.json",
        headers=_headers(),
        timeout=_TIMEOUT,
    )
    subs_resp.raise_for_status()
    subs = subs_resp.json()

    recent = subs.get("filings", {}).get("recent", {})
    forms = recent.get("form", [])
    dates = recent.get("filingDate", [])
    accessions = recent.get("accessionNumber", [])
    reporters = recent.get("reportingOwner", [""] * len(forms)) if "reportingOwner" in recent else [""] * len(forms)

    form4s = []
    for i in range(len(forms)):
        if forms[i] == "4":
            form4s.append(
                {
                    "filing_date": dates[i],
                    "accession_number": accessions[i],
                    "filing_url": f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={cik}&type=4",
                }
            )
            if len(form4s) >= n_filings:
                break

    return {"symbol": symbol, "cik": cik, "form4_filings": form4s}


def fetch_filing_text(symbol: str, filing_type: str = "10-K", max_chars: int = 6000) -> dict:
    """
    Fetch the most recent filing of the given type and return an excerpt of the
    plain text (risk factors section when 10-K).
    filing_type: '10-K' | '10-Q' | '20-F' | 'DEF 14A'
    """
    facts = fetch_company_facts(symbol)
    if "error" in facts:
        return facts

    cik = facts["cik"]
    # Find the most recent filing of the requested type
    target = next(
        (f for f in facts["recent_filings"] if f["form"] == filing_type), None
    )
    if not target:
        return {"symbol": symbol, "error": f"No {filing_type} found for {symbol}"}

    accession = target["accession_number"].replace("-", "")
    idx_url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accession}/{target['accession_number']}-index.htm"

    # Fetch the filing index to find the primary document
    idx_resp = requests.get(idx_url, headers={**_headers(), "Accept": "text/html"}, timeout=_TIMEOUT)
    if not idx_resp.ok:
        # Fallback: construct viewer URL
        return {
            "symbol": symbol,
            "filing_type": filing_type,
            "filing_date": target["filing_date"],
            "viewer_url": f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={cik}&type={filing_type}&dateb=&owner=include&count=5",
            "excerpt": "Document fetch failed — use viewer_url to access the filing directly.",
        }

    import re
    # Find .htm primary document link
    doc_match = re.search(r'href="(/Archives/edgar/data/[^"]+\.htm)"', idx_resp.text, re.IGNORECASE)
    if not doc_match:
        return {"symbol": symbol, "filing_type": filing_type, "error": "Could not locate primary document"}

    doc_url = "https://www.sec.gov" + doc_match.group(1)
    doc_resp = requests.get(doc_url, headers={**_headers(), "Accept": "text/html"}, timeout=_TIMEOUT)

    # Strip HTML and truncate
    from equity_mcp.tools.web import _strip_html
    text = _strip_html(doc_resp.text)

    # Try to find risk factors section for 10-K
    if filing_type == "10-K":
        risk_match = re.search(r"(?i)(item\s+1a[\.\s]*risk factor)", text)
        if risk_match:
            text = text[risk_match.start(): risk_match.start() + max_chars]

    return {
        "symbol": symbol,
        "filing_type": filing_type,
        "filing_date": target["filing_date"],
        "document_url": doc_url,
        "excerpt": text[:max_chars],
        "truncated": len(text) > max_chars,
    }


def search_regulatory_actions(symbol: str) -> dict:
    """
    Search EDGAR full-text search for SEC enforcement actions mentioning the symbol.
    """
    resp = requests.get(
        f"{_EFTS_BASE}/LATEST/search-index",
        params={
            "q": f'"{symbol}" enforcement',
            "forms": "LITIG",
            "dateRange": "custom",
            "startdt": "2018-01-01",
        },
        headers=_headers(),
        timeout=_TIMEOUT,
    )
    if not resp.ok:
        return {"symbol": symbol, "actions": [], "note": "EDGAR litigation search unavailable"}

    hits = resp.json().get("hits", {}).get("hits", [])
    actions = [
        {
            "filing_date": h["_source"].get("period_of_report", ""),
            "description": h["_source"].get("display_names", ""),
            "url": f"https://www.sec.gov{h['_source'].get('file_date', '')}",
        }
        for h in hits[:10]
    ]
    return {"symbol": symbol, "regulatory_actions": actions}
