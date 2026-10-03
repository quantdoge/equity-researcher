import json

with open("data/amd_financial_scores.json") as f:
    amd_fs = json.load(f)
    
with open("data/amd_key_metrics_a.json") as f:
    amd_km = json.load(f)
    
print("AMD Financial Scores:", json.dumps(amd_fs, indent=2))
print("\nAMD Key Metrics latest:")
for row in amd_km:
    if row.get("fiscalYear") == "2025":
        print(json.dumps(row, indent=2))
