# Fin Risk Analyst

- Symbol: EFX
- Elapsed: 77.8s

---
# EQUIFAX INC. (EFX) — FINANCIAL RISK ASSESSMENT

**Price $176.54 | Market cap ~$20.7B | Net debt $5.01B | EV ~$25.8B | Data as of Q3-2026 (filed 20-Oct-2026) plus 4 years of annuals**

*Note on data vintage: the annual financials are FY2025; where a metric is stale I present a TTM through Q3-2026 built from the four most recent quarters (Q4-25 through Q3-26). All ratios below are TTM unless labelled.*

---

## 1. Credit Risk Assessment

**Rating: INVESTMENT GRADE (low-BBB band)** — but with a deteriorating trajectory that warrants watching.

Equifax is a high-quality, oligopolistic, subscription-like data business with 55% gross margins and an unbroken record of positive operating cash flow. Leverage is moderate (2.5x net debt/EBITDA) and interest is covered 5.4x. S&P rates its proposed senior unsecured notes **'BBB'** (2026 rating action; EFX was historically **BBB+/Baa1** pre-2018 breach). ⚠️ *Data gap: I could not independently confirm Moody's current rating/outlook — the search returned unrelated issuers. The 2019 10-K referenced Baa1 stable; assume one notch of drift downward is possible.*

Critically, the company **executed a refinancing in Q3/Q4-2026 that removes the near-term maturity cliff** (see §2) and **upsized its revolver to $2.0B** in April 2026. This is not a liquidity story. It is a leverage-and-capital-allocation story.

---

## 2. Key Financial Risk Metrics

| Metric | FY2022 | FY2023 | FY2024 | FY2025 | **TTM Q3-26** | Assessment |
|---|---|---|---|---|---|---|
| Revenue ($M) | 5,122 | 5,265 | 5,681 | 6,075 | **6,592** | +8.5% TTM growth |
| EBITDA ($M) | 1,681 | 1,579 | 1,720 | 1,869 | **2,004** | Expanding |
| EBIT ($M) | 1,113 | 959 | 1,040 | 1,142 | **1,246** | |
| Interest expense ($M) | 183 | 241 | 229 | 212 | **232** | Rising again (+15% QoQ→YoY) |
| **Interest coverage (EBIT/int.)** | 6.1x | 4.0x | 4.5x | **5.16x** | **5.37x** | Adequate, not strong |
| EBITDA / interest | 9.2x | 6.5x | 7.5x | 8.8x | **8.6x** | OK |
| Total debt ($M) | — | 5,711 | 5,011 | 5,093 | **5,207** | |
| Net debt ($M) | — | 5,494 | 4,841 | 4,913 | **5,014** | |
| **Net debt / EBITDA** | — | 3.48x | 2.81x | **2.63x** | **2.50x** | ✅ Investment-grade |
| **Debt / equity** | — | 1.22x | 1.02x | **1.07x** | **1.16x** | ⚠️ Re-levering |
| Debt / assets | — | 46.5% | 42.6% | 42.9% | **43.6%** | |
| **Current ratio** | — | 0.67x | 0.75x | **0.60x** | **1.09x** | Big improvement |
| Quick ratio | — | 0.67x | 0.75x | 0.60x | **1.09x** | (no inventory) |
| Cash ratio | — | — | — | 0.08x | **0.13x** | Thin |
| Working capital ($M) | — | −654 | −441 | **−923** | **+127** | Flipped positive |
| Cash ($M) | — | 217 | 170 | 181 | **193** | 1.6% of assets |
| **Altman Z (book equity)** | — | — | — | **1.90 (Grey)** | ~1.90 | Grey zone |
| **Altman Z (mkt-cap x4)** | — | — | — | — | **~3.17 (Safe)** | ✅ Use this one |
| **Piotroski F-Score** | — | — | — | **7 / 9** | 7 / 9 | Moderate-strong |

**F-Score decomposition (7/9):** points scored on positive ROA, positive operating cash flow, ROA improvement, accruals quality, no dilution, gross-margin improvement, asset-turnover improvement. **Points lost: F5 (leverage rose) and F6 (equity declined YoY)** — both direct consequences of the buyback programme, not operational weakness.

**Altman nuance:** the tool's 1.90 "Grey" reading uses *book* equity (X4 = 0.66). Substituting market equity ($20.7B / $7.44B liabilities = 2.79) lifts the score to **~3.17, i.e. the safe zone**. I weight the market-based variant more heavily; the book-based score is misleading for an asset-light, high-goodwill company.

### Debt maturity & refinancing (the most improved item)
- FY2025 short-term debt: **$1,038M** → Q2-2026: **$1,410M** (cliff forming) → **Q3-2026: $158M**
- Long-term debt rose $4,056M → $5,049M; total debt roughly flat at $5.21B
- A **$1.0B senior note issuance (13-Oct-2026)** completed the term-out
- **Result: only ~3% of debt matures inside 12 months.** The 2026/27 refinancing cliff has effectively been neutralised — a genuine credit positive.
- **Committed liquidity:** revolver **upsized from $1.5B to $2.0B on 23-Apr-2026** ($150M→$200M sub-limit), which also backstops the commercial paper programme. Against $193M of cash, **undrawn revolver is the real liquidity backbone.**

---

## 3. Market Risk Profile

| Metric | Value | Comment |
|---|---|---|
| Annualised volatility (3Y) | **37.6%** | Very high for a data-services compounder |
| Beta vs SPY (calculated, 756d) | **0.90** | Defensive on this measure |
| Beta (vendor, 5Y monthly) | **1.34** | ⚠️ Conflicts with above — see note |
| **Max drawdown (3Y)** | **−54.4%** | Peak $301.67 (Aug-2024) → $137.24 (30-Sep-2026) |
| Sharpe ratio (3Y, rf=0%) | **−0.455** | Negative risk-adjusted return |
| YTD 2026 return | **−17.9%** | $215.03 → $176.54 |
| Price since Dec-2022 | **−10.0%** | Three years of no capital appreciation |
| Sortino ratio | **n/a** | ⚠️ Data gap — not returned by tool |

**Interpretation.** The beta disagreement (0.90 vs 1.34) matters, and I flag it rather than smooth it: the daily-return estimate over 3 years is dragged down by large *idiosyncratic* gap-downs — 3-Feb-2026 (−12.1%), 2-Oct-2025 (−8.5%), 21-Jul-2026 (−4% gap open) — which depress covariance with SPY and understate true sensitivity. For downside planning I would use **beta ≈ 1.2–1.3**, not 0.9.

**The 37.6% volatility alongside a −54% drawdown tells you the risk here is not cyclical beta — it is event/re-rating risk.** The equity de-rated from ~23x EBITDA to ~12.8x EV/EBITDA despite *growing* revenue 8.5% and EBITDA 15%. That divergence is the single most important market-risk observation in this file: **the market has been repricing the multiple, not the earnings.** The 20-Oct-2026 earnings print (+12% one-day move to $176.54) shows how violently the stock snaps in both directions on guidance.

---

## 4. Downside Scenario Analysis — Revenue −20%

Applied to TTM: revenue $6,592M → $5,274M (−$1,318M). Assumes 60% of cost of revenue is variable (data acquisition, processing, headcount), fixed cost base held.

| Line item | Base (TTM) | **Revenue −20%** | Revenue −30% (tail) |
|---|---|---|---|
| Revenue | $6,592M | $5,274M | $4,614M |
| Gross profit (55.2% → ~51%) | $3,638M | $2,673M | $2,308M |
| **EBIT** | $1,246M | **~$282M** | **~−$200M** |
| **EBITDA** | $2,004M | **~$1,041M** | ~$648M |
| **Interest coverage** | 5.4x | **1.2x** | **0.0x (breach)** |
| **Net debt / EBITDA** | 2.50x | **4.8x** | **7.7x** |
| Free cash flow | $1,104M | **~$450–500M** | ~$0 to negative |
| Dividend ($260M) covered? | 4.2x | **~1.8x — yes** | No |

**Can they survive it? Yes — but the financial policy breaks before the balance sheet does.**

1. **Covenant/lens risk:** net leverage of ~4.8x would sit above the ~3.5x maintenance level typical of EFX's revolver architecture. This is the binding constraint, not solvency. Note the revolver has $2.0B of committed capacity — a covenant trip would *freeze*, not *accelerate*, liquidity.
2. **The buyback is the real shock absorber.** TTM buybacks of **$1,152M** against **$1,104M of FCF** is the single most aggressive number in this file — shareholder returns of $1,412M (buybacks + $260M dividends) exceeded FCF by ~$308M, financed partly by debt (total debt +$114M TTM). In a −20% revenue world, suspending the buyback alone restores ~$1.1B of annual flexibility. That is why this is a *leverage* problem and not a *solvency* problem.
3. **Structural protection:** ~55% gross margins, near-zero inventory, negative working capital in the core bureau, and multi-year contracts mean revenue doesn't collapse the way a cyclical industrial's does. A −20% revenue decline for a credit bureau implies a depression-level collapse in origination and hiring volumes.
4. **Equity cushion:** book equity $4.49B. A −20% scenario leaves book equity intact; it takes goodwill impairment (goodwill = **$8.07B = 68% of assets, 180% of book equity**) to actually damage the balance sheet, and impairment is non-cash and does not trip leverage covenants (EBITDA-based, add-backs apply).

**Interest-rate sensitivity:** interest expense is climbing again (+15% YoY, $62.3M in Q3-26 vs $54.1M). ~$5.2B of mostly fixed-rate debt refinancing at higher coupons adds ~$50–70M/yr per 100bp on any floating/refinanced portion — coverage would drift from 5.4x toward 5.0x. This is a slow bleed, not a shock.

---

## 5. Overall Financial Risk Rating: **MODERATE**

**Credit risk: Low-Moderate. Liquidity risk: Low. Market/equity risk: High.**

The balance sheet is investment grade and the refinancing execution in 2026 was genuinely good. Profitability and cash conversion are excellent (OCF/net income = 2.17x TTM; FCF margin improved from 2.6% in FY2022 to 16.7% TTM). What holds this to "Moderate" rather than "Low" is a capital-allocation policy running at or beyond 100% of free cash flow, rising leverage (D/E 1.02x → 1.16x in four quarters), a goodwill-loaded balance sheet, and an equity that has lost 54% peak-to-trough.

---

## 6. Key Red Flags

1. 🚩 **Shareholder returns exceed free cash flow.** TTM buybacks $1,152M + dividends $260M = **$1,412M vs $1,104M FCF (+128%)**. Debt rose to fund it. This is the clearest policy risk — it converts a business risk into a balance-sheet risk at exactly the wrong point in the cycle.
2. 🚩 **Leverage inflecting upward.** Net debt/EBITDA improved to 2.50x, but D/E worsened to 1.16x and F-Score F5 failed. Rising interest expense (+15% YoY) plus buybacks means the direction of travel has changed.
3. 🚩 **Goodwill/intangibles now 68% of total assets and 180% of book equity**, having jumped **+$1.18B in Q3-2026** — consistent with an acquisition around the "definitive agreement" referenced in the July-2026 S&P rating action, debt-funded and refinanced with the October $1.0B notes. ⚠️ *Inferred from balance-sheet deltas; I could not fetch the deal terms.* Acquisition-led growth at 12.8x EV/EBITDA raises future impairment risk precisely where the equity has already de-rated.
4. 🚩 **Cash is thin: $193M, 1.6% of assets, cash ratio 0.13x.** Solvency rests entirely on cash *flow* and the $2.0B revolver, not on a cash buffer. Any operational or CP-market disruption is absorbed directly by the revolver.
5. 🚩 **Negative 3-year Sharpe (−0.455) and −54.4% drawdown** — the equity offers poor risk-adjusted compensation, with earnings-day gaps of 8–12%.
6. ⚠️ **Altman Z of 1.90 sits in the grey zone on a book-equity basis** — only the market-cap variant (3.17) clears the safe threshold. If the stock keeps falling, that cushion shrinks.
7. ⚠️ **Sector classification anomaly:** EFX is tagged "Industrials / Consulting Services," which will materially distort any peer comparison. Do not screen EFX against industrials.

### Explicit data gaps
- **Moody's current rating and outlook** — not retrievable; S&P 'BBB' is confirmed, prior BBB+/Baa1 assumed downgraded.
- **Full debt maturity ladder by year** (FY2027–FY2031) — only the 12-month bucket ($158M) is derivable from the balance sheet.
- **Covenant thresholds** — assumed ~3.5x maintenance leverage; not verified in filings.
- **Sortino ratio, CDS spreads** — unavailable.
- **Terms of the apparent Q3-2026 acquisition** — inferred from a +$1.18B goodwill step-up, not confirmed.
- **Beta conflict (0.90 calc vs 1.34 vendor)** — unresolved; I recommend using 1.2–1.3 for downside modelling.
