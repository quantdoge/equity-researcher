# Quant Analyst

- Symbol: TEAM
- Elapsed: 46.6s

---
## TEAM (Atlassian Corp.) — Quantitative Factor Report
**Price $153.68 | Mkt cap ~$40.0B | EV ~$40.0B | 260.2M sh | FY26 rev $6.57B | Data as of Nov 6, 2026 close**

---

### 1. Factor Scores Table

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | 17/100 | **6th of 7** (bottom quintile) | **Strong Negative** — EV/EBITDA 188.4x, P/FCF 30.3x, P/B 37.8x, P/E n/a (negative) |
| **Momentum** | 100/100 *(stale)* → **55/100 recomputed** | 1st of 7 on 12–1 | **Positive but decayed / reversal underway** |
| **Quality** | 50/100 | 4th of 7 | **Neutral — split** (best GP/assets 0.91 & accruals, worst ROE −5.1%) |
| **Low Vol** | 5/100 | **7th of 7** (worst) | **Strong Negative** — 87.6% ann. vol, 51.6% max DD |
| **Earnings Revision** | 30/100 | ~5th of 7 | **Negative forward** — growth guide cut; PTs stale-positive |

**Peer set (n=7 SaaS comps, ranks 1 = best):** TEAM, CRM, NOW, WDAY, HUBS, DDOG, ADBE. *Note: the platform's "Technology" sector list is dominated by mega-cap semis/hardware (NVDA, TSM, AVGO) — not valid comparables. n=7 is small; ranks are ordinal and lack statistical power.*

**Detail behind the ranks**
- **Value:** EV/EBITDA 10.4x (ADBE), 16.1x (CRM), 34.3x (NOW), 36.3x (WDAY), 44.7x (HUBS), **188.4x (TEAM)**, 320.6x (DDOG). P/FCF: 10.4x, 14.2x, 15.1x, 18.3x, 23.3x, **30.3x (TEAM)**, 65.0x. TEAM is 6th on both. Only DDOG is more expensive.
- **Momentum:** tool returns **+110.75%** (12–1, ex-last-21d). CRM +27.0, NOW +28.0, WDAY +18.0, DDOG +9.2, HUBS −2.1, ADBE −2.3.
- **Quality:** GP/assets **0.9135 = 1st** (ADBE 0.719, HUBS 0.681); accruals **−0.2305 = 1st (lowest)**; ROE **−5.09% = 7th**; ROIC 0.45% (still far below WACC).
- **Low Vol:** vol 87.6% (worst vs HUBS 79.1, DDOG 76.1, NOW 69.7, WDAY 58.7, CRM 50.7, ADBE 44.7); max DD 51.6% (worst); beta 0.757 (2nd highest after DDOG).

---

### 2. Price Statistics

| Metric | Value |
|---|---|
| Alpha (annualised, vs SPY) | **+62.4%** — t ≈ **11.4** (highly significant in-sample) |
| Beta (vs SPY, 252d) | **0.761** — **t ≈ 1.96, only marginally significant**; 95% CI ≈ **[0.0, 1.5]** |
| R² | **0.0152 (1.5%)** — benchmark explains almost none of TEAM's variance |
| Annualised volatility | **87.61%** (peer median ≈ 69.7%) |
| Annualised return (252d) | +105.91% |
| Sharpe (0% rf) | **1.206** (1.16 at 4% rf) — best in peer set (CRM 0.28, NOW 0.11, WDAY 0.49, DDOG 0.93, HUBS −0.15, ADBE −0.37) |
| Sortino (0% rf) | **2.59** — implies downside deviation ≈ 40.9% vs 87.8% total → heavily **right-skewed** |
| Max drawdown | **−51.64%** (tool, 252d window); independently measured: **−66%** Dec-25 $165 → Apr-10-26 **$56.01** low; then −32.5% from Oct-23-26 high **$227.61** to $153.68 |

**Read-through:** The 2.15× Sortino/Sharpe ratio is *not* evidence of durable risk-adjusted skill. It is the arithmetic of a violent V-shaped recovery (Apr-2026 $56 → Oct-2026 $228, +298%) punctuated by two ~16–35% single-day gap events (Aug 7: $110→$149, +35%; Nov 6: −16% on 2.5× volume). The fat left tail has not yet been sampled symmetrically in this window.

---

### 3. Composite Quant Signal: **NEUTRAL** (leaning cautious)
Equal-weighting (17, 55, 50, 5, 30) = **31/100 — Neutral-to-Sell band**. Using the stale tool momentum (100) yields 40/100 — still Neutral. *Positive* momentum/alpha and P/FCF-supportive cash generation are offset by bottom-quintile value, worst-in-class volatility, and a forward revision regime that just turned negative.

**Important context on the Nov 6 catalyst (verified):** Q1 FY27 *beat* — rev +24% to $1.772B, cloud +31% to $1.30B, adj. EPS $1.65 vs $1.43 est. Stock still fell **16.2%** because FY27 revenue growth was guided to **~13.75%** (vs 24% delivered) and Data Center revenue is guided **−16%**. Class is classic beat-and-derate on deceleration. This is a *valuation-compression* event (multiple reset), not a fundamentals break.

---

### 4. Key Quant Risk Flags

1. **Momentum reversal risk — HIGH (the headline flag).** The +110.75% momentum print **excludes the last 21 trading days**, so it does not contain the −32.5% collapse from the Oct 23 high. Recomputing from verified closes: 12-month return **−1.6%**, 3-month **+39.5%**, but 1-month **−20.8%**. The factor is decaying fast and TEAM is a prime short-term-reversal candidate. Do not size off the 100/100 score.
2. **Earnings-revision data artifact — the tool's −100% is NOT valid.** `calculate_earnings_revision_score` compared FY2031 (EPS estimate $0.00, 4 analysts) against FY2030 ($8.99), producing a mechanical −100%. FY2031 EPS is simply not covered. **Override:** *revenue* estimates already sit at +13.4% for FY27 (consistent with guidance), so the guide cut was largely pre-empted — but the FY27 EPS consensus of $5.505 appears **stale** (Q1 alone printed $1.65 adj., ~$6.60 annualised). Underlying revision direction: **flattening after a strong up-wave**. Analyst PTs (median ~$235, range $190–$280, 12 raises Sep–Oct) imply +53% upside but were **set on or before the crash date** and are not yet refreshed — treat as lagging.
3. **Factor-crowding / non-diversification risk — beta is unusable as a hedge.** R² = 1.5% and beta t ≈ 1.96 (95% CI 0.0–1.5). Hedging TEAM with SPY removes essentially none of its risk. Position sizing on any beta-derived, market-neutral book is invalid. Vol 87.6% ≈ 1.9× the large-cap software norm.
4. **Quality factor is flattered by SBC — the most important accounting flag.** FY26 SBC = **$1.607B = 24.5% of revenue**. GAAP FCF is $1.319B (FCF yield 3.30%), but **FCF less SBC = −$287M → economic FCF yield −0.72%**. The accruals ratio of −0.2305 (which the model scores as *high quality* because net income is negative while OCF is positive) is almost entirely an **SBC add-back artifact**, not conservative accounting. Piotroski 6/9 (F1 ROA negative, F5 leverage and F6 equity change fail; F2/F3/F4/F7/F8/F9 pass). ROIC of 0.45% is below any plausible cost of capital despite 84.8% gross margins — the moat is real, the capital efficiency is not yet.
5. **Liquidity — adequate, not a concern.** ~2–3M shares/day ($300–450M), 7.5M shares on the Nov 6 event; no liquidity discount required.
6. **Sample-size caveat.** All ranks rest on n=7 hand-selected SaaS comps over one 252-day window that contains two unprecedented gap events. Alpha's t≈11 is statistically significant but economically it is a single-name idiosyncratic recovery, not repeatable skill — the factor-model read is **regime-dependent and low-confidence**.

*Growth/quality offset worth noting:* revenue growth is genuinely accelerating (+19.7% FY25 → +26.0% FY26 → +24% Q1 FY27), gross margin +200bp to 84.8%, FY26 buybacks $1.80B (4.5% of cap), and shares outstanding are flat-to-down (261.8M → 260.2M). Fundamental trajectory is intact; **the numbers say the multiple, not the franchise, is the problem.**
