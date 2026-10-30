# Fin Risk Analyst

- Symbol: FTNT
- Elapsed: 32.3s

---
# FORTINET, INC. (FTNT) — Financial Risk Assessment

**Sector:** Technology / Software–Infrastructure (Cybersecurity) | **Market Cap:** ~$102.1B | **Price:** $139.10
**Latest annual data:** FY2025 (12/31/2025) | **Latest interim:** Q3-2026 (9/30/2026)
**Analyst note:** Balance sheet data is available only through FY2025 year-end; P&L data extends through Q3-2026. This is flagged where it affects conclusions.

---

## 1. Credit Risk Assessment

**Rating: INVESTMENT GRADE — high quality, effectively net-cash**

Fortinet carries ~$996M of total debt against $3.58B of cash and short-term investments — a **net cash position of ~$1.50B** at FY2025 year-end. This is not a leveraged company; it is a cash-rich company with a legacy bond issue.

| Metric | FY2025 | Assessment |
|---|---|---|
| Net debt / EBITDA | **−1.05x** (net cash) | No leverage risk |
| Interest coverage (EBIT/interest) | **103.6x** (reported); **~189x** on TTM Q3-26 basis | Trivial debt service burden |
| Debt / assets | 0.10 | Very low |
| Debt / equity | 0.81 | *Distorted — see red flag #1* |
| Moody's rating | **Baa1**, outlook stable (assigned to the notes, 2021 vintage) | Lower-tier IG |

Interest expense is **declining** through 2026 — Q4-25 $4.4M → Q1-26 $4.2M → Q2-26 $3.2M → Q3-26 $3.0M — consistent with the ~$500M classified current at FY2025 being retired from cash. **There is no refinancing cliff**: the remaining debt is fully covered by cash on hand several times over, and annual FCF of ~$2.2–2.3B exceeds total debt in under six months.

**Data gap:** No CDS spread data available; Moody's Baa1 is the most recent rating I could confirm (2021 assignment) and may not reflect current positioning. No covenant schedule available — but with 100x+ coverage and net cash, covenant breach is not a credible scenario.

---

## 2. Key Financial Risk Metrics

| Metric | Value | Read |
|---|---|---|
| **Leverage** | | |
| Net debt / EBITDA | −1.05x | Net cash |
| Debt / equity | 0.81 | Inflated by buybacks (see below) |
| Debt / assets | 0.10 | Low |
| **Coverage** | | |
| Interest coverage (EBIT) | 103.6x FY25 / ~189x TTM | Exceptional |
| Operating margin | 30.6% FY25 → 33.9% Q3-26 | Expanding |
| **Liquidity** | | |
| Current ratio | 1.17 | Weak on the surface; deferred-revenue driven |
| Quick ratio | 1.09 | Adequate |
| Cash ratio | 0.71 | Strong |
| Working capital | $866M | Positive |
| Cash & ST investments | $3,582M | vs $996M total debt |
| **Solvency scores** | | |
| Altman Z-Score | **1.50 ("Distress")** | **⚠️ Model artifact — not a real signal** |
| Piotroski F-Score | **6 / 9** (Moderate) | Depressed by buybacks, not operations |
| **Cash generation** | | |
| FCF (FY25) | $2,226M (32.7% margin) | Best-in-class |
| FCF / net income | 120% | High-quality earnings |
| FCF yield | **2.14%** | Low — valuation risk, not credit risk |

**On the Altman Z of 1.50:** I want to be explicit that I do **not** treat this as distress evidence. The score is dragged down by two inputs that are structurally misleading for this company:

- **x2 = −0.049** (negative retained earnings of −$508M) — the cumulative result of ~$7B+ of share repurchases, **not** accumulated losses. Fortinet has been profitable every year.
- **x4 = 0.135** uses *book* equity ($1.24B) rather than market equity (~$102B), understating the score by construction.

The Altman model was also calibrated on manufacturers; subscription-software balance sheets with multi-billion deferred revenue and buyback-depleted equity routinely misclassify. When a company has 189x interest coverage, net cash, and a Baa1 rating, the "distress" output is a false positive. **I weight the Z-score as non-informative here and rely on the direct leverage/liquidity/coverage evidence.**

**On the Piotroski 6/9:** the three lost points are F5 (leverage — debt/assets ticked up trivially), F6 (equity decreased), and F3 (ROA declined as the asset base grew faster than income). All three trace to the $2.29B buyback, not to operating deterioration. The four profitability signals (positive ROA, positive operating cash flow, clean accruals, gross margin expansion) all score in the company's favor, as do F7 (no dilution) and F9 (asset turnover improvement). **Operationally this is a strong 6.**

---

## 3. Market Risk Profile

Measured over a 756-day (~3-year) window vs SPY:

| Metric | Value | Interpretation |
|---|---|---|
| Annualised volatility | **44.3%** | Very high — roughly 2.8x the market's typical vol |
| Beta vs SPY | **1.14** (3-yr calc); 1.04 (profile) | Modestly above market |
| Max drawdown (3-yr) | **−35.1%** | Severe peak-to-trough loss |
| Sharpe ratio | **0.85** (0% rf assumption) | Decent absolute, but earned with high vol |

**The critical risk observation:** FTNT's beta (1.04–1.14) materially *understates* its standalone risk. Annualised volatility of 44.3% implies the stock's total risk is far above what its market sensitivity suggests — i.e., **most of the risk is idiosyncratic, not market-driven**. For a portfolio holder, this means diversification offers limited protection: a Fortinet-specific shock (growth deceleration, a large deal slipping, competitive share loss in SASE/firewall refresh) drives the drawdown, not a market selloff. A 35% drawdown has already occurred within the last three years.

**Data gap:** Sortino ratio not computed by the available tooling; downside-deviation-adjusted return quality is inferred, not measured.

---

## 4. Downside Scenario Analysis — Revenue −20%

Applied to FY2025 base revenue of $6,800M (a −$1,360M hit), holding gross margin near the 79–81% range and flexing opex:

| Line item | Base FY2025 | −20% Revenue (opex flat) | −20% Revenue (10% opex cut) |
|---|---|---|---|
| Revenue | $6,800M | $5,440M | $5,440M |
| Gross profit (~79%) | $5,497M | $4,298M | $4,298M |
| Operating expense | $3,415M | $3,415M | $3,074M |
| **Operating income** | **$2,082M** | **$883M** (−58%) | **$1,224M** (−41%) |
| Interest expense | $20M | $15M | $15M |
| **Interest coverage** | 104x | **~59x** | **~82x** |
| **FCF (est.)** | $2,226M | **~$980M–1,090M** | **~$1,100M–1,250M** |
| FCF margin | 32.7% | ~18–20% | ~20–23% |
| Net debt / EBITDA | −1.05x | ~−0.6x (still net cash) | ~−0.7x (still net cash) |
| Current ratio | 1.17 | ~1.10 | ~1.10 |

**Conclusion: the company survives a 20% revenue shock without any credit stress whatsoever.** Even with opex held completely flat and no management response, EBIT stays near $900M and coverage stays above 50x. FCF remains roughly $1B — enough to retire all outstanding debt in a single year while still generating surplus cash. Cash of $3.58B covers ~3.5 years of the *entire* debt stack. There is no plausible operational scenario in which Fortinet breaches a covenant or faces a liquidity event.

**The real downside transmission channel is equity valuation, not solvency.** With a 2.14% FCF yield, the stock trades on growth expectations. A 20% revenue decline would likely compress the multiple sharply and produce a drawdown well beyond the 35% already seen — the impairment lands on the equity holder, not the creditor. Management's policy of returning >100% of FCF via buybacks amplifies this: in FY2025 buybacks of $2.29B slightly *exceeded* FCF of $2.23B (cash fell from $4.07B to $3.58B), so there is no cash buffer being built against a growth shock.

---

## 5. Overall Financial Risk Rating

# **LOW**

Balance-sheet risk is genuinely negligible: net cash, ~189x TTM interest coverage, debt retired inside a year of free cash flow, no maturity wall, investment-grade rating, and expanding margins. FCF conversion of 120% of net income confirms high earnings quality, and revenue growth re-accelerated to +20.5% YoY in Q3-2026 with operating margin at 33.9% — the fundamental trajectory is strengthening, not deteriorating.

The risks here are **equity risks, not credit risks**: high volatility, a demonstrated 35% drawdown capacity, an idiosyncratic risk profile poorly captured by beta, and a thin FCF yield offering no valuation cushion.

---

## 6. Key Red Flags & Data Gaps

**Red flags (all equity-side, none credit-side):**

1. **Negative retained earnings (−$508M) and thin book equity (12% of assets).** Purely a buyback artifact — over $7B returned cumulatively — but it inflates debt/equity to 0.81x and misfires the Altman Z-score. Limits the optical "fortress balance sheet" story and reduces book-equity-based financial flexibility.
2. **Payout exceeding free cash flow.** FY2025 buybacks of $2.29B vs FCF of $2.23B drew down cash by ~$480M. Aggressive, but sustainable only while FCF holds — it removes the buffer that would absorb a growth shock.
3. **Very low FCF yield (2.14%).** No valuation margin of safety; the multiple is the risk, and multiple compression is the most probable path to equity loss.
4. **High idiosyncratic volatility (44.3% annualised) with beta of only ~1.1.** Diversification provides limited protection against Fortinet-specific shocks. A −35% drawdown is a demonstrated, not hypothetical, outcome.
5. **Current ratio of 1.17.** Superficially weak, but ~$6B+ of the $9.15B liability base is deferred revenue — a customer-funded, non-cash obligation that is economically an asset. This is a reporting artifact, not a liquidity concern, but it means reported liquidity ratios understate true flexibility.
6. **Capex intensity rising** ($205M in FY2023 → $365M in FY2025, 5.4% of revenue) for SASE/cloud infrastructure. Manageable, but a persistent upward trend in a high-multiple name deserves monitoring.

**Explicit data gaps:**
- No Q3-2026 balance sheet available — net cash and leverage figures are as of 12/31/2025. Given declining interest expense through 2026, the true current net cash position is likely *better* than reported.
- Deferred revenue is not broken out as a line item; the current-ratio adjustment is an estimate.
- No CDS spread data; credit rating (Moody's Baa1) is unconfirmed as current.
- Sortino ratio not computed; no peer benchmarking (e.g., PANW, CRWD, ZS) was gathered within budget, so relative leverage/liquidity positioning is unassessed.
- TTM FCF is estimated (~$2.29B) from components; quarterly cash flow statements were not available.
