
import json
from datetime import datetime

inc = json.load(open('data/cmg_income_statement_12q.json'))
bs = json.load(open('data/cmg_balance_sheet_12q.json'))
cf = json.load(open('data/cmg_cash_flow_12q.json'))
ev = json.load(open('data/cmg_enterprise_value_12q.json'))

# Filter out future dates (beyond 2025-12-31)
cutoff = datetime(2025, 12, 31)
inc_rel = [r for r in inc if datetime.strptime(r['date'], '%Y-%m-%d') <= cutoff]
bs_rel = [r for r in bs if datetime.strptime(r['date'], '%Y-%m-%d') <= cutoff]
cf_rel = [r for r in cf if datetime.strptime(r['date'], '%Y-%m-%d') <= cutoff]
ev_rel = [r for r in ev if datetime.strptime(r['date'], '%Y-%m-%d') <= cutoff]

print(f"Reliable income stmt quarters: {len(inc_rel)}")
print(f"Reliable balance sheet quarters: {len(bs_rel)}")
print(f"Reliable cash flow quarters: {len(cf_rel)}")
print(f"Reliable EV quarters: {len(ev_rel)}")

print("\nReliable inc dates:", [r['date'] for r in inc_rel])
print("Reliable bs dates:", [r['date'] for r in bs_rel])
print("Reliable cf dates:", [r['date'] for r in cf_rel])
