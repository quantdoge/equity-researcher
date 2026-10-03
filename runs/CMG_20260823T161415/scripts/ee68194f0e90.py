import json, os

def load(p):
    with open(p) as f:
        return json.load(f)

base = "data"
print("=== A. Pre-existing statements_* files: symbols & coverage ===")
for fn in ["statements_cashflow-statement.json", "statements_key-metrics.json",
           "statements_metrics-ratios.json", "statements_balance-sheet-statement.json",
           "statements_income-statement.json", "statements_income-statement-growth.json",
           "statements_financial-statement-growth.json"]:
    p = os.path.join(base, fn)
    if not os.path.exists(p):
        print(fn, "MISSING"); continue
    d = load(p)
    syms = sorted(set(r.get("symbol","?") for r in d))
    dates = [r.get("date","?") for r in d]
    print(f"{fn}: rows={len(d)} symbols={syms} dates={sorted(dates, reverse=True)[:12]}")

print()
print("=== B. Cashflow detail (if CMG): date, OCF, capex, FCF ===")
cf = load("data/statements_cashflow-statement.json")
for r in cf:
    print(r.get("symbol"), r.get("date"), "OCF=", r.get("operatingCashFlow"), "capex=", r.get("capitalExpenditure"), "FCF=", r.get("freeCashFlow"), "netCashOps=", r.get("netCashProvidedByOperatingActivities"))

print()
print("=== C. Key-metrics detail: date, evToEBITDA, marketCap, EV, ROIC, ROCE, investedCapital ===")
km = load("data/statements_key-metrics.json")
for r in km:
    print(r.get("symbol"), r.get("date"), "evToEBITDA=", r.get("evToEBITDA"), "mktCap=", r.get("marketCap"),
          "EV=", r.get("enterpriseValue"), "ROIC=", r.get("returnOnInvestedCapital"),
          "ROCE=", r.get("returnOnCapitalEmployed"), "invCap=", r.get("investedCapital"))

print()
print("=== D. Metrics-ratios detail: date, PE, EV/EBITDA (enterpriseValueMultiple), margins, effTax ===")
mr = load("data/statements_metrics-ratios.json")
for r in mr:
    print(r.get("symbol"), r.get("date"), "PE=", r.get("priceToEarningsRatio"),
          "EVMult=", r.get("enterpriseValueMultiple"), "netMgn=", r.get("netProfitMargin"),
          "grossMgn=", r.get("grossProfitMargin"), "opMgn=", r.get("operatingProfitMargin"),
          "effTax=", r.get("effectiveTaxRate"))

print()
print("=== E. Screener file: does it contain our 8 symbols? ===")
sc = load("data/search_search-company-screener.json")
want = {"CMG","CAVA","SHAK","WING","TXRH","MCD","YUM","DPZ"}
rows = {r["symbol"]: r for r in sc if r.get("symbol") in want}
print("screener rows:", len(sc), "| matched:", sorted(rows.keys()))
for s, r in sorted(rows.items()):
    print(s, "| name:", r.get("companyName"), "| price:", r.get("price"), "| mktCap:", r.get("marketCap"), "| industry:", r.get("industry"))
print("all screener symbols:", sorted(set(r["symbol"] for r in sc))[:60])

print()
print("=== F. Price files: latest close ===")
for fn in ["cmg_eod_full.json", "cmg_price_full.json", "chart_historical-price-eod-full.json",
           "spy_eod_full.json", "spy_price_full.json"]:
    d = load("data/"+fn)
    d2 = sorted(d, key=lambda r: r["date"])
    print(fn, "rows:", len(d), "first:", d2[0]["date"], "last:", d2[-1]["date"], "lastClose:", d2[-1]["close"], "symbol:", d2[-1].get("symbol"))

print()
print("=== G. Growth files latest rows ===")
for fn in ["statements_income-statement-growth.json", "statements_financial-statement-growth.json"]:
    d = load("data/"+fn)
    for r in d[:3]:
        print(fn.split("_")[1], r.get("symbol"), r.get("date"), "revGrowth=", r.get("growthRevenue", r.get("revenueGrowth")))

print()
print("=== H. As-reported files structure ===")
for fn in ["cmg_as_reported_income.json", "cmg_as_reported_balance.json"]:
    d = load("data/"+fn)
    r0 = d[0]
    print(fn, "rows:", len(d), "dates:", [r.get("date") for r in d], "| data keys sample:", list(r0.get("data", {}).keys())[:8] if isinstance(r0.get("data"), dict) else type(r0.get("data")))

print()
print("=== I. News headlines (may contain earnings info) ===")
for fn in ["news_stock-news.json", "news_search-stock-news.json"]:
    d = load("data/"+fn)
    print(f"--- {fn} ({len(d)} rows) ---")
    for r in d:
        print(" ", r.get("publishedDate"), "|", r.get("publisher"), "|", (r.get("title") or "")[:110])

print()
print("=== J. Other files: symbols ===")
for fn in ["secFilings_search-by-symbol.json", "insiderTrades_insider-trade-statistics.json",
           "insiderTrades_search-insider-trades.json", "senate_house-trading.json"]:
    d = load("data/"+fn)
    syms = sorted(set(str(r.get("symbol","?")) for r in d))
    print(fn, "rows:", len(d), "symbols:", syms[:12])
sf = load("data/secFilings_search-by-symbol.json")
print("recent CMG filings:", [(r["formType"], r["filingDate"]) for r in sf[:8]])

print()
print("=== K. Error file ===")
print(load("data/cmg_10k_2025.json"))
