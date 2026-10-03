import json, statistics

# ---------- A. CMG EV / ROIC corrected variants (from on-disk FMP files) ----------
def load(p):
    with open(p) as f: return json.load(f)

is_cmg = load("data/is_cmg.json")
r25 = [r for r in is_cmg if str(r["date"])[:4]=="2025"][0]
r24 = [r for r in is_cmg if str(r["date"])[:4]=="2024"][0]
km25 = [r for r in load("data/statements_key-metrics.json") if str(r["date"])[:4]=="2025"][0]
bs = load("data/bs_cmg.json")
b25 = [r for r in bs if str(r["date"])[:4]=="2025"][0]
b24 = [r for r in bs if str(r["date"])[:4]=="2024"][0]

mc = km25["marketCap"]; ebitda = r25["ebitda"]
leases25 = b25["shortTermDebt"] + b25["capitalLeaseObligationsNonCurrent"]   # 302.4 + 4773.4
leases24 = b24["capitalLeaseObligationsCurrent"] + b24["capitalLeaseObligationsNonCurrent"]
cash_sti25 = b25["cashAndShortTermInvestments"]; ltinv25 = b25["longTermInvestments"]
cash_sti24 = b24["cashAndShortTermInvestments"]; ltinv24 = b24["longTermInvestments"]

ev_lease = mc + leases25 - cash_sti25
ev_classic = mc - cash_sti25 - ltinv25
efftax = r25["incomeTaxExpense"]/r25["incomeBeforeTax"]
nopat = r25["ebit"]*(1-efftax)
ic25 = b25["totalStockholdersEquity"] + leases25 - cash_sti25 - ltinv25
ic24 = b24["totalStockholdersEquity"] + leases24 - cash_sti24 - ltinv24

print("=== CMG EV & ROIC variants (computed) ===")
print(json.dumps({
  "marketCap_FY25end_$B": round(mc/1e9,2),
  "EBITDA_FY25_$M": round(ebitda/1e6,1),
  "FMP_EV_$B": round(km25["enterpriseValue"]/1e9,2), "FMP_EV_over_EBITDA": round(km25["evToEBITDA"],2),
  "FMP_totalDebt_$M": round(b25["totalDebt"]/1e6,1),
  "  of which: shortTermDebt_$M": round(b25["shortTermDebt"]/1e6,1),
  "  of which: longTermDebt_$M": round(b25["longTermDebt"]/1e6,1),
  "  of which: capLeaseNonCurrent_$M": round(b25["capitalLeaseObligationsNonCurrent"]/1e6,1),
  "trueLeaseLiabilities_$M": round(leases25/1e6,1),
  "EV_leaseInclusive_singleCount_$B": round(ev_lease/1e9,2), "EV_over_EBITDA_leaseIncl": round(ev_lease/ebitda,2),
  "EV_classic_noLeases_$B": round(ev_classic/1e9,2), "EV_over_EBITDA_classic": round(ev_classic/ebitda,2),
  "interestExpense_FY25_$M": r25["interestExpense"],
  "NOPAT_$M": round(nopat/1e6,1), "effTaxRate%": round(100*efftax,2),
  "IC_leaseIncl_FY25_$M": round(ic25/1e6,1), "IC_leaseIncl_FY24_$M": round(ic24/1e6,1),
  "ROIC_leaseIncl_EOY%": round(100*nopat/ic25,2),
  "ROIC_leaseIncl_avgIC%": round(100*nopat/((ic25+ic24)/2),2),
  "FMP_ROIC%": round(100*km25["returnOnInvestedCapital"],2),
  "FMP_investedCapital_$M": round(km25["investedCapital"]/1e6,1),
}, indent=1))

# ---------- B. Earnings surprise aggregation (web-retrieved values) ----------
# Each entry: (quarter, eps_surprise%, rev_surprise%, source) -- Q2'24 magnitude not retrievable.
primary = [  # Zacks-syndicated where found, TradingKey otherwise
  ("Q4 2023",  6.47,  0.98, "Zacks via Globes (Feb 2024)"),
  ("Q1 2024", 14.96,  1.01, "Zacks via zacks.com STKS news page"),
  ("Q2 2024", None,  None, "NOT RETRIEVABLE - direction only: EPS beat & revenue beat (Benzinga headline via Wedbush, Zacks blog 7/24/2024)"),
  ("Q3 2024", 12.33, -0.81, "TradingKey earnings history table"),
  ("Q4 2024", -0.52, -0.09, "TradingKey earnings history table"),
  ("Q1 2025",  1.52, -2.51, "TradingKey earnings history table"),
  ("Q2 2025", -0.45, -1.55, "TradingKey earnings history table"),
  ("Q3 2025",  3.57, -0.48, "Zacks via zacks.com PTLO news page (TradingKey alt: +0.01/-0.71)"),
  ("Q4 2025",  4.65,  0.60, "Zacks via zacks.com GENK page & TraderFox (TradingKey alt: +5.16/+0.64)"),
  ("Q1 2026", -1.11,  0.41, "Zacks via TraderFox (TradingKey alt: -2.23/+0.63)"),
  ("Q2 2026",  3.13,  0.81, "Zacks via Yahoo Finance/TradingView/public.com, adj EPS 0.33 vs est 0.32 (TradingKey alt: -1.02/+0.52, GAAP 0.32)"),
]
tk_only = [  # pure TradingKey series, Q3'24-Q2'26
  ("Q3 2024", 12.33, -0.81), ("Q4 2024", -0.52, -0.09), ("Q1 2025", 1.52, -2.51),
  ("Q2 2025", -0.45, -1.55), ("Q3 2025", 0.01, -0.71), ("Q4 2025", 5.16, 0.64),
  ("Q1 2026", -2.23, 0.63), ("Q2 2026", -1.02, 0.52),
]

eps_p = [e for _,e,_,_ in primary if e is not None]
rev_p = [v for _,_,v,_ in primary if v is not None]
eps_t = [e for _,e,_ in tk_only]
rev_t = [v for _,_,v in tk_only]

def stats(name, xs):
    return {f"{name}_n": len(xs), f"{name}_mean%": round(sum(xs)/len(xs),2),
            f"{name}_median%": round(statistics.median(xs),2),
            f"{name}_beatRate": f"{sum(1 for x in xs if x>0)}/{len(xs)}"}

res = {}
res["primary_ZacksPreferred"] = {**stats("EPS", eps_p), **stats("Rev", rev_p),
    "EPS_beats_incl_Q2'24_direction": "8/11 (Q2'24 magnitude unknown, headline says beat)",
    "Rev_beats_incl_Q2'24_direction": "6/11"}
res["tradingKey_only_8q"] = {**stats("EPS", eps_t), **stats("Rev", rev_t)}
print("\n=== CMG earnings surprise aggregation (web sources; FMP calendar/earnings-company NOT retrievable) ===")
print(json.dumps(res, indent=1))
print("\nPer-quarter (primary):")
for q,e,v,s in primary:
    print(f"  {q}: EPS {('%+.2f%%'%e) if e is not None else '  n/a '} | Rev {('%+.2f%%'%v) if v is not None else '  n/a '} | {s}")
