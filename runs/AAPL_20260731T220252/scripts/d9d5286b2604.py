
import json, statistics
rows = json.load(open("data/technicalIndicators_relative-strength-index.json"))
vals = [r["rsi"] for r in rows if r.get("rsi") is not None]
print(json.dumps({"n": len(vals), "mean_rsi": round(statistics.mean(vals), 2), "latest": rows[0]["rsi"]}))
