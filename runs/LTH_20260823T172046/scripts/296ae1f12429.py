import json, datetime

def peek(path):
    with open(path) as f:
        d = json.load(f)
    if isinstance(d, dict):
        d = d.get("data", d)
    print(f"--- {path}: {len(d)} rows ---")
    return d

# 1. Reused chart file - is it LTH? what range?
ch = peek("data/chart_historical-price-eod-light.json")
print("first:", ch[0])
print("last :", ch[-1])
print("symbols:", set(r.get("symbol") for r in ch))
print("null prices:", sum(1 for r in ch if r.get("price") is None))

# 2. Reused 8-row income statement - annual or quarterly?
inc8 = peek("data/statements_income-statement.json")
for r in inc8:
    print(r.get("date"), r.get("period"), "FY" if r.get("period")=="FY" else "", 
          "rev:", r.get("revenue"), "ni:", r.get("netIncome"), "epsDil:", r.get("epsDiluted"), "ebitda:", r.get("ebitda"))

# 3. Reused growth file (8 rows)
g8 = peek("data/statements_financial-statement-growth.json")
for r in g8:
    print(r.get("date"), r.get("period"), "revGrow:", r.get("revenueGrowth"), "ebitdaGrow:", r.get("ebitdaGrowth"))

# 4. Treasury rates - latest row
tr = peek("data/economics_treasury-rates.json")
print("last treasury row:", tr[-1])

# 5. My annual files - date ranges
for p in ["data/lth_income_annual.json","data/lth_balance_annual.json","data/lth_cashflow_annual.json",
          "data/lth_key_metrics_annual.json","data/lth_ratios_annual.json","data/lth_income_growth_annual.json",
          "data/lth_enterprise_values.json"]:
    d = peek(p)
    print(p, "->", [r.get("date") for r in d])
