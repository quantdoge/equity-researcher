import json, math
with open('data/cmg_cashflow.json') as f:
    cf = json.load(f)
for row in cf:
    print(f"FY{row['fiscalYear']}: SBC = {row.get('stockBasedCompensation')}")
