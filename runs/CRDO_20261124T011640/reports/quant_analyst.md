# Quant Analyst

- Symbol: CRDO
- Elapsed: 78.0s

---
## CRDO — Credo Technology Group (Semiconductors) | Quant Factor Report
**Price $122.46 (23-Nov-2026) · Mkt cap $23.0bn · Data window 252d to 2026-11-23**

### 1. Factor Scores
| Factor | Score | Peer Rank (NVDA/AVGO/MU/MRVL) | Signal |
|---|---|---|---|
| Value | P/E 48.8x (peer med 47.2x), EV/EBITDA 42.4x (peer med 28.2x), P/FCF 56.6x | **4 of 5** (bottom tier) | **Negative** — expensive |
| Momentum | Vendor 12-1: **−41.84%**; my raw series: 12-1 +2.2%, 6m ex-1m −20.6%, 1m −16.9%, −59.5% off June high | **5 of 5** | **Strong Negative** |
| Quality | ROE 22.9%, ROIC 21.3% (FY25 5.5%, FY24 −6.7%), GP/A 0.396, accruals 0.0035, GM 68.0%, F-Score 7/9 | **2 of 5** on accruals, 3–4 on ROE/GP-A | **Positive** (best-in-class earnings quality) |
| Low Vol | Vol **107.6%** (126d: 110.0%), β 3.69 (126d: 4.29), max DD **66.99%** | **5 of 5** | **Strong Negative** |
| Earnings Revision | −1.07% (FY31 $13.45 vs FY30 $13.60) — **n = 1–2 analysts, cross-horizon artifact** | 4 of 5 | **Neutral/Negative** (low confidence) |

**Revision detail:** sustained PT cuts (Stifel 350→310, Evercore 325→292, BofA→275, Mizuho→245) vs two raises (Rosenblatt 235, Susquehanna 235→250). Median PT **$262.50 (+114%)**. Analyst model implies growth deceleration: FY26 $3.31 → FY27 $6.30 (+90%) → FY28 $9.67 → FY29 $12.38 → FY30 $13.60 → **FY31 $13.45 (decline)**.

### 2. Price Statistics
| Metric | 252d | 126d |
|---|---|---|
| Alpha (vs SPY, ann.) | **+18.56%** (t ≈ 0.2 — **not significant**) | — |
| Beta | 3.687 | 4.285 |
| R² | 0.309 | — |
| Sharpe | 0.527 | **−1.15** |
| Sortino | 0.880 | **−1.77** |
| Ann. vol | 107.6% | 110.0% |
| Max drawdown | **−66.99%** ($302.52 → $99.86) | same |

**Critical caveat:** the 252d Sharpe is arithmetic-mean based (+56.7% ann.); actual geometric 12-month return is **−8.3%**. Volatility drag ≈ 65pp/yr. The +18.6% alpha has a t-stat of ~0.2 with R² = 0.31 — **statistically indistinguishable from zero**; this is a beta vehicle, not an alpha generator.

### 3. Composite Quant Signal
**NEUTRAL (−) —** 3 of 5 factors negative (value, momentum, low-vol), offset by genuinely strong quality and a modest forward multiple (19.4x FY27E, 12.7x FY28E). **On a risk-adjusted basis this grades Sell**: Sortino < 1 over 252d, −1.77 over 126d, and a 67% drawdown. Low conviction; the quality pillar is the only thing preventing a Sell.

### 4. Key Quant Risk Flags
1. **Beta/vol explosion** — β 3.69→4.29, vol ~108%. A 1% SPY move ≈ 3.7% CRDO. Equal-risk sizing requires ~¼ the notional of a market-beta position.
2. **Negative momentum + reversal** — worst in the semi comp set; vendor 12-1 (−41.8%) and my 6m-ex-1m (−20.6%) agree, though the vendor window fails to reconcile with the raw 12-1 (+2.2%). Floor the signal at "negative" either way.
3. **Factor crowding** — correlations 0.62 MU, 0.59 MRVL, 0.57 AVGO, 0.50 NVDA. Zero diversification from the AI-interconnect trade; a sector de-rate hits CRDO ~2x.
4. **Estimate-revision opacity** — long-dated consensus has 1–2 contributors and models an EPS *decline* by FY31. Treat revision score as noise, not signal.
5. **Valuation cliff** — 48.8x trailing sits on FY27E EPS growth of +90%. Any guide-down compresses the multiple non-linearly.
6. **Dilution** — F-Score F7 fails: 188.2M diluted vs 178.5M basic shares.
7. Liquidity is **not** a concern (~$0.7–1.5bn notional/day); the risk is volatility, not access.

**Data note:** sector peer list returns mega-caps only (AAPL/NVDA/MSFT/TSM/AVGO/MU); ranks are computed against a 5-name semiconductor comp set (NVDA, AVGO, MU, MRVL, CRDO). With n = 5, "rank" is qualitative — no quintile statistics are reliable at this sample size.
