# Quant Analyst

- Symbol: NXT
- Elapsed: 41.3s

---
## NXT (Nextpower Inc.) — Quantitative Factor Report
**Sector:** Energy / Solar | **Price:** $91.13 | **Mkt Cap:** $13.83B | **FYE:** 31-Mar

⚠️ **Data note up front:** NXT's GICS sector is "Energy," whose largest members are XOM/CVX/SHEL. Ranking a solar tracker manufacturer against integrated oil majors is not economically meaningful, so cross-sectional ranks below are computed against the closest true comparables (FSLR, ENPH, ARRY — n=3, small sample; treat as directional, not statistically robust).

### 1. Factor Scores Table

| Factor | Score (0–100) | Sector Rank | Signal |
|--------|--------------|-------------|--------|
| **Value** | 25 | 3 of 3 (worst) | **Bearish** — P/E 23.7, EV/EBITDA 17.2, P/FCF 27.2, P/B 5.96. FSLR at P/E 12.8, EV/EBITDA 8.0, P/FCF 16.5 |
| **Momentum** | 20 | 3 of 3 (worst) | **Bearish** — 12-1M **−17.05%**; 6M −2.89%; 3M −0.47%. FSLR −13.1%, ENPH −8.9% |
| **Quality** | 65 | 1 of 3 (best) | **Bullish, decelerating** — ROE 25.1%, GP/Assets 0.285 (FSLR 0.159, ENPH 0.196), accruals +0.72%. But ROIC 50.6%→38.5%→29.2% |
| **Low Vol** | 10 | 3 of 3 (worst) | **Strongly bearish** — 69.4% ann. vol, β 2.65 (1Y) / 3.10 (6M), max DD **51.1%** |
| **Earnings Revision** | 20 | 3 of 3 | **Bearish (see flag)** — tool reports +10.22% "upgrade" but this is a period-mismatch artifact; 8 of 8 recent PTs were *cuts* |

### 2. Price Statistics

| Metric | 252-day | 126-day |
|---|---|---|
| Alpha (ann., vs SPY) | **−30.76%** | **−87.46%** |
| Beta | 2.66 | 3.10 |
| R² | 0.252 | 0.348 |
| Ann. return | −9.97% | −32.27% |
| Ann. vol | 68.67% (69.44% alt calc) | 63.04% |
| **Sharpe** | **−0.145** | **−0.512** |
| **Sortino** | **−0.258** | **−0.894** |
| Max drawdown | **−51.1%** | — |

**Statistical significance — this matters:** Alpha is *not* reliably distinguishable from zero. Residual (idiosyncratic) vol is ~59% annualised on the 1Y window, giving an alpha t-stat of roughly **−0.5**. On the 6M window t ≈ −1.7, i.e. borderline. R² of only 0.25–0.35 means ~65–75% of NXT's variance is stock-specific, so the fitted alpha is a noisy point estimate. **The correct read is "very high beta and very poor realised return," not "statistically proven negative alpha."**

### 3. Composite Quant Signal: **SELL** (weak conviction)
Weighted composite (Value 20 / Momentum 25 / Quality 25 / LowVol 15 / Revision 15) = **~31/100**.

Only quality scores above median. Four of five factors are bottom-of-group. Not a **Strong Sell** solely because the quality factor is genuinely strong (25% ROE, cash-backed earnings) and solvency is not in question.

### 4. Key Quant Risk Flags

1. **Revision signal is a false positive — highest-priority flag.** `calculate_earnings_revision_score` compares FY2031 EPS ($8.387) to FY2030 ($7.609). These are **different forward periods**, so the +10.22% is simply forecast growth, not a revision of the *same* period. Genuine revision momentum from the price-target tape is unequivocally negative: Susquehanna $150→$145, Roth $175→$140, Needham→$143, Northland→$138, BMO $132→$114, Jefferies $131→$115, Mizuho→$101 (8 cuts, all Oct 2026).
2. **Momentum reversal / decelerating decline.** Returns improve monotonically with shorter horizon (−17.1% → −2.9% → −0.5%), so downside momentum is fading. This is an *early-stage* setup, not a confirmed trend turn — no positive print on any window.
3. **Extreme beta (2.65–3.10) + 69% vol.** Supply-chain shocks, tariffs, and rate moves hit this 10–20x harder than the index. A 51% drawdown already occurred in the past year.
4. **Fundamental deterioration despite headline ROE.** Piotroski F-Score **4 (Weak)**: no ROA improvement, accruals-quality point lost, **share count rising (F7=0)**, no gross-margin or asset-turnover improvement. Accruals swung from −4.9% → −4.6% → **+0.72%**; ROIC down 21pp in two years. Growth is being bought, not earned.
5. **Valuation compression risk on decelerating growth.** Consensus EPS growth: FY27→28 +20%, 28→29 +21%, 29→30 +10%, 30→31 +10%. A 23.7x P/E on a ~10% terminal grower at 69% vol has little cushion. **Caveat: FY2030/31 estimates rest on only 3–4 analysts** — thin sample, low reliability.
6. **Tool inconsistency to note:** `calculate_price_volatility` returns Sharpe 0.038, `calculate_sharpe_sortino` returns −0.145 on the same 252d window — differing annualisation conventions. The −0.145/−0.512 series (mean-daily-based) is the internally consistent one and is what I have used.
7. **Moderate peer correlation** (ARRY 0.65, FSLR 0.52, ENPH 0.44) — meaningful but ~55–77% diversifiable. Liquidity is adequate (~$180M/day).

### Bottom line
Quality is real; price action, valuation, and volatility are not. At 23.7x earnings, a 17% negative 12-1 momentum reading, 69% volatility, beta ~2.7, and eight consecutive analyst target cuts, the quant case is **Sell** — the sole offsetting factor is the 25% ROE, which is itself on a visible downhill slope.
