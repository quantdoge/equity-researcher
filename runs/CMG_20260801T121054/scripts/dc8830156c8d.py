import json
import pandas as pd
import numpy as np

# Load technical indicators for CMG
with open('data/technicalIndicators_relative-strength-index.json') as f:
    rsi_data = pd.DataFrame(json.load(f))
with open('data/technicalIndicators_simple-moving-average.json') as f:
    sma_data = pd.DataFrame(json.load(f))
with open('data/technicalIndicators_standard-deviation.json') as f:
    std_data = pd.DataFrame(json.load(f))

rsi_data['date'] = pd.to_datetime(rsi_data['date'])
sma_data['date'] = pd.to_datetime(sma_data['date'])
std_data['date'] = pd.to_datetime(std_data['date'])

latest_rsi = rsi_data.sort_values('date').iloc[-1]
latest_sma = sma_data.sort_values('date').iloc[-1]
latest_std = std_data.sort_values('date').iloc[-1]

print("CMG Technical Indicators (latest):")
print(f"  RSI (latest, {latest_rsi['date'].date()}): {latest_rsi['rsi']:.2f}")
print(f"  SMA (latest, {latest_sma['date'].date()}): {latest_sma['sma']:.2f}")
print(f"  Std Dev (latest, {latest_std['date'].date()}): {latest_std['standardDeviation']:.2f}")

# Load financial scores for CMG
with open('data/cmg_financial_scores.json') as f:
    scores = json.load(f)
if isinstance(scores, list):
    scores = scores[0]
print(f"\nCMG Financial Scores:")
print(f"  Altman Z-Score: {scores['altmanZScore']:.3f}")
print(f"  Piotroski F-Score: {scores['piotroskiScore']}")

# Load cross-sectional ranks
with open('data/cross_sectional_ranks.json') as f:
    cs = json.load(f)
cs_df = pd.DataFrame(cs['metrics'])

# For CMG, compute composite factor scores
cmg_row = cs_df[cs_df['symbol']=='CMG'].iloc[0]

# Value score: average of inverted P/E percentile and inverted EV/EBITDA percentile
# Lower P/E/EV = better value, so use value-oriented percentiles
value_score = (cmg_row['pe_value_pctile'] + cmg_row['ev_ebitda_value_pctile']) / 2

# Quality score: ROIC percentile + Piotroski normalized (0-9 scale -> 0-100)
quality_score = (cmg_row['roic_value_pctile'] + (scores['piotroskiScore'] / 9 * 100)) / 2

# Momentum score: based on 12mo-1mo momentum and recent returns
with open('data/cmg_price_metrics.json') as f:
    pm = json.load(f)
momentum_raw = pm['momentum_12mo_minus_1mo']
# Normalize momentum to 0-100 scale using historical range approx -50% to +50%
momentum_score = max(0, min(100, (momentum_raw + 0.5) / 1.0 * 100))

# Risk score: lower vol = better. Invert vol percentile
vol_full = pm['annualized_vol_full']
# Approximate peer average vol ~25% as median
risk_score = max(0, min(100, (0.40 - vol_full) / 0.40 * 100))

# Overall composite (equal weight: value 25%, quality 25%, momentum 25%, risk 25%)
composite = (value_score + quality_score + momentum_score + risk_score) / 4

print(f"\nCMG Custom Factor Scores:")
print(f"  Value Score (0-100): {value_score:.1f}")
print(f"  Quality Score (0-100): {quality_score:.1f}")
print(f"  Momentum Score (0-100): {momentum_score:.1f}")
print(f"  Risk Score (0-100): {risk_score:.1f}")
print(f"  Composite Score (0-100): {composite:.1f}")

# Altman Z interpretation
if scores['altmanZScore'] > 2.99:
    z_status = "Safe Zone"
elif scores['altmanZScore'] > 1.81:
    z_status = "Grey Zone"
else:
    z_status = "Distress Zone"
print(f"\nAltman Z-Score interpretation: {z_status}")

# Piotroski F interpretation
if scores['piotroskiScore'] >= 7:
    f_status = "Strong"
elif scores['piotroskiScore'] >= 5:
    f_status = "Average"
else:
    f_status = "Weak"
print(f"Piotroski F-Score interpretation: {f_status}")

# Save factor scores
factor_scores = {
    "symbol": "CMG",
    "altman_z_score": scores['altmanZScore'],
    "altman_z_status": z_status,
    "piotroski_f_score": scores['piotroskiScore'],
    "piotroski_f_status": f_status,
    "rsi_latest": latest_rsi['rsi'],
    "sma_latest": latest_sma['sma'],
    "std_dev_latest": latest_std['standardDeviation'],
    "value_score": round(value_score, 2),
    "quality_score": round(quality_score, 2),
    "momentum_score": round(momentum_score, 2),
    "risk_score": round(risk_score, 2),
    "composite_score": round(composite, 2),
    "peer_set": ["CMG", "MCD", "YUM", "QSR", "DRI", "SBUX"],
    "note": "WING excluded due to data unavailability. Revenue growth unavailable for cross-sectional comparison."
}
with open('data/cmg_factor_scores.json', 'w') as f:
    json.dump(factor_scores, f, indent=2)
print("\nSaved factor scores to data/cmg_factor_scores.json")
