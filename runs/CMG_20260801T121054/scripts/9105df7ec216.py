import json
import pandas as pd
import numpy as np

symbols = ['CMG', 'MCD', 'YUM', 'QSR', 'DRI', 'SBUX']
metrics = {}

for sym in symbols:
    with open(f'data/{sym.lower()}_key_metrics.json') as f:
        data = json.load(f)
    # data might be a list
    if isinstance(data, list):
        data = data[0]
    metrics[sym] = data

# Extract relevant fields
rows = []
for sym in symbols:
    m = metrics[sym]
    rows.append({
        'symbol': sym,
        'earningsYield': m.get('earningsYield'),
        'evToEBITDA': m.get('evToEBITDA'),
        'returnOnInvestedCapital': m.get('returnOnInvestedCapital'),
        'date': m.get('date'),
        'fiscalYear': m.get('fiscalYear')
    })

df = pd.DataFrame(rows)
print("Raw metrics from key-metrics:")
print(df.to_string(index=False))

# Compute P/E = 1/earningsYield (handle None or zero)
df['pe_ratio'] = df['earningsYield'].apply(lambda x: 1/x if x and x > 0 else None)

print("\nComputed P/E ratios:")
print(df[['symbol','pe_ratio']].to_string(index=False))

# Percentile ranks (higher value = higher percentile)
# For P/E: lower is typically "better" in value terms, but percentile rank is just position.
# We'll compute percentile rank such that 100 = highest value in peer set.
from scipy.stats import percentileofscore

def pct_rank(series, symbol, lower_is_better=False):
    val = series[series.index == symbol].values[0]
    if pd.isna(val):
        return None
    if lower_is_better:
        # For lower-is-better, percentile rank = % of peers that are WORSE (higher)
        return percentileofscore(series.dropna().values, val, kind='rank') 
    else:
        return percentileofscore(series.dropna().values, val, kind='rank')

# For standard metrics: higher value = higher percentile
for col in ['pe_ratio', 'evToEBITDA', 'returnOnInvestedCapital']:
    df[f'{col}_pctile'] = None

for col in ['pe_ratio', 'evToEBITDA', 'returnOnInvestedCapital']:
    for sym in df['symbol']:
        idx = df[df['symbol']==sym].index[0]
        val = df.loc[idx, col]
        if pd.notna(val):
            pct = percentileofscore(df[col].dropna().values, val, kind='rank')
            df.loc[idx, f'{col}_pctile'] = pct

print("\nPercentile ranks (0-100, 100=highest value in peer set):")
print(df[['symbol','pe_ratio','pe_ratio_pctile','evToEBITDA','evToEBITDA_pctile','returnOnInvestedCapital','returnOnInvestedCapital_pctile']].to_string(index=False))

# Revenue growth: only available for CMG from financial-statement-growth
with open('data/statements_financial-statement-growth.json') as f:
    cmg_growth = json.load(f)
if isinstance(cmg_growth, list) and len(cmg_growth) > 0:
    latest_cmg_growth = cmg_growth[0]
    cmg_revenue_growth = latest_cmg_growth.get('revenueGrowth')
    print(f"\nCMG revenueGrowth (latest annual): {cmg_revenue_growth}")
else:
    cmg_revenue_growth = None
    print("\nCMG revenueGrowth not available")

# Save cross-sectional ranks
cross_sec = {
    "metrics": df.to_dict(orient='records'),
    "revenue_growth_available": False,
    "note": "Cross-sectional ranks computed over CMG, MCD, YUM, QSR, DRI, SBUX. WING missing due to API limits. Revenue growth unavailable for peers."
}
with open('data/cross_sectional_ranks.json', 'w') as f:
    json.dump(cross_sec, f, indent=2)
print("\nSaved cross-sectional ranks to data/cross_sectional_ranks.json")
