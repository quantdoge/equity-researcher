import json, math

# ------------------------------------------------------------------
# CMG Quant Engine Script
# ------------------------------------------------------------------
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

store_counts = {
    '2020': 2768, '2021': 2966, '2022': 3187,
    '2023': 3437, '2024': 3726, '2025': 4056,
}

# 1. CAGRs
print("="*60)
print("1. CAGRs")
print("="*60)
for metric in ['revenue','ebitda','netIncome']:
    c3 = cagr(safe(inc_by['2022'][metric]), safe(inc_by['2025'][metric]), 3)
    c5 = cagr(safe(inc_by['2020'][metric]), safe(inc_by['2025'][metric]), 5)
    print(f"{metric:10s}: 3-yr = {c3*100:6.2f}%, 5-yr = {c5*100:6.2f}%")

eps_cagr = cagr(safe(inc_by['2022']['epsDiluted']), safe(inc_by['2025']['epsDiluted']), 3)
print(f"{'epsDiluted':10s}: 3-yr = {eps_cagr*100:6.2f}%")

# 2. Margins
print("\n" + "="*60)
print("2. MARGIN TRENDS")
print("="*60)
for y in ['2021','2022','2023','2024','2025']:
    rev = safe(inc_by[y]['revenue'])
    gm = safe(inc_by[y]['grossProfit']) / rev
    om = safe(inc_by[y]['operatingIncome']) / rev
    fcfm = safe(cf_by[y]['freeCashFlow']) / rev
    sbcr = safe(cf_by[y]['stockBasedCompensation']) / rev
    print(f"FY{y}: Gross={gm*100:5.2f}%  Op={om*100:5.2f}%  FCF={fcfm*100:5.2f}%  SBC/rev={sbcr*100:5.2f}%")

# 3. SSS proxy
print("\n" + "="*60)
print("3. SSS PROXY")
print("="*60)
for y in ['2022','2023','2024','2025']:
    p = str(int(y)-1)
    rg = safe(inc_by[y]['revenue']) / safe(inc_by[p]['revenue']) - 1
    ug = store_counts[y] / store_counts[p] - 1
    print(f"FY{y}: Rev+{rg*100:5.2f}%  Unit+{ug*100:5.2f}%  SSS_proxy={ (rg-ug)*100:5.2f}%")

# 4. ROIC
print("\n" + "="*60)
print("4. ROIC DECOMPOSITION")
print("="*60)
for y in ['2023','2024','2025']:
    ebit = safe(inc_by[y]['ebit'])
    tax = safe(inc_by[y]['incomeTaxExpense'])
    ibt = safe(inc_by[y]['incomeBeforeTax'])
    eff_tax = tax / ibt if ibt else None
    nopat = ebit * (1-eff_tax) if eff_tax else None
    eq = safe(bal_by[y]['totalStockholdersEquity'])
    debt = safe(bal_by[y]['totalDebt'])
    cash = safe(bal_by[y]['cashAndCashEquivalents'])
    std = safe(bal_by[y]['shortTermDebt']) or 0
    ltd = safe(bal_by[y]['longTermDebt']) or 0
    cap = safe(bal_by[y]['capitalLeaseObligations']) or 0
    adj_debt = (std + ltd) if (ltd and cap and abs(ltd-cap) < 1e-6) else debt
    ic_a = eq + adj_debt - cash
    ta = safe(bal_by[y]['totalAssets'])
    cl = safe(bal_by[y]['totalCurrentLiabilities'])
    ic_b = ta - cl
    print(f"FY{y}: NOPAT={nopat:,.0f}  IC_A={ic_a:,.0f} ROIC_A={nopat/ic_a*100:5.2f}%  IC_B={ic_b:,.0f} ROIC_B={nopat/ic_b*100:5.2f}%")

# 5. Debt/EBITDA
print("\n" + "="*60)
print("5. DEBT/EBITDA (cap lease adjusted)")
print("="*60)
for y in ['2021','2022','2023','2024','2025']:
    ebitda = safe(inc_by[y]['ebitda'])
    debt = safe(bal_by[y]['totalDebt'])
    std = safe(bal_by[y]['shortTermDebt']) or 0
    ltd = safe(bal_by[y]['longTermDebt']) or 0
    cap = safe(bal_by[y]['capitalLeaseObligations']) or 0
    adj = (std + ltd) if (ltd and cap and abs(ltd-cap) < 1e-6) else debt
    print(f"FY{y}: AdjDebt={adj:,.0f}  EBITDA={ebitda:,.0f}  Ratio={adj/ebitda:.2f}x")

# 6. FCF conversion
print("\n" + "="*60)
print("6. FCF CONVERSION")
print("="*60)
for y in ['2021','2022','2023','2024','2025']:
    fcf = safe(cf_by[y]['freeCashFlow'])
    ni = safe(inc_by[y]['netIncome'])
    print(f"FY{y}: FCF={fcf:,.0f}  NI={ni:,.0f}  Conv={fcf/ni*100:5.1f}%")

# 7. Buyback yield
print("\n" + "="*60)
print("7. BUYBACK YIELD")
print("="*60)
for y in ['2024','2025']:
    rep = abs(safe(cf_by[y]['commonStockRepurchased']))
    mc = safe(ev_by[y]['marketCapitalization'])
    print(f"FY{y}: Repurchases=${rep/1e6:5.1f}M  MktCap=${mc/1e9:5.2f}B  Yield={rep/mc*100:4.2f}%")

# 8. SBC trend
print("\n" + "="*60)
print("8. SBC / REVENUE")
print("="*60)
for y in ['2021','2022','2023','2024','2025']:
    sbc = safe(cf_by[y]['stockBasedCompensation'])
    rev = safe(inc_by[y]['revenue'])
    print(f"FY{y}: SBC=${sbc/1e6:5.1f}M  Rev=${rev/1e9:5.2f}B  Ratio={sbc/rev*100:4.2f}%")

# 9. Correlation
print("\n" + "="*60)
print("9. CORRELATION: revenue growth vs capex growth")
print("="*60)
rg, cg = [], []
for y in ['2021','2022','2023','2024','2025']:
    p = str(int(y)-1)
    r = safe(inc_by[y]['revenue']) / safe(inc_by[p]['revenue']) - 1
    c = abs(safe(cf_by[y]['capitalExpenditure'])) / abs(safe(cf_by[p]['capitalExpenditure'])) - 1
    rg.append(r); cg.append(c)
    print(f"FY{y}: Rev+{r*100:5.2f}%  Capex+{c*100:5.2f}%")
mr, mc = sum(rg)/5, sum(cg)/5
num = sum((a-mr)*(b-mc) for a,b in zip(rg,cg))
dr = math.sqrt(sum((a-mr)**2 for a in rg))
dc = math.sqrt(sum((b-mc)**2 for b in cg))
print(f"Pearson r = {num/(dr*dc):.4f}")

# 10. EV/Store
print("\n" + "="*60)
print("10. EV / STORE")
print("="*60)
for y in ['2023','2024','2025']:
    evv = safe(ev_by[y]['enterpriseValue'])
    st = store_counts[y]
    print(f"FY{y}: EV=${evv/1e9:5.2f}B  Stores={st}  EV/Store=${evv/st/1e6:5.2f}M")

# 11. PEG
print("\n" + "="*60)
print("11. PEG RATIO")
print("="*60)
peg = 34.3 / (eps_cagr * 100)
print(f"P/E = 34.3, 3-yr EPS CAGR = {eps_cagr*100:.2f}%, PEG = {peg:.2f}")

# 12. DCF check
print("\n" + "="*60)
print("12. DCF CHECK")
print("="*60)
print(f"FMP DCF value: ${dcf['dcf']:.2f}")
print(f"FMP price in DCF file: ${dcf['Stock Price']:.2f}")
ev_shares = safe(ev_by['2025']['numberOfShares'])
print(f"FMP EV endpoint shares: {ev_shares/1e6:.1f}M")
print(f"TTM mkt cap (key-metrics-ttm): ${safe(key_ttm['marketCap'])/1e9:.2f}B")
print(f"Implied price from mkt cap at ${ev_shares/1e6:.1f}M shares = ${safe(key_ttm['marketCap'])/ev_shares:.2f}")
