import json, math, datetime as dt

def load(p):
    with open(p) as f: return json.load(f)

inc  = {r["date"][:4]: r for r in load("data/statements_income-statement.json")}   # FY2018-2025
bal  = {r["date"][:4]: r for r in load("data/lth_balance_annual.json")}             # FY2020-2025
cf   = {r["date"][:4]: r for r in load("data/lth_cashflow_annual.json")}            # FY2020-2025
km   = {r["date"][:4]: r for r in load("data/lth_key_metrics_annual.json")}
rat  = {r["date"][:4]: r for r in load("data/lth_ratios_annual.json")}
evf  = {r["date"][:4]: r for r in load("data/lth_enterprise_values.json")}

# ---------- A. Annual fundamental series ----------
years = ["2020","2021","2022","2023","2024","2025"]
series = {}
prev_assets = prev_equity = None
for y in years:
    i, b, c = inc[y], bal[y], cf[y]
    rev, ebitda, ebit, ni = i["revenue"], i["ebitda"], i["ebit"], i["netIncome"]
    ocf, capex, fcf = c["operatingCashFlow"], c["capitalExpenditure"], c["freeCashFlow"]
    ta, eq, nd, td = b["totalAssets"], b["totalStockholdersEquity"], b["netDebt"], b["totalDebt"]
    row = {
        "revenue": rev, "grossMargin": i["grossProfit"]/rev, "ebitdaMargin": ebitda/rev,
        "ebitMargin": ebit/rev, "netMargin": ni/rev, "epsDiluted": i["epsDiluted"],
        "ocf": ocf, "capex": capex, "fcf": fcf, "fcfMargin": fcf/rev, "ocfMargin": ocf/rev,
        "ocfToNI": (ocf/ni) if ni else None,
        "totalDebt": td, "netDebt": nd, "equity": eq, "totalAssets": ta,
        "netDebtToEbitda": (nd/ebitda) if ebitda and ebitda>0 else None,
        "interestCoverage": (ebit/i["interestExpense"]) if i.get("interestExpense") else None,
        "sharesDil": i["weightedAverageShsOutDil"], "revPerShare": rev/i["weightedAverageShsOutDil"],
    }
    if prev_assets:
        row["accrualsRatio"] = (ni - ocf)/((ta+prev_assets)/2)
        row["roeAvgEquity"]  = ni/((eq+prev_equity)/2)
        row["roaAvgAssets"]  = ni/((ta+prev_assets)/2)
        row["assetTurnover"] = rev/((ta+prev_assets)/2)
    prev_assets, prev_equity = ta, eq
    series[y] = row

# pre-COVID income-only rows
pre = {y: {"revenue": inc[y]["revenue"], "ebitda": inc[y]["ebitda"], "netIncome": inc[y]["netIncome"],
           "epsDiluted": inc[y]["epsDiluted"]} for y in ["2018","2019"]}

def cagr(a, b, n): return (b/a)**(1/n) - 1
cagrs = {
    "rev_2019_2025_6y": cagr(pre["2019"]["revenue"], inc["2025"]["revenue"], 6),
    "rev_2021_2025_4y": cagr(inc["2021"]["revenue"], inc["2025"]["revenue"], 4),
    "ebitda_2022_2025_3y": cagr(inc["2022"]["ebitda"], inc["2025"]["ebitda"], 3),
    "ni_2023_2025_2y": cagr(inc["2023"]["netIncome"], inc["2025"]["netIncome"], 2),
    "revPerShare_2021_2025_4y": cagr(series["2021"]["revPerShare"], series["2025"]["revPerShare"], 4),
}

# cross-checks: my growth vs FMP growth file + FMP margins vs computed
grw = {r["date"][:4]: r for r in load("data/statements_financial-statement-growth.json")}
xcheck = {}
for y in ["2021","2022","2023","2024","2025"]:
    mine = inc[y]["revenue"]/inc[str(int(y)-1)]["revenue"] - 1
    xcheck[y] = {"myRevGrowth": mine, "fmpRevGrowth": grw[y]["revenueGrowth"],
                 "match": abs(mine - grw[y]["revenueGrowth"]) < 1e-9}
margin_xcheck = {y: {"myGross": series[y]["grossMargin"], "fmpGross": rat[y]["grossProfitMargin"],
                     "myEbitda": series[y]["ebitdaMargin"], "fmpEbitda": rat[y]["ebitdaMargin"],
                     "myNet": series[y]["netMargin"], "fmpNet": rat[y]["netProfitMargin"]} for y in years}

# accounting identity checks
ident = {y: {"assets_eq_liab_equity": bal[y]["totalAssets"] == bal[y]["totalLiabilities"] + bal[y]["totalStockholdersEquity"],
             "totalDebt_components": bal[y]["shortTermDebt"] + bal[y]["longTermDebt"] + bal[y]["capitalLeaseObligationsNonCurrent"]}
         for y in years}

# FY2025 balance-sheet vs cash-flow debt reconciliation (flag)
b25, c25 = bal["2025"], cf["2025"]
debt_recon = {
    "ltDebt_2024": bal["2024"]["longTermDebt"], "ltDebt_2025": b25["longTermDebt"],
    "ltDebt_change": b25["longTermDebt"] - bal["2024"]["longTermDebt"],
    "otherNonCurrLiab_2024": bal["2024"]["otherNonCurrentLiabilities"], "otherNonCurrLiab_2025": b25["otherNonCurrentLiabilities"],
    "cf_netDebtIssuance_2025": c25["netDebtIssuance"],
    "interestExpense_2024": inc["2024"]["interestExpense"], "interestExpense_2025": inc["2025"]["interestExpense"],
}

# ---------- B. Current valuation (quote 2026-08-21) ----------
q_price, q_mcap = 45.11, 10080367843.0
rev25, ebitda25, ni25, ocf25 = inc["2025"]["revenue"], inc["2025"]["ebitda"], inc["2025"]["netIncome"], cf["2025"]["operatingCashFlow"]
eq25, td25, cash25 = bal["2025"]["totalStockholdersEquity"], b25["totalDebt"], b25["cashAndCashEquivalents"]
ev_now = q_mcap + td25 - cash25
# sensitivity: if CF statement (net issuance -20.4M) is right and the +2.53B LT-debt jump is a reclassification artifact
lt_alt = bal["2024"]["longTermDebt"] + c25["netDebtIssuance"]
td_alt = b25["shortTermDebt"] + lt_alt + b25["capitalLeaseObligationsNonCurrent"]
ev_alt = q_mcap + td_alt - cash25
valuation = {
    "asOf": "2026-08-21 close", "price": q_price, "marketCap": q_mcap,
    "pe_diluted_FY25": q_price/inc["2025"]["epsDiluted"],
    "ps_FY25": q_mcap/rev25, "pb_FY25": q_mcap/eq25, "pocf_FY25": q_mcap/ocf25,
    "ev_FY25debt": ev_now, "evEbitda_FY25": ev_now/ebitda25,
    "evEbitda_sensitivity_debtPerCFstmt": ev_alt/ebitda25,
    "netDebtEbitda_reported": b25["netDebt"]/ebitda25,
    "netDebtEbitda_sensitivity": (td_alt - cash25)/ebitda25,
    "fmp_FYend_multiples_123125": {"price": evf["2025"]["stockPrice"], "pe": rat["2025"]["priceToEarningsRatio"],
        "ps": rat["2025"]["priceToSalesRatio"], "pb": rat["2025"]["priceToBookRatio"], "evEbitda": km["2025"]["evToEBITDA"]},
    "price_change_since_FY25_end": q_price/evf["2025"]["stockPrice"] - 1,
}

# DuPont FY2025 (avg balance sheet)
nm = ni25/rev25; at = rev25/((bal["2025"]["totalAssets"]+bal["2024"]["totalAssets"])/2)
em = ((bal["2025"]["totalAssets"]+bal["2024"]["totalAssets"])/2)/((eq25+bal["2024"]["totalStockholdersEquity"])/2)
dupont = {"netMargin": nm, "assetTurnover_avg": at, "equityMultiplier_avg": em,
          "roe_avg_equity": nm*at*em, "roe_ending_equity_FMP": km["2025"]["returnOnEquity"]}

# ---------- C. Price analytics from daily closes ----------
rows = load("data/chart_historical-price-eod-light.json")
rows.sort(key=lambda r: r["date"])
dates = [dt.date.fromisoformat(r["date"]) for r in rows]
px = [r["price"] for r in rows]; vol = [r["volume"] for r in rows]
n = len(px)
rets = [math.log(px[i]/px[i-1]) for i in range(1, n)]

def ret_over(ndays):
    if n-1-ndays < 0: return None
    return px[-1]/px[-1-ndays] - 1

cummax = peak = None; maxdd = 0; dd_date = None
peak = px[0]
for i,p in enumerate(px):
    if p > peak: peak = p
    dd = p/peak - 1
    if dd < maxdd: maxdd, dd_date = dd, dates[i].isoformat()

def wilder_rsi(closes, period=14):
    deltas = [closes[i]-closes[i-1] for i in range(1, len(closes))]
    if len(deltas) < period: return None
    ag = sum(max(d,0) for d in deltas[:period])/period
    al = sum(max(-d,0) for d in deltas[:period])/period
    for d in deltas[period:]:
        ag = (ag*(period-1) + max(d,0))/period
        al = (al*(period-1) + max(-d,0))/period
    if al == 0: return 100.0
    return 100 - 100/(1 + ag/al)

mean = sum(rets)/len(rets)
var  = sum((r-mean)**2 for r in rets)/(len(rets)-1)
m3 = sum((r-mean)**3 for r in rets)/len(rets); m4 = sum((r-mean)**4 for r in rets)/len(rets)
last252 = rets[-251:]
m2a = sum((r-sum(last252)/len(last252))**2 for r in last252)/(len(last252)-1)
yr_ago_price = px[-1-252]
last252c = px[-252:]

# FY-end close cross-check vs EV file
fyend_check = {y: {"ev_file_price": evf[y]["stockPrice"]} for y in ["2021","2022","2023","2024","2025"]}
for y in fyend_check:
    tgt = dt.date(int(y), 12, 31)
    best = min(range(n), key=lambda i: abs((dates[i]-tgt).days))
    fyend_check[y]["chart_close_nearest"] = px[best]
    fyend_check[y]["nearest_date"] = dates[best].isoformat()

price_analytics = {
    "first_close_2021_10_07": px[0], "last_close": px[-1], "n_days": n,
    "return_since_ipo": px[-1]/px[0]-1,
    "cagr_since_ipo": (px[-1]/px[0])**(365.25/(dates[-1]-dates[0]).days)-1,
    "ret_1m": ret_over(21), "ret_3m": ret_over(63), "ret_6m": ret_over(126), "ret_1y": ret_over(252),
    "ytd_2026": (px[-1]/[p for d,p in zip(dates,px) if d.year==2025][-1])-1 if any(d.year==2025 for d in dates) else None,
    "ann_vol_full": math.sqrt(var*252), "ann_vol_trailing1y": math.sqrt(m2a*252),
    "daily_ret_mean": mean, "daily_ret_std": math.sqrt(var),
    "skew": m3/var**1.5, "excess_kurtosis": m4/var**2 - 3,
    "up_day_fraction": sum(1 for r in rets if r>0)/len(rets),
    "best_day": max(rets), "worst_day": min(rets),
    "max_drawdown_close": maxdd, "max_dd_date": dd_date,
    "sma50": sum(px[-50:])/50, "sma200": sum(px[-200:])/200,
    "price_vs_sma50_pct": px[-1]/(sum(px[-50:])/50)-1, "price_vs_sma200_pct": px[-1]/(sum(px[-200:])/200)-1,
    "rsi14_wilder_computed": wilder_rsi(px),
    "hi_52w_close": max(last252c), "lo_52w_close": min(last252c),
    "pct_below_52w_high_close": px[-1]/max(last252c)-1,
    "avg_vol_30d": sum(vol[-30:])/30, "avg_vol_full": sum(vol)/len(vol),
    "quote_check_priceAvg50": 41.755, "quote_check_priceAvg200": 31.50465,
    "quote_52w_high_low": [47.235, 24.14], "beta_profile": 1.498,
    "fyend_close_crosscheck": fyend_check,
}

# ---------- D. Scores + context ----------
scores = {"altmanZ": 1.8117242555523103, "piotroskiF": 7,
          "note": "financial-scores row carries revenue 3,182.4M and totalAssets 8,358.2M - both differ from FY2025 annuals (2,995.3M / 8,789.6M), consistent with a TTM/latest-quarter basis (~mid-2026); quarterly statements unavailable to verify (fmp_call limit)."}
treasury = load("data/economics_treasury-rates.json")[-1]
context = {"treasury_asof": treasury["date"], "ust3m": treasury["month3"], "ust10y": treasury["year10"],
           "earnings_yield_FY25_at_current_price": 1/valuation["pe_diluted_FY25"],
           "earnings_yield_FY25_at_FYend_price": km["2025"]["earningsYield"]}

out = {"preCOVID_income": pre, "annual_series": series, "cagrs": cagrs,
       "growth_crosscheck": xcheck, "margin_crosscheck": margin_xcheck, "identity_checks": ident,
       "fy25_debt_reconciliation_flags": debt_recon,
       "valuation": valuation, "dupont_FY25": dupont, "price_analytics": price_analytics,
       "scores": scores, "macro_context": context}

with open("lth_baseline_summary.json", "w") as f:
    json.dump(out, f, indent=1, default=str)
print(json.dumps(out, indent=1, default=str))
