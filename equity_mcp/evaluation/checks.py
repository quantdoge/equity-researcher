"""
Deterministic checks: everything the model is bad at, done in code.

Jev reads dates as text and counts badly, and its own docs say so. Whether a
section exists, whether an enum parses, how many bullets a list has and whether
a price target's percentage matches its prices are therefore decided here. Jev
gets only the semantic judgments.

Every check returns ``{"passed": bool | None, "value": float | None, "detail": str}``.
``passed is None`` means "could not be evaluated", such as a price target given
only as a narrative. Aggregation treats that as skipped, not failed: an
unparseable band is a fact about the report's format, not evidence it is wrong.
"""

from __future__ import annotations

import re

from equity_mcp.evaluation.extract import run_extract, section_text
from equity_mcp.evaluation.schema import DeterministicCheck, DomainMetric, Extract, Section

ROLE_KEYWORDS: dict[str, tuple[str, ...]] = {
    "sector_researcher": ("sector",),
    "geo_legal_researcher": ("geo", "legal"),
    "macro_researcher": ("macro",),
    "value_researcher": ("value",),
    "growth_researcher": ("growth",),
    "fin_risk_analyst": ("financial risk", "fin risk", "fin-risk", "fin_risk"),
    "nonfin_risk_analyst": ("non-financial", "non financial", "nonfin", "non-fin"),
    "quant_analyst": ("quant",),
    "short_analyst": ("short",),
    "esg_analyst": ("esg",),
    "alt_data_analyst": ("alt data", "alt-data", "alternative data", "alt_data"),
}
_FAILURE_WORDS = re.compile(
    r"unavailable|failed|failure|time[sd]?[\s-]?out|missing|no report|not available|did not (?:return|complete|report)|"
    r"gap|error|absent|could not",
    re.IGNORECASE,
)
_BULLET = re.compile(r"^\s*(?:[-*•]|\d+[.)])\s+\S")
_NUM = r"(\d[\d,]*(?:\.\d+)?)"
SIZE_BANDS: dict[str, tuple[float, float]] = {
    "high": (3.0, 5.0),
    "medium": (1.0, 3.0),
    "low": (0.0, 1.0),
    "split": (0.0, 1.0),
}


def _result(passed: bool | None, value: float | None, detail: str = "") -> dict:
    return {"passed": passed, "value": value, "detail": detail}


def run_extracts(record: dict, extracts: dict[str, Extract], sections: dict[str, Section]) -> dict[str, dict]:
    return {eid: run_extract(ex, section_text(record, ex.section, sections)) for eid, ex in extracts.items()}


# ── Table parsing ─────────────────────────────────────────────────────────────


def _tables(text: str) -> list[list[list[str]]]:
    """Every markdown table in ``text`` as rows of cells, header first, separator dropped."""
    tables, cur = [], []
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("|"):
            if "-" in s and set(s) <= set("|:- "):  # the |---|:--| separator row
                continue
            cur.append([c.strip() for c in s.strip("|").split("|")])
        elif cur:
            tables.append(cur)
            cur = []
    if cur:
        tables.append(cur)
    return tables


def _table_check(chk: DeterministicCheck, text: str) -> dict:
    best = None
    for table in _tables(text):
        header, rows = table[0], table[1:]
        missing_cols = [c for c in chk.columns or [] if not any(c.lower() in h.lower() for h in header)]
        first_cells = [r[0].lower() for r in rows if r]
        missing_rows = [lbl for lbl in chk.row_labels or [] if not any(lbl.lower() in fc for fc in first_cells)]
        ok = len(rows) >= (chk.min_rows or 0) and not missing_cols and not missing_rows
        detail = f"{len(rows)} rows"
        if missing_cols:
            detail += f"; missing columns {missing_cols}"
        if missing_rows:
            detail += f"; missing rows {missing_rows}"
        if ok:
            return _result(True, 1.0, detail)
        best = best or _result(False, 0.0, detail)
    return best or _result(False, 0.0, "no table found")


# ── Price target arithmetic ───────────────────────────────────────────────────


def _num(s: str) -> float:
    return float(s.replace(",", ""))


def price_target_consistency(text: str) -> dict:
    """
    Check a "Price Target: $X–Y (−A% to −B% from current $Z)" line.

    Bands are common, and analysts list the percentages in either order. So
    each stated percentage only has to match the implied move of *some* target
    in the band, within 1.5 percentage points. When there is no reference price
    or no percentage the check is skipped, not failed.
    """
    norm = text.replace("−", "-").replace("–", "-").replace("—", "-").replace("**", "")
    m = re.search(r"\(([^()]*%[^()]*)\)", norm)
    if not m:
        return _result(None, None, "no percentage in parentheses")
    inside = m.group(1)
    ref = re.search(r"(?:from|vs\.?|current|price)\s*(?:current\s*)?(?:price\s*)?(?:of\s*)?\$\s?" + _NUM, inside, re.I)
    if not ref:
        ref = re.search(r"current(?:\s+price)?\s*(?:of\s*)?\$\s?" + _NUM, norm, re.I)
    if not ref:
        return _result(None, None, "no reference price")
    reference = _num(ref.group(1))
    before = norm[: m.start()].splitlines()[-1] if norm[: m.start()].strip() else ""
    targets: list[float] = []
    for tm in re.finditer(r"\$\s?" + _NUM + r"(?:\s*-\s*\$?\s?" + _NUM + ")?", before):
        targets.append(_num(tm.group(1)))
        if tm.group(2):  # a band: either end, or its midpoint, may be what the % refers to
            targets.append(_num(tm.group(2)))
            targets.append((_num(tm.group(1)) + _num(tm.group(2))) / 2)
    pcts = [float(p) for p in re.findall(r"([+-]?\d+(?:\.\d+)?)\s*%", inside)]
    if not targets or not pcts or reference <= 0:
        return _result(None, None, "could not parse targets or percentages")
    implied = [(t / reference - 1) * 100 for t in targets]
    bad = []
    for p in pcts:
        # an unsigned percentage may be either direction ("15% upside")
        candidates = [p] if p < 0 or "+" in inside else [p, -p]
        if not any(abs(c - i) <= 1.5 for c in candidates for i in implied):
            bad.append(p)
    detail = f"targets={targets} ref={reference} stated={pcts} implied={[round(i, 1) for i in implied]}"
    return _result(not bad, 0.0 if bad else 1.0, detail)


# ── Dispatcher ────────────────────────────────────────────────────────────────


def run_check(
    chk: DeterministicCheck,
    record: dict,
    sections: dict[str, Section],
    extracts: dict[str, dict],
    ctx: dict,
) -> dict:
    """Run one check. ``ctx`` carries cross-agent facts: failed_roles, short_earnings_quality."""
    sec = section_text(record, chk.section, sections) if chk.section else None
    text = sec["text"] if sec else ""

    if chk.kind == "not_degenerate":
        return _result(record["status"] == "ok", 1.0 if record["status"] == "ok" else 0.0, record["status"])

    if chk.kind == "sections_present":
        wanted = chk.sections or []
        missing = [s for s in wanted if section_text(record, s, sections) is None]
        frac = (len(wanted) - len(missing)) / len(wanted) if wanted else 1.0
        return _result(not missing, frac, f"missing {missing}" if missing else "all present")

    if chk.kind == "extract_ok":
        ex = extracts.get(chk.extract or "", {})
        ok = ex.get("value") is not None
        return _result(ok, 1.0 if ok else 0.0, f"{chk.extract}={ex.get('value')!r}" + (" (hedged)" if ex.get("hedged") else ""))

    if sec is None and chk.kind not in {"fraud_override"}:
        return _result(False, 0.0, f"section '{chk.section}' not found")

    if chk.kind == "table_present":
        return _table_check(chk, text)

    if chk.kind == "min_matches":
        n = len(re.findall(chk.pattern, text, re.IGNORECASE))
        return _result(n >= chk.min, min(1.0, n / chk.min) if chk.min else 1.0, f"{n} matches")

    if chk.kind == "min_list_items":
        n = sum(1 for line in text.splitlines()[1:] if _BULLET.match(line))
        if n == 0:  # numbered items written as table rows count too
            n = sum(len(t) - 1 for t in _tables(text))
        ok = n >= chk.min and (chk.max is None or n <= chk.max)
        return _result(ok, min(1.0, n / chk.min) if chk.min else 1.0, f"{n} items")

    if chk.kind == "regex_absent":
        m = re.search(chk.pattern, text, re.IGNORECASE)
        return _result(m is None, 0.0 if m else 1.0, f"found {m.group(0)!r}" if m else "absent")

    if chk.kind == "price_target_consistent":
        return price_target_consistency(text)

    if chk.kind == "fraud_override":
        action = extracts.get(chk.extract or "", {}).get("value")
        eq = ctx.get("short_earnings_quality")
        violated = eq == "Fraudulent Risk" and action in {"Initiate", "Add"}
        return _result(not violated, 0.0 if violated else 1.0, f"short earnings quality={eq!r}, action={action!r}")

    if chk.kind == "failures_acknowledged":
        failed = [r for r in ctx.get("failed_roles", []) if r in ROLE_KEYWORDS]
        if not failed:
            return _result(True, 1.0, "no failed specialists")
        lines = [ln.lower() for ln in text.splitlines()]
        missing = [
            r for r in failed
            if not any(any(k in ln for k in ROLE_KEYWORDS[r]) and _FAILURE_WORDS.search(ln) for ln in lines)
        ]
        frac = (len(failed) - len(missing)) / len(failed)
        return _result(not missing, frac, f"unacknowledged {missing}" if missing else f"all {len(failed)} acknowledged")

    if chk.kind == "position_size_band":
        norm = text.replace("–", "-").replace("—", "-")
        pm = re.search(r"(\d+(?:\.\d+)?)\s*%", norm)
        passed_on = re.search(r"\bpass\b|no (?:new )?position|0\s*%", norm, re.IGNORECASE)
        if pm is None:
            return _result(True if passed_on else None, 1.0 if passed_on else None, "no size stated" + (" (pass)" if passed_on else ""))
        size = float(pm.group(1))
        level = extracts.get(chk.extract or "", {}).get("value") if chk.extract else None
        lo, hi = SIZE_BANDS.get(str(level).lower(), (0.0, 5.0))
        ok = lo - 0.01 <= size <= hi + 0.01
        return _result(ok, 1.0 if ok else 0.0, f"size {size}% vs band {lo}-{hi}% for {level!r}")

    return _result(None, None, f"unknown check kind {chk.kind}")


# ── Domain-metric coverage gate ───────────────────────────────────────────────

_NOT_APPLICABLE = re.compile(
    r"not (?:meaningful|applicable|relevant|available|disclosed|reported)|n/?a\b|n\.m\.|"
    r"does(?:n't| not) apply|unavailable|no data",
    re.IGNORECASE,
)


def _substantive_mention(term: str, text: str) -> bool:
    """True if ``term`` appears at least once *not* beside an N/A phrase.

    A bank report that writes "Rule of 40: not meaningful for a lender" names
    the metric only to dismiss it. Counting that as evidence would force Jev to
    pick a level for something the report deliberately declined to assess.
    """
    for m in re.finditer(r"(?<![a-z])" + re.escape(term), text):
        window = text[max(0, m.start() - 60): m.end() + 80]
        if not _NOT_APPLICABLE.search(window):
            return True
    return False


def domain_coverage(metric: DomainMetric, record: dict, sections: dict[str, Section]) -> dict:
    """
    Decide whether a domain metric is worth asking about, without asking.

    Score has no abstain option, so a metric the report never discusses would
    still get a confident-looking level. Code checks for evidence terms first.
    With none present, the metric is ``not_addressed`` and costs nothing.
    """
    first = None
    for sid in metric.section:  # the first listed section that carries evidence wins
        sec = section_text(record, sid, sections)
        if not (sec and sec["text"].strip()):
            continue
        low = sec["text"].lower()
        found = [t for t in metric.evidence_terms if _substantive_mention(t.lower(), low)]
        if found:
            return {"addressed": True, "section": sid, "text": sec["text"], "terms_found": found}
        first = first or sid
    return {"addressed": False, "section": first, "text": "", "terms_found": []}
