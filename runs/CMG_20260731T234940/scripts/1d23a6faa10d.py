import json, math
with open('data/cmg_key_metrics_ttm.json') as f:
    key_ttm = json.load(f)[0]
with open('data/cmg_enterprise_values.json') as f:
    ev = sorted(json.load(f), key=lambda x: x['date'])
with open('data/cmg_income_statement.json') as f:
    inc = sorted(json.load(f), key=lambda x: x['fiscalYear'])

# Print key TTM items
print("Key Metrics TTM:")
for k, v in key_ttm.items():
    print(f"  {k}: {v}")

# EV 2025
print("\nEV 2025:")
for k, v in ev[-1].items():
    print(f"  {k}: {v}")
