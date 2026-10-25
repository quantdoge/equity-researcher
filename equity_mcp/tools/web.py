"""
Web search and page fetch tools.

Providers are tried cheapest first, and each keyed provider falls through to
the next when it fails: Serper.dev (SERPER_DEV_API_KEY), then SerpAPI
(SERP_API_KEY), then Brave (BRAVE_API_KEY). "Fails" means it raised or
returned no results. Providers without a key are skipped.

With no key set at all, a basic DuckDuckGo HTML scrape keeps the tool
nominally usable. That leg is a genuine last resort, not a supported path —
DDG blocks and rate-limits the scrape, so it returns nothing or times out as
often as not. Treat a run with no key set as having no web search at all.
"""

from __future__ import annotations

import logging
import os
import re
import textwrap

import requests

log = logging.getLogger(__name__)

_TIMEOUT = 60
_SERPER_SEARCH_URL = "https://google.serper.dev/search"
_SERP_SEARCH_URL = "https://serpapi.com/search"
_BRAVE_SEARCH_URL = "https://api.search.brave.com/res/v1/web/search"


def web_search(query: str, n_results: int = 8) -> list[dict]:
    """
    Search the web for query and return up to n_results results.
    Each result contains: title, url, description.
    """
    providers = [
        ("serper", "SERPER_DEV_API_KEY", _serper_search),
        ("serpapi", "SERP_API_KEY", _serp_search),
        ("brave", "BRAVE_API_KEY", _brave_search),
    ]
    keyed = [(name, fn, key) for name, var, fn in providers if (key := os.getenv(var))]
    if not keyed:
        return _ddg_search(query, n_results)

    # An empty result falls through too: one extra query on the rare search
    # the cheap provider can't answer beats handing an agent "no results".
    errors = []
    for name, fn, key in keyed:
        try:
            results = fn(query, n_results, key)
        except Exception as exc:
            errors.append(f"{name}: {exc}")
            log.warning("web_search: %s failed (%s), trying next provider", name, exc)
            continue
        if results:
            return results
        log.warning("web_search: %s returned no results, trying next provider", name)

    if errors:
        raise RuntimeError("all web search providers failed: " + "; ".join(errors))
    return []


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


def _serper_search(query: str, n: int, api_key: str) -> list[dict]:
    headers = {"X-API-KEY": api_key, "Content-Type": "application/json"}
    payload = {"q": query, "num": min(n, 20), "gl": "us", "hl": "en"}
    # An exhausted credit balance or a bad key comes back as a 4xx, so
    # raise_for_status is enough to hand off to the next provider.
    resp = requests.post(_SERPER_SEARCH_URL, headers=headers, json=payload, timeout=_TIMEOUT)
    resp.raise_for_status()
    data = resp.json()
    results = []
    for item in data.get("organic", [])[:n]:
        results.append(
            {
                "title": item.get("title", ""),
                "url": item.get("link", ""),
                "description": item.get("snippet", ""),
            }
        )
    return results


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
    # Raise it here so the caller records why, rather than seeing "no results".
    if data.get("error"):
        raise RuntimeError(f"SerpAPI error: {data['error']}")
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
