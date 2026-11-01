# Fin Risk Analyst

- Symbol: CBOE
- Elapsed: 60.8s

---
## CBOE Global Markets, Inc. — Financial Risk Assessment

**Reporting date:** FY2025 audited (12/31/25) plus Q3 2026 10-Q (9/30/26, filed 10/30/26). Price feed ends 6/30/2026; profile quote ($335.53) is later — see Data Gaps.

---

### 1. Credit Risk Assessment — **INVESTMENT GRADE (strong)**

CBOE is a **net-cash** company with an undrawn revolver, an "A-" category rating on its senior unsecured notes, and interest coverage near 29x. This is not a credit-risk story at any reasonable horizon.

| Metric | Value (FY2025) | Read |
|---|---|---|
| Total debt | $1,684.7M (FY25); **$1,443.8M at 6/30/26** | Modest, all fixed-rate senior notes |
| Cash & ST investments | $2,252.6M (FY25); **$2,662.6M at 9/30/26** | |
| Net debt | **−$567.9M (net cash)**; ≈ **−$1,218.8M** at 9/30/26 | Net cash, improving |
| Net debt / EBITDA | **−0.33x** | Negative |
| Debt / equity | 0.33x | Low |
| Debt / assets | 0.18x | Low |
| **Interest coverage (EBIT/int.)** | **28.95x** | Very strong |
| Operating margin | 32.1% (FY25) vs 26.8% FY24, 12.4% FY22 | Recovering/expanding |
| Altman Z (book equity) | 2.62 — "grey" | **Misleading; see note** |
| **Altman Z (market-cap X4)** | **≈ 6.9 — safe zone** | Recomputed |
| Piotroski F-Score | **7 / 9** | Moderate-to-strong |

**Z-score caveat:** the tool's X4 uses *book* equity ($5.14B) against $4.17B liabilities (1.23). Substituting market cap ($35.0B) gives X4 ≈ 8.4 and Z ≈ **6.9**, firmly safe. The book-equity score mechanically penalises CBOE for a goodwill-heavy, low-tangible-equity balance sheet — not for solvency.

**Piotroski detail — the two lost points are margin quality, not solvency:** F8 (gross margin fell 50.6% → 48.9%) and F9 (asset turnover fell 0.526 → 0.507, inflated by cash build). All seven profitability/liquidity/leverage tests pass, including declining leverage and no dilution.

**Covenant:** the revolver carries a **maximum consolidated leverage ratio of 3.50x**; management reported compliance and **zero borrowings** at 9/30/26. Breach would require EBITDA to fall to ~$412M — a **~76% decline** from FY25's $1,741M.

**Ratings evidence:** S&P rated CBOE's $500M senior notes **'A-'** (one source, not cross-verified). No CDS spread data available.

---

### 2. Liquidity Risk — **VERY LOW**

| Metric | Value |
|---|---|
| Current ratio | **1.87x** |
| Quick ratio | **1.87x** (no inventory — exchange model) |
| Cash ratio | **0.95x** |
| Working capital | $2,059.1M |
| Cash / total liabilities | 0.54x |
| Equity / assets | 0.55x |

**Refinancing cliff:** the **3.650% Senior Notes due January 2027** were reclassified from long-term to current debt in Q3 2026. This is the only near-term maturity and is trivially covered: $2.66B cash + **$400M undrawn revolver** (+$200M accordion) + **~$300M** expected TMX proceeds from the Australia (closed 7/31/26) and Canada divestitures ≈ **$3.3B+ of liquidity against $1.44B of total debt.**

**Cash runway:** not a meaningful metric here — CBOE is strongly cash-generative with **no burn** (FY25 FCF $1,153M). Liquidity covers ~21x annual interest expense.

---

### 3. Market Risk Profile — **the real risk in this name**

| Metric | 750-day | 252-day |
|---|---|---|
| Annualised volatility | **29.7%** | **40.3%** |
| Beta vs SPY (computed) | **−0.26** | **−0.60** |
| Max drawdown | **−36.7%** | −36.7% |
| Sharpe (rf = 0%) | 0.93 | 0.85 |
| Company-reported 5Y beta | 0.414 | |

**Verified drawdown (raw closes, no split artifacts — adj_close = close throughout):** peak **$364.92 (5/13/26)** → trough **$230.87 (6/29/26) = −36.7%**, on heavy volume (5.0M shares 6/2, 4.2M on 6/17). Two sharp legs: 6/1–6/2 (−9.8%, then −8.4%) and 6/16–6/18 (−13.5%). The stock has since recovered to the profile quote of $335.53, roughly **−8% below the May peak** and **+45% off the June trough**.

**Critical interpretation — do not trust the negative beta.** A −0.26 to −0.60 beta for an exchange operator is not economically credible; it is an artifact of large *idiosyncratic* 2026 moves that covariance math reads as anti-correlation. I explicitly reject the "diversifier / hedging asset" reading. Realized beta (0.41 reported) plus a 37% single-quarter drawdown says this equity behaves like a **high-multiple, sentiment-sensitive growth compounder**, and volatility (40% on 252d) is well above what an "exchange utility" should show.

**Catalyst — partially unidentified (flagged):** my sources did not confirm the specific trigger of the June 2026 selloff; the volume profile indicates a fundamental/competitive news event rather than a technical break. What is documented is **options market-share erosion: 30.0% in Q2 2026 vs 30.2% prior**. This — share loss to competing options venues — is the correct lens on CBOE's market risk: not cyclicality, but **moat/competitive re-rating**, which compresses the multiple far faster than it compresses the earnings.

**Fundamentals re-accelerated afterwards**, confirming the drawdown was multiple compression, not deterioration: Q3 2026 revenue **$1,358.8M (+19.0% y/y)**, net income **$428.2M (+42%)**, diluted EPS **$4.08 (+43%)**; FY26 organic revenue growth guidance in the high teens.

**FCF sustainability:** FY25 FCF **$1,153.1M**, FCF yield **3.27%** on $35.3B market cap. Capex is remarkably light ($71.0M, ~1.5% of revenue). FCF has compounded $748M → $964M → $1,153M across FY23–25.
⚠️ **Cash-flow quality caveat:** FY25 reported operating cash flow was $1,224.1M, yet the Q3-26 10-Q cites **9M 2025 operating cash flow of $1,400.5M** — implying *negative* Q4 2025 OCF. 9M 2026 OCF of $2,273.9M against ~$1.2B of 9M net income shows large working-capital swings from clearing/regulatory balances. **Treat headline OCF/FCF as chunky; net income + D&A is a cleaner economic read.**

---

### 4. Downside Scenario Analysis — Revenue −20%

Modelled on FY25 actuals, assuming cost of revenue (51% of revenue: royalty, regulatory, liquidity, routing/clearing) is ~60% volume-variable, other opex ~10% flex:

| Line | Base FY25 | Revenue −20% | Δ |
|---|---|---|---|
| Revenue | $4,714.2M | $3,771.4M | −20% |
| EBITDA | $1,741.3M | **$1,166.7M** | −33% |
| EBIT / operating income | $1,514.1M | $939.5M | −38% |
| Op. margin | 32.1% | 19.9% | −12.2pt |
| Interest coverage | 28.9x | **≈18.0x** | Still ample |
| Net income | $1,100.0M | ≈$683M | −38% |
| FCF | $1,153.1M | **≈$734M** | −36% |
| FCF yield (on $35.0B) | 3.3% | **≈2.1%** | |
| Net debt | −$1,219M | still net cash | |
| Gross debt / EBITDA | 0.83x | **1.24x** (covenant 3.50x) | Huge headroom |

**Stress-test conclusion: CBOE cannot be covenant-breached or liquidity-stressed by demand alone.** Even at **revenue −40%**, EBITDA falls to ~$592M, leverage only reaches ~2.4x, coverage stays ~9x, and the company remains net cash. Downside in this equity is a **valuation/multiple event (2.1% FCF yield offers no floor)**, not a solvency event.

---

### 5. Overall Financial Risk Rating: **LOW**

Balance-sheet and liquidity risk are near-minimal (net cash, 29x coverage, IG rating, undrawn revolver, no refinancing cliff). The residual risk is **equity-market and franchise/competitive risk**, not credit risk.

### 6. Key Red Flags

1. **Negative computed beta is a false comfort** — 40% realized vol and a −36.7% drawdown contradict the "low-beta exchange utility" narrative. Do not model CBOE as a hedge.
2. **Options market-share erosion (30.0% vs 30.2%)** — competitive/moat risk is the single largest threat to the franchise, and drove the 2026 de-rating.
3. **Goodwill & intangibles = $4.45B, 48% of assets and 87% of book equity** — impairment risk is real and has precedent (FY2022 net income collapsed to $235M on a $490M operating base, Z-score-type metrics deteriorated sharply).
4. **Index-licensing dependence** — SPX/index options economics rest on royalty arrangements with S&P DJI and other index providers; a repricing would hit the highest-margin revenue directly.
5. **Cash-flow quality** — clearing/regulatory balance flows make OCF volatile (implied negative Q4 2025 OCF); FCF overstates distributable cash in some periods.
6. **Valuation risk, not balance-sheet risk** — 3.3% FCF yield (2.1% in downside) means the stock has limited downside protection if growth expectations reset.
7. Minor: $14.0M incremental credit reserve on CATLLC notes receivable — small but signals judgment risk in legacy investments.

### Data Gaps (explicit)
- **Peer benchmarking unavailable:** `get_sector_peers` returned Vanguard index funds/ETFs, not exchange operators (ICE, NDAQ, CME); no relative-multiple context.
- **Price data truncated at 6/30/2026** while the profile quote (~$335.53) is later; vol/beta/Sharpe are computed on a window ending at the drawdown trough, so 252-day volatility (40.3%) is overstated relative to today.
- **No debt maturity ladder** by year (only total debt and the Jan-2027 notes identified); no CDS spreads.
- **SG&A inconsistent:** FY25 shows $91.5M vs FY24 $603.0M — an 85% drop that is almost certainly a data error; FY25 EBIT ($1,618.9M) also exceeds operating income ($1,514.1M) inconsistently. I used operating income throughout.
- **S&P 'A-' rating** sourced from a single search result, not independently verified.
- Specific catalyst for the June 2026 selloff unconfirmed.
