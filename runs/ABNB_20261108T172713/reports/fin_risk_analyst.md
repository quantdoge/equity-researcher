# Fin Risk Analyst

- Symbol: ABNB
- Elapsed: 45.2s

---
I have sufficient data. One note: the yield curve (Nov-2026) shows 10Y at 5.13% — a high discount-rate backdrop that matters for a long-duration growth equity. Writing the assessment now.

---

# ABNB — Financial Risk Assessment
**As of 8 Nov 2026 | Price $189.99 | Market cap $113.8B | Net cash position**

---

## 1. Credit Risk Assessment

**Rating: INVESTMENT GRADE (high quality) — equivalent to A-/Baa1**

| Evidence | Value |
|---|---|
| S&P issuer rating | **A-** (stable) |
| Moody's rating | **Baa1** |
| Net debt / EBITDA | **−3.24x** (net **cash**, FY2025) |
| Gross debt / EBITDA (TTM) | **0.78x** |
| Cash / total debt | **5.0x** |
| Interest coverage (pro forma) | **~17–19x** |

I verified externally that Airbnb carries a **single-A-tier credit profile** (S&P A-, Moody's Baa1 one notch lower). The company retired its $2.0B **0% convertible** in March 2026 and made a high-grade bond debut of **$2.5B**, which is why reported "interest expense = 0" in FY2025 and a positive $37–45M/quarter thereafter. Solvency risk is negligible: cash of **$12.59B** against ~$2.5B of debt.

**Counterpoint that must be disclosed:** the Altman Z-Score reports **1.224 — "Distress zone."** This is a mechanical artifact, not a credit signal (see §2).

---

## 2. Key Financial Risk Metrics

| Metric | Value | Assessment |
|---|---|---|
| Debt / Equity | 0.28 | Very low |
| Debt / Assets | 0.10 | Very low |
| Net debt / EBITDA | −3.24x | **Net cash** |
| Interest coverage (EBIT/interest) | **n/a reported** (FY2025 interest = $0); pro forma ~17.5x | Strong |
| Current ratio | 1.38 | Adequate |
| Quick ratio | 1.38 | Adequate (no inventory) |
| Cash ratio | 0.81 | Strong |
| Working capital | +$5.15B | Positive |
| Altman Z-Score (book equity) | **1.224 — Distress** | Misleading, see below |
| **Altman Z (market-cap equity)** | **≈ 5.7 — Safe zone** | Recomputed by me |
| Piotroski F-Score | **5 / 9 — Moderate** | Understated by buybacks |
| FCF yield (trailing) | 3.93% (FY2025) / **4.41%** (TTM) | Moderate |
| FCF yield ex-SBC | ~2.9% | Weak-to-moderate |
| Equity / Assets | 0.37 | Thin, buyback-driven |
| Retained earnings | **−$5.50B** | Accumulated deficit |

**Two critical adjustments to the headline scores:**

**(a) Altman Z = 1.224 is a false alarm.** The tool's X4 uses *book* equity ($8.2B / $14.0B liabilities = 0.585) and X2 is negative because of the accumulated deficit. Substituting market capitalization ($113.8B) into X4 gives 7.56, producing **Z ≈ 5.7 — deep in the safe zone**. Using Q3'26 balance sheet: X1 = 0.367, X2 = −0.225, X3 = 0.130, X4 = 7.56, X5 = 0.573 → Z ≈ 5.7. Any analyst quoting 1.224 without this adjustment would badly misjudge the credit.

**(b) Piotroski F = 5 understates quality.** Three of the four missed points are artifacts: **F5 (lower leverage) and F6 (positive equity change)** are penalties caused by **$3.79B of FY2025 buybacks** shrinking book equity, not by deterioration; **F8 (gross margin improvement)** is driven by a data anomaly (see §6). Genuine misses: F3 (ROA improvement) only.

---

## 3. Market Risk Profile

| Window | Ann. Volatility | Beta vs SPY | Max Drawdown | Sharpe |
|---|---|---|---|---|
| 1 year (252d) | **41.8%** | 1.12 | 21.5% | 1.40 |
| 3 years (756d) | **38.2%** | 1.21 | 34.5% | 0.77 |
| 5 years (1260d) | **37.4%** | 1.30 | 37.2% | 0.54 |

- **Volatility is extreme**: 38–42% annualised, roughly 2.3–2.6x a broad equity index. A 1-sigma annual move is ±$72 on a $190 stock.
- **Beta is high and rising** across horizons (1.12 → 1.21 → 1.30; profile beta 1.268). In a market drawdown, expect ABNB to fall **~1.2–1.3x the index** — plus idiosyncratic travel/consumer risk on top.
- **Sharpe ratios improve sharply at short horizons** (1.40 1-yr vs 0.54 5-yr), indicating a strong recent run, not durable risk-adjusted quality.
- **Drawdown caveat:** the 5-yr window begins *after* the Feb-2021 peak, so it understates the true post-IPO peak-to-trough decline (~2021 high to Dec-2022 low exceeded 50%). Treat 37% as a floor, not a ceiling, for cycle risk.
- **Data gap:** Sortino ratio is not computable with the available toolset (no downside-deviation output). Flagged, not estimated.

**Macro overlay (8 Nov 2026):** 2Y 4.74%, 10Y **5.13%**, 30Y 5.47%, 2s10s +39bp (no inversion). Positive slope removes recession-signal comfort, but **5%+ long rates are a direct multiple risk** for a ~35x P/E, long-duration growth equity, and raise the cost of the company's newly issued debt.

---

## 4. Downside Scenario Analysis — Revenue −20%

TTM base (Q4'25 + Q1–Q3'26): revenue **$13,956M**, EBIT **$3,158M** (22.6% margin), FCF **$5,019M**, SBC $1,770M.

Using a **38% variable / 62% contribution-margin** cost structure (fixed cost base ≈ **$5,495M**):

| Scenario | Revenue | EBIT | EBIT margin | Interest cov. | FCF | Net cash |
|---|---|---|---|---|---|---|
| Base (TTM) | $13,956M | $3,158M | 22.6% | ~17x | $5,019M | ~$10.1B |
| **−20%, no cost action** | $11,165M | **$1,427M** | 12.8% | ~8x | ~$2.6B | ~$10B |
| −20% with 15% fixed-cost cut | $11,165M | **$2,251M** | 20.2% | ~12x | ~$3.4B | ~$10B |
| −35% severe | $9,071M | **$129M** | 1.4% | <1x | ~$1.4B | ~$10B |

**Key finding — operating break-even requires a ~36% revenue decline** ($5,495M ÷ 0.62 = $8,863M). In 2020 Airbnb absorbed a ~30% revenue collapse and cut opex >40%; management has demonstrated this flexibility. A 20% revenue shock leaves the company **solidly profitable, FCF-positive, and holding ~$10B of net cash** — it survives comfortably.

**The binding risk is equity valuation, not solvency.** At −20% revenue with no cost action, TTM FCF drops to ~$2.6B (2.3% yield), which at 35x earnings implies severe multiple compression. Downside is a **−40% to −50% share price**, not a credit event.

**Seasonality warning:** Q1 is structurally thin — Q1'26 EBIT was only **$84M (3.1% margin)** on $2,678M of revenue. A demand shock landing in Q1 rather than peak summer produces a quarterly loss even if the full-year math above holds.

---

## 5. Overall Financial Risk Rating

# MODERATE
**(Solvency risk: LOW | Liquidity risk: LOW | Market/equity risk: HIGH | Regulatory risk: ELEVATED)**

This is a **balance-sheet fortress attached to a high-volatility, regulation-exposed equity**. Creditors are well protected (A-/Baa1, net cash, 17x coverage, ~36% revenue cushion to operating break-even). Equity holders bear 38–42% volatility, ~1.2–1.3 beta, and a 21–37% drawdown record.

---

## 6. Key Red Flags & Data Gaps

**Red flags**
1. **FCF margin is deteriorating:** 40.5% (FY22) → 39.2% → 40.7% → 37.8% (FY25) → **36.0% (TTM)**, with a $997M working-capital drag in Q3'26. Growth is being bought with marketing spend; cash conversion is trending the wrong way.
2. **SBC is 12.7% of revenue** ($1.77B TTM). GAAP FCF of $5.0B overstates distributable cash by ~35%; ex-SBC FCF yield is only ~2.9%. Buybacks ($3.9B in FY2025) currently outpace SBC — shares fell 623M → 597M diluted — but that is management discretion in a downturn.
3. **Aggressive capital return into a thin equity base:** retained earnings −$5.5B; equity/assets 0.37. Continued buybacks would shrink the cushion precisely when a shock hits.
4. **Regulatory concentration is the real tail risk:** short-term-rental restrictions in major cities/markets can impair supply and take-rate in ways no financial ratio captures. **Not quantified by any tool — qualitative flag only.**
5. **Reported Altman Z of 1.224 will be misread** by screens and quant models; adjusted Z is ~5.7.

**Data gaps / inconsistencies (flagged, not silently resolved)**
- **Net debt conflict:** leverage tool reports **−$8.74B**; balance sheet reports **−$4.29B** (FY25) / **−$7.27B** (Q3'26). Likely lease-treatment differences. Direction is unambiguous either way (net cash).
- **FY2025 gross margin looks corrupted:** cost of revenue jumped to $3,413M from $1,878M while revenue grew only 10.8%, implying an impossible $1,506M Q1'25 COGS vs $907M actual in Q1'26. Almost certainly a reclassification. The 72.3% gross margin figure is **not** a real margin collapse.
- **Q3'26 balance sheet shows total_debt = $0** despite $45M of quarterly interest expense and $2.50B of debt in Q2'26 — a clear error; I used the Q2'26 $2.496B figure.
- **FY2025 interest expense = 0** (0% convertible notes), so no reported interest coverage ratio exists; I computed it pro forma.
- **Q3'26 D&A = 0** and capex = 0 across periods — depreciation is immaterial (~0.5% of revenue, asset-light) but the zero is not credible.
- **Sortino ratio** unavailable; **peer benchmarking not performed** — the sector-peer list returned only mega-cap Consumer Cyclical names (AMZN, TSLA, HD, MCD) with no direct OTA/marketplace comparables (no BKNG, EXPE, or DASH), making peer multiples non-informative. Flagged as a gap.
- **No debt maturity ladder** was retrievable; based on the March-2026 $2.5B high-grade issuance, the next material maturity appears to be ~2030+, and $12.6B of cash covers all debt ~5x — no refinancing cliff. **Covenant details unverified**; IG senior notes typically carry incurrence rather than maintenance covenants, consistent with low risk.
