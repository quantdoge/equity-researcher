import json, os
with open('data/cmg_dcf.json') as f:
    dcf = json.load(f)
print(json.dumps(dcf, indent=2))