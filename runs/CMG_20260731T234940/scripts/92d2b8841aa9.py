import json, math, statistics, os

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

# Store counts
store_counts = {
    '2020': 2768,
    '2021': 2966,
    '2022': 3187,
    '2023': 3437,
    '2024': 3726,
    '2025': 4056,
}

# ===================
# 5. Debt/EBITDA incl capital leases (adjusted for 2025 double-count)
# ===================
print("="*60)
print("5. DEBT/EBITDA (capital lease adjusted)")
print("="*60)
for y in ['2021','2022','2023','2024','2025']:
    ebitda = safe(inc_by[y]['ebitda'])
    raw_debt = safe(bal_by[y]['totalDebt'])
    std = safe(bal_by[y]['shortTermDebt']) or 0
    ltd = safe(bal_by[y]['longTermDebt']) or 0
    cap_total = safe(bal_by[y]['capitalLeaseObligations']) or 0
    # Adjust for 2025 double counting where longTermDebt == capLeaseNonCurrent
    if ltd and cap_total and abs(ltd - cap_total) < 1e-6:
        adj_debt = std + ltd  # already includes leases
    else:
        adj_debt = raw_debt
    ratio = adj_debt / ebitda if ebitda and ebitda != 0 else None
    print(f"FY{y}: Raw totalDebt={raw_debt:,.0f}, Adj Debt={adj_debt:,.0f}, EBITDA={ebitda:,.0f}, Debt/EBITDA={ratio:.2f}x")

# ===================
# 6. FCF conversion
# ===================
print("\n" + "="*60)
print("6. FCF CONVERSION (FCF / Net Income)")
print("="*60)
for y in ['2021','2022','2023','2024','2025']:
    fcf = safe(cf_by[y]['freeCashFlow'])
    ni = safe(inc_by[y]['netIncome'])
    conv = fcf / ni if ni and ni != 0 else None
    print(f"FY{y}: FCF={fcf:,.0f}, NI={ni:,.0f}, Conversion={conv:.2%}")

# ===================
# 7. Buyback yield
# ===================
print("\n" + "="*60)
print("7. BUYBACK YIELD (shares repurchased / market cap)")
print("="*60)
for y in ['2024','2025']:
    repurchased = safe(cf_by[y]['commonStockRepurchased'])
    if repurchased and repurchased < 0:
        repurchased = -repurchased
    mktcap = safe(ev_by[y]['marketCapitalization'])
    buyback_yield = repurchased / mktcap if repurchased is not None and mktcap and mktcap != 0 else None
    print(f"FY{y}: Repurchases={repurchased:,.0f}, Market Cap={mktcap:,.0f}, Buyback Yield={buyback_yield:.2%}")

# ===================
# 8. SBC / revenue
# ===================
print("\n" + "="*60)
print("8. SBC DILUTION (stockBasedCompensation / revenue)")
print("="*60)
for y in ['2021','2022','2023','2024','2025']:
    sbc = safe(cf_by[y]['stockBasedCompensation'])
    rev = safe(inc_by[y]['revenue'])
    sbc_rev = sbc / rev if rev and rev != 0 else None
    print(f"FY{y}: SBC={sbc:,.0f}, Revenue={rev:,.0f}, SBC/Revenue={sbc_rev:.2%}")

# ===================
# 9. Correlation: revenue growth vs capex growth (5 years)
# ===================
print("\n" + "="*60)
print("9. CORRELATION: revenue growth vs capex growth")
print("="*60)
years_corr = ['2021','2022','2023','2024','2025']
rev_growths = []
capex_growths = []
for y in years_corr:
    prev = str(int(y)-1)
    rev_g = safe(inc_by[y]['revenue']) / safe(inc_by[prev]['revenue']) - 1
    # capex is negative in cashflow statement; use absolute value for growth
    capex_curr = abs(safe(cf_by[y]['capitalExpenditure']))
    capex_prev = abs(safe(cf_by[prev]['capitalExpenditure']))
    capex_g = capex_curr / capex_prev - 1 if capex_prev != 0 else None
    rev_growths.append(rev_g)
    capex_growths.append(capex_g)
    print(f"FY{y}: Rev growth={rev_g*100:.2f}%, Capex growth={capex_g*100:.2f}%")

# Pearson correlation
n = len(rev_growths)
mean_r = sum(rev_growths)/n
mean_c = sum(capex_growths)/n
num = sum((r - mean_r)*(c - mean_c) for r,c in zip(rev_growths, capex_growths))
den_r = math.sqrt(sum((r - mean_r)**2 for r in rev_growths))
den_c = math.sqrt(sum((c - mean_c)**2 for c in capex_growths))
corr = num / (den_r * den_c) if den_r and den_c else None
print(f"Pearson correlation (5-year annual growth rates) = {corr:.4f}")

# ===================
# 10. EV/Store
# ===================
print("\n" + "="*60)
print("10. EV PER STORE")
print("="*60)
for y in ['2023','2024','2025']:
    enterprise_val = safe(ev_by[y]['enterpriseValue'])
    stores = store_counts[y]
    ev_store = enterprise_val / stores if enterprise_val and stores else None
    print(f"FY{y}: EV={enterprise_val:,.0f}, Stores={stores}, EV/Store=${ev_store:,.0f}")

# ===================
# 11. PEG ratio
# ===================
print("\n" + "="*60)
print("11. PEG RATIO")
print("="*60)
pe = 34.3  # user provided
eps_cagr = cagr(safe(inc_by['2022']['epsDiluted']), safe(inc_by['2025']['epsDiluted']), 3)
peg = pe / (eps_cagr * 100) if eps_cagr else None
print(f"P/E = {pe}, 3-yr EPS CAGR = {eps_cagr*100:.2f}%, PEG = {peg:.2f}")

# ===================
# 12. DCF comment
# ===================
print("\n" + "="*60)
print("12. DCF ASSESSMENT")
print("="*60)
print(f"FMP advanced DCF intrinsic value: ${dcf['dcf']:.2f}")
print(f"FMP listed stock price in DCF file: ${dcf['Stock Price']:.2f}")
print(f"User noted price ~$37.47 (post-split)")
# Let's compute implied share count from DCF details or owner earnings
# TTM net income ~1.536B, FCF ~1.448B. If DCF uses pre-split share count (~27.5M) then per-share value would be much higher.
# Let's check what share count FMP's DCF likely used. We'll need DCF components. The DCF endpoint only returned dcf and Stock Price.
# Let's look at market cap and shares from key_metrics_ttm
mkt_cap = safe(key_ttm['marketCap'])
print(f"Key metrics TTM market cap = {mkt_cap:,.0f}")
# Implied shares at $37.47
shares_at_price = mkt_cap / 37.47
print(f"Implied shares at $37.47 = {shares_at_price:,.0f}")
# FMP enterprise values shares for 2025 = 1,337,336,000
print(f"FMP EV endpoint 2025 shares = {safe(ev_by['2025']['numberOfShares']):,.0f}")
