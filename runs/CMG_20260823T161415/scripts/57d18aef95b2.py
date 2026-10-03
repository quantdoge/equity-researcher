import json, math
import numpy as np

rows = json.load(open("data/cmg_eod_full.json"))
d = {r["date"]: float(r["close"]) for r in rows if r.get("close") is not None}
dates = sorted(d); P = np.array([d[x] for x in dates])

# last 14 daily deltas (what Cutler RSI sees)
print("last 15 closes:")
for i in range(len(P)-15, len(P)):
    dl = P[i]-P[i-1] if i>0 else float('nan')
    print(f"  {dates[i]}  close={P[i]:6.2f}  delta={dl:+.2f}")

dl = np.diff(P)
last14 = dl[-14:]
g = np.where(last14>0,last14,0.0); l = np.where(last14<0,-last14,0.0)
print(f"last-14d: mean gain={g.mean():.3f} mean loss={l.mean():.3f} -> Cutler RSI={100*g.mean()/(g.mean()+l.mean()):.2f}")

# Wilder avg gain/loss at the end (state of the smoothing)
gA = np.where(dl>0,dl,0.0); lA = np.where(dl<0,-dl,0.0)
ag, al = gA[:14].mean(), lA[:14].mean()
for i in range(14, len(dl)):
    ag = (ag*13+gA[i])/14; al = (al*13+lA[i])/14
print(f"Wilder final: avgGain={ag:.3f} avgLoss={al:.3f} -> RSI={100-100/(1+ag/al):.2f}")

# cross-checks
mom12_1 = P[-1-21]/P[-1-252]-1; mom12 = P[-1]/P[-1-252]-1; last_m = P[-1]/P[-1-21]-1
print(f"\ncheck: (1+mom12_1)*(1+last-month) = {(1+mom12_1)*(1+last_m)-1:+.4f} vs mom12 = {mom12:+.4f}")
print(f"last-month return = {last_m*100:+.2f}%  (explains 12-1 vs 12m gap: stock rallied into t)")
sharpe_chk = (P[-1]/P[-1-252]-1)  # 1y price return context
print(f"1y price return (P_t/P_t-252) = {sharpe_chk*100:+.2f}%  -> negative Sharpe consistent with fall from 43.07 to 36.90")
