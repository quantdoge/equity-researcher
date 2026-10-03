
import json
import numpy as np
from datetime import datetime

# Load all data
inc = json.load(open('data/cmg_income_statement_12q.json'))
bs = json.load(open('data/cmg_balance_sheet_12q.json'))
cf = json.load(open('data/cmg_cash_flow_12q.json'))
km = json.load(open('data/cmg_key_metrics_8y.json'))
ev = json.load(open('data/cmg_enterprise_value_12q.json'))
fs = json.load(open('data/cmg_financial_scores.json'))

# Sort by date ascending
for stmt in [inc, bs, cf, ev]:
    stmt.sort(key=lambda x: x['date'])

km.sort(key=lambda x: x['date'])

print("Income statement dates:", [r['date'] for r in inc[-4:]])
print("Balance sheet dates:", [r['date'] for r in bs[-4:]])
print("Cash flow dates:", [r['date'] for r in cf[-4:]])
print("Key metrics dates:", [r['date'] for r in km[-4:]])
print("EV dates:", [r['date'] for r in ev[-4:]])

# Check fields in latest inc
print("\nLatest inc keys:", sorted(inc[-1].keys()))
print("\nLatest bs keys:", sorted(bs[-1].keys()))
print("\nLatest cf keys:", sorted(cf[-1].keys()))
