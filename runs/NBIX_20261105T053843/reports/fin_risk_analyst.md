# Fin Risk Analyst

- Symbol: NBIX
- Elapsed: 24.2s

---
I have sufficient data. One note: the web search returned only dictionary definitions (dead query) — I'll flag the news/ratings gap rather than burn budget retrying. Writing the assessment now.

---

# NBIX — Neurocrine Biosciences, Inc.
## Financial Risk Assessment | Data as of Q3 FY2026 (period end 2026‑09‑30), price $166.05 (2026‑11‑04)

---

## 1. Credit Risk Assessment

**Rating: Investment Grade** (implied — no public rating agency coverage returned by the tools; see data gaps)

NBIX is a **net-cash, self-funding commercial-stage biopharma**. Leverage is effectively a non-issue:

- Total debt $415.3M against $1,480.4M cash and short-term investments → **net cash of ~$1,065M** (−1.6× FY25 EBITDA; −1.1× TTM EBITDA).
- Critically, **short-term debt = $0 and long-term debt = $0** on the FY2025 balance sheet. The $415.3M "total debt" line is almost certainly operating lease liabilities (consistent with $545.2M PP&E and a $1.4B+ campus in San Diego). **There is no refinancing cliff.**
- **Interest coverage is effectively undefined/infinite** — FY2025 interest expense was $0, and quarterly interest expense since Q1 2026 is $0–2.9M. The tool returned `null` for interest coverage; this is a *positive* data artifact, not a gap in creditworthiness.
- Free cash flow has been positive every year in the dataset: $322.9M (2022) → $361.6M (2023) → $557.2M (2024) → $748.7M (2025). **Zero years of cash burn in the observable history.**

The credit profile is genuinely fortress-like for a biotech. Bankruptcy risk is negligible on current fundamentals.

---

## 2. Key Financial Risk Metrics

| Metric | Value | Assessment |
|---|---|---|
| **Leverage** | | |
| Debt / Equity | 0.13× | Very low |
| Debt / Assets | 0.09× | Very low |
| Net Debt / EBITDA | **−1.6×** (net cash) | Fortress |
| Interest coverage | N/A (interest expense $0) | No debt service burden |
| **Liquidity** | | |
| Current ratio | 3.39× | Strong |
| Quick ratio | 3.30× | Strong (inventory only $69M) |
| Cash ratio | 1.99× | Strong |
| Working capital | $1,779.3M | Strong |
| Cash runway | **Indefinite** (FCF-positive) | No burn |
| **Solvency scores** | | |
| Altman Z‑Score | **3.08** (Safe zone) | Barely above 2.99 cutoff **on book equity** |
| Altman Z (market-cap x4, my recalc) | **~9.0** | Extremely safe |
| Piotroski F‑Score | **7 / 9** (Moderate) | Misses: gross-margin trend, asset-turnover trend |
| **Cash generation** | | |
| FCF (FY2025) | $748.7M | +34% YoY |
| FCF margin | 26.2% (FY25) vs 21.7% (FY22) | **Improving** |
| FCF yield | 4.4% (FY25 FCF / mkt cap) | Adequate |
| SBC-adjusted FCF yield | **~3.2%** | SBC = 29% of FCF |
| **Growth/margin** | | |
| Revenue FY2025 | $2,860.5M (+21.4% YoY) | Strong |
| TTM revenue (Q4'25–Q3'26) | **$3,701.7M** (~+41% YoY on Q3) | Accelerating |
| Operating margin | 21.6% FY25 / 23.8% TTM | Healthy, expanding |
| Gross margin | 98.2% FY25 / 97.8% TTM | Elite |

*Derived: EV ≈ $15.7B; EV/TTM EBITDA ≈ 16.6×; EV/TTM revenue ≈ 4.25×.*

**Note the Altman caveat:** the 3.08 reading is inflated-deflated by book-equity x4. On market cap, Z ≈ 9.0. Either way, no distress signal — but on the stricter book-equity basis it's only *marginally* in the safe zone, entirely because revenue/assets (x5 = 0.62) is structurally low for a high-margin pharma. This is a scale artifact, not a credit concern.

---

## 3. Market Risk Profile

| Metric | Value (756-day window) |
|---|---|
| Annualised volatility | **35.36%** |
| Beta vs SPY | **0.777** (3Y calc) / 0.362 (vendor profile) |
| Max drawdown (3Y) | **−42.89%** |
| Sharpe ratio | 0.618 (0% RF assumption) |
| Sortino ratio | **Not available — data gap** |
| Dividend | None |
| 3Y total return | +48.9% (~14% CAGR) |

**This is the most important section of the report.** A 35% volatility with a sub-0.8 beta means roughly **95%+ of NBIX's risk is idiosyncratic, not market risk**. The stock will not protect you in a drawdown through low beta — it will generate its own.

Evidence from the price series — **four single-day gaps worse than −10% in under three years**:
- **2024‑08‑28: −18.9%** (152.55 → 123.76, 4.8M shares)
- **2025‑02‑07: −18.5%** (150.51 → 122.62, 6.5M shares)
- **2026‑02‑12: −10.4%** (137.44 → 123.10)
- **2026‑07‑31: −10.1%** (185.50 → 166.80)
- Offset by **2026‑11‑03: +13.4%** (145.35 → 164.85) post-Q3 earnings

The −42.9% max drawdown was a **7½-month grind** from the Aug‑2024 peak ($152.55) to the Apr‑2025 trough ($87.54) — a slow-motion de-rating, not a single shock. That is the more dangerous shape for a risk manager: it allowed ample time for holders to be wrong for two full quarters.

**Portfolio implication:** position sizing should use 35% vol (residual-risk based), not the 0.36–0.78 beta. A beta-based sizing model will materially understate this name's contribution to portfolio VaR.

---

## 4. Downside Scenario Analysis — Revenue −20%

Base: TTM revenue $3,701.7M. Stress: **−$740M to $2,961.4M** (≈ an INGREZZA erosion / competitive VMAT2 entry / pricing-reform scenario). Cost base derived from statements: TTM COGS $81.2M (2.2% of revenue), TTM SG&A $1,426.3M, implied R&D ~$1,313M (backed out — R&D is not a discrete line in the feed), total TTM opex ~$2,739M.

| Line | Base (TTM) | Stress A: no cost flex | Stress B: 15% opex cut |
|---|---|---|---|
| Revenue | $3,701.7M | $2,961.4M | $2,961.4M |
| Gross profit (97.8%) | $3,620.5M | $2,896.4M | $2,896.4M |
| Operating expense | $2,739.3M | $2,739.3M | $2,328.4M |
| **Operating income** | **$881.2M** | **$157.1M** | **$568.0M** |
| Operating margin | 23.8% | **5.3%** | **19.2%** |
| Interest expense | ~$0 | ~$0 | ~$0 |
| **FCF (est.)** | ~$1.0B | **~$260M** | **~$580M** |
| FCF yield on $16.8B mkt cap | ~6% | **~1.6%** | **~3.4%** |
| SBC-adjusted FCF yield | ~4.5% | **~0.3%** | **~2.1%** |

**Interpretation — the crucial conclusion: a 20% revenue decline does not threaten solvency, it threatens the multiple.**

- **Credit: survives comfortably.** Even with zero cost flex, NBIX stays operating-profitable and FCF-positive, holds $1.48B of cash, carries no funded debt maturities, and has no covenant to breach. Altman Z under Stress A would remain in the grey/safe range because leverage stays near zero.
- **Equity: de-rates severely.** FCF yield compresses to 1.6% (0.3% after SBC). At a stressed 15–18× FCF multiple the equity is worth roughly $4–5B, i.e. **−70% to −75%** from today's $16.8B — broadly consistent with the 35% vol / 43% realized drawdown profile. **The asymmetry is entirely in the valuation, not the balance sheet.**
- **The 5.3% operating margin in Stress A is the real number to watch.** Because gross margin is 98%, revenue is almost pure margin — but opex is ~74% of revenue and ~50% of it (R&D) is discretionary only over 12–24 months. Cost flex is a *slow* lever; the stock would re-rate faster than management can cut.

**Cash runway in stress: >4 years of downside FCF deficit coverage** even if revenue fell 20% *and* FCF went to zero, on $1.06B net cash. Liquidity risk is effectively nil.

---

## 5. Overall Financial Risk Rating

# LOW

| Dimension | Rating | Driver |
|---|---|---|
| Credit risk | **Low / Investment Grade** | Net cash $1.07B, no funded debt, no maturities, FCF+ every year |
| Liquidity risk | **Low** | Current 3.39×, cash 1.99×, indefinite runway |
| Solvency risk | **Low** | Piotroski 7/9, Altman 3.08 book / ~9.0 market |
| FCF sustainability | **Low–Moderate** | 26% FCF margin and rising, but SBC consumes 29% of it |
| **Market/equity risk** | **Moderate–High** | 35% vol, 43% max DD, four >10% gaps, ~95% idiosyncratic |

**Bottom line:** This is a **balance-sheet-fortress, single-asset-concentration** situation. The company will not fail. The stock can absolutely halve. Any downside case here is a *valuation and concentration* case, not a *solvency* case — which is exactly the profile that lulls beta-based risk models into under-sizing it.

---

## 6. Key Red Flags & Data Gaps

**Red flags:**

1. **Severe single-product concentration.** INGREZZA is the dominant revenue driver; ONGENTYS, ORILISSA and ORIAHNN are comparatively small. A −40% growth company whose valuation rests on one molecule's franchise durability carries patent-cliff/generic-entry risk that no ratio in this report captures. The Feb‑2025 and Aug‑2024 −19% days are consistent with commercial/pipeline shocks to that concentration.
2. **SBC is a material, under-appreciated cash-quality drag.** FY2025 SBC of $217.9M equals **29% of FCF**. SBC-adjusted FCF yield is 3.2%, not 4.4×. Over FY2024–25 the company spent **$467.7M on buybacks against $413.4M of SBC — net capital returned to shareholders was only ~$54M.** The buyback is functionally dilution offset, not shareholder return. F‑Score credits "no dilution" (F7=1) on a share-count test; diluted shares still rose from 103.4M (Q1'26) to 105.2M (Q3'26), ~1.7% annualised.
3. **Opex volatility / margin quality.** Q2 2026 SG&A spiked to $439.7M (45.8% of revenue) versus $366.3M (32.6%) in Q3 2026 — a 1,320bp swing in one quarter, with operating margin moving 18.7%→29.5%. Margin expansion is not yet smooth or predictable.
4. **Piotroski's two misses are the right two misses.** F8=0 (gross margin *declined*, 98.56%→98.18%) and F9=0 (asset turnover not improving) mean the F-Score of 7 is driven by profitability and leverage, **not by operating efficiency gains**. Earnings quality is good; incremental returns on capital are not clearly improving.
5. **35% realized volatility vs. 0.36–0.78 beta.** Sizing on beta understates tail risk by an order of magnitude.
6. **Significant event risk around prints.** Q3'26 beat drove +13.4% in one session; the same mechanism works in reverse (see Feb'25, Aug'24). Expect ±10–20% gap risk on any given earnings date.

**Data gaps (explicitly flagged):**
- **No credit rating or CDS spread available** — the "Investment Grade" label is my inference from balance-sheet fundamentals, not a rating action.
- **Sortino ratio not computed** by the tool; downside-deviation risk is unquantified.
- **R&D is not a discrete income-statement line** in the feed; the ~$1,313M TTM R&D figure is my back-out (Revenue − COGS − SG&A − Operating Income) and should be verified against the 10-Q.
- **D&A data is internally inconsistent:** FY2025 annual D&A is $30.1M but Q3 2026 quarterly D&A is $44.0M, against $545.2M of PP&E. My stress-case FCF uses a $80M placeholder — **directionally sound but low-confidence.**
- **Net debt discrepancy:** the leverage tool computes −$1,065.1M (cash $1,480.4M − debt $415.3M), but the balance-sheet record's own `net_debt` field reads −$297.7M. I used the former, which reconciles to the reported line items. Flagged for verification.
- **FY2024 interest expense of $126.6M looks anomalous** (vs $4.6M in FY2023 and $0 in FY2025) given no funded debt — likely a debt-extinguishment or financing charge misclassified. It inflates the FY2024 base and is why the tool returns `null` coverage for FY2025.
- **No news/competitive-landscape verification.** The web search returned irrelevant results; INGREZZA patent expiry timing, generic/VMAT2 competitive entry, and any FDA/litigation overhang are **not verified in this report** and are the largest unquantified risk to the downside scenario.
- **TTM FCF (~$1.0B) and FY2026E revenue (~$4.0B) are estimates** extrapolated from FY2025 actuals plus 9M'26 quarterly revenue; no Q4'26 guidance figure was available.
