import json

# ---------------- Load FMP data (all pulled via fmp_call statements/*, saved in data/) ----------------
inc = json.load(open("data/statements_income-statement.json"))   # FY2018-2025
bs  = json.load(open("data/statements_balance-sheet-statement.json"))  # FY2021-2025
cf  = json.load(open("data/statements_cashflow-statement.json")) # FY2016-2025
km  = json.load(open("data/statements_key-metrics.json"))        # FY2016-2025
ar_inc = json.load(open("data/cmg_as_reported_income.json"))     # as-reported FY2023-2025
ar_bs  = json.load(open("data/cmg_as_reported_balance.json"))    # as-reported FY2023-2025

def fy(rows, y):
    r = next((r for r in rows if str(r.get("fiscalYear")) == str(y)), None)
    return r
def g(rows, y, k):
    r = fy(rows, y)
    return None if r is None else r.get(k)
def ar(datalist, y, k):
    r = next((x for x in datalist if str(x.get("fiscalYear")) == str(y)), None)
    return None if (r is None or r.get("data") is None) else r["data"].get(k)

OUT = {}

# =====================================================================
# 1. BENEISH M-SCORE (8-variable), FY2025 vs FY2024 (trend FY2022-25)
# =====================================================================
def beneish(t, t1):
    # t = current FY, t1 = prior FY
    rec_t, rec_p   = g(bs,t,"netReceivables"),      g(bs,t1,"netReceivables")
    rev_t, rev_p   = g(inc,t,"revenue"),            g(inc,t1,"revenue")
    gp_t,  gp_p    = g(inc,t,"grossProfit"),        g(inc,t1,"grossProfit")
    ca_t,  ca_p    = g(bs,t,"totalCurrentAssets"),  g(bs,t1,"totalCurrentAssets")
    ppe_t, ppe_p   = g(bs,t,"propertyPlantEquipmentNet"), g(bs,t1,"propertyPlantEquipmentNet")
    lti_t, lti_p   = g(bs,t,"longTermInvestments"), g(bs,t1,"longTermInvestments")
    ta_t,  ta_p    = g(bs,t,"totalAssets"),         g(bs,t1,"totalAssets")
    da_t,  da_p    = g(inc,t,"depreciationAndAmortization"), g(inc,t1,"depreciationAndAmortization")
    sga_t, sga_p   = g(inc,t,"sellingGeneralAndAdministrativeExpenses"), g(inc,t1,"sellingGeneralAndAdministrativeExpenses")
    ni_t           = g(inc,t,"netIncomeFromContinuingOperations") or g(inc,t,"netIncome")
    cfo_t          = g(cf,t,"netCashProvidedByOperatingActivities")
    tl_t,  tl_p    = g(bs,t,"totalLiabilities"),    g(bs,t1,"totalLiabilities")

    missing = [k for k,v in dict(rec_t=rec_t,rec_p=rec_p,rev_t=rev_t,rev_p=rev_p,gp_t=gp_t,gp_p=gp_p,
        ca_t=ca_t,ca_p=ca_p,ppe_t=ppe_t,ppe_p=ppe_p,lti_t=lti_t,lti_p=lti_p,ta_t=ta_t,ta_p=ta_p,
        da_t=da_t,da_p=da_p,sga_t=sga_t,sga_p=sga_p,ni_t=ni_t,cfo_t=cfo_t,tl_t=tl_t,tl_p=tl_p).items() if v is None]

    dsri = (rec_t/rev_t)/(rec_p/rev_p)
    gmi  = (gp_p/rev_p)/(gp_t/rev_t)
    aqi  = (1-(ca_t+ppe_t+lti_t)/ta_t)/(1-(ca_p+ppe_p+lti_p)/ta_p)
    sgi  = rev_t/rev_p
    depi = (da_p/(da_p+ppe_p))/(da_t/(da_t+ppe_t))
    sgai = (sga_t/rev_t)/(sga_p/rev_p)
    tata = (ni_t-cfo_t)/ta_t
    lvgi = (tl_t/ta_t)/(tl_p/ta_p)
    M = -4.84 + 0.920*dsri + 0.528*gmi + 0.404*aqi + 0.892*sgi + 0.115*depi - 0.172*sgai + 4.679*tata - 0.327*lvgi
    return dict(fiscal_year=t, missing_inputs=missing, DSRI=dsri, GMI=gmi, AQI=aqi, SGI=sgi,
                DEPI=depi, SGAI=sgai, TATA=tata, LVGI=lvgi, M=M,
                inputs=dict(rec_t=rec_t,rec_p=rec_p,rev_t=rev_t,rev_p=rev_p,gp_t=gp_t,gp_p=gp_p,
                            ca_t=ca_t,ppe_t=ppe_t,lti_t=lti_t,ta_t=ta_t,da_t=da_t,da_p=da_p,
                            sga_t=sga_t,sga_p=sga_p,ni_t=ni_t,cfo_t=cfo_t,tl_t=tl_t,tl_p=tl_p,ppe_p=ppe_p))

OUT["beneish"] = {str(y): beneish(y, y-1) for y in (2025, 2024, 2023, 2022)}

# DEPI variant using as-reported PP&E excluding operating-lease ROU assets (FY24/FY25 only)
ppe_ar = {y: ar(ar_bs, y, "propertyplantandequipmentnet") for y in (2024, 2025)}
da  = {y: g(inc, y, "depreciationAndAmortization") for y in (2024, 2025)}
depi_ar = (da[2024]/(da[2024]+ppe_ar[2024]))/(da[2025]/(da[2025]+ppe_ar[2025]))
OUT["beneish"]["2025"]["DEPI_exROU_variant"] = depi_ar

# DSRI variant: trade receivables only (accountsReceivables)
ar25, ar24 = g(bs,2025,"accountsReceivables"), g(bs,2024,"accountsReceivables")
OUT["beneish"]["2025"]["DSRI_trade_AR_only"] = (ar25/g(inc,2025,"revenue"))/(ar24/g(inc,2024,"revenue"))

# =====================================================================
# 2. SLOAN ACCRUALS RATIO, FY2025 & FY2024
# =====================================================================
def sloan(y):
    ni  = g(inc,y,"netIncome")
    cfo = g(cf,y,"netCashProvidedByOperatingActivities")
    ta  = g(bs,y,"totalAssets"); ta_p = g(bs,y-1,"totalAssets")
    avg_ta = (ta+ta_p)/2
    return dict(netIncome=ni, cfo=cfo, ta=y and ta, ta_prior=ta_p, avg_total_assets=avg_ta,
                accruals_ratio=(ni-cfo)/avg_ta)
OUT["sloan"] = {str(y): sloan(y) for y in (2025, 2024)}

# =====================================================================
# 3. DSRI verification vs analyst's observation
# =====================================================================
rec_g = g(bs,2025,"netReceivables")/g(bs,2024,"netReceivables")-1
rev_g = g(inc,2025,"revenue")/g(inc,2024,"revenue")-1
OUT["dsri_check"] = dict(
    receivables_growth=rec_g, revenue_growth=rev_g,
    analyst_claimed=dict(receivables=0.174, revenue=0.054),
    accountsReceivable_growth=g(bs,2025,"accountsReceivables")/g(bs,2024,"accountsReceivables")-1,
    otherReceivables_growth=g(bs,2025,"otherReceivables")/g(bs,2024,"otherReceivables")-1,
    otherReceivables_identity_check=dict(
        std_otherReceivables_FY25=g(bs,2025,"otherReceivables"),
        asreported_incometaxesreceivable_FY25=ar(ar_bs,2025,"incometaxesreceivable")),
    DSRI=OUT["beneish"]["2025"]["DSRI"])

# =====================================================================
# 4. ADJUSTED LEVERAGE
# =====================================================================
ebitda_fmp = g(inc,2025,"ebitda")
ebit_fmp   = g(inc,2025,"operatingIncome")
ebitda_fmp_24 = g(inc,2024,"ebitda")
ebit_fmp_24   = g(inc,2024,"operatingIncome")
# Press-release-consistent operating income (16.2% margin):
#   incomeBeforeTax - interest&other income ; == revenue - as-reported costsandexpenses
ebit_pr  = g(inc,2025,"incomeBeforeTax") - g(inc,2025,"interestIncome")
ebit_pr_check = g(inc,2025,"revenue") - ar(ar_inc,2025,"costsandexpenses")
ebitda_pr = ebit_pr + g(inc,2025,"depreciationAndAmortization")

# debt field mapping vs as-reported tags
map_tbl = dict(
    shortTermDebt_FY25=g(bs,2025,"shortTermDebt"),
    asrep_operatingLeaseLiabilityCurrent_FY25=ar(ar_bs,2025,"operatingleaseliabilitycurrent"),
    longTermDebt_FY25=g(bs,2025,"longTermDebt"),
    asrep_operatingLeaseLiabilityNonCurrent_FY25=ar(ar_bs,2025,"operatingleaseliabilitynoncurrent"),
    capitalLeaseObligations_FY25=g(bs,2025,"capitalLeaseObligations"),
    capitalLeaseObligationsNonCurrent_FY25=g(bs,2025,"capitalLeaseObligationsNonCurrent"),
    totalDebt_FY25=g(bs,2025,"totalDebt"),
    sum_check_STplusLTplusCapLease=g(bs,2025,"shortTermDebt")+g(bs,2025,"longTermDebt")+g(bs,2025,"capitalLeaseObligations"),
    totalDebt_FY24=g(bs,2024,"totalDebt"),
    capLeaseObligations_FY24=g(bs,2024,"capitalLeaseObligations"),
    asrep_lease_liabilities_FY24=ar(ar_bs,2024,"operatingleaseliabilitycurrent")+ar(ar_bs,2024,"operatingleaseliabilitynoncurrent"),
    interestExpense_FY25=g(inc,2025,"interestExpense"), interestPaid_FY25=g(cf,2025,"interestPaid"),
    fmp_interestCoverage_FY25=fy(km,2025).get("interestCoverageRatio") if False else fy(json.load(open("data/statements_metrics-ratios.json")),2025)["interestCoverageRatio"],
)
lease_total_25 = ar(ar_bs,2025,"operatingleaseliabilitycurrent")+ar(ar_bs,2025,"operatingleaseliabilitynoncurrent")
cash = g(bs,2025,"cashAndCashEquivalents"); sti = g(bs,2025,"shortTermInvestments"); lti = g(bs,2025,"longTermInvestments")
ibd = 0.0  # interest-bearing debt excluding operating leases: none exists (see mapping)

netdebt_cash_only   = ibd - cash
netdebt_cash_sti    = ibd - (cash+sti)
netdebt_cash_sti_lti= ibd - (cash+sti+lti)
occ25, occ24 = ar(ar_inc,2025,"occupancynet"), ar(ar_inc,2024,"occupancynet")

OUT["leverage"] = dict(
    field_mapping=map_tbl,
    operating_lease_liabilities_FY25=lease_total_25,
    operating_lease_liabilities_FY24=map_tbl["asrep_lease_liabilities_FY24"],
    ebitda_fmp=ebitda_fmp, ebitda_pressrelease_consistent=ebitda_pr,
    ebit_fmp=ebit_fmp, ebit_pressrelease_consistent=ebit_pr,
    ebit_pr_reconciliation=dict(incomeBeforeTax_minus_interestIncome=ebit_pr,
                                revenue_minus_asrep_costsAndExpenses=ebit_pr_check,
                                margin_check=ebit_pr/g(inc,2025,"revenue")),
    a_interest_bearing_debt_to_ebitda=dict(fmp_ebitda=ibd/ebitda_fmp, pr_ebitda=ibd/ebitda_pr),
    b_interest_bearing_net_debt_to_ebitda=dict(
        cash_only=dict(net_debt=netdebt_cash_only, vs_fmp_ebitda=netdebt_cash_only/ebitda_fmp, vs_pr_ebitda=netdebt_cash_only/ebitda_pr),
        cash_plus_ST_investments=dict(net_debt=netdebt_cash_sti, vs_fmp_ebitda=netdebt_cash_sti/ebitda_fmp, vs_pr_ebitda=netdebt_cash_sti/ebitda_pr),
        cash_plus_ST_plus_LT_investments=dict(net_debt=netdebt_cash_sti_lti, vs_fmp_ebitda=netdebt_cash_sti_lti/ebitda_fmp, vs_pr_ebitda=netdebt_cash_sti_lti/ebitda_pr),
        fmp_published_netDebtToEBITDA=fy(km,2025)["netDebtToEBITDA"]),
    c_rent_adjusted_coverage=dict(
        rent_proxy_occupancy_FY25=occ25, rent_proxy_occupancy_FY24=occ24, interest_expense=0,
        FY25_requested_formula=dict(fmp_ebit=ebit_fmp/(occ25+0), pr_ebit=ebit_pr/(occ25+0)),
        FY25_conventional_EBITRAC=dict(fmp_ebit=(ebit_fmp+occ25)/occ25, pr_ebit=(ebit_pr+occ25)/occ25),
        FY24_requested_formula=dict(fmp_ebit=ebit_fmp_24/occ24),
        FY24_conventional_EBITRAC=dict(fmp_ebit=(ebit_fmp_24+occ24)/occ24)),
    context_lease_adjusted=dict(
        lease_liab_over_ebitdar_fmp=(lease_total_25)/(ebitda_fmp+occ25),
        lease_liab_over_ebitdar_pr=(lease_total_25)/(ebitda_pr+occ25),
        fmp_totalDebt_double_count_excess=g(bs,2025,"totalDebt")-lease_total_25))

# =====================================================================
# 5. EPS GROWTH DECOMPOSITION
# =====================================================================
ni25, ni24 = g(inc,2025,"netIncome"), g(inc,2024,"netIncome")
sh25, sh24 = g(inc,2025,"weightedAverageShsOutDil"), g(inc,2024,"weightedAverageShsOutDil")
eps25, eps24 = g(inc,2025,"epsDiluted"), g(inc,2024,"epsDiluted")
g_eps_printed = eps25/eps24-1
g_eps_exact   = (ni25/sh25)/(ni24/sh24)-1
g_ni   = ni25/ni24-1
g_sh   = sh25/sh24-1
import math
contrib_ni  = math.log(1+g_ni)
contrib_sh  = -math.log(1+g_sh)
OUT["eps_decomposition"] = dict(
    diluted_eps=dict(FY2025=eps25, FY2024=eps24, growth_printed=g_eps_printed, growth_exact=g_eps_exact),
    net_income=dict(FY2025=ni25, FY2024=ni24, growth=g_ni),
    wavg_diluted_shares=dict(FY2025=sh25, FY2024=sh24, growth=g_sh),
    identity_check=(1+g_ni)*(sh24/sh25)-1,
    counterfactual_EPS_FY25_if_share_count_flat=ni25/sh24,
    counterfactual_EPS_FY25_if_net_income_flat=ni24/sh25,
    log_additive_split_pp=dict(net_income_pp=contrib_ni*100, share_reduction_pp=contrib_sh*100,
                               total_pp=(contrib_ni+contrib_sh)*100),
    buyback_context=dict(commonStockRepurchased_FY25=g(cf,2025,"commonStockRepurchased"),
                         commonStockRepurchased_FY24=g(cf,2024,"commonStockRepurchased"),
                         shares_issued_FY25=ar(ar_bs,2025,"commonstocksharesissued"),
                         shares_issued_FY24=ar(ar_bs,2024,"commonstocksharesissued")))

print(json.dumps(OUT, indent=1, default=float))
