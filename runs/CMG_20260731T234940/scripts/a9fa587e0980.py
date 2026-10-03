import json
with open('data/cmg_cashflow.json') as f:
    cf = sorted(json.load(f), key=lambda x: x['fiscalYear'])
for row in cf[5:7]:
    print(f"\nFY{row['fiscalYear']}:")
    for k in ['netIncome','netCashProvidedByOperatingActivities','capitalExpenditure','freeCashFlow','stockBasedCompensation','commonStockRepurchased']:
        v = row.get(k)
        print(f"  {k}: {v}")
