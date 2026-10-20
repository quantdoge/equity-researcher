# Quant Analyst

- Symbol: NRG
- Elapsed: 96.8s

---
## ⚠️ Data Integrity Finding (read first)

Two price feeds disagree, and it materially changes every factor score:

| Source | Price | Implied Price→ |
|---|---|---|
| OHLCV feed, last close 2026-02-20 | **$178.00** | — |
| Valuation ratios / factor-score endpoints | **$99.38** | stale (~Jan-2025 level) |
| Profile market cap $20.91B ÷ 199M shares | ~$105 | stale, corroborates $99.38 feed |

The OHLCV series is internally consistent and shows the real tape (117.57 → 148.39 on 2025-05-12, 171.80 → 146.75 on 2025-08-06). So **raw multiples and all return-based tools that report $99.38 are computed off a ~13-month-stale price and are systematically wrong.** I report tool output, then my correction.

## 1. Factor Scores

| Factor | Score (raw / corrected) | Sector Rank | Signal |
|--------|------------------------|-------------|--------|
| Value | P/E 24.8 → **44.4x**; EV/EBITDA 9.0 → **13.8x**; P/FCF 25.8 → **46.2x**; P/B 11.8 → **21.1x**; div yield 1.88% → **1.05%** | **3 of 4** (cheaper than CEG/NEE, but ~20% richer than DUK on EBITDA) | **Negative** (was flattered by stale price) |
| Momentum | 12-1 **+36.9%** (149.23 vs 108.99, ex-last-21d); 12m +63.3%; 3m +12.0% — *tool's −26.19% is stale-series artifact* | **1 of 4** (CEG +4.4%, NEE −8.8%, DUK −6.2%) | **Strong Positive** |
| Quality | ROE 51.4% (vs CEG 15.6 / NEE 10.3 / DUK 9.4); GP/assets **0.230** (best in peer set); accruals **−0.036** (good) | **1 of 4** on raw components | **Positive, with caveat** — tool's "low" label contradicts its own inputs (likely leverage-adjusted); ROIC fell 18.0%→**10.0%**, and 51% ROE is a thin-equity artifact (BVPS $8.45) |
| Low Vol | σ 51.0%, β 1.25, max DD 47.9% (CEG 48.3%/−30.5%, NEE 21.1%, DUK 16.7%) | **4 of 4 — worst** | **Strong Negative** |
| Earnings Revision | +16.86% | n/a (only 4 analysts) | **Weak Positive / low confidence** — see flag |

## 2. Price Statistics

| Metric | Tool output (stale series) | My recompute from OHLCV |
|---|---|---|
| Annualised return | −41.6% | **≈ +77%** (77.57 → 178.00, 1.46 yrs) |
| Alpha vs SPY | −56.7% | **Not credible / clearly positive** — 12m NDX-relative outperformance is large; precise alpha unrecoverable without SPY series |
| Beta vs SPY | 1.252 (R² 0.104) | Consistent with profile β **1.16**; **R² 0.10 means only ~10% of variance is market — alpha estimate is statistically meaningless** |
| Sharpe | −0.814 | **≈ +1.9** (at ~35–40% realized σ) |
| Sortino | −1.111 | **≈ +2.5** (upside/downside skew favourable) |
| Max drawdown | −47.9% | **−25.2%** (111.21 → 83.23, Feb–Mar 2025); recent DD **−19.4%** (176.33 → 142.15, Oct-25→Jan-26) |
| Realised vol | 51.0% | 51% is *directionally* right — genuine 10–26% single-day gaps exist; treat 45–50% as the usable estimate |

## 3. Composite Quant Signal: **NEUTRAL** (was a misleading Strong Sell on stale data)

- Quality and momentum both rank **1 of 4** in the utilities peer set — genuinely strong.
- But at the **live $178**, value ranks 3 of 4 and the stock is at 44x trailing / 13.8x EV-EBITDA / 46x P-FCF. All of the valuation cushion that the $99.38 feed advertised has been consumed by the re-rating.
- Low-vol factor is the worst in sector, and momentum is now the crowded, extended leg.

Upside case rests on the estimate ladder (2027 $11.02 → 2028 $12.81 → 2030 $17.15, ~16% CAGR), which puts 2028 P/E at 13.9x — reasonable, but it is a 2–8 analyst sketch, not a consensus.

## 4. Key Quant Risk Flags

1. **PRICE FEED CONFLICT (highest severity).** 79% gap between feeds. Every multiples-based output in this report required manual restatement; a downstream memo using raw tool output would conclude NRG is cheap at 9x EBITDA when it is at 13.8x.
2. **Momentum reversal / crowding risk.** +37% 12-1 after a 129% run from Sep-2024, with two >19% drawdowns already in the last 12 months. Utilities-momentum crowding is real; the stock gaps (26% on 2025-05-12, −14% on 2026-01-08... −13.6% on 2025-08-06).
3. **Earnings-revision score is not a revision.** The tool compared FY2030 EPS ($17.15) against FY2029 ($14.68) — inter-year growth, not a same-period revision. Only **4 analysts**, range $14.25–$19.88 (±18%). Discount to near-zero information value.
4. **Quality is leverage-financed.** ROE 51.4% on $8.45 BVPS and ROIC declining 18.0% → 10.0% in one year. Piotroski F-score **5/9**, with losses on leverage (F5), equity change (F6), and asset turnover (F9). Not a compounding-quality profile — it's a capital-return story.
5. **Beta estimates from the low-vol tool are unreliable peer-wide** (NEE β 0.053, DUK β −0.312 — impossible for regulated utilities). Do not use those for cross-sectional vol ranking; use the vol/DD columns.
6. **Low R² (0.104)** on the SPY regression: this is an idiosyncratic, event-driven name. Market-beta hedging will not protect a position here.
7. Liquidity is *not* a constraint — ADTV ~2.2M shares (~$390M), no flag.

**Bottom line:** the numbers support quality + momentum, and reject the value case that stale pricing implied. Neutral, not Buy — the price already pays for the growth ladder.
