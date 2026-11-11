# Fin Risk Analyst

- Symbol: FSLR
- Elapsed: 132.7s

---
## Financial Risk Assessment — First Solar, Inc. (FSLR)

**Data as of:** FY2025 annual statements (period end 2025-12-31), LTM through Q3 2026, price/market data current. Yield curve as of 2026-11-11.

---

### 1. Credit Risk Assessment — **INVESTMENT GRADE** (structurally, likely net-cash A/BBB-equivalent profile)

FSLR carries **$498.6M total debt** against **$2,855.4M cash & short-term investments** — a **net cash position of ~$2.30B**. This is not a leveraged company by any measure.

| Metric | Value | Interpretation |
|---|---|---|
| Total debt | $498.6M (ST $216.0M / LT $282.6M) | Trivial vs. balance sheet |
| Net debt | **–$2,304.9M** | Net cash |
| Net debt / EBITDA | **–1.09x** | Negative = cash exceeds debt |
| Total debt / equity | 0.05x | Effectively unlevered |
| Debt / assets | 0.04x | — |
| Interest coverage (EBIT/interest) | **36.2x** | FY25 EBIT $1,625M / interest $44.1M |
| EBITDA / interest | ~48.8x | FY25 EBITDA $2,154M |
| Altman Z-Score | **3.36 — Safe zone** | See note below |
| Piotroski F-Score | **7 / 9 — Moderate/strong** | — |

**Z-score is understated, not overstated.** The tool uses *book* equity ($9.54B) in x4; at the $19.45B market cap, x4 ≈ 5.1 and the score would exceed 5.0. Even the conservative reading is comfortably in the safe zone.

**F-Score detail:** 7/9 — all profitability, liquidity and leverage tests pass. The two failures are **F7 (net share issuance — mild dilution: 106.8M → 107.2M shares)** and **F8 (gross margin did not improve: 44.2% → 40.6%)**. Neither is a credit concern.

**Refinancing cliff: none.** Short-term debt of $216M is covered **13x** by cash on hand. There is no maturity wall of any consequence through 2026–2027. FSLR has historically used low-coupon convertible notes (2030 maturities) as an opportunistic, near-zero-cost funding source rather than operational leverage.

**Credit rating:** No rating action surfaced in my search (the query returned unrelated Moody's items). FSLR's public unsecured debt is small and largely convertible, so agency coverage is thin. **Data gap** — neither S&P/Moody's issuer ratings nor CDS spreads were retrievable. Based on the metrics (net cash, >35x coverage, 2.7x current ratio), the implied standing is solidly investment grade regardless.

---

### 2. Key Financial Risk Metrics

**Liquidity — excellent, and improving**

| Metric | FY2025 | FY2024 | FY2023 |
|---|---|---|---|
| Current ratio | **2.67x** | 2.45x | 3.55x |
| Quick ratio | **2.20x** | 1.80x | 2.77x |
| Cash ratio | **1.27x** | 0.86x | — |
| Working capital | **$3,774M** | $3,012M | $3,329M |
| Equity / assets | **0.72x** | 0.66x | 0.65x |

**Cash runway: not a meaningful constraint.** With $2.86B cash and positive operating cash flow ($2,057M in FY2025), there is no burn scenario short of a catastrophic demand/policy event. **Unused revolver capacity is a data gap** — not disclosed in the retrieved filings, but immaterial given the cash balance.

**FCF sustainability — the one genuine trend concern**

| | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|
| Operating CF | $873M | $602M | $1,218M | **$2,057M** |
| Capex | $(904)M | $(1,387)M | $(1,526)M | $(870)M |
| **FCF** | $(30)M | $(785)M | $(308)M | **+$1,187M** |
| FCF yield (trailing) | — | — | — | **6.1%** |

FY2025 was the **first materially positive FCF year** after three years of heavy capacity build-out (Alabama/Louisiana/Ohio). This is a genuine inflection, but it rests on capex *stepping down* from ~$1.5B to $870M. If the growth pipeline requires re-acceleration, FCF yield compresses quickly.

---

### 3. Market Risk Profile — **aggressive / policy-driven**

| Metric | Value | Read |
|---|---|---|
| Annualised volatility (756d) | **57.45%** | ~3.5x a typical broad-market figure — very high |
| Beta vs SPY (756d, computed) | **1.10** | — |
| Beta (profile, 5Y) | **1.71** | Discrepancy = regime instability |
| Max drawdown (3Y) | **–52.9%** | Halved within the window |
| Sharpe ratio | **0.079** | Essentially zero risk-adjusted return |
| Sortino | Not available | **Data gap** |

**Note the beta conflict:** the tool's 756-day computed beta (1.10) and the profile's 5-year beta (1.71) diverge sharply. This itself is the finding — FSLR's correlation to the market is unstable, and its realized 57% volatility is driven mostly by **idiosyncratic policy and tariff headlines**, not market beta. Market-beta hedging will not protect a holder here.

The Sharpe of 0.08 means volatility has been almost entirely *uncompensated* over three years. Investors have borne 57% vol for no excess return.

**Valuation context:** at $180.98 (market cap $19.45B) on LTM EPS of ~$17.3, FSLR trades at roughly **10.5x earnings**. A 58% gross-margin business at 10x is the market explicitly discounting the durability of its earnings stream — consistent with the policy-dependency finding below.

**Rate backdrop:** 10Y at 5.13%, 2Y at 4.74%, 2s10s **+39bp (no inversion)**. Elevated long rates raise the discount rate on long-duration, subsidy-linked cash flows and increase the hurdle for the capex program — a mild but persistent headwind for the equity multiple.

---

### 4. Downside Scenario Analysis — Revenue –20%

**Base (LTM Q3'26):** Revenue $5,014M; EBITDA $2,541M; EBIT $1,958M; net income $1,862M; net cash $2,304M.

| | Base LTM | Revenue –20% | Comments |
|---|---|---|---|
| Revenue | $5,014M | **$4,011M** | — |
| Gross profit (≈52% contribution) | $2,541M | $2,019M | Variable cost ~48% of sales |
| EBITDA | $2,541M | **~$2,019M** | EBITDA margin still ~50% |
| EBIT | $1,958M | **~$1,436M** | D&A fixed at ~$583M |
| Interest expense (annualised) | ~$21M | ~$21M | — |
| **Interest coverage** | ~93x | **~68x** | No stress whatsoever |
| Net debt / EBITDA | –0.91x | **–1.14x** | Net cash position *widens* |
| Net income (post-credit) | $1,862M | **~$950M–1.05M** | 45X scales with *volume*, so credits fall ~20% (–$420M) |
| Altman Z | 3.36 | ~3.1 | Still Safe zone |
| Current ratio | 2.67x | >2.2x | — |

**Conclusion: FSLR survives a 20% revenue decline without a covenant breach, a refinancing problem, or a liquidity question.** A 40% decline would still leave interest coverage above 30x and the company in net cash. The credit is robust through any plausible demand shock.

**The real tail risk is not volume — it is policy.** 2026 guidance explicitly bakes in **$2.10–2.19B of Section 45X advanced-manufacturing tax credits**, a figure that *exceeds* LTM net income of $1.86B. Strip the credits and reported profitability falls toward a small fraction of current levels, even though the underlying factory economics remain cash-generative. Separately, guidance carries **$115–135M of underutilization costs**, a signal that factories are already running below capacity. This is an **equity-valuation risk, not a solvency risk** — and the ~10x P/E says the market is already partially pricing it.

*Caveat:* I could not verify precisely where in the P&L 45X is recognized (cost of revenue vs. tax benefit), so the net-income sensitivity above is directionally sound but not a clean bridge. Flagged as a data gap.

---

### 5. Overall Financial Risk Rating: **LOW** (credit) / **MODERATE–HIGH** (equity)

This is the central tension in FSLR. **Balance-sheet risk is genuinely low** — net cash of $2.3B, 0.05x debt/equity, 36x interest coverage, 2.67x current ratio, Z-score in the safe zone, no maturity wall, and FCF newly positive at a 6.1% yield. A prolonged downturn is survivable with room to spare.

But **the equity carries high risk**: 57% annualised volatility, a 53% max drawdown, a near-zero Sharpe, gross margins (58% in Q3'26) that are substantially policy-derived, a backlog that has begun to erode (45.1 GW at Q2'26 → **44.0 GW at Q3'26**), and revenue that declined **23% YoY in Q3 2026** even as earnings rose — the classic signature of a business whose profit is being held up by credits and tariff protection while underlying volume falls.

**Blended rating: MODERATE overall** — low probability of financial distress, high dispersion of equity outcomes.

---

### 6. Key Red Flags

1. **Earnings are policy-funded.** $2.10–2.19B of 45X guidance vs. $1.86B LTM net income. Legislative or administrative erosion of 45X is a direct, first-order hit to reported earnings. *This is the single largest risk in the name.*
2. **Revenue contracting while margins expand.** Q3'26 sales –23% YoY ($1.23B vs. $1.59B) yet net income +25%. Margin expansion is masking volume weakness. Unsustainable as a pattern.
3. **Backlog depletion.** 45.1 GW → 44.0 GW in one quarter. Contracted future revenue is shrinking, not growing.
4. **Underutilization costs of $115–135M** — management is already guiding to factories running below capacity.
5. **Volatility without compensation.** 57% annualised vol / Sharpe 0.079 / –52.9% drawdown. Position sizing must respect this; beta-based hedging is ineffective.
6. **Gross margin deterioration at the annual level.** FY24 44.2% → FY25 40.6% (F-Score F8 fail), even as quarterly margins have since spiked — high quarter-to-quarter dispersion in the core profitability metric.
7. **Capex-step-down dependency.** FSLR's FCF turnaround relies on capex normalizing near $870M. Re-acceleration of the growth build would return the company to negative FCF, as in FY23–FY24.

**Data gaps explicitly flagged:** (a) no agency credit rating or CDS spread retrieved; (b) unused revolver capacity not disclosed in retrieved data; (c) no Sortino ratio; (d) no peer comparison — the sector-peer tool returns oil & gas majors (XOM, CVX, SHEL), which are **not valid comparables** for a solar module manufacturer, so no relative leverage read is offered; (e) exact P&L location of 45X recognition unverified; (f) no annual debt maturity schedule beyond the ST/LT split.
