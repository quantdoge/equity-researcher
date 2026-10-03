
import json
import numpy as np

# Load data
inc_annual = json.load(open('data/cmg_income_statement_annual_3y.json'))
inc_annual.sort(key=lambda x: x['date'])
bs_q = json.load(open('data/cmg_balance_sheet_12q.json'))
cf_q = json.load(open('data/cmg_cash_flow_12q.json'))
ev_q = json.load(open('data/cmg_enterprise_value_12q.json'))

for stmt in [bs_q, cf_q, ev_q]:
    stmt.sort(key=lambda x: x['date'])

inc_2025 = [r for r in inc_annual if r['date'] == '2025-12-31'][0]
inc_2024 = [r for r in inc_annual if r['date'] == '2024-12-31'][0]
bs_2025 = [r for r in bs_q if r['date'] == '2025-12-31'][0]
bs_2024 = [r for r in bs_q if r['date'] == '2024-12-31'][0]
ev_2025 = [r for r in ev_q if r['date'] == '2025-12-31'][0]

cf_2025_q = [r for r in cf_q if r['date'] in ['2025-03-31','2025-06-30','2025-09-30','2025-12-31']]
cf_2024_q = [r for r in cf_q if r['date'] in ['2024-03-31','2024-06-30','2024-09-30','2024-12-31']]
cf_2025 = {'operatingCashFlow': sum(r.get('operatingCashFlow') or 0 for r in cf_2025_q)}
cf_2024 = {'operatingCashFlow': sum(r.get('operatingCashFlow') or 0 for r in cf_2024_q)}

# Helper to get values
def gv(d, k, default=0.0):
    v = d.get(k)
    return float(v) if v is not None else default

# =============================
# 1. Beneish M-Score
# =============================
# Using annual 2025 (t) and annual 2024 (t-1)

# Revenue
rev_t = gv(inc_2025, 'revenue')
rev_t1 = gv(inc_2024, 'revenue')

# Receivables
rec_t = gv(bs_2025, 'accountsReceivables')
rec_t1 = gv(bs_2024, 'accountsReceivables')

# Gross Profit
GP_t = gv(inc_2025, 'grossProfit')
GP_t1 = gv(inc_2024, 'grossProfit')

# Current Assets, PPE, Total Assets
ca_t = gv(bs_2025, 'totalCurrentAssets')
ca_t1 = gv(bs_2024, 'totalCurrentAssets')
ppe_t = gv(bs_2025, 'propertyPlantEquipmentNet')
ppe_t1 = gv(bs_2024, 'propertyPlantEquipmentNet')
ta_t = gv(bs_2025, 'totalAssets')
ta_t1 = gv(bs_2024, 'totalAssets')

# Depreciation & Amortization
da_t = gv(inc_2025, 'depreciationAndAmortization')
da_t1 = gv(inc_2024, 'depreciationAndAmortization')

# SG&A
sga_t = gv(inc_2025, 'sellingGeneralAndAdministrativeExpenses')
sga_t1 = gv(inc_2024, 'sellingGeneralAndAdministrativeExpenses')

# Total Liabilities
tl_t = gv(bs_2025, 'totalLiabilities')
tl_t1 = gv(bs_2024, 'totalLiabilities')

# Net Income, Operating Cash Flow
ni_t = gv(inc_2025, 'netIncome')
ni_t1 = gv(inc_2024, 'netIncome')
ocf_t = cf_2025['operatingCashFlow']
ocf_t1 = cf_2024['operatingCashFlow']

# Components
DSRI = (rec_t / rev_t) / (rec_t1 / rev_t1) if rec_t1 > 0 and rev_t1 > 0 else 1.0
GMI = ((rev_t1 - (gv(inc_2024, 'costOfRevenue'))) / rev_t1) / ((rev_t - (gv(inc_2025, 'costOfRevenue'))) / rev_t) if rev_t > 0 and rev_t1 > 0 else 1.0
AQI = (1 - (ca_t + ppe_t) / ta_t) / (1 - (ca_t1 + ppe_t1) / ta_t1) if ta_t > 0 and ta_t1 > 0 else 1.0
SGI = rev_t / rev_t1 if rev_t1 > 0 else 1.0
DEPI = (da_t1 / (da_t1 + ppe_t1)) / (da_t / (da_t + ppe_t)) if (da_t1 + ppe_t1) > 0 and (da_t + ppe_t) > 0 else 1.0
SGAI = (sga_t / rev_t) / (sga_t1 / rev_t1) if sga_t1 > 0 and rev_t1 > 0 else 1.0
LVGI = (tl_t / ta_t) / (tl_t1 / ta_t1) if ta_t > 0 and ta_t1 > 0 else 1.0
TATA = (ni_t - ocf_t) / ta_t if ta_t > 0 else 0.0

M_score = -4.84 + 0.92*DSRI + 0.528*GMI + 0.404*AQI + 0.892*SGI + 0.115*DEPI - 0.172*SGAI + 4.679*TATA - 0.327*LVGI

print("=== BENEISH M-SCORE ===")
print(f"DSRI  = {DSRI:.4f}")
print(f"GMI   = {GMI:.4f}")
print(f"AQI   = {AQI:.4f}")
print(f"SGI   = {SGI:.4f}")
print(f"DEPI  = {DEPI:.4f}")
print(f"SGAI  = {SGAI:.4f}")
print(f"LVGI  = {LVGI:.4f}")
print(f"TATA  = {TATA:.4f}")
print(f"M-Score = {M_score:.4f}")

# =============================
# 2. Altman Z-Score
# =============================
# Most recent quarter = 2025 Q4 (annual data as proxy)
wc = gv(bs_2025, 'totalCurrentAssets') - gv(bs_2025, 'totalCurrentLiabilities')
re = gv(bs_2025, 'retainedEarnings')
ebit = gv(inc_2025, 'ebit')
mc = gv(ev_2025, 'marketCapitalization')
tl = gv(bs_2025, 'totalLiabilities')
rev = gv(inc_2025, 'revenue')
ta = gv(bs_2025, 'totalAssets')

X1 = wc / ta
X2 = re / ta
X3 = ebit / ta
X4 = mc / tl
X5 = rev / ta

Z_score = 1.2*X1 + 1.4*X2 + 3.3*X3 + 0.6*X4 + 0.999*X5

print("\n=== ALTMAN Z-SCORE ===")
print(f"X1 (WC/TA)     = {X1:.4f}")
print(f"X2 (RE/TA)     = {X2:.4f}")
print(f"X3 (EBIT/TA)   = {X3:.4f}")
print(f"X4 (MVE/TL)    = {X4:.4f}")
print(f"X5 (Rev/TA)    = {X5:.4f}")
print(f"Z-Score = {Z_score:.4f}")

# Cross-check with FMP
print(f"FMP Altman Z  = {fs[0]['altmanZScore']}")

# =============================
# 3. Piotroski F-Score
# =============================
# Most recent year = 2025 vs 2024
# Profitability (4 points)
f1 = 1 if ni_t > 0 else 0
roa_t = ni_t / ta_t
roa_t1 = ni_t1 / ta_t1
f2 = 1 if roa_t > 0 else 0
f3 = 1 if ocf_t > 0 else 0
f4 = 1 if ocf_t > ni_t else 0

# Leverage/Liquidity/Funding (3 points)
ltdebt_t = gv(bs_2025, 'longTermDebt')
ltdebt_t1 = gv(bs_2024, 'longTermDebt')
# F5: Long-term debt ratio down
f5 = 1 if (ltdebt_t / ta_t) < (ltdebt_t1 / ta_t1) else 0
cr_t = gv(bs_2025, 'totalCurrentAssets') / gv(bs_2025, 'totalCurrentLiabilities')
cr_t1 = gv(bs_2024, 'totalCurrentAssets') / gv(bs_2024, 'totalCurrentLiabilities')
f6 = 1 if cr_t > cr_t1 else 0
shares_t = gv(inc_2025, 'weightedAverageShsOut')
shares_t1 = gv(inc_2024, 'weightedAverageShsOut')
f7 = 1 if shares_t <= shares_t1 else 0

# Efficiency (2 points)
gm_t = GP_t / rev_t
gm_t1 = GP_t1 / rev_t1
f8 = 1 if gm_t > gm_t1 else 0
at_t = rev_t / ta_t
at_t1 = rev_t1 / ta_t1
f9 = 1 if at_t > at_t1 else 0

f_score = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9

print("\n=== PIOTROSKI F-SCORE ===")
print(f"F1 (NI>0)        = {f1}")
print(f"F2 (ROA>0)       = {f2}  (ROA={roa_t:.4f})")
print(f"F3 (OCF>0)       = {f3}")
print(f"F4 (OCF>NI)      = {f4}")
print(f"F5 (LTD/TA down) = {f5}")
print(f"F6 (CR up)       = {f6}  (CR={cr_t:.4f} vs {cr_t1:.4f})")
print(f"F7 (No new eq)   = {f7}  (Shares={shares_t:,.0f} vs {shares_t1:,.0f})")
print(f"F8 (GM up)       = {f8}  (GM={gm_t:.4f} vs {gm_t1:.4f})")
print(f"F9 (AT up)       = {f9}  (AT={at_t:.4f} vs {at_t1:.4f})")
print(f"F-Score = {f_score}/9")

# Cross-check with FMP
print(f"FMP Piotroski F = {fs[0]['piotroskiScore']}")

# =============================
# 4. Accruals Ratio
# =============================
accruals_ratio = (ni_t - ocf_t) / ta_t
print("\n=== ACCRUALS RATIO ===")
print(f"Accruals Ratio = {accruals_ratio:.4f}")

# =============================
# 5. Operating Leverage
# =============================
ebit_t = gv(inc_2025, 'ebit')
ebit_t1 = gv(inc_2024, 'ebit')
rev_t = gv(inc_2025, 'revenue')
rev_t1 = gv(inc_2024, 'revenue')

pct_change_ebit = (ebit_t - ebit_t1) / ebit_t1 if ebit_t1 != 0 else 0
pct_change_rev = (rev_t - rev_t1) / rev_t1 if rev_t1 != 0 else 0

operating_leverage = pct_change_ebit / pct_change_rev if pct_change_rev != 0 else None

print("\n=== OPERATING LEVERAGE ===")
print(f"% Change EBIT   = {pct_change_ebit:.4f}")
print(f"% Change Rev    = {pct_change_rev:.4f}")
print(f"Operating Leverage = {operating_leverage:.4f}")

# =============================
# 6. Financial Leverage
# =============================
fin_leverage = ta_t / gv(bs_2025, 'totalStockholdersEquity') if gv(bs_2025, 'totalStockholdersEquity') != 0 else None
print("\n=== FINANCIAL LEVERAGE ===")
print(f"Financial Leverage = {fin_leverage:.4f}")

# =============================
# 7. Interest Coverage
# =============================
int_exp = gv(inc_2025, 'interestExpense')
if int_exp > 0:
    interest_coverage = ebit_t / int_exp
else:
    interest_coverage = float('inf')
print("\n=== INTEREST COVERAGE ===")
print(f"Interest Expense = {int_exp:,.0f}")
print(f"Interest Coverage = {interest_coverage:.2f}x" if interest_coverage != float('inf') else "Interest Coverage = N/A (no interest expense)")

# =============================
# 8. ROIC
# =============================
# NOPAT = EBIT * (1 - Tax Rate)
# Tax Rate = Income Tax Expense / Income Before Tax
# Invested Capital = Total Equity + Total Debt - Cash & Cash Equivalents
# Also compute using Total Assets - Current Liabilities as alternative

ibt = gv(inc_2025, 'incomeBeforeTax')
tax_exp = gv(inc_2025, 'incomeTaxExpense')
tax_rate = tax_exp / ibt if ibt != 0 else 0
nopat = ebit_t * (1 - tax_rate)

total_debt = gv(bs_2025, 'totalDebt')
cash = gv(bs_2025, 'cashAndCashEquivalents')
total_equity = gv(bs_2025, 'totalStockholdersEquity')

invested_capital_1 = total_equity + total_debt - cash
invested_capital_2 = ta_t - gv(bs_2025, 'totalCurrentLiabilities') + gv(bs_2025, 'shortTermDebt')

roic_1 = nopat / invested_capital_1 if invested_capital_1 != 0 else 0
roic_2 = nopat / invested_capital_2 if invested_capital_2 != 0 else 0

print("\n=== ROIC ===")
print(f"Tax Rate = {tax_rate:.4f}")
print(f"NOPAT = {nopat:,.0f}")
print(f"Invested Capital (Eq + Debt - Cash) = {invested_capital_1:,.0f}")
print(f"ROIC (method 1) = {roic_1:.4f}")
print(f"Invested Capital (TA - CL + STD) = {invested_capital_2:,.0f}")
print(f"ROIC (method 2) = {roic_2:.4f}")

# Also check FMP key metrics
km_2025 = [r for r in km if r['date'] == '2025-12-31'][0]
print(f"FMP ROIC = {km_2025.get('returnOnInvestedCapital')}")
print(f"FMP Invested Capital = {km_2025.get('investedCapital')}")
