# Quant Analyst

- Symbol: AXON
- Elapsed: 40.7s

---
# AXON — Quantitative Factor & Risk Report

**Axon Enterprise, Inc.** | Industrials / Aerospace & Defense | Price **$343.05** (2026-11-25) | Mkt cap **$27.94B** | EV **$28.46B**
Note: the price series extends through **2026-11-25**; the stock is **−61% from its Aug-2025 peak of $885.92** and **−46% from its 52-week high of $641.51 (2026-01-13)**. Recent low $291.14 (2026-11-20); currently +17.8% off that low.

## 1. Factor Scores

| Factor | Score (0–10) | Sector Rank | Signal |
|---|---|---|---|
| **Value** | **1 / 10** | **5 of 5** (A&D) | Strong negative |
| **Momentum** | **2 / 10** | **5 of 5** | Negative / accelerating down |
| **Quality** | **4 / 10** | 4 of 5 | Mixed (best GP/A, worst ROIC) |
| **Low Vol** | **1 / 10** | **5 of 5** | Strong negative |
| **Earnings Revision** | **3 / 10** | n/a | Negative on targets; tool signal unreliable (see caveat) |

**Value — 1/10.** P/E **227.2**, EV/EBITDA **144.9**, P/FCF **376.4**, P/B **8.71**, no dividend. Against Aerospace & Defense peers (EV/EBITDA median **20.2**: LMT 17.9, RTX 20.0, BA 20.4, GE 28.7) AXON trades at **7.2× the peer median**; on P/E (peer median 39.2) it is **5.8×**. Dead last in sector on every multiple. *Caveat: trailing multiples are distorted by a 67% collapse in net income (2025 $124.7M vs 2024 $377.0M); on forward consensus the picture is far less extreme — see §4.*

**Momentum — 2/10.** 12-1 momentum **−31.7%**; 6-1 momentum **−6.1%**; last 21 trading days **−19.4%** (Oct 27 $425.87 → $343.05); YTD **−39.1%**. Persistent lower highs since Aug-2025, with a fresh leg down in Nov-2026 on 5.2M shares (≈5× ADV). Negative momentum is *not* decaying — it is re-accelerating, which is the worst configuration for a mean-reversion entry.

**Quality — 4/10.** Genuinely two-sided: gross profit/assets **0.237** is the **highest of the peer set** (GE 0.130, LMT 0.127, RTX 0.104, BA 0.026) and accruals are clean at **−1.24%** (4-yr average negative — no earnings-quality red flag). But ROE **3.84%** (down from 16.2%), ROA 1.78%, and ROIC **−1.2%** (2024 +1.6%, 2023 +6.7%, 2022 +4.7%) mean capital is currently not being rewarded. Piotroski **F-Score 5/9** (failures on ROA improvement, leverage, dilution, gross-margin trend, turnover).

**Low Vol — 1/10.** 2Y annualised vol **60.6–61.1%**, 1Y vol **69.6%**; beta **1.28–1.34** vs SPY (reported beta 1.47); max drawdown **66.6%**. Roughly 3× the volatility of a typical industrial and the highest beta in the peer group.

**Earnings Revision — 3/10.** ⚠️ **The tool's "+33.86% upgrade" is almost certainly a period-misalignment artifact**: it compares FY2028E of 12.64 against a "prior" of 9.44074 — which is *exactly* today's FY2027 consensus. Treat the positive reading as invalid. The **observable** revision flow is unambiguously negative: every post-print target cut (Raymond James 800→675→475; Piper Sandler 732→561→540; TD Cowen →800; RBC →615; Northland →540; Needham →500) following the Nov-6 "rare miss on Dedrone lumpiness."

## 2. Price Statistics

| Metric | 2Y (504d) | 1Y (252d) |
|---|---|---|
| Alpha (ann., vs SPY) | **−54.06%** | **−16.78%** |
| Beta (vs SPY) | **1.282** | **1.343** |
| R² | **0.086** | 0.095 |
| Annualised return | **−38.28%** | n/a |
| Annualised vol | **61.14%** | 69.56% |
| **Sharpe** | **−0.626** | −0.077 |
| **Sortino** | **−0.860** | n/a |
| Max drawdown | **−66.6%** | −54.9% |

**Statistical honesty:** R² of **8.6%** means systematic market exposure explains almost none of AXON's return variance — this is a **91% idiosyncratic** name. With residual vol ≈58% and 504 observations, the standard error on annualised alpha is ≈41pp, so alpha of −54% carries **t ≈ −1.3 — not statistically significant at 5%**. The *sign* is clear and consistent across both windows, but the *magnitude* should not be quoted as an established point estimate. Sortino (−0.86) materially worse than Sharpe (−0.63) confirms the downside-realised vol is larger than upside vol — negative asymmetry, not symmetric noise.

## 3. Composite Quant Signal

**SELL** (composite **2.2 / 10**, equal-weighted across five factors)

Three of five factors sit in the bottom decile of their cross-section (value, momentum, low-vol) with no offset from quality or revisions. This is the classic **de-rating configuration**: extreme multiple compression delivered by negative momentum, high beta, and deteriorating returns on capital. It is **not** a Strong Sell only because (a) gross profitability is best-in-class and accruals are clean, (b) the F-Score is a pass at 5, and (c) an upgrade trigger exists (see below).

**Upgrade trigger (what would move this to Neutral):** 20-day momentum turning positive *while* the rolling vol compresses below ~50% and sell-side EPS estimates for FY2027 stop falling. None of those three conditions is met today. Note that consensus price targets (median ≈**$540**, range $475–800) sit **+57% above spot** — a very wide target/price gap that itself signals unresolved estimate risk rather than a free option.

## 4. Key Quant Risk Flags

1. **Momentum reversal risk / falling knife (HIGH).** −67% peak-to-trough with −19.4% in the last month alone. In the factor literature, deep-negative 12-1 momentum with *rising* short-term volatility has a poor 1–3 month expectancy; the reversal premium only pays when the decline stabilises.
2. **Factor crowding / de-grossing (HIGH).** AXON was a crowded long-duration quality-growth position at 145× EV/EBITDA. The event-day volume spikes (4.9M on 2026-11-05, 5.2M on 11-06, 4.4M on 2026-02-25 vs ~1M typical) are consistent with institutional de-risking, not retail flow — crowding unwinds in clusters.
3. **Idiosyncratic/event risk (HIGH).** R² ≈ 9%. Beta-hedging barely reduces risk; position sizing, not hedging, is the control. Dedrone integration "lumpiness" is now a demonstrated earnings driver.
4. **Earnings-quality optics (MEDIUM).** Trailing P/E 227 is not comparable to the sector; ROIC is negative for the first time in four years. Any further negative EPS revision re-rates the multiple again from an already-compressed base.
5. **Estimate-revision data gap (MEDIUM).** No clean consensus time-series available; the revision tool returned a mismatched comparison period. Revision conclusions here rest on price-target changes, which are a noisier proxy. Sample size for FY2028E is only **4 analysts** (dispersion $8.85–$14.18, i.e. ±42%) — statistically too thin to treat as consensus.
6. **Liquidity (LOW).** ~1.0–1.5M shares/day ≈ $350–500M notional. No execution constraint at institutional sizes.

**Peer-comparability caveat:** the A&D tag is loose — AXON's economics are software/sensors, so its legitimate multiple band is above the LMT/RTX group. Even granting that, it is the worst-ranked name on value, momentum and low-vol within the group, so the relative conclusion is robust to the classification issue.
