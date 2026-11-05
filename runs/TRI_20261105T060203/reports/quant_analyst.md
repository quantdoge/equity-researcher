# Quant Analyst

- Symbol: TRI
- Elapsed: 100.7s

---
## TRI — Thomson Reuters Corp. | Quantitative Factor Report
**Price $117.23 (04-Nov-2026) · Mkt cap $52.7bn · EV $54.2bn · Sector: Industrials / Specialty Business Services**

**Data integrity note (read first):** I reconciled three conflicting feeds. The raw OHLCV series is *corroborated* by the independent analyst price-target feed (2026-05-08 @$93.37, 2026-08-06 @$98.61, 2026-10-13 @$105.32 vs. my series' closes), so **OHLCV is the reliable source**. The system's beta/alpha/Sharpe outputs are **not** — beta 0.013 (R²=0.000) and 0.126 (R²=0.001) over 252d/504d are mechanically impossible for a large-cap vs. SPY. Alpha flips +17.3% (252d) to −25.2% (504d). I recompute from raw prices below and flag the tool values as unusable.

### 1. Factor Scores
| Factor | Score (0–100) | Rank vs. own 5-yr history | Signal |
|---|---|---|---|
| Value | **22** | ~15th pct (expensive) | Negative |
| Momentum | **18** | ~10th pct | Negative |
| Quality | **52** | ~45th pct | Neutral |
| Low Vol | **6** | ~2nd pct | Strongly negative |
| Earnings Revision | **33** | low confidence | Negative |

*Sector rank n/a:* the feed's peer set (GE, CAT, RTX, UNP, DE, BA, LMT, ETN) is aerospace/rail/machinery — not comparable to subscription information services. True comps (RELX, VRSK, FDS, MSCI, WKL) are absent. Ranks above are time-series percentiles.

**Value — expensive on every lens:** P/E 34.5x (GAAP, $3.40 EPS), forward P/E 28.6x (FY26E $4.10), EV/EBITDA 17.8x, P/FCF 25.7x, P/B 4.4x. Against revenue growth of just **+3.0%** (2025 $7.476bn vs $7.258bn) and EBITDA flat ($3.05bn vs $3.05bn), the multiple is unsupported by growth. Only the 2.9% dividend yield is supportive.

**Momentum — decisively negative (raw-data recompute):** trailing 12M **−18.0%** (142.96 → 117.23); 12-1 momentum ≈ **−27%**; peak-to-current **−43.7%** from the $208.19 high (14-Jul-2025). The system's −3.25% (12-1) and −6.65% (6M) materially *understate* the weakness and conflict with OHLCV — use my figures. Offsetting: a genuine **+45.1% rebound** off the $80.80 trough (20-Feb-2026), and 6M total return ≈ +25%.

**Quality — mixed, cash-backed but decaying:** ROIC 14.2% (stable: 10.9→14.0→16.0→14.2), gross profit/assets 0.316, accruals ratio **−6.7%** (excellent — operating CF $2.70bn vs net income $1.50bn), Piotroski **F=7/9** (misses on ROA improvement and equity issuance). But ROE collapsed 24.4%→12.6% and net income fell **−44% in two years** ($2.695bn → $2.210bn → $1.502bn) on rising D&A ($930m vs $822m) and interest. The system's "quality_signal: low" is driven by the falling ROE, not by accruals.

**Low Vol — worst-in-class:** annualised vol **57.7%**, max drawdown **−61.2%** (peak-to-trough). This is a high-beta-risk profile, not a defensive compounder. (System reported −34.68% MDD; my full-window figure is worse.)

**Earnings Revision — low confidence, negative tilt:** the system's +13.9% "upgrade" compares FY2028 EPS ($5.494 vs $4.824) on **1 analyst** — statistically meaningless. FY2026E $4.10 (6 analysts) vs FY2025 $3.40 GAAP; revenue estimates stable at +3%. The real revision signal is in targets: **Goldman $178→$111 (−38%)**, **Barclays $210→$170→$130**, **UBS $215→$183**, **Scotia $156→$138→$135**, **Morgan Stanley $116→$110** — a relentless, still-unfinished downgrade cycle.

### 2. Price Statistics (recomputed from OHLCV)
| Metric | Value | Comment |
|---|---|---|
| Beta vs SPY | **not estimable** | System: 0.013 / 0.126, R²≈0. Assume 0.6–0.8 industry proxy |
| Alpha (ann.) | **not estimable** | System flips +17.3% / −25.2% |
| Trailing 12M return | **−18.0%** | 142.96 → 117.23 |
| Annualised vol | **55–58%** | High but credible given crash+recovery |
| Sharpe | **≈ −0.33** (12M) | System's **+1.06** is a window artifact (anchored near the Feb-2026 low, where return ≈+62% ann.) |
| Sortino | **≈ −0.4 to −0.5** (12M) | System's +1.82 same artifact |
| Max drawdown | **−61.2%** | $208.19 → $80.80 |
| Return since trough | **+45.1%** | $80.80 → $117.23 |

### 3. Composite Quant Signal: **SELL** (composite ≈ 28/100)
Four of five factors are negative: negative momentum, expensive value on 3% growth, highest-decile volatility, and a downgrade cycle that has not stabilised. Not a *Strong Sell* because cash conversion is excellent (accruals −6.7%, F=7) and the multiple has already compressed ~40% from peak. This is a **broken-momentum, de-rating story**, not a balance-sheet failure.

### 4. Key Quant Risk Flags
1. **Momentum reversal risk — two-sided.** A −61% drawdown followed by +45% off the low creates a violent reversal regime; 12-1 momentum is measured *across* the crash and is a poor forward predictor here. Expect continued high dispersion.
2. **Beta/Sharpe/alpha are corrupted** — do not feed these into any factor model. R²≈0 vs SPY is diagnostic of a broken benchmark join.
3. **Analyst target dispersion $85–$183** (median ≈$130, ~+11% vs spot) — extreme disagreement, low signal-to-noise.
4. **Estimate quality thin:** FY2028 consensus rests on **1 analyst**; the "upgrade" is noise.
5. **Corporate action / series continuity:** TRI announced a $600m buyback + $605m return of capital **with share consolidation** (26-Feb-2026). A consolidation distorts unadjusted price series — verify split-adjusted history before any backtest.
6. **Low float / control block:** Woodbridge ownership concentrates voting power and depresses free float, inflating measured volatility and degrading liquidity-adjusted factor validity.
7. **Earnings decay:** net income −44% over two years while EBITDA is flat — D&A and interest are absorbing the operating line. Watch FY2026 margins.
