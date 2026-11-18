# Quant Analyst

- Symbol: AS
- Elapsed: 53.1s

---
# Amer Sports, Inc. (AS) — Quantitative Factor & Risk Report

**Price $30.24 (close 2026‑11‑17) · Mkt cap ~$17.0B · EV ~$18.1B · Consumer Cyclical / Leisure · IPO 2024‑02‑01 (Helsinki‑based; Wilson, Arc'teryx, Salomon)**

---

## 1. Factor Scores Table

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | 1/5 (composite z ≈ −0.9) | **4th of 5** | Bearish |
| **Momentum** | 1/5 | **4th of 5** | Bearish |
| **Quality** | 2/5 | **5th of 5** | Bearish |
| **Low Vol** | 2/5 | **3rd of 5** | Neutral–Bearish |
| **Earnings Revision** | n/d | n/d | Unmeasurable (tool artifact) — target drift negative |

*Rank basis: hand‑built 5‑name athletic/footwear comp set (AS, NKE, DECK, ONON, LULU). The vendor "sector peers" list for AS is mega‑cap Consumer Cyclical (AMZN, TSLA, HD, MCD…), which is **not** a valid comparables universe for a $17B sporting‑goods company — I did not use it for ranking.*

### Factor detail

| Metric | AS | Comps (NKE / DECK / ONON / LULU) | AS rank |
|---|---|---|---|
| P/E | **39.8** | 17.1 / 11.6 / 52.2 / 7.9 | 4th (2nd dearest) |
| EV/EBITDA | **16.4** | 12.1 / 7.4 / 28.8 / 4.5 | 4th |
| P/FCF | **33.8** | 24.3 / 10.8 / 42.0 / 13.5 | 4th |
| P/B | **2.92** | 3.58 / 4.75 / 6.50 / 2.50 | 2nd cheapest |
| 12‑1 momentum | **−16.2%** | −9.1 / −10.3 / −8.7 / −21.8 | 4th |
| ROE | **7.34%** | 20.9 / 41.0 / 12.5 / 31.8 | **5th** |
| Gross profit/assets | **0.376** | 0.518 / 0.856 / 0.667 / 0.743 | **5th** |
| Accruals | **−0.030** | +0.006 / −0.043 / −0.042 / −0.003 | 2nd best |
| Ann. vol (252d) | **40.2%** | 35.9 / 37.7 / 49.6 / 46.6 | 3rd lowest |
| Beta vs SPY | **1.29** (252d) / **1.45** (504d) | 0.66 / 1.10 / 1.21 / 0.94 | **highest** |
| Max DD | **−37.4%** | −47.0 / −35.9 / −45.9 / −51.0 | 2nd best |

**Piotroski F‑Score 7/9 (Moderate).** Positives: positive ROA, positive operating CF, ROA improvement, low accruals, positive equity change, gross‑margin improvement, asset‑turnover improvement. Failures: **F5 leverage increased**, **F7 dilution** (diluted shares 501.7M → 563.1M, **+12.2% YoY**).
**ROIC trend: 0.8% → 4.7% → 7.3% → 9.0% (2022‑2025)** — genuine, monotonic capital‑efficiency improvement. Pre‑IPO ROE of 133%/342% is an artifact of a near‑zero equity base; **exclude from quality assessment.**

---

## 2. Price Statistics (primary = 504‑day window)

| Statistic | 504d | 252d |
|---|---|---|
| Annualised return | **−6.91%** | — |
| Annualised vol | 40.13% | 40.2% |
| Beta vs SPY | **1.453** | 1.286 |
| **Alpha (annualised)** | **−29.55%** | — |
| R² vs SPY | 0.222 | — |
| **Sharpe** | **−0.172** | −0.662 |
| **Sortino** | **−0.304** | — |
| Max drawdown | −37.39% | −37.39% |

**Alpha is not statistically significant.** Idiosyncratic vol = 40.13% × √(1−0.222) = 35.4%; SE(α) over 2 yrs ≈ 25.0% → **t ≈ −1.2**. With R² of only 0.22, 78% of AS's variance is company‑specific, so the regression gives almost no reliable market‑adjusted signal. **Treat beta 1.29/1.45 as a rough range, not an anchor** (vendor 5‑yr beta of 1.97 is unusable post‑IPO).

**Sortino (−0.304) is materially worse than Sharpe (−0.172)** → downside deviation exceeds total‑return‑implied deviation; returns are left‑tail heavy.

**Verified from raw adjusted closes:** 12‑month return **−1.7%**; 2026 YTD **−19.0%**; **−27.9%** from the 2026‑02‑20 peak ($41.96); +125.7% since IPO ($13.40); 6‑month **−10.6%**. Trend structure = lower highs (42.0 → 37.5 → 33.0 → 28.5 → 32.5), i.e. an intact downtrend with a weak bounce off $26.27 (Sep‑2026).

---

## 3. Composite Quant Signal: **NEUTRAL (tilt negative, ≈ −0.6σ)**

Bottom‑half on all four priced factors, and **last** on quality — but two things block a Sell:

1. **The multiple is a trailing artifact.** FY2025A EPS $0.76 → FY2026E $1.307 (**+72%**). At $30.24 that is **23.1x FY26E** and **18.4x FY27E**, versus a trailing P/E of 39.8x. Forward EV/EBITDA is **12.1x** (FY26E EBITDA $1.49B), not 16.4x. The stock is dearest‑in‑class only on stale earnings.
2. **The de‑rating has already happened:** −28% from peak, F‑Score 7, accruals negative, ROIC up 180bp YoY, and consensus targets clustering at **$42 median (10 notes, +38.9% upside; mean $43.3)**, range $31 (Morgan Stanley, Equalweight) to $62 (UBS, May — stale).

**On pure factor ranks this screens Sell; forward earnings power and the completed de‑rating hold it at Neutral.**

---

## 4. Key Quant Risk Flags

1. **Sample size / statistical validity — SEVERE.** Only ~1.8 years of trading history (IPO 2024‑02‑01). No full cycle, no recession beta, no stable factor loadings. Alpha t‑stat ≈ −1.2; **no price statistic here is statistically robust.** All ranks should be treated as low confidence.
2. **Window‑label inconsistency in the stat endpoints.** The 252‑day Sharpe (−0.662) implies a 252‑day return of ≈ −26.6%, which is **not reproducible** from the raw series (12‑month return is −1.7%). Only the 504‑day block is internally consistent — its max drawdown (−37.39%) reproduces exactly from the 41.96 → 26.27 close‑to‑close. **Use the 504‑day set; discount the 252‑day Sharpe.**
3. **Sector momentum reversal risk — high, and it is systemic not idiosyncratic.** *Every* name in the comp set has negative 12‑1 momentum (−8.7% to −21.8%). This is an athletic‑apparel/footwear factor de‑rating, not an AS story. AS has the **highest beta in the peer set** to that factor → highest downside if it continues, strongest snap‑back if it reverses.
4. **Quality trap risk.** Lowest ROE and lowest gross‑profit‑to‑assets of the five. Goodwill‑heavy post‑LBO balance sheet (P/B 2.92 on BVPS $10.34). If gross margin or Arc'teryx/China growth decelerates, there is no quality cushion beneath the multiple.
5. **Earnings‑revision factor is broken — do not use.** The tool reported "+20.9% upgrade," but that compares **FY2030E ($2.95) to FY2029E ($2.44)** — adjacent fiscal years, not a revision of the same forward period. No historical estimate vintages were available, so **true revision breadth is unmeasurable.** Best available proxy: **price‑target drift is negative** — Goldman cut $48→$43 (Sep), and the price‑at‑publication of targets has slid from $35.2 (May) to $31.1 (Nov).
6. **Dilution.** +12.2% diluted shares YoY (F‑Score F7 = 0) erodes per‑share compounding; leverage also rose (F5 = 0).
7. **Event/gap risk.** Earnings days move 15‑20% on 10‑20M shares (2025‑05‑20: +19% on 19.8M; 2026‑02‑24: 11.1M). Liquidity itself is *not* a constraint (~$150‑250M ADTV).
8. **Correlations (252d):** DECK 0.65, ONON 0.59, SPY 0.46, NKE 0.40. Pairing AS with DECK/ONON adds little diversification; AS is an idiosyncratic, high‑vol single‑name bet.

**Bottom line for the memo:** AS is a **negative‑momentum, high‑beta, low‑quality‑rank, expensive‑on‑trailing‑numbers growth‑recovery name** with genuinely improving capital returns and a heavily discounted forward multiple. The quant case is **Neutral, not constructive** — it needs either a stabilization in 12‑1 momentum or evidence of upward *same‑period* EPS revisions (currently unobservable) before the factor stack can turn. Cheapest‑looking argument (18.4x FY27E) is a forecast, not a fact.
