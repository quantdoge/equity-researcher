# Quant Analyst

- Symbol: AXON
- Elapsed: 34.0s

---
## AXON — Quantitative Factor Report
**Spot $390.29 (2026-10-16) | Mkt cap $31.7B basic / $39.0B diluted | A&D peer set n=5**

### 1. Factor Scores

| Factor | Score (0–100) | Sector Rank | Signal |
|---|---|---|---|
| Value | 2 | 5 / 5 | **Strong negative** |
| Momentum (12-1) | 3 | 5 / 5 | **Strong negative** |
| Quality | 42 | 3 / 5 | Neutral (bifurcated) |
| Low Vol | 2 | 5 / 5 | **Strong negative** |
| Earnings Revision | 65 | n/a (not gathered) | Positive — **low confidence** |

Scores are percentile-style vs. the A&D peer set (AXON, GE, RTX, LMT, BA); 50 = peer median.

**Value — rank 5/5, decisively last.** P/E 258.5x, EV/EBITDA 199.8x, P/FCF 519.8x, P/B 12.03x. Peers: LMT 25.7x/16.7x/18.5x, RTX 39.1x/19.7x/33.1x, GE 38.5x/28.4x/46.1x, BA 76.7x/23.1x/neg. AXON trades at 7–12x the peer multiple on EV/EBITDA. On forward numbers it is less extreme but still rich: 50.8x FY26E EPS ($7.69), 36.8x FY27E ($10.60), 28.3x FY28E ($13.79) — i.e. ~35% EPS CAGR is already capitalized at a PEG ≈ 1.45.

**Momentum — rank 5/5, last, and deteriorating monotonically.** 12-1: **−23.07%**; 6M: −27.26%; 3M: −13.61%. The decline is *accelerating*, not stabilizing, and the excluded trailing month added roughly −12% (Sep 15 $442 → Oct 16 $390). Peak-to-trough: $665 intraday (7 Jul) → $390, ≈ **−41%**, against a 52-week max drawdown of 46.07%. No reversal signal on any horizon.

**Quality — rank 3/5, internally contradictory.** Gross profit/assets **0.2369 is the best in the peer set** (Novy-Marx profitability is genuinely strong), and accruals are negative (−0.0123; net income $124.9M vs. OCF $211.3M — clean cash conversion). But ROE has collapsed **16.2% (2024) → 3.85% (2025)** and ROIC **1.57% → −1.20%**. FY2025 operating income was **−$62.1M** on $2,779.5M revenue (SG&A $1,033.4M); net income stayed positive only via non-operating items. Piotroski F-score **5/9**, with failures on ROA improvement, leverage, dilution, and asset turnover.

**Low Vol — rank 5/5, last.** Annualised vol **67.0%**, beta **1.568** vs. SPY (profile beta 1.44). Peers: RTX 26.4%/0.18, LMT 29.3%/−0.10, BA 33.8%/1.23, GE 34.6%/1.24. AXON's volatility is ~2x the next-highest peer.

**Earnings Revision — read this with caution.** The tool reports **+30.16%** (FY28E $13.795 vs. prior $10.598), but the "prior" figure is *numerically identical* to the current FY27E consensus ($10.59828). That is a **period roll-forward artifact, not an analyst upgrade** — the comparison crossed fiscal years. Independent corroboration is genuinely positive but decelerating: Aug 2026 target raises were aggressive (Goldman $535→$715, Barclays $523→$688, Piper $724→$732, MS $600→$640, Argus $460→$600), yet on 15 Oct 2026 **Raymond James cut $800→$675**. Consensus PT (n=6) = **$675, +73% above spot**. Direction of *estimates* remains up; direction of *multiples* is down. Also note only **3 analysts** cover FY2028E — below significance threshold.

### 2. Price Statistics (252d vs. SPY)
- **Alpha (annualised): −63.08%**
- **Beta: 1.577** | **R²: 0.0954**
- **Sharpe: −0.582** | **Sortino: −0.942**
- Annualised return **−39.55%** | vol **67.94%**
- **Max drawdown: 46.07%**

Two critical statistical caveats. **(a) The alpha is not significant.** Implied residual vol = 67.94% × √(1−0.0954) ≈ 64.7%; SE(alpha) over a 1-year window ≈ 64.7%, giving **t ≈ −0.98**. The −63% alpha cannot be distinguished from noise at conventional confidence. **(b)** R² of 0.095 means **~90% of AXON's variance is idiosyncratic** — beta and alpha are poorly identified. Sortino (−0.942) is *better*-behaved than Sharpe implies: implied downside deviation ≈ 42.0% vs. total vol 67.9%, i.e. **positive skew** — a large share of that 67% vol is upward gaps, not drawdown.

### 3. Composite Quant Signal: **SELL**
Weighted composite (Value 20 / Momentum 25 / Quality 25 / LowVol 10 / Revision 20) = **25/100**. AXON is bottom-quintile on three of five factors simultaneously. The upgrade to "Sell" rather than "Strong Sell" reflects: best-in-peer gross profitability, negative accruals, +33% revenue growth ($2.08B → $2.78B), and a positive — if unreliable — revision signal. This is a de-rating story, not a fundamental-breakdown story: the stock is down because the multiple compressed from ~200x to ~50x forward earnings, not because estimates fell.

### 4. Key Quant Risk Flags
1. **Momentum reversal / falling knife.** −23% (12-1), −27% (6M), −14% (3M) with acceleration. No base formation. Trend-following overlays remain short.
2. **Factor crowding — LOW, and that's the point.** Correlation to peers is unusually low: GE 0.20, BA 0.25, RTX 0.15, **LMT 0.06**, SPY 0.31. AXON is not a crowded A&D factor trade; the risk is the *opposite* — unhedgeable idiosyncratic exposure, not sector beta.
3. **Valuation compression risk.** 199.8x TTM EV/EBITDA and 519.8x P/FCF leave no multiple cushion; any FY26/FY27 estimate miss de-rates violently given beta 1.57.
4. **Dilution.** Diluted weighted shares **78.6M (2024) → 100.0M (2025)**, +27%; basic 80.4M vs. diluted 100.0M — a ~24% overhang (convertibles/options). F-score flags this (F7=0). Diluted market cap is ~23% above the headline $31.7B.
5. **Statistical power.** Peer group n=5; window = 1 year; FY28E coverage n=3; alpha t ≈ −1.0. Treat the alpha/beta decomposition and the revision score as indicative only. **Do not anchor a position sizing decision on the −63% alpha.**
6. **Liquidity — not a constraint.** ~0.5–2.8M shares/day (~$200M–$1.1B notional); no flag.

**Bottom line:** AXON is a high-quality-business/low-quality-factor-score name at a still-demanding price. Quant says Sell on the composite; the honest quant read is that the 12-month underperformance is real (−41% from peak) but **not statistically separable from noise in a 1-year sample**, while the value and momentum signals are unambiguous and are not noise.
