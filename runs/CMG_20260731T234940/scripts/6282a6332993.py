import json, math

# Load all data files
with open('data/cmg_income_statement.json') as f:
    inc = json.load(f)
with open('data/cmg_balance_sheet.json') as f:
    bal = json.load(f)
with open('data/cmg_cashflow.json') as f:
    cf = json.load(f)
with open('data/cmg_key_metrics_ttm.json') as f:
    key_ttm = json.load(f)
with open('data/cmg_enterprise_values.json') as f:
    ev = json.load(f)
with open('data/cmg_owner_earnings.json') as f:
    oe = json.load(f)
with open('data/cmg_financial_growth.json') as f:
    growth = json.load(f)
with open('data/cmg_dcf.json') as f:
    dcf = json.load(f)

# Sort by fiscalYear
inc = sorted(inc, key=lambda x: x['fiscalYear'])
bal = sorted(bal, key=lambda x: x['fiscalYear'])
cf = sorted(cf, key=lambda x: x['fiscalYear'])
ev = sorted(ev, key=lambda x: x['date'])
growth = sorted(growth, key=lambda x: x['fiscalYear'])

print("Income statement years:", [x['fiscalYear'] for x in inc])
print("Balance sheet years:", [x['fiscalYear'] for x in bal])
print("Cash flow years:", [x['fiscalYear'] for x in cf])
print("EV years:", [x['date'] for x in ev])
print("Growth years:", [x['fiscalYear'] for x in growth])
