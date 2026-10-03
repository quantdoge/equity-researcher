src = open("lime_valuation.py").read()
assert 'int(s*100)' in src
src = src.replace('int(s*100)', 'round(s*100)')
open("lime_valuation.py", "w").write(src)
ns = {}
exec(src, ns)
print(json.dumps(ns["out"]["5_implied_sam_$M"]) if False else ns["out"]["5_implied_sam_$M"])
import json; print(json.dumps(ns["out"]["7_dcf_primary"]["base A ($103.8M) | WACC 10.0%"]["iv_per_share_$"]))