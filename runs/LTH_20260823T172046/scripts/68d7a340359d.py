import json

def load(p):
    with open(p) as f:
        return json.load(f)

km = load("data/lth_key_metrics_annual.json")
print("=== KEY METRICS (selected) ===")
for r in sorted(km, key=lambda x: x["date"]):
    print(f"{r['date']}  EV/EBITDA={r['evToEBITDA']}  ND/EBITDA={r['netDebtToEBITDA']}  ROIC={r['returnOnInvestedCapital']}  FCFyield={r['freeCashFlowYield']}  incomeQuality={r['incomeQuality']}")

print()
gr = load("data/statements_financial-statement-growth.json")
print("=== GROWTH (selected) ===")
for r in sorted(gr, key=lambda x: x["date"]):
    print(f"{r['date']}  rev={r['revenueGrowth']}  ebitda={r.get('ebitdaGrowth')}  ni={r['netIncomeGrowth']}  ocf={r.get('operatingCashFlowGrowth')}  fcf={r.get('freeCashFlowGrowth')}")

print()
scr = load("data/search_search-company-screener.json")
print("=== SCREENER (41 rows) — what universe is this? ===")
for r in scr[:41]:
    print(f"{r['symbol']:6s} {str(r['companyName'])[:34]:34s} mcap={str(r['marketCap']):>12s} ind={r['industry']} px={r['price']}")
