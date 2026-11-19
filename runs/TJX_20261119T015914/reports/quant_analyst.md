# Quant Analyst

- Symbol: TJX
- Elapsed: 67.7s

---
# TJX Companies (TJX) — Quantitative Factor Report

**Price used:** $152.93 (last close 2026‑02‑13). ⚠️ Note: the valuation/ratio engine returned a **stale $140.30 snapshot**, so all multiples below are **re‑based ×1.090** to the current price. Market cap ≈ $172.0B (1,125M diluted sh).

---

## 1. Factor Scores Table

| Factor | Score (0–100) | Sector Rank | Signal |
|---|---|---|---|
| Value | **30** | **3 of 3** | **Bearish / expensive** |
| Momentum | **65** | **1 of 3** | **Bullish (decelerating)** |
| Quality | **92** | **1 of 3** | **Strong bullish** |
| Low Vol | **85** | **1 of 3** | **Bullish** |
| Earnings Revision | **65** | **1 of 3** | **Mildly bullish (low confidence)** |
| **Composite** | **66 / 100** | — | **Buy (low conviction)** |

### Supporting inputs

**Value (30/100) — the weak leg.** TTM P/E 31.3x (EPS diluted $4.88), P/B **16.9x** (BVPS $9.06), EV/EBITDA **21.0x** ($179.3B EV / $8.546B EBITDA), P/FCF **35.0x** (FCF ≈ $4.92B; FCF yield **2.86%**), dividend yield 1.22%. Forward: 26.7x FY28E EPS $5.73, 23.9x FY29E $6.39. Versus HD (23.7x P/E, 15.9x EV/EBITDA, 26.6x P/FCF) and LOW (18.8x, 13.5x, 16.3x), TJX carries a **30–60% multiple premium** on every metric — the worst of the three retail comps.

**Momentum (65/100) — positive but fading.**
- 12‑1 momentum, hand‑computed from daily closes (2025‑02‑14 $121.63 → 2026‑01‑15 $154.18, 21‑day exclusion): **+26.8%** ⚠️ *the momentum module reported −6.26% for the same window — directly contradicted by raw OHLCV; see risk flag #4.*
- 6‑month (126d) momentum: **+18.46%** — consistent with raw closes (~+17.8%).
- Last 3 months: **−0.8%**; last 20 sessions: **−1.6%**. Price capped at $156.54 (Jan‑8 high), now 2.3% below.
- 252‑session range: $110.35 – $156.54.

**Quality (92/100) — best in peer set.**
- ROIC **30.31%**, and *monotonically improving*: 25.43% → 29.21% → 29.77% → 30.31% (FY23–FY26).
- GP/Assets (Novy‑Marx) **0.5226** — top‑decile profitability.
- Accruals **−0.0386** (negative four years straight: −0.021, −0.053, −0.039, −0.039); CFO/NI = **1.25x** — high earnings quality.
- **Piotroski F‑Score 8/9** (only F9 asset‑turnover improvement fails: 1.69x vs 1.78x).
- ROE 53.92% (down from 61.27% — equity build, not deterioration). Buybacks: 1,159M → 1,142M → 1,125M shares (−1.5%/yr).
- Margin expansion: gross 30.96% (vs 30.60% FY25), operating **11.89%** (+71bp), net 9.10% (+47bp). Revenue +7.1% to $60.37B; diluted EPS +14.6%.

**Low Vol (85/100).** 504d vol **21.7%**, beta **0.252**, vs HD (28.3% vol, 0.70 beta) and LOW (30.7%, 0.60). Lowest-risk name in the group. ⚠️ The 252d module printed 26.0% vol / 0.304 beta, and the company profile lists beta 0.587 — beta estimates span 0.25–0.59, so treat the exact figure as uncertain.

**Earnings Revision (65/100).** Latest consensus **+7.31%** vs 3 months prior on the forward period. **But: the forward period is FY2031 and consensus is 1–2 analysts (`num_analysts: 2`)** — statistically meaningless. Directionally corroborated by the estimate ladder (FY28 $5.73 → FY29 $6.39 → FY30 $6.57, ~+11.5%/yr). Peers also upgraded (LOW +6.14%, HD +4.32%) — TJX ranks first only within noise.

---

## 2. Price Statistics

| Metric | 504‑day (primary) | 252‑day (flag) |
|---|---|---|
| Annualised return | **+12.38%** | −11.4% ⚠️ |
| Annualised vol | **21.7–21.8%** | 26.1% |
| Sharpe (0% rf) | **0.45 / 0.57** | −0.44 ⚠️ |
| Sortino (0% rf) | **0.909** | −0.72 ⚠️ |
| Beta vs SPY | **0.252** | 0.304 |
| Alpha (annualised) | **+5.84%** | −9.19% ⚠️ |
| R² vs SPY | **0.0224** | 0.0286 |
| Max drawdown | 26.83% (unverified) | 26.83% (identical) ⚠️ |

**Statistical caveats that matter:**
- **R² = 2.2–2.9%** — SPY explains almost none of TJX's variance. Residual (idiosyncratic) vol ≈ **21.4%** of the 21.7% total. Beta 0.25 with SE ≈ 0.06 → 95% CI roughly 0.13–0.38; the profile's 0.587 sits outside the point estimate. The low-beta/low-vol classification is real but imprecise.
- Alpha SE ≈ 21.4% / √2yrs ≈ **15%**, so the +5.84% alpha has a **t‑stat ≈ 0.4 → statistically indistinguishable from zero.** Do not claim outperformance from this regression. (Realised raw return of +12.4% annualised vs SPY is the better evidence, but it is not risk-adjusted significance.)
- Sortino/Sharpe = **1.6** — downside deviation is materially smaller than total vol, i.e. fat right tail / contained left tail. This is the most favourable risk statistic in the set.

---

## 3. Composite Quant Signal: **BUY (low conviction)**

Weighted (Value 25%, Momentum 25%, Quality 25%, Low Vol 15%, Revision 10%) → **66/100**.

The entire bull case is **quality + low vol + intact 12‑month momentum**. Nothing in the value leg supports it: TJX is the most expensive of its retail comps on P/E, EV/EBITDA and P/FCF, and it trades at 16.9x book. At 31x TTM earnings, the expected return is almost entirely earnings/FCF compounding (~11–14% EPS growth) with no multiple support and some multiple risk. **Downgrade trigger:** a close below ~$140 (−8.5%, the Oct‑2025 shelf) breaks 12‑1 momentum and would move this to Neutral; below ~$130 the momentum factor flips negative outright.

---

## 4. Key Quant Risk Flags

1. **Momentum reversal risk (moderate-high).** 12‑1 momentum of +26.8% is front-loaded (Feb–Jun 2025 ramp) and has **stalled: 3‑month return −0.8%, capped at $156.54**. Standard momentum crashes hit exactly this profile — high-quality, low-beta, crowded winners — hardest.
2. **Factor crowding / de-rating risk (high).** TJX screens top quintile on quality and low‑vol simultaneously, the most crowded combination in the market. 21x EV/EBITDA leaves no cushion: a 2‑point gross-margin miss would plausibly compress the multiple 15–20%.
3. **Alpha/beta insignificance.** Alpha t‑stat ≈ 0.4, R² 2.2%. Any claim of "risk-adjusted outperformance" from this regression is unsupported. Residual vol 21.4% means this is an idiosyncratic bet, not a market-exposure play.
4. **Material data-integrity failures (please carry into the memo):**
   - Valuation engine snapshot is **stale at $140.30** vs $152.93 close — all multiples re‑based +9.0% by me.
   - **252‑day price-stat module contradicts raw OHLCV**: −6.26% 12‑1 momentum vs +26.8% computed from the daily series; −11.4% annualised return vs +25.7% actual 252‑session price change. The 504‑day module reconciles with the raw data and is used as primary.
   - **Max drawdown prints 26.83% identically on both the 252d and 504d windows** — a stale/fixed value; my own series shows a ~−9% max drawdown over the past 252 sessions. **Do not use 26.83%.**
   - Revision score built on **FY2031 estimates with n=1–2 analysts** — no statistical power.
   - **BABA peer multiples unusable** (P/E 1.92, EV/EBITDA 0.56) → excluded from the peer set.
5. **Peer sample too small for real cross‑sectional ranks.** `get_sector_peers` returned mega-caps across unrelated industries (AMZN, TSLA, TM, MCD, SBUX). Ranks are against **n=2** genuine comps (HD, LOW) — treat quintile language as indicative only.
6. **Liquidity: no concern.** ~5.5M ADV ≈ $840M/day; 377,000 employees; $172B cap. Zero liquidity or capacity constraint.
7. **Watch item — asset turnover is the one deteriorating metric** (1.78x → 1.69x, the sole F‑Score failure). Rising ROIC is coming from margin, not efficiency. If margins plateau, ROIC rolls over.
