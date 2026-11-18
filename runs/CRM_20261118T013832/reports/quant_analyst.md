# Quant Analyst

- Symbol: CRM
- Elapsed: 56.7s

---
# CRM (Salesforce, Inc.) — Quantitative Factor Report
**Sector:** Technology / Software–Application · **Price used:** $183.90 (last close 2026-02-20) · **Mkt cap:** ~$176B

⚠️ **Data-integrity preamble:** the vendor price used by the valuation module ($194.52, as of FY-end 2026-01-31) is stale vs. the price history ($183.90). I recomputed all multiples off $183.90. More seriously, the risk module's return/Sharpe series does not reconcile with the observed price path — details in §2 and §4. Beta estimates are also internally inconsistent with the company's own reported beta (1.24). These are flagged, not hidden.

---

## 1. Factor Scores

| Factor | Score | Sector Rank (of 6 large-cap software) | Signal |
|---|---|---|---|
| **Value** | P/E 23.6x, EV/EBITDA 14.0x, P/FCF 12.2x, FCF yield 8.2%, P/B 2.97x | **4 / 6** (median-to-below) | Neutral |
| **Momentum** | 12-1 return **+23.0%** | **1 / 6** | Strongly positive — *but breaking down* |
| **Quality** | ROE 12.6%, GP/Assets 0.287, Accruals −0.067 | **5 / 6** | Negative (vendor flags "low") |
| **Low Vol** | Vol 50.9%, MaxDD 28.2%, beta 0.29 (unreliable) | **3 / 6** | Neutral |
| **Earnings Revision** | +19.95% (FY2031 est.) | n/a (not computed for peers) | Positive, **low confidence** |

**Peer cross-section (raw inputs):**

| | CRM | MSFT | NOW | ORCL | ADBE | INTU |
|---|---|---|---|---|---|---|
| P/E | 23.6 | 28.2 | 55.6 | 19.7 | **14.1** | 19.5 |
| EV/EBITDA | 14.0 | 18.4 | 31.1 | 13.7 | **10.3** | 12.7 |
| P/FCF | 12.2 | 56.3 | 21.3 | n.m. | **10.2** | 10.3 |
| ROE % | **12.6** | 30.2 | 13.5 | 39.7 | 61.3 | 24.0 |
| GP/Assets | 0.287 | 0.297 | 0.395 | 0.169 | **0.719** | 0.467 |
| Accruals | −0.067 | −0.065 | −0.142 | −0.057 | −0.098 | −0.116 |
| 12-1 Mom % | **+23.0** | +5.3 | +17.3 | −12.9 | −6.0 | +0.7 |
| Ann. Vol % | 50.9 | **34.4** | 69.1 | 60.8 | 43.8 | 53.8 |
| Max DD % | 28.2 | **23.4** | 41.6 | 53.5 | 31.8 | 46.8 |

**Read:** CRM is a *momentum-only* story. It is mid-pack on value, bottom-quartile on quality (lowest ROE in the group, only now earning its cost of capital: ROIC 10.9% vs. 1.4% three years ago), and only "low vol" relative to a high-vol peer set — 50.9% absolute vol is high for a $176B software name. It is **not** the rare top-quintile-on-value-and-quality-and-momentum profile.

**Supporting detail:** Piotroski F-Score **7/9** (moderate) — fails *lower leverage* and *equity issuance* (buyback-driven; share count still ~956M). Accruals deeply negative (−6.7%), i.e. cash earnings well ahead of GAAP — a genuine quality positive. ROIC path: 1.4% → 6.9% → 9.9% → **10.9%**. Dividend yield 0.89%.

---

## 2. Price Statistics

| Metric | 252-day | 126-day |
|---|---|---|
| Alpha (ann., vs SPY) | **+11.03%** | +55.35% |
| Beta vs SPY | 0.29 | 0.46 |
| R² | **0.0068** | 0.0143 |
| Annualised vol | 50.85% | 53.87% |
| Max drawdown | −28.19% | −26.31% |
| Sharpe (0% rf, vendor) | **0.391** | 1.444 |
| Sortino (vendor) | **0.762** | 3.098 |

**Statistical significance: alpha is not significant.** With residual vol ≈51% and R² = 0.7%, the t-stat on annualised alpha is ~0.2 (252d) and ~0.7 (126d). Sample: n=252, one year, single regime. This is noise, not skill.

**Reconciliation of the return series (important):** the vendor reports +20.07% annualised return (252d) and +79.17% (126d). The observed path contradicts this — CRM went from $248.19 (2025-08-01) to $183.90 (2026-02-20), **−25.9%**, and 6-month momentum ex-last-21 is **−5.0%**. Reconstructed 12-month total return from the momentum factors: 1.2296 × 0.8414 − 1 ≈ **+3.5%**. On that return, **Sharpe ≈ 0.07, not 0.391** (Sortino correspondingly far below 0.76). I treat the vendor Sharpe/Sortino as unreliable and would not cite them in a thesis.

**Beta is unreliable.** OLS beta 0.29–0.46 with R² <1.5% and SPY correlation of just **0.082** is implausible for a mega-cap software name (true beta ~1.2; vendor profile beta = **1.238**). Use the peer-derived alternative: CRM's correlation of **0.74 with NOW and 0.74 with ADBE** means its effective risk factor is *application software*, not the index. It is an idiosyncratic, high-vol, rate/software-sentiment trade.

---

## 3. Composite Quant Signal: **NEUTRAL** (negative tilt)

Score: momentum +1, value 0, quality −1, low-vol 0, revisions +0.5 (discounted for data quality) → composite ≈ **−0.1σ**, i.e. market-weight.

The single reason this is not a Buy is the **momentum break**: the +23.0% 12-1 score is entirely a trailing artifact. The stock is **−15.9% over the last 21 sessions** ($218.57 → $183.90) and −5.0% over six months ex-that month. Quality and value give no cushion to offset a momentum unwind.

Context: median sell-side target ~$250 (range $225–$315), implying ~+36% upside — but all six notes carry publish dates of Sep–Oct **2026**, i.e. *forward-dated relative to the price history*. Treat as a stale/anomalous dataset point, not a live consensus.

---

## 4. Key Quant Risk Flags

1. **Momentum reversal risk — HIGH.** Classic rollover signature: strong 12-1, negative 6-month, −16% in one month. This is the dominant risk in the profile.
2. **Quality gap — MEDIUM.** ROIC 10.9% barely clears cost of capital; lowest ROE in peer set. If the multiple compresses, there is no quality floor (contrast ADBE: ROE 61%, GP/A 0.72).
3. **Factor crowding — MEDIUM.** 0.74 correlation to both NOW and ADBE. CRM offers ~zero diversification against an application-software de-rating.
4. **Data integrity — HIGH (methodological).** Beta (0.29 vs. reported 1.24), R² of 0.7%, annualised return/Sharpe mismatch, and an **earnings-estimate curve that is non-monotonic** (FY2027 $16.75 > FY2028 $16.07 vs. FY2026 actual ~$7.80 — a >2x jump that is internally incoherent, likely a GAAP/non-GAAP or vendor-scaling error). The **+19.95% revision score rests on FY2031 estimates with only 8–10 analysts** and falling coverage with horizon. I weight it at roughly half credit.
5. **Liquidity — LOW.** No concern (~10M shares/day, deep mega-cap).

**Bottom line:** quantitatively CRM is a cheap-ish, cash-generative, low-quality-trend name whose sole live factor support (momentum) has just failed. Neutral until either momentum re-bases (a reclaim of the $210–218 area) or the value/quality spread versus ADBE/INTU narrows.
