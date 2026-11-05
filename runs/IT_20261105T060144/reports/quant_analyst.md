# Quant Analyst

- Symbol: IT
- Elapsed: 84.8s

---
## Gartner, Inc. (IT) — Quantitative Factor Report
**Price $207.19 (2026-11-04) · Mkt cap $14.9B · EV $16.8B · No dividend**

### 0. Data-integrity note (read first)
Three of the tool outputs are **materially mis-specified** and I have corrected them from the raw tape:

| Tool output | Problem | Corrected reading |
|---|---|---|
| Momentum "+19.21% (252d)" | The value reproduces a ~3-month window ($155.84 → $185.77), not 12-1 | **12-1 momentum = −18.6%** ($227.17 → $184.92) |
| Earnings revision "+22.58% upgrade" | Compares **2030E EPS $29.11** (2 analysts) to **2029E EPS $23.75** (3) — different fiscal years, not a revision | **Signal invalid**; see §3 |
| Beta 0.086 (252d) / 0.495 (504d), R² 0.0003/0.0115 | R²≈0 ⇒ alpha and beta are **not identified**; daily series dominated by earnings gaps | Use published 5Y β **0.95**; treat daily β as unmeasurable |

The price series itself is clean and confirms a genuine collapse: peak close **$551.80** (2024-11-13) → trough close **$125.73** (2026-06-22) = **−77.2%**, now $207.19.

### 1. Factor Scores

| Factor | Score (percentile est.) | Sector Rank* | Signal |
|---|---|---|---|
| Value | ~82 | ~2–3 of 13 | **Positive.** 21.5x TTM P/E, **13.9x 2026E**, 13.7x EV/EBITDA, 12.7x P/FCF, FCF yield 7.9% — cheapest in comp set (CSCO 21.3x EV/EBITDA & 32.4x P/FCF; ORCL 14.5x, P/FCF negative). P/B 46.7x is an artifact of $320M book equity. |
| Momentum | ~22 | ~10 of 13 | **Negative.** 12-1 = −18.6%; 12M = −8.8%; YTD = −17.9%; −38.5% vs pre-gap $336.71. Offsetting: +40.3% 6M, +11.5% 3M, +12.1% 1M; price 15% above ~200DMA (~$180) and 8% above ~50DMA (~$192). Trend repair, not trend leadership. |
| Quality | ~68 | ~5 of 13 | **Positive but deteriorating.** GP/assets 54.4% (strong), accruals **−6.9%** (cash earnings > net income — high quality), ROIC **26.1%**, F-score 5/9. But ROIC 33.0%→27.2%→26.1% (2023-25), op margin 20.9%→18.5%→**15.8%**, net income $1,254M→**$729M** (−42%), FCF $1,383M→$1,175M. ROE 227.9% is a leverage artifact. |
| Low Vol | ~3 | ~13 of 13 | **Strongly negative.** 252d vol **59.3–63.6%**, 504d 56.5%; max DD −45.8% (252d) / **−71.9%** (504d). ~4 earnings gaps (>13% each: −27.6%, +22.6%, −20.9%, −13.2%) explain roughly half of realized variance; **ex-gap vol est. ~30–35%**. |
| Earnings Revision | n/a | n/a | **Unmeasurable / mildly negative.** FY25 actual EPS **$9.65 vs $12.78 consensus = −24.5% miss**. 2026E $14.93 implies +55% EPS on **−1.0% revenue** ($6.43B vs $6.50B actual) — internally inconsistent, low credibility. PT direction mixed: raises at BMO $231, Truist $235→**downgrade to Hold, PT $210 (Nov 4)**, WF $175, MS $182, UBS $208. Median PT ~$208.5 = **+0.6% upside**. |

\*Rank is vs. the returned "Technology" peer list, which is entirely mega-cap semis/software (AAPL, NVDA, MSFT, TSM…). No true IT-services comps (ACN, CTSH, INFY) were available — **cross-sectional ranks are therefore indicative only and likely flatter IT on value and quality.**

### 2. Price Statistics

| Metric | 252d | 504d |
|---|---|---|
| Alpha (ann., vs SPY) | **+4.34%** | **−46.05%** |
| Beta | 0.086 (R² 0.0003) | 0.495 (R² 0.0115) |
| Ann. return | +55.07% (tool) | −35.29% |
| Ann. vol | 59.29% | 56.45–56.94% |
| Sharpe | **+0.929** | **−0.620 / −0.644** |
| Sortino | **+1.627** | **−0.733** |
| Max drawdown | −45.8% | −71.9% (close-to-close **−77.2%**) |

**None of the risk-adjusted statistics are trustworthy.** The 252d Sharpe of +0.93 sits alongside a raw −8.8% twelve-month price change — a contradiction that means the return series the tool used does not span the window it reports. The 504d figures (−0.62 Sharpe, −46% alpha) are directionally right but statistically empty: with R² of 0.0003–0.0115, the standard error on beta (~±0.15 even at best) swamps the point estimate, and alpha's t-stat is indistinguishable from zero. The published 5Y β of 0.95 is the only beta worth quoting.

### 3. Composite Quant Signal: **NEUTRAL** (value-tilted, no momentum/revision confirmation)
Scoring value +82 and quality +68 against momentum +22, low-vol +3 and an unmeasurable revision signal lands the composite at **Neutral**, not Buy. The setup is a classic **cheap-for-a-reason** profile: 7.9% FCF yield and 13.9x forward earnings against a −18.6% 12-1 momentum reading, a 25% consensus miss, and a downward-sloping margin trend. Cheapness on a depressed 2025 earnings base can be a trap — the P/E of 21.5x is optically high precisely because earnings fell 42%. Upgrade trigger: 12-1 momentum > 0 plus at least two consecutive quarters of positive EPS revisions. Downgrade trigger: another consensus miss or net debt/EBITDA > 2.0x.

### 4. Key Quant Risk Flags
1. **Event/gap risk dominates.** Four >13% single-day moves in 13 months and a −13.2% reaction on 3.2M shares (Nov 3, 2026). Realized vol is not a diversifiable risk factor — it is earnings binary risk. Any vol-targeted or risk-parity sizing will systematically underweight (or be whipsawed by) this name.
2. **Momentum reversal risk, both ways.** The +40% six-month rebound off the June low ($125.73) is exactly the short-term reversal pattern that 12-1 momentum deliberately excludes; a −18.6% 12-1 reading with a +12% one-month reading is a fragile configuration.
3. **Leverage and buyback-funded shrinkage.** Net debt more than doubled to **$1.90B** (1.54x EBITDA); total debt +25% to $3.62B while **$1.99B of buybacks ran 1.7x FCF** ($1.18B). Book equity $320M, tangible equity **−$2.76B**, current ratio 1.00. Goodwill is 38% of assets.
4. **Estimate/analyst data too thin for inference.** 2 analysts on 2030, 7 on 2026; 2025 consensus missed by 24.5%. Any revision-based signal here has no statistical standing.
5. **Liquidity: not a constraint** (~1.5M ADTV, $14.9B cap) — but the market cap is down ~70% from peak, which shrinks institutional/index eligibility and raises crowding-out risk among value managers screening the same 7.9% FCF yield.
