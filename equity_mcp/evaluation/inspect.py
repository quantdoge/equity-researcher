"""
Offline rubric debugger: how one role's rubric reads every real output.

    python -m equity_mcp.evaluation.inspect value_researcher
    python -m equity_mcp.evaluation.inspect quant --verbose
    python -m equity_mcp.evaluation.inspect esg --files outputs/AVGO_*.json

No network and no API key needed. For each section, extract, deterministic
check and domain metric it prints how often it resolves across the outputs.
That is how a heading regex that matches nothing, or an evidence-term list too
narrow to fire, is found before any Jev call is paid for. ``--verbose`` adds
the per-file values.
"""

from __future__ import annotations

import argparse
import glob
import sys
from collections import Counter, defaultdict
from pathlib import Path

from equity_mcp.evaluation.checks import domain_coverage, run_check, run_extracts
from equity_mcp.evaluation.extract import load_run, section_text
from equity_mcp.evaluation.loader import REPO_ROOT, RubricError, load_rubric
from equity_mcp.orchestrator import _resolve_roles
from equity_mcp.roles import ALL_ROLES


def _pct(n: int, d: int) -> str:
    return f"{n:>3}/{d:<3} {100 * n / d:5.1f}%" if d else "  -"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("role")
    parser.add_argument("--files", nargs="*", help="output JSON files or globs (default: outputs/*.json)")
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args(argv)

    role = _resolve_roles([args.role], ALL_ROLES)[0]
    try:
        loaded = load_rubric(role)
    except RubricError as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 1
    rb = loaded.rubric
    drift = loaded.prompt_drift()
    if drift:
        print(f"WARNING: {drift}\n")

    patterns = args.files or [str(REPO_ROOT / "outputs" / "*.json")]
    files = sorted({Path(p) for pat in patterns for p in glob.glob(pat)})

    statuses: Counter = Counter()
    sec_hits: Counter = Counter()
    ext_hits: Counter = Counter()
    ext_hedged: Counter = Counter()
    ext_values: dict[str, Counter] = defaultdict(Counter)
    chk_pass: Counter = Counter()
    chk_skip: Counter = Counter()
    dom_hits: Counter = Counter()
    dom_sections: dict[str, Counter] = defaultdict(Counter)
    n_ok = 0

    for path in files:
        run, records = load_run(path)
        if run["schema_kind"] != "agent_results_v1":
            statuses["legacy file"] += 1
            continue
        rec = records.get(role)
        if rec is None:
            statuses["not in run"] += 1
            continue
        statuses[rec["status"]] += 1
        if rec["status"] != "ok":
            if args.verbose:
                print(f"{path.name}: {rec['status']} {rec['error'] or ''}")
            continue
        n_ok += 1
        for sid in rb.sections:
            if section_text(rec, sid, rb.sections) is not None:
                sec_hits[sid] += 1
        extracts = run_extracts(rec, rb.extract, rb.sections)
        for eid, ex in extracts.items():
            if ex["value"] is not None:
                ext_hits[eid] += 1
                ext_values[eid][str(ex["value"])] += 1
            if ex["hedged"]:
                ext_hedged[eid] += 1
        ctx = {"failed_roles": run["failures"], "short_earnings_quality": None}
        results = {}
        for chk in loaded.alignment.deterministic_checks:
            r = run_check(chk, rec, rb.sections, extracts, ctx)
            results[chk.id] = r
            if r["passed"] is None:
                chk_skip[chk.id] += 1
            elif r["passed"]:
                chk_pass[chk.id] += 1
        cov = {}
        for mid, m in rb.conviction.domain_metrics.items():
            c = domain_coverage(m, rec, rb.sections)
            cov[mid] = c
            if c["addressed"]:
                dom_hits[mid] += 1
            dom_sections[mid][str(c["section"])] += 1

        if args.verbose:
            print(f"\n── {path.name}  ({len(rec['full'])} chars, preamble {len(rec['preamble'])})")
            print("   headings:", " | ".join(h[:50] for h in rec["report"].heading_names))
            for eid, ex in extracts.items():
                print(f"   extract {eid:<22} {ex['value']!r}{'  (hedged)' if ex['hedged'] else ''}")
            for cid, r in results.items():
                print(f"   check   {cid:<22} {r['passed']}  {r['detail'][:90]}")
            for mid, c in cov.items():
                print(f"   domain  {mid:<22} {'yes' if c['addressed'] else 'NO ':<4} [{c['section']}] {c['terms_found'][:4]}")

    print(f"\n{role}: {len(files)} files, statuses {dict(statuses)}\n")
    print("SECTIONS (found in ok reports)")
    for sid in rb.sections:
        print(f"  {sid:<28} {_pct(sec_hits[sid], n_ok)}")
    print("EXTRACTS (parsed)")
    for eid in rb.extract:
        top = ", ".join(f"{v}:{c}" for v, c in ext_values[eid].most_common(6))
        print(f"  {eid:<28} {_pct(ext_hits[eid], n_ok)}  hedged {ext_hedged[eid]:>2}   [{top}]")
    print("DETERMINISTIC CHECKS (passed; skipped)")
    for chk in loaded.alignment.deterministic_checks:
        print(f"  {chk.id:<28} {_pct(chk_pass[chk.id], n_ok)}  skipped {chk_skip[chk.id]}")
    print("DOMAIN METRICS (addressed → sent to Jev)")
    for mid in rb.conviction.domain_metrics:
        secs = ", ".join(f"{s}:{c}" for s, c in dom_sections[mid].most_common())
        print(f"  {mid:<28} {_pct(dom_hits[mid], n_ok)}  sections [{secs}]")
    n_requests = len(loaded.alignment.requests)
    print(f"\nRequests per ok report: 1 conviction + ≤{-(-len(rb.conviction.domain_metrics) // 6)}–"
          f"{len(rb.conviction.domain_metrics)} domain + {n_requests} alignment")
    return 0


if __name__ == "__main__":
    sys.exit(main())
