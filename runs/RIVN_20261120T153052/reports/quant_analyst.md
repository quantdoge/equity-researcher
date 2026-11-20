# Quant Analyst

- Symbol: RIVN
- Elapsed: 30.3s

---
## RIVN — Quantitative Factor & Risk Report

**Rivian Automotive, Inc.** | Consumer Cyclical / Auto Manufacturers | Price $12.18 (last close 2026-11-13) | Mkt cap ~$14.4B | Beta 1.64–1.78

⚠️ **Data caveat up front:** the ratio engine used a price of $10.91–10.93 while the OHLCV tape closes at **$12.18** on 2026-11-13, and market cap is quoted as both $12.96B (1,186M sh × $10.93) and $15.88B. Multiples below inherit this ~11% price uncertainty; all price-derived stats (momentum, alpha, Sharpe) are computed off the tape and are internally consistent.

### 1. Factor Scores

| Factor | Score | Sector Rank (of 5 auto OEMs) | Signal |
|---|---|---|---|
| **Value** | 2 / 10 | 4th | Sell — P/E −3.56, EV/EBITDA −5.28, P/FCF −5.21 (FCF yield **−19.2%**), P/B **2.82** vs BVPS $3.87. EV/Sales 2.51x. Only name with *both* negative earnings and negative FCF yield. |
| **Momentum** | 1 / 10 | 5th (worst) | Strong Sell — 12-1 momentum **−25.2%**. −45.7% from Dec-2025 close high ($22.45), only +6.6% off the Oct-2026 low ($11.43). |
| **Quality** | 1 / 10 | 5th (worst) | Strong Sell — ROE **−79.4%**, ROIC **−31.9%**, ROA −24.5%, GP/Assets **0.97%** (TSLA 12.4%, GM 7.1%). Piotroski **4/9** (Weak). |
| **Low Vol** | 1 / 10 | 5th (worst) | Strong Sell — 66.6% ann. vol (peers 27–47%), beta 1.77 (only TSLA higher), max DD −45.7%. |
| **Earnings Revision** | 4 / 10 | 2nd | Weak positive, low confidence — see caveat below. |

**Earnings revision — the +210% headline is a measurement artifact.** The tool compared FY2030 EPS of **+$0.53** against the FY2029 estimate of **−$0.48**. That is a *cross-fiscal-year* comparison, not a same-period revision, and the positive sign flip makes the percentage meaningless. Both figures also rest on only **4 analysts** (vs 10–21 for revenue) — statistically insignificant.
- What *is* real: consensus loss path narrows **−1.91 (FY27) → −1.36 (FY28) → −0.48 (FY29) → +0.53 (FY30)**; breakeven pushed out to ~FY2030 on an implied ~40% revenue CAGR ($11.6B FY27 → $31.2B FY30).
- Price-target trend is **rolling over**: Jul-2026 notes were all raises (RBC $14→16, MS $13→14, WF $15→16, UBS $16→17, DA Davidson $14→15); the latest 2026-10-30 notes include **cuts** (Cantor →$16, Needham →$18). Median PT ~$16.5 = +35% implied upside — the sole bullish input in the model.

### 2. Cross-Sectional Peer Ranking

| Metric | RIVN | TSLA | GM | F | TM |
|---|---|---|---|---|---|
| 12-1 Momentum | **−25.2%** | +9.5% | −11.9% | −16.5% | +6.1% |
| Ann. Vol | **66.6%** | 47.3% | 34.4% | 39.1% | 27.4% |
| Beta | **1.77** | 2.11 | 1.05 | 0.99 | 0.36 |
| GP/Assets | **0.97%** | 12.4% | 7.1% | 7.9% | 8.0% |
| ROE | **−79.4%** | 4.6% | 4.3% | −22.7% | 9.7% |
| P/FCF | **−5.2x** | 205.8x | 7.2x | 3.7x | 1.5x |

RIVN ranks **last on momentum, quality and low-vol, 4th on value** — a bottom-quintile score on 4 of 5 factors. No peer is similarly bad on all axes simultaneously. *(TM's P/E of 0.07 is a bad data point — excluded from value ranking.)*

### 3. Price Statistics (252-day window)

| Metric | Value |
|---|---|
| Annualised return | **−24.0%** |
| Alpha (ann., vs SPY) | **−26.35%** |
| Beta (OLS) | **1.776** (R² **0.151**) |
| Beta (profile) | 1.644 |
| Ann. volatility | **59.3%** (returns) / **66.6%** (vol engine) |
| Sharpe | **−0.405** (−0.253 alt. window) |
| Sortino | **−0.574** |
| Max drawdown | **−45.7%** |
| 52-wk range (close) | $11.43 – $22.45 |
| ADTV | ~30M sh / **~$365M** |

**Interpretation:** R² of 0.15 means only **15% of RIVN's variance is market beta** — this is a narrative/idiosyncratic instrument, not a beta vehicle. Negative alpha of −26% on beta 1.78 is the worst combination available: you are paid nothing for market exposure and lose heavily on the residual. Sortino/Sharpe = 1.42 indicates downside deviation (41.7%) is *below* total vol — the volatility is genuinely two-sided (see the +14% run from $11.43 to $14.06 in five sessions), so short positioning carries violent squeeze risk.

### 4. Composite Quant Signal: **SELL**

Equal-weighted composite: **1.8 / 10**. Four of five factors sit in the bottom quintile with no offsetting value support (a loss-making company cannot be "cheap" on earnings, and P/B of 2.82 is *not* distressed). I stop short of **Strong Sell** only because fundamentals are inflecting directionally: gross margin turned positive (**+2.7% in FY2025 vs −24.1% FY2024, −45.8% FY2023**), revenue +8.4% to $5.39B, net loss narrowed to −$3.65B from −$4.75B, and Piotroski F-score is 4 rather than 1–2. The tape, however, has not begun to price any of that.

### 5. Key Quant Risk Flags

1. **Momentum reversal / downtrend persistence.** −25% 12-1 momentum with price below the entire 2026 trend. Momentum is the single most robust cross-sectional factor; RIVN is on the wrong side of it.
2. **Dilution is the dominant risk, and it is not in the ratios.** Shares outstanding **+17.1% in one year** (1,013M → 1,186M); Piotroski F7 = 0. Per-share value creation is being diluted faster than operating improvement accrues. Any "cheapness" on forward numbers assumes no further issuance.
3. **Balance-sheet runway is finite.** Cash & ST investments **$6.08B** (−21% y/y), total debt **$6.65B**, net debt **$3.07B** (up from $0.44B). OCF −$779M plus capex implies ongoing external funding need — the equity is structurally a call option on capital markets.
4. **Beta of 1.78 with R² of 0.15 = no diversification value.** Correlation to SPY 0.387, TSLA 0.361, GM 0.311, F 0.298. Low correlation is only attractive if the standalone Sharpe is positive; at **−0.405** it is not. Worst-of-both-worlds risk profile.
5. **Factor crowding: LOW — not a crowded short.** Low peer correlation and high idiosyncratic share mean positioning is not consensus-crowded. The offsetting risk is squeeze: 66% vol cuts both ways.
6. **Liquidity: NOT a constraint.** ~$365M daily dollar volume, ~1.19B shares. Any size can be traded; the risk here is price, not slippage.
7. **Small-sample warnings.** FY2030 EPS consensus = **4 analysts**; FY2030 revenue spread $26.3B–$34.8B (±14%). Alpha/beta R² 0.151 and the 252-day window give wide confidence intervals on alpha (±~8pp at 95%). The earnings-revision score should be treated as **no information**, not as a bullish signal.

**Bottom line:** Every factor that survives rigorous measurement — momentum, quality, low-vol, value-on-book — says avoid. The only supportive evidence is directional margin improvement and analyst PT upside, both of which are forward-looking narrative inputs that the cross-section has repeatedly refused to reward. **Sell**; the position is a financing-risk trade, not a factor trade.
