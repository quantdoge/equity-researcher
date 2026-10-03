import json
with open('data/cmg_balance_sheet.json') as f:
    bal = json.load(f)

for row in sorted(bal, key=lambda x: x['fiscalYear']):
    fy = row['fiscalYear']
    print(f"FY{fy}: shortTermDebt={row.get('shortTermDebt')}, longTermDebt={row.get('longTermDebt')}, capLeaseCurrent={row.get('capitalLeaseObligationsCurrent')}, capLeaseNonCurrent={row.get('capitalLeaseObligationsNonCurrent')}, capLeaseTotal={row.get('capitalLeaseObligations')}, totalDebt={row.get('totalDebt')}")
