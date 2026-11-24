# Quant Analyst

- Symbol: TSN
- Elapsed: 23.4s

---
# Quantitative Factor Analysis — TSN (Tyson Foods, Inc.)

**Price $62.95 | Mkt Cap $21.7–22.3B | EV ~$29.2B | Consumer Defensive / Agricultural Farm Products**
Data window: 252 trading days. Peer set for ranking = Ag/Food sub-industry (**ADM, BG, HRL, CPB**) — the sector's largest names returned (WMT, COST, KO, PG) are retail/beverage/household and not economically comparable to a protein processor.

## 1. Factor Scores Table

| Factor | Score | Sector Rank (of 5) | Signal |
|--------|-------|--------------------|--------|
| **Value** | 52 / 100 | **3rd** | Neutral |
| **Momentum (12-1)** | 45 / 100 | **2nd** | Neutral (relatively strong, absolutely negative) |
| **Quality** | 28 / 100 | **4th** | Sell / Weak |
| **Low Vol** | 62 / 100 | **2nd** | Buy (relative) |
| **Earnings Revision** | 70 / 100 | n/a | Buy (low confidence — see flag) |

**Value detail:** P/E 49.2x is the *highest* in the peer group (CPB 17.5x, BG 18.7x, HRL 26.5x, ADM 30.3x) — but that ratio is distorted by depressed current earnings. The cash-flow based measures are far more supportive: **P/B 1.26x** (cheapest), **EV/EBITDA 11.8x** (2nd cheapest behind CPB 10.7x), **P/FCF 13.4x = 7.5% FCF yield** (2nd best behind ADM). Genuine asset/cash-flow value, no earnings value.

**Quality detail:** ROE **2.56%** (lowest of 5), ROIC **4.32%**, ROA 1.29%, gross profit/assets 0.092 (above only BG). The one bright spot is accruals **-0.0564** — negative accruals mean cash earnings exceed reported income (earnings quality is clean, not overstated). Piotroski **F-Score 5** (moderate): weak on ROA improvement, equity issuance, gross-margin trend, and dilution.

**Revision detail:** Forward consensus EPS revised **+11.26%** over 3 months ($4.67 → $5.19). Direction is unambiguously bullish — but the referenced forward period is **FY2029**, ~3.6 years out. Long-horizon estimates carry low information content and thin analyst coverage; treat as a weak positive, not a conviction signal.

## 2. Price Statistics

| Metric | Value | Read |
|--------|-------|------|
| Annualised return | **8.39%** | Mediocre absolute |
| Annualised volatility | **29.2%** | High for a staple — ~2x sector norm |
| Beta vs SPY | **-0.32** | Negative / counter-cyclical — *unreliable, see below* |
| Alpha (annualised) | **+10.68%** | Positive, but see R² caveat |
| **R-squared** | **0.032** | **Only 3.2% of variance explained by market** |
| Sharpe ratio | **0.287** | Weak (0% rf) |
| Sortino ratio | **0.456** | Downside better contained than total vol suggests |
| Max drawdown | **-25.27%** | In line with vol; no fat left tail |
| Div yield | **3.27%** | Supported by 7.5% FCF yield |

**Critical statistical caveat:** with R² of 0.032, beta (-0.32) and the +10.7% alpha are **not statistically meaningful** — the standard error on beta swamps the point estimate. TSN's returns are ~97% idiosyncratic (protein-cycle, livestock costs, beef-segment margins), not market-driven. Do not use this beta for cost-of-equity or hedging work. A 252-day single window is also a small sample for stable factor estimation.

## 3. Composite Quant Signal: **NEUTRAL** (composite ≈ 51/100)

The factors point in opposite directions and largely cancel. Genuine deep-value characteristics (1.26x book, 7.5% FCF yield, 3.3% dividend) and relative momentum leadership are offset by bottom-of-peer quality (2.6% ROE, 4.3% ROIC) and a **ROIC that sits below any reasonable cost of capital (~6.5–7%) — i.e., the business is currently destroying economic value on invested capital.** This is a classic "cheap for a reason / cyclical trough" profile, not a clean multi-factor top-quintile name. It is emphatically *not* the rare value + momentum + quality trifecta.

## 4. Key Quant Risk Flags

1. **Negative beta / near-zero R² — model risk.** Any risk model that uses the -0.32 beta for TSN will mis-specify its risk contribution. Treat as its own risk bucket.
2. **Momentum reversal risk.** 12-1 momentum is only -2.1% *because* peers fell much harder (HRL -13%, CPB -10%, BG -9.5%). TSN's relative-strength rank (2nd) is being propped up by peer weakness, not own-price strength — fragile.
3. **Quality/value trap.** Cheapness is driven by trough-cycle earnings; P/E 49x on depressed net income ($453M) means the "value" is contingent on margin recovery that the current ROIC does not evidence.
4. **Leverage.** EV $29.2B vs equity $22.3B → ~$7B net debt on $453M net income; high equity multiplier amplifies the weak ROE.
5. **Factor crowding / thin coverage.** Long-dated FY2029 revision estimate suggests sparse analyst coverage; revision momentum is less reliable than for a large-cap staple.
6. **Small sample size:** 252-day single-window estimation for alpha/beta/Sharpe/Sortino; peer cross-section is 5 names. Ranks are directional, not statistically robust.
