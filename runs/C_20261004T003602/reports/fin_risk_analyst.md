# Fin Risk Analyst

- Symbol: C
- Elapsed: 158.3s

---
All data gathered. I have everything needed — financials, risk metrics, market data, CET1/capital info, and ratings context. Here is the complete risk assessment.

---

# Citigroup Inc. (C) — Financial Risk Assessment
**As of FY2025 (Dec-2025) / market data through Oct-2026**

**Framework caveat (read first):** C is a G-SIB with a **$2.66T balance sheet**, not an industrial company. Several off-the-shelf metrics in this stack (Altman Z-Score, interest coverage, current ratio, FCF yield) are **designed for manufacturing firms and are structurally meaningless when applied to a bank**. I report them for completeness but flag them as artifacts; the true credit story is told by capital ratios, liquidity, funding, and ratings.

---

## 1. Credit Risk Assessment: **INVESTMENT GRADE** (A-range / stable-to-positive)

| Signal | Reading |
|---|---|
| Credit rating (external) | Fitch **A / F1** (affirmed, outlook positive per Fitch); Moody's ~**A3**; S&P ~**BBB+** — solid low- to mid-single-A IG, typical for a G-SIB |
| CET1 ratio | **~13.4–13.6%** (2025) vs 4.5% regulatory minimum + buffers — strong capital cushion, passed CCAR 2024/2025 |
| GAAP ROE | 6.7% ($14.3B NI / $213.8B equity) — **below cost of equity (~10–11%)**; profitability is the weakest pillar |
| Tangible common equity / assets | ~7.2% — well capitalized for a peer bank |
| Regulatory status | Subject to Fed/CFPB consent orders (2020 risk-management order; 2024 CFPB fine); transformation/remediation still ongoing — an execution and supervisory overhang, not a solvency issue |

**Solvency conclusion:** No distressed-debt dynamic. $16–17B of net income plus a 13.4% CET1 buffer can absorb a severe recession without breaching minimums. The credit risk is *earnings and capital-return* risk, not default risk.

---

## 2. Key Financial Risk Metrics (FY2025)

| Metric | Value | Verdict |
|---|---|---|
| **Leverage** | | |
| Debt / equity | 3.35x | Bank-normal (assets/equity 12.4x) |
| Net debt / EBITDA | 1.67x | Not meaningful for banks (uses EBITDA) |
| Assets / equity | 12.4x | High absolute leverage — inherent to G-SIB model, regulated via capital rules |
| Short-term debt | **$400.0B** of $715.8B total debt | Heavy reliance on short-term wholesale funding = refinancing/renewal risk in stress |
| **Coverage** | | |
| Interest coverage (EBIT / int. exp.) | 0.24x | **Artifact** — interest expense is $83.1B of funding cost, not a serviced obligation; ignore |
| **Liquidity** | | |
| Cash & ST investments | **$675.4B (25% of assets)** | Massive liquidity stockpile — supports LCR compliance |
| Current ratio / quick ratio | 0.48x | **Artifact** — deposits are "current liabilities"; not a measure of bank liquidity |
| Cash / total liabilities | 0.28 | Strong absolute liquidity buffer |
| **Bankruptcy scores** | | |
| Altman Z-Score | **−0.10 (flag: "Distress")** | **Invalid for banks** (x4 uses book equity, x5 asset-turnover logic breaks); do not use |
| Piotroski F-Score | **4/9 (flag: "Weak")** | Penalized by negative OCF and rising leverage — both normal for a growing bank balance sheet; partial credit. Not a reliable strength read here |
| **Profitability** | | |
| Net income trend | $14.8B (22) → $9.2B (23) → $12.7B (24) → **$14.3B (25)** | Recovering; 2025 best year since 2022 |
| ROA | 0.54% | Modest |
| Capital return | $5.4B div + **$18.3B buybacks = $23.6B vs $14.3B NI (165% payout)** | Returns exceed earnings — funded by excess capital; sustainable only while CET1 stays above target |

---

## 3. Market Risk Profile (3-yr window, vs SPY)

| Metric | Value | Implication |
|---|---|---|
| Annualised volatility | **30.6%** | High — top-decile for large caps; C is a high-beta, high-tail-risk equity |
| Beta vs S&P 500 | **1.28** | ~28% more market sensitivity than the index |
| Max drawdown (window) | **−31.3%** | Realized in the April-2025 tariff shock: C fell ~$78 → ~$53.6 in days (realized tail beta >2) |
| Sharpe ratio (0% rf) | ~1.45 | Good *average* reward-per-risk over the window, driven by the 2025–26 rally — but this masks fat left tails |
| Price context | ~$40 (Jan-23) → $147 peak (Jun-26) → **~$128 now** | Off ~13% from recent high in Sep–Oct 2026 pullback |

**Tail-risk note:** In a 30% market drawdown, a beta of 1.28 implies C falls ~**38–40%**, and its April-2025 behavior shows it can overshoot that in a flight-to-safety. Equity holders bear meaningful downside; bondholders are insulated by the capital buffer.

---

## 4. Downside Scenario Analysis — Revenue −20% (Severe Recession)

Stress applied to FY2025 actuals; illustrative CCAR-style shock:

| Line item ($B) | FY2025 base | −20% revenue stress |
|---|---|---|
| Revenue | 168.3 | 134.6 |
| Non-interest expense (opex −5% assumed) | (148.5) | (141.1) |
| **Pre-provision net revenue** | **+19.8** | **−6.5** |
| Credit loss provisions (doubled) | (~12) | (~24) |
| **Pre-tax income** | ~+8 | **~−30** |
| **After-tax net income** | **+14.3** | **~−20** |
| ROE | 6.7% | ~−9% |
| CET1 (est., ~$1.05T RWA) | 13.4% | ~11.3–11.8% after ~−160bps hit |
| Capital return | $23.6B | **Suspended** (dividends cut per stress practice) |

**Result:** An earnings collapse and suspended capital return, but **CET1 remains ~1.5–2pp above the well-capitalized minimum.** C survives the downturn as a going concern — consistent with its passing CCAR severely-adverse tests. Equity would reprice down ~30–45% (per realized tail behavior). This is a *shareholder-loss* scenario, **not** a credit-default scenario.

---

## 5. Overall Financial Risk Rating: **MODERATE**

| Dimension | Rating | Logic |
|---|---|---|
| Credit / solvency | **Low risk** | 13.4% CET1, IG rating, $675B liquidity |
| Liquidity / funding | **Moderate** | Huge cash, but $400B short-term funding renewal exposure |
| Market (equity) risk | **High** | Beta 1.28, 30.6% vol, −31% realized drawdown |
| Profitability / franchise | **Moderate–High** | ROE 6.7% below cost of equity; transformation/regulatory overhang |

Net: **Moderate.** The credit is investment grade and recession-resilient; the *equity* is a high-volatility instrument with subpar structural profitability. This is not a balance-sheet-distress story — headline tools that say so (Z-score, negative FCF, Piotroski 4) are misapplied to a bank.

---

## 6. Key Red Flags

1. **Headline scorecard misreads (data-quality flags):** Z-Score "distress" (−0.10), Piotroski 4/9, negative FCF (−$74B) and interest coverage 0.24x are **industrial-framework artifacts**. These are not evidence of distress and must not be quoted as such in the memo — the tools do not model banks.
2. **ROE (6.7%) below cost of equity** — the franchise earns less than its capital cost; sustained underperformance keeps the stock cheap (P/B ~1.1x) and limits internal capital generation.
3. **Capital return > earnings (165% payout in 2025)** — buybacks of $18.3B exceed net income; fine while CET1 is fat, but it is the first item cut in a downturn.
4. **Short-term funding concentration** — $400B of debt matures/renews within a year; relies on continuously open wholesale markets.
5. **High market beta & tail risk** — beta 1.28, −31% max drawdown; a 20–30% market selloff implies ~40% equity downside for C.
6. **Regulatory/transformation overhang** — outstanding consent orders, ongoing remediation spend, G-SIB surcharge; supervisory findings can cap capital return at any time.
7. **Rate-cut sensitivity** — $675B in cash/investments means NII is exposed to Fed easing; a steeper, faster cut cycle compresses the single biggest income line.

**Data gaps:** Sector-peers tool returned funds (no bank comparables — peer leverage/ROE benchmarking unavailable); FMP lacks CET1, LCR, NIM, provision, and debt-maturity-schedule fields — those figures come from web sources (CET1 ~13.4%) and are approximate; exact current Moody's/S&P ratings unverified in this session (Fitch A/F1 confirmed). Nothing above changes the Moderate conclusion.

---

**Bottom line for the investment memo:** Lend to C and you're buying an A-rated, heavily regulated, extremely liquid G-SIB — credit risk is low and recession-survivable. Buy the *equity* and you're buying a 1.3-beta, 30%-vol instrument earning below its cost of capital with a 165% payout ratio. Risk rating: **Moderate**, tilted by market risk and weak profitability, not by solvency.
