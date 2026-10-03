import json, math, os, statistics

# Load data
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
with open('data/cmg_dcf.json') as f:
    dcf = json.load(f)[0]

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

# Store counts from verified sources
store_counts = {
    '2020': 2768,
    '2021': 2966,
    '2022': 3187,
    '2023': 3437,
    '2024': 3726,
    '2025': 4056,
}

# ===================
# 1. CAGRs
# ===================
print("="*60)
print("1. REVENUE, EBITDA, NET INCOME CAGRs")
print("="*60)
for metric in ['revenue','ebitda','netIncome']:
    c3 = cagr(safe(inc_by['2022'][metric]), safe(inc_by['2025'][metric]), 3)
    c5 = cagr(safe(inc_by['2020'][metric]), safe(inc_by['2025'][metric]), 5)
    print(f"{metric}: 3-yr CAGR = {c3*100:.2f}%, 5-yr CAGR = {c5*100:.2f}%")

# EPS CAGR for PEG
eps_22 = safe(inc_by['2022']['epsDiluted'])
eps_25 = safe(inc_by['2025']['epsDiluted'])
eps_cagr_3 = cagr(eps_22, eps_25, 3)
print(f"EPS diluted 3-yr CAGR (2022-2025) = {eps_cagr_3*100:.2f}%")

# ===================
# 2. Margins
# ===================
print("\n" + "="*60)
print("2. MARGIN TRENDS (last 5 fiscal years)")
print("="*60)
years5 = ['2021','2022','2023','2024','2025']
for y in years5:
    rev = safe(inc_by[y]['revenue'])
    gp = safe(inc_by[y]['grossProfit'])
    op = safe(inc_by[y]['operatingIncome'])
    fcf = safe(cf_by[y]['freeCashFlow'])
    sbc = safe(cf_by[y]['stockBasedCompensation'])
    print(f"FY{y}: Gross={gp/rev*100:.2f}%, Operating={op/rev*100:.2f}%, FCF={fcf/rev*100:.2f}%, SBC/rev={sbc/rev*100:.2f}%")

# ===================
# 3. SSS proxy
# ===================
print("\n" + "="*60)
print("3. SAME-STORE SALES GROWTH PROXY (revenue growth - unit growth)")
print("="*60)
for y in ['2022','2023','2024','2025']:
    prev_y = str(int(y)-1)
    rev_g = safe(inc_by[y]['revenue']) / safe(inc_by[prev_y]['revenue']) - 1
    unit_g = store_counts[y] / store_counts[prev_y] - 1
    sss_proxy = rev_g - unit_g
    print(f"FY{y}: Revenue growth={rev_g*100:.2f}%, Unit growth={unit_g*100:.2f}%, SSS proxy={sss_proxy*100:.2f}%")

# ===================
# 4. ROIC decomposition
# ===================
print("\n" + "="*60)
print("4. ROIC DECOMPOSITION: NOPAT / Invested Capital")
print("="*60)
# Method: NOPAT = EBIT * (1 - effective tax rate)
# Invested Capital = Total Equity + Total Debt (includes capital leases) - Cash and Cash Equivalents
# Actually standard ROIC denominator: Total Equity + Total Debt - Cash. But let's also show Assets - Current Liabilities.
for y in ['2023','2024','2025']:
    ebit = safe(inc_by[y]['ebit'])
    ibt = safe(inc_by[y]['incomeBeforeTax'])
    tax = safe(inc_by[y]['incomeTaxExpense'])
    rev = safe(inc_by[y]['revenue'])
    # effective tax rate
    eff_tax = tax / ibt if ibt and ibt != 0 else None
    nopat = ebit * (1 - eff_tax) if eff_tax is not None else None
    
    equity = safe(bal_by[y]['totalStockholdersEquity'])
    debt = safe(bal_by[y]['totalDebt'])
    cash = safe(bal_by[y]['cashAndCashEquivalents'])
    
    # Approach A: Equity + Debt - Cash
    ic_a = equity + debt - cash if equity is not None and debt is not None and cash is not None else None
    roic_a = nopat / ic_a if nopat and ic_a and ic_a != 0 else None
    
    # Approach B: Total Assets - Current Liabilities
    ta = safe(bal_by[y]['totalAssets'])
    cl = safe(bal_by[y]['totalCurrentLiabilities'])
    ic_b = ta - cl if ta is not None and cl is not None else None
    roic_b = nopat / ic_b if nopat and ic_b and ic_b != 0 else None
    
    print(f"FY{y}: EBIT={ebit:,.0f}, Tax={tax:,.0f}, ETR={eff_tax*100:.1f}%, NOPAT={nopat:,.0f}")
    print(f"       IC (Equity+Debt-Cash)={ic_a:,.0f}, ROIC_A={roic_a*100:.2f}%")
    print(f"       IC (Assets-CurrLiab)={ic_b:,.0f}, ROIC_B={roic_b*100:.2f}%")
