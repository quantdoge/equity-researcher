# Quant Analyst

- Symbol: NBIX
- Elapsed: 76.8s

---
## NBIX — Neurocrine Biosciences | Quant Factor Report
Price $166.05 (4-Nov-2026) · Mkt cap $16.8B · Healthcare / Biotechnology · ADV ≈1.2–1.5M sh (~$200M/day)

### 1. Factor Scores
| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| Value | 55 / 100 | 2nd of 5 on P/FCF; 3rd on P/E & EV/EBITDA | Neutral |
| Momentum | 42 / 100 | Bottom-half on 12-1; top-quartile on 6-mo | Neutral (improving) |
| Quality | 78 / 100 | 1st of 5 on gross-profit/assets; 2nd on accruals | **Positive** |
| Low Vol | 30 / 100 | Highest absolute vol in cohort; low beta | Negative |
| Earnings Revision | 72 / 100 | Upgrade, +9.64% | **Positive** |

**Value detail:** P/E 35.56 · EV/EBITDA 23.93 · P/B 5.23 · P/FCF 22.73 (FCF yield 4.40%) · no dividend.
Peer cohort (GILD, AMGN, ABBV, LLY): P/E 25.7 / 33.6 / 124.4 / 61.8 · EV/EBITDA 17.3 / 18.0 / 33.3 / 41.3 · P/FCF 23.2 / 32.0 / 29.4 / 141.9. NBIX is at/below peer medians on every cash-flow multiple. Critically, the trailing 35.6x P/E is misleading: on consensus the stock is **17.0x 2027E EPS (9.78)** and **13.7x 2028E (12.08)** — implied 2025→2028 EPS CAGR 37%, PEG ≈0.95. Forward value is the strongest leg of the value case.

**Quality detail:** ROIC 16.9% (2025) vs 18.7% / 9.4% / 12.6% (2024/23/22) — improving; ROE 14.7%. Gross profit/assets **0.606** (highest in cohort: LLY 0.481, GILD 0.393, ABBV 0.321, AMGN 0.287). Accruals **−0.066** (CFO $782.7M vs NI $478.6M = 164% cash conversion), negative accruals 4 straight years. Piotroski F-score **7/9** (misses only on gross-margin and asset-turnover improvement). Note: the factor tool tags quality "low" purely off ROE percentile — headline ROE understates quality here because peers' ROEs (AMGN 89%, LLY 78%, ABBV −131%) are distorted by buyback-thin equity and impairments. On the metrics that actually predict returns (GPA, accruals, ROIC), NBIX is top-quartile.

**Revision detail:** FY2030E EPS 13.876 vs 12.656 three months prior = **+9.64%**. But only 8 analysts cover FY2030, with a 13.13–15.35 range — low confidence. Deeper years are better populated (FY2028: 18 analysts, FY2027: 14) and imply $4.54B→$5.52B revenue 2027→2030 (~7% CAGR). Street price targets: median **$214** (range 183–224), +28.9% vs spot; the two most recent (Guggenheim $224, Cantor $215, both Nov-2026) are at the top of the range.

### 2. Price Statistics
| Metric | Value |
|---|---|
| Alpha vs SPY (ann., 252d) | **+25.28%** — *not significant* (R² 0.052, t ≈ 0.7) |
| Alpha vs XBI (ann., 252d) | +15.96% — *not significant* (R² 0.228, t ≈ 0.5) |
| Beta vs SPY | 0.628 (1y daily); 0.625 (low-vol calc); 0.362 (profile, 5y monthly) |
| Beta vs XBI | 0.570 |
| Annualised vol | 36.37% (Sharpe calc: 36.86%) |
| Sharpe (0% rf, reported) | 0.776 |
| Sortino (0% rf, reported) | 1.062 |
| Max drawdown (252d) | **−27.15%** (peak $185.50 30-Jul-26 → $135.13 13-Oct-26) |
| Realised return, 1y geometric | +15.96% (YTD +17.08%) |
| Return path | 12-1 mo **+1.6%** · 6-mo +23.9% · 3-mo 0.0% · last 21d **+14.1%** |

**Important methodology flag:** the Sharpe tool's 28.58% "annualised return" is an arithmetic (mean×252) figure that embeds ~6.8% variance drag; the geometric 1-year return is +15.96%. On a geometric basis Sharpe is **≈0.43**, not 0.78. Sortino/Sharpe of 1.37 indicates mild positive skew. Similarly, the momentum factor tool returned −21.53% (12-1) and −8.48% (6-1); recomputing directly from OHLCV gives **+1.62%** and **+23.85%**. The tool's figure reproduces the 30-Jul peak → 6-Oct trough leg (−21.6%) and appears to exclude the 3-Nov earnings jump. I have used my own computation; treat the tool's momentum signal as stale.

### 3. Composite Quant Signal: **NEUTRAL (leaning Buy)**
Weighted composite **58.4/100** (Value 20%, Momentum 25%, Quality 25%, Low-Vol 10%, Revision 20%). Two genuine positive legs (quality, revisions) and a de-risked forward multiple are offset by high absolute volatility and a momentum record that is flat over 12 months and driven almost entirely by one event day. This is not a factor-crowded multi-factor top-quintile name: it scores top-quintile on quality only, not on value + momentum + quality jointly. Upgrade to **Buy** on (a) two consecutive quarters of upward EPS revisions with expanding analyst counts, and (b) price holding above the $160 breakout with 12-1 momentum turning positive.

### 4. Key Quant Risk Flags
1. **Alpha is statistically insignificant.** With R² of just 5.2% vs SPY (77% idiosyncratic), the 25% "alpha" has a t-stat near 0.7 — indistinguishable from noise. Do not attribute the trailing outperformance to a repeatable edge; this is a single-name binary-risk asset, not a beta-managed position.
2. **Momentum reversal / event concentration.** +14.1% in 21 days (13% on 3-Nov earnings, 4.1M shares vs 1.2M ADV) is event-driven, not trend. The stock remains 10.5% below its July high. Signals computed before 3-Nov are stale — a classic setup for post-gap reversal.
3. **Volatility/left tail.** 36% annualised vol with a −27.2% drawdown inside 12 months. Low beta (0.63) materially understates risk: 2026 saw a −27% drawdown while the market rose. Size on vol, not beta.
4. **Beta estimate instability (0.36 → 0.63).** Profile beta (5y monthly) is half the 1-year daily beta. Hedge ratios and any beta-neutral sizing are model-choice sensitive.
5. **Single-asset revenue concentration (INGREZZA)** — the quality metrics are strong but the durability of the earnings stream is pipeline/regulatory contingent; accruals and F-score say nothing about patent-cliff timing.
6. **Thin revision sample.** 8 analysts on FY2030, range 13.13–15.35 (±8% around the estimate). The +9.64% revision is directionally informative, not statistically robust.
7. **Peer set mismatch.** The available "Healthcare" peer list is mega-cap diversified pharma/medtech (LLY, JNJ, ABBV, MRK, UNH, NVS…), not mid-cap biotech. Sector ranks above are indicative, computed against a hand-built 5-name cohort (NBIX, GILD, AMGN, ABBV, LLY); a true XBI-based cross-section would likely rank NBIX more favourably on quality and would change the value rank. Liquidity is *not* a constraint (ADV ~$200M/day).
