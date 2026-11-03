# Fin Risk Analyst

- Symbol: VG
- Elapsed: 58.4s

---
# VENTURE GLOBAL, INC. (VG) — COMPLETE FINANCIAL RISK ASSESSMENT

**Data vintage note (important):** Financials are available through **Q2 2026** (filed 2026-08-11); price data ends **2026-03-10** ($11.34). Risk metrics labeled "LTM" use Q3'25–Q2'26. The ratio tools computed off FY2025 (12/31/25); I show both where they diverge materially.

---

## 1. Credit Risk Assessment

**Rating: SUB-INVESTMENT GRADE (BB-/Ba3-equivalent), Negative Outlook**

| Evidence | Reading |
|---|---|
| S&P issuer credit rating, Venture Global LNG, Inc. | **BB-**, negative outlook |
| S&P project rating, Calcasieu Pass | **BBB-** (upgraded from BB+ in 2025) |
| Fitch | Rates senior secured notes (8.125% / 8.375% coupons — classic high-yield pricing) |

The company sits **one to two notches below investment grade at the corporate level**, with a *negative* outlook — direction of travel is wrong. Only the ring-fenced, operating Calcasieu project has achieved IG. The consolidated credit is structurally a **project-finance stack bolted onto a sub-IG corporate holdco**, and that matters enormously: the holdco does not freely own the project cash flows.

**Leverage has roughly doubled in 30 months and is still climbing:**

| | FY2023 | FY2024 | FY2025 | Q1'26 | Q2'26 |
|---|---|---|---|---|---|
| Total debt ($bn) | 21.17 | 29.81 | 34.90 | 37.59 | **42.81** |
| Net debt ($bn) | 16.35 | 26.20 | 32.55 | 35.66 | **39.62** |
| Book equity ($bn) | 2.09 | 6.37 | 10.30 | 12.35 | 12.08 |

Debt rose **$7.9bn in H1 2026 alone**. Equity fell $0.3bn in Q2'26 despite $1.4bn of net income — a red flag on other comprehensive/equity movements I cannot decompose from the tools.

**Interest coverage is adequate but thin and deteriorating at the margin.** LTM EBIT $6,325m / LTM interest $1,801m = **3.51x** (FY2025: 3.46x). EBITDA/interest 4.05x. Critically, average cash interest of 4.2% on $42.8bn of debt is *implausibly low* — a material share of interest is being **capitalised into PP&E during construction** (PP&E $53.9bn). True run-rate interest burden post-completion will be materially higher than the reported $1.8bn. **This is the single most under-appreciated credit fact in the numbers.**

---

## 2. Key Financial Risk Metrics

| Metric | LTM (Q2'26) | FY2025 (tool) | Threshold / Read |
|---|---|---|---|
| Debt / Equity | **3.54x** | 3.39x | Very high |
| Debt / Assets | **69.6%** | 65.0% | Very high |
| Net Debt / EBITDA | **5.43x** | 5.65x | Sub-IG territory (>4.0x) |
| Gross Debt / EBITDA | 5.87x | — | — |
| Interest coverage (EBIT/int.) | **3.51x** | 3.46x | Adequate, low headroom |
| Current ratio | **1.19x** | 0.93x | Weak / borderline |
| Quick ratio | ~1.11x | 0.87x | Weak |
| Cash / current liabilities | 0.83x | 0.54x | Thin |
| Working capital | **+$708m** | −$304m | Improved, thin |
| Equity / Assets | **19.6%** | 19.0% | Thin cushion |
| **Altman Z-Score** | — | **0.82 (Distress)** | <1.81 = distress zone |
| **Piotroski F-Score** | — | **7 / 9** | Moderate/strong |
| **FCF yield** | ~**−20%** | **−20.1%** | Severe cash burn |
| Operating margin | 36.6% | 36.6% | Genuinely strong |

**On the Altman Z of 0.82:** mechanically correct but structurally misleading — x4 uses *book* equity ($12.1bn) rather than market cap ($32.2bn). Re-running with market cap (x4 ≈ 0.65) lifts Z to only **~0.99 — still deep in the distress zone**. The Z-score penalises VG for being a pre-completion, project-financed asset base with thin retained earnings, which is by design, not by accident. But two components are *not* artefacts: debt/assets of 70% and a 0.26x asset-turnover ratio. Directionally, the signal is real.

**On the Piotroski F of 7:** treat with scepticism. The two failures — no dilution (F7=0, share count 2.426bn → 2.489bn) and gross margin improvement (F8=0) — are correct and meaningful. But F4 (accruals quality) and F9 (asset turnover) are flattered by the FY2024→FY2025 revenue jump from $4.97bn to $13.77bn, which reflects **Plaquemines train start-ups and commissioning-cargo sales**, not organic efficiency. The F-score's year-over-year machinery does not model a company in a multi-year build-out.

---

## 3. Market Risk Profile

| Metric | Value | Assessment |
|---|---|---|
| Annualised volatility (252d) | **76.7%** | Extreme — ~4–5x the market |
| Beta vs SPY (tool) | **−1.98** | **Not usable** |
| Beta (company profile) | 0.223 | Conflicts with above |
| Max drawdown (tool) | 39.98% | **Understated — see below** |
| Max drawdown (my calc, close-to-close) | **−75.2%** | $23.71 (1/24/25) → $5.89 (12/16/25) |
| Intraday peak-to-trough | **−77.4%** | $25.19 → $5.69 |
| Sharpe (tool, rf=0%) | 0.92 | Window-dependent, low confidence |
| Price vs IPO ($23.71) | $11.34 → **−52%** | — |

**Beta is a data gap, not a finding.** VG listed 2025-01-24, giving ~14 months of history; the −1.98 and 0.223 are two different windows of an unstable estimate. Neither should enter a cost of equity. The economically correct read: VG's revenue is substantially locked into long-term SPAs (largely take-or-pay, oil/JKM-linked), so *fundamental* cash-flow beta to equity markets is low — but the *equity* trades on project-execution and litigation news, giving it enormous idiosyncratic risk. **Do not model VG as low-beta on the strength of the 0.223 figure.**

**The drawdown figure matters.** The tool's 39.98% is inconsistent with the price series I pulled; the actual peak-to-trough loss from the IPO print is **−75%**. A stock that loses three-quarters of its value in eleven months and then triples off the low (from $5.89 to $12.41) is a **binary-outcome instrument**, not a compounder.

**Event risk is the dominant price driver, not macro:**
- **10 Oct 2025: −25% in one session** (12.48 → 9.37) on BP's arbitration win.
- **2 Mar 2026: +18%** (9.64 → 11.32) on earnings/FID news, on 46m shares.
- Realised vol is litigation-driven and will remain so.

---

## 4. Downside Scenario Analysis

**Base (LTM Q2'26):** Revenue $16,951m; EBITDA $7,294m (43.0%); EBIT $6,325m; interest $1,801m; net debt $39.62bn.

**Key transmission mechanism:** LNG revenue is a spread business — revenue minus gas feedstock. A price-led revenue decline does **not** cut feedstock cost proportionally (liquefaction is fixed-cost), so EBITDA is more levered to price than a 43% margin implies. I run two margin assumptions: a *contracted* case (≈55% incremental margin, sales protected by take-or-pay) and a *spot-exposed* case (≈100%, i.e. a pure realised-price cut with no cost offset).

| Scenario | Revenue | EBITDA | EBIT | Coverage | ND/EBITDA |
|---|---|---|---|---|---|
| Base LTM | 16,951 | 7,294 | 6,325 | **3.51x** | **5.43x** |
| **A. Rev −20%, contracted (55% margin)** | 13,561 | 5,429 | 4,460 | **2.48x** | **7.30x** |
| **B. Rev −20%, spot-exposed (100%)** | 13,561 | 3,904 | 2,935 | **1.63x** | **10.15x** |
| **C. Rev −20% + feedstock +15% (+$1.33bn)** | 13,561 | 4,103 | 3,172 | **1.76x** | **9.66x** |
| **D. Severe: Rev −35%, spot, +$1.5bn arbitration award, +200bp on 25% floating (+$214m int.)** | 11,018 | ~2,200 | ~1,290 | **~0.64x** | **~18x** |

**Read-through:**
- In **Scenario A**, leverage breaches 7x and coverage falls below 2.5x. Any corporate maintenance covenant set at 4.0–5.0x net debt/EBITDA (typical for BB- issuers) would be **tested or breached**. I do not have the covenant schedule — see gaps.
- In **Scenario B/C**, coverage at 1.6–1.8x is below the **~2.0x** level at which high-yield energy issuers routinely lose market access. Equity at 12x+ leverage is likely wiped.
- **Scenario D is the tail that matters**: it is not hypothetical, it is the combination of a repeat of the FY2023→FY2024 commissioning-revenue reversal (revenue fell 37% that year) *plus* the pending arbitration quantum.

**Contingent liability — the real downside driver.** Arbitration outcomes to date: **VG won vs Shell**, but **lost vs BP** (liability found; BP seeking **>$1bn**, quantum hearing 2026) and **lost vs Galp** (damages capped ~$170m, hearing 2027–28). Reuters reports **pending disputes could total ~$4.8bn** in damages — equivalent to **15% of market cap and ~11% of book equity**. I could not verify whether any of this is provisioned. **Unfunded, this is a direct equity impairment and potentially a covenant event.**

**Liquidity / refinancing:** Cash $3.19bn against H1'26 FCF of **−$6.48bn** ($3.24bn/quarter burn) implies **cash runway of roughly one quarter** absent capital markets. This is *not* imminent insolvency — the burn is discretionary growth capex (CP2 Phase 2 FID March 2026, **$8.6bn project financing; $20.7bn total CP2**; Plaquemines Ph2 COD mid-2027), funded by construction debt ($9.4bn raised in H1'26). The correct interpretation: **VG has ~1 quarter of self-sufficiency and is therefore structurally dependent on continuous access to project-finance markets for at least another 12–18 months.** A widening of high-yield spreads or an arbitration-driven loss of confidence is a genuine existential pathway, not a theoretical one. Short-term debt of only $345m means **no near-term maturity cliff** — the risk is *access*, not *maturity*.

Also note: **$465m of dividends paid in FY2025 and ~$0.27bn in H1'26 while burning $6.5bn of FCF.** Small in absolute terms (1.4% yield), but paying cash out while funding construction with debt is a capital-allocation signal worth flagging.

---

## 5. Overall Financial Risk Rating

# **HIGH**

Justification: sub-investment-grade corporate credit with a *negative* outlook, net leverage of 5.4x and rising, negative FCF of ~$8–13bn annualised, cash equal to ~1 quarter of burn, ~$4.8bn of live arbitration exposure, 77% annualised volatility and a −75% drawdown since IPO. **Not Critical** — the business generates $7.3bn of LTM EBITDA at 43% margins, interest coverage is 3.5x, Calcasieu holds an IG project rating, near-term maturities are de minimis, and long-term SPAs underwrite the asset base. **Not Moderate** — because the downside scenarios land squarely on covenant and equity-impairment territory, and the company cannot self-fund.

---

## 6. Key Red Flags

1. **Leverage compounding fast:** net debt $16.4bn → $39.6bn in 10 quarters (+142%). ND/EBITDA 5.4x and *mechanically rising* until CP2 completes (2027+).
2. **Capitalised interest masks the true coverage ratio.** Reported 3.5x coverage uses a $1.8bn interest figure that is understated relative to post-completion economics.
3. **One quarter of cash runway.** $3.19bn cash vs $3.24bn/quarter burn — wholly reliant on project-finance markets staying open for 12–18 months.
4. **$4.8bn of unquantified arbitration exposure** (BP >$1bn sought, Galp ~$170m, others pending; VG lost two of three liability findings). Provisioning status unverified.
5. **Altman Z 0.82 — distress zone** even after correcting for the book-equity distortion (~0.99). Driven by 70% debt/assets and 0.26x asset turnover.
6. **Zero free cash flow, negative for four straight years:** $−3.5bn (2023), $−11.6bn (2024), $−6.8bn (2025), $−6.5bn (H1'26). FCF yield −20%.
7. **Earnings quality is poor and lumpy:** gross margin 66.4% (FY24) → 49.3% (FY25) → **35.0% (Q1'26)** → 57.3% (Q2'26). Revenue recognition on commissioning cargoes makes reported results nearly unforecastable year to year.
8. **Dividends paid out of borrowed money** during peak construction ($465m FY25, ~$270m H1'26).
9. **Dilution:** share count 2.426bn → 2.489bn, Piotroski F7 = 0; IPO priced at $23.71, stock −52% since.
10. **−25% single-day drawdown on litigation news (10 Oct 2025)** — the equity is priced as a litigation/project-execution option, not a cash-flow stream.

---

## Data Gaps (explicitly flagged)

- **Covenant levels and full debt maturity schedule not available** from these tools. The scenario analysis infers breach risk from typical BB- thresholds; actual maintenance covenants, DSCR tests, and restricted-payment baskets require the 10-K/10-Q.
- **Beta is unreliable** — only ~14 months of trading history and two mutually contradictory figures (−1.98 vs 0.223). Excluded from conclusions.
- **Tool-reported max drawdown (39.98%) contradicts the price series (−75.2%).** I used my own computation.
- **Capitalised vs expensed interest not separable** — coverage ratio likely flatters reality.
- **No CDS spread data available** — a direct market read on default probability is missing.
- **Arbitration provisioning not verifiable** — $4.8bn exposure may be entirely off the recorded balance sheet.
- **Peer comparison failed:** the sector tool returned integrated majors (XOM, CVX, SHEL, TTE, COP, PBR), which are not meaningful comparables for a pre-completion LNG developer. Cheniere (LNG) and NextDecade (NEXT) would be the correct set; I did not have tool support to retrieve them within budget.
- **Metric asynchrony:** price data ends 2026-03-10; financials run to 2026-06-30. Market-based ratios (FCF yield uses market cap $33.9bn vs current $32.2bn) mix vintages.
