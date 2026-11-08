# Fin Risk Analyst

- Symbol: HALO
- Elapsed: 50.1s

---
Data retrieval complete. I hit one dead end — the Q4 2025 earnings PDF returned raw binary (unusable), so the exact composition of the Q4 charge is a documented gap. Everything else is solid. Writing the assessment now.

---

# HALO — Halozyme Therapeutics, Inc.
## Financial Risk Assessment
**Sector:** Healthcare / Biotechnology · **Price:** $103.63 · **Market cap:** ~$11.8B · **Employees:** 423
**Base period:** FY2025 (12/31/25, filed 2/17/26) + quarterly data through Q3 CY2026

### Executive Summary

Halozyme is a **royalty-and-milestone platform business**, not a conventional cash-burning biotech. It generates a **46% FCF margin**, carries **~44x interest coverage**, and has **no debt maturing before 2031**. On cash-flow fundamentals this is an investment-grade credit profile wearing a biotechnology label.

However, two reported metrics scream distress and both are **artifacts**, not realities:

1. **Altman Z-Score of 1.537 ("Distress")** — driven entirely by a near-zero *book* equity of $48.8M caused by ~$1.0B of cumulative buybacks. Re-marking equity to market pushes Z to **~4.37 (Safe zone)**.
2. **Net debt/EBITDA of 3.49x** — inflated because vendor EBITDA ($573M) is contaminated by a **one-time, below-the-line Q4 2025 charge of roughly $320–400M**. On a clean operating basis, leverage is **1.8–2.3x**.

My conclusion: **credit risk is LOW, market risk is HIGH, and structural/concentration risk is the real story.** Overall: **MODERATE**.

---

## 1. Credit Risk Assessment

**Rating: INVESTMENT GRADE (framework-implied)** — *formally unrated by the agencies in retrieved data; consistent with a solid BB+/BBB− profile given sector and convertible-heavy capital structure.*

**Why leverage is not what it appears.** The FY2025 balance sheet shows total debt of $2,142.6M against book equity of just **$48.8M** — producing a debt/equity of **43.89x**. This is a capital-allocation artifact, not insolvency: Halozyme repurchased **$342.4M (2025), $250.0M (2024), and $402.4M (2023)** — ~$995M of stock — which has nearly erased the book equity base while the business compounded revenue from $660M (2022) to $1,397M (2025). On **market** equity of $11.76B, debt/equity is a benign **0.18x**.

**The reported EBITDA is contaminated — this is the single most important adjustment in this report.** FY2025 operating income was **$802.6M**, yet the data provider reports "EBIT" of **$485.0M** and EBITDA of **$573.1M**. EBITDA cannot logically sit below operating income. The culprit is visible in the quarterly data:

| Quarter | Revenue | Operating Income | **Net Income** |
|---|---|---|---|
| Q3 2025 | $354.3M | $217.9M | $175.2M |
| **Q4 2025** | **$451.8M** | **$240.7M** | **−$141.6M** |
| Q1 2026 | $376.7M | $184.5M | $150.0M |
| Q2 2026 | $481.0M | $287.7M | $229.9M |
| Q3 2026 | $493.0M | $295.0M | $247.0M |

Q4 2025 posted **strongly positive operating income but a $141.6M net loss** — a ~$382M pre-tax below-the-line hit, in the same quarter Halozyme executed a convertible-note refinancing (0% notes plus 2031/2032/2033 indentures). The pattern is characteristic of a **loss on extinguishment / induced conversion**, a non-cash accounting charge. Critically, **Q1–Q3 2026 net income recovered immediately** ($150.0M → $229.9M → $247.0M), confirming non-recurrence.

**Clean leverage math:**

| Basis | EBITDA | Net Debt / EBITDA |
|---|---|---|
| Vendor-reported (contaminated) | $573.1M | **3.49x** |
| FY2025 clean (op. income + D&A) | $890.7M | **2.25x** |
| Trailing-twelve-months (Q4'25–Q3'26) | ~$1,136M | **~1.76x** |

**Interest coverage is exceptional.** Vendor computes 44.28x using operating income / interest. On the more conservative reported-EBIT basis, coverage is still **26.8x** ($485.0M / $18.1M). TTM coverage: ~46x. Note that **2026 interest expense is falling** ($6.0M in Q3 2026) despite higher gross debt, because the new converts carry a **0% coupon**. This is structurally cheap, non-covenant-heavy debt.

**Maturity profile — essentially no refinancing cliff.** Short-term debt is **$0**. The entire $2.14B sits in long-term convertible notes with indentures dated Nov 2025 maturing **2031, 2032, and 2033**, plus a later $1.3B 2033 offering. Convertible notes of this type carry **no meaningful financial maintenance covenants** — covenant-breach risk is low. **The first material maturity is ~5+ years out.**

**Piotroski F-Score: 5/9 (Moderate).** The failures are capital-structure items, not operating ones:
- ✗ F5 lower leverage — total debt rose $1,505.8M → $2,142.6M (debt-funded buyback)
- ✗ F6 positive equity change — equity fell $363.8M → $48.8M (buybacks)
- ✗ F3 ROA improvement and ✗ F8 gross margin improvement — 83.6% vs 84.3%, a marginal 70bp slip on higher cost of revenue (+43.5% vs revenue +37.5%) and a build in inventory ($141.9M → $176.5M)
- ✓ F1, F2, F4, F7, F9 — profitable, strong cash conversion, no dilution from operations, improving asset turnover

---

## 2. Key Financial Risk Metrics

| Metric | Value | Assessment |
|---|---|---|
| **LEVERAGE** | | |
| Total debt | $2,142.6M | 100% long-term, 0% short-term |
| Net debt | $2,000.8M | |
| Debt / equity (book) | **43.89x** | ⚠️ Artifact of $48.8M book equity |
| Debt / equity (market) | **0.18x** | ✓ Genuinely low |
| Debt / assets | 0.85 | ⚠️ Same book-equity artifact |
| Net debt / EBITDA (reported) | 3.49x | ⚠️ Contaminated by Q4'25 charge |
| **Net debt / EBITDA (clean, FY25)** | **2.25x** | ✓ Comfortable |
| **Net debt / EBITDA (TTM)** | **~1.76x** | ✓ De-levering |
| **COVERAGE** | | |
| Interest coverage (op. income) | **44.28x** | ✓ Exceptional |
| Interest coverage (reported EBIT) | 26.8x | ✓ Still very strong |
| Operating margin | **57.47%** | ✓ Best-in-class |
| **LIQUIDITY** | | |
| Current ratio | **4.66x** | ✓ Strong |
| Quick ratio | 3.66x | ✓ Strong |
| Cash ratio | 0.81x | ✓ Adequate |
| Working capital | $648.1M | ✓ |
| Cash & ST investments | $142.8M | ⚠️ Down from $596.1M (−76%) |
| Cash / total liabilities | 0.06 | ⚠️ Thin vs. long-dated debt |
| Cash runway | **Not applicable — FCF positive** | ✓ ~$644M FCF/yr |
| **SOLVENCY SCORES** | | |
| Altman Z-Score (book) | 1.537 — **Distress** | ⚠️ x4 = 0.0197 on $48.8M book equity |
| **Altman Z-Score (market-cap adjusted)** | **~4.37 — Safe** | ✓ >2.99 threshold |
| Piotroski F-Score | 5/9 — Moderate | Neutral |
| **CASH GENERATION** | | |
| Operating cash flow | $651.6M | 2.06x net income (charge-inflated) |
| FCF | **$644.6M** | |
| FCF margin | **46.2%** | ✓ 46.1% '24, 45.0% '23, 35.6% '22 |
| FCF yield | **5.0–5.5%** | ✓ vs. 10Y Treasury |
| Capex / revenue | 0.5% | ✓ Asset-light royalty model |

**Altman Z reconstruction (transparency):** reported Z = 1.2(0.2566) + 1.4(0.0217) + 3.3(0.1921) + 0.6(0.0197) + 1.0(0.553) = 1.537. Substituting market cap for book equity: x4 = $11.76B / $2.48B = 4.75 → Z = **4.374**. The tool itself flags this limitation. **I weight the market-cap version far more heavily**, but note that a Z-score is a poor fit for an asset-light royalty business in any case (it penalizes low asset turnover by construction).

**FCF sustainability: HIGH.** FCF rose $235M → $373M → $468M → $645M over 2022–2025 (28% CAGR) with capex under 1% of revenue. Cash conversion quality is high, though the 2025 CFO/NI ratio of 2.06x is flattered by the non-cash charge — adjusted, it is ~0.9x, which is normal and healthy.

---

## 3. Market Risk Profile

| Metric | Value | Read |
|---|---|---|
| Annualised volatility (3Y, 756d) | **44.27%** | ⚠️ High — ~3x market |
| Beta vs SPY (3Y calc) | **0.595** | Low sensitivity to market drawdowns |
| Beta (profile field) | 0.897 | Windows differ — see note |
| Max drawdown (3Y) | **−32.33%** | Moderate-to-high |
| Sharpe ratio (rf = 0%) | **0.763** | Decent on a zero-risk-free basis |

**Interpretation — this is the key nuance.** HALO's 44% volatility is **idiosyncratic, not systematic**. Beta of 0.60 means a 20% market decline implies only ~12% for HALO. The stock's risk is **binary/event-driven**: patent litigation outcomes, partner program milestones, royalty-rate resets, and pipeline readouts. That is a fundamentally different risk from cyclical or levered equity risk.

**Caveat on Sharpe:** the 0.763 figure assumes a **0% risk-free rate**. Against a realistic ~4% T-bill, the excess-return Sharpe falls to roughly **0.2–0.3** — meaningfully weaker risk-adjusted returns. Sortino was not computed by the tool (**data gap**), so I cannot confirm how much of the 44% vol is downside vs. upside.

**Beta divergence flag:** 0.595 (computed) vs. 0.897 (profile). Different lookback windows. I use the computed 3Y figure as primary but treat beta as having a **plausible range of 0.6–0.9** — i.e., HALO has historically been a partial defensive, but I would not rely on that persisting.

---

## 4. Downside Scenario Analysis

**Assumption set:** 20% revenue decline to $1,117M. Variable costs estimated at 40% of cost of revenue and 25% of SG&A (royalty-platform cost structure is largely fixed — bulk rHuPH20 supply, partnered manufacturing, fixed R&D). Contribution margin ~89.7%.

| | Base (FY25) | **−20% Revenue** | −35% (Severe) |
|---|---|---|---|
| Revenue | $1,396.6M | **$1,117.3M** | $907.8M |
| Gross profit | $1,167.8M | $917.3M | $723.5M |
| Operating income | $802.6M | **$552.1M** | $366.2M |
| Operating margin | 57.5% | **49.4%** | 40.3% |
| EBITDA (clean) | $890.7M | **$640.2M** | $454.3M |
| **Net debt / EBITDA** | 2.25x | **3.13x** | **4.40x** |
| **Interest coverage** | 44.3x | **~25x** | **~16.6x** |
| FCF (approx.) | $644.6M | **~$480M** | ~$290M |
| FCF yield (on $11.8B) | 5.5% | **~4.1%** | ~2.5% |
| Free cash flow positive? | Yes | **Yes** | **Yes** |

**Conclusion: HALO survives a 20% revenue shock without breaching any covenant, cutting capex, or drawing a revolver — and would still generate ~$480M of free cash flow.** Even a severe 35% decline leaves leverage at 4.4x and coverage at ~17x — stressed but clearly serviceable, with FCF still positive. The high fixed-cost structure means operating leverage cuts both ways (margins compress ~8pts on a 20% revenue hit), but the starting margin of 57% provides an enormous buffer. **This is a very resilient P&L.**

**The scenario that actually breaks this company is not a gradual revenue decline — it is a patent/legal event.** A successful challenge invalidating ENHANZE coverage, or a partner successfully renegotiating/discontinuing royalty obligations, could impair a concentrated revenue stream in a step-function rather than a taper. That risk lives outside the arithmetic above.

---

## 5. Overall Financial Risk Rating

# MODERATE

**Component ratings:**

| Risk Dimension | Rating | Rationale |
|---|---|---|
| **Credit / Default Risk** | **LOW** ✓ | 26–44x coverage, ~1.8–2.3x net leverage, no maturities before 2031, zero short-term debt, no maintenance covenants |
| **Liquidity Risk** | **LOW** ✓ | 4.66x current ratio, $648M working capital, $645M annual FCF generation, self-funding |
| **FCF Sustainability** | **LOW** ✓ | 46% FCF margin, 28% FCF CAGR, 0.5% capex intensity |
| **Market / Price Risk** | **HIGH** ⚠️ | 44% vol, −32% max drawdown, event-driven/binary exposure |
| **Structural / Concentration** | **MODERATE–HIGH** ⚠️ | Near-zero book equity, thin $143M cash, single-platform royalty dependence, patent horizon |

**The thesis in one line:** the *balance sheet* is safe, the *cash flow* is excellent, and the *equity* is volatile and event-exposed. Do not confuse the Altman "Distress" label for credit risk — it is a book-equity artifact. Equally, do not confuse 44x interest coverage for a low-risk *stock*.

---

## 6. Key Red Flags

1. **⚠️ Book equity has nearly been erased — $48.8M against $2,142.6M of debt.** Cumulative buybacks of ~$995M across 2023–2025 have pushed equity/assets to 0.02. Any book-based covenant, rating-agency metric, or lender test that uses tangible net worth would now be **severely strained**. Continued buybacks risk **negative book equity**, which can trigger index-exclusion and lender technical-default issues even when cash flow is fine. *(No such covenant is evident in convertible indentures, but this is the single largest structural fragility.)*

2. **⚠️ Cash buffer thinned by 76%** — from $596.1M to $142.8M in one year, deployed into $342.4M of buybacks. The company is now operationally dependent on continuous FCF generation rather than a cash cushion. Fine today; less fine if a royalty stream is disrupted while a $1.3B convertible has just been layered on.

3. **⚠️ Gross margin slipped** (84.3% → 83.6%) with cost of revenue +43.5% vs. revenue +37.5%, and inventory up 24% ($141.9M → $176.5M). Q3 2026 cost of sales jumped to $82.5M from $55.2M on bulk rHuPH20 purchases. Early signal of royalty-stack cost inflation or inventory build — **monitor, not yet alarm.**

4. **⚠️ Single-platform concentration.** Revenue is overwhelmingly ENHANZE royalty/milestone-based, dependent on a handful of large partners (Roche, J&J, AbbVie, argenx, BMS, Lilly, Pfizer). Revenue *growth* has been excellent (+37.5% in 2025), but the *durability* rests on patent life and partner behavior — not diversification.

5. **⚠️ Q4 2025 loss of −$141.6M against +$240.7M of operating income.** Even as a one-time non-cash charge, this is a genuine governance/transparency flag: a ~$382M below-the-line item in a single quarter materially distorts FY2025 GAAP EPS ($2.56 vs. $3.43 in 2024) and every screen that keys off reported net income.

6. **⚠️ 44% annualized volatility with −32% max drawdown** — position sizing must reflect equity risk that the credit metrics do not capture.

---

## 7. Data Gaps & Methodology Notes

Flagged explicitly, per mandate:

- **Q4 2025 one-time charge composition: NOT VERIFIED.** The FY2025 earnings release PDF returned unparseable binary content. The existence and ~$320–400M magnitude are confirmed by arithmetic across
