# Fin Risk Analyst

- Symbol: AXON
- Elapsed: 141.9s

---
I have what I need — the debt structure is now clear. Writing the assessment.

---

# AXON — Financial Risk Assessment
**As of: latest close 2026-08-20 ($614.26) | Latest annual data: FY2025 (12/31/25) | Latest quarterly: Q2 FY2026**

---

## 1. Credit Risk Assessment

**Rating: Investment Grade (low-BBB equivalent on fundamentals) — but unrated and priced as Sub-Investment Grade at B+/BB-**

This is an unusual bifurcation, and it is the single most important observation in this report. AXON's *fundamental* credit profile — 0.6x net leverage, $1.7B cash, no maturities before 2030 — is comfortably investment grade. But the company priced its March 2025 inaugural bond deal at **6.125% (2030) and 6.25% (2033)**, a spread that in the March 2025 market implied a **BB-/B+ rating**. The market was pricing credit risk the fundamentals don't show, and the gap is explained by two things: GAAP operating margins near zero, and cash flow that depends entirely on excluding $634M of stock-based comp.

Credit breakdown by metric:
- **Solvency: strong.** $1.71B cash and short-term investments vs. $203M net debt. Debt/equity 0.59, debt/assets 0.27. This company cannot go bankrupt from leverage in any plausible near-term scenario.
- **Coverage: weak, and this is the real constraint.** FY2025 GAAP operating income was **–$62.1M**, giving interest coverage of **–0.66x** (per the tool, which uses operating income as EBIT). On a trailing-twelve-month basis to Q2 FY2026, underlying operating income of **$83.9M** against **$114.5M** of interest = **0.73x**. Cash interest is genuinely ~$110–115M/yr (the 6.125%/6.25% coupons on $1.75B fully reconcile the ~$28M/quarter run-rate), so this is not a non-cash accounting artifact. AXON does **not** currently cover its cash interest bill from operating profit.
- **Refinancing cliff: none.** $1.0B 2030 notes, $750M 2033 notes, plus $1.15B of **0%** convertible notes due 2031. Short-term debt is only $80.6M. The nearest material maturity is four years out, and the zero-coupon tranche carries no cash cost. This is a genuinely excellent maturity ladder and materially de-risks the credit.

The 0% 2031 converts are convertible at ~$652/share (1.5336 shares per $1,000). With the stock at $614, that tranche is **out-of-the-money** — meaning if AXON does not re-rate above $652 by 2031, it must settle $1.15B in cash. Worth flagging as a latent obligation, not a near-term one.

---

## 2. Key Financial Risk Metrics Table

| Metric | Value | Assessment |
|---|---|---|
| Total debt / Net debt | $1,909.7M / **$203.1M** | Low |
| Net debt / EBITDA | **1.03x** (FY25 reported); **0.73x** on TTM underlying EBITDA | Very low |
| Debt / equity | 0.59 | Moderate-low |
| Debt / assets | 0.27 | Low |
| **Interest coverage (op. income / interest)** | **–0.66x** FY25; **0.73x** TTM | **Weak / red flag** |
| EBITDA / interest | 2.09x FY25; 2.43x TTM underlying | Thin |
| Current ratio / Quick ratio | **2.53 / 2.29** | Strong |
| Cash ratio | 1.16 | Strong |
| Working capital | $2,243M | Strong |
| Cash | $1,706.6M | Strong |
| **Altman Z-Score** | **1.54 ("Distress")** — *see caveat* | Model artifact, see below |
| **Piotroski F-Score** | **5 / 9 ("Moderate")** | Adequate |
| FCF (FY25) / FCF margin | $75.1M / **2.7%** | Deteriorating sharply |
| FCF yield | **0.15%** | Extremely low |
| SBC / revenue | **22.8%** ($634.2M) | **Red flag** |
| Goodwill + intangibles | $1,567M (22% of assets, 48% of equity) | Impairment exposure |

**Critical caveat on the Altman Z-Score.** The 1.54 "distress" reading is driven almost entirely by component x4, which the tool computes on **book equity** (0.86x). Recomputing with market capitalization ($49.4B at $614.26 vs. $3,757.7M total liabilities) gives x4 ≈ 13.1 and a **Z-Score of ~8.9 — deep in the safe zone**. Even at the stale $390 profile price, Z ≈ 6.2. **The distress classification should be disregarded**; it is a methodology artifact of applying a book-value model to a company trading at ~15x book. I am flagging this rather than reporting 1.54 as a finding.

Piotroski detail (5/9): fails F3 (ROA improvement), F5 (lower leverage — leverage rose), F7 (no dilution — shares diluted), F9 (asset turnover). Passes profitability, operating cash flow, accruals quality, equity issuance, and gross margin improvement.

---

## 3. Market Risk Profile

| Metric | 3-Year (756d) | 1-Year (252d) |
|---|---|---|
| Annualised volatility | **58.9%** | **67.0%** |
| Beta vs. SPY | 1.26 | **1.57** |
| Max drawdown | **60.3%** | 46.1% |
| Sharpe ratio | 0.33 | **–0.61** |

This is one of the most volatile large-cap industrials available. The realized path confirms it: **$885.92 (Aug 2025) → $339.01 (Apr 2026) → $645.72 (Aug 19, 2026)** — a 62% peak-to-trough decline followed by an 82% recovery in under five months.

Beta has **risen** from 1.26 to 1.57 over the past year, meaning the stock's sensitivity to market drawdowns is increasing, not decreasing. The one-year Sharpe of **–0.61** indicates shareholders have been paid *negatively* for the risk taken over the last twelve months despite the recent rally.

Implied risk quantiles: 1-day 95% VaR ≈ **–6.1%**; 1-day 99% VaR ≈ **–8.7%**. Monthly σ ≈ 17%, so a **20% one-month decline is roughly a 1.2-sigma event — approximately a 1-in-8 outcome.** For position sizing, this name requires a materially smaller weight than a typical Industrials holding.

---

## 4. Downside Scenario Analysis: Revenue –20%

Applied to TTM revenue of $3,219M (Q3 FY25–Q2 FY26), holding gross margin at 59.4% and assuming 30% of the $1,120M SG&A base is variable:

| Line item | TTM Actual | –20% Revenue | Δ |
|---|---|---|---|
| Revenue | $3,219.1M | $2,575.3M | –$643.8M |
| Gross profit (59.4%) | $1,912.4M | $1,530.0M | –$382.4M |
| SG&A (net of variable savings) | $1,120.2M | $1,053.0M | –$67.2M |
| **Operating income** | **$83.9M** | **–$231.3M** | **–$315.2M** |
| Underlying EBITDA | $277.8M | **–$37.4M** | –$315.2M |
| Interest expense | $114.5M | $114.5M | flat |
| **EBITDA / interest** | 2.43x | **negative** | — |
| Net debt / EBITDA | 0.73x | **n/m (negative EBITDA)** | — |

**Interpretation — and an important distinction.** A 20% revenue decline turns EBITDA **negative** and would breach any conventional 3.0x net leverage or 2.0x coverage maintenance covenant. **However, AXON's high-yield-style notes almost certainly carry incurrence covenants, not maintenance covenants** (data gap: exact covenant terms not verified). If so, this is a metrics breach, not a technical default or an acceleration event.

**Liquidity survives comfortably in every scenario.** With $1,706.6M cash against a downside operating cash burn of roughly $200–400M/yr (partially offset by a working-capital *release* — FY25 consumed $481.7M of WC, which reverses in contraction), cash runway exceeds **4–5 years** even with zero access to capital markets. They would cut the $136M capex budget first, extending runway further. **There is no liquidity-driven solvency risk here.**

**Where the damage actually lands is the equity, not the balance sheet.** In this scenario: (a) the growth multiple collapses — the stock already demonstrated a 62% drawdown on far less fundamental deterioration; (b) the 0% 2031 converts finish deep out-of-the-money and require $1.15B cash settlement; (c) $1,567M of goodwill and intangibles (largely from the Dedrone and Prepared acquisitions) becomes impairment-exposed, since goodwill rose from $93M to $1,567M in a single year; and (d) SBC of $634M/yr becomes untenable at a lower share price, destroying retention economics. **A 20% revenue decline is a 50–70% equity impairment event even though the company remains solvent.**

Structural mitigant: revenue is heavily recurring (multi-year agency subscriptions, SaaS backlog, contracted hardware refresh cycles), and municipal/state budgets are sticky through normal recessions. A sudden 20% decline is a low-probability tail — but the realistic trigger (a severe state & local budget contraction) is exactly the kind of shock that hits the whole revenue base at once.

---

## 5. Overall Financial Risk Rating

### **MODERATE**

**Rationale:** The balance sheet is genuinely strong — 0.73x–1.03x net leverage, $1.7B cash, no maturities before 2030, current ratio 2.53 — and that caps the credit risk firmly at investment-grade-equivalent levels. There is no credible path to insolvency. But three factors push the *overall financial risk* up from "Low": (1) **interest coverage of 0.73–2.43x** on a fully cash-pay $110M+ coupon, (2) **FCF margin collapse from 15.8% to 2.7%** in one year, producing a **0.15% FCF yield**, and (3) **extreme market risk** — 59–67% volatility, 1.57 beta, 62% realized drawdown, negative one-year Sharpe.

The key insight for the investment memo: **AXON's risk is a valuation-and-dilution risk, not a credit risk.** The bond market priced it at BB-/B+ in March 2025; the equity market prices it at ~15x book. Both cannot be right, and the credit market's skepticism is better supported by the cash flow evidence.

---

## 6. Key Red Flags

1. **FCF quality is materially worse than reported earnings suggest.** FY2025 free cash flow fell **77% to $75.1M** (from $329.5M) *despite* revenue growing 33.5%. Two causes: a **$481.7M working-capital drain** (vs. $72.7M prior year — receivables at 125 days, inventory at 111 days) and capex up 73%. Growth here consumes cash, it does not generate it.

2. **Stock-based compensation of $634M equals 22.8% of revenue.** Reported FCF is positive only because SBC is added back as non-cash. Charging SBC economically, **AXON consumed roughly $559M of value in FY2025**. Shares outstanding rose from 71.1M (2022) to 80.4M (2025), **+13% dilution** with no buyback to offset. Diluted shares reached 82.5M in Q2 FY2026.

3. **Interest coverage is below 1.0x on a GAAP operating basis.** FY2025 operating income was **–$62.1M**. The company is funding a $114M cash interest bill out of cash reserves and equity issuance, not operating profit.

4. **Interest expense jumped 13x** — from $7.1M (FY24) to $94.2M (FY25) — while gross debt rose only 36%. The step-up is explained by the March 2025 refinancing of low-coupon converts into 6.125–6.25% senior notes, permanently raising the cash cost of capital.

5. **Goodwill and intangibles exploded from $93M to $1,567M** — now 22% of total assets and 48% of book equity. This is acquisition-driven (Dedrone, Prepared) and carries real impairment risk if growth decelerates.

6. **The $1.15B zero-coupon 2031 convertible is a latent $1.15B cash obligation** if the stock is below ~$652 at maturity. It is currently out-of-the-money.

7. **Reported TTM EBITDA of $477M is inflated by ~$200M of non-operating gains.** Q1 FY2026 EBIT was $228.9M against operating income of $29.2M — a **$199.6M non-operating gain**. Any analysis using headline TTM EBITDA overstates true earnings power by ~72%. I have used **underlying TTM EBITDA of $277.8M** throughout.

---

## 7. Explicit Data Gaps

- **No quarterly balance sheet available** — the latest balance sheet is FY2025 (12/31/25). Debt and cash figures are therefore ~8 months stale and do not reflect the 2026 zero-coupon convertible issuance, which likely adds ~$1.15B to both debt and cash (roughly net-debt-neutral, but it changes gross leverage and liquidity).
- **Stale market-cap snapshots.** The company profile reports market cap $31.7B at a price of $390.29, while the price history shows $614.26 on 2026-08-20; the FCF-yield tool used $39.0B. These three are mutually inconsistent. I computed market cap directly from the latest close × 80.4M shares = **$49.4B**, giving an FCF yield of **0.15%**. On the tool's snapshots the figure ranges 0.15%–0.24% — either way, negligible.
- **Covenant terms not verified.** I could not retrieve indenture details; my incurrence-vs-maintenance characterization is an inference from typical high-yield structure, not a confirmed fact.
- **No credit rating or CDS data available.** The BB-/B+ implied rating is my inference from the 6.125%/6.25% March 2025 coupons, not a published rating.
- **No peer comparison performed** — deprioritized in favor of balance-sheet depth given the execution budget.

**Bottom line for the memo:** AXON will not go bankrupt. It *can* lose half its value. Size the position for 60%+ annualized volatility and a sub-1.0x cash interest coverage ratio, and do not treat the "distress" Altman Z-Score as a real signal.
