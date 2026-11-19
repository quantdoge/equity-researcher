# Fin Risk Analyst

- Symbol: GNRC
- Elapsed: 40.4s

---
## GNRC — Financial Risk Assessment

**Generac Holdings Inc.** | Industrials / Industrial–Machinery | Power generation, energy storage, outdoor power equipment
Price $205.45 | Market cap ~$12.1B | 9,400 FTE | Data through **Q3 FY2026 (9/30/2026)**

**Critical framing note:** FY2025 (Dec-2025) was a **trough year** — revenue −2%, EBITDA −31%, and a Q4 FY2025 operating loss. The pre-computed ratio tools all key off FY2025 year-end, which materially **overstates** current leverage and understates coverage. I have therefore built a TTM view (Q4'25 + Q1–Q3'26) alongside the reported FY2025 figures. Both are shown.

---

## 1. Credit Risk Assessment

**Rating: SUB-INVESTMENT GRADE (crossover / low-BB) — but improving rapidly**

| Evidence | Source |
|---|---|
| Moody's **Ba1** on senior secured debt | Moody's Ratings |
| S&P **BB+** on senior secured TLB (downgraded from BBB-) | S&P Global |
| "No significant debt maturities over the next 12 months" | Moody's |
| Net debt/EBITDA 1.36x TTM vs 2.13x FY2025 | Computed |

The ratings sit one notch into high-yield despite balance-sheet metrics that compute to **~1.4x net leverage and >7x interest coverage**. The gap is explained by **business cyclicality** (demand tied to outage events/hurricanes and residential discretionary spend), a history of negative FCF in stress years (FY2022: −$28M), and M&A-driven goodwill. This is a *ratings-agency conservatism* discount, not a liquidity problem.

**Debt structure:** Total debt $1,334M (Q3'26), of which only **$89.9M short-term (6.7%)**. Long-term $1,244M. Cash $394M. No refinancing cliff. *Data gap:* exact note-by-note maturity ladder and revolver size/availability were not retrievable from the annual statements; the "no significant 12-month maturities" characterization rests on the Moody's release rather than a primary schedule.

---

## 2. Key Financial Risk Metrics

| Metric | FY2025 (reported) | TTM Q3'26 | Read |
|---|---|---|---|
| Revenue | $4,209M | $4,619M | +9.7% |
| EBITDA | $465M | $690M | +48% |
| Debt / Equity | 0.51x | **0.44x** | Low |
| Debt / Assets | 0.24x | 0.22x | Low |
| **Net debt / EBITDA** | 2.13x | **1.36x** | Comfortable |
| **Interest coverage (EBIT/int.)** | 4.09x | **7.14x** | Adequate → good |
| Current ratio | 2.03x | 1.97x | Solid |
| Quick ratio | 1.00x | **1.06x** | Thin — inventory-heavy |
| Cash ratio | 0.28x | 0.28x | Adequate |
| Working capital | $1,247M | $1,379M | +$132M |
| **Altman Z-Score** | **2.477 (Grey)** | ~2.61 (Grey) | Borderline |
| **Piotroski F-Score** | **5 / 9 (Moderate)** | n/a | Mediocre |
| FCF (year) | $268M | $414M | +55% |
| FCF yield | 2.2% | **3.4%** | Modest |

**Z-Score caveat (important):** The tool's x4 uses *book* equity ($3.01B / $3.13B liabilities = 0.96x). Substituting **market** cap ($12.1B / $3.13B = 3.88x) lifts the Z-Score to **~4.4 — deep in the safe zone**. The grey-zone reading is largely a book-vs-market artifact; true bankruptcy probability is low.

**F-Score decomposition (FY2025):** positive ROA ✓, positive operating CF ✓, accruals quality ✓, positive equity change ✓, no dilution ✓ — but **ROA deterioration ✗, leverage increase ✗, gross margin deterioration ✗, asset turnover deterioration ✗**. The four failures are all trough-year cyclical effects; on 2026 data (GP margin 35.1%→39.9%, ROA up, turnover up) the score would plausibly print 7–8. The 5/9 is a backward-looking artifact.

**Liquidity/runway:** Cash $394M + $1.38B working capital + undrawn revolver. TTM FCF $414M covers TTM interest $65M by **6.3x**. Even at zero FCF, cash alone funds ~6 quarters of interest. **No liquidity risk in any realistic near-term scenario.**

---

## 3. Market Risk Profile

| Metric | Value |
|---|---|
| Annualised volatility (3y) | **52.2%** |
| Beta vs SPY (3y daily) | 1.49 |
| Beta (5y, vendor) | **1.86** |
| Max drawdown (3y) | **−47.8%** |
| Sharpe ratio (approx, rf=0) | 0.53 |
| Sortino | Not available (data gap) |

**This is the dominant risk in the name — not the balance sheet.** 52% vol and a ~48% three-year peak-to-trough loss mean equity holders, not creditors, absorb the stress. Beta of 1.5–1.9 implies a 30% market drawdown maps to a **~45–56% drawdown** in GNRC. The Sharpe of 0.53 is mediocre: you are being paid modestly for a lot of variance. Fundamentals are stabilizing while the *stock* remains a high-beta cyclical.

---

## 4. Downside Scenario Analysis

**Base:** TTM revenue $4,619M, GM 39.9%, SG&A $997M, interest $65M. Assume 60% of COGS variable, 25% of SG&A variable.

| | Base | **Revenue −20%** | Revenue −35% (severe) |
|---|---|---|---|
| Revenue | $4,619M | $3,695M | $3,002M |
| Gross profit (margin) | $1,844M (39.9%) | $1,253M (33.9%) | $810M (27.0%) |
| SG&A | $997M | $947M | $910M |
| **EBIT** | $467M | **$306M** | **−$100M** |
| EBITDA | $690M | $529M | $123M |
| **Interest coverage** | 7.1x | **4.7x** | **Negative** |
| **Net debt / EBITDA** | 1.36x | **1.78x** | **7.6x** |
| Net income | $301M | ~$185M | ~−$127M |
| FCF | $414M | **~$238M (positive)** | **~breakeven** |
| Liquidity needed | none | none | draws revolver |

**A 20% revenue decline is comfortably survivable** — leverage stays under 1.8x, coverage above 4.5x, FCF remains solidly positive, and no liquidity facility is touched. This is a genuinely resilient balance sheet to a normal cyclical contraction.

**The −35% tail is where it breaks.** Below roughly **−30% revenue**, EBIT goes negative, net leverage blows past 7x, and the company would breach the 3.5x-type maintenance covenant that typically attaches to Ba1/BB+ facilities — requiring covenant relief or an equity raise. Note that GNRC's revenue *did* fall 12% from FY2022 to FY2023 and EBITDA fell 23%, so a mid-teens decline is empirically well within the historical distribution; a 30%+ decline requires a simultaneous outage-light year *and* a consumer-spending recession. **Probability of the −20% case in any given year: meaningful (~20–25%). Probability of −35%: low single digits.**

---

## 5. Overall Financial Risk Rating: **MODERATE**

**Solvency risk (low) — Equity risk (high).** The company will comfortably survive a prolonged downturn: 1.4x net leverage, 7x coverage, $1.4B working capital, no 2027 maturities, and self-funding FCF. It earns a Moderate rather than Low rating because of (a) sub-investment-grade ratings, (b) demonstrable FCF volatility including a negative-FCF year, (c) a thin 1.06x quick ratio backed by $1.29B of inventory, and (d) cyclical revenue that is flat-to-down over four years ($4.57B in FY2022 → $4.62B TTM).

---

## 6. Key Red Flags

1. **FY2025 EBITDA collapse (−31%) and a Q4'25 operating loss (−$10.8M)** driven by an SG&A spike to $319M — the single most important data point. Verify whether this was restructuring, impairment, or a permanent cost-structure ratchet. *Data gap: no line-item breakdown available.*
2. **FCF halved in FY2025** ($605M → $268M), and was **negative in FY2022**. Working capital is a $465M swing factor; cash generation is not reliable through cycles.
3. **Goodwill + intangibles $2.32B = 38% of assets and 77% of book equity.** Tangible equity is only ~$690M — a $2.3B impairment would wipe out most book equity (though not cash flow). This is the main reason S&P is at BB+ despite 1.4x leverage.
4. **Ratings are crossover junk (Ba1/BB+)** with an S&P downgrade on record — financing costs and covenant terms reflect that.
5. **Inventory $1.29B (+25% YoY) growing faster than revenue (+16%)** — potential obsolescence/overstock risk if demand normalizes.
6. **Equity risk is severe:** 52% vol, 1.5–1.9 beta, −47.8% max drawdown, 0.53 Sharpe. Any downside scenario transmits fully to shareholders.
7. **Revenue stagnation FY2022–FY2025** — the top line is event-driven (storm/outage demand), not secularly compounding.

**Data gaps flagged:** definitive debt maturity ladder and revolver capacity; Sortino ratio; CDS spread; peer leverage comparison.

**Bottom line:** GNRC is a **credit-quality-stable, equity-quality-volatile** name. The balance sheet survives a 20% revenue shock with room to spare (1.8x net leverage, 4.7x coverage, positive FCF). Risk is concentrated in the *equity* — high beta, high vol, deep drawdowns, and a ratings ceiling of Ba1/BB+ that caps cheap refinancing. Watch inventory turns and whether the 2026 margin recovery is structural or just easier comps against a trough.
