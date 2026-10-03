import json
with open('data/cmg_balance_sheet.json') as f:
    bal = sorted(json.load(f), key=lambda x: x['fiscalYear'])
for row in bal[-3:]:
    print(f"\nFY{row['fiscalYear']}:")
    for k, v in row.items():
        if v is not None and v != 0 and k not in ['symbol','reportedCurrency','cik','filingDate','acceptedDate','fiscalYear','period','date']:
            print(f"  {k}: {v}")
