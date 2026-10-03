import json
import pandas as pd
import numpy as np

symbols = ['CMG', 'MCD', 'YUM', 'QSR', 'DRI', 'SBUX']
metrics = {}

for sym in symbols:
    with open(f'data/{sym.lower()}_key_metrics.json') as f:
        data = json.load(f)
    if isinstance(data, list):
        data = data[0]
    metrics[sym] = data

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

# Compute P/E = 1/earningsYield
df['pe_ratio'] = df['earningsYield'].apply(lambda x: 1/x if x and x > 0 else None)

# Percentile rank using pandas rank
def compute_pctile(series):
    # rank: 1 = lowest, n = highest
    # percentile = (rank - 1) / (n - 1) * 100
    ranked = series.rank(method='average')
    n = series.count()
    if n <= 1:
        return pd.Series([None]*len(series), index=series.index)
    pct = (ranked - 1) / (n - 1) * 100
    return pct

for col in ['pe_ratio', 'evToEBITDA', 'returnOnInvestedCapital']:
    df[f'{col}_pctile'] = compute_pctile(df[col])

print("Cross-sectional metrics and percentile ranks (0=lowest, 100=highest value in peer set):")
display_cols = ['symbol','pe_ratio','pe_ratio_pctile','evToEBITDA','evToEBITDA_pctile','returnOnInvestedCapital','returnOnInvestedCapital_pctile']
print(df[display_cols].to_string(index=False))

# For value-oriented interpretation, note that lower P/E and lower EV/EBITDA = better value
print("\nValue-oriented ranks (lower = better):")
df['pe_value_rank'] = df['pe_ratio'].rank(ascending=True, method='average')
df['ev_ebitda_value_rank'] = df['evToEBITDA'].rank(ascending=True, method='average')
df['roic_value_rank'] = df['returnOnInvestedCapital'].rank(ascending=False, method='average')
n = len(df)
df['pe_value_pctile'] = (n - df['pe_value_rank'] + 1) / n * 100  # Actually simpler: just use rank ascending pctile
df['ev_ebitda_value_pctile'] = (df['evToEBITDA'].rank(ascending=True, method='average') - 1) / (n - 1) * 100
df['pe_value_pctile'] = (df['pe_ratio'].rank(ascending=True, method='average') - 1) / (n - 1) * 100
df['roic_value_pctile'] = (df['returnOnInvestedCapital'].rank(ascending=False, method='average') - 1) / (n - 1) * 100

print(df[['symbol','pe_value_pctile','ev_ebitda_value_pctile','roic_value_pctile']].to_string(index=False))

# Revenue growth: only for CMG
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
    "metrics": df[['symbol','pe_ratio','pe_ratio_pctile','evToEBITDA','evToEBITDA_pctile','returnOnInvestedCapital','returnOnInvestedCapital_pctile','pe_value_pctile','ev_ebitda_value_pctile','roic_value_pctile']].to_dict(orient='records'),
    "revenue_growth_available": False,
    "note": "Cross-sectional ranks computed over CMG, MCD, YUM, QSR, DRI, SBUX. WING missing due to API limits. Revenue growth unavailable for peers."
}
with open('data/cross_sectional_ranks.json', 'w') as f:
    json.dump(cross_sec, f, indent=2)
print("\nSaved cross-sectional ranks to data/cross_sectional_ranks.json")
