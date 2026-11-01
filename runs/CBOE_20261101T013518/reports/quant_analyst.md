# Quant Analyst

- Symbol: CBOE
- Elapsed: 38.8s

---
## CBOE Global Markets — Quantitative Factor Report

**Sector:** Financial Services / Financial – Data & Stock Exchanges
**Price:** $335.53 (valuation source) vs. $286.58 (last OHLCV close, 2026‑02‑20) — **see Risk Flag #1**
**Market cap ≈ $35.0–35.3B | Diluted shares 105.1M | Div yield 0.94%**

### ⚠️ Data Integrity Note (read first)
The derived-statistics pipeline is returning figures that are **internally inconsistent with the clean OHLCV series**. Verbatim: 12‑1 momentum **−4.51%**, 252d vol **40.3%**, 126d vol **46.8%**, beta **−0.60/−1.00**, max DD **36.7%**. From the actual daily closes (2025‑01‑02 $192.75 → 2026‑02‑20 $286.58), I reconstruct:

| Metric | Tool output | Reconstructed from OHLCV | Verdict |
|---|---|---|---|
| Total return (window) | +41.5% ann. | +48.68% total (~41% ann.) | ✅ agrees |
| 12‑1 momentum | −4.51% | **+32.3%** (205.0 → 271.1) | ❌ tool wrong |
| 126d momentum | −13.36% | **+15.3%** (248.6 → 286.6) | ❌ tool wrong |
| Annualized vol | 40.3% | **~19–20%** (59 weekly obs, MAD→σ) | ❌ ~2x overstated |
| Max drawdown | 36.7% | **−14.3%** intraday / **−8.9%** close‑to‑close | ❌ tool wrong |
| Beta vs SPY | −0.598 (R²=0.038) | degenerate; profile 5Y β = **0.41** | ⚠️ not significant |

Bonus diagnostic: the tool reports vol *rising* (40%→47%) as the window shortens, which cannot happen on a smooth series — confirming a corrupted/unadjusted source. **I use reconstructed values below and flag tool figures in parentheses.**

### 1. Factor Scores

| Factor | Score | Sector Rank (of 5) | Signal |
|---|---|---|---|
| **Value** | P/E 32.2 · P/B 6.86 · EV/EBITDA 19.9 · P/FCF 30.6 | **4–5 (bottom quintile)** | **Sell / Bearish** |
| **Momentum** | **+32.3%** 12‑1 (recon.); last 21d +5.7% | **1 (best)** | **Strong Buy** |
| **Quality** | ROE 21.4% · ROIC 22.2% · GP/Assets 0.248 · Accruals −0.013 · Pio F=7 | **1 (best)** | **Strong Buy** |
| **Low Vol** | β ≈ 0.41 (5Y); recon. vol ~19–20% (tool: 40.3%) | **1 (lowest β)** | **Buy** |
| **Earnings Revision** | +4.67% (FY2030, **n=1**) | n/a | **Neutral (no signal)** |

**Value detail:** premium to the exchange median on *every* multiple — P/E 32.2 vs 28.2 median (+14%), P/B 6.86 vs 4.41 (+56%, highest), EV/EBITDA 19.9 vs 17.9 (+11%), P/FCF 30.6 vs 24.3 (+26%, highest), and the lowest dividend yield (0.94% vs CME 3.73%, MKTX 1.89%). Forward P/E 23.6x on FY26E $14.22 (20.2x on the $286.58 close).

**Quality detail:** ROIC 9.2% → 18.9% → 18.7% → **22.2%** (2022→2025) — a genuine, sustained re-rating of returns on capital. Best ROE and GP/Assets in the peer set; cash conversion strong (NI $1.10B vs OCF $1.224B). *Caveat:* the tool's `quality_signal: "low"` label fires for CME, ICE and NDAQ too — the GP/Assets threshold is Novy‑Marx logic built for industrials and is not meaningful for an exchange operator. Disregard the label; the raw metrics are top-tier.

### 2. Price Statistics
| Metric | Reconstructed | Tool (flagged unreliable) |
|---|---|---|
| Annualized return | 41.5% | 41.51% ✅ |
| Annualized vol | ~19–20% | 40.3% ❌ |
| **Sharpe** (rf=0) | **~2.05–2.10** | 1.018 |
| **Sortino** | **~2.9–3.0** (scaled by observed Sortino/Sharpe ratio 1.42) | 1.449 |
| **Beta vs SPY** | **~0.41** (long-run); regression β −0.60 is noise | −0.598 |
| R² vs SPY | ~0.00–0.04 | 0.0379 |
| **Alpha (ann.)** | **statistically ~0** — not distinguishable from zero at R²=0.04 | 42.6% |
| Max drawdown | −14.3% (intraday), −8.9% (closes) | 36.73% |

**Interpretation:** the +42.6% "alpha" is an artifact. With R² = 0.038, ~96% of CBOE's variance is idiosyncratic, so the standard error on alpha is roughly ±40pp — the coefficient is meaningless. What is real: this is a **defensive, near-market-neutral, high-return-on-capital compounder** whose entire move was stock-specific. Beta near 0.4 means the 41% return came with roughly 40% of the market's systematic risk.

### 3. Composite Quant Signal: **BUY**
Three of five factors in the **top quintile of the peer set** (momentum #1, quality #1, low-vol #1) — the classic quality‑momentum‑defensive triad. It is not a **Strong Buy** because the single strongest mean-reversion offset is fully present: value ranks bottom-quintile and the P/E premium (+14%) is not supported by faster growth (FY26→FY27 EPS +7.7%, revenue +5.0%). Deleveraging the momentum score: +32% 12‑1 driven largely by multiple expansion while the forward estimate path is mid‑single‑digit — that is the weakest form of momentum.

### 4. Key Quant Risk Flags
1. **DATA INTEGRITY — highest priority.** Two price sources disagree by 17% ($335.53 vs $286.58) and four of seven risk statistics are irreproducible from the underlying series. Do not size a position or quote a Sharpe to the desk until the price series is reconciled. All risk‑adjusted stats above are my own reconstruction.
2. **Momentum isolation / crowding.** Every peer has flat momentum (CME +3.95%, ICE +5.19%, NDAQ +0.23%). CBOE's +32% is an outlier in a group that has not participated — that is idiosyncratic positioning, not a factor‑wide trend, so there is no factor‑crowding cushion to lean on and reversal risk is single‑name specific.
3. **Multiple-driven momentum + rich valuation.** Buying a 32x P/E on 7% EPS growth after a 48% run is paying up for the re-rating already booked. Mean-reversion risk to the 28x peer multiple is ~−13% of downside on the multiple alone.
4. **Earnings revision signal is void.** The +4.67% revision compares FY2030 vs FY2029 consensus with **1 analyst**. Statistically unusable — I assign zero weight. FY2026 has 10 analysts; the revision history for the near year could not be retrieved.
5. **Model/label artifacts.** The `quality_signal: "low"` label and the GP/Assets sub-factor are mismeasured for Financial Services (no COGS line). Cross-sector factor z‑scores built on `rank_universe_by_factor` will systematically misrank exchanges.
6. **Business concentration (qualitative, unquantified here).** Revenue leverage to index‑options volume/licensing (S&P DJI agreement) and volatility‑product complex — a structurally lower‑volume regime compresses both earnings and the multiple simultaneously.

**Net:** strong business, strongly rising returns on capital, defensive beta, best-in-class momentum — but priced for it. Factor score supports **Buy on quality/momentum with a valuation-based cap on position size.**
