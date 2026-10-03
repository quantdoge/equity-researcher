import json
from datetime import datetime

def load(p):
    with open(p) as f:
        return json.load(f)

px = load("data/chart_historical-price-eod-light.json")
print("=== PRICE HISTORY ===")
print("rows:", len(px), "first:", px[0]["date"], px[0]["price"], " last:", px[-1]["date"], px[-1]["price"])
# quick stats
prices = [(r["date"], r["price"]) for r in px]
print("min:", min(prices, key=lambda x: x[1]), " max:", max(prices, key=lambda x: x[1]))
# 52-week range
last_date = prices[-1][0]
recent = [p for d,p in prices if d >= "2025-08-01"]
print("since 2025-08-01: n=%d min=%.2f max=%.2f last=%.2f" % (len(recent), min(recent), max(recent), recent[-1]))

print()
ins = load("data/insiderTrades_search-insider-trades.json")
print("=== INSIDER TRADES (search, 15 rows) ===")
for r in sorted(ins, key=lambda x: x.get("transactionDate") or ""):
    print(f"{r.get('transactionDate')}  {r.get('reportingName')[:28]:28s} {r.get('acquisitionOrDisposition'):1s} px={r.get('price')}  qty={r.get('securitiesTransacted')}  owned_after={r.get('securitiesOwned')}  type={r.get('typeOfOwner')} form={r.get('formType')}")

print()
tr = load("data/economics_treasury-rates.json")
print("=== TREASURY RATES ===")
print("rows:", len(tr), "first:", tr[0]["date"], "last:", tr[-1]["date"])
last = tr[-1]
print("latest:", {k: last[k] for k in ["date","month1","month3","month6","year1","year2","year3","year5","year7","year10","year20","year30"]})
