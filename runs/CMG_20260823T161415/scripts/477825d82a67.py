import json

cmg = json.load(open("data/cmg_eod_full.json"))
spy = json.load(open("data/spy_eod_full.json"))
tr  = json.load(open("data/treasury_rates.json"))

print("CMG rows:", len(cmg), "| first:", cmg[-1]["date"], cmg[-1]["close"], "| last:", cmg[0]["date"], cmg[0]["close"])
print("SPY rows:", len(spy), "| first:", spy[-1]["date"], spy[-1]["close"], "| last:", spy[0]["date"], spy[0]["close"])
print("TR  rows:", len(tr),  "| first:", tr[-1]["date"], "| last:", tr[0]["date"])

# Check ordering (FMP returns newest-first per preview)
dates = [r["date"] for r in cmg]
print("CMG newest-first?", dates[0] > dates[-1])

# Split check: look at closes around June 2024 (50-for-1 split effective 2024-06-26)
around = [r for r in cmg if "2024-06-20" <= r["date"] <= "2024-07-03"]
print("\nCMG closes around the June 2024 split:")
for r in sorted(around, key=lambda x: x["date"]):
    print(f'  {r["date"]}  close={r["close"]:>10}  changePercent={r["changePercent"]}')

# Any pre-split-scale prices anywhere (close > 200)?
big = [r for r in cmg if r["close"] and r["close"] > 200]
print("\nrows with close > 200:", len(big))
if big:
    print("  range:", min(r["date"] for r in big), "to", max(r["date"] for r in big))
    print("  example:", big[len(big)//2])

# Earliest 5 rows to see scale of oldest data
print("\nCMG earliest 3 rows:", [(r["date"], r["close"]) for r in sorted(cmg, key=lambda x: x["date"])[:3]])
