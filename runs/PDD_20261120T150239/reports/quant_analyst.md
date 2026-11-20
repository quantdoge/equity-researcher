# Quant Analyst

- Symbol: PDD
- Elapsed: 40.8s

---
## PDD Holdings Inc. (PDD) — Quantitative Factor Report
**Price $86.43 | Mkt cap $128.2B (1,482.4M diluted shares) | Sector: Consumer Cyclical / Specialty Retail | Reporting currency: CNY**

### ⚠️ Data Integrity Flag (read first)
The vendor ratio engine returns **P/E 1.33, P/B 0.31, EV/EBITDA –2.96, EV –$362.8B**. These are **artifacts**, not values — it divides a *USD* market cap by *CNY* earnings/equity/cash. Same defect appears in BABA (P/E 1.92, P/FCF –4.0). All ratios below are **recomputed** at CNY/USD ≈ 7.15, and BABA peer comparisons corrected the same way. The negative "EV" is real in *direction* (net cash) but ~7× too large.

---

### 1. Factor Scores Table

| Factor | Score (raw) | Sector Rank (of 5 comps) | Signal |
|---|---|---|---|
| **Value** | P/E **9.4x** · P/B **2.21x** · EV/EBITDA **3.5x** · EV/Sales **0.99x** · EV/NI **4.3x** · P/FCF ~9.0x | **1 / 5** (cheapest) | **Strong Buy** |
| **Momentum** | 12-1 return **–6.09%** | **2 / 5** | Neutral (weak, but least-bad) |
| **Quality** | ROE 23.57% · ROIC 22.14% · GP/Assets 0.386 · Accruals **–1.44%** · F-Score **5/9** | **3 / 5** | Neutral (good level, negative trend) |
| **Low Vol** | Ann. vol **36.1%** (252d) / 33.0% (504d) · Beta **0.281** | **3 / 5** vol · **1 / 5** beta | Neutral — low beta, *high* idio vol |
| **Earnings Revision** | **–7.56%** (flagged downgrade) · FY25 actual EPS 65.24 vs 75.18 cons. = **–13.2% miss** | **4 / 5** | **Sell** |

**Comp-set, corrected valuation:** PDD 9.4x < BABA ~13.7x < TJX 28.8x < AMZN 36.2x < ABNB 43.4x.
**Note on ranks:** N=5 comp set pulled from vendor sector list (AMZN, BABA, TJX, ABNB + PDD). These are 1-of-5 ordinal ranks, **not** true sector quintiles — treat as directional only.

**Revision caveat:** the tool's "prior estimate" of 96.51 for FY2029 is identical to the current FY2028 row — a **period-alignment artifact**, so the –7.56% is not a clean apples-to-apples 3-month revision. The *independent* confirmation of downgrade pressure is the FY25 miss (–13.2%). Consensus curve: FY26 69.85 → FY27 83.51 → FY28 96.51, i.e. the street still models **reacceleration**, with FY28 dispersion of 72.4–118.6 (±24%, 16 analysts) — high disagreement.

---

### 2. Price Statistics

| Metric | 504d (2yr) | 252d (1yr) |
|---|---|---|
| Annualised return | **–6.55%** | — |
| Annualised vol | 33.02% | 36.11% |
| **Beta vs SPY** | **0.624** | 0.281 |
| **Alpha (annualised)** | **–13.41%** | — |
| **R² vs SPY** | **0.06** | — |
| **Sharpe** | **–0.197** | –0.496 |
| **Sortino** | **–0.296** | — |
| Max drawdown | **–46.93%** | –31.43% |

**Statistical significance (this matters):**
- **R² = 0.06** → SPY explains only 6% of PDD's variance. PDD is **94% idiosyncratic**. It is not a market-beta instrument; the profile's stated beta of –0.008 is a different-window artifact and should not be used.
- **Beta 0.624 is significant** (SE ≈ 0.11, t ≈ 5.7, n=504 daily obs).
- **Alpha –13.4% is NOT significant** (annualised residual vol ≈ 32%; t ≈ –0.6 over a 2-year window). **Do not present alpha as evidence of underperformance** — 2 years is too short a sample against 33% vol. Direction is negative; confidence is low.
- Negative Sharpe *and* negative Sortino, with |Sortino| > |Sharpe| → downside deviation < total vol (normal), but the return is negative so both ratios are uninformative about quality, only about direction.
- **Max DD –46.9%** over 2 years is the dominant risk fact.

---

### 3. Composite Quant Signal: **NEUTRAL** (valuation-driven, not momentum-confirmed)

Weighted rank ≈ 3.2 of 5. Value is top-decile cheap and quality is above-water, but **two of five factors are negative** and ROIC is rolling over. Per framework discipline, the numbers that argue *against* a Buy win on trend.

**The genuine bull case (why this isn't a Sell):**
- Net cash **CNY 491.1B** ($68.7B) = **54% of market cap**. Core operating business trades at ~$59.5B EV against $13.7B net income.
- Accruals **–1.44%** (and negative all four years: –1.9%, –9.8%, –7.2%) → earnings are cash-backed, **not** accounting-inflated. This is the single highest-quality datapoint in the file.
- ROIC 22.1% with **zero long-term debt**.

**The bear case (why not a Buy):**
- ROIC 22.1% vs 33.5% (FY24) and 29.7% (FY23) — **~1,130bp of ROIC compression in two years**.
- Momentum negative, revisions negative, –47% drawdown, F-Score 5/9 with **zero** points on ROA improvement, gross margin improvement, asset turnover improvement, or dilution.
- This is the textbook **value-trap signature**: cheap, cash-rich, decelerating.

---

### 4. Key Quant Risk Flags

1. **Value-trap risk (highest).** Valuation rank 1/5 paired with momentum rank 2/5 and revisions 4/5. Cheap + deteriorating + no catalyst = multiple can stay compressed.
2. **Momentum reversal / trend persistence.** 12-1 of –6.09% sits inside a –46.9% two-year drawdown. Negative 12-1 has weak but positive continuation tendency; no reversal trigger identified.
3. **Data/liquidity/structural.** Beta estimate unstable across windows (0.281 → 0.624 → –0.008); 94% idiosyncratic variance means peer-hedged or sector-neutral positioning will **not** neutralize the risk.
4. **Currency / ADR / policy.** CNY functional reporting into a US-listed ADR. Every multiple requires an FX assumption; the vendor feed is demonstrably unreliable on this name. Geopolitical/ADR delisting and China stimulus-policy sensitivity are unmodeled binary risks.
5. **Factor crowding — LOW.** Correlation with BABA 0.557 (the only meaningful link); AMZN 0.150, TJX 0.092, SPY 0.113. No evidence of a crowded quant position; the name is treated as a China-internet proxy, not a global retail comp.
6. **Estimate dispersion.** FY28 EPS range 72.4–118.6 (±24%) on 16 analysts. Any single-point EPS estimate carries ~±25% error.

**Bottom line:** a statistically cheap, cash-hedged, cash-generative business with a real quality base, offset by a genuine fundamental deceleration and negative price/revision momentum. **Neutral** — the valuation is compensation for the ROIC decline, not a mispricing to exploit until revisions stabilize. Alpha is not statistically established at n=504 days.
