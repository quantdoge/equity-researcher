"""
Web search and page fetch tools.

Search runs on SerpApi (https://serpapi.com), keyed by SERP_API_KEY. There is no
fallback provider: without the key web_search returns a single tagged marker
result rather than an empty list, so an unconfigured run is visible instead of
looking like the web simply had nothing to say.
"""

from __future__ import annotations

import logging
import os
import re
import textwrap

import requests

_TIMEOUT = 15
_SERPAPI_URL = "https://serpapi.com/search"

_log = logging.getLogger(__name__)
_missing_key_warned = False


def web_search(query: str, n_results: int = 8) -> list[dict]:
    """
    Search the web for query and return up to n_results results.
    Each result contains: title, url, description (plus source and date when
    the engine reports them).

    Never raises. A failure comes back as one result carrying a "kind" of
    not_configured, unavailable, or search_error; an empty list means the
    search genuinely returned no hits.
    """
    api_key = os.getenv("SERP_API_KEY")
    if not api_key:
        global _missing_key_warned
        if not _missing_key_warned:
            _missing_key_warned = True
            _log.warning("SERP_API_KEY is not set; web_search cannot return results")
        return [_failure("SERP_API_KEY is not set", "not_configured")]
    return _serpapi_search(query, n_results, api_key)


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


def _failure(message: str, kind: str) -> dict:
    return {"title": "Search unavailable", "url": "", "description": message, "kind": kind}


def _serpapi_search(query: str, n: int, api_key: str) -> list[dict]:
    params = {"engine": "google", "q": query, "num": n, "api_key": api_key}
    try:
        resp = requests.get(_SERPAPI_URL, params=params, timeout=_TIMEOUT)
        data = resp.json()
    except requests.RequestException as exc:
        _log.error("SerpApi request for %r failed: %s", query, exc)
        return [_failure(str(exc), "unavailable")]
    except ValueError as exc:  # non-JSON body
        _log.error("SerpApi returned a non-JSON response for %r: %s", query, exc)
        return [_failure(f"SerpApi returned a non-JSON response: {exc}", "unavailable")]

    # SerpApi reports bad keys and exhausted quotas in the body, not the status
    # code. Pass its wording through so the agent can read what went wrong.
    if error := data.get("error"):
        _log.error("SerpApi error for %r: %s", query, error)
        return [_failure(str(error), "search_error")]

    results = []
    for item in (data.get("organic_results") or [])[:n]:
        result = {
            "title": item.get("title", ""),
            "url": item.get("link", ""),
            "description": item.get("snippet", ""),
        }
        for extra in ("source", "date"):
            if item.get(extra):
                result[extra] = item[extra]
        results.append(result)
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
