"""
News API tools for sentiment and event monitoring.
Uses NewsAPI.org (freemium). Falls back to web search when key is absent.
"""

from __future__ import annotations

import os
from datetime import date, timedelta

import requests

_NEWSAPI_BASE = "https://newsapi.org/v2"
_TIMEOUT = 15


def fetch_news(
    query: str,
    n_days: int = 7,
    n_articles: int = 10,
    language: str = "en",
) -> list[dict]:
    """
    Fetch recent news articles matching query.
    Returns list of {title, source, published_at, url, description}.
    """
    api_key = os.environ.get("NEWS_API_KEY", "")
    if api_key:
        return _newsapi_search(query, n_days, n_articles, language, api_key)
    # Fallback: web search
    from equity_mcp.tools.web import web_search
    results = web_search(f"{query} news", n_results=n_articles)
    return [
        {"title": r["title"], "source": "", "published_at": "", "url": r["url"], "description": r["description"]}
        for r in results
    ]


def fetch_news_sentiment_score(symbol: str, n_days: int = 7) -> dict:
    """
    Fetch recent news for the symbol and return a simple aggregate sentiment.
    Sentiment is computed by counting positive vs negative keywords in headlines.
    Returns: {symbol, article_count, positive_count, negative_count, sentiment_score (-1 to 1)}.
    """
    articles = fetch_news(f"{symbol} stock", n_days=n_days, n_articles=20)

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


def fetch_geopolitical_news(region: str, n_days: int = 14, n_articles: int = 10) -> list[dict]:
    """Fetch geopolitical news for a country or region."""
    return fetch_news(
        f"{region} geopolitical sanctions trade policy regulation",
        n_days=n_days,
        n_articles=n_articles,
    )


def fetch_esg_controversy_news(symbol: str, n_days: int = 30, n_articles: int = 10) -> list[dict]:
    """Fetch ESG-related controversy news for the symbol."""
    return fetch_news(
        f"{symbol} ESG environment social governance controversy scandal",
        n_days=n_days,
        n_articles=n_articles,
    )


def fetch_regulatory_news(symbol: str, n_days: int = 30) -> list[dict]:
    """Fetch regulatory and legal news for the symbol."""
    return fetch_news(
        f"{symbol} regulatory SEC fine lawsuit investigation",
        n_days=n_days,
        n_articles=10,
    )


# ── Internal helpers ──────────────────────────────────────────────────────────


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
        }
        for a in articles
    ]
