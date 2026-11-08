# Quant Analyst

- Symbol: HALO
- Elapsed: 51.6s

---
# HALO (Halozyme Therapeutics) — Quantitative Factor Report

**Sector:** Healthcare / Biotechnology · **Price:** $103.63 · **Mkt cap:** $11.8B · **Data as-of:** FY2025 (2025-12-31) annuals + 252-day price window

## 1. Factor Scores

| Factor | Score | Sector Rank* | Signal |
|---|---|---|---|
| Value | P/E 40.5 · EV/EBITDA 25.9 · P/FCF 19.9 | **3 / 5** (~40th pct) | **Neutral** |
| Momentum | **+32.6%** (12-1) | **1 / 5** (top) | **Strong Buy** |
| Quality | ROIC 36.6% · GP/Assets 0.463 · Accruals −0.133 | **1 / 5** (top) | **Strong Buy** |
| Low Vol | Vol 43.5% · Beta 0.60 · MDD 24.1% | **5 / 5** (worst) | **Strong Sell** |
| Earnings Revision | **−7.46%** (FY2030 EPS) | n=1 | **Weak / not significant** |

\*Peer set = HALO, ALNY, VRTX, GILD, BMRN (the `get_sector_peers` output returned only mega-cap pharma — LLY, JNJ, ABBV — which is *not* a valid comp set for an $11.8B drug-delivery royalty platform, so I built a biologic-peptide/rare-disease comp set instead).

**Value detail (rank within 5-name set):** P/FCF 2nd (19.9x vs BMRN 15.3, GILD 22.2, VRTX 44.2, ALNY 45.1); EV/EBITDA 3rd; P/E 4th. Cheapest on cash conversion, not on earnings. Note trailing P/E 40.5x is computed off FY2025 net income of $317M ($2.56/sh) — **materially inconsistent** with the FY2025 consensus EPS of $6.55 in the estimates file. On FY2026E EPS of $8.62 HALO is **~12.0x forward**, and ~9.9x on FY2027E $10.42. The value signal is highly sensitive to which EPS figure is correct; treat the 40.5x trailing multiple as unreliable.

**Quality detail:** ROE 649% and P/B 265.7x (BVPS $0.39) are **artifacts of buyback-shrunk book equity**, not genuine profitability — discard both. The defensible metric is ROIC, which has compounded 16.0% → 21.3% → 29.5% → **36.6%** across FY22–FY25, above every peer. Accruals −13.3% (best in set = cleanest cash conversion; OCF $652M vs NI $317M) and GP/Assets 0.463 (2nd only to ALNY 0.612). Piotroski F-Score 5/9 (moderate) — the four misses are ROA improvement, leverage reduction, equity issuance (buybacks), and gross-margin improvement.

**Revision detail — the one genuine red flag:** the estimate term structure is non-monotonic: FY26 $8.62 → FY27 $10.42 → FY28 $12.16 → **FY29 $10.81 → FY30 $10.01**. Estimates peak in FY2028 then *decline*, consistent with the ENHANZE/rHuPH20 royalty base rolling off post-patent-expiry. The −7.46% cut to FY2030 is directionally consistent with that but rests on **1 analyst** — not statistically meaningful. Counter-evidence: sell-side price targets have been raised repeatedly (H.C. Wainwright $95→$115→$130, Morgan Stanley $93→$105, Wells Fargo $75→$95, Leerink upgrade to Outperform). Recent targets cluster **$95–130, median ~$101** vs $103.63 spot — i.e., the market has already run past the median target and the two $130 outliers were posted when the stock traded at $111–122.

## 2. Price Statistics (252 days)

| Metric | Value |
|---|---|
| Annualised return | 43.28% |
| Annualised volatility | 43.5% |
| **Sharpe** | **0.99** |
| **Sortino** | **1.38** |
| Beta vs SPY | **0.60** (regression) / 0.90 (5y profile) |
| **Alpha (annualised)** | **+51.2%** |
| R² vs SPY | **0.039** |
| Max drawdown | 24.1% |

**Beta is inconsistent across sources** (0.60 one-year daily vs 0.90 five-year in the profile) — use 0.60 for current risk budgeting but recognize the longer-run sensitivity is materially higher.

**The alpha is not statistically significant.** With R² of only 3.9%, just 4% of HALO's variance is market-explained; the annualised alpha standard error is ≈ 43.5% × √0.961 ≈ **42.7%**, giving a **t-stat of ~1.2**. The +51% "alpha" is essentially the residual of one very strong idiosyncratic year, not a repeatable market-neutral edge. This is a single-factor (own-story) stock, not a beta play — a genuine diversification benefit, but do not underwrite the alpha.

Internal inconsistency to flag: the volatility tool reports Sharpe **1.314** while the dedicated Sharpe/Sortino tool reports **0.991** on the same 252-day window (the 1.31 appears to use a different annualisation convention off the same 43.5–43.7% vol). I use **0.99** as the conservative primary figure; either way Sortino > Sharpe by ~40%, indicating downside deviation is smaller than total deviation — returns are positively skewed.

## 3. Composite Quant Signal

# **BUY**

Top-quintile **momentum (1/5)** and **quality (1/5)** — a rare combination — combined with improving ROIC and negative accruals carry the rating. It is capped below Strong Buy by three offsetting facts: (a) valuation is only mid-pack and the "cheap" P/FCF sits against a 40x trailing earnings multiple; (b) the low-vol factor is the worst in the comp set (43.5% vol, highest beta of the five); (c) the forward estimate curve implies peak earnings in FY2028 with decline thereafter. Statistically, momentum + quality is the highest-Sharpe factor pairing in the literature, and HALO screens at the intersection of both — but with a 43.5% vol name, position sizing matters more than the signal.

## 4. Key Quant Risk Flags

- **Momentum reversal / crowding risk — high.** +32.6% 12-1 momentum after a year in which the stock traded from ~$64 to ~$122 before pulling back ~15% to $103.63. Post-run-up names with 43% vol are prone to sharp give-back; the 24.1% max drawdown already occurred inside this window.
- **Idiosyncratic concentration — high.** R² 0.039 means SPY beta provides almost no hedge. This is a single-asset, single-platform (ENHANZE royalty) risk; diversification value is high but so is single-news-event exposure.
- **Factor-model artifact risk — moderate.** P/B 265.7x and ROE 649% will make HALO screen as "expensive"/"low quality" in any naive value/quality model. Any screener using those raw fields will misclassify it. Use ROIC and accruals instead.
- **Estimate-horizon / data-quality flag.** Revision signal rests on n=1 analyst at a 5-year horizon; FY2025 EPS is internally inconsistent between the valuation tool and the estimates file. **Low confidence in the revision sub-score.**
- **Liquidity — not a constraint** (large-cap, $11.8B, 124M diluted shares).
- **Sample size caveat:** all factor ranks are computed against a **5-name** comp set. This is not a statistically robust cross-sectional rank — treat "1/5" as "best of a small hand-picked group," not as a universe-wide quintile.
