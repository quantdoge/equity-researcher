
import json
from datetime import datetime

# Load and sort ascending
inc = json.load(open('data/cmg_income_statement_12q.json'))
bs = json.load(open('data/cmg_balance_sheet_12q.json'))
cf = json.load(open('data/cmg_cash_flow_12q.json'))
ev = json.load(open('data/cmg_enterprise_value_12q.json'))
km = json.load(open('data/cmg_key_metrics_8y.json'))
fs = json.load(open('data/cmg_financial_scores.json'))

for stmt in [inc, bs, cf, ev]:
    stmt.sort(key=lambda x: x['date'])

# Filter reliable data (<= 2025-12-31)
cutoff = '2025-12-31'
inc_rel = [r for r in inc if r['date'] <= cutoff]
bs_rel = [r for r in bs if r['date'] <= cutoff]
cf_rel = [r for r in cf if r['date'] <= cutoff]
ev_rel = [r for r in ev if r['date'] <= cutoff]

print("Available reliable dates:")
print("  INC:", [r['date'] for r in inc_rel])
print("  BS :", [r['date'] for r in bs_rel])
print("  CF :", [r['date'] for r in cf_rel])
print("  EV :", [r['date'] for r in ev_rel])

# Select TTM periods
# TTM current: 2025 Q1-Q4
ttm_curr_dates = ['2025-03-31', '2025-06-30', '2025-09-30', '2025-12-31']
# TTM prior: 2024 Q1-Q4
ttm_prior_dates = ['2024-03-31', '2024-06-30', '2024-09-30', '2024-12-31']

inc_curr = [r for r in inc_rel if r['date'] in ttm_curr_dates]
inc_prior = [r for r in inc_rel if r['date'] in ttm_prior_dates]
cf_curr = [r for r in cf_rel if r['date'] in ttm_curr_dates]
cf_prior = [r for r in cf_rel if r['date'] in ttm_prior_dates]

bs_curr = [r for r in bs_rel if r['date'] == '2025-12-31'][0]
bs_prior = [r for r in bs_rel if r['date'] == '2024-12-31'][0]
ev_curr = [r for r in ev_rel if r['date'] == '2025-12-31'][0]

print(f"\nTTM Current quarters: {[r['date'] for r in inc_curr]}")
print(f"TTM Prior quarters: {[r['date'] for r in inc_prior]}")

# TTM sums
def sum_fields(rows, fields):
    result = {}
    for f in fields:
        result[f] = sum(r.get(f) or 0 for r in rows)
    return result

inc_fields = ['revenue', 'costOfRevenue', 'grossProfit', 'sellingGeneralAndAdministrativeExpenses', 
              'operatingExpenses', 'operatingIncome', 'ebit', 'depreciationAndAmortization',
              'netIncome', 'incomeTaxExpense', 'incomeBeforeTax', 'interestExpense']
cf_fields = ['netIncome', 'operatingCashFlow', 'depreciationAndAmortization']

ttm_curr_inc = sum_fields(inc_curr, inc_fields)
ttm_prior_inc = sum_fields(inc_prior, inc_fields)
ttm_curr_cf = sum_fields(cf_curr, cf_fields)
ttm_prior_cf = sum_fields(cf_prior, cf_fields)

print("\nTTM Current (2025):")
for k, v in ttm_curr_inc.items():
    print(f"  {k}: {v:,.0f}")
print("  OCF:", ttm_curr_cf['operatingCashFlow'])

print("\nTTM Prior (2024):")
for k, v in ttm_prior_inc.items():
    print(f"  {k}: {v:,.0f}")
print("  OCF:", ttm_prior_cf['operatingCashFlow'])

print("\nBS Current (2025-12-31):")
bs_fields = ['totalAssets','totalCurrentAssets','totalCurrentLiabilities','totalLiabilities',
             'totalStockholdersEquity','propertyPlantEquipmentNet','accountsReceivables',
             'inventory','longTermDebt','shortTermDebt','totalDebt','cashAndCashEquivalents',
             'retainedEarnings','goodwillAndIntangibleAssets']
for f in bs_fields:
    print(f"  {f}: {bs_curr.get(f)}")

print("\nBS Prior (2024-12-31):")
for f in bs_fields:
    print(f"  {f}: {bs_prior.get(f)}")

print("\nEV Current (2025-12-31):")
print(f"  marketCapitalization: {ev_curr.get('marketCapitalization')}")
print(f"  enterpriseValue: {ev_curr.get('enterpriseValue')}")
