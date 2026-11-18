# Quant Analyst

- Symbol: ARM
- Elapsed: 25.1s

---
## ARM Holdings (ARM) — Quantitative Factor Scorecard

**Sector:** Technology / Semiconductors · **Price:** $183.39 · **Mkt cap:** ~$195.9B · **IPO:** 2023-09-14 (~2.3 yrs public history)

---

### 1. Factor Scores Table

Peer set = NVDA, AVGO, AMD, MU, TSM (+ARM). TSM valuation data is corrupted (P/E 1.09, EV/EBITDA −0.07) and is **excluded from value ranking** → value ranks out of 5.

| Factor | Raw Score / Inputs | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E **215.8x**, EV/EBITDA **137.1x**, P/FCF **200.1x**, P/B 23.6x, fwd P/E 81.8x (FY27E $2.24) | **5 of 5 (worst)** | **Strong Sell** |
| **Momentum** | 12-1m **−17.47%**; 6m **−8.59%**; SPY −0.27% | **5 of 6** (only AVGO −20.7% worse) | **Sell** |
| **Quality** | ROE 10.9%, ROIC 10.4%, GP/A **0.425** (3rd), accruals **−0.058** (2nd best); F-Score **6/9** | **3 of 6 (mid)** | **Neutral** |
| **Low Vol** | Vol **91.2%**, beta **3.83**, max DD **−62.1%** | **6 of 6 (worst)** | **Strong Sell** |
| **Earnings Revision** | Tool: +71.3% "upgrade" — **invalid**, see flag | n/a | **Neutral/Negative** |

**Peer context (why ranks matter):** MU 9.6x P/E · NVDA 31.7x · AVGO 71.6x · AMD 190.0x · **ARM 215.8x**. ARM is the most expensive name in the group on *every* one of P/E, EV/EBITDA and P/FCF, while earning the *lowest* ROE (10.9%) outside AMD. MU delivers 61% ROE at 9.6x; ARM delivers 11% ROE at 216x. That is the single most damning cross-sectional fact in this screen.

**⚠️ Earnings Revision — data integrity failure.** The tool reports a +71.3% upgrade by comparing $10.724 EPS **FY2031** against $6.260 **FY2030**. Those are *different forward periods*, not a revision of the same period — the "upgrade" is just embedded 5-yr growth (and FY2031 carries 18 analysts with a $9.84–$11.66 spread). I would not use it. The genuine revision evidence is negative: on 2026-11-05, **5 of 6** notes were price-target **cuts** (TD Cowen→$250, RBC→$300, Piper→$270, Wells Fargo→$255, Barclays→$325; Needham reiterated $255). Median target $262.5 (+43% vs spot), but the *direction* is down — revisions are being marked down into the print.

---

### 2. Price Statistics

| Metric | 252-day | 126-day |
|---|---|---|
| Annualised return | **+91.4%** | **−123.5%** |
| Annualised vol | 92.8% | 85.2% |
| **Alpha (ann., vs SPY)** | **+55.8%** | **−134.3%** |
| **Beta (vs SPY)** | **3.85** | 3.75 |
| R² | 0.370 | 0.385 |
| **Sharpe** | **0.984** | **−1.449** |
| **Sortino** | **1.853** | **−2.544** |
| Max drawdown | **−62.1%** | — |

**The headline Sharpe of 0.98 is a trap.** It is a trailing-12-month artifact of a first-half melt-up; the most recent 6 months annualise to −123% with a −1.45 Sharpe and −2.54 Sortino. The two windows disagree by ~200 points of annualised return and ~190 points of alpha — that is not a stable return stream, it is a boom-bust. Beta 3.85 with R² of only 0.37 means **63% of variance is idiosyncratic**: ARM is not a market proxy, it is a leveraged narrative bet. Note the vendor-reported beta of 3.94 in the profile corroborates the regression, but this magnitude reflects extreme event-driven swings, not a durable sensitivity.

---

### 3. Composite Quant Signal: **SELL (Underweight)**

Crude z-composite across the five factors: Value −1.5, Momentum −1.0, Quality 0.0, Low Vol −1.5, Revision −0.5 → **mean ≈ −0.9 (Sell)**.

Rationale: zero valuation support, bottom-quintile momentum, and worst-in-class volatility, with only mid-pack quality (decent GP/A 0.425 and negative accruals −0.058 are genuine positives — earnings are cash-backed) as an offset. This is the classic profile of a stock whose fundamentals are respectable but whose *price* has already discounted a decade of perfection. Quality does not pay when you overpay for it by 20x.

### 4. Key Quant Risk Flags

1. **Momentum reversal / crash risk — HIGH.** Negative 12-1 momentum (−17.5%), negative 6m (−8.6%), 6m Sharpe −1.45. Falling-knife characteristics; no trend support.
2. **Beta/vol blowup — HIGH.** 91% vol, beta 3.85, −62% max drawdown. Any position must be sized at ~1/4 of a market-beta-equivalent; a 50bp portfolio weight carries ~1.9% portfolio beta contribution.
3. **Valuation downside convexity — HIGH.** 216x earnings, 200x FCF, 24x book for 10.9% ROE. No multiple floor; de-rating risk is the dominant path.
4. **Theme crowding.** ARM screens as a quality-momentum AI name on GP/A and accruals; crowded ownership plus a 3.85 beta means sector rotation transmits violently.
5. **Revision direction contradicts the model.** Target cuts (5 of 6 same day) vs the tool's spurious +71% "upgrade."
6. **Statistical reliability — LOW.** Only ~2.3 years of trading history; no full cycle. Beta, alpha, Sharpe all flip sign across windows, so **do not treat any single-window statistic as a stable estimate**. Beta 3.85 in particular should be treated as an unstable point estimate with wide error bands.
7. **Peer data caveat:** TSM valuation ratios failed integrity checks and were dropped from ranking; peer sample of 5 is below the ~10 needed for meaningful quintile assignment — treat ranks as *tercile/ordinal* guidance, not precise quintiles.
