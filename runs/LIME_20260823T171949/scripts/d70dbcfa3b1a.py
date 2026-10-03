import json

files = ["lime_eod", "spy_eod", "lyft_eod", "uber_eod", "brds_eod", "lime_quote",
         "lime_income_q", "lime_balance_q", "lime_cashflow_q"]

for f in files:
    try:
        d = json.load(open(f"data/{f}.json"))
    except Exception as e:
        print(f, "ERROR", e); continue
    if isinstance(d, dict):
        d = [d]
    print("="*70)
    print(f, "| rows:", len(d))
    if d and "status" in d[0]:
        print("  ->", d[0].get("status"), "|", d[0].get("message", "")[:120])
        continue
    if f == "lime_quote":
        print(json.dumps(d[0], indent=2))
        continue
    # EOD files: sorted newest-first in FMP; find chronological first/last
    dates = [r["date"] for r in d]
    print("  newest:", max(dates), "| oldest:", min(dates), "| unique dates:", len(set(dates)))
    # null check across numeric fields
    nulls = {}
    for r in d:
        for k, v in r.items():
            if v is None:
                nulls[k] = nulls.get(k, 0) + 1
    print("  null counts:", nulls if nulls else "none")
    # chronological first and last rows
    rows = sorted(d, key=lambda r: r["date"])
    print("  FIRST row:", {k: rows[0][k] for k in ("date","open","high","low","close","volume")})
    print("  LAST  row:", {k: rows[-1][k] for k in ("date","open","high","low","close","volume")})
    closes = [r["close"] for r in rows]
    print("  close min/max: %.2f / %.2f" % (min(closes), max(closes)))
