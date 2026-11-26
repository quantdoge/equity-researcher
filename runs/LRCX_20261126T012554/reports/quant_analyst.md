# Quant Analyst

- Symbol: LRCX
- Elapsed: 84.1s

---
Reconciliation complete — and it's the single most important finding. The latest close is **$185.01 on 2026-11-25**, which matches the profile price exactly. The stock peaked at **$432.87 (Jun-30-2026)** and has since collapsed ~57%. My first OHLC pull ended at the peak, which is why it looked bullish; the full series reveals a post-parabolic breakdown. All the negative risk readings now reconcile. Here is the report.

---

# LRCX — Quantitative Factor & Risk Report
**Lam Research Corp. | Semiconductors | Price (2026-11-25): $185.01 | Mkt cap ~$231B**

> **Critical data note first:** The analysis date is **2026-11-25**. LRCX ran from ~$82 (Jun-2025) to a **$432.87 peak on 2026-06-30**, then fell to **$185.01** — a **−57% drawdown**. My initial OHLC pull ended at the June peak and looked bullish; the full series + Oct/Nov price targets confirm a severe post-peak breakdown. Every negative risk reading below is consistent with this collapse.

## 1. Factor Scores

| Factor | Score | Sector Rank* | Signal |
|--------|-------|--------------|--------|
| **Value** | P/E 32.1 · EV/EBITDA 26.6 · P/FCF 47.7 · ROE 58% | 3 of 4 (~mid-low) | **Neutral** — not cheap; expensive vs MU/NVDA, cheaper than AVGO. FY26 multiples sit on **peak-cycle** earnings |
| **Momentum** | 12-1 return **−22.5%**; trend **−57% from Jun peak** | 4 of 4 (bottom) | **Negative** — clean downtrend, lower highs/lows Jul→Nov |
| **Quality** | ROE 58.3% · GP/Assets 0.50 · accruals **+6.0%** | 3 of 4 (mid-low) | **Low** — strong absolute ROE but highest accruals in group (>5% = quality ding); F-score 8 offsets |
| **Low Vol** | β **3.29** (calc) / 2.01 (profile) · ann. vol **75%** · maxDD **−57.7%** | 4 of 4 (bottom) | **Very Negative** — highest beta/vol in peer set |
| **Earnings Revision** | **+19.2% "upgrade"** ⚠️ | n/a | **Spurious — disregard.** Tool compared **FY2031 ($18.67) vs FY2030 ($15.66)** — two *different* fiscal years, not a same-period revision. It's just the year-over-year earnings growth curve, not estimate momentum |

\*Rank among 4 usable semis peers (NVDA, MU, AVGO; **TSM excluded — corrupt data**: P/E 1.03, EV/EBITDA −0.11).

**Real revision read (price-target level):** On 2026-10-22 sell-side targets were being **cut across the board** (UBS $425→$400, BofA $385→$345, MS $385→$339, Needham $390→$290). That is **negative** revision momentum — the opposite of the tool's headline.

## 2. Price Statistics (252-day window, vs SPY)

| Metric | Value | Read |
|--------|-------|------|
| Alpha (annualised) | **−30.7%** | Severe underperformance vs market |
| Beta | **3.31** (calc) / 2.01 (profile) | Extreme market sensitivity — see flag |
| R² | 0.49 | ~Half of variance is market-driven |
| Sharpe | **−0.027** | Negative risk-adjusted return |
| Sortino | **−0.043** | Negative — downside vol not compensated |
| Annualised return (calc) | −2.1% | Flat-to-negative despite the round-trip |
| Annualised volatility | **76.3%** | ~Top-decile risk |
| Max drawdown | **−57.7%** | Peak $432.87 (Jun-30) → $181.77 (Nov-20) |
| Current vs peak | **−57.3%** | Downtrend intact |

## 3. Composite Quant Signal: **SELL**

| Factor | Direction |
|--------|-----------|
| Momentum | Sell (bottom rank, −57% trend) |
| Alpha | Sell (−30.7%) |
| Low Vol | Sell (β 3.3, vol 75%) |
| Quality | Soft sell (accruals) |
| Value | Neutral (not cheap on FCF; peak-cycle multiples) |
| Earnings Revision | Neutral (headline spurious; PTs being cut) |
| Fundamentals | Offset (F-score 8, ROIC 49%) |

**Four of five factors are negative**, and the only "positive" (earnings revision) is a data artifact. This is a **peak-cycle semi-equipment name rolling over** — quantified. The strong F-score-8/ROIC-49% signals quality *at the top of the cycle* and are backward-looking; the market is already discounting a down-cycle. Not "Strong Sell" only because the stock is now −57% from peak and valuation has de-rated — but there is no quant confirmation of a bottom yet.

## 4. Key Quant Risk Flags

1. **Falling knife / realized momentum reversal.** −57% from the June peak with unbroken lower highs/lows through November (recent bounce to $235 failed, back to $185). Trend, alpha, and drawdown all point the same way — no base building yet.
2. **Extreme beta (3.3 calc vs 2.0 profile).** Discrepancy itself is a data caveat, but both confirm **high/rising downside beta**; in a semi down-cycle this amplifies losses. This is the dominant risk for position sizing.
3. **Peak-cycle quality illusion.** F-score 8 and 49% ROIC rest on record gross margins; **accruals already +6.0%** signals degrading earnings quality. High mean-reversion risk in margins/estimates.
4. **Stale, falling sell-side targets.** Average PT ~**$347 vs $185 spot (+87%)** — but every target was *cut* and price has fallen *through* them since. Treat as **lagging**, likely to be reduced further; **not** a value floor.
5. **Factor crowding / cyclicality.** LRCX trades on WFE-capex beta, not idiosyncratic merit; correlated to NVDA/MU/AVGO memory-logic cycle — any semi selloff hits it hardest (β 3.3).
6. **Data-integrity caveats:** (a) profile β 2.01 vs calc 3.29; (b) earnings-revision +19% is a **cross-year (FY31 vs FY30) artifact**, not a true revision — **do not use**; (c) TSM peer multiples corrupt (P/E 1.03) — excluded from rankings. Liquidity is **not** a concern (large-cap, heavy volume).

**Bottom line:** On the systematic evidence, LRCX is a **quantitative Sell** — broken momentum, negative alpha, extreme beta/high vol, and low earnings quality, with the sole "upgrade" signal being a methodology artifact and sell-side targets in retreat. Sample window (252d) and peer set (n=4 usable) are modest — factor ranks above ~60th percentile carry limited statistical weight.
