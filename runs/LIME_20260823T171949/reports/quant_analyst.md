# quant_analyst

_2026-08-23T09:30:22+00:00_

# QUANT FACTOR REPORT — LIME (Neutron Holdings, Inc.)

**Ticker:** LIME · NASDAQ · Neutron Holdings, Inc. · Industrials / Rental & Leasing Services
**Data vantage:** 2026-08-21 close (FMP quote timestamp 1787342401). **IPO July 1, 2026 at $25.00.**
**CRITICAL SAMPLE-SIZE FLAG:** LIME's full EOD history is ~37 trading days (~7 weeks). 6M/12M momentum, robust beta, annualized-vol, and Sharpe/Sortino are **statistically unreliable to non-computable** on this window. Everything below that is derived is flagged as a COMPUTE REQUEST, per my remit.

Also flagged up front: FMP's data budget for this session was **exhausted** mid-pull, so several peer/index series I needed were **not retrievable via FMP** (detailed in §5). I used FMP raw data where I had it, and web-sourced company/press figures for fundamentals (clearly cited as such). **No derived statistics appear below as findings** — normalized labels only.

---

## (1) RAW PRICE / MOMENTUM DATA PULLED

### LIME quote — `quote` / `quote`
| Field | Raw value |
|---|---|
| price | **$41.06** |
| previousClose | $42.03 (change $-0.97, **-2.31%**) |
| open | $42.52; dayLow $40.00; dayHigh **$42.84** |
| 52w/ytd high | $42.84 |
| 52w/ytd low | **$23.87** |
| marketCap | **$2,628,905,932** (~$2.63B) |
| priceAvg50 | **$30.809** |
| priceAvg200 | **$30.809** (identical → ≤50 trading days of data; MA structure broken) |
| exchange / volume | NASDAQ / 348,618 |

### LIME EOD closes — `chart` / `historical-price-eod-full` (37 rows)
Latest three rows (raw OHLC close / changePct):
| Date | Close | +/– % |
|---|---|---|
| 2026-08-19 | $37.73 | –2.56% |
| 2026-08-20 | $42.03 | +12.35% |
| 2026-08-21 | $41.06 | –3.43% |

(Full 37-row series saved to `data/lime_price_full.json` for the quant_engineer.)

### LIME RSI(14,1day) — `technicalIndicators` / `relative-strength-index`
Latest raw: **66.94** (2026-08-21); prior 20: 70.18, 62.78 -> **bullish-neutral, not overbought** (23 rows total).

### LIME SMA(200) — `technicalIndicators` / `simple-moving-average`
**not_found** — insufficient history (expected). Short SMA periods (10/20) could still be pulled for a crossover check; **only** the quote's priceAvg50/200 = $30.81 is currently available raw.

### IPO reference (web-sourced)
Listed 7/1/2026 at **$25.00** (range $24–26), day-1 close **$26.02** (+4.1%), ~$182M raised, ~$1.7B valuation (Yahoo Finance / Caproasia / Renaissance Capital).

---

## (2) VOLATILITY POSTURE — POOR / LOW-VOL FACTOR IS NEGATIVE

- **Raw spread:** 52w low $23.87 → 52w high $42.84; current $41.06 is essentially pinned near the post-IPO high.
- **Raw daily moves (July–Aug) are LARGE** (e.g., +12.35% on 8/20, –3.43% on 8/21, –2.56%; these are from `chart` fields). This is clearly a high-dispersion, low-trading-history name, not a low-vol name.
- Low-volatility factor = **disqualifying** on raw evidence: typical daily move >> market. Any annualized std dev is a **COMPUTE REQUEST** and would be statistically thin over ~37 points.
- Drawdown from $42.84 high (raw levels: $41.06) is small in raw spikes but **% drawdown must be computed**, and the day 1-close base ($26.02) to current ($41.06) makes the "peak-to-now" look benign; the raw dispersion underneath is wild. Flagged in §5.

---

## (3) FACTOR ASSESSMENT (momentum / value / quality / low-vol)

| Factor | Posture (raw) | Definability |
|---|---|---|
| Momentum | Strongly positive, but small sample. RSI14 66.94 bullish-not-overbought; price well above both 50/200-day avg ($30.81 raw) and IPO ($25). 1-month footprint-or-returns **computable only from ~4.6 wks**; 6M/12M **undefined**. | Partial — 1M/3M computable, §5 **C1/C2/C7** |
| Value | **UNDEFINED / negative.** 2025 GAAP net loss **–$59.3M**, 2024 –$33.9M (web, S-1/StockTitan). P/E negative (no trailing EPS). EV/EBITDA not pulled (FMP exhausted). Revenue growth +29% FY25, +24% Q2'26 — growth strong, profits absent. | **Definability = No** (unprofitable) |
| Quality | **UNDEFINABLE.** ROIC/ROE and vested capital require positive NOPAT — GAAP unprofitable → factor in real. Gross-profit/assets & accruals not pulled. Positive *operating* income $70.4M (2025) vs GAAP loss = mixed quality signal only. | **No (not computable this session)** |
| Low-volatility | **Negative.** High daily dispersion (raw, §2); annualized SD is a compute request but confidanal drawback is major. | Partial (compute req C3/C4) |
| Earnings-revision momentum | **N/A.** No analyst EPS consensus exists for a 7-wk IPO; `analyst` endpoints not reachable. Treat as blank, not neutral. | No |

**Composite (qualitative leaning, NOT a computed score):** momentum-lifted but statistically unproven, value/quality **undefined** because unprofitable, low-vol poor. The only definable factor (momentum) scores well; the other three are either undefinable or Negative. A final **composite signal cannot be responsibly issued** from raw data alone — see §5 for what to compute first.

---

## (4) PEER COMPARISON

**Peer set — Bird (BRDS) is DEAD:** BRDS was NYSE-suspended (Aug 2023), filed Chapter 11 bankruptcy (2024), last traded ~Feb 2024 at ~$0.05. **Exclude** from the active peer group. Effective micromobility/ride-hail comps = **LYFT, UBER** (+ broader Rental/Logistics not pulled).

### Quotes — `quote` / `quote` (raw)
| Ticker | Price | 52w High | 52w Low | Mcap | avg50 | avg200 |
|---|---|---|---|---|---|---|
| LIME | **41.06** | 42.84 | 23.87 | $2.63B | 30.81 | 30.81 |
| LYFT | 17.47 | 25.54 | 12.46 | $6.63B | 15.56 | 16.21 |
| UBER | 78.80 | 101.99 | 65.41 | $160.4B | 72.92 | 77.10 |

- LIME is the only name that has NEVER paid / earned GAAP; it trades at a **raw premium relative to all-50-day average** (>> peers) because it is a fresh IPO with a tight float. 52w-range setup shows LIME near its 52-week high, LYFT/Uber mid-range — raw only.
- **I could NOT pull LY/UBER EOD return series (FMP budget exhausted)** → compute requests C5/C6 awaiting those series.
- LYFT FY25: revenue $6.3B, net income $2.8B (GAAP, but includes a large one-time benefit — treat single-year as distorted); UBER FY25 revenue $52.0B GAAP net income modest; LIME trailing net loss. So on the *quality/earnings* axis, LIME sits **last** among active peer (negative vs positive), despite the fastest revenue growth. That is the honest cross-resolution: high-growth, low-profitability, high-momentum serial.

---

## (5) EXPLICIT COMPUTE REQUESTS for the QUANT_ENGINEER

Series needed that I could **not pull from FMP this session** (budget exhausted): **characters — LYFT (`chart/y|history-price-eod-full`), UBER (same), SPY / ^SPX (S&P 500 (et `chart` / `indexes`)**. All of the below can be run once those are re-fetched; otherwise block until a fresh pull. Use `data/lime_price_full.json` + `data/lime_rsi14.json` + `lime_quote.json` as the authoritative LIME inputs.

1. **Trailing returns** (COMPUTE): series = LIME daily close, `chart/historical-price-eod-full`; compute 1M, 3M, 6M, 12M simple trailing returns to 2026-08-21; also cumulative total-return from IPO open (7/1 $25.00 → close). Output: % per window. If a window's start date < first close (2026-06..7/1), return NaN and note.
2. **Posture vs MAs:** compare current close ($41.06; `quote`) vs priceAvg50 and priceAvg200 ($30.81); compute %, output dev% per MA, and derive whether 50d mAA post-G(sub) — given avg50==avg200, request a short SMA(10/20) from `technical_indicators/simple-moving-average` LIME if FMP returns it.
3. **Volatility:** from LIME full daily log-returns → annualized std dev (×√252); output annualized σ and n-count. Flag n≈37 as low-significance in the header.
4. **Drawdown:** from 52w high $42.838 (quote) to current $41.06 → % max drawdown (look through daily closes too; output both peak-to-current and peak-to-trough).
5. **Volatility-adjusted / market regressions** — **pending peer/series re-fetch**:
   - OLS beta of LIME daily returns vs returns of SPY/index ^SPX over the *aligned LIME-IPO window* (~37 days). Output $\β$, R², n; if n<30, flag as low-confidence.
   - Correlation: LIME vs LYFT and LIME vs UBER (Pearson and Spearman) over common window (LIME-limited).
   - Sharpe (risk-free → use treasury via `economics` / treasury-rates for the period) & Sortino for LIME over available window.
6. **Cross-sectional rank:** build a 3-name table {LIME, LYFT, UBER} on (a) trailing momentum (use window 1M or 3M, smallest that overlaps LIME), (b) annualized vol, (c) std/risk metrics, output LIME's **rank / strong-quintile position** within the set. Output: rank per factor.
7. **Value/quality viability:** with `statements/metrics-ratios-tTM` (or `key-metrics`) for LIME and peers (re-fetch), compute P/E, EV/EBITDA, P/B. Given GAAP net loss (raw: -$59.3M FY25), expect NaN/robust errors for LIME — verify. Also approximate FCF yield from cash-flow series — expected negative/undefined. Overall output: mark each "definable / undefined" for the factor scores table.
8. **Sector rank context:** LIME has no FMP peer listing (`company/peers` → not_found), so a full R&L-sector rank is **not silable**; note as a gap.

---

## (6) QUANT RISK FLAGS (qualitative, from pulled data)

- **Momentum-reversal risk:** RSI 66.94 ~ +12% single-day spike (8/20) followed by –3.4% (8/21) = frothy, thin-float, routinely reverting. Momentum is positive but fragile.
- **Factor crowding:** the WHOLE case rests on the momentum factor; value/quality (the three durable factors) are **undefined/negative**. Momentum-only crowding = classic fresh-IPO regime.
- **Low liquidity / short-history:** ~7 weeks of data, ~350k share volume, tight float → beta & correlation effectively unreliable; 6M/12M returns **do not exist**.
- **Valuation overhang:** current $41 vs 1) $2.63B cap on GAAP-negative earner; growth real (+29% TS; +24% Q2) but profits 0'.

**Bottom line (no computed composite issued):** Data supports a **positive momentum tilt with very LOW statistical confidence**; value/quality/low-vol are **undefined/negative**. I will **withhold a Strong-Buy composite** pending C1–C8 across re-pulled peer/index series — flagging now that any such score would rest on <40 trading days.
</antml>
