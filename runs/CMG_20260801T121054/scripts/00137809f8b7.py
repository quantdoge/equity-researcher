import json
import pandas as pd
with open('data/economics_treasury-rates.json') as f:
    tr = json.load(f)
tr_df = pd.DataFrame(tr)
print("Treasury rate date range:", tr_df['date'].min(), "to", tr_df['date'].max())
mask = tr_df['date'] <= '2025-05-30'
if mask.any():
    closest = tr_df[mask].iloc[-1]
    print("Closest treasury rate before 2025-05-30:", closest.to_dict())
else:
    print("No treasury rate before 2025-05-30")
    print("First available:", tr_df.iloc[0].to_dict())
