# Fin Risk Analyst

- Symbol: TEM
- Elapsed: 87.6s

---
# TEM — Tempus AI, Inc.
## Financial Risk Assessment
**Data as of:** 16-Nov-2026 (last close $64.76) | FY2025 audited + Q3'26 (period ended 30-Sep-2026)

---

## 1. Credit Risk Assessment

**Rating: SUB-INVESTMENT GRADE (B+/BB- equivalent, unrated, no CDS available)**

The company is loss-making on a GAAP basis with negative free cash flow and negative tangible equity — textbook sub-investment-grade characteristics. However, the *default* risk is genuinely low, and materially lower than the Altman score implies, for three structural reasons:

| Credit mitigant | Evidence |
|---|---|
| Debt is almost entirely long-dated, near-zero-coupon convertible paper | $460M **0.00%** converts due May-2032 issued May-2026 (net proceeds $441.9M); 0.75% converts due 2030 outstanding. **Short-term debt = $0** at Q3'26 |
| No refinancing cliff | Earliest maturity is 2030. Nothing due inside 3 years |
| Secured bank debt retired | $307.7M secured senior credit facility **fully repaid** May-2026 from convert proceeds — no maintenance covenants, no secured claims ahead of converts |

Interest expense is collapsing as a direct consequence: **$15.3M (Q1'25) → $15.3M (Q3'25) → $14.3M (Q1'26) → $10.3M (Q2'26) → $6.7M (Q3'26)**. Cash coupon burden is now roughly $3–5M/yr (convert coupons only); the P&L charge is mostly non-cash issuance-cost amortisation. **Cash debt service is not a solvency variable for this issuer before 2030.**

The real credit question is not default — it is **dilution and equity-market access**.

---

## 2. Key Financial Risk Metrics

### Leverage & Coverage

| Metric | FY2023 | FY2024 | FY2025 | Q3'26 / LTM |
|---|---|---|---|---|
| Total debt ($M) | 488.1 | 468.1 | 1,326.7 | **1,431.9** |
| Cash & ST inv. ($M) | 197.6 | 448.3 | 755.0 | **637.4** |
| Net debt ($M, debt − cash) | 290.6 | 19.8 | 571.7 | **794.5** |
| Total equity ($M) | (1,382.2) | 56.3 | 491.3 | 500.4 |
| **Debt / equity** | n.m. | 8.3x | 2.70x | **2.86x** |
| **Net debt / equity** | n.m. | 0.35x | 1.16x | **1.59x** |
| **Debt / assets** | 0.87 | 0.51 | 0.58 | **0.58** |
| **Net debt / EBITDA** | n.m. | n.m. | **(4.83x)** | n.m. (neg. EBITDA); **12.2x** on FY26E adj. EBITDA $65M |
| **Interest coverage (EBIT/int.)** | (3.6x) | (12.1x) | **(3.14x)** | **(0.85x)** annualised Q3'26 |
| Tangible book equity ($M) | — | (28.7) | **(334.1)** | **(322.1)** |
| Goodwill + intangibles / equity | — | 151% | 168% | **164%** |

Net-debt-to-EBITDA is the single weakest reported metric — but it is a **denominator problem, not a numerator problem**. On FY2026 guided Adjusted EBITDA of ~$65M leverage is ~12.2x, which would be alarming for a term-loan borrower and is largely irrelevant for a 0%-coupon convert issuer with $637M of cash.

### Liquidity (Q3'26)

| Metric | Value | Read |
|---|---|---|
| Current ratio | **2.61x** (FY25: 3.13x) | Strong |
| Quick ratio | **2.48x** | Strong |
| Cash ratio | **1.46x** | Strong |
| Working capital | **$700.5M** | Ample |
| Cash / total liabilities | 0.33x | Adequate |
| **Cash runway** (LTM FCF burn $150.6M) | **~4.2 years** | Comfortable |
| Cash runway (worst trailing qtr, Q1'26 burn $83.3M) | ~1.9 years | Still adequate |
| Q3'26 OCF | **+$9.2M (first positive quarter)** | Inflection |

### Bankruptcy / Distress Scores

| Score | Value | Interpretation |
|---|---|---|
| **Altman Z-Score** | **−0.651** | "Distress" zone |
| Z components | x1 0.349, x2 **−1.053**, x3 −0.097, x4 0.276, x5 0.559 | x2 (retained earnings/assets) is the driver: accumulated deficit **−$2.531bn** |
| **Z re-run with market cap in x4** | **≈ +2.72** | Grey zone, near safe-zone boundary |
| **Piotroski F-Score** | **5 / 9** — Moderate | Passes: ROA improvement, accruals quality, lower leverage, positive equity change, gross-margin improvement. Fails: positive ROA, positive OCF, no dilution, asset-turnover improvement |

**Caveat on Z-Score:** the model is structurally hostile to cash-rich, high-growth, loss-making issuers — it penalises an accumulated deficit built by design (SBC, R&D) while ignoring $637M of cash and 2030+ maturities. Substituting the $11.5bn market capitalisation for book equity lifts the score from −0.65 to roughly **+2.7**. I treat the "Distress" label as **not a reliable default signal here**; it is a reliable *profitability* signal.

---

## 3. Market Risk Profile

| Metric | Value | Comment |
|---|---|---|
| Annualised volatility (3y, 756d) | **93.2%** | ~6x the S&P 500 — extreme |
| Beta vs SPY (3y) | **2.66** | 1% S&P move → ~2.7% TEM move |
| Beta (vendor, long-run) | **3.61** | Alternate measure; range 2.7–3.6 |
| Max drawdown (3y) | **−59.8%** | Severe capital-impairment risk realised historically |
| Sharpe ratio (rf = 0%) | **0.53** | Positive but poor risk-adjusted quality |
| Price vs 52-wk high ($103.42, Oct-25) | **−37.4%** | Currently in drawdown |
| Price vs Oct-26 high ($87.99) | **−26.4%** | Drawdown ongoing into Nov-26 ($64.76) |

A 93% vol / 2.7 beta / 60% max-drawdown profile means a 20–30% single-event price hit is a routine occurrence, not a tail event. Positions should be sized on vol, not on conviction. Note the drawdown is *not* accompanied by fundamental deterioration — Q3'26 was the best operating quarter in company history. That divergence is itself the market-risk story: **sentiment, not solvency, is driving the price.**

---

## 4. Downside Scenario Analysis

**LTM baseline (Q4'25–Q3'26):** Revenue $1,509.4M · Gross margin 64.5% · Implied opex $1,251.9M (SG&A $862.5M + implied R&D ~$389M) · Operating loss $(278.9)M · EBITDA $(31.6)M · FCF $(150.6)M

### Scenario A — Revenue −20% (revenue $1,207.5M)
Assumptions: COGS is materially fixed (lab, sequencing, pathology personnel) → COGS falls only ~15%, gross margin compresses 64.5% → ~62%. Opex cut 8% (discretionary SBC, marketing, G&A; R&D ring-fenced).

| Line | Base | Stress (−20%) |
|---|---|---|
| Revenue | 1,509.4 | 1,207.5 |
| Gross profit | 973.0 | 751.5 |
| Opex | 1,251.9 | 1,151.7 |
| **Operating income** | **(278.9)** | **(400.2)** |
| Cash interest | ~5 | ~5 |
| **FCF** | **(150.6)** | **~ (335)** |
| Cash balance | 637.4 | 637.4 |
| **Runway** | 4.2 yrs | **~1.9 yrs (2.3–2.4 yrs incl. ~$60M receivables release)** |

**Outcome:** No default. No covenant to breach (secured facility repaid). Convert maturities are 2030+. The company would need to raise **$300–400M of equity or converts in 2028**, likely at a depressed price → **material dilution (est. 10–20%)**. Credit outcome: survives. Equity outcome: painful.

### Scenario B — Revenue −40% (severe; revenue $905.6M)
Gross margin ~58%; opex cut 16% to $1,051M → operating loss ~$(505)M; FCF ~$(440)M. Runway **~1.4 years**. Requires immediate capital raise plus restructuring. **Still not a 2027 default** — but converts would trade at deep distress levels and the equity would be heavily impaired.

### Scenario C — Rate / market shock, fundamentals intact
Beta 2.7–3.6 → a 20% S&P drawdown implies a **~55–70% TEM drawdown**. Fundamentals unaffected; Altman/credit unaffected. This is the highest-probability risk for a holder.

### Scenario D — Goodwill impairment
Goodwill + intangibles $822.5M (164% of equity, 34% of assets) largely from the $600M Ambry Genetics deal (closed Feb-2025). A 20% revenue miss concentrated in the hereditary/oncology diagnostics segment could trigger a non-cash impairment of $200–400M → **total equity to near zero or negative**. No cash or covenant impact, but it re-breaks the Altman score and can force index/fund selling.

---

## 5. Overall Financial Risk Rating

## **MODERATE**

*(Equity/market risk: **HIGH**; credit/default risk: **LOW–MODERATE**)*

**Why not High:** No debt matures before 2030. $637M cash against a ~$150M annual burn. Q3'26 delivered the company's **first positive operating cash flow** (+$9.2M), positive Adjusted EBITDA of **$25.6M vs $1.5M a year earlier**, and gross margin of **64.8%**. FY2026 guidance is revenue of **$1.60–1.605bn** (vs $1.272bn in FY2025) with **~$65M Adjusted EBITDA** — the company crosses into profitability guidance within two years of IPO. Cash debt service is ~$5M/yr.

**Why not Low:** GAAP operating loss of $278.9M LTM, FCF of −$150.6M LTM, negative tangible equity of −$322M, Altman Z in the distress zone, and an accumulated deficit of $2.53bn. Deleveraging depends entirely on EBITDA inflecting, not on debt being repaid.

**Why the framework caps the score at Moderate for equity holders:** 93% annualised vol, 2.66 beta, and a 60% realised max drawdown dominate the risk budget even though balance-sheet survival is not in question.

---

## 6. Key Red Flags

1. **Adjusted EBITDA is SBC-financed.** LTM stock-based compensation of **$200.2M (13.3% of revenue)** exceeds the FY26 guided Adjusted EBITDA of ~$65M by 3x. The "profitability inflection" narrative is a non-GAAP construct; GAAP operating loss is $(278.9)M. Treat any Adjusted-EBITDA-based valuation or leverage metric with scepticism.
2. **Negative tangible equity (−$322M)** and a $2.53bn accumulated deficit. Any large impairment takes book equity toward zero.
3. **Leverage tripled in twelve months** ($468M → $1,327M FY24→FY25) to fund the $600M Ambry Genetics acquisition. Goodwill/intangibles now 164% of equity — impairment risk sits directly on the equity cushion.
4. **Persistent FCF deficit:** FY2023 −$248.9M, FY2024 −$211.2M, FY2025 −$245.4M, LTM −$150.6M. Cumulative ~$856M burned over four years. Improving, but not yet self-funding.
5. **Dilution is the transfer mechanism.** Shares 174.3M → 181.3M (+4.0% YoY) plus $200M/yr of SBC plus a convertible overhang. Piotroski fails the "no new shares issued" test. Convert holders get paid; equity holders absorb the dilution.
6. **Unexplained Q3'26 cash outflow of ~$178.6M** (cash $816.0M → $637.4M) against FCF of only −$5.5M. Implies ~$170M of debt repayment, acquisition, or investment not visible in the retrieved statements. **Disclosure gap — needs primary-source confirmation.**
7. **Extreme market risk.** 93% vol, beta 2.66–3.61, −59.8% max drawdown, current price 37% below the 52-week high despite record operating results.
8. **Reimbursement concentration.** Diagnostics revenue depends on CMS/private-payer rates for NGS panels; a rate cut is a direct gross-margin shock not captured in any metric above.

---

## Data Gaps (explicitly flagged)

- **No credit rating and no CDS** — TEM is unrated; no market-implied default signal available.
- **No covenant package disclosed** in retrieved data (largely moot post-repayment of the secured facility).
- **Convertible note sizes**: $460M 0.00% due 2032 confirmed. The 0.75% due-2030 tranche is confirmed to exist but its principal and conversion price were **not confirmed from retrieved sources**; implied non-term-loan debt is ~$1,280M pre-May-2026.
- **R&D line not broken out** in the income statement feed — implied ~$389M LTM, derived as residual (gross profit + operating loss − SG&A).
- **Net debt discrepancy**: the ratio tool reports $572.1M/FY25 and $841.4M/Q3'26 net debt vs. $571.7M and $794.5M computed as debt minus cash. The ~$47M gap is consistent with operating-lease liabilities being included in the tool's net-debt field. I have used debt-minus-cash throughout.
- **No peer benchmarking performed** (FMP peer/multiples data not retrieved within budget).
- **Q3'26 figures are unaudited**; source is the 2-Nov-2026 filing.
- No segment-level revenue or margin split (Diagnostics vs. Data & Applications) was available — the mix shift toward lower-multiple data licensing vs. diagnostics is a material unassessed variable.
