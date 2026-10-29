# Quant Analyst

- Symbol: FFIV
- Elapsed: 45.5s

---
## FFIV (F5, Inc.) — Quantitative Factor Report

**Data caveat up front:** the `calculate_valuation_ratios` / profile feed returned a price of **$365.53**, while the OHLC tape ends at **$456.58** (2026‑10‑15) and PT notes reference $459.36. The multiples feed is **~25% stale**. I present multiples restated to the live price and flag original tool output. Also, §4 shows the earnings‑revision factor is methodologically broken for this name.

---

### 1. Factor Scores Table

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | Trailing GAAP P/E **36.5x**; fwd non‑GAAP **25.0x**; EV/EBITDA **25.7x**; P/FCF **30.3x**; P/B 6.6x | **4th of 7** peers (~43rd pct) | **Negative** — pays a growth multiple |
| **Momentum** | **+47%** 12‑1 (computed from OHLC); tool reports +8.92% | 1st of 7 on OHLC / 4th of 7 on tool | **Positive** (measurement conflict — see §4) |
| **Quality** | ROE 18.0%, **GP/A 0.398 (best in peer set)**, accruals **−3.4%**, ROIC 19.4% rising 4 yrs straight (14.2→18.3→18.8→19.4) | 2nd of 4 (~50th pct) | **Positive** — cash earnings exceed reported |
| **Low Vol** | Vol **42.7%** ann.; beta **1.056**; max DD 23.8% (252d) | 2nd of 4 on vol, 2nd of 4 on beta | **Negative** — market beta, high absolute vol |
| **Earnings Revision** | Tool: +6.79% "upgrade" — **invalid** (period mismatch). Corroborated by 5 of 6 recent PT raises | n/a | **Positive, low confidence** |

**Supporting fundamentals:** Piotroski **F‑Score 6/9** (moderate; fails ROA improvement, leverage reduction, asset turnover). Estimates: FY26E EPS $17.33 → FY27E $18.27 → FY28E $20.19 → FY29E $21.56; revenue $3.38B → $4.19B (~7.3% CAGR). Modest growth, not a high‑growth profile.

**Peer set used** (application delivery / network security — *not* the returned NVDA/AAPL/MSFT list, which is not comparable to a $21B software name): CHKP, AKAM, CSCO, FTNT, ANET, NET.

| Peer | P/E | EV/EBITDA | P/FCF | 12‑1 Mom | Vol | Beta |
|---|---|---|---|---|---|---|
| FFIV | 36.5 | 25.7 | 30.3 | +47.0% | 42.7% | 1.06 |
| CHKP | 16.1 | 15.4 | 14.6 | −1.6% | 43.8% | −0.21 |
| AKAM | 32.0 | 15.0 | 20.6 | −14.9% | 66.7% | 1.53 |
| CSCO | 33.1 | 22.7 | 34.4 | −4.1% | 38.4% | 1.22 |
| FTNT | 71.6 | 51.8 | 58.5 | +13.1% | n/a | n/a |
| ANET | 67.9 | 52.6 | 56.0 | +16.6% | n/a | n/a |
| NET | n.m. | 1045.8 | 342.4 | +27.5% | n/a | n/a |

---

### 2. Price Statistics (252 trading days, vs SPY)

| Metric | Value |
|---|---|
| Annualised return | **47.34%** |
| Annualised volatility | **42.11%** (vol tool: 42.68%) |
| Beta vs SPY | **1.062** (vol tool: 1.056) |
| **Alpha (annualised)** | **+33.77%** |
| **R²** | **0.104** |
| Sharpe | **1.124** (vol tool: 1.258) |
| Sortino | **1.217** |
| Sortino / Sharpe | **1.08** |
| Max drawdown (252d) | **−23.8%** |
| Drawdown, Oct‑25 peak → Nov‑25 trough | **−34.7%** (close 343.17 → 223.99) |

**Alpha is not statistically significant.** With R² = 0.104, residual vol ≈ 39.9% ann. (2.51% daily). Daily alpha 0.134% ÷ SE 0.158% gives **t ≈ 0.85**. The headline +33.8% alpha is noise from 2–3 large idiosyncratic earnings moves, not a repeatable edge — only 10% of FFIV's variance is explained by the market.

**Sortino/Sharpe = 1.08 is a warning, not a comfort.** Downside volatility is almost identical to total volatility — returns are near‑symmetric with no fat right tail. The Sharpe of 1.12 is therefore *not* being flattered by a favourable skew; it rests entirely on one large up-move.

---

### 3. Composite Quant Signal: **BUY (moderate conviction)**

Quality (GP/A top of peer set, negative accruals, ROIC up 4 straight years) + genuine upward estimate/PT revisions + strong absolute momentum outweigh a rich multiple and market‑level beta. It is **not** a Strong Buy: there is no value cushion, and the stock trades at/above consensus fair value.

**Consensus target check:** recent PTs $500 / $475 / $461 / $450 / $397 / $300 (BofA Underperform) → **median $455.5, mean $430.5 vs price $456.58**. Price is already **at the median target** (−0.2% implied upside). The quant upside is largely realised.

---

### 4. Key Quant Risk Flags

1. **Earnings‑revision factor is invalid as returned.** The tool compared FY2029E ($21.56) against FY2028E ($20.19) and labelled the 6.79% differential a "revision." That is simply the FY29/FY28 growth rate, not a time‑series estimate change. **A true revision signal cannot be computed from the available snapshots.** My positive read is triangulated only from PT direction (Wells Fargo $500, Evercore upgrade + $475, Piper $461, RBC $450, Barclays $386→$397 — vs one BofA $300). Note the FY2029 estimate rests on **2 analysts**; treat as low confidence.
2. **Momentum measurement conflict — the single largest uncertainty.** The momentum tool returns +8.92% 12‑1; my computation from the raw OHLC tape gives **+47.2%** (295.35 → 434.62). The two do not reconcile and the tool's anchor appears to use the stale price series. If 8.92% is correct, the composite drops to **Neutral**; if +47% is correct, momentum is the top of the peer group. I weight the observable OHLC higher but flag the ambiguity.
3. **Momentum reversal / crowding risk is elevated.** FFIV is +104% off its Nov‑2025 low ($224 → $480) and has already rolled over **−4.8% from the Oct‑9 closing high** ($479.83 → $456.58). A +47% 12‑1 return entering a decelerating revenue growth profile (~7% CAGR) is the classic setup for momentum unwinds.
4. **Valuation offers no support.** Restated EV/EBITDA 25.7x sits above AKAM (15.0x), CHKP (15.4x) and CSCO (22.7x). A −34.7% drawdown occurred just 11 months ago on a single earnings print — the multiple compresses violently.
5. **Beta is 1.06, not defensive.** Despite the "infrastructure software" label, FFIV offers no low‑vol diversification benefit; 42.7% annualised vol is high for a $21B large cap.
6. **Low‑vol factor is contaminated in this peer set.** CHKP's beta of −0.21 and 43.8% vol are internally inconsistent (negative beta with 44% vol), and NET/FTNT/ANET vol data was unavailable. Cross‑sectional low‑vol ranks are therefore unreliable.
7. **F‑Score 6/9 with three failing components** (asset turnover, leverage, ROA trend) is consistent with a mature business buying growth rather than compounding it organically.
8. **Sample limitations:** 252 daily observations is adequate for beta/vol but thin for alpha with R² = 0.10. Peer group is 4–7 names, so percentile ranks are coarse and should not be read as sector‑wide.

**Data gaps:** peer betas/vols for FTNT, ANET, NET; peer correlation matrix not computed; true estimate‑revision time series unavailable.
