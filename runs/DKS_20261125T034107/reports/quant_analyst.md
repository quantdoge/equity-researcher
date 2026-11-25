# Quant Analyst

- Symbol: DKS
- Elapsed: 42.7s

---
## DKS — DICK'S Sporting Goods | Quantitative Factor & Risk Report

**Price $153.17 · Mkt cap ~$13.04B (13.62B per profile) · EV ~$19.43B · 85.1M diluted sh · FYE Jan-31**
**Context:** FY2025-26 figures are the first to consolidate the Foot Locker acquisition — this distorts YoY ROE/ROIC, leverage, and FCF, and is the dominant driver of the recent price action.

### 1. Factor Scores Table
Peer set for ranking: ASO, SPWH, TJX, NKE, ROST (n=6 incl. DKS) — **small cross-section; percentiles are indicative only, not statistically robust.**

| Factor | Score (raw) | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E 15.4 · EV/EBITDA 11.5 · P/FCF 32.6 · Div yld 3.24% · P/B 2.35 | **2 / 6** (top tercile) | **Positive** — 2nd cheapest on P/E and EV/EBITDA behind ASO (13.0x / 10.0x). Only P/FCF (32.6x) is mid-pack because FCF is temporarily depressed; 2nd-worst to none — SPWH and TJX/ROST screen far worse on cash flow |
| **Momentum (12-1)** | **−27.21%** | **6 / 6** (worst) | **Strong Negative** — underperforms every peer; ASO at +29.1%. Classic downtrend / falling-knife profile |
| **Quality** | ROE 15.3% · GP/Assets 0.326 · Accruals −3.95% | **4 / 6** (middle) | **Neutral-positive** — tool flags "high" (cash conversion excellent: OCF $1,537M vs NI $849M), but ROE/ROIC have collapsed YoY (ROE 36.4%→15.3%, ROIC 19.2%→10.0%) from deal dilution, and GP/Assets is *lowest* in the peer group |
| **Low Vol** | Ann. vol **55.4%** · Beta 0.731 · Max DD **48.9%** | **6 / 6** (worst) | **Strong Negative** — vol is ~2.1x TJX (26.0%) and 1.8x ROST (30.4%). Beta <1 but total risk is extreme |
| **Earnings Revision** | +10.98% (FY2031 est 19.20 vs prior 17.30) | n/a | **Weak Positive / low confidence** — see flag below |

**Revision caveat (important):** the +11% revision is measured on the **FY2031** consensus, which carries only **3–4 analysts** vs 16 on FY2027. This is a long-dated, thin-coverage estimate, not a near-term revision signal. Near-term census is clean and upward-sloping (FY27 $11.42 → FY28 $12.93 → FY29 $14.79, 8–16 analysts), implying forward P/E of **~13.4x** on FY27 — i.e., value case reinforces. I could not retrieve true 3-month-ago same-period consensus, so treat revision momentum as **unconfirmed**.

### 2. Price Statistics (252 trading days, vs SPY, rf = 0%)
| Metric | Value |
|---|---|
| Annualised return | **−23.11%** |
| Annualised volatility | **55.4–56.3%** |
| Beta (regression) | **0.735** (company-published 5y beta 1.095) |
| Alpha (annualised) | **−25.39%** |
| R² vs SPY | **0.045** |
| Sharpe ratio | **−0.411** |
| Sortino ratio | **−0.452** |
| Max drawdown | **−48.86%** |

**Interpretation:** R² of 0.045 means **only ~4.5% of DKS's variance is market-explained** — this is an almost purely idiosyncratic, event-driven stock right now. The −25.4% alpha carries a very wide standard error (t-stat is roughly in the −1 range given the low R² and 55% vol), so the alpha estimate is directionally negative but **not statistically distinguishable from zero**. Do not treat it as precise. What *is* reliable: the return distribution is bad — negative Sharpe and a Sortino marginally worse than Sharpe indicates downside volatility dominates upside volatility (negative skew).

### 3. Composite Quant Signal: **NEUTRAL (leaning Sell on momentum, Buy on value)**

Weighting the evidence: value (top-tercile, positive) and quality (accruals clean, mid-rank) argue for ownership; momentum (dead last) and low-vol (dead last, 49% drawdown) are the two factors with the strongest empirical track records and both are maximally negative. These offset. Not a Strong Sell because the valuation cushion is real and FCF quality is genuinely high; not a Buy because you are fighting a −27% 12-1 trend with 55% vol and an unhedged integration event.

### 4. Piotroski & Fundamental Cross-Checks
- **F-Score 5/9** (Moderate). Positives: positive ROA, positive OCF, accruals quality, lower leverage, positive equity change. **Failures: no ROA improvement, dilution (F7 = 0), no gross-margin improvement, no asset-turnover improvement** — exactly the deterioration pattern you'd expect post-acquisition.
- **Accruals ratio −3.95%** (FY26) — best quality reading in three years; earnings are cash-backed (OCF/NI = 1.81x).

### 5. Key Quant Risk Flags
1. **Momentum reversal / falling knife** — worst-in-universe 12-1 return; the tool's own signal is "negative." Empirically the single most defensible short/avoid signal in the table.
2. **Volatility regime break** — 55% annualised vol is ~2x its own historical characteristic (published beta 1.095 vs realised regression beta 0.735; the gap signals unstable factor loadings). Any sizing must be vol-scaled; a standard risk-parity weight would be ~40% of a TJX-sized position.
3. **Leverage / integration risk** — EV $19.43B vs $13.04B mkt cap ⇒ **~$6.4B net debt**, roughly 2x LTM EBITDA. Beta *understates* true risk here because deal-specific risk is unsystematic (hence R² 0.045).
4. **Factor crowding** — low. DKS is a contrarian, out-of-favour name; no crowding penalty, but also no catalyst from crowding.
5. **Dividend yield 3.24%** is elevated vs history, which is arithmetically a falling-price artifact, not a payout increase — verify payout sustainability against $1.5B OCF before treating as income support.
6. **Sample-size gaps (disclosed):** peer cross-section n=6; revision signal built on 3–4 analysts on a 5-year-out period; FY2024–2023 ROE/ROIC unavailable (nulls break the 4-year trend); no intraday volume data retrieved, so liquidity is *unassessed* (though a ~$13B cap with $1.5B+ OCF is presumptively liquid).

**Bottom line:** cheap and cash-generative, but momentum, volatility, and drawdown are all bottom-of-universe. The numbers support a **wait-for-price-confirmation** stance: value establishes the floor case, the momentum/vol block establishes why you don't add before the trend stabilises.
