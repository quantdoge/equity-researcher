
import json
import numpy as np
from datetime import datetime

# Load annual income statement
inc_annual = json.load(open('data/cmg_income_statement_annual_3y.json'))
inc_annual.sort(key=lambda x: x['date'])

# Load quarterly data
inc_q = json.load(open('data/cmg_income_statement_12q.json'))
bs_q = json.load(open('data/cmg_balance_sheet_12q.json'))
cf_q = json.load(open('data/cmg_cash_flow_12q.json'))
ev_q = json.load(open('data/cmg_enterprise_value_12q.json'))
km = json.load(open('data/cmg_key_metrics_8y.json'))

for stmt in [inc_q, bs_q, cf_q, ev_q]:
    stmt.sort(key=lambda x: x['date'])

# Use annual data for 2025 and 2024
inc_2025 = [r for r in inc_annual if r['date'] == '2025-12-31'][0]
inc_2024 = [r for r in inc_annual if r['date'] == '2024-12-31'][0]

# Use Q4 balance sheets as annual
bs_2025 = [r for r in bs_q if r['date'] == '2025-12-31'][0]
bs_2024 = [r for r in bs_q if r['date'] == '2024-12-31'][0]

# Use Q4 EV as annual
ev_2025 = [r for r in ev_q if r['date'] == '2025-12-31'][0]

# Construct annual cash flow by summing quarters
cf_2025_quarters = [r for r in cf_q if r['date'] in ['2025-03-31','2025-06-30','2025-09-30','2025-12-31']]
cf_2024_quarters = [r for r in cf_q if r['date'] in ['2024-03-31','2024-06-30','2024-09-30','2024-12-31']]

cf_2025 = {'operatingCashFlow': sum(r.get('operatingCashFlow') or 0 for r in cf_2025_quarters)}
cf_2024 = {'operatingCashFlow': sum(r.get('operatingCashFlow') or 0 for r in cf_2024_quarters)}

print("Annual 2025:")
print(f"  Revenue: {inc_2025['revenue']:,}")
print(f"  Net Income: {inc_2025['netIncome']:,}")
print(f"  EBIT: {inc_2025['ebit']:,}")
print(f"  Gross Profit: {inc_2025['grossProfit']:,}")
print(f"  SG&A: {inc_2025['sellingGeneralAndAdministrativeExpenses']:,}")
print(f"  D&A: {inc_2025['depreciationAndAmortization']:,}")
print(f"  Total Assets: {bs_2025['totalAssets']:,}")
print(f"  Current Assets: {bs_2025['totalCurrentAssets']:,}")
print(f"  Current Liabilities: {bs_2025['totalCurrentLiabilities']:,}")
print(f"  Total Liabilities: {bs_2025['totalLiabilities']:,}")
print(f"  Total Equity: {bs_2025['totalStockholdersEquity']:,}")
print(f"  PPE: {bs_2025['propertyPlantEquipmentNet']:,}")
print(f"  Receivables: {bs_2025['accountsReceivables']:,}")
print(f"  Retained Earnings: {bs_2025['retainedEarnings']:,}")
print(f"  Market Cap: {ev_2025['marketCapitalization']:,}")
print(f"  OCF: {cf_2025['operatingCashFlow']:,}")

print("\nAnnual 2024:")
print(f"  Revenue: {inc_2024['revenue']:,}")
print(f"  Net Income: {inc_2024['netIncome']:,}")
print(f"  EBIT: {inc_2024['ebit']:,}")
print(f"  Gross Profit: {inc_2024['grossProfit']:,}")
print(f"  SG&A: {inc_2024['sellingGeneralAndAdministrativeExpenses']:,}")
print(f"  D&A: {inc_2024['depreciationAndAmortization']:,}")
print(f"  Total Assets: {bs_2024['totalAssets']:,}")
print(f"  Current Assets: {bs_2024['totalCurrentAssets']:,}")
print(f"  Current Liabilities: {bs_2024['totalCurrentLiabilities']:,}")
print(f"  Total Liabilities: {bs_2024['totalLiabilities']:,}")
print(f"  Total Equity: {bs_2024['totalStockholdersEquity']:,}")
print(f"  PPE: {bs_2024['propertyPlantEquipmentNet']:,}")
print(f"  Receivables: {bs_2024['accountsReceivables']:,}")
print(f"  Retained Earnings: {bs_2024['retainedEarnings']:,}")
print(f"  OCF: {cf_2024['operatingCashFlow']:,}")
