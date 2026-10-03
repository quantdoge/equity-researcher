import json, math

def load_eod(name):
    d = json.load(open(f"data/{name}.json"))
    rows = sorted(d, key=lambda r: r["date"])
    return {r["date"]: r for r in rows}

LIME = load_eod("lime_eod"); SPY = load_eod("spy_eod")
LYFT = load_eod("lyft_eod"); UBER = load_eod("uber_eod")

def closes(dm): return {d: r["close"] for d, r in dm.items()}
def series(dm):
    ds = sorted(dm.keys()); return ds, [dm[d] for d in ds]

def logret(cs): return [math.log(cs[i]/cs[i-1]) for i in range(1, len(cs))]
def simpret(cs): return [cs[i]/cs[i-1] - 1 for i in range(1, len(cs))]

def mean(xs): return sum(xs)/len(xs)
def std(xs, ddof=1):
    m = mean(xs); n = len(xs)
    return math.sqrt(sum((x-m)**2 for x in xs)/(n-ddof))
def corr(xs, ys):
    mx, my = mean(xs), mean(ys)
    cov = sum((x-mx)*(y-my) for x, y in zip(xs, ys))/(len(xs)-1)
    return cov/(std(xs)*std(ys))

TD = 252  # trading days per year
out = {}

# ---------- LIME core series ----------
lds, lcl = series(closes(LIME))
n = len(lds)
out["lime_history"] = {
    "n_trading_days": n, "n_return_obs": n-1,
    "first_date": lds[0], "first_close": lcl[0], "first_open": LIME[lds[0]]["open"],
    "last_date": lds[-1], "last_close": lcl[-1],
    "calendar_span_days": (int(lds[-1].replace("-","")) - int(lds[0].replace("-","")))  # rough
}
# calendar span properly
from datetime import date
d0 = date(*map(int, lds[0].split("-"))); d1 = date(*map(int, lds[-1].split("-")))
out["lime_history"]["calendar_span_days"] = (d1-d0).days

last = lcl[-1]
# ---------- 1. Trailing returns ----------
# 1M: 21 trading days back (primary) + calendar anchor 2026-07-21
r_1m_td = last/lcl[-1-21] - 1
cal_anchor = "2026-07-21"
idx_cal = max(i for i,d in enumerate(lds) if d <= cal_anchor)
r_1m_cal = last/lcl[idx_cal] - 1
r_since_ipo_close = last/lcl[0] - 1
r_since_ipo_open  = last/LIME[lds[0]]["open"] - 1
peak_close = max(lcl); peak_date = lds[lcl.index(peak_close)]
out["returns"] = {
    "1M_21tradingdays": {"from_date": lds[-1-21], "from_close": lcl[-1-21], "to_date": lds[-1], "to_close": last, "ret_pct": round(r_1m_td*100,2)},
    "1M_calendar(2026-07-21 anchor)": {"from_date": lds[idx_cal], "from_close": lcl[idx_cal], "ret_pct": round(r_1m_cal*100,2)},
    "3M": "N/A - only 37 trading days of history (~1.7 months)",
    "6M": "N/A", "12M": "N/A",
    "since_IPO_firstdayclose": {"from": f"{lds[0]} close {lcl[0]}", "to": f"{lds[-1]} close {last}", "ret_pct": round(r_since_ipo_close*100,2)},
    "since_IPO_firstdayopen": {"from": f"{lds[0]} open {LIME[lds[0]]['open']}", "ret_pct": round(r_since_ipo_open*100,2)},
    "return_from_peak_close": {"peak_date": peak_date, "peak_close": peak_close, "ret_pct": round((last/peak_close-1)*100,2)}
}

# ---------- 2. Volatility & drawdown ----------
lr = logret(lcl); sr = simpret(lcl)
vol_full = std(lr)*math.sqrt(TD)
# last 21 trading-day window (the only sub-window available; 3M == full history here)
lr_21 = logret(lcl[-22:])
vol_21d = std(lr_21)*math.sqrt(TD)
# max drawdown on closes
mdd, peak_v, peak_d, tr_v, tr_d, cur_peak, cur_pd = 0.0, None, None, None, None, -1e9, None
for d, c in zip(lds, lcl):
    if c > cur_peak: cur_peak, cur_pd = c, d
    dd = c/cur_peak - 1
    if dd < mdd: mdd, peak_v, peak_d, tr_v, tr_d = dd, cur_peak, cur_pd, c, d
# intraday variant using high/low
hi = {d: LIME[d]["high"] for d in lds}; lo = {d: LIME[d]["low"] for d in lds}
mdd_in = 0.0; cp, cpl = -1e9, None; tv=None; td_=None
for d in sorted(lds):
    if hi[d] > cp: cp, cpl = hi[d], d
    dd = lo[d]/cp - 1
    if dd < mdd_in: mdd_in, tv, td_ = dd, lo[d], d
out["vol_drawdown"] = {
    "vol_annualized_full_36obs": round(vol_full*100,2),
    "vol_annualized_last21tradingdays": round(vol_21d*100,2),
    "vol_3M": "N/A - full history (37 days) is shorter than 3 months; equals full-history figure",
    "daily_logret_mean": round(mean(lr)*100,4),
    "max_drawdown_close_based": {"depth_pct": round(mdd*100,2), "peak_date": peak_d, "peak_close": peak_v, "trough_date": tr_d, "trough_close": tr_v},
    "max_drawdown_intraday_low_vs_prior_high": {"depth_pct": round(mdd_in*100,2), "peak_high_date": cpl, "peak_high": cp, "trough_low_date": td_, "trough_low": tv}
}

# ---------- 3. Beta vs SPY ----------
common = sorted(set(LIME) & set(SPY))
cs_l = [LIME[d]["close"] for d in common]; cs_s = [SPY[d]["close"] for d in common]
rl, rs = simpret(cs_l), simpret(cs_s)
xbar, ybar = mean(rs), mean(rl)
sxx = sum((x-xbar)**2 for x in rs); sxy = sum((x-xbar)*(y-ybar) for x,y in zip(rs,rl))
beta = sxy/sxx; alpha_d = ybar - beta*xbar
yhat = [alpha_d + beta*x for x in rs]
sse = sum((y-yh)**2 for y,yh in zip(rl,yhat)); sst = sum((y-ybar)**2 for y in rl)
r2 = 1 - sse/sst
se_beta = math.sqrt((sse/(len(rl)-2))/sxx)
corr_ls = corr(rs, rl)
# log-return variant
ll, ls_ = logret(cs_l), logret(cs_s)
xbar2, ybar2 = mean(ls_), mean(ll)
sxx2 = sum((x-xbar2)**2 for x in ls_); sxy2 = sum((x-xbar2)*(y-ybar2)**2 for x,y in zip(ls_,ll)) if False else sum((x-xbar2)*(y-ybar2) for x,y in zip(ls_,ll))
beta_log = sxy2/sxx2
out["beta_vs_spy"] = {
    "window": f"{common[0]} .. {common[-1]}", "n_pairs": len(rl),
    "beta_simple_returns": round(beta,4), "beta_95CI": [round(beta-1.96*se_beta,4), round(beta+1.96*se_beta,4)],
    "se_beta": round(se_beta,4),
    "alpha_daily_pct": round(alpha_d*100,4), "alpha_annualized_pct": round(alpha_d*TD*100,2),
    "r_squared": round(r2,4), "correlation": round(corr_ls,4),
    "beta_log_returns_variant": round(beta_log,4)
}

# ---------- 4. Correlation matrix ----------
syms = {"LIME": LIME, "LYFT": LYFT, "UBER": UBER, "SPY": SPY}
common4 = sorted(set(LIME))
rets = {}
for s, dm in syms.items():
    cs = [dm[d]["close"] for d in common4]
    rets[s] = simpret(cs)
out["corr_matrix"] = {
    "window": f"{common4[0]} .. {common4[-1]}", "n_obs": len(common4)-1, "return_type": "simple daily",
    "BRDS": "EXCLUDED - no EOD data returned (delisted)",
    "matrix": {a: {b: (1.0 if a==b else round(corr(rets[a], rets[b]),4)) for b in syms} for a in syms}
}

# ---------- 5. Sharpe & Sortino ----------
def sharpe_sortino(cs, rf_annual=0.0):
    lr_ = logret(cs); sr_ = simpret(cs)
    rfd = rf_annual/TD
    ex = [r - rfd for r in lr_]           # excess log return
    ann_mean = mean(ex)*TD
    vol_ = std(lr_)*math.sqrt(TD)
    sharpe = ann_mean/vol_
    dn = [min(r, 0.0) - 0.0 for r in lr_]  # MAR=0 for rf=0; for rf>0 use min(r-rfd,0)
    if rf_annual > 0: dn = [min(r-rfd, 0.0) for r in lr_]
    dd_dev = math.sqrt(sum(x*x for x in dn)/len(dn))*math.sqrt(TD)
    sortino = ann_mean/dd_dev
    return {"ann_ret_log_pct": round(mean(lr_)*TD*100,2), "ann_vol_pct": round(vol_*100,2),
            "sharpe": round(sharpe,3), "ann_downside_dev_pct": round(dd_dev*100,2), "sortino": round(sortino,3),
            "n_obs": len(lr_)}

out["sharpe_sortino"] = {
    "assumption_primary": "risk-free = 0% (proxy per task); annualization 252 days; log returns; downside dev uses all obs, MAR=0",
    "LIME_rf0": sharpe_sortino(lcl, 0.0),
    "LIME_rf4pct_sensitivity": sharpe_sortino(lcl, 0.04),
    "peers_same_window_rf0": {s: sharpe_sortino([syms[s][d]["close"] for d in common4], 0.0) for s in ["LYFT","UBER","SPY"]}
}

# ---------- 6. Cross-sectional ----------
def trailing(cs, days):
    if len(cs) <= days: return None
    return cs[-1]/cs[-1-days] - 1
def ann_vol(cs):
    lr_ = logret(cs); return std(lr_)*math.sqrt(TD)

xsec = {}
for s, dm in syms.items():
    ds_, cs_ = series(closes(dm))
    if s == "LIME":
        m3, m6 = None, None
    else:
        m3, m6 = trailing(cs_, 63), trailing(cs_, 126)
    # common window (LIME life): 2026-07-01 .. 2026-08-21
    ccs = [dm[d]["close"] for d in common4]
    mom_common = ccs[-1]/ccs[0] - 1
    vol_common = ann_vol(ccs)
    # beta over common window
    scs = [SPY[d]["close"] for d in common4]
    a, b = simpret(ccs), simpret(scs)
    xb, yb = mean(b), mean(a)
    sxx_ = sum((x-xb)**2 for x in b); sxy_ = sum((x-xb)*(y-yb) for x,y in zip(b,a))
    xsec[s] = {
        "mom_3M_pct": None if m3 is None else round(m3*100,2),
        "mom_6M_pct": None if m6 is None else round(m6*100,2),
        "mom_common_window_pct": round(mom_common*100,2),
        "vol_common_window_pct": round(vol_common*100,2),
        "beta_common_window": round(sxy_/sxx_,4)
    }
# peers full-history vol (reference)
xsec_refvol = {s: round(ann_vol(series(closes(syms[s]))[1])*100,2) for s in ["LYFT","UBER","SPY"]}

# ranks among LIME/LYFT/UBER (rank 1 = best; momentum: highest; vol: lowest; beta: lowest)
ranks = {}
grp = ["LIME","LYFT","UBER"]
ranks["mom_common_window_rank1_highest"] = sorted(grp, key=lambda s: -xsec[s]["mom_common_window_pct"])
ranks["vol_common_window_rank1_lowest"] = sorted(grp, key=lambda s: xsec[s]["vol_common_window_pct"])
ranks["beta_common_window_rank1_lowest"] = sorted(grp, key=lambda s: xsec[s]["beta_common_window"])
out["cross_sectional"] = {"window": f"{common4[0]}..{common4[-1]} (LIME life; only window where LIME has data)",
    "metrics": xsec, "peers_full_history_vol_pct_410obs": xsec_refvol, "ranks": ranks,
    "note_3M_6M_momentum": "LIME 3M/6M momentum NOT computable (37 trading days); peers shown for reference; common-window momentum used for ranking"}

print(json.dumps(out, indent=1))
