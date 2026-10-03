import json

def load(p):
    with open(p) as f: return json.load(f)

bs = load("data/bs_cmg.json")
print("=== CMG balance sheet detail, FY2025 & FY2024 ($M) ===")
for r in bs:
    if str(r.get("date",""))[:4] in ("2025","2024"):
        keep = {k: r.get(k) for k in [
            "date","cashAndCashEquivalents","shortTermInvestments","cashAndShortTermInvestments",
            "longTermInvestments","totalInvestments","shortTermDebt","longTermDebt",
            "capitalLeaseObligationsCurrent","capitalLeaseObligationsNonCurrent","capitalLeaseObligations",
            "totalCurrentLiabilities","totalLiabilities","totalStockholdersEquity","totalEquity",
            "totalAssets","totalDebt","netDebt"]}
        print(json.dumps(keep, indent=1))

bs5 = load("data/statements_balance-sheet-statement.json")
r24 = [r for r in bs5 if str(r.get("date",""))[:4]=="2024"][0]
print("\nFY2024 (5-row file) equity/totalDebt/cash:",
      round(r24["totalStockholdersEquity"]/1e6,1), round(r24["totalDebt"]/1e6,1),
      round(r24["cashAndShortTermInvestments"]/1e6,1), "leases:",
      round((r24.get("capitalLeaseObligationsCurrent") or 0)/1e6,1),
      round((r24.get("capitalLeaseObligationsNonCurrent") or 0)/1e6,1))

print("\n=== as-reported income statement, FY2025 row: all keys ===")
ar = load("data/cmg_as_reported_income.json")
row25 = [r for r in ar if str(r.get("date",""))[:4]=="2025"][0]
for k,v in row25["data"].items():
    if v is not None:
        print(f"  {k}: {v:,.0f}" if isinstance(v,(int,float)) else f"  {k}: {v}")

print("\n=== as-reported income statement, FY2024 row (for comparison) ===")
row24 = [r for r in ar if str(r.get("date",""))[:4]=="2024"][0]
for k in ["revenues","revenuesfromcontractwithcustomerexcludingassessedtaxe","foodandbeveragerevenue","deliveryservicerevenue"]:
    if k in row24["data"]:
        print(f"  {k}: {row24['data'][k]:,.0f}")
