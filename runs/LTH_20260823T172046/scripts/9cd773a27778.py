import json
from collections import defaultdict

def load(p):
    with open("data/"+p) as f:
        return json.load(f)

# ---------- 9. Insider transactions: dedupe co-reported blocks ----------
rows = load("insiderTrades_latest-insider-trade.json") + load("insiderTrades_search-insider-trades.json")
# dedupe exact duplicates across the two files
seen = set(); uniq = []
for r in rows:
    k = (r["symbol"], r["filingDate"], r["transactionDate"], r["reportingName"], r["transactionType"],
         r.get("acquisitionOrDisposition"), r.get("securitiesTransacted"), r.get("price"), r.get("formType"))
    if k not in seen:
        seen.add(k); uniq.append(r)
print(f"raw rows: {len(rows)}, unique: {len(uniq)}")
print(f"date range: {min(r['transactionDate'] for r in uniq)} .. {max(r['transactionDate'] for r in uniq)}")

# group dispositions by (transactionDate, price) to spot co-reported blocks
blocks = defaultdict(list)
for r in uniq:
    if r.get("acquisitionOrDisposition") == "D":
        blocks[(r["transactionDate"], r.get("price"))].append(r)

print("\n=== DISPOSITION BLOCKS (date, price) ===")
block_true = {}
for (d, p), rs in sorted(blocks.items()):
    by_filer = defaultdict(int)
    for r in rs: by_filer[r["reportingName"]] += r.get("securitiesTransacted") or 0
    # co-reported block: same day+price, filers reporting identical/partitioned totals
    filer_totals = sorted(by_filer.items(), key=lambda kv: -kv[1])
    true_qty = max(t for _, t in filer_totals)  # largest single-filer total at that date+price
    raw_total = sum(t for _, t in filer_totals)
    block_true[(d, p)] = {"true_qty": true_qty, "raw_total": raw_total, "filers": dict(by_filer)}
    flag = "  <-- CO-REPORTED (deduped)" if raw_total > true_qty*1.001 else ""
    print(f"{d} @ {p}: raw={raw_total:>10,} true={true_qty:>10,} value=${true_qty*p/1e6:7.1f}M{flag}")
    for f, q in filer_totals:
        print(f"    {f[:40]:40s} {q:>10,}")

# acquisitions
print("\n=== ACQUISITIONS (date, price) ===")
acq = defaultdict(lambda: [0, 0.0])
for r in uniq:
    if r.get("acquisitionOrDisposition") == "A":
        q = r.get("securitiesTransacted") or 0; p = r.get("price") or 0
        acq[(r["transactionDate"], p)][0] += q
        acq[(r["transactionDate"], p)][1] += q*p
for (d, p), (q, v) in sorted(acq.items()):
    print(f"{d} @ {p}: qty={q:>10,} value=${v/1e6:6.1f}M")

tot_d_val = sum(b["true_qty"]*p for (d, p), b in block_true.items())
tot_d_qty = sum(b["true_qty"] for b in block_true.values())
tot_a_val = sum(v for q, v in acq.values()); tot_a_qty = sum(q for q, v in acq.values())
print(f"\nTOTAL (deduped): dispositions {tot_d_qty:,} sh = ${tot_d_val/1e6:.1f}M | acquisitions {tot_a_qty:,} sh = ${tot_a_val/1e6:.1f}M | NET SELLING ${ (tot_d_val-tot_a_val)/1e6:.1f}M")
