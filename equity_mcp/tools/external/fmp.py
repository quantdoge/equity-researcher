"""
Financial Modeling Prep REST client.

A thin shared wrapper, not a full SDK — callers pass the endpoint path and its
query parameters and get back the decoded JSON.  It lives here rather than
inside news.py because db.py needs the same client: every tool in db.py now
sources its data from FMP rather than from the (not yet provisioned) Supabase
schema.

Plan gating is the thing worth centralising.  FMP sells its endpoints in tiers,
and a key on a lower tier gets HTTP 402 on anything above it — an outcome that
is permanent for the life of the subscription and must never be retried or
debugged as an auth fault.  fmp_get raises FMPPlanDenied so callers can tell it
apart from an outage and degrade deliberately.

Caching is the other thing worth centralising, and db.py is why.  The 13 agents
run concurrently and their tool sets overlap heavily — seven of them can ask for
the same symbol's income statement in a single run — while two calculation tools
fan out over peers and would otherwise issue a hundred requests apiece.  Use
fmp_cached for anything an agent can trigger; reserve bare fmp_get for
one-shot calls whose parameters carry a timestamp anyway (the news feeds).
"""

from __future__ import annotations

import copy
import os
import threading
import time
from collections import OrderedDict
from typing import Any

import requests

_BASE = "https://financialmodelingprep.com/stable"

# Longer than the 15s the other external modules use.  FMP's news feeds are
# slow and highly variable — a 250-row request measured 5s once and 32s the
# next time — and a timeout here is indistinguishable from an empty result to
# the caller, so a tight ceiling silently drops real data.  The tool layer caps
# the whole call at 90s (langchain_bridge._TOOL_TIMEOUT_S) regardless.
_TIMEOUT = 45

# How long a cached payload stays fresh.  Annual fundamentals do not move
# intraday and a run lasts about half an hour, so a quarter-hour is generous for
# correctness and still collapses the overlap between concurrent agents.
_DEFAULT_TTL = 900.0

# Cache ceiling.  A multi-symbol universe scan touches hundreds of distinct
# (path, params) pairs, and without a bound the cache would grow for the life of
# the process.  Oldest-inserted entries go first.
_CACHE_MAX = 512

# Transient faults worth one more go.  Deliberately excludes 402 (a plan
# ceiling, permanent) and every other 4xx (a bad request stays bad).
_RETRY_STATUS = {429, 500, 502, 503, 504}

# A connection refused or reset fails fast, so retrying it is nearly free.  A
# read timeout has already spent _TIMEOUT seconds, and the tool layer caps the
# whole call at 90s (langchain_bridge._TOOL_TIMEOUT_S) — so it gets one retry,
# not two, and the budget stays inside that ceiling.
_FAST_FAIL_ATTEMPTS = 3
_TIMEOUT_ATTEMPTS = 2
_BACKOFF = 1.0


class FMPPlanDenied(RuntimeError):
    """The endpoint exists but the current FMP subscription does not reach it."""


# ── Connection reuse ──────────────────────────────────────────────────────────

# One Session per thread rather than one shared Session.  langchain_bridge
# dispatches tools across a 48-thread pool, and requests.Session is not
# documented as thread-safe; a thread-local keeps the connection pooling without
# sharing mutable state across those threads.
_local = threading.local()


def _session() -> requests.Session:
    session = getattr(_local, "session", None)
    if session is None:
        session = requests.Session()
        _local.session = session
    return session


# ── Response cache ────────────────────────────────────────────────────────────

_cache: "OrderedDict[tuple, tuple[float, Any]]" = OrderedDict()
_cache_lock = threading.Lock()


def _cache_key(path: str, params: dict) -> tuple:
    # str() the values so 8 and "8" — which FMP treats identically in a query
    # string — do not occupy two entries.
    items = tuple(sorted((k, str(v)) for k, v in params.items() if v is not None))
    return (path.strip("/"), items)


def fmp_get(path: str, **params: Any) -> list | dict:
    """
    GET an FMP endpoint and return its decoded JSON.

    *path* is relative to the /stable base, e.g. "news/stock".  Parameters with
    a value of None are dropped, so optional arguments can be passed through
    unconditionally.

    Raises:
        RuntimeError:   FMP_API_KEY is not set.
        FMPPlanDenied:  the subscription does not cover this endpoint (HTTP 402).
        requests.HTTPError / requests.RequestException: anything else.
    """
    api_key = os.getenv("FMP_API_KEY")
    if not api_key:
        raise RuntimeError(
            "FMP_API_KEY is not set — add it to .env to use Financial Modeling Prep data."
        )

    query = {k: v for k, v in params.items() if v is not None}
    query["apikey"] = api_key

    url = f"{_BASE}/{path.lstrip('/')}"
    timeouts_left = _TIMEOUT_ATTEMPTS
    fast_fails_left = _FAST_FAIL_ATTEMPTS
    attempt = 0

    while True:
        attempt += 1
        try:
            resp = _session().get(url, params=query, timeout=_TIMEOUT)
        except requests.Timeout:
            timeouts_left -= 1
            if timeouts_left <= 0:
                raise
            time.sleep(_BACKOFF)
            continue
        except requests.ConnectionError:
            fast_fails_left -= 1
            if fast_fails_left <= 0:
                raise
            time.sleep(_BACKOFF * attempt)
            continue

        if resp.status_code == 402:
            raise FMPPlanDenied(
                f"FMP endpoint '{path}' is not available on the current "
                "subscription plan."
            )

        if resp.status_code in _RETRY_STATUS:
            fast_fails_left -= 1
            if fast_fails_left > 0:
                time.sleep(_BACKOFF * attempt)
                continue

        resp.raise_for_status()
        return resp.json()


def fmp_cached(path: str, *, ttl: float = _DEFAULT_TTL, **params: Any) -> list | dict:
    """
    GET an FMP endpoint through a process-wide TTL cache.

    Same contract as fmp_get, including the exceptions: a failure is never
    cached, so a transient outage does not poison the entry for *ttl* seconds.
    An empty result *is* cached — a symbol FMP has no data for would otherwise be
    re-requested by every agent that asks.

    The returned object is a deep copy, so callers may treat it as their own.
    """
    key = _cache_key(path, params)
    now = time.monotonic()

    with _cache_lock:
        entry = _cache.get(key)
        if entry is not None:
            stored_at, payload = entry
            if now - stored_at < ttl:
                return copy.deepcopy(payload)
            del _cache[key]  # expired

    payload = fmp_get(path, **params)

    with _cache_lock:
        _cache[key] = (time.monotonic(), payload)
        while len(_cache) > _CACHE_MAX:
            _cache.popitem(last=False)

    return copy.deepcopy(payload)


def cache_clear() -> None:
    """Drop every cached payload. For tests and long-lived processes."""
    with _cache_lock:
        _cache.clear()
