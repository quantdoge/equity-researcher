# Fin Risk Analyst

- Symbol: MCHP
- Elapsed: 49.3s

---
I have the full picture. Writing the assessment now.

---

# MCHP — Financial Risk Assessment
**Microchip Technology Inc.** | Semiconductors (Analog/MCU) | Price $58.35 | Mkt cap $31.68B | FYE March 31
*Data anchor: FY26 (ended 3/31/26) plus Q1–Q2 FY27 (through 9/30/26) reported results.*

## 1. Credit Risk Assessment — **INVESTMENT GRADE (low BBB)**
Fitch affirmed **BBB** senior unsecured on 10-Mar-2026, with a **$2.25B revolver maturing 25-Mar-2030**. The company is comfortably IG, but at the weaker end: leverage is elevated, coverage is only now recovering, and there is a quasi-debt preferred claim that most screens ignore.

The credit story is a **cyclical trough that has clearly turned**. Revenue collapsed 48% peak-to-trough ($8.44B FY23 → $4.40B FY25), bottoming at $970.5M in the Mar-2025 quarter, and has since risen for six consecutive quarters to $1,621.5M (+42.2% y/y, +9.2% q/q) with book-to-bill well above 1.0. TTM operating EBITDA has roughly doubled off the trough. That trajectory, not the trailing ratios, is what supports the rating.

Critically, the reported **Altman Z-Score of 1.561 ("Distress") is a false signal.** The tool uses book equity for x4. Substituting market capitalization ($31.68B / $8.02B liabilities = 3.95), the Z-Score is **~3.56 — solidly in the safe zone**. I would not treat MCHP as a distress candidate on this basis, though the book-equity reading is a fair warning that the balance sheet itself carries little cushion.

## 2. Key Financial Risk Metrics

| Metric | FY26 (3/31/26) | Latest TTM / 9-30-26 | Assessment |
|---|---|---|---|
| Total debt | $5,535M | $5,555M | Flat; all classified long-term, $0 current |
| Cash & ST inv. | $240M | $457M | **Rebuilding (+$217M in 6 mo)** |
| Net debt | $5,295M | $5,098M | Peaked FY24 at $5,713M |
| **Preferred (mezz.)** | $1,485M | $1,485M | **7.50% Series A mandatory convertible** |
| Net debt / EBITDA | 3.78x | **2.99x** | Improving fast; **3.86x incl. preferred** |
| Debt / equity (book) | 0.86x | 0.84x | Moderate |
| Debt / assets | 0.39x | 0.38x | OK |
| **Interest coverage (EBIT)** | **2.21x** | **5.03x** | Latest qtr alone: **9.8x** |
| EBITDA / interest | 6.3x | 8.2x | Adequate |
| Current ratio | 2.09x | 2.24x | Strong |
| Quick ratio | 1.18x | 1.33x | Adequate |
| Cash ratio | 0.21x | 0.37x | Thin, improving |
| **Altman Z** | 1.56 (book) | **3.56 (mkt-cap adj.)** | Artifact — see above |
| **Piotroski F** | **6/9** | — | Moderate; fails leverage, equity change, dilution |
| FCF (reported) | $871M | — | vs. $1,274M returned = **146% payout** |
| FCF yield | 2.72% | — | Low absolute, high vs. own history at trough |
| Working capital | $1,241M | $1,522M | Positive and growing |

**Debt maturity ladder** (qualitative — principal amounts by instrument not disclosed in my data; **gap**): nearest maturities are the **1.625% convertible notes due Feb-2027**, then **4.90% notes due Feb-2028**, **5.050% notes due Mar-2029**, and **5.050% notes due Mar-2030**, plus **0.750% and zero-coupon converts due 2030**. There is **no near-term refinancing cliff**: the 2027 convertible is almost certainly deep in-the-money-strike territory and settles in equity (dilution, not cash), the revolver runs to 2030, and average coupon on the fixed stack is ~3.5% versus 4.9–5.05% for any new 2028+ issuance — refinancing will raise interest cost modestly, not threaten solvency.

**Liquidity runway**: $457M cash + fully undrawn $2.25B revolver = **~$2.7B available**. Against quarterly common dividends (~$248M) + preferred (~$28M) = $276M, that is **~10 quarters of committed shareholder returns even at zero operating cash flow**. Cash runway is not a constraint at the current rating.

## 3. Market Risk Profile — **HIGH**

| Metric | Value | Interpretation |
|---|---|---|
| Annualized volatility (3y daily) | **54.6%** | ~3x the market; semis-cyclical extreme |
| Beta vs SPY (3y) | **2.14** | 5y profile beta 1.85; sensitivity rising |
| Max drawdown (3y) | **-55.5%** | Equity holders have already absorbed a halving |
| Sharpe ratio | **0.071** | Sharpe × vol ≈ 3.9% excess return ≈ the risk-free rate → **essentially zero risk-adjusted excess return** |
| Sortino / CDS spreads | **Not available** | Data gap |

In a market drawdown, MCHP should be expected to fall **~2x the index**. The 55.5% realized drawdown is the honest tail estimate: this is a stock that halves in bad cycles, and has done so within the last three years. Risk-adjusted returns have been non-compensatory — investors have been paid roughly T-bill returns for triple the volatility.

## 4. Downside Scenario Analysis
Base = Q2 FY27 annualized revenue of **$6.49B** (TTM $5.43B), GAAP gross margin 65.9%, non-GAAP opex ~$1.75B, D&A ~$0.62B, cash interest ~$190M.

| | **Base** | **-20% revenue** | **-35% revenue (repeat of FY25 trough)** |
|---|---|---|---|
| Revenue | $6.49B | $5.19B | $4.22B |
| Gross margin | 65.9% | 60.0% (under-absorption) | 55.0% |
| GAAP EBIT | ~$2.35B | **$0.91B** | **$0.17B** |
| EBITDA | ~$2.97B | **$1.53B** | **$0.79B** |
| Interest coverage | 12.4x | **4.8x** | **~0.9x EBIT / 4.2x EBITDA** |
| Net debt / EBITDA | 1.72x | **3.3x (3.9x w/ pref.)** | **6.5x (8.3x w/ pref.)** |
| Approx. FCF | ~$2.4B | **$0.97B** | **$0.25B** |
| Dividend ($1.10B) covered? | 2.2x | **No — $130M shortfall** | **No — cut required** |
| Liquidity verdict | Ample | Funded by revolver/cash; buyback suspended | 2+ years of liquidity; **dividend cut + likely downgrade to BB** |

**The -35% case is not a tail scenario — it is what already happened.** Revenue fell 48% from FY23 to FY25. A repeat would push net leverage above 6.5x and break the dividend, but would **not** break the company: no maturity wall before 2027 (equity-settled convert), $2.25B undrawn revolver, and positive FCF throughout the last downturn (FY25 FCF was +$772M). The realistic downside is a **downgrade and dividend reset, not default**.

**The underappreciated risk is impairment, not insolvency.** Goodwill ($6.70B) + intangibles ($1.92B) = **$8.62B, or 59% of total assets**, against book equity of $6.64B. **Tangible book value is negative (~-$1.98B)**. A renewed downturn would likely trigger a multi-billion-dollar write-down that impairs a third or more of book equity overnight — irrelevant to cash flow, but damaging to the covenant and rating optics.

## 5. Overall Financial Risk Rating: **MODERATE** (credit: Low-Moderate / market: High)
Leverage of ~3.0x (3.9x including preferred), 5x+ and rising interest coverage, $2.7B of liquidity, no refinancing cliff before 2027, and six quarters of sequential revenue recovery with robust bookings make the balance sheet sound. The offsetting risks are entirely cyclical and equity-holder-facing: 54.6% volatility, 2.14 beta, and a demonstrated ability to halve. This is a **moderate-credit-risk, high-market-risk** profile — treat the equity as a high-beta cyclical, not a defensive compounder.

## 6. Key Red Flags
1. **Shareholder returns exceeded free cash flow.** FY26: FCF $871M vs. dividends $1,092.5M + buybacks $182.1M = $1,274M (**146% of FCF**). Cash fell from $772M to $240M. The annualized dividend (~$990M common + $111M preferred = $1.10B) still exceeds FY26 FCF. The payout is dependent on continued cyclical recovery — it was very nearly uncovered at the trough.
2. **$1,485M of 7.50% mandatory convertible preferred is off most leverage screens.** Its ~$111M/yr dividend is a senior claim, and mandatory conversion is a dilution overhang on top of already-rising share count (Piotroski fails the no-dilution test).
3. **Negative tangible book value (-$2.0B)** and goodwill/intangibles at 59% of assets — significant impairment exposure if the cycle rolls over.
4. **Coverage optics are trailing.** The 2.21x FY26 interest coverage in the standard screen reflects a bottom-of-cycle EBIT; true run-rate coverage is ~9.8x. Conversely, don't extrapolate 9.8x either — the cycle cuts both ways.
5. **Beta is rising** (1.85 five-year → 2.14 three-year) as leverage and cyclicality compound.
6. **M&A resumption.** Hailo (Sept-2026) and Vorago (Oct-2026) were completed while net leverage was still ~3x and goodwill already dominant — monitor for further debt-funded deals.

**Data gaps flagged explicitly:** no covenant terms/thresholds (net leverage covenants not disclosed in available data), no CDS spreads, no Sortino ratio, no instrument-level principal amounts for the maturity ladder, no peer leverage comparison, and Q2 FY27 operating cash flow was not directly available (FCF figures for the base case are estimates derived from EBITDA, D&A and capex). Fiscal-year data carries a March 31 year-end, so FY26 comparisons understate the current run-rate.
