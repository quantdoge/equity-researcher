# Quant Analyst

- Symbol: QXO
- Elapsed: 61.3s

---
## QXO, Inc. (Industrials — Industrial Distribution) — Quantitative Factor Report
**Price $13.78 (close 2026‑11‑09) | Market cap $8.45B (613M sh) | Sector: Industrials**

### ⚠️ Data integrity flags (read before the tables)
Three feed problems materially affect interpretation. I report tool output *and* my reconciliation from raw OHLC:

1. **Sharpe/alpha return series is corrupt.** `sharpe_sortino` (252d) implies annualized return of −69.1%; the actual 252‑day price path (18.40 → 13.78) is **−25.1%**. Two tools also disagree on the same window's Sharpe (−1.038 vs −0.534). The **126‑day** window is internally consistent and I weight it more heavily.
2. **Market cap / share count conflict.** `calculate_valuation_ratios` uses 613M shares → $8.45B mkt cap, EV $10.0B. The company profile shows **$14.30B** (~1.04B shares). EV/EBITDA is therefore **38.5x or ~61x** depending on the count — an enormous spread. Not resolved.
3. **Earnings-revision "upgrade" is an artifact.** The +33.66% compares FY**2030** EPS ($1.92) against FY**2029** ($1.44) — different periods, not a revision. FY29/FY30 carry **1 analyst each**. True revision evidence (below) is *negative*.

---

### 1. Factor Scores

| Factor | Score | Sector Rank | Signal |
|--------|-------|-------------|--------|
| **Value** | Raw: P/B 0.87, EV/EBITDA 38.5x (61x alt.), P/FCF 46.1x, P/E n/m (EPS −$0.63) | n/a¹ | **Neutral** — book-value support vs. rich cash-flow multiples on depressed EBITDA |
| **Momentum** | 12‑1: **−20.0%**; 6‑1: −20.3%; 3‑1: −13.2% | n/a¹ | **Negative** (persistent, all horizons) |
| **Quality** | ROE **−2.88%**, ROIC **−0.42%**, GP/Assets **7.2%**, accruals −0.034, F‑score **4/9** | n/a¹ | **Low** (tool signal: "low") |
| **Low Vol** | 252d vol **69.9%**, beta **2.74** vs SPY, max DD **−62.5%** | n/a¹ | **Strongly negative** — anti-low-vol |
| **Earnings Revision** | Tool: +33.7% "upgrade" (**artifact**). Reality: PT cuts across the board | n/a¹ | **Negative** (my override) |

¹ Cross-sectional percentile ranks are **not computable** with available tools — no rank-percentile output for a named symbol, and `get_sector_peers` returned mega-cap industrials (GE, CAT, RTX, BA, LMT) that are **invalid comparables** for a building-products distributor. Ranks above are judgmental quintiles vs. true distribution peers (BLDR, GMS, BECN), not measured percentiles. **Sample-size caveat: do not treat these as factor-model percentiles.**

**Revision evidence (my override of the tool):** Baird $35→$30, Truist **$26→$15**, RBC **$27→$18**, Wells Fargo $18→$16→$15, Stephens $29→$26, D.A. Davidson $26→$20. Six consecutive cuts, two of them >40%. Median PT ≈ **$17 (+23% vs. spot)** — the only bullish quant input in the model.

### 2. Price Statistics

| Metric | 252d | 126d | Note |
|---|---|---|---|
| Alpha (ann., vs SPY) | −71.3%* | −22.3% | *inflated by bad series; 126d more credible |
| Beta vs SPY | **2.75** | **2.89** | **Robust** — two independent windows agree |
| R² | 0.322 | 0.340 | **~66% idiosyncratic** |
| Annualized vol | 69.9% | 70.1% | Consistent, credible |
| Sharpe | −1.038* | **−0.321** | 504d: +0.066 |
| Sortino | −2.129* | **−0.697** | 504d: +0.131 |
| Max drawdown | **−62.54%** | — | Peak $27.07 (2026‑02‑13) → trough $10.14 (2026‑10‑19); verified close-to-close |
| Total return (verified) | **−25.1%** | −25.3% | 18.40 → 13.78 |

**Momentum structure is the key nuance:** 12‑1 and 6‑1 are both ≈ −20%, but the **last 21 trading days are +27.5%** (10.81 → 13.78). Price is +35.8% off the October low yet −49% below the February high. This is a high-volatility bear-market rally inside a downtrend — not a trend change confirmed by the factor.

**Correlations (252d):** QXO–SPY **0.565**, QXO–BLDR **0.625**, BLDR–SPY 0.380. QXO trades as a **levered building-products-cycle proxy** — its correlation to BLDR exceeds BLDR's own correlation to the market. (GMS and BECN returned no data — BECN delisted post-acquisition. Peer correlation matrix is effectively n=2.)

### 3. Fundamental / Valuation Cross-Check
FY2025 (Dec): revenue **$6.842B** (vs. $56.9M FY24 — Beacon acquisition closed Apr‑2025), gross margin **16.8%**, EBITDA **$259.5M**, EBIT **−$163.6M**, net income **−$279.4M**, EPS **−$0.63**. D&A $423.1M (PPA-heavy) and interest expense **$173.5M** are the earnings killers. Accruals are **negative (−0.034) — earnings are cash-backed**, and OCF is **+$261M** vs. net income −$279M; that is the one genuine quality positive. F‑score 4/9 with flags on ROA, leverage, dilution (F7=0 — share count expanded), and gross margin trend.

**Leverage:** EV $10.0B − mkt cap $8.45B ⇒ net debt ≈ **$1.55B ≈ 6.0x EBITDA**; EBITDA/interest coverage only **1.5x**.

Estimates: FY26 $0.23 (10 analysts), FY27 $0.53, FY28 $0.97 — a steep hockey-stick requiring ~$31.8B revenue by FY30 (vs. $6.8B now). At $13.78 the stock is ~60x FY26E and ~26x FY27E. **The value case rests entirely on unverifiable long-dated estimates.**

### 4. Composite Quant Signal: **SELL**

Four of five factors are negative and one (revisions) is negative once the artifact is corrected. Momentum is negative on every horizon beyond one month, quality is bottom-tier (ROIC negative, F‑score 4), volatility/beta are in the worst decile of Industrials, and revisions are sharply down. The lone offset is **P/B 0.87** — the market is pricing the equity below stated book ($15.83/sh), which caps downside and is why I do not call Strong Sell. A pure factor composite ranks QXO in the **bottom quintile of Industrials**.

### 5. Key Quant Risk Flags
- **Momentum reversal / bear-rally risk:** +27.5% in 21 days against −20% 12‑1 momentum. Entering long here is buying the reversal leg; entering short risks a squeeze on 70% vol.
- **Extreme idiosyncratic risk:** R² 0.34, beta 2.7–2.9. A 1% SPY move implies ~2.8% on QXO; ~66% of variance is deal/integration/leverage-specific and **not hedgeable with index shorts**.
- **Leverage + coverage:** ~6x net debt/EBITDA with 1.5x interest coverage — the most quantitatively dangerous line item; refinancing or a covenant event is a fat left tail.
- **Dilution:** F‑score F7 = 0, shares 408M → 613M in one year (−33% per-share). Ongoing M&A-funded equity issuance would cap per-share factor improvement.
- **Estimate fragility:** FY29/FY30 EPS rest on **one analyst**. Any consensus-building revision will be violent.
- **Liquidity: NOT a flag** — ~15–40M shares/day (~$200–550M notional). Deep enough for institutional sizing; expect high slippage only in gap events.
- **Factor crowding: not assessable** (no short-interest/ownership feed).

**What would flip the signal:** two consecutive quarters of positive ROIC *and* upward FY27 EPS revisions, or a reclaim of the 200‑day (~$16) on declining volume. Until then the numbers say the story is not yet in the data.
