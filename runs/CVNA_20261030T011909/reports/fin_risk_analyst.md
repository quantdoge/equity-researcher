# Fin Risk Analyst

- Symbol: CVNA
- Elapsed: 97.2s

---
## CVNA — Financial Risk Assessment

**Company:** Carvana Co. (Consumer Cyclical / Auto Dealerships) · Market cap ~$74.9B · Price $68.30 · FY2025 (period end 2025-12-31)

> ⚠️ **Data integrity warning up front.** The FY2025 income statement contains internally contradictory fields: reported `ebitda` = **–$110M** and `ebit` = **–$385M** against reported `operating_income` = **+$1,881M** (9.26% margin) and net income of +$1,407M. The tool-computed `net_debt_to_ebitda` of **–24.62x** and the Altman Z input `x3` are derived from the corrupted EBIT figure. I have recomputed using operating income + D&A and flag both readings below. This is the single most important caveat in this report.

---

## 1. Credit Risk Assessment

**Rating: SUB-INVESTMENT GRADE (upper tier / crossover)**

| Agency | Rating | Note |
|---|---|---|
| S&P | **BB-** (affirmed, outlook **Positive**) | Expects leverage comfortably <3x in 2026; 'BB'/'2' recovery on proposed $1B senior secured (Aug 2026) |
| Moody's | **B2** (upgraded from B3, outlook **Positive**) | Senior secured B2; **senior unsecured Caa1** |
| Fitch | **BB+** | 9% senior secured notes rated BB+ |

Carvana sits at the top of high yield with positive momentum and a genuine turnaround in leverage. The critical structural point is the **Caa1 senior unsecured** rating — unsecured holders sit deep behind a growing secured stack (9% secured notes, ABS/floorplan facilities), so recovery in a stress case is weak. The trajectory is improving, but this is not an investment-grade credit.

---

## 2. Key Financial Risk Metrics

| Metric | Value | Read |
|---|---|---|
| Total debt | $5,521M | ST debt only $285M, LT $4,830M |
| Net debt | $2,708M (BS field: $3,194M) | — |
| Debt / equity | **1.31x** | Moderate |
| Net debt / EBITDA | **1.26x** *(recomputed)* · –24.62x *(tool, corrupted)* | Low leverage on corrected basis |
| Gross debt / EBITDA | 2.56x | Consistent with S&P <3x |
| EBIT / interest | **3.72x** | Adequate but thin for HY |
| EBITDA / interest | 4.27x | — |
| Avg cost of debt | **~8.7–9.1%** | High; 9% secured coupon confirms |
| Debt / assets | 0.42x | — |
| Current ratio | **4.31x** | Strong |
| Quick ratio | 2.73x | Strong |
| Cash ratio | 1.85x | — |
| Cash | $2,813M | 0.31x total liabilities |
| Working capital | $5,030M | — |
| Altman Z | **2.18 reported / ~2.75 corrected** | Grey zone; ~7.6 on market-cap x4 |
| Piotroski F-Score | **6 / 9** | Moderate |
| FCF | $889M (CFO $1,036M, capex $147M) | Positive 3 yrs running |
| FCF yield | **1.16%** | Thin vs valuation |
| FCF margin | 4.4% | Improving (2024: 6.0%) |
| Equity | $4,203M (from **–$384M** in 2023) | Deficit nearly eliminated (RE –$9M) |
| Revenue growth FY25 | **+48.6%** | $13.7B → $20.3B |
| Gross margin | 20.6% (2022: 7.4%) | Strong structural improvement |

**F-Score detail:** profitability 3/4 (ROA positive and improving; accruals quality fails — CFO $1,036M < net income), leverage/liquidity 3/3 (leverage down, positive equity change), efficiency 1/2. **F7 = 0 (dilution)** and **F9 = 0 (asset turnover fell 1.61x → 1.54x)**.

**Cash runway:** not applicable — the company is cash generative, with $2.8B cash plus $5.0B working capital. No liquidity event risk on a 12-month view. Near-term refinancing cliff is minimal: only **$285M** of debt matures within a year.

---

## 3. Market Risk Profile

| Metric | Value | Read |
|---|---|---|
| Annualised volatility (3y) | **66.3%** | Extreme — ~4x market |
| Beta vs SPY | **2.16** (computed) / 3.55 (profile field) | Flagged discrepancy; both very high |
| Max drawdown (3y) | **–43.0%** | Severe |
| Sharpe ratio (rf = 0%) | 0.935 | Decent compensation for the risk taken |
| Sortino | **Not available** | Data gap |

Equity risk is the dominant risk in this name. A 66% vol / 2.2 beta profile means a 20% market drawdown plausibly maps to a 40–45% drawdown here — roughly the realized 3-year max. The Sharpe of 0.94 is respectable but is entirely a function of the enormous trailing return; the downside dispersion is what matters for risk sizing. Note the beta conflict: profile beta of 3.55 vs. 2.16 computed on 756 days — I would treat 2.2 as the more defensible estimate and 3.5 as the tail-sensitive reading.

---

## 4. Downside Scenario Analysis — Revenue –20%

Base FY2025: revenue $20,322M, gross margin 20.6%, SG&A $2,308M, D&A $275M, EBIT $1,881M, interest $505M.

**Scenario A — volume shock, GM compresses 200bps to 18.6%, SG&A flexes –10% (moderate flex)**

| | Value |
|---|---|
| Revenue | $16,258M |
| Gross profit | $3,024M |
| SG&A | $2,077M |
| EBIT | **$672M** (–64%) |
| EBITDA | $947M |
| EBIT / interest | **1.33x** |
| Net debt / EBITDA | **2.86x** |
| FCF (incl. ~$300M WC release) | **~+$550M** |

Still profitable, still FCF positive, leverage under 3x. **No covenant or liquidity crisis.**

**Scenario B — volume shock + margin war (GM to 17.0%, SG&A flexes only –5%)**

| | Value |
|---|---|
| Gross profit | $2,764M |
| EBIT | **$296M** |
| EBITDA / interest | **1.13x** |
| EBIT / interest | **0.59x — breach** |
| Net debt / EBITDA | **4.74x** |
| FCF before WC | **–$81M** |

This is the tail: coverage below 1.0x, leverage through 4.5x, and the company would be consuming cash absent inventory liquidation. Given SG&A is only 11.4% of revenue and Carvana's cost base carries meaningful semi-fixed reconditioning/logistics capacity, Scenario B is the realistic bad case rather than a stress fantasy.

**Rate sensitivity:** +100bps on $5.5B of debt = +$55M interest. Base coverage falls 3.72x → 3.34x; Scenario A falls 1.33x → 1.20x. With the 10Y at **4.99%** and 30Y at **5.37%** (2s10s +34bps, no inversion), refinancing the stack is expensive — the 9% secured coupon is the price of that curve.

**Not modeled (data gap):** Carvana's retained interests in securitized receivables and ABS funding dependence. In a consumer-credit downturn, both loan loss provisions and ABS market access are correlated with the same revenue shock — this is the unquantified amplifier and I would not assume Scenario B is the floor.

---

## 5. Overall Financial Risk Rating: **MODERATE**

Split view, because the credit and equity risk profiles genuinely diverge:

- **Credit / balance-sheet risk: MODERATE (improving).** Net leverage 1.26x, current ratio 4.3x, $2.8B cash, positive FCF, only $285M due within a year, equity rebuilt from negative to $4.2B, and two agencies on positive outlook. This is a materially de-risked balance sheet versus 2022–23.
- **Market / equity risk: HIGH.** 66% vol, beta ~2.2, 43% max drawdown, FCF yield of just 1.16% against a $75B cap. The equity is priced for sustained execution.
- **Business-model risk: HIGH.** Operating leverage cuts both ways; a combined volume + margin shock takes coverage below 1.0x.

---

## 6. Key Red Flags

1. **Reported EBITDA/EBIT fields are corrupted** (–$110M / –$385M vs. +$1,881M operating income). Any screen keying on `net_debt_to_ebitda` = –24.62x or raw Altman Z = 2.18 will misclassify this company. Also: net income $1,407M (income statement) vs. $1,895M (cash flow statement) — unresolved.
2. **Interest coverage of 3.72x is the binding constraint.** At ~9% average cost of debt on $5.5B, coverage is thin for a BB-/B2 credit and is the first metric to break in a downturn.
3. **Caa1 senior unsecured rating** — weak recovery for unsecured holders behind a growing secured/ABS stack.
4. **Persistent dilution:** basic shares 504M → 547M → 612M → 688M (+36.5% over 3 years, +12.5% in FY25). Piotroski F7 = 0. Additionally, weighted diluted shares of **1,121M** vs. basic 688M implies a **63% potential overhang** — flagging this as a probable data artifact but it cannot be dismissed without the dilution note.
5. **Accruals quality weak** (F4 = 0): CFO $1,036M trails net income, and FY25 FCF fell to $889M despite a 49% revenue increase — cash conversion is deteriorating as working capital absorbs $480M.
6. **Inventory +50% YoY to $2,408M.** Correct for growth, but a demand shock risks writedowns on top of margin compression.
7. **Off-balance-sheet ABS / retained receivables exposure is not disclosed in the data provided** — the largest unquantified risk.
8. **Capex at 0.7% of revenue** ($147M vs. $20.3B) — extremely light; sustainable only while growth is funded by working capital and existing PP&E.

**Explicit data gaps:** debt maturity schedule by year, covenant terms and headroom, CDS spreads, Sortino ratio, securitization/loan-book detail, and quarterly granularity (all ratios are annual, period-end, which understates intra-year stress). Peer benchmarking was not run — no peer multiples are included.
