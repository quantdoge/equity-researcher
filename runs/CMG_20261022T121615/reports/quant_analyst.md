# Quant Analyst

- Symbol: CMG
- Elapsed: 192.3s

---
Data gathering complete. Here is the quantitative factor analysis for **CMG (Chipotle Mexican Grill)**.

---

## 1. Factor Scores Table

| Factor | Score | Sector Rank* | Signal |
|--------|-------|-------------|--------|
| **Value** | P/E 24.7 · EV/EBITDA 17.6 · P/FCF 26.1 · P/B 13.3 | 2nd of 4 on P/E & EV/EBITDA; 3rd on P/FCF | **Neutral** (mid-pack, no margin of safety) |
| **Momentum** | 12-1 return **−10.21%**; full-period ann. return **−41.9%** | 1st of 4 — but all four peers ≈ −10.5% | **Negative** |
| **Quality** | ROE 54.3% · ROIC 25.5% · GP/Assets 0.336 · Accruals −0.064 · F-Score 6/9 | **1st of 4** (peers all negative ROE/ROIC) | **Strong / Bullish** |
| **Low Vol** | Ann. vol 41.0% · Beta 0.467 · Max DD 31.2% | n.m. (peer vol unavailable) | **Mixed** — low beta, high absolute vol |
| **Earnings Revision** | Forward EPS revised **−5.74%** (1.92 → 1.81); 4 of 5 recent PTs cut | n.m. (peer revisions unavailable) | **Bearish** |

*Sector rank = within restaurant peer set CMG / MCD / SBUX / YUM. Small (n=4) peer group — treat ranks as directional, not statistically robust.*

**Fundamental detail:** ROIC has risen every year — 19.0% (2022) → 21.9% (2023) → 23.4% (2024) → 25.5% (2025); a genuinely improving profitability trend. Note ROE of 54.3% is flattered by buyback-driven equity shrinkage (Piotroski F6 "positive equity change" = 0); ROIC 25.5% is the cleaner quality read. Accruals have been consistently negative (−0.061 to −0.069) — high earnings quality. Piotroski 6/9 "Moderate"; misses on leverage (F5) and equity change (F6).

---

## 2. Price Statistics (252-day window vs SPY)

| Metric | Value |
|--------|-------|
| **Alpha (annualised)** | **−42.9%** |
| **Beta** | **0.467** (profile beta 0.958 — calc vs SPY is lower) |
| **R²** | **0.0223** — only 2.2% of return variance is market-explained |
| **Sharpe** | **−1.02** |
| **Sortino** | **−1.574** |
| **Annualised return** | −41.9% |
| **Annualised volatility** | 41.1% |
| **Max drawdown** | 31.2% |

**Price trajectory confirmation:** CMG gapped down ~18% on 2025-10-30 ($39.76 → $32.53, likely earnings) and has ground lower all year. It sits at ~$28.12, essentially the 52-week low (high ~$42.8). The 12-1 momentum (−10.2%) is far milder than the full-period return (−41.9%) — the gap confirms the decline is **recent and accelerating**, with the latest weeks making fresh lows. Sortino (−1.57) worse than Sharpe (−1.02) means downside volatility dominates.

---

## 3. Composite Quant Signal: **NEUTRAL (bearish tilt)**

The composite is genuinely split, and the tie-breaker is momentum:

- **Bullish leg:** Best-in-class quality (ROIC 25.5% and rising, top ROE, negative accruals, F-Score 6), and valuation mid-pack vs peers (P/E 24.7 vs SBUX 60.8, YUM 27.2; cheaper than SBUX/YUM on EV/EBITDA).
- **Bearish leg:** Momentum firmly negative and hitting 52-week lows, EPS estimates cut 5.74%, four of five recent price targets lowered ($51→$45 DB, $42→$36 GH, $42.50→$37 RJ, $40→$38 Stephens; only MS raised $39→$40), alpha −42.9%, Sharpe −1.02, Sortino −1.57.

Quality and valuation keep this from a hard **Sell**, but the negative momentum, downward revisions and deeply negative alpha block any **Buy**. **Neutral with a bearish tilt** is the honest quant verdict — a high-quality business in a clear, unresolved downtrend.

---

## 4. Key Quant Risk Flags

1. **Momentum-reversal / falling-knife risk (HIGH):** −10.2% 12-1 momentum, −41.9% annualised return, −31.2% max drawdown, price at 52-week low. Downtrend is intact and accelerating into lows; no base formation yet.
2. **Estimate-revision risk (HIGH):** −5.74% forward EPS cut with a cluster of price-target reductions. Revisions lead price — the direction is bearish. Caveat: forward estimate coverage is thin (2030 EPS consensus from only 4 analysts), so revision signal has low statistical confidence.
3. **High idiosyncratic / low R² risk (HIGH):** R² = 0.022 vs SPY — 98% of return variance is stock-specific. Beta 0.467 badly understates realized risk; 41% annualised vol is high in absolute terms. This is a single-name event-risk profile, not a market-beta hedge.
4. **Quality metric distortion (MEDIUM):** ROE 54.3% is inflated by buybacks/low equity (F-Score flags no positive equity change). Use ROIC (25.5%) and ROA (17.1%) as the true quality gauges — still strong, but less spectacular than headline ROE.
5. **Valuation cushion insufficient (MEDIUM):** P/E 24.7 and P/FCF 26.1 are only marginally below the peer group — not cheap enough to provide a hard downside floor if estimates keep falling.
6. **Sample-size caveat:** Peer set is only four names and several factor ranks (low-vol, revisions) lack peer data — sector-percentile claims are directional only.

**Bottom line:** Exceptional quality and reasonable (not cheap) valuation vs a broken price trend and negative estimate momentum. Quant signal is **Neutral (bearish tilt)** — wait for momentum/revision stabilization before adding exposure; quality alone is not a catalyst.
