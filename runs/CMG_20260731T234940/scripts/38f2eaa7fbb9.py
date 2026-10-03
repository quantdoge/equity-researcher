import json
with open('data/cmg_balance_sheet.json') as f:
    bal = sorted(json.load(f), key=lambda x: x['fiscalYear'])

for row in bal:
    fy = row['fiscalYear']
    std = row.get('shortTermDebt') or 0
    ltd = row.get('longTermDebt') or 0
    cap_cur = row.get('capitalLeaseObligationsCurrent') or 0
    cap_nc = row.get('capitalLeaseObligationsNonCurrent') or 0
    cap_total = row.get('capitalLeaseObligations') or 0
    td = row.get('totalDebt')
    print(f"FY{fy}: STD={std}, LTD={ltd}, CapCur={cap_cur}, CapNC={cap_nc}, CapTotal={cap_total}, TotalDebt={td}")
