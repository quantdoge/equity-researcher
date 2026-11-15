# Quant Analyst

- Symbol: U
- Elapsed: 38.9s

---
# Quantitative Factor Report — Unity Software Inc. (U)

**Price basis: $18.25 (close 2026-02-20). Diluted shares 420.9M → mkt cap $7.68B; net debt $0.33B → EV $8.01B.**

⚠️ **Data-integrity flag up front:** the profile/valuation endpoints report a price of **$52.81**. That is stale. The price history shows U closing at **$18.25** on 2026-02-20 — a **−65%** move from the December 2025 peak. All multiples below are recomputed on the live price; I ignore the tool-supplied P/E of −55.0, P/B of 6.37, P/FCF of 55.0 and EV/EBITDA of 251x, which are inflated ~2.9x by the stale price.

---

## 1. Factor Scores

| Factor | Score | Sector Rank (of 7) | Signal |
|---|---|---|---|
| **Value** | P/FCF 19.0x · FCF yield 5.3% · EV/EBITDA **89.3x** · EV/Sales 4.3x · P/B 2.20x · P/E **n.m.** (EPS −$0.96) | **5 / 7** | **Negative** — cheapest thing about it is book value; earnings-based multiples unusable |
| **Momentum (12‑1)** | **−1.0%** (tool, as-of pre-crash). Realized spot: 1M **−56.1%**, 3M **−51.6%**, 6M **−49.1%**, 12M **−15.0%**, YTD **−58.7%** | **4 / 7** on 12‑1; **7 / 7** on current trend | **Strongly negative** |
| **Quality** | ROE −11.5% · ROIC −8.2% · GP/Assets 0.201 · Accruals −0.121 · F‑Score **7** | **6 / 7** | **Negative**, but improving |
| **Low Vol** | Vol 68.3% (252d) / 69.6% (504d) · Beta 1.02 (252d) / **1.70 (504d)** · Max DD 41.0% / **65.4%** | **7 / 7** | **Negative** — highest beta in the comp set |
| **Earnings Revision** | +108.7% (2030 EPS $0.23→$0.48) | n/a | **Nominal positive — not credible** (see §4) |

**Peer panel (Application/Infrastructure Software):**

| | U | CRM | ADBE | NOW | SHOP | PATH | SNOW |
|---|---|---|---|---|---|---|---|
| P/FCF | 19.0 | 14.5 | **10.5** | 23.4 | 95.6 | 20.5 | 87.7 |
| EV/EBITDA | 89.3 | 16.4 | **10.6** | 34.4 | 96.6 | 49.7 | n.m. |
| ROE % | −11.5 | 12.6 | **61.3** | 13.5 | 9.1 | 13.6 | −69.2 |
| GP/Assets | 0.201 | 0.287 | **0.719** | 0.395 | — | — | — |
| 12‑1 Mom % | −1.0 | **+29.1** | −5.8 | +21.0 | +15.0 | −8.2 | −3.5 |
| Vol % | **68.3** | 49.8 | 43.7 | 68.8 | — | — | — |

*Note: the tool's "Technology" sector list returns AAPL/NVDA/MSFT/TSM — mega-cap semis, not software comparables. I built the panel manually.*

---

## 2. Price Statistics

| Metric | 252d | 504d |
|---|---|---|
| Annualised vol | 68.3% | 69.6–70.0% |
| Beta vs SPY | 1.02 | **1.70** (profile: 2.11) |
| Alpha (annualised) | — | **+41.0%** |
| R² | — | **0.097** |
| Sharpe | 1.77 (approx) | **1.116** |
| Sortino | — | **1.509** |
| Max drawdown | 41.0% | **65.4%** |

**These risk-adjusted stats are retrospective and now misleading.** The 41% alpha and 1.12 Sharpe are artefacts of the Jun–Dec 2025 rally that has since been fully retraced. On an as-traded basis at $18.25, trailing 12-month return is **−15.0%** against 68.3% vol → **Sharpe ≈ −0.22**. Current drawdown from the 2025-12-11 close ($49.23) is **−62.9%**; from the intraday high ($52.15), **−65.0%**.

**Alpha is statistically hollow:** R² of 0.097 means ~90% of U's variance is idiosyncratic. The beta is not stable (1.02 → 1.70 → 2.11 depending on window), so factor attribution for U should be treated as indicative only. (Peer betas from the same endpoint — ADBE 0.078, CRM 0.218 — are implausible for those names, so I discount the beta estimates generally.)

---

## 3. Composite Quant Signal: **SELL**

Momentum, quality, value and low-vol all rank in the bottom tercile of the peer group. The one offsetting factor is genuine fundamental improvement:

- **FCF inflection:** −$117M (FY22) → $179M (FY23) → $273M (FY24) → **$404M (FY25)**
- **Gross margin:** 66.5% (FY23) → **74.2% (FY25)**, +7.7pp
- **ROIC:** −13.7% (FY22) → **−8.15% (FY25)**, +5.5pp; net loss narrowed $919M → $403M
- **Accruals −0.121** = cash earnings exceed accounting earnings (high earnings quality)
- **F-Score 7/9**, 5 of 9 components improving

But the trend is broken and the valuation did not reset enough: at 4.3x EV/Sales and 89x EV/EBITDA the stock is still priced for a recovery that two consecutive earnings disappointments (−24.2% on 2026-01-30, then −26.3% on 2026-02-11 on **105M shares**, 25% of the float) suggest is not arriving. Revenue grew **+2.0%** in FY25 after **−17.1%** in FY24.

---

## 4. Key Quant Risk Flags

1. **Momentum reversal / trend break (highest severity).** Two >24% gap-downs in three weeks on 6–27x normal volume. Post-earnings-announcement drift following a guidance miss is typically negative for 30–60 days. U is last in the panel on 1M/3M/6M returns.
2. **SBC-distorted FCF — the core quality problem.** FY25 SBC of **$385.2M = 95.4% of the $403.9M FCF**. FCF ex-SBC is **≈$19M** → **EV/FCF ex-SBC ≈ 428x**. The headline 5.3% FCF yield is largely a non-cash accounting artefact. This is why Quality ranks 6/7 despite the accruals score looking pristine.
3. **Dilution.** Shares 395.9M → 420.9M (**+6.3% YoY**); Piotroski F7 = 0. Growth is being purchased with equity.
4. **Earnings-revision signal is not investable.** The +108.7% "upgrade" compares a **2030** estimate ($0.48) to its value 3 months ago ($0.23), on **11 analysts**, five years out. The estimate curve is internally inconsistent: FY28 EPS **$2.82** → FY29 **$0.23** → FY30 **$0.48**, and FY26 revenue consensus of $2.365B (**+28%**) contradicts FY25 actual growth of +2.0%. Treat this estimate set as unreliable; I assign it **zero weight** in the composite, and note the post-earnings −26% reaction points to *downward* near-term revision pressure.
5. **Factor-model risk / crowding.** R² 0.097 → the stock is an idiosyncratic binary, not a factor exposure. Beta instability (1.02 to 2.11) means any beta-hedged or factor-neutral construction will mis-size the position. Momentum-reversal crowded longs from the 2025 rally were likely the marginal seller in the January/February gaps.
6. **Value trap risk isn't the issue — valuation risk is.** Even after −65%, EV/EBITDA of 89x and EV/Sales of 4.3x leave no margin of safety for a company with 2% revenue growth.
7. **Liquidity: not a concern.** ~$220–250M average daily dollar volume; the Feb 11 event traded $2.2B. No capacity constraint.
8. **Sample-size caveat.** IPO 2020-09-18 → only ~5.4 years of public history, and the 504d regression is fit across a single regime (post-2024 recovery). Alpha/beta/Sharpe have no out-of-sample validation.

**Bottom line:** the numbers say the turnaround is real but slow, while the price says the market has stopped paying for it. Negative on all four classic factors, worst-in-class momentum and beta, with the only support coming from improving cash generation that is almost entirely stock compensation. **Sell**, with a fundamental-trigger re-entry watch on FY26 revenue growth re-accelerating above 10% and FCF ex-SBC turning decisively positive.
