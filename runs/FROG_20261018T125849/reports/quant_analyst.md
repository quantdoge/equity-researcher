# Quant Analyst

- Symbol: FROG
- Elapsed: 39.0s

---
## FROG (JFrog Ltd.) — Quantitative Factor Report
Price $84.31 · Mkt cap $10.21B · EV $9.11B (net cash ~$686M) · Technology / Software–Application

**Peer-set caveat (important):** `get_sector_peers` returns the broad "Technology" sector ranked by size — NVDA/AAPL/MSFT/TSM/AVGO. That is not a valid comparison set for a $10B DevOps vendor, so sector ranks below are computed against a hand-built **DevOps/data-software comp set: GTLB, DDOG, SNOW, CRWD (n=5)**. n=5 is too small for statistically meaningful quintiles; ranks shown are ordinal within this micro-set, not true sector percentiles.

### 1. Factor Scores

| Factor | Score (0–100) | Sector Rank (of comps) | Signal |
|---|---|---|---|
| Value | 25 | 2/5 on P/B (11.04x) & P/FCF (68.9x) — cheapest group is GTLB | **Negative** (expensive; only "relatively" cheap vs a very rich cohort) |
| Momentum | 30 | 2/3 measured (GTLB +45.4%, FROG −2.8%, DDOG −14.5%) | **Negative** — 12-1 = −2.82%, 6-mo = −2.46% |
| Quality | 35 | 3/3 on ROE (−8.09%), 3/3 on GP/assets (0.305), 2/3 on accruals (−0.162) | **Weak** — F-Score 5/9, "low" quality signal |
| Low Vol | 15 | 4/4 — highest vol (75.8%) and highest beta (1.36) in set | **Strongly negative** |
| Earnings Revision | 70 | +25.2% FY28 EPS revision; PTs raised 4× in 3 months | **Positive** |

Supporting data:
- **Value detail:** P/E −136.0 and EV/EBITDA −219.4 (both meaningless — no GAAP profit). P/B 11.04 (BVPS $7.64), P/FCF **68.86 → 1.45% FCF yield**. EV/Sales 17.1x FY25, **14.0x FY26E**, 11.9x FY27E. P/E 86.0x FY26E non-GAAP, 73.6x FY27E.
- **Quality detail:** ROE −8.09%, ROA −5.35%, ROIC −9.92% (worst FY22: −13.5%, so improving 4 yrs straight). Accruals ratio −16.2% is genuinely strong (cash earnings ≫ book earnings). Gross margin eroding: 78.0% (FY23) → 77.1% → 76.8% (FY25). Asset turnover improving. F-Score components fail on ROA<0, leverage, dilution, and gross-margin trend.
- **Revision detail:** FY28 consensus $1.4337 vs $1.1451 three months prior (+25.2%) but **only 2 analysts** contributing — thin, low-confidence. The robust evidence is FY26 $0.980 (13 analysts) / FY27 $1.145 (13) plus price-target actions: Raymond James $80→$120, Truist $105→$110, UBS $120→$125, RBC initiates Outperform $118. Mean PT ≈ $115 → **+36% implied upside**.
- **Growth context:** Revenue FY22 $280.0M → FY25 $531.8M = **23.8% CAGR**; FY25 +24.1%; consensus FY26 +22.6%, FY27 +17.8%. FCF $72.2M → $107.8M → $142.3M (+32.0% in FY25; 26.8% margin). **Rule of 40 = 24.1 + 26.8 = 50.9** — best-in-class on this screen.

### 2. Price Statistics (252-day window, vs SPY)

| Metric | Value |
|---|---|
| Annualised volatility | 75.8% (return-series 76.7%) |
| Beta (OLS) | 1.367 — profile 5Y beta 1.24 |
| R² | **0.0559** — only 5.6% of variance explained by market |
| Alpha (annualised) | +55.4% (see significance flag) |
| Annualised return | 84.9% |
| Sharpe | **1.107** (vol-tool variant 0.987) |
| Sortino | **1.609** → downside dev ≈ 52.8% vs 76.7% total; Sortino/Sharpe 1.45 |
| Max drawdown | **−42.16%** |
| Correlations | GTLB 0.549 · DDOG 0.490 · SNOW 0.394 · MSFT 0.381 |

**Alpha is not statistically significant.** With R² = 0.056, residual vol = 76.7%×√(1−0.056) ≈ **74.5%**; SE of the annualised alpha ≈ 74.5%, giving **t ≈ 0.74**. The +55% alpha is mechanically the by-product of one high-variance year — economically indistinguishable from zero at this sample size. Sharpe/Sortino carry the same caveat: a single 252-day window on a 76%-vol name supports no inferential claim.

### 3. Composite Quant Signal: **NEUTRAL** (composite 39/100)
Weights: Value 20%, Quality 25%, Momentum 20%, Low-Vol 10%, Revision 25% → 0.20(25)+0.25(35)+0.20(30)+0.10(15)+0.25(70) = **38.8**.

The revision upgrade cycle and rule-of-40 economics (+30 pts) are offset by negative momentum, top-quartile-high volatility, no GAAP earnings anchor, and a 1.45% FCF yield. This is a **"good business, wrong factor profile, right story"** setup — not a quant buy, not a short.

### 4. Key Quant Risk Flags

1. **FCF is an SBC artifact — the most important flag.** FY25 SBC **$156.7M (29.5% of revenue)** *exceeds* FCF of $142.3M. SBC-adjusted FCF ≈ **−$14.4M**. Diluted shares 103.3M → 109.7M → 116.2M (**+5.9%/yr**). Quality score and P/FCF 68.9x are therefore overstated; genuine owner-earnings yield is negative.
2. **Data-integrity conflict in the price series.** The Sharpe tool's +84.9% annualised return is irreconcilable with 12-1 momentum of −2.82% (it would imply a ~+90% move in the excluded last month) and with price ($84.31) sitting *below* the $87.87–$98.53 levels at which the Aug–Oct 2026 targets were published. I trust **momentum (−2.8%) and the 42% drawdown** over the return/Sharpe/alpha figures, and I discount the latter accordingly.
3. **Negative price / estimate divergence.** Analysts raised targets four times while the stock fell ~14% from those print levels. Rising estimates + falling price = classic momentum-reversal warning; the market is not validating the revisions.
4. **Momentum reversal & factor crowding.** −2.82% (12-1) and −2.46% (6M) with a 42% peak-to-trough drawdown already realized in 12 months. Correlation to GTLB 0.55 — FROG trades as a levered beta expression of the DevOps group, not on idiosyncratic merit.
5. **High-beta / high-vol sleeve only.** Beta 1.37, vol 76% (4/4 in comps) — must be sized against a drawdown tolerance well beyond 40%, not as a defensive holding.
6. **Thin coverage on the revision signal.** The +25.2% revision rests on 2 analysts and a 3-year-forward period; the FY26/FY27 lines (13 analysts) are the only revision inputs with real statistical support, and those are stable rather than accelerating.
7. **No liquidity flag** — $10.2B cap, 1,800 employees, active trading; proceeds fine.
8. **Small-sample disclaimer (n=5 comps, n=1 annual window):** all ranks above are ordinal within a micro-set. This analysis cannot support fine-grained quintile claims and should not be read as a full cross-sectional factor rank.
