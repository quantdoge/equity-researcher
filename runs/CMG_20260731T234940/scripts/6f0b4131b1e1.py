import json, math
with open('data/cmg_cashflow.json') as f:
    cf = sorted(json.load(f), key=lambda x: x['fiscalYear'])
for row in cf[-6:]:
    fy = row['fiscalYear']
    capex = abs(float(row['capitalExpenditure'])) if row['capitalExpenditure'] else 0
    print(f"FY{fy}: Capex = {capex:,.0f}")
