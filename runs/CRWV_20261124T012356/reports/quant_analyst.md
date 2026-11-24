# Quant Analyst

- Symbol: CRWV
- Elapsed: 44.3s

---
## CRWV — Quantitative Factor Report
**Price used: $48.33 (close 2026‑11‑23) · Market cap $21.0B · EV $46.9B · Sector: Technology / Software‑Infrastructure · IPO 2025‑03‑28**

> **Data integrity note (resolved):** the profile "price" of $48.33 initially looked stale against a $89.25 print — it is not. The live snapshot is late‑Nov 2026, and $48.33 reconciles exactly with EV/EBITDA (46.87/2.468 = 19.0x) and P/B (48.33/7.67 = 6.3x). All multiples below are current. Analyst‑estimates endpoint unavailable on plan; revision score comes from the factor tool only.

### 1. Factor Scores

| Factor | Score (raw) | Sector Rank* | Signal |
|---|---|---|---|
| **Value** | P/E −17.2x · P/B 6.3x · EV/EBITDA 19.0x · P/FCF −2.9x | 10 / 10 (bottom) | **Strong Sell** |
| **Momentum** | 12‑1 = −47.6% · 6M −54.2% · 3M −44.0% · 1M −10.9% | 10 / 10 (bottom) | **Strong Sell** |
| **Quality** | ROE −35.0% · ROIC −0.14% · GP/Assets 7.5% · Piotroski 5/9 | 9 / 10 | **Sell** |
| **Low Vol** | Ann. vol 103.6% · β 3.48 · max DD 71.4% (252d) | 10 / 10 (bottom) | **Strong Sell** |
| **Earnings Revision** | FY2030 EPS $19.59 vs $6.98 = **+180.5%** | n/a (see caveat) | *Nominal Buy — reject* |

\*Ranked against the 10 largest Technology peers (AAPL, NVDA, MSFT, TSM, AVGO, ANT, SKHY, MU, AMD, ASML). Caveat: that comp set is a mega‑cap cohort ($0.5–5T) — a $21B name is structurally penalised on Value/Quality/Low‑Vol, so treat ranks as directional, not precise.

**Positive only:** accruals ratio −0.0857 (cash flow exceeds net income — genuinely clean, and improving from −0.20 → −0.09). Accruals quality is the one factor where CRWV screens well.

### 2. Price Statistics

| Metric | 252d | 127d |
|---|---|---|
| Annualised return | **−41.9%** | −113.7% |
| Alpha vs SPY (ann.) | **−63.2%** | −112.6% |
| Beta vs SPY | **3.48** | 3.96 |
| R² | 0.29 | 0.35 |
| Sharpe | **−0.40** | −0.98 |
| Sortino | **−0.73** | −1.88 |
| Annualised vol | 103.6% | 116.0% |
| Max drawdown | 71.4% (252d) | — |

- **Full‑history drawdown is worse than reported:** close‑to‑close $183.58 (2025‑06‑20) → $39.51 (2026‑11‑20) = **−78.5%**; intraday $187.00 → $39.28 = −79.0%. The 71.4% figure only covers the post‑Nov‑2025 window and misses the June 2025 peak.
- Correlations (252d): NVDA 0.53 · MU 0.55 · AMD 0.52 · SPY 0.54 · MSFT 0.25.
- **Statistical significance — read carefully:** beta 3.48 is significant (t ≈ 10). **Alpha is NOT.** Residual vol is 87.6% ann. (252d) and 93.6% (127d), giving SE(alpha) of ~88% and ~132% respectively → t ≈ −0.7 and −0.9. The −63% alpha is economically alarming but statistically indistinguishable from zero. Do not cite it as a proven skill/anti‑skill estimate. Likewise 127d annualised return of −113.7% is a short‑window artefact of a 116% vol name, not a forecast.

### 3. The Revision Conflict (the report's key finding)

The factor tool's **+180.5% EPS upgrade is not tradeable information.** It compares a **FY2030** consensus ($19.59) to its level three months prior — a five‑year‑out estimate with negligible analyst coverage and no near‑term earnings in the denominator. It should be rejected.

The authoritative revision evidence points the other way. All 10 recent price targets, struck at $44–60 (i.e. at today's price), were **lowered**: Morgan Stanley $99→$70, UBS $120→$105, Cantor $100, Mizuho $68, Stifel $60, DA Davidson $45, Raymond James $75, Argus $100 — with headlines citing "AI‑Cloud sector derating" and "reduced risk appetite." Median PT $87.50, mean $89.80 (+86% vs spot) — but a *falling* target distribution. **Direction of revision is negative; level is stale.** Score the revision factor as **Sell**, overriding the tool.

### 4. Fundamental Stress Test (what the factors are actually pricing)

- Revenue $5.13B (+168% YoY), gross margin **71.7%** — the business is scaling and high‑margin.
- But: net income **−$1.17B**, D&A $2.45B, **interest expense $1.23B** = **50% of the $2.47B EBITDA** consumed by interest. EBIT/interest = 0.01x.
- Total debt $29.8B; **net debt/EBITDA 10.5x**; debt/equity 8.9x; current ratio **0.46** (negative working capital).
- Piotroski 5/9 fails on: negative ROA, **dilution (shares 218M → 435M)**, gross‑margin trend, asset turnover.

This is a leveraged, dilutive capex story priced at 19x EV/EBITDA with negative FCF. The factor stack is not a mispricing — it is correctly identifying duration risk.

### 5. Composite Quant Signal: **SELL**

Four of five factors sit in the sector's bottom decile; value, momentum, quality and low‑vol all point the same direction with no offsetting factor support. I stop short of Strong Sell only because (a) the nominal revision signal is positive, and (b) the 71.7% gross margin and 168% revenue growth rule out a broken‑business thesis — this is a de‑rating, not a deterioration.

### 6. Key Quant Risk Flags

1. **Momentum reversal / squeeze risk (high):** −78.5% from the peak, then **+22.3% in a single session** (2026‑11‑20 → 11‑23, on 94M shares). Shorting a 104%‑vol name at a capitulation low carries violent gap risk. Suggest sizing at ≤⅓ normal weight, or expressing via puts.
2. **Factor crowding — inverse:** the *crowded* trade is long AI‑infrastructure. Multiple underwriters explicitly de‑rated the whole "AI‑Cloud" complex simultaneously, meaning CRWV's −0.55 correlation to MU/AMD/NVDA is not diversification — it is **shared factor exposure**. Cross‑sectional risk is concentrated, not spread.
3. **Liquidity: adequate, not a constraint.** ~$3.6B ADV at $48; 94M‑share days confirm depth. This is a volatility risk, not a liquidity risk.
4. **Beta instability & model risk:** beta 3.5 (252d) → 4.0 (127d) → 7.7 (vendor field). With R² of only 0.29–0.35, beta explains a third of variance; hedging with SPY leaves ~88% residual vol unhedged. Any beta‑neutral construction here is largely fictional.
5. **Sample size:** ~20 months of trading history, all of it either IPO ramp or de‑rating. Every statistic above is one regime. No factor conclusion here has survived a full cycle.
6. **Refinancing/rate sensitivity:** 10.5x net leverage with 50% of EBITDA to interest — a rate or covenant shock is the dominant tail risk and is not captured by any price factor.

*What would flip the signal to Neutral/Buy: two consecutive quarters of consensus **PT and near‑term EPS** revisions turning up (not FY2030), net leverage below 6x, and momentum turning positive on a 3‑month basis.*
