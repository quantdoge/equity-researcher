"""
News tools for sentiment and event monitoring.

Articles come from Financial Modeling Prep, which is the only news source the
project already pays for.  FMP's news is *symbol-scoped* on the Starter plan —
there is no keyword search — so the thematic tools below pull a symbol's recent
coverage and filter it here, topping up from web search when too little of it is
on-topic.  Every FMP call degrades to web search rather than raising, so a
plan-gated endpoint or an FMP outage costs detail, not the whole analysis.

Each article carries a "source" naming its origin (the publisher for FMP rows,
"web search" for topped-up ones) so an agent can weigh a published article
differently from a search snippet.
"""

from __future__ import annotations

import re
from datetime import date, timedelta

import requests

from equity_mcp.tools.external.fmp import FMPPlanDenied, fmp_get

_WEB_SOURCE = "web search"


def fetch_news(
    query: str,
    n_days: int = 7,
    n_articles: int = 10,
    symbol: str | None = None,
) -> list[dict]:
    """
    Fetch recent news articles.

    Pass *symbol* to get that ticker's coverage from Financial Modeling Prep.
    Without one there is nothing to scope an FMP request to, so *query* is sent
    to web search instead.
    Returns list of {title, source, published_at, url, description}.
    """
    if symbol:
        articles = _fmp_stock_news(symbol, n_days, n_articles)
        if articles:
            return articles

    return _web_search_news(query, n_articles)


def fetch_news_sentiment_score(symbol: str, n_days: int = 7) -> dict:
    """
    Fetch recent news for the symbol and return a simple aggregate sentiment.
    Sentiment is computed by counting positive vs negative keywords in headlines.
    Returns: {symbol, article_count, positive_count, negative_count, sentiment_score (-1 to 1)}.
    """
    articles = fetch_news(f"{symbol} stock", n_days=n_days, n_articles=20, symbol=symbol)

    positive_words = {
        "beat", "surpassed", "raised", "upgrade", "outperform", "record", "growth",
        "strong", "positive", "gain", "rally", "bullish", "exceeded", "profit",
        "expansion", "buy", "overweight",
    }
    negative_words = {
        "miss", "lowered", "downgrade", "underperform", "loss", "decline", "weak",
        "negative", "fall", "bearish", "missed", "lawsuit", "investigation", "fraud",
        "sell", "underweight", "warning", "cut", "concern",
    }

    pos_count = 0
    neg_count = 0
    scored_articles = []

    for art in articles:
        text = (art.get("title", "") + " " + art.get("description", "")).lower()
        words = set(text.split())
        pos = len(words & positive_words)
        neg = len(words & negative_words)
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
        "article_count": len(articles),
        "positive_signals": pos_count,
        "negative_signals": neg_count,
        "sentiment_score": score,
        "overall": "positive" if score > 0.1 else ("negative" if score < -0.1 else "neutral"),
        "articles": scored_articles[:10],
    }


_GEOPOLITICAL_WORDS = {
    "geopolitical", "sanction", "sanctions", "tariff", "tariffs", "trade",
    "export", "import", "embargo", "treaty", "diplomatic", "policy",
    "regulation", "regulatory", "election", "conflict", "war", "security",
}
_ESG_WORDS = {
    "esg", "environment", "environmental", "climate", "carbon", "emissions",
    "sustainability", "social", "governance", "controversy", "scandal",
    "labor", "labour", "diversity", "boycott", "pollution", "waste", "ethics",
}
_REGULATORY_WORDS = {
    "regulator", "regulatory", "regulation", "sec", "ftc", "doj", "antitrust",
    "fine", "fined", "penalty", "lawsuit", "sue", "sued", "litigation",
    "investigation", "probe", "subpoena", "settlement", "compliance", "ruling",
}


def fetch_geopolitical_news(region: str, n_days: int = 14, n_articles: int = 10) -> list[dict]:
    """Fetch geopolitical news for a country or region."""
    # No ticker to scope an FMP request to, so the general feed stands in for a
    # keyword search: pull it, then keep what mentions the region.
    candidates = _fmp_general_news(n_days, limit=250)
    on_topic = [
        a for a in candidates
        if _mentions_region(a, region) and _matches(a, _GEOPOLITICAL_WORDS)
    ]
    return _top_up(
        on_topic,
        f"{region} geopolitical sanctions trade policy regulation",
        n_articles,
    )


def fetch_esg_controversy_news(symbol: str, n_days: int = 30, n_articles: int = 10) -> list[dict]:
    """Fetch ESG-related controversy news for the symbol."""
    return _themed_news(
        symbol,
        _ESG_WORDS,
        f"{symbol} ESG environment social governance controversy scandal",
        n_days,
        n_articles,
    )


def fetch_regulatory_news(symbol: str, n_days: int = 30) -> list[dict]:
    """Fetch regulatory and legal news for the symbol."""
    return _themed_news(
        symbol,
        _REGULATORY_WORDS,
        f"{symbol} regulatory SEC fine lawsuit investigation",
        n_days,
        n_articles=10,
    )


# ── Internal helpers ──────────────────────────────────────────────────────────


def _fmp_stock_news(symbol: str, n_days: int, limit: int) -> list[dict]:
    """A ticker's recent coverage from FMP, or [] if FMP can't serve it."""
    return _fmp_news("news/stock", n_days, limit, symbols=symbol.upper())


def _fmp_general_news(n_days: int, limit: int) -> list[dict]:
    """FMP's general news feed, or [] if FMP can't serve it."""
    return _fmp_news("news/general-latest", n_days, limit)


def _fmp_news(path: str, n_days: int, limit: int, **params) -> list[dict]:
    """
    Call an FMP news endpoint and normalise it to the tool's article shape.

    Returns [] rather than raising on any FMP failure — plan gating, an outage,
    a malformed response — because every caller has a web-search fallback and
    losing one source should cost detail, not the whole tool.
    """
    try:
        rows = fmp_get(
            path,
            **params,
            limit=limit,
            **{
                "from": (date.today() - timedelta(days=n_days)).isoformat(),
                "to": date.today().isoformat(),
            },
        )
    except (FMPPlanDenied, requests.RequestException, RuntimeError, ValueError):
        return []

    if not isinstance(rows, list):
        return []

    return [
        {
            "title":        r.get("title", ""),
            "source":       r.get("publisher") or r.get("site", ""),
            "published_at": r.get("publishedDate", ""),
            "url":          r.get("url", ""),
            "description":  r.get("text", ""),
        }
        for r in rows
        if isinstance(r, dict)
    ]


def _web_search_news(query: str, n_articles: int) -> list[dict]:
    """Web search rendered in the article shape, for when FMP has nothing."""
    from equity_mcp.tools.web import web_search

    return [
        {
            "title":        r["title"],
            "source":       _WEB_SOURCE,
            "published_at": "",
            "url":          r["url"],
            "description":  r["description"],
        }
        for r in web_search(f"{query} news", n_results=n_articles)
    ]


def _article_text(article: dict) -> str:
    return f"{article.get('title', '')} {article.get('description', '')}".lower()


def _matches(article: dict, words: set[str]) -> bool:
    """True when any of *words* appears in the article's title or description."""
    text = _article_text(article)
    return any(w in text for w in words)


def _mentions_region(article: dict, region: str) -> bool:
    """
    True when the article names *region*.

    Matched on word boundaries rather than as a substring, because the regions
    that matter most here are short: a substring test would have "US" hit
    "business" and "EU" hit "Europe" and "euro" indiscriminately.  Every token
    counts — filtering short ones out would leave "US" and "EU" with nothing to
    match on at all.
    """
    text = _article_text(article)
    tokens = [re.escape(w.lower()) for w in region.split() if w]
    return any(re.search(rf"\b{t}\b", text) for t in tokens)


def _themed_news(
    symbol: str,
    keywords: set[str],
    query: str,
    n_days: int,
    n_articles: int,
) -> list[dict]:
    """
    A symbol's FMP coverage narrowed to one theme, topped up from web search.

    FMP has no keyword search on the plans this project uses, so the theming
    happens here: pull a wide window of the ticker's articles and keep the ones
    that mention the theme.  A ticker with no on-topic coverage in the window is
    the normal case for a narrow theme, which is what the top-up is for.
    """
    candidates = _fmp_stock_news(symbol, n_days, limit=250)
    on_topic = [a for a in candidates if _matches(a, keywords)]
    return _top_up(on_topic, query, n_articles)


def _top_up(articles: list[dict], query: str, n_articles: int) -> list[dict]:
    """
    Pad *articles* out to n_articles with web-search results, skipping dupes.

    A failed search is swallowed here, unlike in fetch_news: the top-up is a
    bonus on top of articles already in hand, and a flaky search provider must
    not cost the caller the FMP rows it already has.
    """
    if len(articles) >= n_articles:
        return articles[:n_articles]

    try:
        extras = _web_search_news(query, n_articles - len(articles))
    except requests.RequestException:
        return articles

    seen = {a["url"] for a in articles}
    for extra in extras:
        if extra["url"] not in seen:
            articles.append(extra)
            seen.add(extra["url"])

    return articles[:n_articles]
