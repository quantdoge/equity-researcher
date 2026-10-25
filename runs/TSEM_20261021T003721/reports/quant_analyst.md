# Quant Analyst

- Symbol: TSEM
- Elapsed: 29.6s

---
## TSEM — Quantitative Factor Report (Tower Semiconductor)

**Data note:** β from company profile (0.889) is a long-run figure; 1-yr realized beta vs SPY is 3.06 — I use the realized value throughout. Peer ranks below are built on a 5-name analog foundry/large-cap semiconductor set (TSEM, TSM, MU, AVGO, AMD). **n=5 is too small for statistical significance — treat ranks as directional context, not formal quintiles.** TSM's P/E (1.28) and EV/EBITDA (0.05) are ADR/units artifacts and are flagged, not used to rank TSEM as "expensive vs TSM."

### 1. Factor Scores Table

| Factor | Score / Raw Inputs | Peer Rank (n=5) | Signal |
|---|---|---|---|
| **Value** | P/E 94.7 · EV/EBITDA 36.6 · P/B 7.19 · **P/FCF −508 (negative FCF)** | 3rd of 5 | **Negative** — rich multiple, negative FCF yield |
| **Momentum** | 12-1m return **+3.02%** | 4th of 5 (MU +17.0, AMD +16.7, TSM +7.5, AVGO −4.9) | Neutral / weak positive |
| **Quality** | ROE 7.6% · Gross profit/assets 10.9% · Accruals −5.3% (good) | 4th–5th of 5 | **Negative** — lowest ROE and GP/assets in set |
| **Low Vol** | Vol 87.7% · β 3.05 · Max DD 42.0% | **5th of 5 (highest vol, deepest DD)** | **Strongly negative** |
| **Earnings Revision** | Fwd (2029) EPS $14.39 vs $10.49 = **+37.2%** | n/a | **Positive (upgrade)** — but far-dated, thin sample |
| *Piotroski F-Score* | **6 / 9 (Moderate)** | — | Mixed; fails ROA improvement, dilution, margin |

### 2. Price Statistics (252-day window)

| Metric | TSEM | Read |
|---|---|---|
| Annualised alpha (vs SPY) | **+45.87%** | Very large, but... |
| Beta (vs SPY) | **3.06** | Aggressive; 3x market sensitivity |
| R² | **0.21** | Only 21% of variance is market — 79% idiosyncratic |
| Sharpe | **0.96** | Respectable |
| Sortino | **1.68** | Good — downside vol controlled relative to upside |
| Annualised return | **85.6%** | — |
| Annualised vol | **89.0%** | Extreme |
| Max drawdown | **42.0%** | Severe |

### 3. Composite Quant Signal: **NEUTRAL**

The signal is genuinely split, and the numbers argue against conviction either way:
- **Bull case (quant-backed):** +45.9% alpha, +37% forward EPS revision, Sortino 1.68, negative accruals (−5.3% = clean earnings quality).
- **Bear case (quant-backed):** Worst low-vol score in the peer set (89% vol, β 3.06, 42% DD), bottom-quartile quality (ROE 7.6%, GP/assets 10.9%), expensive on EV/EBITDA (36.6) with **negative free cash flow** (P/FCF −508), and only 4th-of-5 momentum.
- **The tell:** a 85.6% annualized return but only a **+3.02% 12-1m momentum** reading means the overwhelming majority of the trailing-year gain is concentrated in the *last 21 trading days*. That is the textbook setup for short-term reversal — the alpha is real but freshly minted and fragile.

Net: strong recent price action + strong revisions, offset by poor value/quality/vol profile. Not a factor-aligned "strong buy." Rated **Neutral**.

### 4. Key Quant Risk Flags

1. **Momentum reversal risk (high):** Momentum strip-out leaves only +3% after excluding the last month while full-period return is +85.6% — extreme recent-date concentration. A 42% max drawdown already exists in-sample.
2. **Factor mismatch / no style tailwind:** TSEM ranks bottom-quintile on *both* quality and low-vol, and mid-pack on value and momentum — it is not aligned with any of the currently rewarded factors. Buying it is a concentrated idiosyncratic bet (R² 0.21), not a factor exposure.
3. **Volatility & beta risk:** 89% annualized vol, β 3.06 → a 10% SPY drawdown implies ~30% TSEM drawdown mechanically. Position sizing must account for this.
4. **Negative free cash flow:** P/FCF −508 and EV/EBITDA 36.6 mean valuation is entirely dependent on the 2029 estimate revision materializing — a far-dated, low-confidence anchor.
5. **Small-sample caveats:** Peer ranking n=5 (not statistically robust); earnings-revision anchor is a single 2029 period, not a multi-quarter revision trend; TSM value inputs are unit artifacts and excluded from relative conclusions.

**Bottom line:** Quantitatively a high-alpha, high-risk idiosyncratic momentum name with weak factor fundamentals. Neutral — would upgrade to Buy only on confirmation of a sustained (not one-month) momentum trend plus positive FCF inflection; would downgrade to Sell on any momentum reversal through the recent breakout.
