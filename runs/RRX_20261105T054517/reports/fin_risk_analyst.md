# Fin Risk Analyst

- Symbol: RRX
- Elapsed: 37.0s

---
I now have a complete dataset, including credit ratings, the debt maturity ladder, and the latest Q3 2026 metrics. Writing the assessment.

---

# RRX — Regal Rexnord Corporation
## Financial Risk Assessment

**Sector:** Industrials / Industrial – Machinery | **Market cap:** $11.54B | **Price:** $173.38 | **Rating:** Fitch **BBB-** (Stable, affirmed Feb 2026)
**Analytical base:** FY2025 (audited, 12/31/25), reconciled to latest reported Q3 2026.

> **Note on data vintage:** Tool-computed ratios are anchored to FY2025 (period_end 2025-12-31). Q3 2026 company disclosure (net leverage 2.92x) is included where available and flagged, as it materially post-dates the audited base.

---

## 1. Credit Risk Assessment

**Rating: Investment Grade — but the lowest rung (BBB-), with a thin cushion.**

RRX is investment grade, affirmed BBB- stable by Fitch in Feb 2026. It carries $5.06B of gross debt and $4.53B net debt (FY2025). The credit profile improved meaningfully through 2025: total debt fell 9.8% ($5.61B → $5.06B), net debt fell to $4.53B, and the 2026 maturities were refinanced in Feb 2026. Company-reported net leverage reached **2.92x adjusted EBITDA (incl. synergies)** as of Q3 2026, down from 3.77x on FY2025 GAAP EBITDA — a genuine deleveraging trend.

However, credit strength is constrained by **weak GAAP interest coverage (1.96x EBIT/interest)** and **negative tangible equity** (goodwill + intangibles of $10.03B exceed total equity of $6.85B). A BBB- rating with ~$5B debt and 1.96x GAAP coverage is a thinner cushion than the rating implies. The relevant intermediate credit (BBB-/Baa3) is justified by strong FCF (7.7% yield) and the absence of near-term maturities, not by balance-sheet ballast.

---

## 2. Key Financial Risk Metrics

| Metric | FY2025 (audited) | Read-through |
|---|---|---|
| **Debt / Equity** | 0.74x | Moderate |
| **Debt / Assets** | 0.36x | Moderate |
| **Net Debt / EBITDA** | **3.77x** (GAAP) | Elevated; **2.92x adjusted incl. synergies (Q3'26)** |
| **Interest Coverage (EBIT/Int.)** | **1.96x** | **Weak** — the key vulnerability |
| **EBITDA / Interest** | 3.44x (1,201.3/349.2) | Adequate |
| **Current Ratio** | 2.15x | Strong |
| **Quick Ratio** | 1.10x | Adequate |
| **Cash Ratio** | 0.41x | Adequate |
| **Cash & ST Inv.** | $521.7M | — |
| **Working Capital** | $1,448M | Strong |
| **Altman Z-Score (book)** | **1.52 — Distress zone** | Distorted by negative tangible equity |
| **Altman Z (market-cap x4, my est.)** | **~1.92 — Grey zone** | More representative |
| **Piotroski F-Score** | **8 / 9 — Strong** | Operational strength |
| **FCF Yield** | **7.73%** | Strong |
| **Goodwill+Intangibles / Total Assets** | **72%** | **High impairment exposure** |

**Critical adjustment — Altman:** The book-equity Z of 1.52 understates solvency because book equity is depressed by a negative tangible book. Recomputing x4 with market cap ($11.54B / $7.07B liabilities = 1.63 vs. 0.97 book) lifts Z to **~1.92 — grey zone, not distress.** Treat the 1.52 as a floor, not a verdict. Even so, ~1.9 is only the lower edge of grey.

**Tangible equity is negative:** Total assets $13.92B − goodwill/intangibles $10.03B = $3.89B tangible assets, against $7.07B liabilities → **~−$3.18B tangible book.** This is the single most important balance-sheet fact. It reflects the 2021 Rexnord PMC merger and means reported equity is largely goodwill — impairable, and non-recoverable in a liquidation.

---

## 3. Market Risk Profile

| Metric | Value | Comment |
|---|---|---|
| **Annualised volatility** | **55.9%** | Very high for an industrial — reflects recent re-rating |
| **Beta vs SPY (realized, 252d)** | **2.20** | vs. **1.09** company-reported/structural beta |
| **Max drawdown (3yr)** | **37.9%** | Severe peak-to-trough |
| **Sharpe (0% rf)** | 0.56 | Mediocre compensation for risk |

**Flag — beta divergence:** realized beta of 2.20 over the trailing year is double the 1.09 structural beta in the profile. This is characteristic of an idiosyncratic re-rating episode (data-center/electrification narrative drove outsized 2026 moves) rather than a permanent change in market sensitivity. **Use ~1.1–1.3 for structural downside-beta modeling; the 2.20 is a trailing-window artifact.** Either way, realized volatility near 56% places RRX in the top decile of industrial risk — drawdowns will be violent relative to the sector.

---

## 4. Downside Scenario Analysis — Revenue −20%

**Shock:** −$1,187M revenue (to $4,748M), gross margin held at 37.4% (variable-cost = COGS/revenue), SG&A initially fixed.

| Line item | Base FY2025 | −20% Revenue (no mitigation) | −20% w/ $180M cost cuts |
|---|---|---|---|
| Revenue | $5,934.5M | $4,747.6M | $4,747.6M |
| Gross profit | $2,217.8M | $1,774.2M | $1,774.2M |
| EBIT | $701.7M | **$258.1M** | ~$438M |
| EBITDA | $1,201.3M | **$757.7M** | ~$938M |
| Interest expense | $349.2M | $349.2M | $349.2M |
| **EBIT / Interest** | **1.96x** | **0.74x — below 1.0x** | ~1.25x |
| **EBITDA / Interest** | 3.44x | 2.17x | ~2.69x |
| **Net Debt / EBITDA** | 3.77x | **6.0x** | ~4.8x |
| **vs ~4.0x revolver covenant** | ~0.2x cushion | **Likely breach** | **Breach** |

**Findings:**
- Under a pure −20% revenue shock with no cost action, **EBIT fails to cover interest (0.74x)** and **net leverage jumps to ~6.0x — a probable covenant breach** against a typical ~4.0x maintenance test on the revolver.
- Cost mitigation ($180M, ~15% of SG&A) restores coverage to ~1.25x but leverage of ~4.8x still breaches a 4.0x covenant. **Roughly $300M+ of mitigation is needed to stay inside a 4.0x test** — difficult within one year without restructuring charges.
- **Liquidity holds:** $521.7M cash + $1.5B revolver + positive FCF (protected by $499.6M D&A) keep RRX solvent through the shock. This is a **covenant/ratings risk, not a solvency risk.**
- **FCF resilience:** the high D&A load means OCF compresses far less than EBIT; a working-capital release (receivables/inventory) would partly offset the gross-profit hit. FCF likely stays positive (~$400–500M), covering the ~$93M dividend.
- **Downside credit trajectory:** a −20% year would likely trigger a **downgrade to BB+ (sub-investment grade)** on leverage gating, raising refinancing costs on the 2028 notes.

---

## 5. FCF Sustainability

| | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Operating cash flow | $715.3M | $609.4M | **$990.8M** |
| Capex | ($119.1M) | ($109.5M) | ($97.7M) |
| **FCF** | $596.2M | $499.9M | **$893.1M** |
| **FCF margin** | 9.5% | 8.3% | **15.0%** |
| Dividends | ($92.8M) | ($93.0M) | ($93.0M) |

FY2025 FCF of $893M (15.0% margin, 7.73% yield) is strong and easily covers the dividend (10.4% of FCF). **But the 2026 guide of ~$600–650M represents a >25% decline** despite revenue growth — driven by working-capital build, $127M unmitigated tariff costs, and restructuring. This is a **deterioration signal worth watching**: FCF margin is reverting toward ~10–11%, still healthy but no longer a deleveraging accelerant. The quality of the FY2025 FCF was flattered by a $204.5M working-capital release that will not repeat.

---

## 6. Overall Financial Risk Rating: **MODERATE**

- **Credit:** Investment Grade (BBB-/Stable) — lowest rung, thin cushion.
- **Liquidity:** **LOW risk** — 2.15x current ratio, $522M cash, $1.5B revolver, no material maturities until the 2028 notes.
- **Solvency/leverage:** **MODERATE-to-HIGH** — 3.77x GAAP leverage, 1.96x interest coverage, negative tangible equity.
- **Market risk:** **HIGH** — 56% realized vol, 38% max drawdown.
- **Composite: Moderate**, upgraded from High by the credit rating, refinancing profile, strong FCF, and the Q3 2026 deleveraging to 2.92x.

**Refinancing cliff: none near-term.** 2026 notes refinanced Feb 2026; Fitch confirms "no material debt maturities until 2028" (2028 senior notes due April 2028; DDTL due 2029; 2031 notes at 4.125%). With 10Y UST at 5.13% and 2Y–10Y positive (+39bp, no inversion), refinancing the 2028 stack will be **more expensive than the 4.125% legacy coupons** — a margin drag, not a cliff.

---

## 7. Key Red Flags

1. **Negative tangible equity (~−$3.18B).** Goodwill + intangibles are 72% of total assets. A large write-down is a live risk — FY2023's −$57.4M net loss and Q3 2026's −$12.3M GAAP net loss show the P&L is periodically hit by non-cash charges/impairments.
2. **Interest coverage of 1.96x on GAAP EBIT** — the thinnest metric in the stack. Falls below 1.0x under a −20% revenue shock. Debt service depends on EBITDA, not EBIT, given the heavy D&A.
3. **Covenant vulnerability in a downturn.** ~4.0x revolver maintenance test vs. 2.92x now → only ~1.1x of headroom; a severe cyclical shock breaches it even with cost cuts.
4. **✓ Deleveraging is real but partly flattered:** 2.92x relies on "adjusted EBITDA including synergies" ($1,370.8M vs. GAAP $1,201.3M). On GAAP EBITDA, leverage is closer to 3.5x.
5. **FCF guide down >25% for 2026** despite organic growth (+6.1% Q3) — working-capital, tariffs ($127M), and restructuring are consuming cash.
6. **High market risk:** 56% realized vol and 38% drawdown mean equity holders bear near-cyclical-beta risk for an industrial.
7. **Cyclical end-market exposure** (industrial powertrain, motion control, HVAC) — the −20% revenue scenario is a realistic mid-cycle stress, not a tail.

**Data gaps flagged:** S&P/Moody's ratings and CDS spreads not directly retrieved (Fitch BBB- confirmed). Exact covenant thresholds and the full maturity-by-year schedule inferred from filing snippets, not the 10-K table. Beta from the volatility tool (2.20) conflicts with the profile beta (1.09); both reported with explanation.

---
**Bottom line:** RRX is a **solvent, investment-grade, cash-generative industrial with adequate liquidity and no near-term refinancing cliff — but a leveraged, goodwill-heavy balance sheet with negative tangible equity and dangerously thin GAAP interest coverage.** It survives a −20% revenue shock on liquidity and FCF, but would likely breach a leverage covenant and lose its investment-grade rating. **Risk rating: Moderate (credit) / High (equity market risk).**
