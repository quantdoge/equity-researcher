import json
import math
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Load CMG prices
with open('data/cmg_prices.json') as f:
    cmg_raw = json.load(f)
cmg = pd.DataFrame(cmg_raw)
cmg['date'] = pd.to_datetime(cmg['date'])
cmg = cmg.sort_values('date').reset_index(drop=True)

# Load SPY prices
with open('data/spy_prices.json') as f:
    spy_raw = json.load(f)
spy = pd.DataFrame(spy_raw)
spy['date'] = pd.to_datetime(spy['date'])
spy = spy.sort_values('date').reset_index(drop=True)

# Compute log returns
cmg['log_return'] = np.log(cmg['close'] / cmg['close'].shift(1))
spy['log_return'] = np.log(spy['close'] / spy['close'].shift(1))

# Ensure same dates for correlation
merged = pd.merge(cmg[['date','log_return']], spy[['date','log_return']], on='date', suffixes=('_cmg','_spy'))
merged = merged.dropna()

print(f"CMG price data: {len(cmg)} rows from {cmg['date'].min().date()} to {cmg['date'].max().date()}")
print(f"SPY price data: {len(spy)} rows from {spy['date'].min().date()} to {spy['date'].max().date()}")
print(f"Overlapping returns: {len(merged)} rows")

# 30-day, 90-day, 1-year realized volatility (annualized)
# Use trading days ~252/year
latest_date = cmg['date'].max()
vol_30 = cmg[cmg['date'] > latest_date - timedelta(days=45)]['log_return'].std() * math.sqrt(252)
vol_90 = cmg[cmg['date'] > latest_date - timedelta(days=120)]['log_return'].std() * math.sqrt(252)
vol_1yr = cmg[cmg['date'] > latest_date - timedelta(days=400)]['log_return'].std() * math.sqrt(252)

print(f"\nRealized Volatility (annualized):")
print(f"  30-day: {vol_30:.4f} ({vol_30*100:.2f}%)")
print(f"  90-day: {vol_90:.4f} ({vol_90*100:.2f}%)")
print(f"  1-year: {vol_1yr:.4f} ({vol_1yr*100:.2f}%)")

# Max drawdown from 52-week high
year_ago = latest_date - timedelta(days=365)
cmg_1yr = cmg[cmg['date'] >= year_ago].copy()
if len(cmg_1yr) > 0:
    cmg_1yr['cummax'] = cmg_1yr['close'].cummax()
    cmg_1yr['drawdown'] = (cmg_1yr['close'] - cmg_1yr['cummax']) / cmg_1yr['cummax']
    max_drawdown = cmg_1yr['drawdown'].min()
    print(f"\nMax drawdown from 52-week high: {max_drawdown:.4f} ({max_drawdown*100:.2f}%)")
else:
    max_drawdown = None
    print("Not enough data for 52-week max drawdown")

# 12-month minus 1-month momentum return
price_12m_ago = cmg[cmg['date'] <= latest_date - timedelta(days=360)]['close'].iloc[-1] if any(cmg['date'] <= latest_date - timedelta(days=360)) else None
price_1m_ago = cmg[cmg['date'] <= latest_date - timedelta(days=28)]['close'].iloc[-1] if any(cmg['date'] <= latest_date - timedelta(days=28)) else None
price_now = cmg['close'].iloc[-1]

if price_12m_ago is not None and price_1m_ago is not None:
    ret_12m = price_now / price_12m_ago - 1
    ret_1m = price_now / price_1m_ago - 1
    momentum = ret_12m - ret_1m
    print(f"\nMomentum (12mo - 1mo return):")
    print(f"  12-month return: {ret_12m:.4f} ({ret_12m*100:.2f}%)")
    print(f"  1-month return: {ret_1m:.4f} ({ret_1m*100:.2f}%)")
    print(f"  12mo - 1mo momentum: {momentum:.4f} ({momentum*100:.2f}%)")
else:
    momentum = None
    print("Not enough data for momentum calculation")

# Sharpe ratio using 3-month Treasury rate as risk-free proxy
with open('data/economics_treasury-rates.json') as f:
    tr = json.load(f)
treasury_df = pd.DataFrame(tr)
treasury_df['date'] = pd.to_datetime(treasury_df['date'])
latest_treasury = treasury_df.sort_values('date').iloc[-1]
rf_annual = latest_treasury['month3'] / 100  # 3-month rate
print(f"\nRisk-free rate (3-month Treasury, {latest_treasury['date'].date()}): {rf_annual*100:.2f}%")

# Sharpe over the full sample (~1 year)
avg_daily_return = cmg['log_return'].mean()
annualized_return = avg_daily_return * 252
annualized_vol = cmg['log_return'].std() * math.sqrt(252)
sharpe = (annualized_return - rf_annual) / annualized_vol if annualized_vol > 0 else None
print(f"Annualized return (log, full sample): {annualized_return:.4f} ({annualized_return*100:.2f}%)")
print(f"Annualized vol (full sample): {annualized_vol:.4f} ({annualized_vol*100:.2f}%)")
print(f"Sharpe ratio: {sharpe:.4f}")

# CMG-SPY correlation of daily log returns
corr = merged['log_return_cmg'].corr(merged['log_return_spy'])
print(f"\nCMG-SPY daily log return correlation: {corr:.4f}")

# Also compute beta
merged['spy_log_return_sq'] = merged['log_return_spy'] ** 2
cov = merged['log_return_cmg'].cov(merged['log_return_spy'])
var_spy = merged['log_return_spy'].var()
beta = cov / var_spy if var_spy > 0 else None
print(f"CMG beta (to SPY, daily log returns): {beta:.4f}")

# Save price metrics
price_metrics = {
    "symbol": "CMG",
    "latest_date": str(latest_date.date()),
    "realized_vol_30d": round(vol_30, 6),
    "realized_vol_90d": round(vol_90, 6),
    "realized_vol_1yr": round(vol_1yr, 6),
    "max_drawdown_52wk": round(max_drawdown, 6) if max_drawdown is not None else None,
    "momentum_12mo_minus_1mo": round(momentum, 6) if momentum is not None else None,
    "sharpe_ratio": round(sharpe, 6) if sharpe is not None else None,
    "annualized_return": round(annualized_return, 6),
    "annualized_vol_full": round(annualized_vol, 6),
    "risk_free_3m_treasury": round(rf_annual, 6),
    "cmg_spy_correlation": round(corr, 6),
    "cmg_beta_spy": round(beta, 6),
    "price_data_start": str(cmg['date'].min().date()),
    "price_data_end": str(cmg['date'].max().date()),
    "n_observations": len(cmg),
    "trading_days_overlap_with_spy": len(merged)
}
with open('data/cmg_price_metrics.json', 'w') as f:
    json.dump(price_metrics, f, indent=2)
print("\nSaved price metrics to data/cmg_price_metrics.json")
