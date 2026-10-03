import json, math, os

# Load data
with open('data/cmg_income_statement.json') as f:
    inc = sorted(json.load(f), key=lambda x: x['fiscalYear'])
with open('data/cmg_balance_sheet.json') as f:
    bal = sorted(json.load(f), key=lambda x: x['fiscalYear'])
with open('data/cmg_cashflow.json') as f:
    cf = sorted(json.load(f), key=lambda x: x['fiscalYear'])
with open('data/cmg_enterprise_values.json') as f:
    ev = sorted(json.load(f), key=lambda x: x['date'])
with open('data/cmg_financial_growth.json') as f:
    growth = sorted(json.load(f), key=lambda x: x['fiscalYear'])
with open('data/cmg_key_metrics_ttm.json') as f:
    key_ttm = json.load(f)[0]
with open('data/cmg_dcf.json') as f:
    dcf = json.load(f)[0]

# Build dictionaries by fiscal year
inc_by = {r['fiscalYear']: r for r in inc}
bal_by = {r['fiscalYear']: r for r in bal}
cf_by = {r['fiscalYear']: r for r in cf}
ev_by = {r['date'][:4]: r for r in ev}
gr_by = {r['fiscalYear']: r for r in growth}

# Helper functions
def safe(v):
    return float(v) if v is not None else None

def cagr(start, end, years):
    if start is None or end is None or start <= 0 or end <= 0:
        return None
    return (end / start) ** (1 / years) - 1

# --- 1. Historical CAGRs ---
# We need revenue, EBITDA, net income
years_needed = ['2020','2021','2022','2023','2024','2025']
metrics = {}
for y in years_needed:
    metrics[y] = {
        'revenue': safe(inc_by[y].get('revenue')),
        'ebitda': safe(inc_by[y].get('ebitda')),
        'netIncome': safe(inc_by[y].get('netIncome')),
        'epsDiluted': safe(inc_by[y].get('epsDiluted')),
        'weightedAverageShsOutDil': safe(inc_by[y].get('weightedAverageShsOutDil')),
    }

print("=== Annual figures ===")
for y in years_needed:
    print(y, metrics[y])

# CAGR 3-year (2022 -> 2025)
# CAGR 5-year (2020 -> 2025)
cagr_results = {}
for metric in ['revenue','ebitda','netIncome']:
    cagr_results[metric] = {
        '3yr': cagr(metrics['2022'][metric], metrics['2025'][metric], 3),
        '5yr': cagr(metrics['2020'][metric], metrics['2025'][metric], 5),
    }

print("\n=== CAGRs ===")
for metric, vals in cagr_results.items():
    print(f"{metric}: 3yr={vals['3yr']:.4f} ({vals['3yr']*100:.2f}%), 5yr={vals['5yr']:.4f} ({vals['5yr']*100:.2f}%)")
