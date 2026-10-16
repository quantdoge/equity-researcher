"""
Turn an outputs/*.json result into one record per agent, and reports into sections.

Three facts about the output files shape this module:

- ``agent_results`` holds only the 11 specialists. The portfolio strategist and
  head of research exist only as the ``portfolio_brief`` and ``investment_memo``
  strings, and their failure shows only in ``failures``. So each record is
  built from whichever of the three sources applies.
- "Success" does not mean output. A run that hits LangGraph's recursion limit
  returns ``"Sorry, need more steps to process this request."`` with
  ``error: None``. That is classed ``degenerate`` here and never sent to Jev,
  so the model is never paid to grade a placeholder.
- Specialists write ``## N. Title — **Enum**`` markdown headings. The memo
  writes ``**Verdict**: …`` bold-line pseudo-headings. The section splitter
  accepts both, but bold lines count only in documents without real headings,
  because inside a markdown report they are emphasis (``**Weaknesses:**``),
  not structure.

Files are classified by their keys, never their names: ``AMD_20260822T152843``
has a current-style name and the old master-agent schema.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

from equity_mcp.evaluation.schema import Extract, Section

PASS2_ROLES = ("portfolio_strategist", "head_of_research")

_MD_HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
_BOLD_HEADING = re.compile(r"^\*\*([^*\n]{2,100})\*\*")
_STUB = re.compile(
    r"sorry, need more steps|i (?:was|am) unable to (?:complete|finish)|i apologi[sz]e|"
    r"ran out of (?:steps|time|budget)",
    re.IGNORECASE,
)
_FULL_CAP = 12000


def role_label(role: str) -> str:
    """``fin_risk_analyst`` → ``Fin Risk Analyst``, the form reports and memos use."""
    return role.replace("_", " ").title()


# ── Sections ──────────────────────────────────────────────────────────────────


def _plain(heading: str) -> str:
    return heading.replace("**", "").replace("__", "").strip()


class Report:
    """A report split into headed sections."""

    def __init__(self, text: str) -> None:
        self.text = text
        self.lines = text.splitlines()
        md = []
        for i, line in enumerate(self.lines):
            m = _MD_HEADING.match(line.strip())
            if m:
                md.append((i, len(m.group(1)), m.group(2)))
        if sum(1 for _, lvl, _ in md if lvl >= 2) >= 3:
            heads = md
        else:
            bold = [
                (i, 4, line.strip())
                for i, line in enumerate(self.lines)
                if _BOLD_HEADING.match(line.strip()) and not _MD_HEADING.match(line.strip())
            ]
            heads = sorted(md + bold)
        # The document title is the first heading when it sits above most later headings.
        self._title_idx = None
        if len(heads) > 1:
            base = Counter(lvl for _, lvl, _ in heads[1:]).most_common(1)[0][0]
            if heads[0][1] < base:
                self._title_idx = 0
            # A stray "# **HOLD**" inside a "## 5. Verdict" section is emphasis, not a new
            # top-level section. Demote it to a child so the verdict section keeps its body.
            heads = [heads[0]] + [(i, base + 1 if lvl == 1 < base else lvl, h) for i, lvl, h in heads[1:]]
        self.headings: list[tuple[int, int, str]] = heads

    @property
    def heading_names(self) -> list[str]:
        return [_plain(h) for _, _, h in self.headings]

    def _span(self, k: int) -> tuple[int, int]:
        start, level, _ = self.headings[k]
        end = len(self.lines)
        for j in range(k + 1, len(self.headings)):
            if self.headings[j][1] <= level:
                end = self.headings[j][0]
                break
        return start, end

    def find(self, section: Section) -> dict | None:
        """``{"heading", "body", "text"}`` for the matching section, or None."""
        pattern = re.compile(section.heading, re.IGNORECASE)
        hits = []
        for k, (_, _, head) in enumerate(self.headings):
            if k == self._title_idx:
                continue
            if pattern.search(_plain(head)):
                hits.append(k)
                if not section.all_matches:
                    break
        if not hits:
            return None
        parts = []
        heading_line = self.lines[self.headings[hits[0]][0]]
        for k in hits:
            start, end = self._span(k)
            parts.append("\n".join(self.lines[start:end]).strip())
        text = "\n\n".join(parts)[: section.max_chars]
        body = "\n".join(text.splitlines()[1:])
        return {"heading": heading_line.strip(), "body": body, "text": text}


def split_preamble(text: str) -> tuple[str, str]:
    """``(preamble, report)``: the chatter before the first heading, if it is short."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        s = line.strip()
        if _MD_HEADING.match(s) or (i > 0 and _BOLD_HEADING.match(s)):
            if i == 0:
                return "", text
            pre = "\n".join(ln for ln in lines[:i] if ln.strip() not in {"---", "***"}).strip()
            if len(pre) <= 1500:
                return pre, "\n".join(lines[i:]).strip()
            return "", text
    return "", text


def is_degenerate(report: str) -> bool:
    body = report.strip()
    if len(body) < 400:
        return True
    if _STUB.search(body[:300]) and len(body) < 2000:
        return True
    if not Report(body).headings and len(body) < 1500:
        return True
    return False


# ── Extraction ────────────────────────────────────────────────────────────────


def _norm(s: str) -> str:
    """Case and separator insensitive: "In-Line", "in line" and "IN  LINE" compare equal."""
    return re.sub(r"[\s\-/]+", " ", s.lower()).strip()


def _enum_regex(ex: Extract) -> tuple[re.Pattern, dict[str, str]]:
    canon = {_norm(v): v for v in ex.values or []}
    canon.update({_norm(a): v for a, v in ex.aliases.items()})
    alts = sorted(canon, key=len, reverse=True)  # longest first: "strong buy" before "buy"
    body = "|".join(r"[\s\-/]+".join(re.escape(tok) for tok in a.split(" ")) for a in alts)
    return re.compile(rf"(?<![A-Za-z])({body})(?![A-Za-z])", re.IGNORECASE), canon


def _scan_enum(text: str, ex: Extract) -> tuple[str | None, bool]:
    rx, canon = _enum_regex(ex)
    found: list[str] = []
    for m in rx.finditer(text):
        value = canon.get(_norm(m.group(1)))
        if value and value not in found:
            found.append(value)
    if not found:
        return None, False
    return found[0], len(found) > 1


def run_extract(ex: Extract, section: dict | None) -> dict:
    """``{"value", "hedged", "found", "snippet"}``. ``value`` is None when nothing parses."""
    out = {"value": None, "hedged": False, "found": section is not None, "snippet": None}
    if section is None:
        return out
    heading, body = section["heading"], section["body"]
    if ex.anchor:
        m = re.search(ex.anchor, section["text"], re.IGNORECASE)
        if not m:
            return out
        regions = [section["text"][m.start(): m.start() + max(ex.body_chars, 80)]]
    else:
        bold = " ".join(re.findall(r"\*\*([^*]+)\*\*", heading))
        regions = [r for r in (bold, heading, body[: ex.body_chars]) if r]

    for region in regions:
        if ex.values is not None:
            value, hedged = _scan_enum(region, ex)
            if value is not None:
                out.update(value=value, hedged=hedged, snippet=region[:160])
                return out
        else:
            m = re.search(ex.pattern, region, re.IGNORECASE)
            if m:
                raw = m.group(1).replace(",", "")
                try:
                    num: float | int = int(raw) if ex.type == "int" else float(raw)
                except ValueError:
                    continue
                if ex.range and not ex.range[0] <= num <= ex.range[1]:
                    out["snippet"] = f"out of range: {raw}"
                    return out
                out.update(value=num, snippet=region[:160])
                return out
    return out


# ── Records ───────────────────────────────────────────────────────────────────


def classify(result: Any) -> str:
    if isinstance(result, dict) and isinstance(result.get("agent_results"), list):
        return "agent_results_v1"
    return "legacy"


def _agent_record(role: str, text: str | None, error: str | None, elapsed: float | None, failed: bool) -> dict:
    raw = text or ""
    preamble, report = split_preamble(raw)
    if failed or error or not raw.strip():
        status = "failed"
    elif is_degenerate(report):
        status = "degenerate"
    else:
        status = "ok"
    return {
        "role": role,
        "status": status,
        "error": error,
        "elapsed_seconds": elapsed,
        "raw": raw,
        "preamble": preamble,
        "full": report,
        "report": Report(report) if status == "ok" else None,
        "output_sha256": hashlib.sha256(raw.encode("utf-8")).hexdigest() if raw else None,
    }


def load_run(path: Path) -> tuple[dict, dict[str, dict]]:
    """``(run, records)`` for one output file. ``records`` is empty for legacy files."""
    data_bytes = path.read_bytes()
    result = json.loads(data_bytes.decode("utf-8"))
    run = run_from_result(result, path)
    run["source_sha256"] = hashlib.sha256(data_bytes).hexdigest()
    return run, records_from_result(result) if run["schema_kind"] == "agent_results_v1" else {}


def run_from_result(result: dict, path: Path | None) -> dict:
    kind = classify(result)
    stem = path.stem if path else None
    run_id = result.get("run_id") or stem
    symbol = result.get("symbol") or (stem.split("_")[0] if stem else None)
    run_date = result.get("date")
    if not run_date and run_id:
        m = re.search(r"_(\d{4})(\d{2})(\d{2})T", run_id)
        run_date = f"{m.group(1)}-{m.group(2)}-{m.group(3)}" if m else None
    return {
        "run_id": run_id,
        "symbol": symbol,
        "run_date": run_date,
        "source_path": str(path).replace("\\", "/") if path else None,
        "source_sha256": None,
        "schema_kind": kind,
        "skipped_synthesis": bool(result.get("skipped_synthesis", False)),
        "failures": list(result.get("failures") or []),
        "elapsed_seconds": result.get("elapsed_seconds"),
        "agent_models": result.get("models"),
        "skip_reason": None if kind == "agent_results_v1" else "legacy schema: no agent_results",
    }


def records_from_result(result: dict) -> dict[str, dict]:
    failures = set(result.get("failures") or [])
    timings = result.get("per_agent_timings") or {}
    records: dict[str, dict] = {}
    for item in result.get("agent_results") or []:
        role = item.get("agent_role")
        if not role:
            continue
        records[role] = _agent_record(
            role, item.get("output"), item.get("error"), item.get("elapsed_seconds"), role in failures
        )
    if not result.get("skipped_synthesis"):
        for role, key in (("portfolio_strategist", "portfolio_brief"), ("head_of_research", "investment_memo")):
            text = result.get(key)
            if text is None and role not in failures:
                continue
            records[role] = _agent_record(role, text, None, timings.get(role), role in failures)
    return records


def section_text(record: dict, sid: str, sections: dict[str, Section]) -> dict | None:
    """Resolve a section id, built-ins included, against a record."""
    if sid == "full":
        t = record["full"][:_FULL_CAP]
        return {"heading": "", "body": t, "text": t}
    if sid == "raw":
        t = record["raw"][:_FULL_CAP]
        return {"heading": "", "body": t, "text": t}
    if sid == "preamble":
        t = record["preamble"]
        return {"heading": "", "body": t, "text": t} if t else None
    report: Report | None = record.get("report")
    if report is None:
        return None
    return report.find(sections[sid])
