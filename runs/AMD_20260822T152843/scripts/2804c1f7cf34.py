import json
import statistics

# ==============================
# Load all data
# ==============================
with open("data/amd_balance_sheet.json") as f:
    bs = {row["fiscalYear"]: row for row in json.load(f)}

with open("data/statements_income-statement.json") as f:
    inc = {row["fiscalYear"]: row for row in json.load(f)}

with open("data/statements_cashflow-statement.json") as f:
    cf = {row["fiscalYear"]: row for row in json.load(f)}

with open("data/amd_key_metrics_a.json") as f:
    amd_km = {row["fiscalYear"]: row for row in json.load(f)}

with open("data/statements_metrics-ratios.json") as f:
    amd_mr = {row["fiscalYear"]: row for row in json.load(f)}

with open("data/amd_financial_scores.json") as f:
    amd_fs = json.load(f)[0]

# Peer data
peers = {}
for sym in ["nvda", "intc", "qcom"]:
    with open(f"data/{sym}_key_metrics.json") as f:
        km = json.load(f)[0]
    with open(f"data/{sym}_metrics_ratios.json") as f:
        mr = json.load(f)[0]
    with open(f"data/{sym}_financial_scores.json") as f:
        fs = json.load(f)[0]
    peers[sym.upper()] = {"km": km, "mr": mr, "fs": fs}

# Helper to get values safely
def get(d, key, scale=1.0):
    v = d.get(key)
    if v is None:
        return None
    return float(v) / scale

# ==============================
# 1. Beneish M-Score FY2025
# ==============================
t = "2025"
t1 = "2024"

# Inputs
rev_t = get(inc[t], "revenue", 1e6)
rev_t1 = get(inc[t1], "revenue", 1e6)
rec_t = get(bs[t], "netReceivables", 1e6)
rec_t1 = get(bs[t1], "netReceivables", 1e6)
ga_t = get(inc[t], "grossProfit", 1e6)
ga_t1 = get(inc[t1], "grossProfit", 1e6)
ca_t = get(bs[t], "totalCurrentAssets", 1e6)
ca_t1 = get(bs[t1], "totalCurrentAssets", 1e6)
ppe_t = get(bs[t], "propertyPlantEquipmentNet", 1e6)
ppe_t1 = get(bs[t1], "propertyPlantEquipmentNet", 1e6)
ta_t = get(bs[t], "totalAssets", 1e6)
ta_t1 = get(bs[t1], "totalAssets", 1e6)
da_t = get(inc[t], "depreciationAndAmortization", 1e6)
da_t1 = get(inc[t1], "depreciationAndAmortization", 1e6)
sga_t = get(inc[t], "sellingGeneralAndAdministrativeExpenses", 1e6)
sga_t1 = get(inc[t1], "sellingGeneralAndAdministrativeExpenses", 1e6)
ltd_t = get(bs[t], "longTermDebt", 1e6)
ltd_t1 = get(bs[t1], "longTermDebt", 1e6)
ni_t = get(inc[t], "netIncome", 1e6)
# Use income statement netIncome for TATA as per formula description
ocf_t = get(cf[t], "operatingCashFlow", 1e6)

print("=== Beneish Inputs (in millions) ===")
print(f"Revenue t={rev_t}, t-1={rev_t1}")
print(f"NetReceivables t={rec_t}, t-1={rec_t1}")
print(f"GrossProfit t={ga_t}, t-1={ga_t1}")
print(f"CurrentAssets t={ca_t}, t-1={ca_t1}")
print(f"PPE t={ppe_t}, t-1={ppe_t1}")
print(f"TotalAssets t={ta_t}, t-1={ta_t1}")
print(f"D&A t={da_t}, t-1={da_t1}")
print(f"SG&A t={sga_t}, t-1={sga_t1}")
print(f"LongTermDebt t={ltd_t}, t-1={ltd_t1}")
print(f"NetIncome t={ni_t}")
print(f"OCF t={ocf_t}")

# Compute variables
gm_t = ga_t / rev_t if rev_t else None
gm_t1 = ga_t1 / rev_t1 if rev_t1 else None

DSRI = (rec_t / rev_t) / (rec_t1 / rev_t1) if rev_t and rev_t1 and rec_t1 else None
GMI = gm_t1 / gm_t if gm_t and gm_t1 else None
AQI = ((1 - (ca_t + ppe_t)/ta_t) / (1 - (ca_t1 + ppe_t1)/ta_t1)) if ta_t and ta_t1 else None
SGI = rev_t / rev_t1 if rev_t1 else None
DEPI = ((da_t1 / (ppe_t1 + da_t1)) / (da_t / (ppe_t + da_t))) if (ppe_t1+da_t1) and (ppe_t+da_t) else None
SGAI = ((sga_t / rev_t) / (sga_t1 / rev_t1)) if rev_t and rev_t1 and sga_t1 else None
LVGI = ((ltd_t / ta_t) / (ltd_t1 / ta_t1)) if ta_t and ta_t1 and ltd_t1 else None
TATA = (ni_t - ocf_t) / ta_t if ta_t else None

M_Score = -4.84 + 0.92*DSRI + 0.528*GMI + 0.404*AQI + 0.892*SGI + 0.115*DEPI - 0.172*SGAI - 0.327*LVGI + 4.679*TATA if all([DSRI, GMI, AQI, SGI, DEPI, SGAI, LVGI, TATA]) else None

print("\n=== Beneish Components ===")
print(f"DSRI = {DSRI:.6f}")
print(f"GMI = {GMI:.6f}")
print(f"AQI = {AQI:.6f}")
print(f"SGI = {SGI:.6f}")
print(f"DEPI = {DEPI:.6f}")
print(f"SGAI = {SGAI:.6f}")
print(f"LVGI = {LVGI:.6f}")
print(f"TATA = {TATA:.6f}")
print(f"M-Score = {M_Score:.6f}")

# ==============================
# 2. Total Accruals / Total Assets
# ==============================
print("\n=== Total Accruals / Total Assets ===")
for yr in ["2023", "2024", "2025"]:
    ni = get(inc[yr], "netIncome", 1e6)
    ocf = get(cf[yr], "operatingCashFlow", 1e6)
    ta = get(bs[yr], "totalAssets", 1e6)
    accruals = (ni - ocf) / ta if ta else None
    print(f"FY{yr}: (NI={ni:.1f} - OCF={ocf:.1f}) / TA={ta:.1f} = {accruals:.6f}")

# ==============================
# 3. SBC-Adjusted OCF / Net Income FY2025
# ==============================
sbc = get(cf["2025"], "stockBasedCompensation", 1e6)
ni25 = get(inc["2025"], "netIncome", 1e6)
ocf25 = get(cf["2025"], "operatingCashFlow", 1e6)
adj_ocf_ni = (ocf25 - sbc) / ni25 if ni25 else None
print(f"\n=== SBC-Adjusted OCF / Net Income FY2025 ===")
print(f"OCF={ocf25:.1f}, SBC={sbc:.1f}, NI={ni25:.1f}")
print(f"(OCF - SBC)/NI = {adj_ocf_ni:.6f}")

# ==============================
# 4. Value Factor Z-Scores
# ==============================
# Extract metrics
metrics = {}
for sym in ["AMD", "NVDA", "INTC", "QCOM"]:
    if sym == "AMD":
        pe = get(amd_mr["2025"], "priceToEarningsRatio")
        ps = get(amd_mr["2025"], "priceToSalesRatio")
        pfcf = get(amd_mr["2025"], "priceToFreeCashFlowRatio")
        evebitda = get(amd_km["2025"], "evToEBITDA")
    else:
        pe = get(peers[sym]["mr"], "priceToEarningsRatio")
        ps = get(peers[sym]["mr"], "priceToSalesRatio")
        pfcf = get(peers[sym]["mr"], "priceToFreeCashFlowRatio")
        evebitda = get(peers[sym]["km"], "evToEBITDA")
    metrics[sym] = {"P/E": pe, "P/S": ps, "P/FCF": pfcf, "EV/EBITDA": evebitda}

print("\n=== Value Metrics ===")
for sym, vals in metrics.items():
    print(f"{sym}: {vals}")

def z_score(x, arr):
    arr = [v for v in arr if v is not None]
    if len(arr) < 2:
        return None
    mu = statistics.mean(arr)
    sigma = statistics.stdev(arr)
    if sigma == 0:
        return 0
    return (x - mu) / sigma

print("\n=== Value Factor Raw Z-Scores ===")
# P/E and P/FCF: INTC is negative, so exclude from cross-section for those metrics
for factor in ["P/E", "P/S", "P/FCF", "EV/EBITDA"]:
    vals = [metrics[s][factor] for s in metrics if metrics[s][factor] is not None]
    # For P/E and P/FCF, exclude negative values for cross-section
    if factor in ["P/E", "P/FCF"]:
        vals = [v for v in vals if v > 0]
    print(f"\n{factor} cross-section (n={len(vals)}): {vals}")
    for sym in ["AMD", "NVDA", "INTC", "QCOM"]:
        v = metrics[sym][factor]
        if v is None or (factor in ["P/E", "P/FCF"] and v <= 0):
            print(f"  {sym}: excluded (value={v})")
            continue
        z = z_score(v, vals)
        print(f"  {sym}: z={z:.4f}")

# Composite value factor (higher = cheaper, so invert z-scores)
print("\n=== Composite Value Factor Z-Score ===")
for sym in ["AMD", "NVDA", "INTC", "QCOM"]:
    zs = []
    for factor in ["P/E", "P/S", "P/FCF", "EV/EBITDA"]:
        v = metrics[sym][factor]
        vals = [metrics[s][factor] for s in metrics if metrics[s][factor] is not None]
        if factor in ["P/E", "P/FCF"]:
            vals = [v for v in vals if v > 0]
        if v is None or (factor in ["P/E", "P/FCF"] and v <= 0):
            continue
        z = z_score(v, vals)
        zs.append(-z)  # invert so higher = cheaper
    if zs:
        composite = statistics.mean(zs)
        print(f"{sym}: individual_zs={[-round(x,4) for x in zs]}, composite_value_z={composite:.4f}")
    else:
        print(f"{sym}: N/A")

# ==============================
# 5. Quality Factor Z-Scores
# ==============================
qmetrics = {}
for sym in ["AMD", "NVDA", "INTC", "QCOM"]:
    if sym == "AMD":
        roic = get(amd_km["2025"], "returnOnInvestedCapital")
        roe = get(amd_km["2025"], "returnOnEquity")
        gm = get(amd_mr["2025"], "grossProfitMargin")
        om = get(amd_mr["2025"], "operatingProfitMargin")
        cr = get(amd_km["2025"], "currentRatio")
        piotroski = amd_fs.get("piotroskiScore")
        altman = amd_fs.get("altmanZScore")
    else:
        roic = get(peers[sym]["km"], "returnOnInvestedCapital")
        roe = get(peers[sym]["km"], "returnOnEquity")
        gm = get(peers[sym]["mr"], "grossProfitMargin")
        om = get(peers[sym]["mr"], "operatingProfitMargin")
        cr = get(peers[sym]["km"], "currentRatio")
        piotroski = peers[sym]["fs"].get("piotroskiScore")
        altman = peers[sym]["fs"].get("altmanZScore")
    qmetrics[sym] = {
        "ROIC": roic,
        "ROE": roe,
        "GrossMargin": gm,
        "OperatingMargin": om,
        "CurrentRatio": cr,
        "PiotroskiF": float(piotroski) if piotroski is not None else None,
        "AltmanZ": float(altman) if altman is not None else None,
    }

print("\n=== Quality Metrics ===")
for sym, vals in qmetrics.items():
    print(f"{sym}: {vals}")

print("\n=== Quality Factor Z-Scores ===")
for factor in ["ROIC", "ROE", "GrossMargin", "OperatingMargin", "CurrentRatio", "PiotroskiF", "AltmanZ"]:
    vals = [qmetrics[s][factor] for s in qmetrics if qmetrics[s][factor] is not None]
    print(f"\n{factor} cross-section (n={len(vals)}): {[round(v,4) for v in vals]}")
    for sym in ["AMD", "NVDA", "INTC", "QCOM"]:
        v = qmetrics[sym][factor]
        if v is None:
            print(f"  {sym}: missing")
            continue
        z = z_score(v, vals)
        print(f"  {sym}: z={z:.4f}")

print("\n=== Composite Quality Factor Z-Score ===")
for sym in ["AMD", "NVDA", "INTC", "QCOM"]:
    zs = []
    for factor in ["ROIC", "ROE", "GrossMargin", "OperatingMargin", "CurrentRatio", "PiotroskiF", "AltmanZ"]:
        v = qmetrics[sym][factor]
        vals = [qmetrics[s][factor] for s in qmetrics if qmetrics[s][factor] is not None]
        if v is None:
            continue
        z = z_score(v, vals)
        zs.append(z)  # higher = better quality
    if zs:
        composite = statistics.mean(zs)
        print(f"{sym}: individual_zs={[round(x,4) for x in zs]}, composite_quality_z={composite:.4f}")
    else:
        print(f"{sym}: N/A")
