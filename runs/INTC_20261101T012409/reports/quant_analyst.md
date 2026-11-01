# Quant Analyst

- Symbol: INTC
- Elapsed: 53.0s

---
## INTC — Quantitative Factor Panel
**As-of price: $65.76 (2026‑10‑30 close)** · Semis peer set: NVDA, TSM, AVGO, AMD, MU

### Data integrity note (read first)
Three feeds disagree and I've resolved them against the raw tape: `calculate_valuation_ratios`/profile correctly use **$65.76** (10/30/26), while `get_price_history` was truncated at 2025 — I pulled 2026 separately. The 53.34% max drawdown reconciles exactly ($140.94 on 2026‑06‑22 → $65.76 = **−53.3%**), and 86% vol is consistent with a $40→$141→$66 round trip, so the OHLC series is the trustworthy one. Two tools are nonetheless unreliable: **TSM's value ratios are corrupted** (P/E 1.23, EV/EBITDA 0.02) and **the momentum tool's level (+19.06%) is off by an order of magnitude** vs. the raw series (+199%). Ranks below are computed from raw data.

### 1. Factor Scores

| Factor | Score (−2…+2) | Sector Rank | Signal |
|---|---|---|---|
| Value | **−1** | 5 of 6 | P/B 2.53 is the cheapest in group, but P/E n/m (−1,116x), P/FCF −64.5x, EV/EBITDA 22.9x — "cheap" only on a book value that is eroding (ROE −0.2%). Classic value trap optics. |
| Momentum | **0** | 1 of 6 | 12‑1 momentum **+199%** (+64% 12‑mo), highest in group (+19% AMD, +14% TSM, +12% NVDA, +9% MU, −9% AVGO) — but **−45% in 1 month**, −27% in 3 months. Level bullish, *direction broken*. |
| Quality | **−2** | 6 of 6 | ROE −0.21%, ROIC −1.28%, gross profit/assets **0.087** vs peers 0.22–0.74. Piotroski 6/9 (moderate). Only offset: accruals −4.7% (cash > accounting earnings; OCF +$9.7B vs NI −$0.27B). |
| Low Vol | **−2** | 6 of 6 | 86.0% annualised vol, beta **3.59** (252d) / 2.95 (504d). Worst in peer set; deepest quintile. |
| Earnings Revision | **n/a** | — | ⚠️ **Invalid reading.** Tool's +45.5% compares FY2030 EPS ($6.77) to FY2029 ($4.65) — two *different* forecast years, not a same-period 3‑month revision. Also only **6 analysts** on 2030. No valid revision signal available. |

### 2. Price Statistics (252d unless noted)

| Metric | Value |
|---|---|
| Alpha (ann., 504d, vs SPY) | **+51.3%** |
| Beta (504d / 252d / 5Y monthly) | 2.95 / 3.59 / 2.23 |
| R² (504d) | **0.221** |
| Sharpe | **0.90** (alt. calc 1.004) |
| Sortino | **1.34** |
| Ann. return / vol | +77.1% / 85.8% |
| Max drawdown | **−53.3%** |
| Current drawdown from peak | **−53.3%** (unrecovered) |

**The alpha is not statistically significant.** With R² = 0.22, residual vol ≈ 75.9% ann.; SE(alpha) ≈ 75.9/√2 ≈ 53.7% → **t ≈ 0.96**. A +51% "alpha" is indistinguishable from noise. Beta 2.95 with only 22% R² means INTC is an idiosyncratic 3x-levered semis bet, not a market proxy — 78% of its variance is stock-specific. Sortino/Sharpe = 1.49 implies ~36% of total vol is downside deviation.

### 3. Composite Quant Signal: **SELL** (conviction: moderate, downgrade is *fresh*)
Factor composite is unambiguously bottom-quartile: last on quality, last on low-vol, bottom on true value. The single bullish leg (12‑1 momentum) has just rolled over — a textbook **momentum-reversal setup**, which is precisely where crashes cluster. Note the trade is *not* cheap on near-term estimates: **43.6x FY26E EPS ($1.51), 35x FY27E ($1.88), 21x FY28E ($3.12), 9.7x FY30E ($6.77)** — the "cheapness" requires delivery of a 4-year, 4.5x EPS ramp on n≈6 analysts.

### 4. Key Quant Risk Flags
1. **Momentum crash in progress** — −28.6% on **455.6M shares (≈4.5x 20‑day avg)**, the heaviest volume in the entire two-year sample. High-volume capitulation on a 3.6-beta name typically marks the *start* of de-risking, not the end. 12‑1 momentum will turn negative within ~2 months mechanically.
2. **Factor crowding / reflexivity** — the +199% 12‑mo run to $141 was a momentum-and-narrative trade; the reversal is now reflexive (down 45% in a month).
3. **Quality/valuation trap** — negative TTM EPS, **FCF ≈ −$5.0B** (OCF $9.7B less ~$14.6B capex). Foundry capex consumes the entire operating cash flow; book value per share ($26.02) is the only support, and P/B 2.53 on negative ROE is not a floor.
4. **Statistical caveats** — 6-analyst coverage on 2029/2030 estimates; revision signal **unusable**; alpha insignificant (t≈0.96); TSM peer multiples corrupted, so my "5 of 6" value rank leans on 4 comparables.
5. **Liquidity is not a constraint** (~$0.9B/day traded) — this is a volatility and fundamentals problem, not a capacity one.

**Peer factor detail (raw):** EV/EBITDA — MU 8.9x, **INTC 22.9x**, NVDA 34.4x, AVGO 47.0x, AMD 112.7x. Gross profit/assets — NVDA 0.74, MU 0.55, TSM 0.29, AVGO 0.25, AMD 0.22, **INTC 0.09**. ROE — NVDA 76.3%, MU 61.4%, TSM 31.5%, AVGO 28.5%, AMD 6.9%, **INTC −0.2%**.
