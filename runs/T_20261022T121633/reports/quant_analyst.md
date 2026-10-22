# Quant Analyst

- Symbol: T
- Elapsed: 226.2s

---
## Quantitative Factor Report — AT&T Inc. (NYSE: T)
**Price used: $21.91** | Market cap ~$157B | Enterprise value ~$313B | Sector: Communication Services / Telecommunications Services
Data as of latest close 2026-10-21. All ratios latest FY (12/31/2025).

---

### 1. Factor Scores Table

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | **Strong.** P/E 7.21 · EV/EBITDA 5.72 · P/FCF 8.09 · P/B 1.22 · FCF yield 12.4% · div yield 5.07% | **#2 of 4** telecom peers (CMCSA 4.1x < **T 7.2x** < VZ 10.7x < TMUS 15.8x); top-quintile in broad Comm Svcs | **Positive** |
| **Momentum** | **Weak.** 52-wk price return −10.2% (24.39→21.91); 1-mo −13.0%; −22.0% from 52-wk high 28.10 | **#3 of 4** (12-1: VZ +9.5%, **T ~+1.8%**, CMCSA −2.8%, TMUS −11.0%) | **Negative** |
| **Quality** | **Neutral.** ROE 17.0% · ROA 5.2% · ROIC 8.3% · GP/assets 0.178 · accruals −0.044 · **Piotroski F-score 8/9 (Strong)** | **#3 of 4** (ROE: CMCSA 20.5 > TMUS 18.6 > **T 17.0** > VZ 16.2; GP/A: CMCSA .326 > TMUS .192 > **T .178** > VZ .156) | **Neutral** |
| **Low Vol** | **Mixed.** 252-day ann. vol 29.9% (high in absolute terms); max drawdown −28.9%; beta unreliable (see flags) | **#2 of 4** on beta if 0.43 reported figure used | **Neutral** |
| **Earnings Revision** | **Mixed/negative.** Tool prints +10.1% "upgrade," but this compares the FY2030 estimate ($3.49, **1 analyst**) to FY2029 ($3.17) — a growth rate, not a 3-month revision. Actual price-target changes skew down | — | **Neutral-to-Negative** |

**Peer detail (telecom-services subset, n=4):**

| | P/E | EV/EBITDA | P/FCF | ROE % | GP/Assets | Accruals | 12-1 Mom % |
|---|---|---|---|---|---|---|---|
| **T** | **7.21** | **5.72** | **8.09** | 17.04 | 0.178 | −0.044 | ~+1.8* |
| VZ | 10.73 | 7.67 | 9.37 | 16.24 | 0.156 | −0.049 | +9.5 |
| TMUS | 15.82 | 9.28 | 11.27 | 18.57 | 0.192 | −0.077 | −11.0 |
| CMCSA | 4.10 | 3.91 | 4.17 | 20.54 | 0.326 | −0.050 | −2.8 |

*Recomputed from price series; the factor tool returned +18.9% on a stale window (see flags).

---

### 2. Price Statistics

| Metric | Value | Note |
|---|---|---|
| Alpha (ann., vs SPY) | **+8.63%** | Statistically hollow — see R² |
| Beta (vs SPY) | **−0.476** | **Not credible**; reported 5Y beta = **0.431** |
| R² | **0.043** | Only 4.3% of variance explained → alpha/beta estimates are noise |
| Sharpe (252d) | **−0.02** | Ann. return −0.6%, vol 30.4% |
| Sortino (252d) | **−0.025** | Downside/deviation ≈ total vol; little cushion |
| Annualised volatility | **29.9%** | Elevated for a telecom |
| Max drawdown | **−28.9%** | 28.10 (3/27/26) → 19.98 (7/1/26), close basis |
| Current drawdown | **−22.0%** | From 52-wk high |
| 52-wk range (close) | 19.98 – 28.10 | |

**Reconciliation of return figures:** the Sharpe/Sortino tool's −0.6% annualised return is directionally consistent with the raw series (actual 12-month price return **−10.2%**); the `price_volatility` Sharpe of +0.035 uses a different (older) window. Treat **Sharpe ≈ −0.02** as the working figure. Positive alpha despite a negative absolute return is arithmetically possible here because a negative beta implies a negative benchmark-predicted return — it is an artifact of an unstable regression, not evidence of outperformance.

---

### 3. Composite Quant Signal: **NEUTRAL**

Deep value (top-quintile cheapness, 12.4% FCF yield, 5.1% dividend) and a Strong Piotroski F-score of 8/9 are offset by decisively negative momentum and deteriorating sell-side sentiment. This is a **cheap-but-falling** profile — the valuation case is real, but the tape is actively working against it. Not a Strong Sell given the valuation floor and cash-flow support; not a Buy until momentum stabilises. Net: **Neutral**.

---

### 4. Key Quant Risk Flags

1. **Momentum reversal risk — SEVERE.** Stock peaked at 28.10 on 3/27/26 and has since fallen 22% to 21.91. Two gap-downs on 3–6× normal volume: 10/9/26 (−9.8%, 150.5M shares vs ~30M avg) and 10/21/26 (−6.4%, 84.5M shares). 1-month return −13.0%, 3-month −0.5%. The trend structure is lower highs. **The tool's +18.9% momentum is stale and should be ignored**; recomputed 12-1 momentum is only **+1.8%** and near-term momentum is sharply negative.
2. **Value-trap risk.** P/E 7.2x and 5.1% yield look compelling, but the multiple has stayed low for years — this is structurally cheap (low growth, high leverage), not a mispricing waiting to close. CMCSA at 4.1x shows how much cheaper the space can get.
3. **Leverage / rate sensitivity.** Net debt ≈ **$156B** (EV $313B − mkt cap $157B). EV/EBITDA 5.7x is moderate, but the absolute debt load makes the equity highly sensitive to rate moves — a key driver of the drawdowns.
4. **Beta estimate is broken.** Computed beta **−0.476** with R² = 0.043 is statistically insignificant and economically implausible for a regulated telecom. Reported 5Y beta **0.431** is the credible figure; classify T as low-beta/defensive, but do not use the regression output for risk budgeting.
5. **Earnings-revision metric is methodologically flawed.** The +10.1% "upgrade" compares the FY2030 consensus ($3.49, **n=1 analyst**) against FY2029 — not the same period 3 months apart. Genuine revision depth sits at FY2027 (n=12). Recent target actions skew negative: Barclays $24→$21 (−12.5%), Goldman $30→$27, Scotiabank $29.25→$27.50→$26.50, Bernstein **downgrade to Market Perform** ($24). Counterweights: Wolfe and BNP upgrades to Outperform, KeyBanc $36, Morgan Stanley $25→$27. Median target ≈ $26.5 vs $21.91 spot (~+21%), but the direction of revisions is down.
6. **Sector-rank sample is small (n=4).** The broad Communication Services peer list is dominated by internet/media names (GOOG, META, NFLX) with entirely different economics; only VZ, TMUS and CMCSA are true telecom comparables. Ranks above are relative to that 4-name set — not statistically robust.
7. **Quality signal conflict.** Factor model flags quality "low" (driven by thin 17.8% gross margin, a structural telecom trait), yet Piotroski F-score is 8/9 and ROE rose from 9.1% (2024) to 17.0% (2025). The accruals ratio is negative (−0.044), i.e. cash earnings exceed reported earnings — a genuine positive. Treat "low quality" as margin-structure, not earnings-manipulation, risk.

---

**Bottom line:** Attractive on valuation and cash generation, but the quantitative momentum and revision signals are pointing down, with fresh negative catalysts driving high-volume breakdowns. Neutral — wait for momentum to base before adding.
