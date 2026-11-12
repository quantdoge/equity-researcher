# Fin Risk Analyst

- Symbol: NTES
- Elapsed: 49.7s

---
## NetEase, Inc. (NTES) — Financial Risk Assessment

**Reporting note:** financials are in **CNY**; price/market cap in **USD**. I use CNY/USD ≈ 7.10 as an estimate (no FX tool available) — all cross-currency ratios below are labelled as estimates. Latest annual = FY2025 (Dec-25); I extended the view with quarterly data through **Q2 2026** since the current date is ~Nov 2026 and FY2025 is stale.

---

### 1. Credit Risk Assessment — **INVESTMENT GRADE (effectively AAA-equivalent balance sheet)**

NetEase carries essentially **no debt**: total debt of CNY 6.39bn (~$0.9bn), of which **100% is short-term and long-term debt is literally zero**. Against that sits CNY 167.0bn of cash and short-term investments (~$23.5bn), i.e. ~**30% of the entire market cap in cash**. Net cash position is CNY 160.6bn per the components (see flag #3 on the discrepancy). Interest expense is **CNY 0** across every period in the dataset — the company has no debt-service obligation at all, so interest coverage is *not applicable* rather than weak. This is a fortress, not a leveraged credit.

---

### 2. Key Financial Risk Metrics

| Metric | FY2025 / Latest | Assessment |
|---|---|---|
| Total debt | CNY 6.39bn (~$0.90bn) | Negligible |
| Cash + ST investments | CNY 167.0bn (~$23.5bn) | 26.2x total debt |
| Net cash | CNY 160.6bn (~$22.6bn) | ~29% of mkt cap |
| Debt / Equity | 0.04 (4%) | Very low |
| Debt / Assets | 0.03 | Very low |
| Net debt / EBITDA | **−3.73x** (net cash) | No leverage |
| Interest coverage (EBIT/Int.) | **N/A** — interest expense = 0 | No constraint |
| Altman Z-Score | **3.57 reported** (Safe); ~**4.5 adjusted** | Safe zone |
| Piotroski F-Score | **8 / 9 — Strong** | Only asset turnover fails |
| Current ratio | 3.45 | Strong |
| Quick ratio | 3.44 | Strong (inventory trivial) |
| Cash ratio | 3.19 | Exceptional |
| Working capital | CNY 128.3bn | ~110% of TTM revenue |
| Assets / liabilities | 3.93 | Strong |
| Equity / assets | 0.75 | Strong |
| Debt maturity profile | 100% current, **0 long-term** | No refinancing cliff |
| FCF yield (corrected) | **~8.7%** (see flag #1) | Attractive |
| FCF / net income | 1.43x | High-quality earnings |

**FCF sustainability is excellent and improving:** FCF margin rose 26.0% (2022) → 30.0% (2023) → 35.6% (2024) → **42.9% (2025)**, on FCF of CNY 48.3bn. Capex is only CNY 1.04bn (0.9% of revenue) — an asset-light model. Dividends (CNY 13.45bn) + buybacks (CNY 0.62bn) consume just **29% of FCF**, so shareholder returns are ~3.4x covered.

---

### 3. Market Risk Profile — the weakest link

| Metric | Value | Read |
|---|---|---|
| Annualised volatility (3Y) | **37.8%** | High |
| Beta vs SPY (3Y daily) | **0.48** | Low |
| Beta (vendor, 5Y monthly) | 0.77 | Moderate |
| Max drawdown (3Y) | **−34.0%** | Significant |
| Sharpe (rf = 0) | **0.38** | Mediocre |
| Sharpe on 10Y UST 5.13% | ~0.25 (est.) | Weak risk-adjusted return |
| Sortino | **Not available** | Data gap |

**This is the critical asymmetry:** the low 0.48 beta badly understates the stock's true risk. Volatility of 37.8% is roughly 2.5x what a 0.48-beta stock should exhibit, meaning **the risk is overwhelmingly idiosyncratic/China-specific, not market-driven**. Beta-based models will understate NTES tail exposure. The −34% max drawdown confirms this is a name that can lose a third of its value without the index moving.

**Rates context:** the curve is upward-sloping (2Y 4.74%, 10Y 5.13%, 30Y 5.47%, +39bp, not inverted). Because NTES is *net cash*, higher rates are a mild **tailwind** (interest income on CNY 167bn) and there is zero refinancing-rate sensitivity.

---

### 4. Downside Scenario Analysis (revenue shock, TTM base)

TTM base (Q3'25–Q2'26): revenue CNY 116.5bn, gross margin 67.2%, total opex CNY 37.2bn, operating income CNY 41.0bn (35.2% margin).

| Scenario | Revenue | Operating income | Op margin | FCF (est.) | Dividend coverage |
|---|---|---|---|---|---|
| **Base** | 116.5 | 41.0 | 35.2% | ~48 | 3.4x |
| **−20%** (rigid opex) | 93.2 | **25.4** | 27.3% | ~30 | 2.2x |
| −20% (60% opex flex) | 93.2 | 29.9 | 32.1% | ~34 | 2.5x |
| **−40%** | 69.9 | **9.8** | 14.0% | ~15 | 1.1x |
| **−52%** | 55.4 | **≈ 0** | 0% | ~2 | 0.2x — dividend cut |
| **−60%** | 46.6 | −5.9 | −5.1% | negative | eliminated |

**Key finding: the operating breakeven point is roughly a −52% revenue collapse.** The company can lose more than half its revenue and still not report an operating loss. Even in the −60% catastrophe case, net cash of CNY 160.6bn covers the annual operating loss (~CNY 5.9bn) for **~27 years**. There are no covenants to breach because there are no lenders. In a −20% scenario the balance sheet is entirely unaffected and FCF remains ~CNY 30bn — this company would be *buying back stock* in that scenario, not defending solvency.

---

### 5. Overall Financial Risk Rating: **LOW**

Credit risk is among the lowest in the entire Technology universe — net cash equal to ~3.7x EBITDA, no long-term debt, an 8/9 F-Score, and Z-Score deep in the safe zone. Liquidity is exceptional. Downside tolerance is extreme. **The only non-Low element is market/price risk (Moderate-High): 37.8% volatility and a −34% drawdown against a deceptively low 0.48 beta.** For an equity holder, NTES risk is *quotational and geopolitical*, not *solvency* risk.

---

### 6. Key Red Flags

1. **Earnings quality below the operating line (most important).** Q2 2026 shows *operating* income +33% YoY (CNY 12.06bn vs 9.06bn) with operating margin expanding to 40.1% — yet **net income fell 19% YoY** (CNY 6.96bn vs 8.60bn), and diluted EPS dropped to 10.85 from 13.50. Roughly CNY 5bn of value leaked between EBIT and net income (investment fair-value losses / FX / impairments). This matches the vendor-reported non-GAAP drop to $1.78/ADS from $2.60. **The core business is accelerating; the investment portfolio is the volatility engine.** This is the single largest driver of the high volatility despite low beta.
2. **Valuation vs. declining net income.** At ~$123/share and TTM diluted EPS of ~CNY 50 (~$7.07), NTES trades ~17x for *negative* trailing net income momentum. The multiple requires the market to look through non-operating losses to operating strength — a reasonable but not risk-free assumption.
3. **China regulatory / ADR-structure risk is unquantified in the financials.** Sector-wide: NPPA game-licence approvals, minor-protection rules, and VIE/ADR structure. Partial mitigation: the 20-F notes the PCAOB vacated its 2021 determination and **removed China/HK from the non-inspection list in Dec 2022**, materially reducing delisting risk. NTES also maintains a HK dual listing, providing a conversion path. Still, this tail is invisible to the balance sheet.
4. **Title concentration.** Revenue is heavily dependent on a small number of legacy and new franchise titles — a single failed launch is a larger threat than any financial lever.
5. **Currency mismatch for USD holders.** Reports in CNY, trades in USD; CNY depreciation flow-through to USD EPS is unhedged at the ADR level.

---

### 7. Data Gaps and Tool Discrepancies (flagged explicitly)

1. **FCF yield of 60.76% reported by the tool is wrong — currency mismatch.** FCF (CNY 48.3bn) was divided by market cap (USD 79.5bn). Corrected: 48.32 / (78.45 × 7.10 ≈ 557bn CNY) = **~8.7%**; ~7.2% ex-working-capital. Use the corrected figure.
2. **Altman Z-Score understated.** x2 was computed as 0.0 because the FY2025 balance sheet returned `retained_earnings: 0` (FY2024 was CNY 132.3bn — clearly a field error). Rebuilding x2 at ~0.65 lifts Z to **~4.5**. Both readings are "Safe," but 3.57 is not the true figure.
3. **Net debt conflict.** The balance-sheet field shows net debt of −CNY 45.1bn while the leverage calculator (total debt − cash & ST investments) shows −CNY 160.6bn. I use the −160.6bn gross-cash view for survivability and treat **−CNY 45bn as a conservative floor**. Even at the floor, there is no net leverage.
4. **Stock-based compensation reported as CNY 0 in FY2025** vs CNY 3.88bn in FY2024 and ~CNY 3.2bn in 2022–23. This is almost certainly a data error. If SBC is ~CNY 3–4bn, FCF quality is overstated by ~7–8% and the F-Score's accrual component is slightly flattered.
5. **Interest coverage is not computable** — interest expense is zero in every period. This is a genuine "not applicable," not missing data, but it means coverage cannot be used as a risk discriminator here.
6. **No public credit rating found.** Targeted search returned no Moody's/S&P/Fitch issuer rating for NTES (consistent with a company that issues no material debt). My "Investment Grade" call is therefore **inferred from the balance sheet, not agency-assigned**.
7. **Sortino ratio unavailable** from the toolset.
8. **Peer credit comparison not performed** — FMP sector peers for NTES are US mega-cap Tech, which are not meaningful credit comps for a China-domiciled gaming issuer.

**Bottom line:** NTES is a financially fortress-like company facing almost no credit or liquidity risk, whose real exposure is equity-price volatility and below-the-line earnings noise generated by its investment portfolio. Judge it as a *quality balance sheet with a volatile income statement*, not as a leveraged or distressed credit.
