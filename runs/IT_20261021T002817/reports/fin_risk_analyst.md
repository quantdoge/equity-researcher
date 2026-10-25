# Fin Risk Analyst

- Symbol: IT
- Elapsed: 143.5s

---
# GARTNER, INC. (NYSE: IT) — FINANCIAL RISK ASSESSMENT

**Sector:** Technology / IT Services · **Market cap:** $13.87B (price $219.63) · **Latest data:** Q2 FY2026 (filed 2026-08-04)

---

## 1. Credit Risk Assessment

**Rating: INVESTMENT GRADE (lower tier) — metrics-implied BBB-/Baa3 equivalent. Formal agency ratings unavailable from tools (data gap).**

The balance sheet is *not* the problem. Leverage is low, coverage is strong, and there is no near-term maturity wall in the retrieved data (short-term debt = $0 at 30-Jun-2026). The anomaly is book equity: **shareholders' equity is now NEGATIVE (-$167M)** after $1.99B of FY2025 buybacks and $1.08B in H1 FY2026, which makes standard leverage ratios (D/E 11.3x FY2025) and the book-equity-based Altman Z meaningless as distress signals. This is a capital-allocation artifact, not insolvency — but it removes the equity cushion entirely.

| Credit metric | Value | Read |
|---|---|---|
| Net debt / EBITDA | **1.54x** (FY25, tool) / **1.14x** (net debt $1,490.6M ÷ TTM EBITDA $1,303.8M) | Strong |
| Gross debt / EBITDA | 2.29x (debt $2,979.3M) | Comfortable |
| Interest coverage (EBIT/int.) | **9.15x** FY25; **~14.2x** TTM (EBIT $1,114.3M / int. $78.7M) | Improving — debt prepaid in H1 FY26 |
| Debt / assets | 0.45 (FY25 tool); 41.4% latest quarter | Moderate |
| Equity / assets | **0.04 → negative** | Red flag (buyback-driven) |

**Note on data inconsistency:** annual FY2025 total debt is reported as $3,617.9M vs $3,348.0M in the quarterly series (net debt $1,895.6M vs $1,625.4M) — likely lease treatment. I use the more conservative annual figure for ratios and the quarterly figure for the stress test; direction is unaffected.

---

## 2. Key Financial Risk Metrics

| Metric | FY2022 | FY2023 | FY2024 | FY2025 | Latest (Q2 FY26 / TTM) |
|---|---|---|---|---|---|
| Revenue ($M) | 5,475.8 | 5,907.0 | 6,267.4 | 6,497.3 | 6,463.6 TTM (-0.6% yoy in Q2) |
| Gross margin | 69.1% | 67.8% | 67.7% | 67.7% | 68.9% |
| Operating margin | 20.1% | 20.9% | 18.5% | **15.8%** | 17.2% |
| EBITDA ($M) | 1,345.3 | 1,471.0 | 1,720.7* | 1,229.0 | 1,303.8 |
| FCF ($M) | 993.4 | 1,052.6 | 1,383.2 | 1,175.2 | ~1,250–1,300 (est.) |
| FCF margin | 18.1% | 17.8% | 22.1% | 18.1% | ~19–20% |
| Current / quick ratio | — | — | — | 1.00 / 1.00 | **0.88 / 0.88** |
| Cash / current liabilities | — | — | — | 0.22 | 0.41 |
| Working capital ($M) | — | — | — | -5.6 | **-439** |
| Total debt ($M) | — | 3,070 | 2,900 | 3,618 | 2,979 |
| Equity ($M) | — | 681 | 1,359 | 320 | **-167** |
| **Altman Z** | — | — | — | **2.41 (Grey)** | ~3.5 market-cap adjusted |
| **Piotroski F** | — | — | — | **5 / 9 (Moderate)** | — |
| FCF yield | — | — | — | 7.4% (tool, stale mcap) | **~9%** on $13.87B |

\*FY2024 EBITDA/EBIT fields include ~$362M of non-operating income (EBIT $1,518M vs operating income $1,156M, and net income > operating income) — FY2024 profitability is flattered; do not use it as the comparison base.

**Altman Z detail (2.41, Grey):** driven down almost entirely by x4 = 0.041 (book equity/liabilities) and x1 = -0.0007 (negative working capital). Substituting market equity ($13.87B / $7.77B liabilities = 1.79) lifts the score to **~3.46 — safe zone**. Treat Z = 2.41 as a mechanical artifact.

**Piotroski F = 5:** positives — positive ROA, positive operating cash flow, accrual quality (OCF > net income), **no dilution** (share count 72.0M → 66.5M), asset-turnover improvement. Negatives — ROA deteriorated, leverage rose, equity change negative (buybacks), gross margin declined.

---

## 3. Market Risk Profile

| Metric | 3-year | 1-year |
|---|---|---|
| Annualised volatility | **42.5%** | **55.7%** |
| Beta vs SPY | 0.84 | **0.43** |
| Max drawdown | **-77.2%** | -52.4% |
| Sharpe (rf = 0%) | -0.15 | -0.01 |
| Sortino | **Not available (data gap)** | — |

Price path confirms the tool: peak ≈ **$607** → trough **$138.35** (52-week low) → **$219.63** now (+59% off the low, -64% from the peak). A single-day -22.8% move has occurred in this window.

**Interpretation:** volatility of 42–56% is 3–4x what a subscription-research compounder should exhibit, and the **falling beta (0.98 profile → 0.84 → 0.43)** is diagnostic: the drawdown was *idiosyncratic*, not market-driven. This is a narrative/AI-disruption repricing, not a beta event. Practical implication: conventional market beta understates IT's risk; downside participation comes from company-specific sentiment shocks, and diversification benefit is illusory in a growth scare.

---

## 4. Downside Scenario Analysis (revenue -20%, TTM base)

Base TTM: revenue $6,463.6M, gross margin 68.9%, SGA $3,053.4M (47.2%), D&A $189M, other opex ~$96M, EBIT $1,114.3M, interest ~$85M annualised.

| Scenario (rev. -20% = -$1,293M) | EBIT | EBITDA | Int. cover | Net debt/EBITDA | FCF |
|---|---|---|---|---|---|
| **A. Managed (10% SGA cut)** | $530M (10.2% margin) | $719M | **6.2x** | **2.1x** | ~$455M |
| **B. No cost action** | $224M (4.3% margin) | $413M | **2.6x** | **3.6x** | ~$210M |
| **C. Severe (-35% rev., no cuts)** | **-$444M** | -$255M | Negative | n/m | ~-$250M burn |

**Findings:**
- A 20% revenue shock is **survivable without covenant or liquidity stress** in both A and B. Net leverage would rise to 2.1–3.6x from 1.14x — still inside typical 3.5–4.0x maintenance covenants.
- The **binding constraint is not solvency but the buyback**: at $1.0–1.1B/yr of repurchases against FCF of $1.19B, any revenue decline forces an immediate suspension of the program — which removes the only EPS-growth engine (share count -7.6% yoy), turning a 20% revenue decline into a ~20%+ EPS decline.
- Real tail risk is scenario C, where cash burn of ~$250M/yr meets $2.98B of debt. With $1.49B cash, that's ~6 years of liquidity, but the debt becomes unrefinanceable. This requires a *sustained* contract-value contraction, not a cyclical dip — the probability is low but non-zero and is precisely what the market is pricing.
- **Structural buffer:** Insight/research revenue is ~100% subscription-based with contract value of $5.28B (+1.7% yoy, +0.3% qoq in Q2 FY26 — re-accelerating off the 0.8% Q4 FY25 trough). A -20% revenue year would require mass non-renewal, which is a step-change, not a normal-cycle outcome. Large deferred revenue in current liabilities also means the sub-1.0 current ratio overstates liquidity risk (obligations are settled with service, not cash).

---

## 5. Overall Financial Risk Rating: **MODERATE**

**Justification:** Low net leverage (1.1–1.5x), 9–14x interest coverage, ~$1.3B FCF (~9% yield), no debt maturing within 12 months in the available data, and highly recurring revenue argue for Low. Offsetting: revenue has stalled (-0.6% yoy in Q2 FY26), operating margin fell 270bp in FY2025 (15.8% vs 18.5%), book equity is negative, distributions are running ahead of cash generation, and the equity has traded with 56% volatility and a 77% drawdown. Net: **Moderate financial risk, with high equity/valuation risk.** Credit risk and equity risk are decoupled here — the bonds are fine; the stock is not.

---

## 6. Key Red Flags

1. **Negative shareholders' equity (-$167M) and D/E of 11.3x** (FY2025) — zero book cushion; all future buybacks must be debt- or cash-funded. Watch for a leverage-target policy change or buyback pause as the real credit event signal.
2. **Distribution > cash generation:** $3.07B of buybacks over 18 months vs ~$1.93B of FCF ($1.99B FY2025 alone; $1.08B in H1 FY2026 vs $749M FCF — a $333M shortfall funded off the balance sheet).
3. **Revenue stagnation / margin compression:** FY2025 revenue +3.7% but operating income -11.3%; Q2 FY2026 revenue -0.6% yoy. Contract value growth of 1.7% is stabilization, not health — below the ~5%+ needed to support the historical multiple.
4. **Q3 FY2025 operating income collapse** to $86M from ~$330M run-rate (restructuring/charge) — confirm this recurs at lower magnitude; it distorted FY2025 comparisons.
5. **Working capital negative (-$439M), current ratio 0.88** — manageable given deferred-revenue mechanics, but it leaves no headroom if billings slow.
6. **Volatility/idiosyncratic repricing risk:** 55.7% 1-yr vol, -77% max drawdown, single-day -22.8% move, 1-yr beta 0.43. Risk is event-driven, not market-driven.

## Data Gaps (explicitly flagged)
- **Debt maturity schedule and covenant terms** — not retrievable from tools; "no near-term maturity wall" rests on short-term debt = $0, which is a proxy, not a schedule.
- **Formal credit ratings / CDS spreads** — web search returned no Gartner-specific rating action; the IG characterization is metrics-based inference only.
- **Sortino ratio** — unavailable.
- **Q1/Q2 FY2025 quarterly cash flow** — not retrieved, so TTM FCF (~$1.25–1.30B) is an estimate; FCF yield range 8.5–9.4%.
- **Annual vs quarterly debt discrepancy** ($3.62B vs $3.35B at FY2025) — reconciliation unresolved (likely lease inclusion).
- **Peer benchmark multiples** — not gathered (budget); no relative leverage context.
