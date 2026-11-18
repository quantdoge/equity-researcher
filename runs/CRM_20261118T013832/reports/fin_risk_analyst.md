# Fin Risk Analyst

- Symbol: CRM
- Elapsed: 106.7s

---
# Financial Risk Assessment — Salesforce, Inc. (CRM)

**Analysis date:** FY2026 10-K (period ended 2026-01-31) plus quarterly data through Q2 FY2027 (2026-07-31). Price/market data as of ~2026-11.

**Headline finding:** Salesforce's *operating* credit quality is excellent and improving. But the balance sheet has been **transformed in six months by a debt-funded buyback**, and every leverage and coverage metric has deteriorated sharply. This is no longer the fortress balance sheet of FY2026. The risk is not solvency — it is that the margin of safety has been spent on share repurchases at a cyclical and narrative low.

---

## 1. Credit Risk Assessment

**Rating: Investment Grade (upper tier) — but with a materially weakened trajectory.**

| Evidence | Reading |
|---|---|
| S&P senior unsecured | **'A+'** (assigned 2026-03-11 to new senior unsecured notes) |
| Moody's | Not confirmed in retrieved sources — **data gap** |
| Net debt / EBITDA (TTM operating) | **2.40x** (was 0.58x at FY2026) |
| Interest coverage (TTM) | **8.9x** (was 25.7x at FY2026) |
| Interest coverage (Q2 FY27 run-rate) | **~4.9x** |
| Altman Z (FY2026, as reported) | 1.499 — "Distress" zone |
| Altman Z (pro-forma, Jul-2026 B/S) | **~1.06** book-equity basis; ~1.77 on market cap |

**The decisive event.** In Q1 FY2027 Salesforce repurchased **$27.2B of stock in a single quarter** — roughly two years of free cash flow. Total debt rose from **$17.2B to $41.9B** and total equity fell from **$59.1B to $38.4B** (−35%) in six months. Net debt went from **$7.6B to $30.3B**. Interest expense ran at $67M/quarter through FY2026; it hit **$317M in Q1 FY27 and $473M in Q2 FY27** — an annualised run-rate near $1.9B, roughly 6x the prior year.

This is a deliberate, disclosed capital-structure decision, not distress. But it converts an equity-risk story into a credit-risk story. The 'A+' rating was assigned *during* this leveraging window and may not yet reflect the full pro-forma capital structure — treat it as stale.

**Why the Altman Z-score misleads here (and why I still flag it).** The model penalises Salesforce structurally: working capital is negative because of unearned (deferred) revenue — a customer-funded, non-cash liability that is a *sign of prepaid demand*, not a liquidity problem; and asset turnover is depressed by $65.4B of goodwill from the Slack/Tableau/MuleSoft/Informatica deals. The Z-score should not be read literally. That said, the direction of travel is real: pro-forma Z falls to ~1.06, and even substituting market cap for book equity (the standard public-company version) yields ~1.77 — still below the 1.81 distress threshold. **This is the first time in years CRM screens as distressed on any standard model.**

---

## 2. Key Financial Risk Metrics

### Leverage & Coverage (the deterioration is the story)

| Metric | FY2024 | FY2025 | FY2026 (Jan-26) | Q2 FY2027 (Jul-26) | Change |
|---|---|---|---|---|---|
| Total debt | $12.59B | $11.39B | $17.18B | **$41.74B** | +143% vs FY26 |
| Cash & ST inv. | $14.19B | $14.03B | $9.57B | $11.40B | — |
| Net debt | $4.12B | $2.54B | $7.61B | **$30.34B** | 4.0x |
| Total equity | $59.65B | $61.17B | $59.14B | **$38.38B** | −35% |
| Debt / equity | 0.21x | 0.19x | 0.29x | **1.09x** | 3.8x |
| Debt / assets | 0.13x | 0.11x | 0.15x | **0.38x** | 2.5x |
| Equity / assets | 0.60x | 0.59x | 0.53x | **0.35x** | — |
| Net debt / EBITDA | 0.4x | 0.2x | 0.58x | **2.40x** | 4.1x |
| Interest coverage (EBIT/int.) | n.m. | 28.2x | 25.7x | **8.9x TTM / ~4.9x fwd** | −81% |

*Note: net debt = total debt less cash & short-term investments. The data feed's separate `net_debt` field reports $33.4B at Jul-26 and $9.85B at Jan-26; the difference appears to be treatment of short-term investments. I use the more conservative-to-neutral total-debt-less-cash figure and flag the inconsistency.*

### Liquidity

| Metric | FY2026 | Q2 FY2027 | Comment |
|---|---|---|---|
| Current ratio | 0.76 | **0.84** | Sub-1.0, but deferred-revenue distortion |
| Quick ratio | 0.76 | n/a | No inventory (software) |
| Cash ratio | 0.26 | 0.43 | Improving |
| Working capital | −$8.90B | −$4.25B | Negative = unearned revenue |
| Cash | $9.57B | $11.40B | Ample |
| Cash / current liabilities | 0.18 | 0.43 | — |
| Short-term debt | $4.00B | **$0.00B** | FY27 maturity was refinanced into long-term |

**Liquidity verdict: adequate.** The current ratio below 1.0 is a *feature* of the subscription model, not a defect — deferred revenue is cash already collected. **Data gap:** the feed does not break out current unearned revenue, so I cannot compute a clean ex-deferred-revenue current ratio. Historically this adjustment lifts CRM's current ratio well above 1.0. Critically, **short-term debt is now zero** — there is no refinancing cliff inside 12 months, and the entire $39.3B sits in long-term maturities.

### Cash Generation (genuinely strong)

| Metric | FY2023 | FY2024 | FY2025 | FY2026 | Trend |
|---|---|---|---|---|---|
| Revenue | $31.35B | $34.86B | $37.90B | $41.53B | +9.6% (decelerating) |
| Gross margin | 73.3% | 75.5% | 77.2% | **77.7%** | Expanding |
| Operating margin | 3.3% | 14.4% | 19.0% | **20.1%** | Strong expansion |
| Free cash flow | $6.31B | $9.50B | $12.43B | **$14.40B** | 3-yr CAGR 31.6% |
| FCF margin | 20.1% | 27.3% | 32.8% | **34.7%** | Expanding |
| SBC | $3.28B | $2.79B | $3.18B | $3.51B | 8.5% of revenue |
| FCF less SBC | $3.03B | $6.71B | $9.25B | **$10.89B** | 26.2% margin |
| FCF yield | — | — | — | **~8.9%** (7.74% on feed's cap) | Very high |

FY2026 capital returns were **$14.18B (buybacks $12.60B + dividends $1.59B) = 98.5% of FCF**. That is the crux: capital returns were already at 100% of FCF *before* the debt-funded $27.2B buyback. FCF conversion (FCF/net income) is 193%.

**Piotroski F-Score: 7/9** ("Moderate"). Points lost on F5 (leverage rose) and F6 (equity declined) — both directly attributable to the buyback. Post-Q1 FY2027, leverage is far higher, so the score's quality is more fragile than the 7 suggests.

---

## 3. Market Risk Profile

| Metric | Value | Comment |
|---|---|---|
| Annualised volatility (3y) | **40.75%** | Very high for a mega-cap |
| Beta vs SPY (3y, computed) | **0.847** | Below market |
| Beta (FMP profile, 5y) | 1.238 | **Discrepancy flagged** — different window/frequency |
| Max drawdown (3y) | **58.67%** | Peak ~$363 (Dec-2024) to trough ~$155 (mid-2026) |
| Sharpe ratio | **−0.135** | Negative risk-adjusted return |
| Sortino ratio | **Not available — data gap** | — |

**The most important market-risk insight:** volatility of 40.75% with a beta of only ~0.85 means **roughly 94% of CRM's variance is idiosyncratic, not market-driven.** Salesforce will not be protected in a market drawdown by low beta, because its risk is single-name narrative risk, not systematic risk. A −58.7% peak-to-trough drawdown and a negative three-year Sharpe confirm shareholders have been paid nothing for that risk.

The driver is well documented: the stock fell **40.9% in H1 2026** in what the market has termed the "SaaSpocalypse," on fears that agentic AI will compress seat-based SaaS pricing. This is a *business-model* risk that flows directly into credit risk — it is the same force that made management retire equity at the bottom.

---

## 4. Downside Scenario Analysis — Revenue −20%

Applied to the **post-buyback** capital structure (net debt $30.34B, forward interest run-rate $1.89B). TTM revenue ~$43.9B, TTM operating EBITDA ~$12.66B.

| Line item | Base (TTM) | Downside (−20% rev) | Severe (−20% rev, GM→73%) |
|---|---|---|---|
| Revenue | $43.9B | $35.1B | $35.1B |
| Gross margin | 77.3% | 76.0% | 73.0% |
| Gross profit | $33.96B | $26.71B | $25.66B |
| Opex (assume −12% / −8% cost action) | $25.22B | $22.19B | $23.20B |
| **Operating income** | **$8.74B** | **$4.52B** (12.9% mgn) | **$2.46B** (7.0% mgn) |
| EBITDA | $12.66B | $8.44B | $6.38B |
| **Net debt / EBITDA** | **2.40x** | **3.59x** | **4.76x** |
| **Interest coverage (fwd)** | **~4.9x** | **~2.4x** | **~1.3x** |
| FCF (approx.) | ~$14.2B | ~$10.5B | ~$8.5B |

**Interpretation.** Even in the severe case, CRM remains cash-generative ($8.5B FCF), covers its $1.46B dividend ~6x, and has no maturity inside 12 months. **Solvency is not at risk.** But interest coverage at 1.3–2.4x in stress is sub-investment-grade territory — the kind of number that triggers a multi-notch downgrade and restricts refinancing access exactly when it is needed.

**The mitigant that saves this credit:** the buyback is entirely discretionary. Suspending it (as they effectively did in Q2 FY27 — only $84M repurchased) throws off ~$10–14B of annual FCF for deleveraging. At that pace, net debt of $30.3B returns below 1.0x EBITDA within roughly three years even in the downside case. **The credit survives because the cash flow engine is intact; it is impaired only in the sense that the cushion was voluntarily surrendered.**

---

## 5. Overall Financial Risk Rating

# **MODERATE (elevated, and rising)**

**Rationale.** Downgraded from what would have been "Low" twelve months ago. Justification for not going to "High":
- FCF is $14.4B, growing, at a 34.7% margin, with conversion of 193% of net income
- Cash of $11.4B against **zero** short-term debt
- Operating margin expanded 3.3% → 20.1% in four years
- Revenue growth actually *re-accelerated* to 13.3% / 10.8% in Q1/Q2 FY2027, contradicting the disruption bear case
- A-rated, and the buyback — the source of all the leverage — is discretionary

Justification for the upgrade in risk from "Low": net leverage 4.1x higher, coverage down 81%, tangible equity now **−$27.0B**, and the equity base down 35% in two quarters.

**Split verdict:** Credit risk = **Investment Grade, stable**. Equity/market risk = **High**. The two have decoupled because management swapped equity for debt at a depressed multiple.

---

## 6. Key Red Flags

1. **$27.2B single-quarter buyback funded by ~$24.7B of new debt.** Debt rose 143% in six months; net debt rose 4x to $30.3B. This is the dominant risk fact in the entire assessment.
2. **Interest coverage collapsed from 25.7x to 8.9x TTM, ~4.9x forward run-rate.** Under a −20% revenue shock, forward coverage falls to
