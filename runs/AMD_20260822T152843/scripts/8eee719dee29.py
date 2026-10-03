
import json
import math
from collections import OrderedDict

def load(path):
    with open(path) as f:
        return json.load(f)

# Load all data
quote = load('data/amd_quote.json')[0]
kma = sorted(load('data/amd_key_metrics_a.json'), key=lambda x: x['fiscalYear'], reverse=True)
mrt = load('data/amd_metrics_ratios_ttm.json')[0]
fs = load('data/amd_financial_scores.json')[0]
dcf_adv = load('data/amd_dcf_advanced.json')[0]
dcf_lev = load('data/amd_dcf_levered.json')[0]

inc_all = sorted([r for r in load('data/statements_income-statement.json') if r.get('period')=='FY'],
                 key=lambda x: x['fiscalYear'], reverse=True)
bs_all = sorted([r for r in load('data/amd_balance_sheet.json') if r.get('period')=='FY'],
                key=lambda x: x['fiscalYear'], reverse=True)
cf_all = sorted([r for r in load('data/statements_cashflow-statement.json') if r.get('period')=='FY'],
                key=lambda x: x['fiscalYear'], reverse=True)
ph = load('data/chart_historical-price-eod-dividend-adjusted.json')

years_5 = ['2025','2024','2023','2022','2021']
inc_5 = [r for r in inc_all if r['fiscalYear'] in years_5]
bs_5 = [r for r in bs_all if r['fiscalYear'] in years_5]
cf_5 = [r for r in cf_all if r['fiscalYear'] in years_5]

# Helpers
def getv(row, key, default=None):
    return row.get(key, default)

def cagr(begin_val, end_val, years):
    if begin_val is None or end_val is None or begin_val <= 0 or years <= 0:
        return None
    return (end_val / begin_val) ** (1/years) - 1

# Results container
R = OrderedDict()

# ── 1. Current Market Data ─────────────────────────────────────────
R['Price (USD)'] = round(quote['price'], 2)
R['Market Cap (USD B)'] = round(quote['marketCap']/1e9, 2)
R['52-Week High'] = round(quote['yearHigh'], 2)
R['52-Week Low'] = round(quote['yearLow'], 2)
R['50-Day MA'] = round(quote.get('priceAvg50',0), 2) if quote.get('priceAvg50') else None
R['200-Day MA'] = round(quote.get('priceAvg200',0), 2) if quote.get('priceAvg200') else None

# ── 2. Valuation Multiples (TTM) ──────────────────────────────────
R['P/E TTM'] = round(mrt['priceToEarningsRatioTTM'], 2)
R['EV/EBITDA TTM'] = round(mrt['enterpriseValueMultipleTTM'], 2)
R['P/S TTM'] = round(mrt['priceToSalesRatioTTM'], 2)
R['P/B TTM'] = round(mrt['priceToBookRatioTTM'], 2)
R['P/FCF TTM'] = round(mrt['priceToFreeCashFlowRatioTTM'], 2)

# ── 3. Revenue CAGR ───────────────────────────────────────────────
rev_2025 = getv(inc_all[0], 'revenue')
rev_2022 = next((getv(r,'revenue') for r in inc_all if r['fiscalYear']=='2022'), None)
rev_2020 = next((getv(r,'revenue') for r in inc_all if r['fiscalYear']=='2020'), None)
R['Revenue CAGR 3Y (%)'] = round(cagr(rev_2022, rev_2025, 3)*100, 2)
R['Revenue CAGR 5Y (%)'] = round(cagr(rev_2020, rev_2025, 5)*100, 2)

# ── 4. Margin Trends (FY2021–FY2025) ────────────────────────────
for r in inc_5:
    fy = r['fiscalYear']
    rev = getv(r,'revenue')
    gp = getv(r,'grossProfit')
    op = getv(r,'operatingIncome')
    ni = getv(r,'netIncome')
    R[f'Gross Margin {fy} (%)'] = round(gp/rev*100, 2) if rev and gp else None
    R[f'Op Margin {fy} (%)'] = round(op/rev*100, 2) if rev and op else None
    R[f'Net Margin {fy} (%)'] = round(ni/rev*100, 2) if rev and ni else None

# ── 5. ROE / ROIC Trends ──────────────────────────────────────────
for r in kma:
    fy = r['fiscalYear']
    if fy in years_5:
        R[f'ROE {fy} (%)'] = round(getv(r,'returnOnEquity')*100, 2) if getv(r,'returnOnEquity') is not None else None
        R[f'ROIC {fy} (%)'] = round(getv(r,'returnOnInvestedCapital')*100, 2) if getv(r,'returnOnInvestedCapital') is not None else None

# ── 6. Balance Sheet Health ───────────────────────────────────────
for r in bs_5:
    fy = r['fiscalYear']
    td = getv(r,'totalDebt')
    te = getv(r,'totalStockholdersEquity')
    ca = getv(r,'totalCurrentAssets')
    cl = getv(r,'totalCurrentLiabilities')
    R[f'Debt/Equity {fy}'] = round(td/te, 3) if te and td is not None else None
    R[f'Current Ratio {fy}'] = round(ca/cl, 2) if ca and cl else None

# ── 7. Cash Flow Trends ───────────────────────────────────────────
for r in cf_5:
    fy = r['fiscalYear']
    ocf = getv(r,'operatingCashFlow')
    fcf = getv(r,'freeCashFlow')
    capex = getv(r,'capitalExpenditure')
    R[f'OCF {fy} (USD M)'] = round(ocf/1e6, 1) if ocf else None
    R[f'FCF {fy} (USD M)'] = round(fcf/1e6, 1) if fcf else None
    R[f'CapEx {fy} (USD M)'] = round(capex/1e6, 1) if capex else None

# ── 8. Altman Z & Piotroski F ─────────────────────────────────────
R['Altman Z-Score'] = round(fs['altmanZScore'], 2)
R['Piotroski F-Score'] = fs['piotroskiScore']

# ── 9. DCF Valuation ──────────────────────────────────────────────
R['DCF Advanced (USD)'] = round(dcf_adv['dcf'], 2)
R['DCF Levered (USD)'] = round(dcf_lev['dcf'], 2)
R['DCF vs Price (%)'] = round((dcf_adv['dcf']/quote['price'] - 1)*100, 1)

# ── 10. Beneish M-Score Inputs ───────────────────────────────────
# Revenue growth, receivables growth, gross margin index, etc.
for i, r in enumerate(inc_5):
    fy = r['fiscalYear']
    bs_row = next((b for b in bs_5 if b['fiscalYear']==fy), None)
    if bs_row:
        rev = getv(r,'revenue')
        gp = getv(r,'grossProfit')
        ar = getv(bs_row,'netReceivables')
        ta = getv(bs_row,'totalAssets')
        R[f'Beneish_Rev_{fy} (USD M)'] = round(rev/1e6, 1) if rev else None
        R[f'Beneish_AR_{fy} (USD M)'] = round(ar/1e6, 1) if ar else None
        R[f'Beneish_GM_{fy}'] = round(gp/rev, 4) if rev and gp else None
        R[f'Beneish_TA_{fy} (USD M)'] = round(ta/1e6, 1) if ta else None

# Compute growth rates for Beneish
for i in range(1, len(inc_5)):
    fy_curr = inc_5[i-1]['fiscalYear']
    fy_prev = inc_5[i]['fiscalYear']
    rev_curr = getv(inc_5[i-1], 'revenue')
    rev_prev = getv(inc_5[i], 'revenue')
    ar_curr = next((getv(b,'netReceivables') for b in bs_5 if b['fiscalYear']==fy_curr), None)
    ar_prev = next((getv(b,'netReceivables') for b in bs_5 if b['fiscalYear']==fy_prev), None)
    if rev_prev and rev_curr:
        R[f'Beneish_RevGrowth_{fy_curr}/{fy_prev} (%)'] = round((rev_curr/rev_prev - 1)*100, 2)
    if ar_prev and ar_curr:
        R[f'Beneish_ARGrowth_{fy_curr}/{fy_prev} (%)'] = round((ar_curr/ar_prev - 1)*100, 2)

# ── 11. Accruals Ratio ────────────────────────────────────────────
for r in cf_5:
    fy = r['fiscalYear']
    ni = getv(r,'netIncome')
    cfo = getv(r,'operatingCashFlow')
    bs_row = next((b for b in bs_5 if b['fiscalYear']==fy), None)
    ta = getv(bs_row,'totalAssets') if bs_row else None
    if ni is not None and cfo is not None and ta and ta != 0:
        R[f'Accruals Ratio {fy}'] = round((ni - cfo) / ta, 4)
    else:
        R[f'Accruals Ratio {fy}'] = None

# ── 12. Volatility ───────────────────────────────────────────────
if ph:
    closes = [d['adjClose'] for d in ph if d.get('adjClose')]
    if len(closes) > 1:
        import statistics
        log_returns = [math.log(closes[i]/closes[i-1]) for i in range(1, len(closes))]
        daily_vol = statistics.stdev(log_returns)
        ann_vol = daily_vol * math.sqrt(252)
        R['Annualized Volatility 2Y (%)'] = round(ann_vol*100, 2)
    else:
        R['Annualized Volatility 2Y (%)'] = None

# ── 13. Beta Proxy ───────────────────────────────────────────────
# Unavailable: market index data not fetched
R['Beta Proxy'] = 'N/A (market index data unavailable)'

# Save
with open('data/amd_computed_metrics.json', 'w') as f:
    json.dump(dict(R), f, indent=2)

# Print formatted table
print("="*80)
print("AMD (Advanced Micro Devices, Inc.) — Pre-Computed Quantitative Metrics")
print("="*80)
for k, v in R.items():
    val = "N/A" if v is None else v
    print(f"{k:<45} {val}")
print("="*80)
