
import json
import numpy as np

# Load data
inc = json.load(open('data/cmg_income_statement_12q.json'))
bs = json.load(open('data/cmg_balance_sheet_12q.json'))
cf = json.load(open('data/cmg_cash_flow_12q.json'))
km = json.load(open('data/cmg_key_metrics_8y.json'))
ev = json.load(open('data/cmg_enterprise_value_12q.json'))
fs = json.load(open('data/cmg_financial_scores.json'))

# Sort ascending by date
for stmt in [inc, bs, cf, ev]:
    stmt.sort(key=lambda x: x['date'])

# Helper to safely get value
def getv(d, k, default=0.0):
    v = d.get(k)
    if v is None:
        return default
    return float(v)

# Build TTM summaries from quarterly data
# Use last 4 quarters as TTM_current, next 4 as TTM_prior
ttm_current_inc = {k: 0.0 for k in inc[0].keys() if k not in ['date','symbol','reportedCurrency','cik','filingDate','acceptedDate','fiscalYear','period','eps','epsDiluted']}
ttm_prior_inc = {k: 0.0 for k in inc[0].keys() if k not in ['date','symbol','reportedCurrency','cik','filingDate','acceptedDate','fiscalYear','period','eps','epsDiluted']}

for i in range(-4, 0):
    for k in ttm_current_inc:
        ttm_current_inc[k] += getv(inc[i], k)

for i in range(-8, -4):
    for k in ttm_prior_inc:
        ttm_prior_inc[k] += getv(inc[i], k)

# Same for cash flow
ttm_current_cf = {k: 0.0 for k in cf[0].keys() if k not in ['date','symbol','reportedCurrency','cik','filingDate','acceptedDate','fiscalYear','period']}
ttm_prior_cf = {k: 0.0 for k in cf[0].keys() if k not in ['date','symbol','reportedCurrency','cik','filingDate','acceptedDate','fiscalYear','period']}

for i in range(-4, 0):
    for k in ttm_current_cf:
        ttm_current_cf[k] += getv(cf[i], k)

for i in range(-8, -4):
    for k in ttm_prior_cf:
        ttm_prior_cf[k] += getv(cf[i], k)

# Balance sheets: point-in-time, use last and 4th-last
bs_current = bs[-1]
bs_prior = bs[-5]

print("TTM Current Revenue:", ttm_current_inc['revenue'])
print("TTM Prior Revenue:", ttm_prior_inc['revenue'])
print("TTM Current Net Income:", ttm_current_inc['netIncome'])
print("TTM Prior Net Income:", ttm_prior_inc['netIncome'])
print("TTM Current EBIT:", ttm_current_inc['ebit'])
print("TTM Prior EBIT:", ttm_prior_inc['ebit'])
print("Current Total Assets:", bs_current['totalAssets'])
print("Prior Total Assets:", bs_prior['totalAssets'])
print("Current Total Liabilities:", bs_current['totalLiabilities'])
print("Prior Total Liabilities:", bs_prior['totalLiabilities'])
print("Current Total Equity:", bs_current['totalStockholdersEquity'])
print("Prior Total Equity:", bs_prior['totalStockholdersEquity'])

# Check receivables
print("Current Receivables:", bs_current['accountsReceivables'])
print("Prior Receivables:", bs_prior['accountsReceivables'])

# Check COGS / costOfRevenue
print("Current COGS:", ttm_current_inc['costOfRevenue'])
print("Prior COGS:", ttm_prior_inc['costOfRevenue'])

# Check SG&A
print("Current SG&A:", ttm_current_inc['sellingGeneralAndAdministrativeExpenses'])
print("Prior SG&A:", ttm_prior_inc['sellingGeneralAndAdministrativeExpenses'])

# Check D&A from income statement
print("Current D&A (inc):", ttm_current_inc['depreciationAndAmortization'])
print("Prior D&A (inc):", ttm_prior_inc['depreciationAndAmortization'])

# Check PPE
print("Current PPE:", bs_current['propertyPlantEquipmentNet'])
print("Prior PPE:", bs_prior['propertyPlantEquipmentNet'])

# Check current assets/liabilities
print("Current Current Assets:", bs_current['totalCurrentAssets'])
print("Current Current Liabilities:", bs_current['totalCurrentLiabilities'])
print("Prior Current Assets:", bs_prior['totalCurrentAssets'])
print("Prior Current Liabilities:", bs_prior['totalCurrentLiabilities'])

# Check interest expense
print("Current Interest Expense:", ttm_current_inc['interestExpense'])
print("Prior Interest Expense:", ttm_prior_inc['interestExpense'])

# Check operating cash flow
print("Current OCF:", ttm_current_cf['operatingCashFlow'])
print("Prior OCF:", ttm_prior_cf['operatingCashFlow'])
