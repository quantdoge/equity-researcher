# Quant Analyst

- Symbol: DVA
- Elapsed: 142.3s

---
## DVA (DaVita Inc.) — Quantitative Factor Report

**Sector:** Healthcare / Medical-Care Facilities · **Price:** $150.73 (2026-02-20 close) · **Mkt cap ≈ $10.5B** · **Net debt $14.29B** · **EV ≈ $24.8B**

> ⚠️ **Data-integrity warning up front.** The `alpha_beta` / `price_volatility` / `sharpe_sortino` / `correlation_matrix` tools returned statistically impossible output for DVA: beta vs SPY of **−0.114 (R²=0.0009)** on 252d and **+0.112 (R²=0.0011)** on 504d, plus JNJ–UNH correlation of **0.077**. Independent healthcare equities cannot show zero correlation with the market. The cross-symbol return series are date-misaligned. I report the tool outputs for completeness but **substitute recomputed figures from raw OHLCV** and flag every affected line.

---

### 1. Factor Scores Table

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E 18.4x (15.9x repriced), EV/EBITDA 11.3x (~10.0x), P/FCF 11.8x (10.1x) | **1 of 4** on all three multiples | **Strongly bullish** |
| **Momentum** | 12-1 return **−22.0%**; raw 12M +3.3% | Bottom quintile | **Bearish** (but see caveat) |
| **Quality** | ROIC 12.4% (↓ from 14.8%), ROA 4.3%, GP/Assets 21.1%, accruals −6.5%, F-score 4/9 | Middle | **Neutral-to-bearish** |
| **Low Vol** | Realized vol ~33% (recomputed) vs SPY ~15%; beta 0.80 (profile) | Bottom third on vol | **Unfavourable** |
| **Earnings Revision** | −7.28% (FY2029E, **n=1 analyst**) | n/a — not measurable | **No valid signal** |

**Value (strongest factor).** Against the available healthcare large caps, DVA is the cheapest on every metric: P/FCF 11.8x vs UNH 23.7x / JNJ 32.0x / ABBV 28.8x; EV/EBITDA 11.3x vs 18.7x / 16.0x / 32.7x. Forward multiples are cheaper still: **10.2x 2026E EPS ($14.83) and 8.9x 2027E ($16.96)** on the current $150.73 close. Note the tool computed ratios at a **stale $175.35 price** (profile price is ~Jan-2025 vintage); repricing to the last close lowers P/E ~14%.

**Momentum (conflicted).** The 12-1 reading of −22.0% is negative and the stock fell from $177 (Jan-2025) to $103.87 (Jan-14-2026), a **−41.4% drawdown**. But the last 21 days — deliberately *excluded* by the 12-1 construction — delivered **+45.0%** (Feb-3-2026: **+21.2% on 4.8M shares**, ~6x normal volume, immediately around the FY2025 report). The negative score is mechanically stale; momentum is inflecting, not deteriorating.

**Quality.** ROE of 64.5% is an artifact of a **near-zero equity base** ($1.16B equity on $17.48B assets = 6.6% equity/assets), not excellence. ROIC of 12.4% is only a modest spread over cost of capital and is **declining** (14.8% → 12.4%). Genuine positives: accruals ratio **−6.5%** (operating CF $1.89B vs net income $0.75B — high cash conversion, consistently negative for 4 years) and improving asset turnover. Piotroski F-score 4/9 is weak, though F6/F7 fail largely because aggressive buybacks shrink equity — a known bias in that score.

**Earnings revision — not statistically usable.** The −7.28% "downgrade" compares FY2029E ($18.12, **1 analyst**) against the FY2028E figure ($19.54, 3 analysts) — a period mismatch, not a revision. Coverage is 1–5 analysts across all years. The estimate ladder (2026E $14.83 → 2027E $16.96 → 2028E $19.54) implies ~14–15% annual growth, but I place **no weight** on this signal.

---

### 2. Price Statistics (252 trading days)

| Statistic | Tool output | My recomputation | Verdict |
|---|---|---|---|
| Total return 12M | +76.4% ann. | **+3.3%** ($145.92 → $150.73) | Tool rejected |
| Alpha (ann., vs SPY) | +74.5% | **not estimable** (R²=0.001) | Unusable |
| Beta (vs SPY) | −0.114 | **0.80** (profile, 5Y) | Tool rejected |
| R² | 0.0009 | — | Implausible |
| Realized vol (ann.) | 50.8% | **~33%** (343 obs) | Tool overstated |
| Sharpe (0% rf) | 1.49 | **~0.10** (3.3%/33%) | Tool rejected |
| Sortino (0% rf) | 2.22 | **~0.13** | Tool rejected |
| Max drawdown | −27.9% | **−32.7%** ($154.29 → $103.87); **−41.4%** from Jan-25 peak | Tool understated |

*(504d window for reference: vol 41.3%, beta 0.112, Sharpe 0.538, Sortino 0.777, ann. return 22.4% — same misalignment defect.)*

**Short-horizon returns:** 1M **+45.0%** · 3M **+30.7%** · YTD **+32.7%**. Correlation to UNH/JNJ/ABBV reported at 0.04–0.05 is an artifact; genuine healthcare correlations should run 0.3–0.6, meaning DVA's **true market/sector co-movement is materially understated** and the ~33% vol is largely idiosyncratic.

---

### 3. Composite Quant Signal: **NEUTRAL (value-tilted, momentum-conflicted)**

Top-decile value, but offset by negative (if stale) momentum, sub-par and deteriorating returns on capital, ~2x-market volatility, and unmeasurable estimate revisions. One factor of five is strongly positive — not enough for Buy on a rules-based composite.

**Trigger to upgrade to Buy:** one more month holding above the ~$120 breakout with 12-1 momentum turning positive (a further ~8% from here mechanically flips the score) → would become a rare cheap-plus-momentum setup.
**Trigger to downgrade to Sell:** failure back below $120 (retraces the Feb-2026 gap) or net debt/EBITDA moving above 6.5x.

---

### 4. Key Quant Risk Flags

1. **Leverage / solvency (highest-severity flag).** Net debt **$14.29B** (+$2.16B y/y) against **$1.16B equity** = **12.3x net debt/equity** and **~5.9x net debt/EBITDA**. Total liabilities are 93.4% of assets. Goodwill+intangibles of $7.77B are **6.7x book equity** — tangible book is deeply negative. This is the dominant risk to the value thesis; it is also why the multiple is cheap.
2. **Momentum reversal risk — two-sided.** A +21.2% single-day gap on 6x volume is event-driven, not trend-driven. Post-gap gaps fill frequently; the stock is +45% in a month after −41%. Expect elevated realized vol regardless of direction.
3. **Factor crowding / peer-basket problem.** The "sector peer" set is mega-cap pharma (LLY, JNJ, ABBV, UNH, MRK), not dialysis comps. **Fresenius Medical Care (FMS) and Baxter are the true comparables and were unavailable.** All sector ranks above are therefore low-confidence — DVA's cheapness vs pharma does not prove cheapness vs dialysis peers.
4. **Volatility/factor-model instability.** At ~33% realized vol and R² vs market of ~0, DVA contributes almost no beta exposure and substantial idiosyncratic variance. Any factor-model risk decomposition built on the tool's beta (−0.11) would badly misstate portfolio risk.
5. **Liquidity — adequate, with event spikes.** Median volume ~700k shares (~$105M/day) is fine for most institutional sizing, but earnings days see 2.2–5.1M shares; expect slippage on size around catalysts.
6. **Analyst coverage too thin for revision signals.** 1–5 analysts; no statistically valid revision momentum. Any claim of "downgrade" or "upgrade" pressure here is noise.
7. **Stale input data.** Profile price ($175.35) and market cap ($11.19B) are ~13 months old relative to the $150.73 close; shares implied are inconsistent across sources (63.8M vs ~70M vs 87M). All multiples and the EV build carry this uncertainty.
8. **Buyback-distorted quality score.** Piotroski F 4/9 and negative retained earnings (−$328M) partly reflect capital returns, not operating distress — read the F-score with that haircut.
