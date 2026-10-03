import json, math
from collections import defaultdict

def load(p):
    with open("data/"+p) as f:
        return json.load(f)

# ---------- 7. Beta vs SPY ----------
lth = load("chart_historical-price-eod-light.json")
spy = load("data/spy_historical.json") if False else load("spy_historical.json")
lth_d = {r["date"]: r["price"] for r in lth}
spy_d = {r["date"]: r["price"] for r in spy}
common = sorted(set(lth_d) & set(spy_d))
print(f"common trading days: {len(common)} ({common[0]} to {common[-1]})")

def returns(dates, d):
    rets = []
    for i in range(1, len(dates)):
        p0, p1 = d[dates[i-1]], d[dates[i]]
        if p0 and p1: rets.append((dates[i], p1/p0 - 1))
    return dict(rets)

rl, rs = returns(common, lth_d), returns(common, spy_d)
dates_r = sorted(set(rl) & set(rs))
x = [rs[d] for d in dates_r]; y = [rl[d] for d in dates_r]

def stats(x, y):
    n = len(x); mx = sum(x)/n; my = sum(y)/n
    cov = sum((a-mx)*(b-my) for a,b in zip(x,y))/(n-1)
    vx = sum((a-mx)**2 for a in x)/(n-1)
    vy = sum((b-my)**2 for b in y)/(n-1)
    return cov/vx, cov/math.sqrt(vx*vy), math.sqrt(vy)*math.sqrt(252), math.sqrt(vx)*math.sqrt(252)

b_all, c_all, vol_lth, vol_spy = stats(x, y)
# trailing 2y (~504 obs)
b_2y, c_2y, vl_2y, vs_2y = stats(x[-504:], y[-504:])
b_1y, c_1y, vl_1y, vs_1y = stats(x[-252:], y[-252:])
print(f"full period (n={len(x)}): beta={b_all:.2f} corr={c_all:.2f} LTH vol={vol_lth*100:.0f}% SPY vol={vol_spy*100:.0f}%")
print(f"trailing 2y (n=504):     beta={b_2y:.2f} corr={c_2y:.2f} LTH vol={vl_2y*100:.0f}%")
print(f"trailing 1y (n=252):     beta={b_1y:.2f} corr={c_1y:.2f} LTH vol={vl_1y*100:.0f}%")

# ---------- 8. rf, ERP, WACC ----------
tr = load("economics_treasury-rates.json")
rf_row = tr[0]  # file is desc by date; first row = latest
print(f"\ntreasury latest row date: {rf_row['date']}, 10Y = {rf_row['year10']}%, 5Y = {rf_row['year5']}%, 30Y = {rf_row['year30']}%")
rf = rf_row["year10"]/100

erp_rows = [r for r in load("econ_market_risk_premium.json") if r["country"]=="United States"]
print("US ERP row:", erp_rows)
erp = erp_rows[0]["totalEquityRiskPremium"]/100

mcap = 10080367843.0
fin_debt = 31774000 + 1465999000
lease = 83247000 + 2682256000
cash = 223647000
ttm_int_mapped = 51500000  # 51.5M mapped; ~70M normalized (Q4'25 mapped 0)
kd_norm = 70000000/((1507787000+fin_debt)/2)
kd_mapped = ttm_int_mapped/((1507787000+fin_debt)/2)
t_tax = 150300000/565200000

print(f"\nrf(10Y)={rf*100:.2f}%  ERP(US)={erp*100:.2f}%  tax rate TTM={t_tax*100:.1f}%")
print(f"kd: mapped {kd_mapped*100:.2f}%, normalized(~70M int) {kd_norm*100:.2f}%, [FY24 implied: 148.1M/avg 1.55B = 9.5%]")

for beta_used, label in [(b_all, "beta full"), (b_2y, "beta 2y")]:
    ke = rf + beta_used*erp
    for D, dl in [(fin_debt, "fin debt only"), (fin_debt+lease, "incl. leases")]:
        E = mcap
        wacc = E/(E+D)*ke + D/(E+D)*kd_norm*(1-t_tax)
        print(f"WACC [{label}, {dl}]: ke={ke*100:.2f}%  D/(D+E)={D/(E+D)*100:.1f}%  WACC={wacc*100:.2f}%")

ke_base = rf + b_2y*erp
print(f"\nBase case: ke={ke_base*100:.2f}%, WACC(fin)={(mcap/(mcap+fin_debt)*ke_base + fin_debt/(mcap+fin_debt)*kd_norm*(1-t_tax))*100:.2f}%")
