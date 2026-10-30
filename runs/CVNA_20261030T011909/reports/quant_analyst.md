# Quant Analyst

- Symbol: CVNA
- Elapsed: 80.7s

---
## CVNA — Quantitative Factor Profile
*Carvana Co. · Consumer Cyclical / Auto–Dealerships · Price $67.32 (2026‑02‑20) · Mkt cap ≈$76.6B (diluted)*

### ⚠️ Data-integrity preface (read before the table)
Four input defects materially affect the raw factor outputs; I have corrected where defensible and flagged where not.

| Issue | Evidence | Treatment |
|---|---|---|
| **EV/EBITDA = −721x is corrupt** | FY25 EBITDA field printed at **−$110M** while operating income is **$1.881B** and D&A **$275M** (gross profit $4.192B − SG&A $2.308B ✓) | Implied EBITDA ≈ **$2.16B** → **EV/EBITDA ≈ 36.7x** |
| **Momentum module inconsistent with OHLCV** | Tool: 12‑1 = **+0.46%**, 6‑1 = −14.75%. Raw series implies **+97.4%** (46.10 → 91.00) and **+33.2%** (68.31 → 91.00) | Report both; **peer-relative rank is robust** (all peers negative) |
| **Revision factor uses a 2030 stub** | forward_period "2030‑12‑31", EPS $2.85 vs $2.59 | Low information content; cross-checked vs. price targets |
| **Diluted share gap** | 688.2M basic vs **1,121.4M diluted** (converts); diluted EPS 1.69 ≠ NI/shares (1.25) | Use diluted (conservative); dilution is itself a flag (F‑score item F7 = 0) |

---

### 1. Factor Scores

| Factor | Score | Sector Rank* | Signal |
|---|---|---|---|
| **Value** | P/E 40.4x · P/B 18.2x · EV/EBITDA 36.7x (corr.) · P/FCF 86.2x | **7 / 7** | **Strong Negative** — most expensive in comp set on every multiple |
| **Momentum** | 12‑1: **+0.46%** (tool) / **+97.4%** (raw) · 6‑1: −14.75% (tool) / +33.2% (raw) | **2 / 7** | **Positive but reversing** — see decay |
| **Quality** | ROE 33.5% · ROIC 19.3% · GP/A 0.318 · Accruals 0.028 · F‑score 6/9 | **2 / 7** | **Positive** — best ROE in group, but accruals only 6th |
| **Low Vol** | Vol 62.3% · β 2.10 (1Y daily) / 3.55 (5Y monthly) · Max DD −41.2% | **7 / 7** | **Strong Negative** — worst in group on both axes |
| **Earnings Revision** | +10.04% (2.59 → 2.85) on a 2030 stub | n/a | **Neutral / unreliable** — 6 of 8 recent PT actions were *cuts* (Barclays 93→80, Stephens 91.5→83, MS 90→88, Wells 80→75); only DB and UBS nudged up |

*\*Peer set = CVNA, KMX, AN, ABG, PAG, LAD, ACVA (n=7). **Small-sample caveat: at n=7 a "rank" is 1–2 names wide; treat as ordinal color, not a statistically meaningful z-score.** The sector identifier returns mega-cap Consumer Cyclical (AMZN, TSLA, HD) which are not economic comps — I substituted auto retail/adjacent names.*

**Supporting peer cross-section**

| | CVNA | KMX | AN | ABG | PAG | LAD | ACVA |
|---|---|---|---|---|---|---|---|
| P/E | 40.4 | 33.4 | 9.9 | 7.9 | 15.0 | 9.2 | n.m. |
| EV/EBITDA | 36.7* | 16.1 | 10.5 | 9.9 | 13.4 | 9.5 | n.m. |
| ROE % | **33.5** | 4.2 | 27.7 | 12.6 | 16.8 | 12.4 | −15.4 |
| GP/A | 0.318 | 0.106 | **0.344** | 0.261 | 0.284 | 0.228 | 0.434 |
| Accruals | 0.028 | −0.058 | 0.037 | −0.024 | −0.002 | 0.018 | −0.133 |
| 12‑1 Mom % | +0.5 / +97* | −2.7 | −19.9 | −20.1 | −4.8 | −9.8 | **+51.5** |

*Note CVNA's quality is genuine — ROE 33.5% on a business that went 15.3% → 33.5% in one year with revenue +48.6% ($13.7B → $20.3B) and ROIC 19.3%. But it is bought at 36.7x EBITDA and 18x book versus peers at 9–16x and 1–3x. Quality is real; it is not cheap.*

---

### 2. Price Statistics (252 trading days, vs SPY)

| Metric | Value | Read |
|---|---|---|
| Annualized return | **−5.81%** | Negative absolute return in a strong tape |
| Annualized volatility | **60.5%** (62.3% alt calc) | ~3.8x market |
| Beta vs SPY | **2.114** (R² 0.192) | 5Y monthly β 3.548 |
| **Alpha (annualized)** | **−53.2%** | **t ≈ −1.0 → NOT statistically significant** |
| R² | 0.192 | Only 19% of variance is market — 81% idiosyncratic |
| **Sharpe** | **−0.096** | Return does not compensate for risk |
| **Sortino** | **−0.166** | Worse on downside-only basis |
| Max drawdown | **−41.2%** | Occurred Feb–Apr 2025 (54.23 → 32.51) |
| Current drawdown | **−29.5%** from $95.54 peak (2026‑01‑27) | Active reversal |
| YTD 2026 | **−20.2%** (84.40 → 67.32) | Momentum breaking down |

**On the alpha:** −53% is a large number but statistically fragile. With 60% vol, R² of 0.19 and 252 observations, the standard error on annualized alpha is roughly ±54%, giving **t ≈ −1.0**. The economically meaningful statement is narrower: *at a beta of 2.1, the market's rise should have delivered CVNA ~+30–45%; it delivered −5.8%. That ~35–50pt give-back is the real signal*, and it is corroborated by the 6‑1 deceleration and the −29.5% break since January. Do not present −53% as a precise estimate.

---

### 3. Composite Quant Signal: **NEUTRAL (High Risk)** — not investable on pure quant grounds

Equal-weight quintile blend of the four scored factors: **z ≈ −0.24 → Neutral**.

- **+ Quality (2/7)** and **+ Momentum (2/7)** are the only two supportive legs.
- **− Value (7/7)** and **− Low Vol (7/7)** are disqualifying: the two worst readings in the group, and they are *not* offset by cheapness.
- Momentum is the leg I would weight **lowest right now**, not highest: the trailing factor reading is positive, but the live series has broken −29.5% in 17 sessions on elevated volume (88.7M shares on 2026‑02‑19 vs ~12M typical). That is the signature of **factor crowding unwinding**, not accumulating.

**Conclusion: rank behind AN and KMX on a risk-adjusted basis.** AN offers 9.9x P/E, 27.7% ROE, 0.344 GP/A — better quality *at one-quarter the multiple*.

---

### 4. Key Quant Risk Flags

1. **Momentum-reversal risk — active, not hypothetical.** Stock is −29.5% from its 27‑Jan peak and −20.2% YTD; the 12‑1 reading (+0.46% tool / +97% raw) is a *stale* positive. Six of eight recent price-target actions were cuts. 5.5x average volume on the 2026‑02‑19 down day confirms institutional distribution.
2. **Extreme beta / vol regime.** β 2.10 daily, 3.55 monthly, vol 60–62%, 41% max DD. Position sizing, not conviction, is the binding constraint.
3. **Valuation has no cushion.** 18.2x book and 86x FCF price in flawless execution of a +48.6% revenue year. Any deceleration reprices both earnings and multiple.
4. **Earnings-quality / dilution flag.** F‑score 6/9 with **F4 (accruals) = 0** and **F7 (no dilution) = 0**; diluted shares 1.121B vs 688M basic — convertible overhang is large and the diluted-EPS figure doesn't reconcile to net income. CFO < net income.
5. **Liquidity is fine, data quality is not.** Dollar volume ~$1–2B/day — no liquidity constraint. But four separate feed defects (EBITDA, momentum, revision horizon, share count) mean this name should be **re-verified against filings before any sizing decision**.
6. **Sample-size caveat:** n=7 peer set, 252 daily obs, R² 0.19. Sector ranks are ordinal color; the alpha t-stat is ~−1.0. Nothing here clears conventional significance except the volatility and valuation levels, which are unambiguous.
