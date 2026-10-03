import json

with open("data/statements_metrics-ratios.json") as f:
    amd_ratios = json.load(f)
    
# Show the latest row
print("Latest AMD metrics-ratios:")
print(json.dumps(amd_ratios[0], indent=2))
