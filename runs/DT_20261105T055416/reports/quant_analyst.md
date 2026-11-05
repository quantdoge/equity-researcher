# Quant Analyst

- Symbol: DT
- Elapsed: 105.9s

---
## DT — Dynatrace, Inc. | Quantitative Factor Report
**Price $46.78** (close 2026-11-04) | Mkt cap $13.5B | Technology / Software–Application | FY ends Mar-31

### 1. Factor Scores Table

Sector rank = position among 4-name application-software comp set (DT, DDOG, ESTC, MSFT). The tool's default "Technology" peer list is mega-cap semis/hardware (AAPL, NVDA, TSM, AVGO) — not valid comparables for a $13.5B observability vendor, so I built a like-for-like set instead.

| Factor | Raw metrics | Score (0–100) | Rank / 4 | Signal |
|---|---|---|---|---|
| Value | P/E 86.6 · P/B 5.35 · EV/EBITDA 40.1 · P/FCF 26.5 (FCF yield 3.8%) · div 0% | 42 | 2 | **Negative** — expensive on earnings; only FCF yield defensible |
| Momentum | 12-1 return **+36.2%** (252d, excl. last 21d) | 72 | 3 | **Positive but stale** — window ends ~Oct 5, pre-dating collapse |
| Quality | ROE 6.2% · GP/assets 37.3% · accruals **−0.090** · ROIC 9.5% · F-score 6/9 | 45 | 3 | **Neutral** — low ROE, but best accruals in the set |
| Low Vol | Ann. vol **49.4%** · beta 0.56 · R² 0.023 | 25 | 4 | **Negative** — high absolute vol; "low beta" is an artifact |
| Earnings Revision | Fwd EPS 2.630 vs 2.671 prior = **−1.5%** (n=1 analyst) | 45 | n/m | **Neutral / not measurable** — statistically meaningless sample |

**Peer detail (value/quality):** DDOG 629x P/E, 338.7x EV/EBITDA, 68.6x P/FCF, ROE 2.9%; ESTC 26.2x, 254.8x, 29.9x, ROE 28.8%, quality "high"; MSFT 31.0x, 20.2x, 61.8x, ROE 30.2%. DT is cheaper than DDOG on all three multiples and cheaper than MSFT on EV/EBITDA and P/FCF — but more expensive than ESTC on earnings multiples and materially weaker on ROE. **Momentum peers:** ESTC +49.9%, DT +36.2%, MSFT +34.9%, DDOG +8.2%.

**Quality nuance:** the "low" quality label is driven by ROE falling 18.45% (FY25) → 6.23% (FY26), but net income fell $483.7M → $162.7M while operating cash flow *rose* $459.4M → $559.4M — FY25 was inflated by a one-off tax item. Cash-based quality is improving; ROIC is up 6.65% → 9.51%. The screener penalizes DT for an accounting base effect.

### 2. Price Statistics (252d window, benchmark SPY)

| Metric | Value | Note |
|---|---|---|
| Alpha (annualised) | **+22.2%** | **Not significant** — SE ≈ 48pp, t ≈ 0.46 |
| Beta | **0.565** | R² = 0.023 → 97.7% idiosyncratic; beta ≈ 0 |
| R² | 0.023 | Profile beta 0.769 (different window); both unreliable |
| Annualised vol | 49.4% | High absolute; ~3x a typical large-cap |
| Annualised return | 56.0% | Realised, window-specific |
| Sharpe | **1.16** | Alternative longer window gives **0.62** (see §5) |
| Sortino | **1.52** | Implied downside dev ≈ 36.9% |
| Max drawdown | **−28.3%** | Peak close 65.25 (10-12) → 46.78 |

### 3. Composite Quant Signal: **NEUTRAL** (composite ≈ 45/100, negative tactical bias)
No factor is strongly positive. Value and low-vol are clearly negative; quality and revisions are neutral; momentum is positive but **the signal is backward-looking** — the 12-1 window ends before the recent break. A 2-of-5 negative, 1-of-5 positive configuration does not clear the bar for Buy. Price has already de-rated ~29% from the October peak, so the "sell" case is partly priced, but no factor yet supports adding.

### 4. Key Quant Risk Flags

1. **Momentum reversal risk — highest priority.** The +36.2% 12-1 score is computed excluding the last 21 trading days. Since that cutoff: 62.81 (10-28) → 46.78 = **−25.5%**, including a **−14.7% gap on 2026-11-03** (open 46.00 vs prior close 55.13) on 22.6M shares, ~3.4x average volume. At the next rebalance the momentum factor flips sharply negative. Do not treat the positive momentum reading as live.
2. **Idiosyncratic risk dominates.** R² 0.023 means 97.7% of variance is company-specific. Beta hedging is ineffective; alpha "outperformance" is indistinguishable from noise (t ≈ 0.46). No statistical basis to claim skill or market-neutral exposure.
3. **Estimate revision signal is unusable.** The −1.5% revision is against a single analyst's FY2031 estimate. Only the FY2026/FY2027 periods have real coverage (20 and 9 analysts). Directionally, FY27 consensus $1.9067 vs FY26 $1.6835 implies **+13.3% EPS growth**, and October price targets were being *raised* (median ~$73.5 across 10 notes) before a Nov-4 cut to $65 — the revision trend has just inflected down. Treat as neutral-to-deteriorating, not measurable.
4. **Valuation de-rating risk remains.** Even after −29%, trailing EV/EBITDA is 40x and P/E 87x. On FY27 consensus ($1.91 EPS, $688M EBITDA) that is ~24.5x earnings and ~18.9x EBITDA — reasonable, but contingent on hitting estimates that are now being trimmed. The gap-down implies guidance disappointment; multiples can compress further.
5. **Conflicting risk statistics.** Sharpe is 1.16 on the 252-day window but 0.62 on the longer window from the low-vol calc — a large discrepancy signalling that trailing-year performance is not representative. Longer-window Sharpe <1 is the more conservative estimate for sizing.
6. **Liquidity: not a flag.** $13.5B cap, ~6M shares/day typical turnover. Position sizing unconstrained.

### 5. Data Gaps
- Broad "Technology" sector ranks not computed; ranks are against a 4-name software comp set (small n — indicative, not statistically robust).
- Price history between 2026-01-06 and 2026-08-04 was truncated in the feed, so the 52-week low is "≤$41.55" (Jan 2, 2026), not confirmed.
- No 3-month-prior consensus snapshots for FY2026/FY2027, so a proper revision delta could not be constructed; only the single-analyst FY2031 pair was available.
- Consensus target median (~$73.5) is stale — struck when DT traded in the low-$60s; only the Nov-4 Needham note ($65) is near current price.
