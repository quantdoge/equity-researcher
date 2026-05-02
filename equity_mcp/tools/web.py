"""
Web search and page fetch tools.

Uses Brave Search API when BRAVE_API_KEY is set, falls back to a basic
DuckDuckGo HTML scrape so the tool remains usable without a paid key.
"""

from __future__ import annotations

import os
import re
import textwrap

import requests

_TIMEOUT = 15
_BRAVE_SEARCH_URL = "https://api.search.brave.com/res/v1/web/search"


def web_search(query: str, n_results: int = 8) -> list[dict]:
    """
    Search the web for query and return up to n_results results.
    Each result contains: title, url, description.
    """
    api_key = os.getenv("BRAVE_API_KEY")
    if api_key:
        return _brave_search(query, n_results, api_key)
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
