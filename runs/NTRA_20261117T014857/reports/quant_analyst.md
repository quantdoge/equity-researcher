# Quant Analyst

- Symbol: NTRA
- Elapsed: 59.2s

---
# NTRA — Natera, Inc. | Quantitative Factor Report
**Price $288.48 · Mkt Cap $41.8B · EV $38.6B · Healthcare / Diagnostics & Research · 6,138 FTE**

---

## 1. Factor Scores

Peer set (n=6, incl. NTRA): GH, TXG, ILMN, MYGN, RDNT — liquid-biopsy / molecular diagnostics. *EXAS excluded (returned 3.58% vol, beta 0.0, Sharpe 3.73 — corrupted series; would have poisoned the ranks).*

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E **−189.8** (n.m.), EV/EBITDA **−174.9** (n.m.), P/FCF **361.5**, P/B **23.0** | **6 / 6** | **Strong Sell** (worst in peer set) |
| **Momentum** | 12-1m **+24.0%** · 6-1m +16.9% · 3-1m **−2.2%** | **4 / 6** | **Neutral** (decaying) |
| **Quality** | GP/Assets **0.6235** (best in set), accruals **−0.177** (good), ROE **−12.2%**, ROIC **−16.1%**, F-Score **5/9** | **2 / 6** | **Buy** (franchise) / flags on returns |
| **Low Vol** | Vol **56.6%**, beta **1.46** (1y) → **1.69** (63d) | **4 / 6** | **Sell** |
| **Earnings Revision** | Tool: **+78.8%** → *artifact, see below* | **n/a** | **Indeterminate** |

**⚠ Earnings Revision is invalid as computed.** The tool compared FY2030 EPS of $4.19 against a "prior" of $2.3435 — which is *identically* the FY2029 consensus ($2.34349). That is a **fiscal-year mismatch, not a revision**. True estimate curve:

| FY | 2025A | 2026E | 2027E | 2028E | 2029E | 2030E |
|---|---|---|---|---|---|---|
| EPS | **−1.52** | −1.59 | −0.48 | **+1.06** | +2.34 | +4.19 |
| Revenue | $2.31B | $3.00B | $3.65B | $4.49B | $5.49B | $6.46B |

Profitability inflection is **FY2028**, three years out. Genuine upward revision evidence comes from price targets: Barclays $340→$475, Morgan Stanley $355→$435, Canaccord $375→$500 (Oct 2026). Median of 6 targets **$455** (+58% vs spot).

---

## 2. Price Statistics

| Metric | 2Y (504d) | 1Y (252d) | 63d |
|---|---|---|---|
| **Alpha (ann., vs SPY)** | **+29.27%** | — | — |
| **Beta vs SPY** | 1.307 | 1.461 | **1.690** |
| R² vs SPY | **0.1216** | — | — |
| **Sharpe** (rf=0) | **1.032** | 1.003 | **−0.321** |
| **Sortino** (rf=0) | **1.435** | — | — |
| Ann. Return | **+50.08%** | — | — |
| Ann. Volatility | 48.52% | 56.55% | 55.48% |
| **Max Drawdown** | **−33.83%** | −33.83% | **−33.83%** |

**Alpha is not statistically significant.** With R² of only 0.12, residual vol ≈ 45.5%. The standard error on annualised alpha over 2 years is ≈ 45.5/√2 ≈ **32%**, giving t ≈ **0.91**. Report the +29% alpha, but do not build a thesis on it — 88% of NTRA's variance is idiosyncratic.

**The three identical −33.83% drawdowns are the headline.** The trough sits inside the last 63 days — this is *live*, not historical: ~$400 (Oct 12) → $310.68 (Nov 6) → $288.48. Roughly **−28% in two months**.

---

## 3. Composite Quant Signal: **NEUTRAL** (momentum-positive, valuation-hostile)

Factor blend: Quality 2/6 and Momentum 4/6 carry the long case; Value 6/6 and Low-Vol 4/6 cap it.

**The bull case is real but not a *factor* case — it's a fundamental-inflection case:** revenue +35.9% YoY (FY25 $2.31B), 3-yr CAGR **41.2%**, gross margin **64.85%** vs 45.5% in FY23, operating cash flow inflecting to **+$215.3M** from −$431.5M in FY22. On Novy-Marx gross profitability NTRA ranks #1 in its peer set.

**The numbers that veto a higher rating:**
- **Zero value support.** P/FCF 361×; implied P/E on FY2030 EPS = **69×**. The market has already paid for 2030. ILMN trades at 22× EV/EBITDA while NTRA's is negative.
- **Persistent dilution.** Diluted shares 98.4M → 115.0M → 124.7M → **136.7M** (FY22→FY25): **+38.9% cumulative, ~11.6%/yr**. F-Score flags this (F7=0). Per-share value creation lags enterprise progress.
- **Negative returns on capital** (ROIC −16.1%, ROE −12.2%) with F-Score 5/9 — leverage and asset-turnover components both fail (F5=0, F9=0).

---

## 4. Key Quant Risk Flags

1. **Momentum reversal, already in progress.** Term structure is deteriorating monotonically: 12-1m **+24.0%** → 6-1m **+16.9%** → 3-1m **−2.2%**. The 12-1 signal is stale; the leading edge has already turned negative. Recent Sharpe of −0.32 confirms.
2. **Beta is rising into a drawdown:** 1.31 (2y) → 1.46 (1y) → **1.69 (63d)**. Downside participation is accelerating, not decaying.
3. **Crowding in the liquid-biopsy cluster.** Correlation to GH **0.604**, TXG **0.531**, ILMN **0.407**. The NVDA-style "MRD winner" narrative is a single crowded factor — a 1-unit shock to GH transmits ~0.60 to NTRA. Low correlation to RDNT (0.267) provides little diversification value.
4. **Analyst-target / price divergence.** Targets raised to $435–500 while price fell 28%. Either the market is discounting something targets haven't caught, or targets are stale. Targets are 1–2 months old — treat the +58% "upside" as unreliable.
5. **Statistical adequacy:** alpha t-stat ≈ 0.9; peer set n=5 after excluding EXAS; EPS revision tool unusable. Ranks in Sections 1–2 are **indicative, not significant**.
6. **Governance:** price-target note flags a "CEO transition." Unquantifiable here, but a transition at a story stock with a 69× 2030 P/E removes the estimate anchor.
