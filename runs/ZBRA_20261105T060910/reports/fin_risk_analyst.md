# Fin Risk Analyst

- Symbol: ZBRA
- Elapsed: 52.6s

---
## ZBRA — Financial Risk Assessment

**Zebra Technologies Corp.** | Technology / Communication Equipment (AIDC) | Price $332.44 | Mkt cap ~$17.0B | Employees 10,700
*Data through FY2025 (period end 2025-12-31, filed 2026-02-12). No interim 2026 data returned by tools — see gaps.*

---

### 1. Credit Risk Assessment — **SUB-INVESTMENT GRADE (BB+)**

S&P rates ZBRA **'BB+'**, affirmed, explicitly tied to the belief the company can "refinance its upcoming bank debt maturities in the second half of 2026." That is the single most important fact in this assessment: this is a **speculative-grade credit with a 2026 refinancing event pending.**

The company has a **$3.25B senior secured credit facility (SOFR + 1.00%) maturing May 25, 2027**, with the revolver's average rate at 5.01%. Current curve (as of 2026-11-05): 2Y 4.74%, 5Y 4.93%, 10Y 5.13%, 30Y 5.47% — **no inversion, positively sloped, with a term premium**. Refinancing into a 5.0–5.5% environment implies a step-up from the current blended ~4.2% cost (interest $108M / avg debt ~$2.6B). On $2.8B of debt, a 130bp repricing adds ~$35M of annual interest — roughly 8% of net income.

Leverage is **deteriorating, not deleveraging**: net debt rose from $1,461M to $2,691M (+84% YoY) while EBITDA *fell* from $937M to $853M. The company funded a ~$1.2B acquisition (goodwill + intangibles +$1,228M) *and* $587M of buybacks with debt and a $776M drawdown of cash.

### 2. Key Financial Risk Metrics

| Metric | FY2025 | FY2024 | FY2023 | Read |
|---|---|---|---|---|
| Total debt | $2,816M | $2,362M | $2,414M | +19% YoY |
| Net debt | $2,691M | $1,461M | $2,277M | **+84% YoY** |
| Net debt / EBITDA | **3.15x** | 1.56x | 2.99x | Back above 3x |
| Debt / equity | 0.78x | 0.66x | 0.80x | — |
| Debt / assets | 0.33x | 0.30x | 0.33x | — |
| Interest coverage (EBIT) | **6.19x** | 5.93x | 4.40x | Adequate |
| Interest coverage (op. income, tool basis) | 7.41x | — | — | Adequate |
| Current ratio | **0.97x** | 1.43x | 1.05x | Below 1.0 |
| Quick ratio | **0.58x** | — | — | Weak |
| Cash ratio | **0.07x** | — | — | Very weak |
| Working capital | **–$56M** | +$736M | +$74M | Deficit |
| Cash | $125M | $901M | $137M | **–86% YoY** |
| Altman Z-Score | **2.19 (Grey)** | — | — | Distress-adjacent |
| Piotroski F-Score | **6 / 9 (Moderate)** | — | — | Cracks showing |
| FCF | $831M | $954M | –$91M | –13% YoY |
| FCF margin | 15.4% | 19.2% | –2.0% | Deteriorating |
| FCF yield | 4.88% | — | — | ~5.3% on profile mcap |

**Altman Z detail:** x1 (WC/TA) **–0.007**, x2 (RE/TA) 0.62, x3 (EBIT/TA) 0.079, x4 (book equity/TL) 0.73, x5 (sales/TA) 0.63. The negative x1 is a genuine structural flag. Restating x4 at market value ($17.0B / $4,914M = 3.46) lifts Z to approximately **2.85 — still inside the grey zone** and short of the 2.99 safe threshold. Both book and market variants agree: no margin of safety.

**F-Score breakdown (6/9):** positive (ROA > 0, positive operating CF, accruals quality, no dilution, asset turnover improvement). **Failing:** ROA declined, **leverage increased**, **gross margin did not improve**.

### 3. Market Risk Profile — **HIGH**

| Metric | Value |
|---|---|
| Annualised volatility (756d) | **45.11%** |
| Beta vs SPY | **1.63** (profile: 1.58) |
| Max drawdown (3yr) | **–52.67%** |
| Sharpe ratio | **0.214** |
| Implied 3yr annualised return | ~9.7% total / ~3.1% p.a. |
| Sortino | **Not available** (tool gap) |

45% volatility for a $17B business with 15% FCF margins is extreme — it prices ZBRA as a cyclical, not a compounder. A 1.63 beta plus a 52.7% realized drawdown means **a 20% market decline historically transmitted to roughly a 33% ZBRA decline.** Reward for that risk has been poor: ~3.1% p.a. over three years against 45% vol. This is a fundamentally unfavourable risk-adjusted profile — you are not being paid for the beta.

### 4. Downside Scenario Analysis — Revenue –20%

**The most valuable datapoint here: ZBRA already ran this experiment.** FY2022→FY2023 revenue fell 20.7% ($5,781M → $4,584M). The observed result:
- EBIT fell $936M → $585M (–$351M, a **29% incremental margin** on the revenue decline)
- **Operating cash flow collapsed to –$4M** (from +$488M) — a $515M working-capital *use*
- **Free cash flow went to –$91M**
- Gross margin actually *held* (45.4% → 46.3%); the damage was operating leverage and working capital

That is the crux of the credit story: **in the last 20% revenue decline, this company did not generate free cash flow.** It burned it.

**Modelled –20% case on FY2025 base** (revenue $4,317M):
- Gross margin holds at 45.9% (2023 precedent) → GP $1,982M; opex flexes ~8% → $1,545M
- **EBIT ≈ $437M**, EBITDA ≈ $622M
- Interest coverage falls to **~4.0x**
- **Net debt / EBITDA rises to ~4.3x** — likely through any 3.5x maintenance covenant on the secured facility
- FCF falls to roughly **$250–350M**; the $587M buyback becomes unfundable and must be cut entirely

**Severe case** (gross margin –250bps to 43.4%, opex flexes only 5%):
- **EBIT ≈ $279M**, EBITDA ≈ $464M → coverage **2.6x**, **net debt/EBITDA ≈ 5.8x**
- FCF approaching zero to modestly negative after working capital

**Liquidity in the downside is the binding constraint.** At $125M of cash, a 0.97 current ratio, and $141M of short-term debt, the company has essentially **zero standalone liquidity** and is entirely dependent on the revolver to bridge. The revolver exists ($3.25B facility) and is the reason this is not a distress case — but the drawn amount is unknown, and the facility matures May 2027, *after* the H2 2026 bank maturities S&P flags.

### 5. Overall Financial Risk Rating — **HIGH**

Not Critical, because: FCF remains $831M positive, interest coverage is 6.2–7.4x, no dividend obligation to defend, and a large secured revolver backstops liquidity. But the combination of **BB+ rating, ~3.2x and rising leverage against falling EBITDA, a 0.97 current ratio with $125M cash, negative tangible equity, an unresolved H2 2026 refinancing, and demonstrated FCF burn in the last downturn** places this firmly in the High bucket. The balance sheet has moved from clearly comfortable (1.56x in FY2024) to constrained in a single year.

### 6. Key Red Flags

1. **Cash down 86%** ($901M → $125M). Cash is now 3% of liabilities. This is the sharpest single-year liquidity deterioration in the dataset.
2. **Buybacks into a leveraged balance sheet.** $587M of repurchases in FY2025 ($751M in FY2022) while debt rose and cash was drained — buying back stock at a 53% peak-to-trough volatility profile with borrowed money.
3. **Goodwill + intangibles $5,536M = 65% of total assets and 154% of book equity.** Tangible equity is **–$1,948M**. A $1.2B acquisition was added in FY2025 into a period of *gross-margin compression* — impairment risk is material and would hit equity and covenants simultaneously.
4. **Negative working capital (–$56M) and current ratio below 1.0.**
5. **Cash generation is not recession-proof.** FY2023: OCF –$4M, FCF –$91M. Directly contradicts any "stable, recurring-revenue" narrative.
6. **EBITDA declining while debt rises.** EBITDA $1,140M (FY2022) → $853M (FY2025), –25%, against debt +17% over the same span. Leverage math is working against the company.
7. **Gross margin –250bps** (48.4% → 45.9%) and **net income –21% despite revenue +8%.** Operating leverage is currently negative.
8. **SBC up 83%** ($89M → $163M), now 3.0% of revenue — inflates EBITDA quality and FCF optics.
9. **Capex at only 1.6% of revenue** ($86M) — low, which flatters FCF but raises a question about under-investment, especially with D&A of $185M running well above capex.
10. **Market risk is severe:** 45% vol, 1.63 beta, 52.7% max drawdown, 0.21 Sharpe.

### Data Gaps (explicitly flagged)

- **No FY2026 interim data** returned by the financial statement tools; latest period is FY2025. The 10-Q referenced in search results (Q1 2026) is not reflected here. **This is the most significant gap** — three quarters of post-acquisition performance are unobserved.
- **Debt maturity schedule by year not obtainable.** Known: revolver matures May 2027; bank maturities due H2 2026 per S&P. Individual tranche amounts unknown.
- **Revolver drawn amount and available capacity unknown** — critical to the liquidity conclusion.
- **R&D not itemised** in the income statement feed (residual opex of ~$593M implied between SG&A and operating income); downside model treats it as largely fixed.
- **CDS spreads unavailable.**
- **Sortino ratio unavailable** from the risk tool.
- **Peer comparables unusable:** `get_sector_peers` returned AAPL, NVDA, MSFT, TSM, AVGO, SKHY, MU, AMD — megacap semiconductors, not AIDC/industrial-tech comparables. No valid peer benchmarking performed.
- **Market cap inconsistency:** profile states $15.73B, but price × diluted shares implies ~$17.0B and the FCF-yield tool used $17.03B. FCF yield is 4.88% on the higher figure, ~5.3% on the profile figure.
- **D&A ($185M) looks low relative to a $5.5B intangible base** — suggests limited amortisation or a classification difference; EBIT/EBITDA quality should be treated with caution.
