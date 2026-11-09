# Fin Risk Analyst

- Symbol: SITM
- Elapsed: 50.1s

---
# Financial Risk Assessment — SiTime Corporation (SITM)

**Critical framing note:** SITM's capital structure changed fundamentally in mid-2026. The ratio tools returned **annual FY2025 data (pre-acquisition)** — net cash, no debt. As of Q3 2026 the company carries **$1.35B of convertible notes**. All FY2025-based metrics below are therefore historical and no longer describe current credit risk. I flag this throughout rather than presenting stale numbers as current.

---

## 1. Credit Risk Assessment

**Rating: Sub-Investment Grade (indicative BB-/B+ area) — NOT verified against agency ratings; SITM appears unrated.** Data gap: no rating/CDS spread available from tools. I note this explicitly.

The company was **net-cash and effectively debt-free** through FY2025 (total debt $4.7M = leases; cash $808.4M). That is no longer true:

| Event (2026) | Amount |
|---|---|
| Acquisition of Renesas Timing business (closed Jul 1, 2026) | $1,499.3M cash + 3,558,691 shares |
| 0% Convertible Senior Notes due 2031 (issued May 2026) | $1,350M principal |
| Cash + ST investments, Sep 30, 2026 | $324.3M |
| **Pro forma net debt** | **≈ $1,026M** |

**Direction of travel: net cash of +$804M (Dec-2025) → net debt of ~–$1,026M (Sep-2026), a ~$1.8B swing in six months.** This is the single most important fact in this report.

Mitigants are genuinely strong: the coupon is **0%**, so cash interest expense is zero; the notes mature **June 2031** (no near-term refinancing cliff); the issue was accompanied by **capped call transactions** (partial dilution offset); and the acquired business was underwritten at ~$300M revenue at ~70% gross margin.

The real credit risk is not interest coverage — it is **repayment/conversion of a $1.35B bullet**. If the equity does not appreciate, this is cash debt that must be refinanced against a company whose historical FCF never exceeded ~$35M. That is a classic "good coverage, weak principal repayment capacity" high-yield profile.

---

## 2. Key Financial Risk Metrics

| Metric | Value | As-of | Read |
|---|---|---|---|
| Debt / Equity | **0.00x** | FY2025 | Stale — pre-deal |
| Net debt / EBITDA | **–(net cash)** | FY2025 | Stale — pre-deal |
| Interest coverage (EBIT/int.) | n/a (no debt) | FY2025 | Stale |
| Current ratio | **11.3x** | FY2025 | Stale — pre-deal |
| Quick ratio | 10.33x | FY2025 | Stale |
| Cash ratio | 9.62x | FY2025 | Stale |
| Equity / Assets | 89% | FY2025 | Stale |
| **Altman Z-Score** | **5.71 (Safe)** | FY2025 | Stale — assumes zero debt |
| **Piotroski F-Score** | **7 / 9 (Moderate)** | FY2025 | Losses on F1 (ROA<0) and F7 (dilution) |
| Operating margin | –18.5% (FY2025) → **+2.8% GAAP (Q3'26)** | — | Inflection |

**Estimated current (Q3 2026 annualized) leverage — my own calculation, since tools cannot see the Sept-30 balance sheet:**

| Item | Estimate |
|---|---|
| Q3-26 non-GAAP operating income (reported) | $129.5M → ~$518M annualized |
| + Depreciation (ex-intangible amortization) | ~$48M annualized |
| **Adjusted EBITDA, annualized** | **~$566M** |
| Less stock-based comp (~$35M/qtr) | ~$140M annualized |
| **Cash EBITDA after SBC** | **~$426M** |
| **Net debt / adj. EBITDA** | **~1.8x** |
| **Net debt / cash EBITDA (post-SBC)** | **~2.4x** |
| Cash interest coverage | **effectively infinite (0% coupon)**; ~$7–9M/yr non-cash issuance-cost amortization |

**Data gap:** `get_balance_sheet` returned annual periods only; the Sept-30-2026 balance sheet is not retrievable through the tools. Net debt and leverage above are constructed from 10-Q disclosures ($1,350M notes, $324.3M cash) and are **estimates with ±$100M+ uncertainty** (working capital and earnout liabilities moving fast).

---

## 3. Market Risk Profile

| Metric | Value |
|---|---|
| Annualised volatility (756d) | **84.5%** |
| Beta vs SPY | **2.77** (profile: 2.91) |
| Max drawdown (3y) | **–60.6%** |
| Sharpe ratio | 0.99 |
| Sortino | not available (data gap) |
| Latest close | $745.56 |
| 52-week-ish range evident in data | ~$105 → ~$901 |

This is an **extremely high-beta, high-volatility equity**. The –60.6% max drawdown is real and recent: Feb-2025 ~$257 → Apr-2025 ~$105 (–59%) in ten weeks. In 2026 the stock ran from ~$311 (Mar 30) to $901 (May 11), then fell 30% to ~$626 within four weeks. A beta of 2.8 means a 20% index drawdown implies a **~55–60% decline** in SITM. At **19x annualized sales and ~46x annualized non-GAAP EPS**, there is very little valuation support — the stock is priced as a derivative on AI-datacenter timing demand, not on balance sheet.

**FCF yield is ~0.2–0.3%** (FY2025: $34.7M FCF / $10.4B mcap = 0.33%; on the current ~$22.5B market cap with $39.6M TTM FCF, ~0.18%). **The equity provides essentially no cash return cushion.**

*Caveat:* the vol/beta/drawdown were computed on a window that does not appear to extend through the full 2026 run-up; treat as indicative, likely understating current realized volatility.

---

## 4. Downside Scenario: Revenue –20%

Applied to the ~$1.19B annualized 2026 run-rate, with non-GAAP gross margin ~68% after fixed-cost absorption and opex largely fixed (~$326M):

| Line | Base | –20% Revenue | –40% (severe) |
|---|---|---|---|
| Revenue | $1,190M | $952M | $714M |
| Gross profit (~68%) | $841M | $647M | $486M |
| Non-GAAP opex | $326M | $326M | $326M |
| Non-GAAP op income | $518M | **$321M** | **$160M** |
| Adj. EBITDA (annualized) | $566M | ~$371M | ~$208M |
| **Net debt / EBITDA** | **1.8x** | **~2.8x** | **~4.9x** |
| FCF (after SBC, capex, tax) | ~$180M | **~+$120M** | **~–$40M** |
| Implied equity move (β 2.8) | — | **–45% to –60%** | –70%+ |

**The operating business survives a 20% revenue decline comfortably** — leverage of ~2.8x on a 0% coupon with 2031 maturity is not a credit event. **The equity does not.** And the second-order effect is the real risk: a 50%+ stock decline puts the $1.35B convert deep out of the money, converting it from an equity-linked instrument into a **hard cash obligation refinanced in 2031** — at precisely the moment the company's cost of capital is highest. At a –40% revenue shock, 4.9x leverage plus negative FCF is genuine distress territory for a cyclical semiconductor supplier.

Additional downside amplifier: **Q3 2026 consumed $126.5M of working capital** (inventory and receivables build for the TPD integration, including inventory step-up). If demand reverses, that build becomes a **writedown risk** rather than a recoverable asset.

---

## 5. Overall Financial Risk Rating: **HIGH**

Split by risk type, because the blended answer is misleading:

- **Solvency / liquidity risk: LOW.** $324M cash, zero cash interest, 2031 maturity, no covenants disclosed, positive GAAP net income ($17.3M 9M-2026).
- **Leverage risk: MODERATE** (~1.8–2.4x net debt/EBITDA; but a 2031 bullet that likely requires refinancing or conversion).
- **Market / valuation risk: CRITICAL.** 84.5% vol, 2.8 beta, –60.6% historical drawdown, 19x sales, 0.2% FCF yield.
- **Business/earnings-quality risk: HIGH.** ~97% of Q3 non-GAAP net income ($130.3M) is excluded by GAAP ($4.4M).

The company will not go bankrupt in a normal downturn. The **equity** can lose half its value on a modest demand wobble, and the convert structure creates an asymmetric refinancing exposure that only bites if the growth story breaks.

---

## 6. Key Red Flags

1. **Overnight releveraging:** net cash $804M → net debt ~$1.03B in six months via a $1.35B convert and a $1.5B acquisition. Credit profile is now unproven and integration-dependent.
2. **$1.35B bullet vs. thin FCF:** trailing FCF $39.6M; FCF/debt ≈ **3%**. Repayment capacity rests entirely on the equity conversion option or a future refinancing.
3. **Stock-based compensation of $103.5M in FY2025 = 32% of revenue** (~$140M annualized in 2026). Non-GAAP profitability is substantially an SBC-exclusion artifact; F7 dilution flag on the Piotroski score is corroborated by 26.4M → 30.2M shares outstanding.
4. **GAAP earnings near zero despite record revenue:** Q3 2026 GAAP net income $4.4M on $298.7M revenue, held down by **$73.3M/qtr amortization of acquired intangibles plus $37.4M of acquisition costs**. GAAP EPS will stay depressed for years.
5. **Extreme valuation & volatility:** 19x sales, ~46x annualized non-GAAP EPS, 84.5% vol, beta 2.8, 60.6% max drawdown. No valuation floor.
6. **Working capital reversal risk:** –$126.5M working capital swing in Q3 2026 turned FCF negative (–$17.7M); inventory step-up amortization signals above-market inventory carrying values.
7. **Concentration/cyclicality:** semiconductor timing components, heavily Taiwan/Hong Kong distribution and Asian manufacturing; AI-datacenter demand concentration is a single-theme dependency.
8. **Governance/near-term overhang:** 3-for-1 stock split effective Dec 4, 2026; notes not yet convertible at Sep-30 (no conversion condition met), so upside participation accrues to noteholders only in a rising-stock scenario.

---

## Data Gaps (explicit)
- **No quarterly balance sheet available** — Sept-30-2026 debt, cash, goodwill, earnout liabilities and current ratios are estimated from 10-Q text, not tool data. Post-deal current/quick ratios, Z-score and F-score **cannot be computed** on a current basis.
- **All ratio tools (Z-score 5.71, F-score 7, current ratio 11.3x, D/E 0.0x) are FY2025, pre-acquisition, and should be disregarded for present credit assessment.**
- **No credit rating or CDS spread** retrieved; rating above is my indicative construct.
- **Sortino ratio not available.**
- **Tool price/market-cap fields are stale** ($416.92 / $12.5B) versus the latest close in the price history ($745.56). Implied market cap at $745.56 × 30.21M shares ≈ **$22.5B** — I used this for FCF-yield and valuation work.
- No peer-multiple benchmark computed (sector peer list returned mega-caps: NVDA, AVGO, AMD — not size-appropriate comparables for a $22B timing specialist).
