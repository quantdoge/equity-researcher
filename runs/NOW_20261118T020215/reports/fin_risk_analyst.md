# Fin Risk Analyst

- Symbol: NOW
- Elapsed: 93.3s

---
## FINANCIAL RISK ASSESSMENT — ServiceNow, Inc. (NOW)

**Data as-of:** FY2025 audited (filed 2026-01-29) + Q3 FY2026 results (filed 2026-10-28); last close $102.25 (2026-11-13). Note: the ratio tools (`leverage/liquidity/altman/piotroski`) return **FY2025 year-end only** and are ~3 quarters stale — I recomputed everything on a TTM-to-Q3'26 basis. Peer benchmark unavailable (see gaps).

---

### 1. Credit Risk Assessment — **INVESTMENT GRADE (lower tier), NEGATIVE TRAJECTORY**

NOW entered FY2026 as a net-cash company and levered up mid-year to fund a ~$7.6B acquisition. Solvency remains comfortable, but *every* credit metric deteriorated simultaneously in the last three quarters:

| Credit metric | FY2024 | FY2025 | TTM Q3'26 | Direction |
|---|---|---|---|---|
| Total debt | $2.28B | $2.40B | **$8.42B** | ▲ 3.5x |
| Cash & ST inv. | $5.76B | $6.28B | $4.61B | ▼ |
| Net debt | $(26)M | $(3.88B) | **+$6.02B** | ▼ swing |
| Debt/equity | 0.24x | 0.19x | **0.64x** | ▲ |
| Debt/assets | 0.11x | 0.09x | 0.26x | ▲ |
| Net debt/EBITDA | ~0.0x | −1.29x | **1.75x** | ▲ |
| EBITDA / interest | ~101x | ~130x | **21.7x** | ▼ |
| Operating income / interest | ~77x | 79.3x | **9.4x** | ▼ |
| Goodwill+intangibles / equity | 15% | 36% | **104%** | ▲ |

Forward run-rate coverage is thinner still: Q3'26 interest expense was $81M (≈$324M annualised vs. $6M/quarter in early FY2026), implying **~10.6x EBITDA / ~4.6x operating-income coverage** on the new capital structure.

**Mitigants:** $4.75B TTM free cash flow covers total debt in <2 years; $4.61B cash covers all $8.4B debt at 0.55x… more precisely cash/total debt = 0.55x and cash + one year of FCF ≈ $9.4B > total debt. Interest-bearing debt is now ~3.9% coupon, fixed, no near-term covenant stress disclosed. No credit rating or CDS spread was available in the feed (gap) — I would expect a mid-BBB profile with negative outlook.

**Refinancing:** $2.09B short-term + $1.49B legacy 2027 converts ≈ **$3.6B due within ~15 months**, against $4.6B cash and $4.75B annual FCF. Covered, but the cushion is no longer the fortress it was in FY2025.

---

### 2. Key Financial Risk Metrics Table

| Metric | FY2025 | TTM Q3'26 | Read |
|---|---|---|---|
| Revenue / growth | $13.28B / +20.9% | $15.43B / +20.5% (Q3) | Growth intact |
| Gross margin | 77.5% | **73.1%** (Q3'26: 70.5%) | ⚠ −4.4pp, structural? |
| GAAP operating margin | 13.7% | **9.7%** (Q2'26: 4.1%) | ⚠ severe compression |
| EBITDA margin | 22.6% | 22.3% | Stable |
| FCF / FCF margin | $4.58B / 34.5% | $4.75B / **30.8%** | ▼ but healthy |
| SBC / revenue | 14.7% | **15.1%** | High, sticky |
| SBC / FCF | 42.7% | **48.9%** | ⚠ ~half of FCF is stock comp |
| FCF yield (mkt cap $105.6B) | 4.7% | 4.5% | Adequate; **2.3% ex-SBC** |
| Current ratio | 1.00 | **0.72** | ⚠ headline weak |
| Quick / cash ratio | 1.00 / 0.60 | 0.72 / 0.39 | Deferred-revenue artefact |
| Working capital | +$28M | **−$3.32B** | ⚠ |
| Altman Z (book equity) | 1.675 (distress) | **1.21** (distress) | ⚠ but see caveat |
| Altman Z (market equity) | ~5.5 (safe) | **~4.18** (safe) | True reading |
| Piotroski F-Score | **5 / 9** | n/a (not recomputed) | Moderate |
| Net debt/EBITDA | −1.29x | 1.75x | Still <2x |

**Altman caveat (important):** the tool's Z uses *book* equity (x4 = 0.70) and penalises deferred revenue via x1 (negative working capital). Substituting the actual $105.6B market cap (x4 = 5.64) gives **Z ≈ 4.2 — safe zone**. The book-based "distress" reading is a false positive for subscription software with customer prepayments; however, the *deterioration* from 1.68 → 1.21 is real and directionally correct.

**Piotroski (5/9):** lost points on ROA decline, net dilution, gross-margin decline, and asset-turnover decline — three of four are acquisition artefacts, one (dilution) is genuine.

---

### 3. Market Risk Profile — **HIGH / TAIL-RISK ELEVATED**

| Metric | Value |
|---|---|
| Annualised volatility (3y) | **52.2%** (~3x the index) |
| Beta vs SPY | 1.155 (vendor profile: 0.984 — inconsistent) |
| Max drawdown (3y) | **−64.5%** ($234.08 Jan-2025 close → $83.00 Apr-2026) |
| Peak-to-current | **−56.3%** ($102.25) |
| Sharpe (3y, rf=0) | **−0.348** |
| Sortino | *Not provided by tool — data gap* |
| Fat-tail events | −27.0% (2026-10-29, 76M shares), −13.9% (2026-04-09), −11.5% (2025-12-15), −11.5% (2026-07-23), −10.0% (2026-01-29) |

**Interpretation:** beta of ~1.0–1.16 materially *understates* risk. NOW's drawdown is idiosyncratic (multiple compression + AI-disruption de-rating against seat-based licensing), not market-driven. Five separate −10%+ single-day gaps in 22 months means options-implied tail risk, not beta, governs position sizing. A −65% peak-to-trough and a subsequent −36% three-week collapse (Oct 23 → Nov 13) confirm the equity is a high-duration asset whose price is a *sentiment* function, not a solvency function.

---

### 4. Downside Scenario Analysis — Revenue −20%

Applied to TTM base ($15.43B revenue, 73% GM, $9.78B opex, $3.44B EBITDA, $1.49B op. income, $4.75B FCF):

| Line | Base TTM | −20% rev, no cost action | −20% rev, 15% opex cut |
|---|---|---|---|
| Revenue | 15,431 | 12,345 | 12,345 |
| Gross profit (73%) | 11,277 | 9,012 | 9,012 |
| Opex | 9,784 | 9,784 | 8,316 |
| Operating income | 1,493 | **−772** | **+696** |
| EBITDA | 3,436 | ~1,214 | ~2,682 |
| Interest (fwd $324M) | 158→324 | 324 | 324 |
| **EBITDA / interest** | 21.7x | **~3.7x** | **~8.3x** |
| **Net debt / EBITDA** | 1.75x | **~5.0x** | **~2.2x** |
| FCF (~12–15% margin) | 4,750 | ~1,500–1,850 | ~1,850–2,300 |
| Cash + FCF vs $3.6B maturities | ample | **adequate (needs revolver)** | adequate |

**Conclusion:** a 20% revenue decline — which would be unprecedented for NOW (worst-ever growth is +20.9%) — does *not* threaten solvency. It converts the company from net cash to ~2–5x levered with 4–8x interest coverage: still investment grade, but it would force a rating outlook cut, halt buybacks, and likely trigger a goodwill impairment against the $13.6B intangible balance (104% of equity). The realistic bear case is not default; it is **de-rating plus impairment plus dilution**.

Liquidity runway is not a binding constraint in any scenario: the company is cash-generative at 30.8% of revenue, so cash burn = $0.

---

### 5. Overall Financial Risk Rating: **MODERATE** *(was Low in FY2025)*

- **Solvency/credit risk: Low-to-Moderate** — net debt/EBITDA 1.75x, FCF/debt 0.56x/yr, cash covers near-term maturities with a year of FCF to spare.
- **Liquidity risk: Moderate** — current ratio 0.72 and −$3.3B working capital look alarming but are dominated by deferred revenue; true cash liquidity ($4.6B) is fine.
- **Market/equity risk: High** — 52% vol, −64.5% drawdown, negative 3-year Sharpe, repeated double-digit gaps.
- **Direction of travel: Negative.** Leverage tripled, coverage fell ~85%, gross margin fell 4–7pp, FCF margin fell 3.7pp, and buybacks were suspended to fund M&A — all in nine months.

---

### 6. Key Red Flags

1. **Leverage inflection:** $6.0B of debt raised in Q2 FY2026 to fund ~$7.6B of goodwill. Net debt swung from −$3.9B to +$6.0B in three quarters. Classic late-cycle, debt-funded M&A.
2. **Goodwill = 104% of equity** ($13.6B, 43% of assets). Any impairment hits book equity directly; equity is the Altman cushion.
3. **Gross margin collapse 77.5% → 70.5%** — the most credit-relevant trend in the file. If AI inference/hosting costs are structural rather than transitional, the long-run FCF margin (currently 30.8%) compresses permanently.
4. **Cash conversion deterioration:** working capital drag of −$1.50B across Q1–Q3 FY2026 (vs. +$826M inflow in Q4'25). Q2'26 FCF fell to $473M and Q3'26 to $748M — billings/collections are softening even as revenue grows 20%+.
5. **SBC ≈ 49% of FCF** ($2.32B TTM, 15.1% of revenue) plus ~0.7%/yr dilution. "True" owner earnings FCF yield is 2.3%, not 4.5%.
6. **Coverage optics:** operating income covered interest 9.4x TTM and only ~4.6x on the Q3'26 annualised interest run-rate.
7. **Deferred-revenue-driven liquidity optics:** current ratio 0.72, quick ratio 0.72, negative working capital — will screen as a liquidity failure in naive models.
8. **Demand-side thesis risk:** per news, the equity de-rating is driven by cRPO/backlog disappointment and fears that AI agents hollow out seat-based licensing — a revenue-durability question no balance-sheet metric can answer.
9. **Beta mis-measures risk:** 1.16 beta vs 52% realised vol and −64.5% drawdown.

### Data Gaps (explicit)
- **No credit rating or CDS spread** in the feed — investment-grade call is inferred from ratios, not confirmed.
- **No Sortino ratio, no implied volatility, no options skew.**
- **Peer benchmarking unavailable:** `get_sector_peers` returned mega-cap semiconductors/Apple/Microsoft, not application-software comps; no peer multiples computed.
- **Altman Z and Piotroski F are only available on FY2025 annual data** (no TTM version); Piotroski not recomputed for FY2026.
- **Quarterly history pre-2025 unavailable**, so seasonality in FCF/working capital cannot be normalised — the Q2/Q3 FCF weakness may be partly seasonal (Q1 is billings-heavy).
- News feed returned items dated later/earlier than the price series in places; treated as directional context only.
- Vendor inconsistencies flagged: profile beta 0.984 vs computed 1.155; profile price $92.90 vs last close $102.25; balance-sheet `net_debt` (−$1.32B) vs computed (−$3.88B) for FY2025.
