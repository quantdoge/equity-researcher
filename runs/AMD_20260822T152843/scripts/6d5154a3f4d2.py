
import json
import math
from collections import OrderedDict

# Helper to load
def load(path):
    with open(path) as f:
        return json.load(f)

quote = load('data/amd_quote.json')[0]
kma = load('data/amd_key_metrics_a.json')  # annual key metrics
mrt = load('data/amd_metrics_ratios_ttm.json')[0]
fs = load('data/amd_financial_scores.json')[0]
dcf_adv = load('data/amd_dcf_advanced.json')[0]
dcf_lev = load('data/amd_dcf_levered.json')[0]
inc = load('data/amd_income_statement.json')  # 5 annual
bs = load('data/amd_balance_sheet.json')  # 5 annual
cf = load('data/statements_cashflow-statement.json')  # 10 rows, mixed periods
inc_full = load('data/statements_income-statement.json')  # 10 rows
gr = load('data/statements_financial-statement-growth.json')  # 10 rows
ph = load('data/chart_historical-price-eod-dividend-adjusted.json')

# Sort annual statements by fiscal year descending
inc_annual = sorted([r for r in inc_full if r.get('period') == 'FY'], key=lambda x: x['fiscalYear'], reverse=True)
bs_annual = sorted([r for r in bs if r.get('period') == 'FY'], key=lambda x: x['fiscalYear'], reverse=True)
cf_annual = sorted([r for r in cf if r.get('period') == 'FY'], key=lambda x: x['fiscalYear'], reverse=True)
gr_annual = sorted([r for r in gr if r.get('period') == 'FY'], key=lambda x: x['fiscalYear'], reverse=True)

print(f"Annual income statements: {len(inc_annual)} rows, years: {[r['fiscalYear'] for r in inc_annual]}")
print(f"Annual balance sheets: {len(bs_annual)} rows, years: {[r['fiscalYear'] for r in bs_annual]}")
print(f"Annual cash flows: {len(cf_annual)} rows, years: {[r['fiscalYear'] for r in cf_annual]}")
print(f"Annual growth: {len(gr_annual)} rows, years: {[r['fiscalYear'] for r in gr_annual]}")

# Show what fields are available in cash flow for first annual row
if cf_annual:
    print(f"\nCash flow fields FY{cf_annual[0]['fiscalYear']}: {list(cf_annual[0].keys())}")
