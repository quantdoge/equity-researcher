import json
from collections import defaultdict

def load(p):
    with open("data/"+p) as f:
        return json.load(f)

rows_all = load("insiderTrades_latest-insider-trade.json") + load("insiderTrades_search-insider-trades.json")
rows = [r for r in rows_all if r.get("symbol") == "LTH"]
print(f"LTH rows: {len(rows)} of {len(rows_all)} (latest file is market-wide; search file is LTH-specific)")

seen = set(); uniq = []
for r in rows:
    k = (r["filingDate"], r["transactionDate"], r["reportingName"], r.get("acquisitionOrDisposition"),
         r.get("securitiesTransacted"), r.get("price"), r.get("formType"))
    if k not in seen:
        seen.add(k); uniq.append(r)
print(f"unique LTH rows: {len(uniq)}, dates {min(r['transactionDate'] for r in uniq)} .. {max(r['transactionDate'] for r in uniq)}")

# disposition blocks by (date, price)
blocks = defaultdict(list)
for r in uniq:
    if r.get("acquisitionOrDisposition") == "D":
        blocks[(r["transactionDate"], r.get("price"))].append(r)

print("\n=== LTH DISPOSITION BLOCKS ===")
tot_d_val = 0.0; tot_d_qty = 0
for (d, p), rs in sorted(blocks.items()):
    by_filer = defaultdict(int)
    for r in rs: by_filer[r["reportingName"]] += r.get("securitiesTransacted") or 0
    filer_totals = sorted(by_filer.items(), key=lambda kv: -kv[1])
    true_qty = max(t for _, t in filer_totals)
    raw_total = sum(t for _, t in filer_totals)
    tot_d_qty += true_qty; tot_d_val += true_qty*(p or 0)
    dup = "  [CO-REPORTED x%d -> counted once]" % (raw_total//true_qty) if raw_total > true_qty*1.001 else ""
    print(f"{d} @ {p:>8}: {true_qty:>9,} sh @ = ${true_qty*(p or 0)/1e6:6.1f}M  {' / '.join(f'{f}({q:,})' for f,q in filer_totals)}{dup}")

# acquisitions
tot_a_qty = 0; tot_a_val = 0.0
print("\n=== LTH ACQUISITIONS ===")
acq = defaultdict(lambda: [0,0.0])
for r in uniq:
    if r.get("acquisitionOrDisposition") == "A":
        q = r.get("securitiesTransacted") or 0; p = r.get("price") or 0
        acq[(r["transactionDate"], p)][0] += q; acq[(r["transactionDate"], p)][1] += q*p
for (d,p),(q,v) in sorted(acq.items()):
    tot_a_qty += q; tot_a_val += v
    print(f"{d} @ {p:>8}: {q:>9,} sh = ${v/1e6:5.1f}M  (likely option exercises at strike)")

print(f"\nLTH TOTALS: dispositions {tot_d_qty:,} sh = ${tot_d_val/1e6:.1f}M | acquisitions {tot_a_qty:,} sh = ${tot_a_val/1e6:.1f}M | NET = ${ (tot_d_val-tot_a_val)/1e6:.1f}M")
# Buss net: market-value sale only
print("\nNote: Buss 7/31 legs: A legs = option exercises at strikes (13.65-19.32), D @ 44.9721 for 479,240 sh = $21.6M market sale;")
print("the D legs at strike prices are the exercise-related share surrenders, not open-market sales.")
print(f"Buss net share change on 7/31: acquired 479,240, disposed at market 479,240 -> net 0 shares, cash +${479240*44.9721/1e6:.1f}M (full exercise-and-sell)")
print(f"Green LTF / Danhakl / Galashan block on 8/10: 5,119,099 sh @ 43.16 = ${5119109*43.16/1e6:.1f}M single block (3 co-filers)")
