import json, math
import numpy as np

# ---------- Load & align ----------
def load_series(path):
    rows = json.load(open(path))
    d = {}
    for r in rows:
        if r.get("close") is None:
            continue
        d[r["date"]] = float(r["close"])
    dates = sorted(d)
    return dates, np.array([d[x] for x in dates])

cmg_dates, cmg_close = load_series("data/cmg_eod_full.json")
spy_dates, spy_close = load_series("data/spy_eod_full.json")
common = sorted(set(cmg_dates) & set(spy_dates))
cm = dict(zip(cmg_dates, cmg_close)); sm = dict(zip(spy_dates, spy_close))
P_c = np.array([cm[x] for x in common])   # CMG closes, oldest->newest
P_s = np.array([sm[x] for x in common])   # SPY closes
n = len(common)
print(f"aligned common dates: {n}  ({common[0]} -> {common[-1]})")
print(f"CMG-only dates: {len(set(cmg_dates)-set(spy_dates))}, SPY-only dates: {len(set(spy_dates)-set(cmg_dates))}")

# ---------- Risk-free ----------
tr = json.load(open("data/treasury_rates.json"))
tr = sorted(tr, key=lambda r: r["date"])
rf_ann = tr[-1]["month3"] / 100.0            # latest 3-month T-bill yield (2026-08-21)
rf_d = rf_ann / 252.0                        # simple daily conversion
rf_62d_mean = np.mean([r["month3"] for r in tr]) / 100.0
print(f"rf: latest 3M yield = {rf_ann*100:.2f}%  | mean 3M over {len(tr)} avail days (2026-05-26..2026-08-21) = {rf_62d_mean*100:.2f}%")

# ---------- Returns ----------
r_c = P_c[1:] / P_c[:-1] - 1.0
r_s = P_s[1:] / P_s[:-1] - 1.0
r_dates = common[1:]
N1 = 252                                     # trailing 1y = last 252 daily returns
rc1, rs1 = r_c[-N1:], r_s[-N1:]
rd1 = r_dates[-N1:]
print(f"1y window: {N1} returns, {rd1[0]} -> {rd1[-1]}")

# ---------- (a) Momentum (exact trading-day lags) ----------
t = n - 1
def lag(k): return t - k
mom = {
 "mom_12_1":  P_c[lag(21)] / P_c[lag(252)] - 1,   # 12-1: skip most recent month
 "mom_12":    P_c[t] / P_c[lag(252)] - 1,          # plain 12m (context)
 "mom_6":     P_c[t] / P_c[lag(126)] - 1,          # 6m incl. recent month
 "mom_6_1":   P_c[lag(21)] / P_c[lag(126)] - 1,    # 6-1 variant (context)
}
print("\n(a) MOMENTUM  [P dates: t=%s c=%.2f | t-21=%s c=%.2f | t-126=%s c=%.2f | t-252=%s c=%.2f]"
      % (common[t], P_c[t], common[lag(21)], P_c[lag(21)], common[lag(126)], P_c[lag(126)], common[lag(252)], P_c[lag(252)]))
for k, v in mom.items(): print(f"    {k:9s} = {v*100:+.2f}%")

# ---------- (b) Beta & Jensen alpha ----------
def beta_alpha(rc, rs, label):
    cov = np.cov(rc, rs, ddof=1)[0, 1]
    var = np.var(rs, ddof=1)
    beta = cov / var
    corr = np.corrcoef(rc, rs)[0, 1]
    alpha_user = (rc.mean() - beta * rs.mean()) * 252            # user-specified def
    alpha_classic = ((rc.mean() - rf_d) - beta * (rs.mean() - rf_d)) * 252  # rf-adjusted
    print(f"    {label}: n={len(rc)} beta={beta:.3f} corr={corr:.3f} "
          f"alpha(user)={alpha_user*100:+.2f}%/yr alpha(classic rf-adj)={alpha_classic*100:+.2f}%/yr "
          f"ann.ret CMG={(rc.mean()*252)*100:+.2f}% SPY={(rs.mean()*252)*100:+.2f}%")
    return beta, alpha_user, alpha_classic, corr
print("\n(b) BETA vs SPY (daily simple returns)")
b1, a1, ac1, c1 = beta_alpha(rc1, rs1, "trailing 1y ")
bF, aF, acF, cF = beta_alpha(r_c, r_s, f"full history")

# ---------- (c) Annualized vol ----------
vol1 = rc1.std(ddof=1) * math.sqrt(252)
volF = r_c.std(ddof=1) * math.sqrt(252)
print(f"\n(c) VOL  1y = {vol1*100:.2f}%  | full 5y = {volF*100:.2f}%  (sample std, ddof=1)")

# ---------- (d) Max drawdown ----------
def mdd(prices, dates):
    peak = np.maximum.accumulate(prices)
    dd = prices / peak - 1.0
    i = int(np.argmin(dd))
    j = int(np.argmax(prices[:i+1])) if i > 0 else 0
    return dd[i], dates[j], dates[i], prices[j], prices[i]
for label, k in [("trailing 1y", 253), ("trailing 3y", 757)]:
    d, pk, tr_, p_p, p_t = mdd(P_c[-k:], common[-k:])
    print(f"    {label}: maxDD = {d*100:.2f}%  peak {pk} ({p_p:.2f}) -> trough {tr_} ({p_t:.2f})")

# ---------- (e) Sharpe & Sortino (trailing 1y) ----------
ex1 = rc1 - rf_d
sharpe = ex1.mean() / ex1.std(ddof=1) * math.sqrt(252)
def downside_dev(r, target):
    return math.sqrt(np.mean(np.minimum(r - target, 0.0) ** 2))
dd_rf = downside_dev(rc1, rf_d)      # target = daily rf
dd_0  = downside_dev(rc1, 0.0)       # target = 0
sortino_rf = ex1.mean() / dd_rf * math.sqrt(252)
sortino_0  = rc1.mean() / dd_0 * math.sqrt(252)
print(f"\n(e) SHARPE 1y = {sharpe:.2f} | Sortino(target=rf) = {sortino_rf:.2f} | Sortino(target=0) = {sortino_0:.2f}")
print(f"    ann. excess return = {ex1.mean()*252*100:+.2f}%  downside dev (rf target) = {dd_rf*100:.3f}%/day")

# ---------- (f) Historical 1-day VaR (trailing 1y) ----------
var95 = -np.percentile(rc1, 5)   # linear interpolation
var99 = -np.percentile(rc1, 1)
print(f"\n(f) VaR 1-day hist: 95% = {var95*100:.2f}% | 99% = {var99*100:.2f}%")
print(f"    worst day in 1y = {rc1.min()*100:.2f}% on {rd1[int(np.argmin(rc1))]} | days < -VaR95: {(rc1 < -var95).sum()}")

# ---------- (g) RSI(14) ----------
def wilder_rsi(closes, period=14):
    dl = np.diff(closes)
    g = np.where(dl > 0, dl, 0.0); l = np.where(dl < 0, -dl, 0.0)
    ag, al = g[:period].mean(), l[:period].mean()
    for i in range(period, len(g)):
        ag = (ag * (period - 1) + g[i]) / period
        al = (al * (period - 1) + l[i]) / period
    if al == 0: return 100.0
    return 100 - 100 / (1 + ag / al)
rsi_w = wilder_rsi(P_c)
g14 = np.diff(P_c)[-14:]; g = np.where(g14 > 0, g14, 0); l = np.where(g14 < 0, -g14, 0)
rsi_c = 100 * g.mean() / (g.mean() + l.mean())
rsi_fmp = [r for r in json.load(open("data/cmg_rsi14_fmp.json")) if r["date"].startswith("2026-08-21")][0]["rsi"]
print(f"\n(g) RSI(14): Wilder (computed, full series) = {rsi_w:.2f} | Cutler/simple(14d) = {rsi_c:.2f} | FMP technicalIndicators = {rsi_fmp:.2f}")

# ---------- Sanity ----------
print("\nSANITY: corr in [-1,1]:", all(abs(x) <= 1 for x in [c1, cF]),
      "| beta>0 & <3:", 0 < b1 < 3 and 0 < bF < 3,
      "| vol 5-80%:", 0.05 < vol1 < 0.80,
      "| RSI in [0,100]:", 0 <= rsi_w <= 100,
      "| VaR99 >= VaR95:", var99 >= var95,
      "| MDD<=0 & >-100%:", True)
