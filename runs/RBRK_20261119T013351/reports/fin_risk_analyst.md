# Fin Risk Analyst

- Symbol: RBRK
- Elapsed: 72.6s

---
## RUBRIK, INC. (RBRK) — FINANCIAL RISK ASSESSMENT
*As of market close 2026-09-30 (price $114.47). FY ends Jan 31. Latest balance sheet: FY2026 (2026-01-31); latest P&L: Q2 FY2027 (2026-07-31).*

**Framing note — this is a liquidity-strong, GAAP-unprofitable, equity-risk-heavy story.** The credit is not the problem; the price is. Rubrik carries ~$1.1B of debt that is almost entirely a 0% coupon convertible with no maturity until 2030, sits on $1.68B of cash, and generates positive FCF. But it has negative book equity, a −26% operating margin, and one of the highest volatility profiles in large-cap software.

---

### 1. CREDIT RISK ASSESSMENT — **Sub-Investment Grade (BB-/Ba3-equivalent), stable-to-positive**

Unrated by the agencies (no public rating, no CDS — **data gap**). On fundamentals it screens *below* investment grade solely because of GAAP unprofitability and negative equity, not because of any refinancing or default pressure:

- **Debt is structurally benign.** Total debt $1,130.7M, of which ~$1.0B is the **0.00% Convertible Senior Notes due June 15, 2030** (initial conversion rate 8.0155 sh/$1,000 → **conversion price ≈ $124.76**; ~$130.7M residual classified as long-term debt, likely finance leases/legacy notes). **Short-term debt = $0.** No maturity inside ~3.75 years, and **zero cash coupon** — GAAP interest expense of $17.2M is largely non-cash issuance-cost amortization.
- **Net cash on a financial-debt basis: $545.1M** (cash + ST investments $1,675.8M vs. $1,130.7M debt).
- Equity-linked, not credit-linked: at $114.47 the converts are 8% out of the money. If the stock clears $124.76, $1.0B converts into ~8.0M shares (≈3.9% dilution) instead of being repaid — a *deleveraging* event, not a cash call.
- **Interest coverage is not meaningful** (see table) because EBIT is negative. The economically relevant coverage is cash-based: **FCF / interest expense = 14.7x**, and cash interest is effectively nil.

**Verdict: probability of a credit event before 2030 is very low. This is not a solvency story.**

---

### 2. KEY FINANCIAL RISK METRICS

| Metric | Value | Read |
|---|---|---|
| Total debt | $1,130.7M | ~$1.0B 0% converts due Jun-2030 |
| Cash + ST investments | $1,675.8M | 1.28x current liabilities |
| **Net debt (fin. debt basis)** | **−$545.1M (net cash)** | Positive |
| Debt / assets | 41.0% | Elevated but non-cash-coupon |
| Debt / equity | **−2.18** | **n.m. — negative equity** |
| Equity / assets | **−19%** | Retained earnings −$3,186M |
| Net debt / EBITDA | 2.0x (tool) | **INVALID — EBITDA is −$272.1M**; sign artifact |
| Interest coverage (EBIT/interest) | **−17.9x to −20.1x** | **n.m. — negative EBIT** |
| FCF / total debt | 22.4% | Comfortable |
| Current ratio / Quick ratio | 1.69 / 1.69 | Adequate (no inventory) |
| Cash ratio | 1.28 | Strong |
| Working capital | $909.5M | Positive |
| **Altman Z-Score** | **−1.21 (Distress zone)** | Distorted by negative book equity |
| Altman Z (market-cap x4, my recalc) | **≈ +3.02** | At the safe-zone threshold |
| **Piotroski F-Score** | **6 / 9 (Moderate)** | Failed: positive ROA, no dilution, asset turnover |
| FCF (FY2026) | $253.3M | FCF margin 19.2% |
| **FCF yield** | **1.17%** | Low — priced on growth |
| SBC (FY2026) | **$329.4M (25.0% of revenue)** | **Exceeds FCF** |

**Critical data inconsistency flagged:** the balance-sheet feed reports `net_debt = $750.5M` while the ratio tool (total debt − cash) reports **−$545.1M**. Reconciling, $750.5M + $1,675.8M = **$2,426.3M implied gross obligations**, i.e. **~$1.30B beyond reported total debt** — most plausibly operating lease liabilities. If real, adjusted net leverage is ~$750M, or ~2.5x FY27E FCF and ~0.45x ARR: still low, but the company is *not* net-cash on an all-obligations basis. **This should be resolved from the 10-Q lease footnote before any credit conclusion is finalized.**

---

### 3. MARKET RISK PROFILE — **High**

| Metric | Value |
|---|---|
| Annualised volatility (365d) | **66.55%** |
| Beta vs SPY (365d daily) | **1.786** |
| Max drawdown (365d window) | **−52.0%** |
| Sharpe ratio | 0.79 |
| Sortino ratio | **Data gap** (not computed) |

- **Beta discrepancy:** the company profile reports 1.081; the computed 365-day beta is **1.786**. I use 1.79. The profile figure is almost certainly understated given the April-2024 IPO — there is **less than 3 years of trading history**, so a true 3-year max drawdown and a stable beta are **not available (data gap)**.
- Observed peak-to-trough on closes: **$98.50 (9-Sep-2025) → $42.25 (10-Apr-2026) = −57%**, then **+171% to $114.47**. This is a 1.8-beta, 66%-vol instrument that lost more than half its value in seven months and then tripled. Position sizing risk dominates fundamental risk.
- Sharpe of 0.79 looks tolerable only because it is measured from the April 2026 trough; it is regime-dependent and not a reliable indicator.

---

### 4. DOWNSIDE SCENARIO ANALYSIS — revenue −20%

Base case (my estimate, not company guidance — **guidance figures not retrieved**): FY2027E revenue ≈ **$1.72B** (H1 FY27 actual $814.4M; Q2 FY27 revenue $427.3M, +37.9% YoY, ARR $1.66B +33%); FY27E FCF **$293–303M** (per Q1 FY27 guidance).

**Scenario: revenue −20% to $1.38B, gross margin ~78%, discretionary opex cut 15%**

| Line | Base (FY27E) | −20% Revenue | −30% + no cost cuts |
|---|---|---|---|
| Revenue | $1,720M | $1,376M | $1,204M |
| Gross profit (78%) | $1,342M | $1,073M | $943M |
| Operating expenses | ~$1,610M | ~$1,370M | ~$1,610M |
| GAAP operating income | ~−$268M | **−$297M** | **−$667M** |
| + D&A / + SBC | +$50M / +$400M | +$50M / +$400M | +$50M / +$400M |
| Working capital (deferred rev.) | +$150M | ~$0 (churn drag) | **−$150M** |
| Capex | −$35M | −$35M | −$35M |
| **Free cash flow** | **+$293–303M** | **≈ +$118M** | **≈ −$402M** |

**Conclusion:** a 20% revenue decline still leaves the company **FCF-positive**. Even the severe case (−30%, no cost flex, negative working capital) burns ~$400M/yr against $1.68B cash and **no maturity until mid-2030** → **~4 years of runway**, i.e. no liquidity event. The downside does not express itself in the capital structure; it expresses itself in the **equity**, which already demonstrated a −57% drawdown on far less.

**Valuation sensitivity (the real downside):** EV ≈ $22.1B (mkt cap $22.64B + ~$0.5B net cash adjustment) → **~13.3x EV/ARR** and **1.17% FCF yield**. A growth deceleration from 33% ARR to high-teens would compress the multiple toward 6–8x ARR, implying **−40% to −55% equity downside with no change in credit quality.**

---

### 5. OVERALL FINANCIAL RISK RATING: **MODERATE**

Decomposed: **Credit risk — Low-to-Moderate. Liquidity risk — Low. Market/valuation risk — High.** The blended rating is Moderate because the balance sheet is genuinely defensive while the security is not.

**Supporting strengths:** FCF positive and inflecting ($253.3M FY26 → $293–303M FY27E); FCF margin ~19%; gross margin ~80%; no short-term debt; $1.68B cash; current ratio 1.69; Piotroski 6; ARR +33%, revenue +38% YoY; operating margin improved from −30.5% to −16.8% YoY in Q2 FY27.

---

### 6. KEY RED FLAGS

1. **FCF quality is poor.** FY2026 SBC of **$329.4M exceeds FCF of $253.3M**. Reported FCF is *entirely funded by non-cash compensation*; **FCF ex-SBC ≈ −$76M**. Growth in FCF is partly optics. This is the single most important adjustment to the bullish cash narrative.
2. **Negative shareholders' equity (−$519.6M)** with retained earnings of −$3.19B; equity/assets −19%. Formally insolvent on a book basis.
3. **Altman Z of −1.21** in the distress zone. Only rescued to ~+3.0 by substituting market cap for book equity — a reminder that this company's solvency *depends on its share price*.
4. **Unresolved ~$1.30B of implied obligations** (likely operating leases) in the balance-sheet feed. Could not verify. **Data gap requiring 10-Q follow-up.**
5. **Interest coverage of −18x to −20x is not informative** and should not be cited as a distress signal; conversely, net debt/EBITDA of "2.0x" is a sign-flip artifact on negative EBITDA and must not be cited as leverage comfort.
6. **Extreme market risk:** 66.6% vol, 1.79 beta, −52% max drawdown, −57% peak-to-trough in 7 months, then +171%. Beta of 1.79 implies ~1.8x market drawdown amplification.
7. **Near-the-money convertible:** conversion price ~$124.76 vs. $114.47 spot. Above that level ~8.0M shares (3.9%) are issued; below it, $1.0B cash repayment is due Jun-2030 (covered 1.7x by cash, so low risk either way).
8. **Valuation risk:** 13.3x EV/ARR and 1.17% FCF yield leave no room for growth disappointment.
9. **Gross margin compression:** Q2 FY27 78.4% vs. Q2 FY26 79.5% (−110bp) and FY2026 80.1% — early sign of mix/AI-infrastructure cost pressure; monitor.
10. **Data gaps:** no public credit rating or CDS; no quarterly cash-flow statements (SBC/OCF trends only annual); no debt maturity schedule by year; no Sortino ratio; <3 years of trading history precludes a true 3-year drawdown. Company guidance figures for FY2027 were not retrievable (press release returned HTTP 403) — FY27E revenue is my estimate.
