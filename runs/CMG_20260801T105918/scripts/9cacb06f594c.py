
import json
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Load price data
cmg_price = json.load(open('data/cmg_price_3y.json'))
sp500_price = json.load(open('data/sp500_price_3y.json'))

# Convert to DataFrames
cmg_df = pd.DataFrame(cmg_price)
sp500_df = pd.DataFrame(sp500_price)

cmg_df['date'] = pd.to_datetime(cmg_df['date'])
sp500_df['date'] = pd.to_datetime(sp500_df['date'])

cmg_df = cmg_df.sort_values('date').reset_index(drop=True)
sp500_df = sp500_df.sort_values('date').reset_index(drop=True)

print(f"CMG price data: {cmg_df['date'].min()} to {cmg_df['date'].max()}, {len(cmg_df)} rows")
print(f"S&P 500 price data: {sp500_df['date'].min()} to {sp500_df['date'].max()}, {len(sp500_df)} rows")

# Compute daily returns
cmg_df['daily_return'] = cmg_df['close'].pct_change()
sp500_df['daily_return'] = sp500_df['close'].pct_change()

# Merge on date
merged = pd.merge(cmg_df[['date','close','daily_return']], sp500_df[['date','close','daily_return']], on='date', suffixes=('_cmg','_sp500'))
merged = merged.dropna()

print(f"Merged data: {len(merged)} rows")
print(f"Latest date: {merged['date'].max()}")

# =============================
# Momentum calculations
# =============================
latest_date = merged['date'].max()

def get_price_on_or_before(df, target_date, price_col='close'):
    mask = df['date'] <= target_date
    if mask.sum() == 0:
        return None
    return df.loc[mask, price_col].iloc[-1]

# 12-month momentum
price_12m_ago = get_price_on_or_before(cmg_df, latest_date - timedelta(days=365))
# 6-month momentum
price_6m_ago = get_price_on_or_before(cmg_df, latest_date - timedelta(days=182))
# 3-month momentum
price_3m_ago = get_price_on_or_before(cmg_df, latest_date - timedelta(days=91))

latest_price = cmg_df['close'].iloc[-1]

mom_12m = (latest_price / price_12m_ago - 1) * 100 if price_12m_ago else None
mom_6m = (latest_price / price_6m_ago - 1) * 100 if price_6m_ago else None
mom_3m = (latest_price / price_3m_ago - 1) * 100 if price_3m_ago else None

print("\n=== PRICE MOMENTUM ===")
print(f"Latest Price ({latest_date.strftime('%Y-%m-%d')}): ${latest_price:.2f}")
print(f"12-month momentum: {mom_12m:.2f}%")
print(f"6-month momentum: {mom_6m:.2f}%")
print(f"3-month momentum: {mom_3m:.2f}%")

# =============================
# Beta vs S&P 500
# =============================
# Use all overlapping daily returns
cmg_returns = merged['daily_return_cmg']
sp500_returns = merged['daily_return_sp500']

covariance = np.cov(cmg_returns, sp500_returns)[0, 1]
sp500_variance = np.var(sp500_returns, ddof=1)
beta = covariance / sp500_variance if sp500_variance != 0 else None

print("\n=== BETA vs S&P 500 ===")
print(f"Beta = {beta:.4f}")

# =============================
# Standard deviation of daily returns (annualized)
# =============================
daily_std = np.std(cmg_returns, ddof=1)
annualized_std = daily_std * np.sqrt(252)

print("\n=== VOLATILITY ===")
print(f"Daily std = {daily_std:.6f}")
print(f"Annualized std = {annualized_std:.4f} ({annualized_std*100:.2f}%)")

# =============================
# Max drawdown (last 2 years)
# =============================
cmg_2y = cmg_df[cmg_df['date'] >= (latest_date - timedelta(days=730))].copy()
cmg_2y = cmg_2y.sort_values('date').reset_index(drop=True)
cmg_2y['cumulative'] = (1 + cmg_2y['daily_return'].fillna(0)).cumprod()
cmg_2y['peak'] = cmg_2y['cumulative'].cummax()
cmg_2y['drawdown'] = (cmg_2y['cumulative'] - cmg_2y['peak']) / cmg_2y['peak']
max_dd = cmg_2y['drawdown'].min()
max_dd_date = cmg_2y.loc[cmg_2y['drawdown'].idxmin(), 'date']

print("\n=== MAX DRAWDOWN (2 years) ===")
print(f"Max Drawdown = {max_dd:.4f} ({max_dd*100:.2f}%)")
print(f"Max Drawdown Date = {max_dd_date.strftime('%Y-%m-%d')}")

# =============================
# Sharpe Ratio
# =============================
# Using 3-month T-bill proxy. Let me search for current rate later.
# For now, compute excess return.
# Annualized return over the period
n_days = len(cmg_df['daily_return'].dropna())
total_return = (cmg_df['close'].iloc[-1] / cmg_df['close'].iloc[0]) - 1
annualized_return = (1 + total_return) ** (252 / n_days) - 1

print("\n=== RETURN METRICS ===")
print(f"Total return over {n_days} trading days: {total_return*100:.2f}%")
print(f"Annualized return: {annualized_return*100:.2f}%")
print(f"Annualized volatility: {annualized_std*100:.2f}%")

# Sharpe will need risk-free rate
print("\n=== SHARPE RATIO ===")
print("Needs risk-free rate (3-month T-bill)")
print(f"If risk-free = 0%, Sharpe = {annualized_return / annualized_std:.4f}")
