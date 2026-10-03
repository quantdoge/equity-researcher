import json, statistics

def load(p):
    with open(p) as f: return json.load(f)

SYMS = ["CMG","CAVA","SHAK","WING","TXRH","MCD","YUM","DPZ"]
is_ = {s: load(f"data/is_{s.lower()}.json") for s in SYMS}

def fy(rows, year):
    for r in rows:
        if str(r.get("fiscalYear")) == str(year):
            return r
    for r in rows:  # fallback: match on date year
        if str(r.get("date",""))[:4] == str(year):
            return r
    return None

out = {}

# ---------- SECTION 1: cross-sectional FY2025 ----------
cross = {}
nulls = []
for s in SYMS:
    r25, r24 = fy(is_[s], 2025), fy(is_[s], 2024)
    for fld in ["revenue","grossProfit","operatingIncome","netIncome","ebitda","ebit"]:
        if r25.get(fld) is None or r24.get("revenue") is None:
            nulls.append(f"{s} FY2025 {fld} is None")
    cross[s] = {
        "fyEnd25": r25["date"], "fyEnd24": r24["date"],
        "rev25_$M": round(r25["revenue"]/1e6,1), "rev24_$M": round(r24["revenue"]/1e6,1),
        "grossMargin%": round(100*r25["grossProfit"]/r25["revenue"],2),
        "opMargin%": round(100*r25["operatingIncome"]/r25["revenue"],2),
        "netMargin%": round(100*r25["netIncome"]/r25["revenue"],2),
        "ebitMargin%": round(100*r25["ebit"]/r25["revenue"],2),
        "revGrowth%": round(100*(r25["revenue"]/r24["revenue"]-1),2),
    }
out["crossSectional_FY2025"] = cross

def rank_higher(metric):
    vals = [(cross[s][metric], s) for s in SYMS]
    vals.sort(reverse=True)
    return {s: i+1 for i,(v,s) in enumerate(vals)}

ranks = {}
for m in ["grossMargin%","opMargin%","netMargin%","revGrowth%"]:
    r = rank_higher(m)
    ranks[m] = {"CMG_rank": r["CMG"], "order_best_to_worst": [s for _,s in sorted([(v,k) for k,v in r.items()])]}
med = {}
for m in ["grossMargin%","opMargin%","netMargin%","revGrowth%"]:
    vals8 = [cross[s][m] for s in SYMS]
    vals7 = [cross[s][m] for s in SYMS if s!="CMG"]
    med[m] = {"median_all8": round(statistics.median(vals8),2), "median_exCMG": round(statistics.median(vals7),2)}
out["ranks_and_medians"] = {"ranks": ranks, "medians": med}
out["nulls_encountered"] = nulls

# ---------- SECTION 2: CMG margin trend FY2021-2025 ----------
cmg_is = is_["CMG"]
mr = load("data/statements_metrics-ratios.json")
mr_by_year = {str(r["fiscalYear"]): r for r in mr}
trend = []
for y in [2021,2022,2023,2024,2025]:
    r = fy(cmg_is, y)
    trend.append({
        "FY": y,
        "revenue_$M": round(r["revenue"]/1e6,1),
        "grossMargin%": round(100*r["grossProfit"]/r["revenue"],2),
        "opMargin%": round(100*r["operatingIncome"]/r["revenue"],2),
        "netMargin%": round(100*r["netIncome"]/r["revenue"],2),
        "FMP_ratios_grossMargin%": round(100*mr_by_year[str(y)]["grossProfitMargin"],2),
        "FMP_ratios_opMargin%": round(100*mr_by_year[str(y)]["operatingProfitMargin"],2),
        "FMP_ratios_netMargin%": round(100*mr_by_year[str(y)]["netProfitMargin"],2),
    })
out["cmg_margin_trend"] = trend

# ---------- SECTION 3: CMG revenue CAGR + reconciliation ----------
r19, r25, r24 = fy(cmg_is,2019), fy(cmg_is,2025), fy(cmg_is,2024)
cagr = (r25["revenue"]/r19["revenue"])**(1/6)-1
growth25 = r25["revenue"]/r24["revenue"]-1
asrep = load("data/cmg_as_reported_income.json")
asrep25row = [r for r in asrep if str(r.get("date",""))[:4]=="2025"]
asrep25 = asrep25row[0]["data"].get("revenues") if asrep25row else "row not found"
fsg = load("data/statements_financial-statement-growth.json")
fsg25 = [r for r in fsg if str(r.get("date",""))[:4]=="2025"][0]
out["cmg_revenue"] = {
    "FY2019_rev_$M": round(r19["revenue"]/1e6,1),
    "FY2025_rev_$M": round(r25["revenue"]/1e6,1),
    "CAGR_2019_2025_%": round(100*cagr,2),
    "growth_FY2025_%": round(100*growth25,2),
    "FMP_growth_file_%": round(100*fsg25["revenueGrowth"],2),
    "asReported_10k_revenues_$": asrep25,
    "FMP_minus_11930M_$M": round(r25["revenue"]/1e6 - 11930,1),
    "FMP_vs_11.93B_diff_%": round(100*(r25["revenue"]/1.193e10-1),3),
}

# ---------- SECTION 4: Rule of 40 ----------
cf = load("data/statements_cashflow-statement.json")
cf25 = [r for r in cf if str(r.get("date",""))[:4]=="2025"][0]
cf24 = [r for r in cf if str(r.get("date",""))[:4]=="2024"][0]
def r40(cfr, rev):
    ocf, capex = cfr["operatingCashFlow"], cfr["capitalExpenditure"]
    fcf = ocf - abs(capex)
    return {"OCF_$M": round(ocf/1e6,1), "capex_$M": round(abs(capex)/1e6,1),
            "FCF_computed_$M": round(fcf/1e6,1), "FCF_field_$M": round(cfr["freeCashFlow"]/1e6,1),
            "FCF_margin%": round(100*fcf/rev,2)}
g24 = fy(cmg_is,2024)["revenue"]/fy(cmg_is,2023)["revenue"]-1
out["rule_of_40"] = {
    "FY2025": {"revGrowth%": round(100*growth25,2), **r40(cf25, r25["revenue"]),
               "Rule_of_40": round(100*growth25 + 100*(cf25["operatingCashFlow"]-abs(cf25["capitalExpenditure"]))/r25["revenue"],2)},
    "FY2024_context": {"revGrowth%": round(100*g24,2), **r40(cf24, fy(cmg_is,2024)["revenue"]),
                       "Rule_of_40": round(100*g24 + 100*(cf24["operatingCashFlow"]-abs(cf24["capitalExpenditure"]))/fy(cmg_is,2024)["revenue"],2)},
}

# ---------- SECTION 5: AUV ----------
out["cmg_AUV"] = {"revenue_$M": round(r25["revenue"]/1e6,1), "units": 4056,
                  "AUV_$M_per_unit": round(r25["revenue"]/4056/1e6,4),
                  "AUV_$_per_unit": round(r25["revenue"]/4056,0)}

# ---------- CMG multiples & ROIC ----------
km = load("data/statements_key-metrics.json")
km25 = [r for r in km if str(r.get("date",""))[:4]=="2025"][0]
mr25 = mr_by_year["2025"]
bs = load("data/bs_cmg.json")
bs25 = [r for r in bs if str(r.get("date",""))[:4]=="2025"][0]
eff_tax = r25["incomeTaxExpense"]/r25["incomeBeforeTax"]
nopat = r25["ebit"]*(1-eff_tax)
ic_simple = bs25["totalDebt"] + bs25["totalStockholdersEquity"] - bs25["cashAndShortTermInvestments"]
lease_tot = (bs25.get("capitalLeaseObligationsCurrent") or 0) + (bs25.get("capitalLeaseObligationsNonCurrent") or 0)
ic_lease = ic_simple + lease_tot
ev_alt = km25["marketCap"] + bs25["totalDebt"] - bs25["cashAndShortTermInvestments"]

px = sorted(load("data/cmg_eod_full.json"), key=lambda r: r["date"])
px_by_date = {r["date"]: r["close"] for r in px}
ye25 = px_by_date.get("2025-12-31")
latest = px[-1]
out["cmg_multiples_FY2025TTM"] = {
    "FMP_key_metrics_FY2025": {"evToEBITDA": round(km25["evToEBITDA"],2), "marketCap_$B": round(km25["marketCap"]/1e9,2),
                        "enterpriseValue_$B": round(km25["enterpriseValue"]/1e9,2),
                        "returnOnInvestedCapital%": round(100*km25["returnOnInvestedCapital"],2),
                        "returnOnCapitalEmployed%": round(100*km25["returnOnCapitalEmployed"],2),
                        "investedCapital_$M": round(km25["investedCapital"]/1e6,1)},
    "FMP_metrics_ratios_FY2025": {"PE": round(mr25["priceToEarningsRatio"],2),
                           "enterpriseValueMultiple_EV_EBITDA": round(mr25["enterpriseValueMultiple"],2),
                           "netProfitMargin%": round(100*mr25["netProfitMargin"],2)},
    "computed_ROIC": {"formula": "EBIT*(1 - incomeTaxExpense/incomeBeforeTax) / (totalDebt + totalStockholdersEquity - cashAndShortTermInvestments)",
                      "EBIT_$M": round(r25["ebit"]/1e6,1), "effTaxRate%": round(100*eff_tax,2),
                      "NOPAT_$M": round(nopat/1e6,1),
                      "IC_exLease_$M": round(ic_simple/1e6,1), "ROIC_exLease%": round(100*nopat/ic_simple,2),
                      "leaseObligations_$M": round(lease_tot/1e6,1),
                      "IC_inclLeases_$M": round(ic_lease/1e6,1), "ROIC_inclLeases%": round(100*nopat/ic_lease,2),
                      "FMP_investedCapital_$M": round(km25["investedCapital"]/1e6,1)},
    "EV_decomposition": {"EV_minus_marketCap_$B": round((km25["enterpriseValue"]-km25["marketCap"])/1e9,2),
                         "BS_totalDebt_$M": round(bs25["totalDebt"]/1e6,1), "BS_netDebt_$M": round(bs25["netDebt"]/1e6,1),
                         "BS_cash&STI_$M": round(bs25["cashAndShortTermInvestments"]/1e6,1),
                         "BS_equity_$M": round(bs25["totalStockholdersEquity"]/1e6,1),
                         "EV_alt_simple_$B": round(ev_alt/1e9,2),
                         "EV_alt_over_EBITDA": round(ev_alt/r25["ebitda"],2),
                         "EBITDA_IS_$M": round(r25["ebitda"]/1e6,1)},
    "price_crosschecks": {"close_2025_12_31": ye25, "close_latest_date": latest["date"], "close_latest": latest["close"],
                          "PE_check_ye25close_over_epsDiluted": round(ye25/r25["epsDiluted"],2),
                          "PE_check_ye25close_over_epsBasic": round(ye25/r25["eps"],2),
                          "PE_mixedperiod_latestPrice_over_FY2025_epsDiluted": round(latest["close"]/r25["epsDiluted"],2),
                          "FY2025_epsDiluted": r25["epsDiluted"]},
}

# ---------- CAVA computed ROIC ----------
bsc = load("data/bs_cava.json")
bsc25 = [r for r in bsc if str(r.get("date",""))[:4]=="2025"][0]
c25 = fy(is_["CAVA"], 2025)
c_eff_tax = c25["incomeTaxExpense"]/c25["incomeBeforeTax"]
c_nopat = c25["ebit"]*(1-c_eff_tax)
c_ic = bsc25["totalDebt"] + bsc25["totalStockholdersEquity"] - bsc25["cashAndShortTermInvestments"]
out["cava_computed_ROIC"] = {"formula": "EBIT*(1-effTax)/(totalDebt+equity-cash&STI)",
                             "NOPAT_$M": round(c_nopat/1e6,1), "IC_$M": round(c_ic/1e6,1),
                             "ROIC%": round(100*c_nopat/c_ic,2) if c_ic and c_ic>0 else "IC<=0 or missing, not meaningful"}

# ---------- cross-checks ----------
txrh_g = load("data/statements_income-statement-growth.json")
txrh25 = [r for r in txrh_g if str(r.get("date",""))[:4]=="2025"][0]
out["crosschecks"] = {
    "TXRH_growth_computed_vs_FMP": [cross["TXRH"]["revGrowth%"], round(100*txrh25["growthRevenue"],2)],
    "CMG_growth_computed_vs_FMP": [cross["CMG"]["revGrowth%"], round(100*fsg25["revenueGrowth"],2)],
    "CMG_FCF_computed_vs_FMP_field_$M": [round((cf25["operatingCashFlow"]-abs(cf25["capitalExpenditure"]))/1e6,1), round(cf25["freeCashFlow"]/1e6,1)],
    "CMG_FY2025_margins_IS_vs_FMP_ratios": {
        "gross": [cross["CMG"]["grossMargin%"], round(100*mr25["grossProfitMargin"],2)],
        "op": [cross["CMG"]["opMargin%"], round(100*mr25["operatingProfitMargin"],2)],
        "net": [cross["CMG"]["netMargin%"], round(100*mr25["netProfitMargin"],2)]},
}

print(json.dumps(out, indent=1))
