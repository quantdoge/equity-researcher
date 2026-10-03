import json

files = [
    "data/statements_income-statement.json",
    "data/statements_balance-sheet-statement.json",
    "data/statements_cashflow-statement.json",
    "data/statements_key-metrics.json",
    "data/statements_metrics-ratios.json",
]
for f in files:
    rows = json.load(open(f))
    print("="*80)
    print(f, "rows:", len(rows))
    for r in rows:
        print("  ", r.get("symbol"), r.get("date"), "FY:", r.get("fiscalYear"), "period:", r.get("period"))
