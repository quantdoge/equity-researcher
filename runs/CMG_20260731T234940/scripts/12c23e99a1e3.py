import json, math, os

with open('data/cmg_income_statement.json') as f:
    inc = sorted(json.load(f), key=lambda x: x['fiscalYear'])
with open('data/cmg_balance_sheet.json') as f:
    bal = sorted(json.load(f), key=lambda x: x['fiscalYear'])
with open('data/cmg_cashflow.json') as f:
    cf = sorted(json.load(f), key=lambda x: x['fiscalYear'])
with open('data/cmg_enterprise_values.json') as f:
    ev = sorted(json.load(f), key=lambda x: x['date'])
with open('data/cmg_key_metrics_ttm.json') as f:
    key_ttm = json.load(f)[0]
with open('data/cmg_financial_growth.json') as f:
    growth = sorted(json.load(f), key=lambda x: x['fiscalYear'])

inc_by = {r['fiscalYear']: r for r in inc}
bal_by = {r['fiscalYear']: r for r in bal}
cf_by = {r['fiscalYear']: r for r in cf}
ev_by = {r['date'][:4]: r for r in ev}
gr_by = {r['fiscalYear']: r for r in growth}

def safe(v):
    return float(v) if v is not None else None

def cagr(start, end, years):
    if start is None or end is None or start <= 0 or end <= 0:
        return None
    return (end / start) ** (1 / years) - 1

# Collect needed years
years5 = ['2021','2022','2023','2024','2025']
years_last5 = ['2021','2022','2023','2024','2025']

# 2. Margins
def margin_trend(metric, num_field, den_field):
    out = {}
    for y in years5:
        src = inc_by if num_field in inc_by[y] else cf_by
        num = safe(src[y].get(num_field)) if num_field in inc_by[y] else safe(cf_by[y].get(num_field))
        den = safe(inc_by[y].get(den_field))
        out[y] = num / den if num is not None and den and den != 0 else None
    return out

gm = margin_trend('grossMargin', 'grossProfit', 'revenue')
om = margin_trend('operatingMargin', 'operatingIncome', 'revenue')

# FCF margin: use freeCashFlow from cashflow statement
fcf_margin = {}
for y in years5:
    fcf = safe(cf_by[y].get('freeCashFlow'))
    rev = safe(inc_by[y].get('revenue'))
    fcf_margin[y] = fcf / rev if fcf is not None and rev and rev != 0 else None

print("=== 2. Margin trends (last 5 years) ===")
for y in years5:
    print(f"FY{y}: Gross={gm[y]:.4f} ({gm[y]*100:.2f}%), Operating={om[y]:.4f} ({om[y]*100:.2f}%), FCF={fcf_margin[y]:.4f} ({fcf_margin[y]*100:.2f}%)")
