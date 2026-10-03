import json, math
d = json.load(open("data/lime_eod.json"))
rows = sorted(d, key=lambda r: r["date"])
ds = [r["date"] for r in rows]; cl = [r["close"] for r in rows]
hi = [r["high"] for r in rows]; lo = [r["low"] for r in rows]

# --- intraday max drawdown with CORRECT peak-at-trough labels ---
mdd, cp, cpl, tv, td_, peak_at_trough, peak_at_trough_date = 0.0, -1e9, None, None, None, None, None
cur_peak, cur_pd = -1e9, None
for i in range(len(ds)):
    if hi[i] > cur_peak: cur_peak, cur_pd = hi[i], ds[i]
    dd = lo[i]/cur_peak - 1
    if dd < mdd:
        mdd, tv, td_ = dd, lo[i], ds[i]
        peak_at_trough, peak_at_trough_date = cur_peak, cur_pd
print("INTRADAY MDD (low vs running max of daily highs):")
print(f"  depth {mdd*100:.2f}% | peak high {peak_at_trough} on {peak_at_trough_date} -> trough low {tv} on {td_}")

# --- daily return extremes ---
rets = [(ds[i], cl[i]/cl[i-1]-1) for i in range(1,len(cl))]
best = max(rets, key=lambda x: x[1]); worst = min(rets, key=lambda x: x[1])
neg = sum(1 for _,r in rets if r < 0)
print(f"\nBest day:  {best[0]} {best[1]*100:+.2f}%")
print(f"Worst day: {worst[0]} {worst[1]*100:+.2f}%")
print(f"Up days: {len(rets)-neg}/{len(rets)} ({(len(rets)-neg)/len(rets)*100:.1f}%)")

# --- arithmetic annualized return since IPO (compound) ---
n_ret = len(rets)
tot = cl[-1]/cl[0]-1
ann = (cl[-1]/cl[0])**(252/n_ret)-1
print(f"\nSince-IPO total: {tot*100:.2f}% over {n_ret} trading days ({(int(ds[-1].replace('-',''))-int(ds[0].replace('-','')))} cal days approx)")
print(f"Compound-annualized (252d): {ann*100:.1f}%  [extrapolation of a 36-day window - not meaningful]")

# --- verify 1M return both ways ---
print(f"\n1M (21td): {cl[-22]} -> {cl[-1]} = {(cl[-1]/cl[-22]-1)*100:.2f}%")
i21 = max(i for i,x in enumerate(ds) if x <= "2026-07-21")
print(f"1M (cal anchor 2026-07-21, close {cl[i21]}): {(cl[-1]/cl[i21]-1)*100:.2f}%")

# --- sanity: corr(x,x)=1 in matrix, betas via corr*vol ratio ---
# (quick numeric cross-check of beta identity for LIME)
import math as m
def sd(xs):
    mu=sum(xs)/len(xs); return m.sqrt(sum((x-mu)**2 for x in xs)/(len(xs)-1))
sl=[cl[i]/cl[i-1]-1 for i in range(1,len(cl))]
spy=json.load(open("data/spy_eod.json")); srows={r["date"]:r["close"] for r in spy}
sc=[srows[x] for x in ds]; ss=[sc[i]/sc[i-1]-1 for i in range(1,len(sc))]
cov=sum((a-sum(sl)/len(sl))*(b-sum(ss)/len(ss)) for a,b in zip(sl,ss))/(len(sl)-1)
print(f"\nbeta check LIME: cov/var = {cov/(sd(ss)**2):.4f}")
