# Quant Analyst

- Symbol: HPE
- Elapsed: 43.5s

---
## HPE — Quantitative Factor Report
Hewlett Packard Enterprise · Technology / Computer Hardware · Price **$40.19** · Mkt cap ~$58.1B (1,445M dil. sh.) · FY end Oct-31

**Data note up front:** the 12-1 momentum, Sharpe and alpha figures below are computed on a 252-day window that *includes* the Jul–Oct 2026 melt-up but whose "skip most recent month" rule **excludes** the Nov crash. I have therefore cross-checked every trend measure against raw daily data (Oct–Nov 2026), and I override where the window is stale. That override is the single most important judgment in this report.

### 1. Factor Scores Table

| Factor | Score | Sector Rank (of 6 hardware peers) | Signal |
|---|---|---|---|
| **Value** | **85 / 100** | **2 / 6** | **Strong Buy** — cheapest on EV/EBITDA & P/FCF |
| **Momentum** | **30 / 100** | **5 / 6** | **Sell** — 12-1 looks +5.9%, but trailing 1M is −31.6% |
| **Quality** | **40 / 100** | **5 / 6** | Negative — low GP/A, dilution, high leverage |
| **Low Vol** | **15 / 100** | **5 / 6** | Strong Sell — 72.4% vol, β 2.44, −45.3% DD |
| **Earnings Revision** | **35 / 100** | n/a | Deteriorating — tool's "+14.15%" is a horizon artifact |

**Value (85).** P/E 13.09, EV/EBITDA **8.49**, P/FCF 15.04. Ranks 3rd/6 on P/E, **2nd on EV/EBITDA** (only SMCI cheaper at 5.52), **1st on P/FCF**. Peer set: DELL 34.0/18.7/23.6 · NTAP 25.7/16.3/17.5 · STX 34.7/26.7/35.6 · WDC 11.3/20.9/29.9 · SMCI 6.9/5.5/neg. HPE is a genuine outlier on cash-flow-based value — the one factor that scores well.

**Momentum (30) — the tool is wrong here, and it matters.** `calculate_momentum_score` returns **+5.86%** ("positive"), but that window ends ~21 trading days before the last print. Raw closes: **$73.46 (Oct 9 high) → $40.19 (Nov 24) = −45.3%**. Trailing 1-month (Oct 26 $58.72 → $40.19) = **−31.6%**; from Oct 1 ($64.58) = **−37.8%**. Peers over the same 12-1 window: NTAP +11.7%, DELL +4.8% — HPE is mid-pack on the stale metric and **worst-in-class on the live metric**. Every trend overlay I run on the post-peak series is negative.

**Quality (40).** ROE 16.05% and accruals −0.0241 (clean, cash-backed — OCF $6.57B vs NI $4.43B) are fine; Piotroski **F=7** ("Moderate") with improvement in ROA, gross margin and asset turnover. But **gross profit/assets 0.1997 is the lowest of the six peers** (NTAP 0.456, STX 0.557, WDC 0.455, DELL 0.224), F-score fails on **leverage (F5=0)** and **share issuance (F7=0)** — diluted 1,445M vs basic 1,335M, ~8% dilution. Tool verdict: quality signal "low."

**Low Vol (15).** Annualised vol **72.4%**, β **2.442** vs SPY, max drawdown **45.29%** — and that drawdown *is the present one*, not a historical event: the stock is sitting essentially at its trough. Only DELL (92.7% vol, β 2.82) is more volatile.

**Earnings Revision (35) — flag the artifact.** The tool reports +14.15% "upgrade," but it is comparing the **FY2029** consensus (6.543, **only 2 analysts**) against **5.73213**, which is *exactly* the current FY2028 estimate. This is a **fiscal-horizon roll, not a revision** — the +14.15% is simply implied FY2028→FY2029 EPS growth. Real revision evidence points the other way:
- Nov 24 (one day): Susquehanna **$70→$55**, Piper Sandler **$54**, Wells Fargo **$50** — three cuts, "concerns linger on growth and margins."
- Oct 14: Barclays **downgraded to Equal Weight**.
- FY2026 diluted EPS came in at **$3.07** (0.31 + 0.44 + 1.06 + 1.26) vs consensus **$3.836** — a material miss, which is the proximate cause of the −45% drawdown.

### 2. Price Statistics

| Metric | Value | Read |
|---|---|---|
| Alpha (annualised, vs SPY) | **+83.63%** | Statistically fragile — see R² |
| Beta (1y daily, vs SPY) | **2.455** | Extremely high; profile beta 1.466 is a 5y monthly figure |
| R² | **0.294** | **Only 29% of variance explained** — alpha has a very wide standard error; do not underwrite it |
| Annualised return | 116.11% | Window captures a single extraordinary run; not repeatable |
| Annualised vol | 73.21% | ~4.6× SPY implied |
| **Sharpe** | **1.586** | Backward-looking; flattered by the pre-Nov melt-up |
| **Sortino** | **2.512** | Downside dev 46.2% < total vol 73.2% → positive skew *historically* |
| Max drawdown | **−45.29%** | Occurring **now**, at the trough |
| Corr vs SPY | 0.540 | |
| Corr vs DELL / NTAP / STX / WDC | **0.733** / 0.683 / 0.487 / 0.478 | Heavy crowding in the DELL/NTAP hardware complex |

Note the **Sharpe/Sortino–drawdown inconsistency**: a 1.59 Sharpe alongside a 45% drawdown that is unresolved means the risk-adjusted metrics describe a distribution HPE no longer trades in. Treat both as low-confidence.

### 3. Composite Quant Signal

Weights: Value 25% · Momentum 25% · Quality 20% · Low Vol 15% · Revision 15%
→ (85×.25) + (30×.25) + (40×.20) + (15×.15) + (35×.15) = **44.3 / 100**

## **NEUTRAL (with a negative trend bias)**
Genuine deep-value score (2/6, cheapest on EV/EBITDA and P/FCF at 8.5× and 15.0×) is fully offset by bottom-quintile quality, bottom-quintile low-vol, and an active momentum collapse. This is the classic **value-trap signature**: cheap for a reason, deteriorating on every other axis. The 12-month-forward P/E of **8.1×** (FY2027E EPS $4.97) is only attractive *if* a +62% EPS step-up over TTM $3.07 is delivered — the recent miss and PT cuts argue for scepticism. A trend overlay alone would rate this **Sell**.

### 4. Key Quant Risk Flags

1. **Momentum reversal risk — trigger already fired.** −45.3% from the Oct 9 peak, with **capitulation volume**: 44.9M and 46.8M shares on Nov 23–24 vs a ~15M ADV (3× normal). Distribution, not accumulation. The 12-1 factor score is **stale and will roll negative** within one month as the crash enters the window — expect mechanical momentum-fund selling.
2. **Earnings revision signal is an artifact — do not trade it.** +14.15% rests on **2 analyst estimates** for a FY2029 period and is a horizon roll, not a revision. Sample size is far below any significance threshold.
3. **Factor crowding.** 0.733 correlation with DELL and 0.683 with NTAP means HPE offers little diversification against the AI-server/hardware trade — this is a high-beta proxy, not a value hedge (β 2.455).
4. **Leverage and dilution.** F-score F5=0 (leverage rising) and F7=0 (8% dilution, 1,445M vs 1,335M shares). Interest expense appeared on the P&L in Q1/Q2 FY2026 after being zero in Q3 — consistent with acquisition-related debt (the revenue step-up to $46.7B FY2026 from a ~$30B base implies a large deal). Balance-sheet integration risk is real.
5. **Estimate dispersion is enormous.** FY2027E EPS range **$4.68–$5.49**; FY2029E **$5.62–$7.47** on 2 analysts. With PTs reset to $50–55 against a $40.19 price, the Street's own view is 25–37% above spot — but those same targets were $70–77 in October. Target credibility is low.
6. **Liquidity: NOT a concern.** ~$720M ADV. The problem is *direction* of volume, not depth.
7. **Data inconsistency to note:** profile beta 1.466 vs computed 1.455–2.455 (5y-monthly vs 1y-daily); profile market cap $53.3B vs $58.1B from 1,445M × $40.19. Minor, but the beta gap means vol-sensitive sizing should use the 2.44 figure.

**Bottom line:** the numbers do not support the value story on a risk-adjusted basis. HPE ranks 2/6 on value and 5/6 on momentum, quality and low-vol simultaneously — the definition of a cheap-but-broken screen. Neutral, and I would not add until either (a) the momentum factor prints a positive turn on *live* data, or (b) gross profit/assets and leverage inflect — neither is present today. **Small-sample caveat:** 252-day single-regime window, 2-analyst revision data, and R²=0.294 mean the alpha and Sharpe figures should not be treated as statistically significant.
