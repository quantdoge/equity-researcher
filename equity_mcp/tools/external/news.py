"""
News tools for sentiment and event monitoring.

Sourced from Financial Modeling Prep's stable News API — the same ``FMP_API_KEY``
that feeds the Supabase pipeline and backs every ``db.py`` tool. FMP headlines
arrive pre-tagged with the ticker they concern, which NewsAPI cannot do.

See https://site.financialmodelingprep.com/developer/docs/stable/general-news

Providers are tried in order, mirroring the degrade-never-crash contract in
``db.py``:

    FMP  →  NewsAPI.org (if NEWS_API_KEY)  →  web search

The ``/stable/news/*`` endpoints are gated behind a paid FMP tier and answer 402
on a plan that lacks them. That is a fallback trigger, not an error — the chain
simply moves to the next provider and logs which one served the call.

Two shape mismatches drive the routing below. FMP filters by ticker and has no
free-text keyword search, so a query that isn't a symbol goes to the general feed
and is filtered client-side; and a region (``fetch_geopolitical_news``) has no FMP
representation at all, so it realistically lands on web search.
"""

from __future__ import annotations

import logging
import os
import re
from datetime import date, timedelta
from typing import Any, Iterable, Sequence

import requests

_log = logging.getLogger(__name__)

_FMP_BASE = "https://financialmodelingprep.com/stable"
_NEWSAPI_BASE = "https://newsapi.org/v2"
_TIMEOUT = 15

# FMP rejects a larger page than this on the news endpoints.
_FMP_MAX_LIMIT = 250

# A bare ticker: 1–5 letters, optionally exchange- or class-suffixed (BRK.B, 7203.T).
_TICKER_RE = re.compile(r"^[A-Z]{1,5}(?:[.\-][A-Z0-9]{1,4})?$")

# Query words too generic to filter a headline feed on.
_STOPWORDS = frozenset({
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "in", "is",
    "it", "its", "of", "on", "or", "s", "that", "the", "to", "was", "with",
    "news", "stock", "stocks", "shares", "company", "inc", "corp",
})

# Topical filters for the ESG and regulatory tools. FMP returns a symbol's whole
# feed, so the topic has to be applied here rather than in the query.
_ESG_TERMS = frozenset({
    "esg", "environment", "environmental", "emissions", "carbon", "climate",
    "sustainability", "sustainable", "pollution", "waste", "renewable",
    "social", "diversity", "labor", "labour", "workers", "union", "safety",
    "governance", "board", "executive", "compensation", "shareholder",
    "controversy", "scandal", "boycott", "protest", "activist",
})
_REGULATORY_TERMS = frozenset({
    "regulator", "regulators", "regulatory", "regulation", "sec", "ftc", "doj",
    "fda", "antitrust", "compliance", "probe", "investigation", "investigating",
    "lawsuit", "sued", "suit", "litigation", "settlement", "settle", "fine",
    "fined", "penalty", "penalties", "subpoena", "injunction", "court",
    "ruling", "violation", "sanction", "sanctions", "recall", "consent",
})

_POSITIVE_WORDS = frozenset({
    "beat", "surpassed", "raised", "upgrade", "outperform", "record", "growth",
    "strong", "positive", "gain", "rally", "bullish", "exceeded", "profit",
    "expansion", "buy", "overweight",
})
_NEGATIVE_WORDS = frozenset({
    "miss", "lowered", "downgrade", "underperform", "loss", "decline", "weak",
    "negative", "fall", "bearish", "missed", "lawsuit", "investigation", "fraud",
    "sell", "underweight", "warning", "cut", "concern",
})


class FmpNewsUnavailable(RuntimeError):
    """FMP has no key, refused the plan, or returned an error envelope."""


# ── Public tools ──────────────────────────────────────────────────────────────


def fetch_news(
    query: str,
    n_days: int = 7,
    n_articles: int = 10,
    language: str = "en",
    symbols: str | list[str] | None = None,
) -> list[dict]:
    """
    Fetch recent news articles matching query.

    Pass ``symbols`` (a ticker, or a list/comma-separated string of them) to pull
    FMP's per-company feed; otherwise a query that looks like a bare ticker is
    treated as one, and anything else searches the general feed by keyword.

    Returns list of {title, source, published_at, url, description, symbol}.
    """
    return _fetch(query, n_days, n_articles, language, symbols)


def fetch_news_sentiment_score(symbol: str, n_days: int = 7) -> dict:
    """
    Fetch recent news for the symbol and return a simple aggregate sentiment.
    Sentiment is computed by counting positive vs negative keywords in headlines.
    Returns: {symbol, article_count, positive_count, negative_count, sentiment_score (-1 to 1)}.
    """
    articles, source = _fetch_with_source(
        f"{symbol} stock", n_days=n_days, n_articles=20, symbols=symbol
    )

    pos_count = 0
    neg_count = 0
    scored_articles = []

    for art in articles:
        words = set(_searchable(art).split())
        pos = len(words & _POSITIVE_WORDS)
        neg = len(words & _NEGATIVE_WORDS)
        sentiment = "positive" if pos > neg else ("negative" if neg > pos else "neutral")
        pos_count += pos
        neg_count += neg
        scored_articles.append({
            "title": art["title"],
            "published_at": art["published_at"],
            "url": art["url"],
            "sentiment": sentiment,
        })

    total = pos_count + neg_count
    score = round((pos_count - neg_count) / total, 3) if total > 0 else 0.0

    return {
        "symbol": symbol,
        "n_days": n_days,
        "source": source,
        "article_count": len(articles),
        "positive_signals": pos_count,
        "negative_signals": neg_count,
        "sentiment_score": score,
        "overall": "positive" if score > 0.1 else ("negative" if score < -0.1 else "neutral"),
        "articles": scored_articles[:10],
    }


def fetch_geopolitical_news(region: str, n_days: int = 14, n_articles: int = 10) -> list[dict]:
    """
    Fetch geopolitical news for a country or region.

    A region is not a ticker, so FMP can only offer its general feed filtered by
    keyword — this usually settles on the web search fallback.
    """
    return _fetch(
        f"{region} geopolitical sanctions trade policy regulation",
        n_days=n_days,
        n_articles=n_articles,
    )


def fetch_esg_controversy_news(symbol: str, n_days: int = 30, n_articles: int = 10) -> list[dict]:
    """Fetch ESG-related controversy news for the symbol."""
    return _fetch(
        f"{symbol} ESG environment social governance controversy scandal",
        n_days=n_days,
        n_articles=n_articles,
        symbols=symbol,
        topic=_ESG_TERMS,
    )


def fetch_regulatory_news(symbol: str, n_days: int = 30) -> list[dict]:
    """Fetch regulatory and legal news for the symbol."""
    return _fetch(
        f"{symbol} regulatory SEC fine lawsuit investigation",
        n_days=n_days,
        n_articles=10,
        symbols=symbol,
        topic=_REGULATORY_TERMS,
    )


# ── Provider chain ────────────────────────────────────────────────────────────


def _fetch(
    query: str,
    n_days: int,
    n_articles: int,
    language: str = "en",
    symbols: str | list[str] | None = None,
    topic: Iterable[str] | None = None,
) -> list[dict]:
    return _fetch_with_source(query, n_days, n_articles, language, symbols, topic)[0]


def _fetch_with_source(
    query: str,
    n_days: int,
    n_articles: int,
    language: str = "en",
    symbols: str | list[str] | None = None,
    topic: Iterable[str] | None = None,
) -> tuple[list[dict], str]:
    """
    Run the FMP → NewsAPI → web search chain, returning the articles and the name
    of the provider that served them. A provider that raises or comes back empty
    hands off to the next one; only the final fallback's result stands.
    """
    topic = frozenset(topic) if topic is not None else None

    try:
        articles = _fmp_search(query, n_days, n_articles, symbols, topic)
        if articles:
            return articles[:n_articles], "fmp"
        _log.info("FMP news returned nothing for %r — falling back", query)
    except FmpNewsUnavailable as exc:
        _log.info("FMP news unavailable (%s) — falling back", exc)
    except requests.RequestException as exc:
        _log.warning("FMP news request failed (%s) — falling back", exc)

    api_key = os.environ.get("NEWS_API_KEY", "")
    if api_key:
        try:
            articles = _newsapi_search(query, n_days, n_articles, language, api_key)
            if articles:
                return articles[:n_articles], "newsapi"
            _log.info("NewsAPI returned nothing for %r — falling back to web search", query)
        except requests.RequestException as exc:
            _log.warning("NewsAPI request failed (%s) — falling back to web search", exc)

    from equity_mcp.tools.web import web_search

    results = web_search(f"{query} news", n_results=n_articles)
    return [
        {
            "title": r["title"],
            "source": "",
            "published_at": "",
            "url": r["url"],
            "description": r["description"],
            "symbol": None,
        }
        for r in results
    ], "web_search"


# ── FMP client ────────────────────────────────────────────────────────────────


def _fmp_get(path: str, **params: Any) -> list[dict]:
    """
    GET one FMP stable endpoint and return its rows.

    Raises FmpNewsUnavailable for the conditions the chain treats as "try the next
    provider": no key, a plan gate (401/402/403), or an error envelope in place of
    the expected list.
    """
    key = os.environ.get("FMP_API_KEY", "")
    if not key:
        raise FmpNewsUnavailable("FMP_API_KEY not set")

    query = {k: v for k, v in params.items() if v is not None}
    resp = requests.get(
        f"{_FMP_BASE}/{path}", params={**query, "apikey": key}, timeout=_TIMEOUT
    )
    if resp.status_code in (401, 402, 403):
        # 402 is FMP's "Restricted Endpoint" — the news feeds need a paid tier.
        raise FmpNewsUnavailable(f"{path}: HTTP {resp.status_code} {resp.text[:120]}")
    resp.raise_for_status()

    try:
        payload = resp.json()
    except ValueError as exc:
        raise FmpNewsUnavailable(f"{path}: non-JSON payload {resp.text[:120]}") from exc

    if isinstance(payload, dict):
        for field in ("Error Message", "error"):
            if field in payload:
                raise FmpNewsUnavailable(f"{path}: {payload[field]}")
        return [payload]
    if isinstance(payload, list):
        return [r for r in payload if isinstance(r, dict)]
    raise FmpNewsUnavailable(f"{path}: unexpected payload {type(payload).__name__}")


def _fmp_search(
    query: str,
    n_days: int,
    n_articles: int,
    symbols: str | list[str] | None,
    topic: frozenset[str] | None,
) -> list[dict]:
    """
    Route to FMP's per-symbol feed when we have tickers, else its general feed.

    The symbol feed is already scoped to the company, so it is narrowed only when
    the caller named a topic (ESG, regulatory). The general feed has no keyword
    search at all, so there the query itself has to serve as the filter.
    """
    tickers = _as_symbols(symbols) or _as_symbols(query)
    window = {
        "from": (date.today() - timedelta(days=n_days)).isoformat(),
        "to": date.today().isoformat(),
        "page": 0,
        "limit": min(n_articles, _FMP_MAX_LIMIT),
    }

    if tickers:
        rows = _fmp_get("news/stock", symbols=",".join(tickers), **window)
        return _keyword_filter(_normalize_fmp(rows), topic)

    articles = _normalize_fmp(_fmp_get("news/general-latest", **window))
    return _keyword_filter(articles, topic or _query_terms(query))


def _normalize_fmp(rows: Sequence[dict]) -> list[dict]:
    """Reshape FMP news rows into this module's article shape."""
    return [
        {
            "title": _pick(r, "title", "newsTitle") or "",
            "source": _pick(r, "publisher", "newsPublisher", "site", "newsBaseURL") or "",
            "published_at": _pick(r, "publishedDate", "date") or "",
            "url": _pick(r, "url", "newsURL", "link") or "",
            "description": _pick(r, "text", "content", "snippet") or "",
            "symbol": _pick(r, "symbol", "tickers"),
        }
        for r in rows
    ]


def _pick(row: dict, *keys: str) -> Any:
    """Return the first non-null value among keys — FMP renames fields between plans."""
    for key in keys:
        value = row.get(key)
        if value is not None:
            return value
    return None


# ── Filtering helpers ─────────────────────────────────────────────────────────


def _as_symbols(value: str | list[str] | None) -> list[str]:
    """
    Read tickers out of a symbols argument or a query that is itself a ticker.

    A multi-word query is prose, not a symbol list, so it yields nothing and the
    caller falls through to the general feed.
    """
    if not value:
        return []
    parts = value if isinstance(value, list) else re.split(r"[,\s]+", value)
    tickers = [p.strip().upper() for p in parts if p and p.strip()]
    return tickers if tickers and all(_TICKER_RE.match(t) for t in tickers) else []


def _query_terms(query: str) -> frozenset[str]:
    """Meaningful lowercase words from a free-text query, for feed filtering."""
    words = {w for w in re.findall(r"[a-zA-Z]{2,}", query.lower())}
    return frozenset(words - _STOPWORDS)


def _keyword_filter(articles: Sequence[dict], terms: frozenset[str] | None) -> list[dict]:
    """
    Keep articles mentioning at least one term. No terms means no filtering.

    An empty result is left empty rather than falling back to the unfiltered feed:
    the chain reads that as "this provider had nothing" and moves on to one that
    can actually search text.
    """
    if not terms:
        return list(articles)
    return [a for a in articles if terms & set(re.findall(r"[a-z]{2,}", _searchable(a)))]


def _searchable(article: dict) -> str:
    return f"{article.get('title', '')} {article.get('description', '')}".lower()


# ── NewsAPI fallback ──────────────────────────────────────────────────────────


def _newsapi_search(
    query: str, n_days: int, n_articles: int, language: str, api_key: str
) -> list[dict]:
    from_date = (date.today() - timedelta(days=n_days)).isoformat()
    resp = requests.get(
        f"{_NEWSAPI_BASE}/everything",
        params={
            "q": query,
            "from": from_date,
            "sortBy": "relevancy",
            "language": language,
            "pageSize": min(n_articles, 100),
            "apiKey": api_key,
        },
        timeout=_TIMEOUT,
    )
    resp.raise_for_status()
    articles = resp.json().get("articles", [])
    return [
        {
            "title": a["title"],
            "source": a["source"]["name"],
            "published_at": a["publishedAt"],
            "url": a["url"],
            "description": a.get("description", ""),
            "symbol": None,
        }
        for a in articles
    ]
