# Quant Analyst

- Symbol: ACM
- Elapsed: 40.1s

---
## ACM (AECOM) — Quantitative Factor Report
*Price $80.53 | Mkt cap $10.46B | Industrials / Engineering & Construction | FY26 (Sep-26) reported 2026-11-16*

### ⚠️ Read this before the scores: three data-integrity breaks
1. **FY26 balance sheet is truncated.** `total_debt = 0`, `net_debt = −$1.24B (net cash)`, `total_current_liabilities = 0`, `goodwill = 0`, `ppe_net = 0` — vs FY25 debt of **$3.36B**. Because EV is computed off net cash, the tool's **EV/EBITDA of 13.34x is wrong** (implies EV $9.21B < market cap). Restating with last reliable net debt ($1.78B): **EV ≈ $12.2B**.
2. **FY26 operating cash flow printed as 0.0** → FY26 accruals (+0.024) and P/FCF are artifacts; the $15.27 P/FCF actually derives from FY25 FCF ($685M) and is usable.
3. **The "+29.74% upgrade" is a roll-forward artifact, not a revision.** Current 9.08 = the **FY2029** estimate (1 analyst); prior 6.99881 = the **FY2028** estimate. Different fiscal years. See revision section for the real signal.

### 1. Factor Scores Table
Scores are my 0–100 percentile composites from tool outputs. Sector rank = of 5 broad Industrials comps (ACM, CAT, ETN, UNP, GE) — **note: no true E&C peers (FLR/FCN/Jacobs) in the peer feed, so ranks are approximate.**

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | 72 | **1 / 5** | **Attractive** |
| **Momentum** | 20 | 5 / 5 | **Negative** (inflecting) |
| **Quality** | 32 | 5 / 5 | **Weak** |
| **Low Vol** | 25 | 5 / 5 | **Poor** |
| **Earnings Revision** | 45 | 4 / 5 | **Neutral, turning up** |

**Value detail (this is the only clean positive):**
| Metric | ACM | CAT | ETN | UNP | GE |
|---|---|---|---|---|---|
| P/FCF | **15.3x** | 36.2x | 37.0x | 32.1x | 47.9x |
| EV/EBITDA | **~9.5x norm.** (13.3 reported, 17.7 on depressed FY26 GAAP) | 20.5x | 22.8x | 16.0x | 29.5x |
| P/E | 35.6x GAAP / **12.9x fwd adj.** | 30.4x | 32.2x | 24.8x | 40.0x |
| P/B | 4.55x | — | — | — | — |
| Div yield | 1.58% (just raised) | — | — | — | — |

ACM is the cheapest name on cash flow and normalized EBITDA by a wide margin. The 35.6x headline P/E is an artifact of **GAAP EPS $2.26 vs FY27 adjusted guidance of $6.15–6.35** (midpoint $6.25). Valuation is entirely a bet on the adjusted/normalized number.

**Quality detail:** ROE 12.8% (FY25: 20.8%), ROA 2.42% (4.6%), gross profit/assets 0.0723 — **lowest of all five comps** (CAT .22, ETN .25, UNP .21). Piotroski **F-Score = 4 (Weak)**; failing on ROA improvement, gross margin improvement, asset turnover, leverage, and equity change. The one genuine positive: **accruals have been negative for 4 straight years** (−5.7%, −3.5%, −2.1%, and FY26 −4.3% in the quality tool) = clean cash conversion, FCF > net income every year. Caveat: the tool's FY26 **ROIC of 26.96% is not credible** — it jumps from 16.94% while ROE/ROA fell, because equity-only invested capital was used after debt was nulled. Use **~17%** (FY25).

**Momentum detail:** 12-1 momentum **−19.1% → negative**, 5th of 5. Critically, the excluded 21-day window contains **+38.8%** (58.02 → 80.53), so measured momentum through mid-October was materially worse than −19.1%. The stock crashed from $133 to $58 (−56%) between Nov-25 and Oct-26.

**Earnings revision detail (real, not the tool's artifact):**
- Every one of the **10 most recent price targets was cut** (Citi 84→79, RBC 105→90, GS 100→91, Truist 85→75, Argus 85→75, Baird 73→65…). Twelve months of negative revision.
- FY26 GAAP EPS $2.26 vs consensus $3.985 = **−43% miss** (driven by a one-off: **Q2 FY26 gross profit was −$34M**, net loss −$86.7M).
- **Nov 17 inflection:** Q4 adjusted EPS beat, **record $28B backlog**, dividend hike, FY27 guide $6.15–6.35 vs consensus $6.17–6.24 → slightly above. Stock **+11.1% on 3.5× volume**, and +21.5% over two sessions.
- Estimate series is too thin to quantify (1–6 analysts; FY26 revenue estimate $7.33B vs $15.10B actual — unusable).

### 2. Price Statistics (252-day window, 0% rf)
| Metric | Value |
|---|---|
| Annualized return | **−15.04%** |
| Annualized volatility | **38.7% – 41.2%** (two tool variants) |
| Beta vs SPY | **0.711** |
| Alpha (annualized) | **−27.50%** |
| R² vs SPY | **0.0617** |
| Sharpe | **−0.388** |
| Sortino | **−0.514** |
| Max drawdown | **−43.4%** (tool); **≈−56% observed** close-to-close (133.31 → 57.98) |

Interpretation: **R² of 6% is the headline.** Only 6% of ACM's variance is market-driven; the −27.5% alpha and the −56% drawdown are almost entirely idiosyncratic. The low 0.71 beta is **not** a risk-management feature — it is a statistical artifact of near-zero correlation; realized vol (41%) is 2× the market.

### 3. Composite Quant Signal: **NEUTRAL** (38.8 / 100)
Equal-weighted (Value 72, Revision 45, Quality 32, Low Vol 25, Momentum 20).

The screen is a genuine barbell: **top-quintile value against bottom-quintile quality, momentum and volatility**, with a deeply negative alpha. That combination is a classic "cheap for a reason until the catalyst lands" profile — and a catalyst did land on Nov 17 (backlog, guidance, dividend). But one good quarter does not create a revision trend, and momentum/quality still score in the bottom quintile. **Not a Buy** until the next quarter confirms upward estimate revisions; **not a Sell** given 15x FCF and a validated backlog.

### 4. Key Quant Risk Flags
1. **Event / gap risk — severe.** Four single-day drops of −8% to −14% in twelve months (Nov-19-25 −11.1%, Feb-12-26 −12.4%, May-12-26 −13.9%, Aug-12-26 −9.0%), plus +11.1% on Nov-17. With R² = 0.06, **beta-based hedging provides almost no protection.** Size positions to realized 41% vol, not the 0.71 beta.
2. **Momentum reversal risk — two-sided.** 12-1 is −19.1% but the last month is +38.8%. A short-momentum/mean-reversion model would be whipsawed here; the trend signal and the catalyst are in direct conflict.
3. **GAAP-vs-adjusted fragility.** The entire value case rests on ~$6.25 of adjusted EPS vs $2.26 GAAP. Q2 FY26 produced negative gross profit. **If the "one-off" charge recurs, the 12.9x forward multiple becomes 35x** and the value factor collapses. This is the single largest analytical risk.
4. **Data integrity / restatement risk.** FY26 debt, current liabilities, goodwill and PP&E all null in the feed; EV/EBITDA (13.34x) and ROIC (26.96%) are both invalid as delivered. Any factor model ingesting these will mis-rank ACM on value *and* quality.
5. **Estimate-data thinness.** 1–6 analysts per period; the surface "+29.7% upgrade" is a fiscal-year roll-forward. **Do not feed this into a revision factor** — the honest read is "negative trend, fresh positive inflection, unquantifiable confidence."
6. **Not a liquidity flag.** ~1.3M shares/day, $10.4B cap, ~$80 price. Fine.
7. **Share count falling** 140.1M (FY23) → 129.9M (FY26), −7.3%, with $388M buybacks and no dilution (F7 = 1). Genuine, quantifiable shareholder-return support.
