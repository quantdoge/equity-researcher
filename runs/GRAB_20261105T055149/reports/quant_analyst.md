# Quant Analyst

- Symbol: GRAB
- Elapsed: 47.0s

---
## GRAB — Quantitative Factor Report
*Grab Holdings Ltd · Technology (software-app) / SE Asia super-app · Price $3.36 · Mkt cap $13.35B · EV $9.38B*

### ⚠️ Two data-integrity flags up front
1. **Price staleness in the return series.** The OHLCV series I retrieved ends at $4.38 (2026-02-20) while the live quote is **$3.36**. Post-Feb-2026 the stock fell a further ~23% to a trough near **$2.87** (Oct-2026 price-target notes printed against $2.865–$2.96), then rebounded ~17% to $3.36. **All momentum/Sharpe/vol figures below are measured to the stale anchor and therefore understate realised drawdown.**
2. **The earnings-revision score is a period mismatch, not a revision.** The tool compared FY**2029** EPS ($0.1747) against FY**2028** ($0.22516) — different forward periods. The −22.4% "downgrade" is an artifact. Genuine curve is *rising*: FY25 $0.054 → FY26 $0.131 → FY27 $0.158 → FY28 $0.225.

---

### 1. Factor Scores

| Factor | Score (raw) | Rank vs true peers* | Signal |
|---|---|---|---|
| **Value** | P/E 52.8 · P/B 2.09 · EV/EBITDA 18.2 · **P/FCF 105.5** | **3 of 4** | Negative |
| **Momentum** | 12-1 return **−10.7%** | **3 of 4** | Negative |
| **Quality** | ROE 3.97% · ROIC 2.52% · GP/Assets 0.122 · Accruals 0.0031 | **4 of 4** | Strong negative |
| **Low Vol** | Vol 40.0% · β 1.36 · MaxDD 42.2% | 4 of 4 | Negative |
| **Earnings Revision** | Headline −22.4% (**invalid**); true FY25→FY28 EPS CAGR **+61%** | 2 of 4 | Neutral |

\* **Sector rank caveat:** the "Technology" peer list returned AAPL/NVDA/MSFT/TSM/AVGO — mega-cap US semis, an invalid comparison set for a Singapore-based super-app. I re-scored the correct comp set (UBER, DASH, SE, MELI) on the same tools. Peer comparators: P/E UBER 14.8 / SE 31.8 / GRAB 52.8 / DASH 93.2; EV/EBITDA SE 15.6 / **GRAB 18.2** / UBER 21.8 / DASH 50.4; P/FCF SE 11.3 / UBER 15.2 / DASH 40.2 / **GRAB 105.5**; ROE UBER 35.8% / SE 12.5% / DASH 9.3% / **GRAB 4.0%**; GP/Assets UBER 0.335 / DASH 0.355 / SE 0.349 / **GRAB 0.122**. Momentum: DASH −2.2% / UBER −3.2% / **GRAB −10.7%** / SE −11.9%.

**Piotroski F-Score: 5/9 (Moderate).** Passing: positive ROA, positive OCF, ROA improvement, positive equity change, gross-margin improvement. **Failing: accruals quality, leverage, dilution (F7 = 0), asset turnover.**

**Quality detail — the weakest pillar.** ROIC 2.52% sits well below any reasonable WACC (~10–11%), i.e. **economically loss-making on capital** despite GAAP profitability, though the trajectory is a genuine turn: −16.1% → −5.3% → −0.8% → **+2.5%** (FY22–25). Mitigants: accruals pristine (+0.0031 vs −10.3% in FY24), gross margin 5.4% → 36.5% → 42.0% → **43.2%**. Aggravators: **SBC $241M = 90% of net income and 7.2% of revenue**; diluted shares +5.3% y/y (3.995B → 4.206B). Reported profit is substantially a stock-compensation-financed construct.

---

### 2. Price Statistics

| Metric | Value | Note |
|---|---|---|
| Alpha (504d, vs SPY) | **−46.4% annualised** | t ≈ −1.8 (est.), **not significant at 95%** |
| Beta (504d) | **1.423** | R² **0.1906** — only 19% market-explained |
| Beta (252d) | 1.36 | Company-reported 5y monthly β **0.833** — large methodology gap |
| Annualised vol | **40.0%** | ~2.5× market |
| Sharpe | **−0.611** | (ann. return −24.4%) |
| Sortino | **−1.16** | Worse than Sharpe → downside semidev ~21% |
| Max drawdown (tool) | **−42.2%** | Realised peak-to-trough: $6.45 → $2.87 = **−55.5%** |
| Residual/idiosyncratic vol | ~36% | Dominant risk is stock-specific, not market |

**Correlations (252d):** SPY **0.449** · DASH 0.471 · SE 0.438 · UBER 0.438 · MELI 0.425. Notably GRAB correlates *more* with SPY than UBER does with SPY (0.284) — it trades as a high-beta risk asset rather than on platform-sector fundamentals. Loose clustering with the platform complex means **no evidence of factor crowding**. Alpha confidence: with R² = 0.19 the −46% alpha rests on a 2-year sample and should be treated as directional, not statistically established.

---

### 3. Composite Quant Signal: **NEUTRAL (negative tilt)**

Scored −2 to +2 per factor: Value −1, Momentum −1, Quality −2, Low Vol −1, Revisions 0 → **−5 of ±10**.

Not a Sell because: (a) **EV/EBITDA 18.2x is mid-pack**, and on forward EBITDA it compresses hard — FY26E **9.4x**, FY27E **7.9x**, FY28E **6.2x**; (b) **net cash $3.97B = $0.94/sh = 28% of market cap** (ex-cash trailing P/E 38x, ex-cash FY26E P/E **18.5x**); (c) forward EPS curve is steeply rising ($0.054 → $0.225, 2025–28); (d) the momentum weakness is **group-wide** (every platform peer negative), i.e. a de-rating of the complex, not stock-specific deterioration.

Not a Buy because: quality fails on every axis (ROIC < WACC, worst GP/assets, 90% SBC/NI, dilution), cash conversion is thin (FY25 FCF $134M, 1.0% FCF yield — FY24's $775M was working-capital-inflated), and the trend is still down.

**Corroborating sell-side (stale):** mean target **$5.81**, median **$5.85** (+73% vs $3.36) — but the *path* is lower: Barclays $7 → $5 → **$4**; Morgan Stanley $6.40 → $5.90 → $6.25; Bernstein $5.80. Recent-cluster implied value is **$4–5 (+19% to +49%)**, not the headline mean. 8 targets, all pre-dating the current price.

---

### 4. Key Quant Risk Flags

1. **Momentum reversal / downtrend fragility** — −10.7% 12-1 plus a further −23% beyond the data anchor; the +17% bounce off $2.87 is unconfirmed. High probability of a lower-low retest in a 40-vol name.
2. **Earnings-quality / dilution leakage** — SBC 90% of net income; share count +5.3%/yr caps per-share compounding. Watch `F7` and accruals for deterioration.
3. **Sub-optimal capital allocation return** — ROIC 2.52% < WACC; the bull case requires the margin ramp (EBITDA −$1.42B → +$517M) to continue for another 2–3 years.
4. **Statistical fragility of alpha** — R² 0.19, t ≈ −1.8, 2-year window; do not lean on the −46% alpha as a stable estimate.
5. **Factor crowding: LOW** — correlations 0.42–0.47 vs peers, no tight cluster. Genuine diversifier within consumer-internet, but idiosyncratic vol ~36% dominates.
6. **Liquidity: NOT a constraint** — volume typically 25–80M shares/day ($0.1–0.3B), deep enough for institutional position sizing.
7. **Estimate reliability: weak** — FY26E covers only **5 analysts** (range $0.112–$0.159, ±18%); FY28–29E cover 3 and the FY29 net margin (11.4%) is *inconsistent* with the FY28 figure (15.8%). Long-dated consensus should be discounted heavily.
