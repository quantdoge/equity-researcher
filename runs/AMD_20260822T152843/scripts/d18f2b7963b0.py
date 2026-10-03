
import json
import math
from collections import OrderedDict

def load(path):
    with open(path) as f:
        return json.load(f)

# Load data
quote = load('data/amd_quote.json')[0]
kma = sorted(load('data/amd_key_metrics_a.json'), key=lambda x: x['fiscalYear'], reverse=True)
mrt = load('data/amd_metrics_ratios_ttm.json')[0]
fs = load('data/amd_financial_scores.json')[0]
dcf_adv = load('data/amd_dcf_advanced.json')[0]
dcf_lev = load('data/amd_dcf_levered.json')[0]

# Use full statement files for maximum history
inc_all = sorted([r for r in load('data/statements_income-statement.json') if r.get('period')=='FY'],
                 key=lambda x: x['fiscalYear'], reverse=True)
bs_all = sorted([r for r in load('data/amd_balance_sheet.json') if r.get('period')=='FY'],
                key=lambda x: x['fiscalYear'], reverse=True)
cf_all = sorted([r for r in load('data/statements_cashflow-statement.json') if r.get('period')=='FY'],
                key=lambda x: x['fiscalYear'], reverse=True)
gr_all = sorted([r for r in load('data/statements_financial-statement-growth.json') if r.get('period')=='FY'],
                key=lambda x: x['fiscalYear'], reverse=True)
ph = load('data/chart_historical-price-eod-dividend-adjusted.json')

# Filter last 5 years for most trends, but keep full for CAGR
years_5 = ['2025','2024','2023','2022','2021']
inc_5 = [r for r in inc_all if r['fiscalYear'] in years_5]
bs_5 = [r for r in bs_all if r['fiscalYear'] in years_5]
cf_5 = [r for r in cf_all if r['fiscalYear'] in years_5]
gr_5 = [r for r in gr_all if r['fiscalYear'] in years_5]

# Helper to get value safely
def getv(row, key, default=None):
    return row.get(key, default)

# Helper CAGR
def cagr(begin_val, end_val, years):
    if begin_val is None or end_val is None or begin_val <= 0 or years <= 0:
        return None
    return (end_val / begin_val) ** (1/years) - 1

results = OrderedDict()

# 1. Current price & valuation multiples from quote / TTM
results['Current Price'] = quote.get('price')
results['Market Cap (B)'] = round(quote.get('marketCap',0)/1e9, 2) if quote.get('marketCap') else None
results['52-Week High'] = quote.get('yearHigh')
results['52-Week Low'] = quote.get('yearLow')
results['P/E TTM'] = mrt.get('priceToEarningsRatioTTM')
results['EV/EBITDA TTM'] = mrt.get('enterpriseValueMultipleTTM')  # EV/EBITDA proxy
results['P/S TTM'] = mrt.get('priceToSalesRatioTTM')
results['P/B TTM'] = mrt.get('priceToBookRatioTTM')
results['Beta'] = None  # Cannot compute without market index data

# 2. Revenue CAGR
rev_2025 = getv(inc_all[0], 'revenue') if len(inc_all)>0 else None
rev_2022 = next((getv(r,'revenue') for r in inc_all if r['fiscalYear']=='2022'), None)
rev_2020 = next((getv(r,'revenue') for r in inc_all if r['fiscalYear']=='2020'), None)
results['Revenue CAGR 3Y'] = round(cagr(rev_2022, rev_2025, 3)*100, 2) if cagr(rev_2022, rev_2025, 3) else None
results['Revenue CAGR 5Y'] = round(cagr(rev_2020, rev_2025, 5)*100, 2) if cagr(rev_2020, rev_2025, 5) else None

# 3. Margin trends (last 5 years)
for r in inc_5:
    fy = r['fiscalYear']
    rev = getv(r,'revenue')
    gp = getv(r,'grossProfit')
    op = getv(r,'operatingIncome')
    ni = getv(r,'netIncome')
    results[f'Gross Margin {fy}'] = round(gp/rev*100, 2) if rev and gp else None
    results[f'Operating Margin {fy}'] = round(op/rev*100, 2) if rev and op else None
    results[f'Net Margin {fy}'] = round(ni/rev*100, 2) if rev and ni else None

# 4. ROE and ROIC trends from key-metrics annual
for r in kma:
    fy = r['fiscalYear']
    if fy in years_5:
        results[f'ROE {fy}'] = round(getv(r,'returnOnEquity')*100, 2) if getv(r,'returnOnEquity') else None
        results[f'ROIC {fy}'] = round(getv(r,'returnOnInvestedCapital')*100, 2) if getv(r,'returnOnInvestedCapital') else None

# 5. Debt/Equity and Current Ratio
for r in bs_5:
    fy = r['fiscalYear']
    td = getv(r,'totalDebt')
    te = getv(r,'totalStockholdersEquity')
    ca = getv(r,'totalCurrentAssets')
    cl = getv(r,'totalCurrentLiabilities')
    results[f'Debt/Equity {fy}'] = round(td/te, 2) if te and td is not None else None
    results[f'Current Ratio {fy}'] = round(ca/cl, 2) if ca and cl else None

# 6. FCF generation trend
for r in cf_5:
    fy = r['fiscalYear']
    fcf = getv(r,'freeCashFlow')
    ocf = getv(r,'operatingCashFlow')
    results[f'FCF {fy} (M)'] = round(fcf/1e6, 1) if fcf else None
    results[f'OCF {fy} (M)'] = round(ocf/1e6, 1) if ocf else None

# 7. Altman Z & Piotroski F
results['Altman Z-Score'] = round(fs.get('altmanZScore'), 2) if fs.get('altmanZScore') else None
results['Piotroski F-Score'] = fs.get('piotroskiScore')

# 8. DCF
results['DCF Advanced'] = round(dcf_adv.get('dcf'), 2) if dcf_adv.get('dcf') else None
results['DCF Levered'] = round(dcf_lev.get('dcf'), 2) if dcf_lev.get('dcf') else None

# 9. Beneish M-Score inputs
# We need: receivables growth, revenue growth, gross margin index, etc.
# For years where we have both inc and bs
for i, r in enumerate(inc_5):
    fy = r['fiscalYear']
    bs_row = next((b for b in bs_5 if b['fiscalYear']==fy), None)
    if bs_row:
        rev = getv(r,'revenue')
        gp = getv(r,'grossProfit')
        ar = getv(bs_row,'netReceivables')
        results[f'Beneish_Revenue_{fy}'] = rev
        results[f'Beneish_Receivables_{fy}'] = ar
        results[f'Beneish_GrossMargin_{fy}'] = round(gp/rev, 4) if rev and gp else None

# 10. Accruals ratio = (Net Income - CFO) / Total Assets
for i, r in enumerate(cf_5):
    fy = r['fiscalYear']
    ni = getv(r,'netIncome')
    cfo = getv(r,'operatingCashFlow')
    bs_row = next((b for b in bs_5 if b['fiscalYear']==fy), None)
    ta = getv(bs_row,'totalAssets') if bs_row else None
    if ni is not None and cfo is not None and ta and ta != 0:
        results[f'Accruals Ratio {fy}'] = round((ni - cfo) / ta, 4)
    else:
        results[f'Accruals Ratio {fy}'] = None

# 11. Price volatility (annualized) from 2-year daily history
if ph:
    closes = [d['adjClose'] for d in ph if d.get('adjClose')]
    if len(closes) > 1:
        import statistics
        log_returns = [math.log(closes[i]/closes[i-1]) for i in range(1, len(closes))]
        daily_vol = statistics.stdev(log_returns)
        ann_vol = daily_vol * math.sqrt(252)
        results['Annualized Volatility (2Y)'] = round(ann_vol*100, 2)
    else:
        results['Annualized Volatility (2Y)'] = None
else:
    results['Annualized Volatility (2Y)'] = None

# Print clean table
print("\n" + "="*70)
print("AMD QUANTITATIVE METRICS")
print("="*70)
for k, v in results.items():
    if v is None:
        v = "N/A"
    elif isinstance(v, float):
        v = f"{v:.2f}" if abs(v) < 1000 else f"{v:,.2f}"
    print(f"{k:<40} {v}")
print("="*70)

# Also save to file for reproducibility
with open('data/amd_computed_metrics.json', 'w') as f:
    json.dump(dict(results), f, indent=2)
print("\nSaved to data/amd_computed_metrics.json")
