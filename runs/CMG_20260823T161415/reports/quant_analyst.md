# quant_analyst

_2026-08-23T08:18:53+00:00_

# CMG (Chipotle) — Quantitative Factor Analysis — Raw Inputs & Compute Requests

**Data as of session timestamp 2026-08-21** (quote endpoint). All figures below are *raw inputs fetched*, not computed scores. Anything with an asterisk (*) is a raw input that requires quant_engineer processing.

---

## 1. Momentum Signals (with attributable values)

| Signal | Value | Source |
|---|---|---|
| Last close (PX) | **$36.90** | `quote/quote` → CMG |
| 50-day SMA | **$33.711** | `quote/quote` → `priceAvg50` (also `technicalIndicators/simple-moving-average`, period 50, 1day → latest SMA 33.711) |
| 200-day SMA | **$34.517** | `quote/quote` → `priceAvg200` (also SMA-200 endpoint, latest 34.517) |
| Price vs MAs | Price **above both** MAs; note MA50 (33.71) **<** MA200 (34.52) → short-term downtrend vs long-term | derived structure from above |
| 14-day RSI (1day) | **62.43** on 2026-08-21; 56.83 on 08-20; 54.36 on 08-19 → rising ~8 pts in 3 days, near-neutral upper band, not yet overbought (>70) | `technicalIndicators/relative-strength-index` (periodLength 14, timeframe 1day) |
| 52-week range | Year–high **$43.59**, year–low **$28.04** | `quote/quote` |
| Day move | +4.56% (prev close $35.29 → $36.90) | `quote/quote` |
| Price history | 911 EOD sessions (Jan-2023 → Aug-2026) saved to `data/cmg_price_full.json` for 12–1M momentum | `chart/historical-price-eod-full` |

Signal (qualitative, attribution only): **recovering/upper-momentum**. Price > 200d MA, RSI rising from mid-50s to low-60s over 3 sessions. But 50d MA < 200d MA still indicates the major downtrend (from $66 area in 2024) is not conclusively reversed.

## 2. Volatility & Beta Inputs (raw)

| Input | Value | Source |
|---|---|---|
| 30-day std dev (raw, per-point on ~$35 px) | **1.7706** (08-21); 1.697 (08-19) → rising sc | `technicalIndicators/standard-deviation` (periodLength 30, timeframe 1day) |
| Annualized volatility | *NB4* compute from CMG daily returns | `chart/historical-price-eod-full` |
| Beta vs S&P500 ETF (SPY) | *NB4*, regression | `chart/historical-price-eod-full` SPY → `data/spy_price_full.json` |
| Maximum drawdown | *NB4* | `chart/cmg_price_full` |

Note: 30-day std dev of **$1.77** on a ~$35 price ≈ 5% daily-scale dispersion; annualization is quant_engineer's job.

## 3. Valuation / Quality Raw Inputs

**Valuation (from `key-metrics-ttm` unless noted):**
- Market cap $47.33B; enterprise value $52.52B
- EV/EBITDA **23.10**; EV/Sales **4.23**; EV/FCF **33.48**; EV/OCF 22.57
- Earnings yield **2.99%**; FCF yield **3.31%**
- P/E (TTM) **33.85**, P/E growth -9.56, fwd P/E **1.75**, P/B **21.60**, P/S **3.81**, P/FCF **30.17**, P/OCF **20.42** (all `metrics-ratios-ttm`)
- Net debt/EBITDA **2.28**; debt/EBITDA **2.28**

*These are classic value-factor inputs: at ~34x TTM earnings and 23x EBITDA, CMG screens as expensive on static value, though FWD P/E 1.75 and negative P/E growth weighting suggest market expects strong forward earnings growth — a tension to resolve in cross-sectional ranking.*

**Quality (from `key-metrics-ttm`):**
- ROE **53.3%**, ROA **16.0%**, ROIC **32.22%**, ROCE **25.0%**, opROA **21.4%**
- Operating margin **15.2%**, net margin **11.4%**, gross margin **24.1%**, EBITDA margin **18.3%** (`metrics-ratios-ttm`)
- Income quality (FCF/NetInc) **1.64**; operating-cash-flow coverage ~7.34x; interest/debt coverage not set (0/5.75)
- ROIC/ROE are strong (top-quintile on quality vs most peers)

## 4. Explicit compute requests for quant_engineer (exact formula + endpoints)

| # | Request | Formula / Logging | Input |
|---|---|---|---|
| 1 | **12–1 month price momentum** | `(P_monthly_now − P_monthly_11monthBack) / P_11mBack` — (exclude latest month) over daily closes from `chart/historical-price-eod-full` (`data/cmg_price_full.json`). Provide percentile vs sector trend. | CMG price series |
| 2 | **BM momentum** | same formula, on 2009-… split-aware; MUST handle June-2024 50:1 split (use adjusted or `nonadjusted`/`dividend-adjusted` correctly) | CMG series |
| 3 | **B / alpha vs S&P500 (SPY)** | Regress CMG daily log-returns on SPY daily log-returns in `to-1` returns: `β = cov(rc,rm)/var(rm)`, `α = E[rc]−βE[rm]` over trailing 1y and the full series. Endpoint `chart/historical-price-eod-full` CMG + SPY | CMG & SPY series |
| 4 | **Sharpe & Sortino** | `Sharpe = E[excess daily]·252 / (σ·252)`, `Sortino = E[excess]·252 / downside_dev·252` where downside below risk-free daily rate. Risk‑free for the risk-free short rate from **`economics/treasury-rates`** (3M/2Y) or state assumed rate. | CMG series + Treasury |
| 5 | **Annualized volatility & max drawdown** | `σ_ann = σ_daily·√252`; `drawdown = max peak‑to‑trough decline in price` over 1y. | CMG series |
| 6 | **Earnings‑revision momentum** | Analyze `analyst/financial-estimates` (EPS quarterly sequence) for trend; sign/slope of sequential estimate revisions. | analyst endpoint (CMG) |
| 7 | **Cross-sectional ranking** | z‑score/percentile CMG's EV/EBITDA, P/E, ROIC, net margin, RSI‑momentum vs sector peers. Peers from `company/peers`; multi-factor universe = peers' `key-metrics-ttm` as basis. Rank within sector. | key-metrics-ttm CMG + peers |
| 8 | **Factor score blend** | Weighted of (momentum, value, quality, low‑vol, earnings‑rev) with top-quintile flag logic per my framework. | output of #1–7 |

Return scores table (per your format) with Signal: Buy/Sell. Do **not** invent any ratio — every figure must map to the endpoint above.

## 4. Data Diversion Gaps & caveats

- FMP **Starter-capacity limit** — few calls returned `Tool call limit exceeded`; could not fetch `income-statement-growth` nor **`analyst/price-target-consensus` / `income-statement-growth`** directly. Where these are named above, quant_engineer must re-fetch (rate limit is per-call, not per-token).
- **Split risk (stock-split nonstationarity)**: the 2023→2026 CMG series shows a 50:50 split adjustment. Confirmed raw prices (66.16√ in use. During split in 2024) vs adjusted — we **cannot confirm** the endpoint is auto-adjusted; verify `adjusted` flag before momentum. If `chart/historical-price-eod` returned pre-split values 2023–24, momentum will be severely distorted. Prefer `historical-price-eod-full` and cross-check vs `key-metrics-ttm` (FCF‑per‑share $1.22 imputes a base).
- **Risk-free curve** not fetched (economics nod) — needed for Sharpe/Sortino absolute level; if `economics/treasury-rates` denied, assume explicit (state) 4% and revisit.
- **Cross-sector percentile** needs peers list; `statements/key-metrics-ttm` is only CMG; I have **only** raw CMG series, so quant_engineer must collect peer metrics.

## Summary (attribution-level — NOT a computed score)

- Value factors: **expensive on static multiples** (EV/EBITDA 23x, P/E ~34x); **offset by growth** loaded in price `TTM`.
- Quality: **outstanding** (ROIC ~24%, ROE 53%, 15% op-margin) — likely top-quintile vs sector.
- Momentum: **improving short-term-strong, but structural IT below MAs** — needs RSI/src minimal for Signal.
- Volatility: 30-day std rising; **beta/Sortino/max‑drawdown uncomputed**.
- Composite Signal: **abstain / Buy-skewed pending quant compute** — not determinable from raw inputs alone.

Let me know if you want me to emergency‑fetch any single endpoint (e.g., analyst/consolidated) before the Head routes to engine.
