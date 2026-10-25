"""
Guards web_search's provider fallback: Serper.dev → SerpAPI → Brave.

Serper is first because it is cheapest, so a regression that silently skipped
it would only show up on the bill. And a provider that fails without falling
through hands the agent nothing, so assert both directions.

Runs under pytest, or standalone:  python tests/test_web_search.py
No network: requests.get / requests.post are replaced with fakes.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from equity_mcp.tools import web  # noqa: E402

_KEYS = ("SERPER_DEV_API_KEY", "SERP_API_KEY", "BRAVE_API_KEY")

SERPER_OK = {"organic": [{"title": "Serper hit", "link": "https://a.example", "snippet": "from serper"}]}
SERPAPI_OK = {"organic_results": [{"title": "SerpAPI hit", "link": "https://b.example", "snippet": "from serpapi"}]}


class _Resp:
    def __init__(self, status: int, body: dict):
        self.status_code = status
        self._body = body

    def raise_for_status(self) -> None:
        if self.status_code >= 400:
            raise requests.HTTPError(f"{self.status_code} Client Error", response=self)

    def json(self) -> dict:
        return self._body


def _run(env: dict[str, str], post: _Resp | None = None, get: _Resp | None = None):
    """Call web_search with only *env*'s keys set; return (result-or-exc, calls)."""
    calls: list[str] = []

    def fake_post(url, **kw):
        calls.append(url)
        assert post is not None, f"unexpected POST {url}"
        return post

    def fake_get(url, **kw):
        calls.append(url)
        assert get is not None, f"unexpected GET {url}"
        return get

    saved_env = {k: os.environ.pop(k, None) for k in _KEYS}
    saved = (web.requests.post, web.requests.get)
    os.environ.update(env)
    web.requests.post, web.requests.get = fake_post, fake_get
    try:
        try:
            out = web.web_search("apple earnings", n_results=5)
        except Exception as exc:
            out = exc
    finally:
        web.requests.post, web.requests.get = saved
        for k in _KEYS:
            os.environ.pop(k, None)
            if saved_env[k] is not None:
                os.environ[k] = saved_env[k]
    return out, calls


BOTH = {"SERPER_DEV_API_KEY": "s", "SERP_API_KEY": "p"}


def test_serper_success_skips_serpapi() -> None:
    out, calls = _run(BOTH, post=_Resp(200, SERPER_OK))
    assert calls == [web._SERPER_SEARCH_URL], calls
    assert out == [{"title": "Serper hit", "url": "https://a.example", "description": "from serper"}], out


def test_serper_http_error_falls_back() -> None:
    out, calls = _run(BOTH, post=_Resp(400, {"message": "Not enough credits"}), get=_Resp(200, SERPAPI_OK))
    assert calls == [web._SERPER_SEARCH_URL, web._SERP_SEARCH_URL], calls
    assert out[0]["title"] == "SerpAPI hit", out


def test_serper_empty_falls_back() -> None:
    out, calls = _run(BOTH, post=_Resp(200, {"organic": []}), get=_Resp(200, SERPAPI_OK))
    assert calls == [web._SERPER_SEARCH_URL, web._SERP_SEARCH_URL], calls
    assert out[0]["url"] == "https://b.example", out


def test_no_serper_key_goes_straight_to_serpapi() -> None:
    out, calls = _run({"SERP_API_KEY": "p"}, get=_Resp(200, SERPAPI_OK))
    assert calls == [web._SERP_SEARCH_URL], calls
    assert out[0]["title"] == "SerpAPI hit", out


def test_all_fail_raises_with_every_reason() -> None:
    out, _ = _run(BOTH, post=_Resp(403, {}), get=_Resp(200, {"error": "Your account has run out of searches."}))
    assert isinstance(out, RuntimeError), out
    msg = str(out)
    assert "serper:" in msg and "serpapi:" in msg and "run out of searches" in msg, msg


def test_all_empty_returns_empty_list() -> None:
    out, calls = _run(BOTH, post=_Resp(200, {"organic": []}), get=_Resp(200, {"organic_results": []}))
    assert out == [], out
    assert len(calls) == 2, calls


if __name__ == "__main__":
    failures = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"  PASS  {name}")
            except AssertionError as exc:
                failures += 1
                print(f"  FAIL  {name}: {exc}")
    print("\nall passed" if not failures else f"\n{failures} failure(s)")
    sys.exit(1 if failures else 0)
