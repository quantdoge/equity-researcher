"""
Web search and page fetch tools.

Providers are tried in order of how much we trust them: Brave when
BRAVE_API_KEY is set, then SerpAPI when SERP_API_KEY is set, then a basic
DuckDuckGo HTML scrape so the tool remains nominally usable without any key.

The DuckDuckGo leg is a genuine last resort, not a supported path — DDG blocks
and rate-limits the scrape, so it returns nothing or times out as often as not.
Treat a run with neither key set as having no web search at all.
"""

from __future__ import annotations

import os
import re
import textwrap

import requests

_TIMEOUT = 60
_BRAVE_SEARCH_URL = "https://api.search.brave.com/res/v1/web/search"
_SERP_SEARCH_URL = "https://serpapi.com/search"


def web_search(query: str, n_results: int = 8) -> list[dict]:
    """
    Search the web for query and return up to n_results results.
    Each result contains: title, url, description.
    """
    brave_key = os.getenv("BRAVE_API_KEY")
    if brave_key:
        return _brave_search(query, n_results, brave_key)

    serp_key = os.getenv("SERP_API_KEY")
    if serp_key:
        return _serp_search(query, n_results, serp_key)

    return _ddg_search(query, n_results)


def fetch_page(url: str, max_chars: int = 8000) -> dict:
    """
    Fetch a web page and return its plain-text content (stripped of HTML tags).
    Returns: {url, title, content, truncated}.
    """
    headers = {"User-Agent": "equity-researcher/0.1"}
    try:
        resp = requests.get(url, headers=headers, timeout=_TIMEOUT)
        resp.raise_for_status()
    except requests.RequestException as exc:
        return {"url": url, "title": "", "content": f"Fetch error: {exc}", "truncated": False}

    text = _strip_html(resp.text)
    truncated = len(text) > max_chars
    return {
        "url": url,
        "title": _extract_title(resp.text),
        "content": text[:max_chars],
        "truncated": truncated,
    }


# ── Internal helpers ──────────────────────────────────────────────────────────


def _brave_search(query: str, n: int, api_key: str) -> list[dict]:
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "X-Subscription-Token": api_key,
    }
    params = {"q": query, "count": min(n, 20)}
    resp = requests.get(_BRAVE_SEARCH_URL, headers=headers, params=params, timeout=_TIMEOUT)
    resp.raise_for_status()
    data = resp.json()
    results = []
    for item in data.get("web", {}).get("results", [])[:n]:
        results.append(
            {
                "title": item.get("title", ""),
                "url": item.get("url", ""),
                "description": item.get("description", ""),
            }
        )
    return results


def _serp_search(query: str, n: int, api_key: str) -> list[dict]:
    params = {
        "q": query,
        "api_key": api_key,
        "engine": "google",
        "num": min(n, 20),
    }
    resp = requests.get(_SERP_SEARCH_URL, params=params, timeout=_TIMEOUT)
    resp.raise_for_status()
    data = resp.json()

    # SerpAPI reports an exhausted quota or a malformed query as HTTP 200 with
    # an "error" key and no organic_results, so raise_for_status never sees it.
    results = []
    for item in data.get("organic_results", [])[:n]:
        results.append(
            {
                "title": item.get("title", ""),
                "url": item.get("link", ""),
                "description": item.get("snippet", ""),
            }
        )
    return results


def _ddg_search(query: str, n: int) -> list[dict]:
    """Minimal DuckDuckGo HTML scrape as no-key fallback."""
    url = "https://html.duckduckgo.com/html/"
    headers = {"User-Agent": "equity-researcher/0.1"}
    try:
        resp = requests.post(url, data={"q": query}, headers=headers, timeout=_TIMEOUT)
        resp.raise_for_status()
    except requests.RequestException as exc:
        return [{"title": "Search unavailable", "url": "", "description": str(exc)}]

    results = []
    for m in re.finditer(
        r'<a class="result__a"[^>]*href="([^"]+)"[^>]*>([^<]+)</a>.*?'
        r'<a class="result__snippet"[^>]*>([^<]+)</a>',
        resp.text,
        re.DOTALL,
    ):
        results.append({"title": m.group(2).strip(), "url": m.group(1), "description": m.group(3).strip()})
        if len(results) >= n:
            break
    return results


def _strip_html(html: str) -> str:
    text = re.sub(r"<script[^>]*>.*?</script>", " ", html, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<style[^>]*>.*?</style>", " ", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"&nbsp;", " ", text)
    text = re.sub(r"&amp;", "&", text)
    text = re.sub(r"&lt;", "<", text)
    text = re.sub(r"&gt;", ">", text)
    text = re.sub(r"\s{2,}", " ", text)
    return textwrap.dedent(text).strip()


def _extract_title(html: str) -> str:
    m = re.search(r"<title[^>]*>([^<]+)</title>", html, re.IGNORECASE)
    return m.group(1).strip() if m else ""
