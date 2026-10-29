# Quant Analyst

- Symbol: STLA
- Elapsed: 87.1s

---
## STLA — Stellantis N.V. | Quantitative Factor Report
**Data as of 2026-10-28 | Price $4.68 | Mkt cap $13.5bn | EV $28.1bn | Reporting ccy EUR | Sector: Consumer Cyclical / Auto Manufacturers**

### 1. Factor Scores

| Factor | Score / Raw | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/B **0.25x**; P/E **−0.6x**; EV/EBITDA **−1.84x**; P/FCF **−0.83x**; Fwd P/E 2026E 9.8x → 2028E 3.5x | Top decile on P/B only; earnings-based multiples **unrankable** (negative) | **Neutral / Value trap** |
| **Momentum** | 12‑1m **−24.6%** (tool); verified 12m total return **−57.0%**; 6m −17.1% | Bottom decile | **Strong Sell** |
| **Quality** | ROE **−41.4%**, ROIC **−22.2%**, Gross profit/assets **−0.0216**, F‑Score **3/9** ("Weak") | Bottom decile | **Strong Sell** |
| **Low Vol** | σ 252d **53.5%** (504d 50.8%), β 1.14, max DD **60.3%** | Bottom decile (highest-risk decile) | **Strong Sell** |
| **Earnings Revision** | Tool: **+16.5%** "upgrade" — **not usable, see note** | — | **Negative (downgrade cycle)** |

**Ranking caveat:** percentile ranks are assigned on a *sector* ("Consumer Cyclical") whose top members are AMZN, TSLA, HD, BABA, TM, MCD — not a valid comparable set. True auto-manufacturer peers (TSLA, TM) were used qualitatively; peer factor scores were not retrievable, so ranks above are directional, not z-score derived.

### 2. Price Statistics

| Metric | 504d (verified) | 252d (reported) |
|---|---|---|
| Annualised return | **−39.3%** | −85.2% ⚠️ *artifact* |
| Annualised vol | 50.8% | 53.5% |
| Beta vs SPY | **1.53** | 1.14 |
| R² | 0.135 | 0.076 |
| Alpha (ann., vs SPY) | **−77.2%** | −96.0% ⚠️ *artifact* |
| Sharpe | **−0.77** | −1.58 ⚠️ |
| Sortino | **−1.09** | −2.01 |
| Max drawdown | — | **−60.3%** |

**Verified price math (closing prices):** $11.31 (2025‑10‑28) → $4.68 (2026‑10‑28) = **−57.0% 12‑month**. Peak-to-trough ≈ $11.31 → $4.06 (2026‑10‑23) = **−64%**; drawdown from the 2024 peak (~$25) ≈ **−81%**. R² of 0.076–0.135 means **beta and alpha are estimated imprecisely** — only 8–14% of STLA's variance is explained by the market. Decouple risk from SPY beta; this is an idiosyncratic, event-driven name.

### 3. Composite Quant Signal: **STRONG SELL**

Four of five factors are decisively negative and the fifth (value) is disqualified. The only "cheap" metrics (P/B 0.25x, 16.5% dividend yield, normalized EV/EBITDA ~2.5x on 2026E) are classic **melting-ice-cube signatures**, not mispricing. There is no factor here that offsets the negative momentum–quality–revision cluster.

### 4. Key Quant Risk Flags

1. **Value trap — multiples are not comparable.** FY2025 net income **−€22.4bn** (EPS −€7.75) on revenue €153.5bn, with **gross profit negative** (−€4.2bn) and operating income −€22.2bn. Negative P/E, EV/EBITDA and P/FCF are **arithmetic artifacts of a ~€10–12bn goodwill impairment** (goodwill €54.4bn → €44.9bn; equity €82.1bn → €54.0bn). Any valuation work must be on normalised/non-GAAP earnings.
2. **The value score is contaminated by an accounting artifact.** The quality model reports accruals ratio **−0.0866** ("good") — but this is purely mechanical: net income is deeply negative from non-cash write-downs while operating CF is only modestly negative. **Do not read this as earnings quality.** ROIC collapsed +20.6% (2023) → +4.6% (2024) → **−22.2% (2025)**.
3. **The earnings-revision "upgrade" is spurious.** The tool compared a **FY2030** estimate ($2.14) to a prior FY2030 figure, based on **n = 1 analyst** — statistically meaningless at a 5-year horizon. **Actual revision direction is sharply negative:** Piper Sandler $38 → $15 → **$4** (double-downgrade to Underweight, July 2026); Morgan Stanley $10.90 → **$5.20** (Underweight, Sep 2026); Evercore $7.50. Consensus price targets have fallen ~70% in nine months and now bracket the spot price.
4. **Dividend yield of 16.5% is a trap, not income.** With a €22bn loss, negative gross profit and €15.8bn net debt, the trailing payout is not covered. Model zero dividend, not 16.5%.
5. **Momentum reversal / gap risk is symmetric and violent.** Daily gaps of **−23.7%** (2026‑02‑06) and **+13%** on 119m shares (2026‑10‑28, ~5x ADV). High 53% vol plus a beta that explains <15% of returns means position sizing, not stop placement, is the only real risk control.
6. **Liquidity is adequate** (ADV ~20–30m shares, ~$100m+) — no illiquidity flag. **Factor crowding is not the risk**; single-name solvency/restructuring risk is.

### Data Integrity Notes
- **The 252-day annualised return (−85.2%), alpha (−96.0%) and Sharpe (−1.58) fail verification.** Closing prices give −57.0% over that window; a −57% return on 54% vol implies Sharpe ≈ **−1.06** and alpha ≈ **−76%**. The 504-day set reproduces my hand calculation almost exactly (−39.3% reported vs −38.8% computed), so **the 504-day risk statistics are the trustworthy ones** and are reported as primary.
- Financials are in **EUR**; price/market cap in **USD** — FX contaminates any cross-currency ratio (EV/EBITDA shown is approximate, ~1.10 USD/EUR).
- FY2025 statements carry a filing date of 2026‑02‑26; my first price pull was truncated at 2026‑02‑20 and was corrected. All metrics above use 2026‑10‑28 data.
