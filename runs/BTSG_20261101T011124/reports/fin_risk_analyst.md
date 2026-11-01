# Fin Risk Analyst

- Symbol: BTSG
- Elapsed: 73.0s

---
I now have enough to complete the assessment. The picture diverges sharply from the FY2025 annuals — LTM through Q3 2026 shows major deleveraging.

---

# BrightSpring Health Services (BTSG) — Financial Risk Assessment

**As of:** Q3 FY2026 (period ended 2026-09-30); last reported annual = FY2025 (2025-12-31). Price $66.89, market cap ~$13.2B.

**Critical framing note:** FY2025 GAAP annuals (net leverage **5.7x**, coverage **1.88x**) materially overstate current risk. The trailing-twelve-month (LTM) picture through Q3 2026 is dramatically stronger — **net leverage 2.34x, EBIT coverage 3.80x**. All ratios below are shown both ways; the LTM column is the correct basis for forward risk.

---

## 1. Credit Risk Assessment

**Rating: SUB-INVESTMENT GRADE — upper tier (BB-range / "crossover-positive"), improving trajectory**

BTSG is not an investment-grade credit, but it is a solid, deleveraging high-yield credit rather than a stressed one. Justification:

- Net leverage fell from **5.90x (2023) → 5.70x (FY2025) → 2.34x (LTM Q3'26)** on reported EBITDA, or **1.79x** on the company's adjusted EBITDA (per Q3'26 disclosure). Even on the conservative reported-EBITDA basis this is comfortably BB territory.
- Coverage improved from **1.88x → 3.80x** as interest expense fell from $228M (FY2024) to $145M (LTM) following IPO-driven debt paydown and the 2026 term loan repricing. Note the Q1'26 10-Q language on reduced "variable-rate and applicable margin" — this is a genuine, structural interest reduction.
- **No refinancing cliff.** The $2.55B Term Loan B was refinanced in 2026 to a **February 2031** maturity. Short-term debt is only **$35.3M** against **$717.8M** of cash. Total liquidity ≈ **$1.19B** ($718M cash + $475M undrawn revolver, undrawn as of 3/31/26). The next material maturity is >4 years out.
- Offset: negative tangible book equity and a thin 4.65% EBITDA margin keep this out of IG.

---

## 2. Key Financial Risk Metrics

| Metric | FY2025 (annual) | **LTM Q3'26** | Assessment |
|---|---|---|---|
| Revenue | $12,911M | **$15,251M** (+~26% y/y) | Strong growth |
| Reported EBITDA | $459.5M | **$709.2M** | +54% y/y |
| EBITDA margin | 3.56% | **4.65%** | Thin but expanding |
| Net debt | $2,618.9M | **$1,661.1M** | Down $958M |
| **Net debt / EBITDA** | 5.70x | **2.34x** | ✅ Rapid de-lever |
| Total debt / equity | 1.44x | **1.09x** | ✅ |
| Debt / assets | 0.42x | **0.38x** | ✅ |
| **EBIT / interest** | 1.88x | **3.80x** | ⚠️ Improved, still thin |
| EBITDA / interest | 2.92x | **4.89x** | ⚠️ |
| Current ratio | 1.57x | **1.62x** | ✅ |
| Quick ratio | 1.12x | **1.22x** | ✅ |
| Cash ratio | 0.05x | **0.42x** | ✅ Improved sharply |
| Working capital | $1,045M | **$1,055M** | ✅ |
| **Altman Z-Score** | 2.59 (Grey, book-equity basis) | **~3.28 book / ~4.9 mkt-cap** | ✅ Safe zone |
| **Piotroski F-Score** | **7 / 9** | n/a | ✅ Moderate-strong |
| FCF (period) | $394.7M | ~$500M est. (gap) | ✅ |
| FCF yield | 2.98% | ~3.8% est. | Adequate |

**Z-Score reconciliation (important):** The tool's 2.594 for FY2025 uses *book* equity (X4 = 0.417). Substituting market cap ($13.2B / $4.08B liabilities = 3.24) lifts the score to **~4.9 — firmly in the safe zone**. The tool explicitly flags this limitation; on the standard public-company basis BTSG is not in distress territory.

**F-Score detail (7/9):** Points lost on **F7 (dilution)** and **F8 (gross margin)**. Both are real and I weight them heavily — see red flags. Points gained on ROA, operating cash flow, accruals quality, declining leverage, and asset turnover.

**Data gaps flagged:** (a) No confirmed issuer credit rating or CDS spread — my searches returned unrelated issuers; ratings are not in the data feed. (b) No quarterly cash flow statements, so LTM FCF is **my estimate**, not reported. (c) Market cap is inconsistent across tools ($13.24B profile vs $14.70B used in the FCF-yield calc); I use $13.2B.

---

## 3. Market Risk Profile

| Metric | Value | Comment |
|---|---|---|
| Annualised volatility (1y) | **44.2%** | ~2.2x a typical index; high |
| Beta vs SPY (1y daily) | **1.13** | |
| Beta (5y monthly, FMP) | **1.85** | Conflicts with above |
| Max drawdown (1y window) | **23.6%** | Tool output |
| Max drawdown since IPO | **~–34.6%** | $12.14 (1/26/24) → $7.94 (3/14/24) |
| Sharpe ratio | **2.00** | Strong, but see caveat |
| Sortino ratio | n/a | Not available |

**Interpretation:**
- **Beta is unresolved (data gap):** the two sources (1.13 vs 1.85) disagree by 64%. BTSG only IPO'd in January 2024, so any "5-year" beta is unreliable. I would underwrite to the **higher 1.5–1.85** for downside modelling — this is a levered, sponsor-influenced, reimbursement-exposed small/mid-cap, which behaves cyclically in drawdowns regardless of the measured beta.
- **Volatility of 44% is elevated but not extreme** for a recent-IPO healthcare services name with a concentrated ownership structure.
- **The 23.6% max drawdown understates tail risk.** Within the ~2.8-year trading history there were two separate >30% peak-to-trough declines (–34.6% in Q1 2024 post-IPO; –32.6% Jan–Mar 2025). A "3-year max drawdown" is not computable — **only ~2.8 years of price history exists**. Flag explicitly.
- **Sharpe of 2.00 should be discounted.** It captures the extraordinary 2026 re-rating ($41 → $67, +61% since Feb 2026) and uses a 0% risk-free rate; with T-bills near 4%, the true excess-return Sharpe is meaningfully lower. It is a *momentum* artifact, not evidence of low risk.

**Valuation risk (equity-level):** EV ≈ $14.9B on $709M LTM EBITDA = **~21x EV/EBITDA** (~16x on adjusted EBITDA). There is **no valuation cushion for a business shock** — see scenario below.

---

## 4. Downside Scenario: –20% Revenue

A 20% revenue decline is severe but not fanciful for this business — the exposure is concentrated in Medicare/Medicaid and pharmacy reimbursement, where a policy or rate change transmits directly to revenue. Critically, BTSG has **extreme operating leverage**: the 12.5% LTM gross margin absorbs almost all fixed-cost coverage, and SG&A is only 8.9% of revenue.

**LTM baseline:** Revenue $15,251M | Gross profit $1,906M (12.5%) | SG&A $1,355M | EBITDA $709M | EBIT $551M | Interest $145M

| Line item | Base | Stress A (SG&A flexes –5%) | Stress B (no cost action) |
|---|---|---|---|
| Revenue | 15,251 | 12,201 | 12,201 |
| Gross profit @12.5% | 1,906 | 1,525 | 1,525 |
| SG&A | 1,355 | 1,287 | 1,355 |
| **EBITDA** | **709** | **238** | **170** |
| EBITDA margin | 4.65% | 1.95% | 1.39% |
| D&A | 158 | 158 | 158 |
| **EBIT** | **551** | **79** | **12** |
| Interest | 145 | 145 | 145 |
| **EBIT / interest** | **3.80x** | **0.55x ❌** | **0.08x ❌** |
| Net debt / EBITDA | 2.34x | **7.0x** | **9.8x** |
| FCF (after ~$110M capex) | ~$500M | **≈ $0 to –$50M** | **Negative** |

**Reading this correctly — two offsets matter:**
1. Stress A/B assume gross margin *holds*. In reality a volume/reimbursement shock would likely be partly offset by variable cost flex, so a **more realistic central stress is EBITDA of $330–400M** (SG&A partially flexed, some COGS variability). That implies **net leverage 4.2–5.1x** and **EBIT coverage of 1.2–1.6x**.
2. **Liquidity is the shock absorber, not the P&L.** Against a ~$1.19B liquidity pool and a 2031 maturity, even the harsh case is a *covenant and ratings* problem, not a *solvency* problem. There is no maturity wall to trip over — the company would have 4+ years to repair the business.

**Verdict:** A 20% revenue shock is **survivable without refinancing risk**, but it would push reported net leverage to 4–5x, likely trigger a downgrade into the B category, and — with the equity at 21x EV/EBITDA — invite a severe de-rating. Sensitivity of the *equity* to this scenario is far greater than sensitivity of the *enterprise*.

---

## 5. Overall Financial Risk Rating: **MODERATE**

*(Improving from High. This is a genuinely better credit than the FY2025 GAAP numbers suggest, but the margin structure leaves little room for error.)*

**Supporting:** rapid and real deleveraging ($958M net debt reduction in nine months); coverage nearly doubled; interest expense down 36% y/y; $1.19B liquidity; no maturities until Feb 2031; positive and growing FCF; F-Score 7; Z-Score in safe zone on a market-cap basis.

**Restraining:** 4.65% EBITDA margin means a modest revenue shock becomes a large EBITDA shock; negative tangible equity; goodwill/intangibles at 48% of assets; volatile cash conversion history; persistent dilution; equity priced for perfection.

---

## 6. Key Red Flags

1. **Extreme operating leverage / thin margin — the single biggest risk.** 4.65% LTM EBITDA margin. A 20% revenue decline removes 45–76% of EBITDA depending on cost action. This is a business that converts a normal cyclical/regulatory event into a credit event. The current margin expansion is the tailwind; the framework has no asymmetry cushion.

2. **Negative tangible book equity of –$843M** (equity $2,186M less goodwill/intangibles $3,029M). Goodwill+intangibles are **48.3% of total assets**. A single impairment charge would erase a large share of book equity and mechanically re-inflate leverage ratios. This is the most under-appreciated balance-sheet risk here.

3. **Gross margin is structurally compressing while revenue grows.** Gross margin fell from **14.1% (FY2024) → 11.8% (FY2025) → 12.5% (LTM)** as the mix shifts toward lower-margin pharmacy. This is why F-Score loses the F8 point. Revenue +26% while gross profit grows far slower — the operating leverage is currently being won back through SG&A (12.3% → 8.9% of revenue), and that lever has finite room.

4. **Dilution and dilution overhang.** Weighted diluted shares rose from 193.0M (FY2024) to 202.6M (FY2025), **+5.0%**, with no buyback to offset (F-Score F7 = 0). Worse: **diluted outstanding 219.8M vs basic 202.6M — a 17.2M (~8.5%) gap** of dilutive instruments. Shareholders are absorbing meaningful ongoing dilution.

5. **Cash conversion has been erratic.** Operating cash flow collapsed to **$23.8M in FY2024** from $210.8M in FY2023 (a –$270M working-capital swing), producing **negative FCF of –$57M**. It recovered to $490M in FY2025. With receivables at $1,216M and inventory at $672M against revenue growing >25%, working capital is a live risk to FCF quality. LTM cash flow is unverified — **no quarterly cash-flow data available**.

6. **Adjusted-vs-reported EBITDA gap of ~$219M (~31%).** Company-reported leverage of 1.79x implies ~$928M of adjusted EBITDA versus $709M reported. The bridge (SBC $70M + acquisition/restructuring costs) is large relative to the ~$145M interest bill. My credit conclusions use **reported** EBITDA deliberately; any investor relying on the 1.79x figure is accepting a materially different credit.

7. **Equity valuation, not solvency, is the fragile link.** ~21x EV/LTM EBITDA on a 4.65%-margin, 1.1x-levered business. A 44% vol, 1.5–1.85 beta, and two separate >30% drawdowns since IPO confirm the market prices this with a hair trigger.

---

### Explicit data gaps
- **No confirmed credit rating or CDS spread** — the biggest gap; my sub-IG classification is inferred from leverage/coverage, not an agency opinion.
- **No quarterly cash-flow statements** → LTM FCF (~$500M) and FCF yield are estimates.
- **Covenant detail unavailable** — I cannot confirm headroom on the Term Loan B financial covenant; treat as unquantified.
- **Beta is unreliable (1.13 vs 1.85)** and **only ~2.8 years of price history exists** — a true 3-year max drawdown, Sortino ratio, and long-run beta are not computable for this recent IPO.
- No peer benchmarking was performed; sector-relative leverage judgment is absent from this note.
