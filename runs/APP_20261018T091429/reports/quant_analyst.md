# Quant Analyst

- Symbol: APP
- Elapsed: 107.5s

---
## Data Integrity Note (read first)

Two conflicting price series exist in the feed. My initial OHLCV pull was truncated at 2025-12-31 ($673.82), which made the factor outputs look contradictory. Extending the series resolved it: **the live quote is $266.13 as of 2026-10-16**, and every ratio/factor tool is internally consistent with that. The stock has fallen **−63.7% from its $733.60 close peak (2025-12-22)**. All figures below use $266.13.

One residual inconsistency I could not fully reconcile: the factor tool reports a 252-day annualised return of **−70.95%**, while OHLCV recomputation gives **−56.1%** ($605.68 → $266.13). I report both; the sign and magnitude of the conclusion are unaffected.

---

## 1. Factor Scores

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E 27.3x trail / **16.9x 2026E** / 13.3x 2027E; EV/EBITDA 21.1x (13.7x 2026E); P/FCF 23.1x (FCF yield 4.33%); P/B 42.7 | **4 of 5** | Neutral–Slightly Negative |
| **Momentum** | **−40.81%** (12-1) | **5 of 5 (worst)** | **Strong Negative** |
| **Quality** | ROIC 73.1%, ROE 156.2%, GP/A 0.663, accruals −0.088, **Piotroski 9/9** | **1 of 5** | **Strong Positive** |
| **Low Vol** | Vol 76.5%, beta 2.16 (regression) / 2.56 (profile) | **5 of 5 (worst)** | Strong Negative |
| **Earnings Revision** | +15.52% — *but see caveat* | n/a (not computed for peers) | Weak Positive (low confidence) |

Rank = 5-name ad-tech/application-software cohort (APP, TTD, CRM, NOW, ADBE), not a true sector percentile. Small cross-section — treat as indicative only.

**Earnings-revision caveat (important):** the +15.52% is derived from the **FY2030** consensus ($29.78 vs $25.78 prior) — a 4½-year-forward number covered by only **6 analysts**. Meanwhile the near-term, high-relevance signal runs the other way: all 10 recent price targets were **cuts** (Wedbush $610→560, GS $465→400, MS $450→400, Oppenheimer $560→490, Jefferies $550→375, Piper $385→325, BTIG $408→396). I weight the revision factor **weakly**, and it contradicts the headline "upgrade" label.

---

## 2. Price Statistics (252d, vs SPY)

| Metric | Value | Assessment |
|---|---|---|
| Alpha (annualised) | **−116.7%** | Catastrophic — but see significance flag |
| Beta | **2.166** (R² = 0.138) | Very high, statistically significant (t ≈ 7) |
| Ann. volatility | 76.5–76.8% | ~5x market |
| Sharpe (rf=0) | **−0.924** (tool) / −1.121 (alt calc) | Deeply negative |
| Sortino | **−1.178** | Worse than Sharpe — downside vol dominates |
| Max drawdown | **60.79%** (tool); **−64.3%** on close basis ($733.60→$262.19) | Severe, unresolved |

**Statistical-significance flag:** R² of 0.138 means ~86% of APP's variance is idiosyncratic. With one year of daily data, the standard error on annualised alpha is roughly 71%, so **alpha of −117% carries a t-stat of only ≈ −1.6 — not significant at the 5% level.** The negative alpha is economically real but statistically it is a single company-specific event, not a repeatable "skill" estimate. Likewise the 60.79% vs 64.3% drawdown gap suggests the tool uses intraday lows or a marginally different window.

**Return path (OHLCV, close-basis):** 12-mo −56.1% · YTD 2026 −60.5% · 6-mo −42.9% · 3-mo −38.7% · 1-mo −18.5%. The decline is **accelerating**, not basing.

**Correlations:** SPY 0.370 · META 0.337 · NOW 0.303 · MSFT 0.274. Low correlation to tech peers despite beta 2.17 — the de-rating is **company-specific, not sector-driven**, and offers genuine diversification value.

---

## 3. Peer Comparison (the key cross-section)

| | P/E | EV/EBITDA | P/FCF | ROE | GP/A | 12-1 Mom |
|---|---|---|---|---|---|---|
| **APP** | 27.3 | 21.1 | 23.1 | **156%** | 0.663 | **−40.8%** |
| TTD | **13.4** | **6.5** | **7.4** | 17.8% | 0.370 | −29.5% |
| ADBE | 14.7 | 10.7 | 10.6 | 61.3% | **0.719** | +11.8% |
| CRM | 30.9 | 18.1 | 16.0 | 12.6% | 0.287 | **+46.7%** |
| NOW | 85.0 | 48.3 | 32.5 | 13.5% | 0.395 | +24.5% |

Diagnosis: APP has **best-in-class profitability** (ROIC 73%, 87.9% gross margin, 75.8% operating margin, FY25 revenue +70%, net income +111%) paired with **worst-in-class price action** and **mid-pack valuation**. This is the signature of **multiple compression, not fundamental deterioration**: at the Dec-2025 peak the trailing P/E was ~75x; it is now 27.3x on *higher* earnings.

---

## 4. Composite Quant Signal

### **NEUTRAL** (leaning cautious)

**Scorecard:** Quality **+2** · Value **−1** · Momentum **−2** · Low Vol **−2** · Revision **+0.5** → net **−2.5**

Reasoning: the quality and value legs are genuinely exceptional and would normally dominate a multi-factor screen. But I cannot upgrade this to Buy while it ranks **last of five on both momentum and low-volatility**, is still making new lows (1-mo −18.5%), and carries Sharpe −0.92 / Sortino −1.18. Momentum is the most persistently rewarded of the factors, and a −64% drawdown with no basing pattern is not a "cheap" signal — it is an unresolved de-rating. Equally I will not call Sell: 16.9x forward earnings against ~60% expected 2026 EPS growth, a 9/9 F-Score, and consensus targets averaging **$438 (median $425, +64.6% upside)** make the downside case statistical rather than fundamental.

---

## 5. Key Quant Risk Flags

1. **Momentum reversal / downtrend continuation — highest severity.** −40.8% 12-1, worst in cohort; decline accelerating (−18.5% in one month). No evidence of a floor.
2. **Factor crowding unwound, not reversed.** Beta 2.17 + 76% vol made APP a momentum-crowding magnet on the way up; the crash has largely cleared that positioning, which is a *forward* positive — but there is no positioning data confirming capitulation. I flag this as unverified rather than resolved.
3. **Estimate quality risk.** The positive revision signal rests on FY2030 with 6 analysts. Note the estimate curve decelerates hard: 2028E $25.05 → 2029E $25.78 (**+2.9%**). If the long-tail growth story is being marked down, the "cheap" forward multiple is illusory.
4. **Valuation artifact in P/B.** 42.7x P/B on BVPS of $6.24 — ROE of 156% is a denominator effect (buybacks plus accumulated deficit), not evidence of returns this sustainable. Do not read the value/quality scores at face value on this name.
5. **Alpha not statistically significant** (t ≈ −1.6, R² 0.138). Do not extrapolate −117% alpha.
6. **Liquidity: not a risk.** ~$1.2B daily dollar volume (4–5M shares); institutional entry/exit is unconstrained. Flagged as clear.
7. **Turning-point fragility.** A 76% vol / beta 2.17 name is a poor fit for tight risk budgets: a single disappointing quarter historically moves this stock 15–20% in a day (e.g., −20% on 2026-02-04, −20% on 2026-08-06).

**What would flip me to Buy:** price reclaiming the 200-day (roughly the $400 area), two consecutive quarters of *near-term* (FY26/FY27) EPS revisions up, and momentum turning positive on a 3-month basis. All three are absent today.

**Data gaps, stated honestly:** (a) peer volatility/low-vol scores were not computed — the 5-of-5 low-vol rank is inferred from APP's absolute 76% vol and beta >2, not from a measured peer distribution; (b) earnings-revision ranks across peers unavailable; (c) short interest and full rating distribution unavailable — target notes carried no rating field; (d) the sector-peer tool returned mega-cap semiconductors for a software company, so I substituted a hand-selected ad-tech/application-software cohort, which is a 5-name sample and not sufficient for statistically robust cross-sectional ranking.
