# Quant Analyst

- Symbol: MSTR
- Elapsed: 35.7s

---
## MSTR (Strategy Inc.) — Quantitative Factor Report
*Data note up front: the feeds disagree with each other. Verifiable price history (2024-06→2026-03-31, close \$124.80) is material to several conclusions, and I reconcile the tool outputs against it below rather than passing through contradictory numbers.*

### 1. Factor Scores

| Factor | Score (0–100) | Sector Rank | Signal |
|---|---|---|---|
| Value | 45 | n/a (see note) | Neutral / Distorted |
| Momentum | 18 | Bottom quintile | **Negative** |
| Quality | 10 | Bottom decile | **Strongly Negative** |
| Low Vol | 3 | Bottom decile | **Strongly Negative** |
| Earnings Revision | 15 | n/a | **Negative (tool signal is an artifact)** |

**Value — 45.** P/E −6.34, EV/EBITDA −6.32, P/FCF −252.3: all meaningless because earnings, EBITDA and FCF are negative. The only usable datapoint is **P/B 0.56** (BVPS \$173.62 vs reported price \$96.50) — or **0.72** using the price-history close of \$124.80. Either way the equity trades *below* stated book, unusual for MSTR and a genuine value flag (mNAV < 1). Score held at neutral, not "cheap," because the earnings-based legs of the factor are uncomputable.

**Momentum — 18. ⚠ Data conflict, resolved against the tool.** `calculate_momentum_score(252d)` returns **+46.64%**. That is not reproducible from the raw series: close on 2025‑03‑31 was \$288.27; the 12‑1 endpoint (≈2026‑03‑02) was \$137.65 → **12‑1 momentum ≈ −52%**. Full 12‑month return \$288.27 → \$124.80 = **−56.7%**. 3‑month momentum (tool, consistent with history) **−10.81%**. I use the history-derived figures.

**Quality — 10.** ROE **−7.54%**, ROA −6.24%, ROIC −0.07%, gross profit/assets **0.0053** (Novy-Marx quality essentially nil). **Piotroski F-Score 3/9 — Weak.** Only credits: negative accruals (−0.0613, the one genuine positive), lower leverage, positive equity change. Zero for positive ROA, positive operating cash flow (OCF **−\$67M**), and **zero for no-dilution** — dilution is the defining feature of this capital structure.

**Low Vol — 3.** Annualised vol **79.5%**, beta vs SPY **2.89** (5Y reported beta 3.61), max drawdown 57.99% as computed. This is the least "low-vol" large cap in the market.

**Earnings Revision — 15. Reject the "+468% upgrade" signal.** The score compares the FY**2029** estimate (\$100.57) to the FY**2028** estimate (\$17.71) — *different forward periods*, and FY2029 rests on **1 analyst** with a \$29.6bn net-income estimate against \$476M of revenue. That is a period-rollover artifact, not a revision. The real near-term revision path is adverse: **FY2026 consensus EPS −\$5.93** (range −31.90 to +21.11) versus FY2025 +\$16.51, with FY2026 EBITDA −\$1.45bn.

### 2. Price Statistics

| Metric | Value | Note |
|---|---|---|
| Alpha vs SPY (252d) | **−41.9%** annualised | R² 0.278 |
| Alpha vs QQQ (252d) | **−36.0%** annualised | R² 0.249 |
| Beta vs SPY | **2.908** | vs QQQ 1.726 |
| Volatility | 79.5% | vol(504d) 75.6% |
| Sharpe (252d / 504d) | **−0.105 / −0.894** | 504d: ann. return −67.6% |
| Sortino (252d / 504d) | **−0.215 / −1.635** | downside dev. dominates |
| Max drawdown | −58.0% (tool) vs **−74%** (verified) | \$416.92 (2025‑05) → \$106.99 (2026‑02‑05) |
| Correlation | COIN **0.81**, MARA 0.54, RIOT 0.45, SPY 0.52 | crypto-complex factor, not software |

Only **25–28% of variance is market-explained**, yet beta is ~2.9 — the residual 72% is idiosyncratic crypto/leverage factor risk, not diversifiable in any practical sense because it is the entire thesis.

### 3. Composite Quant Signal

**SELL** (composite score 18/100; weights: quality 25%, momentum 25%, value 20%, low-vol 15%, revisions 15%).

No factor in the top half of its distribution. The one offset is price-to-book below 1.0 plus negative accruals — a balance-sheet/accounting-quality argument, not a factor-model argument. Quantitatively this is a high-beta, negative-alpha, heavily dilutive asset whose return stream is 81% correlated to COIN and 52% to SPY with an R² of 0.28, i.e. you are paid no diversification for the vol.

### 4. Key Quant Risk Flags

1. **Data integrity / as-of mismatch (highest priority).** Price appears as \$96.50 (market cap \$28.4bn, 294M diluted shares) in the valuation feed but \$124.80 on 2026‑03‑31 in the price feed (profile market cap \$38.9bn). Momentum (+46.6%) and 252d annualised return (−8.36%) are both irreconcilable with the raw series (−52%/−57%). **Trade sizing decisions should not rely on the stale-feed multiples.**
2. **Momentum reversal risk — already realised.** −56.7% over 12 months, −10.8% over 3 months, currently 16.6% off the \$106.99 low and 70% below the 12-month high. Trend is down with high volatility of the trend itself.
3. **Factor crowding in the crypto-beta complex.** 0.81 correlation to COIN means any dedicated quant allocation here duplicates crypto exposure at ~2.9 beta and 79% vol.
4. **Piotroski 0 for no-dilution.** Share count growth plus negative OCF is the mechanical driver of the persistent negative alpha; book value per share is a moving target.
5. **Analyst coverage too thin for inference.** 6 price targets (median **\$209.5**, +68% vs \$124.80) but posted at \$130–151 spot levels, and EPS estimates span 1–6 analysts with ranges wider than the estimate (−\$31.90 to +\$21.11 for FY26). **Sample sizes are too small for statistical significance** — treat consensus as noise, not signal.
6. **Peer/sector rank unavailable.** The vendor maps MSTR to Technology/Software and returns AAPL, MSFT, NVDA as "peers" — not economic comparables. No valid cross-sectional factor rank can be computed; the cohort ranks above are directional judgements, not quintile placements.

**Verdict: Sell.** The only quantitively defensible long case is P/B < 1 (book value ~\$174/share vs price), which is a single datapoint against five factor scores in the bottom decile.
