# Quant Analyst

- Symbol: CRWD
- Elapsed: 70.6s

---
# CRWD — Quantitative Factor Report
**CrowdStrike Holdings, Inc.** · Technology / Software – Infrastructure · Market cap $214.0B · Price $208.97 (23-Nov-2026)

---

## 1. Factor Scores Table

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | **1 / 10** | **4 / 4** (0th pctile) | **Strong Sell** |
| **Momentum** | **5 / 10** | **2 / 4** (67th pctile) | **Neutral — decaying** |
| **Quality** | **5 / 10** | **3 / 4** (33rd pctile) | **Neutral (mixed)** |
| **Low Vol** | **3 / 10** | **3 / 4** (33rd pctile) | **Sell** |
| **Earnings Revision** | **7 / 10** | **1 / 4** (top) | **Buy (low confidence)** |

*Peer set = PANW, FTNT, ZS (true cybersecurity comps; the sector screen returns megacaps AAPL/NVDA/MSFT which are unusable comparables). n=4 — ranks are ordinal and not statistically robust.*

**Value — bottom of peer group, decisively.** EV/Sales (TTM rev $5,745M) = **35.7x**; EV/EBITDA 1,123.6x; P/FCF 159.9x (**FCF yield 0.63%**); P/B 46.85x. P/E is not usable (−1,306x on GAAP). Even on *consensus adjusted* EPS, forward P/E is 166.6x (FY27 $1.254) → 130.2x (FY28) → 71.2x (FY31). P/FCF vs FTNT 45.0 / ZS 43.1 / PANW 65.7 — CRWD is ~2.5–3.7x the peer multiple.

**Quality — genuinely split.** Cash-based quality is excellent: accruals ratio **−0.1601** (best in peer set; negative accruals = conservative earnings), gross profit/assets 0.3241 (vs PANW 0.167, ZS 0.327, FTNT 0.527), gross margin 75.9%, TTM OCF margin 28.1%. But GAAP profitability is negative: ROE −3.63%, ROA −1.47%, ROIC **−5.54%** (worse than FY25's −2.93%), and **Piotroski F-Score 4/9 (Weak)** — fails on negative ROA, negative ROA improvement, share dilution (1,002M → 1,025M shares), and no gross-margin/asset-turnover improvement. Rule of 40 ≈ **56** (28.3% growth + 28.1% OCF margin) — strong.

**Earnings Revision — most bullish factor, weakest evidence.** Tool output: FY2031 EPS consensus $2.935 vs $2.44 = **+20.29%**, signal "upgrade." **Caveat: only 5 analysts cover FY2031 and it is a 5-year-forward estimate — not a tradeable revision signal.** Better corroboration: consensus EPS path FY27→FY31 implies a **23.7% CAGR**, and sell-side targets were raised repeatedly into Dec-2026 (BofA $260→$290, Citi $260→$295, KeyBanc $245→$265, Mizuho $250→$275, Barclays →$265, Deutsche Bank **upgraded to Buy** $300). Mean PT **$266.70 (+27.6%)**, median **$270 (+29.2%)**; one outlier (Bernstein $177). Revenue +28.3% YoY in the Oct-Q, with *accelerating* sequential growth (+6.2% → +7.7%).

---

## 2. Price Statistics

| Metric | Value | Note |
|---|---|---|
| Beta vs SPY | **1.058–1.064** | Company profile 1.15 |
| Alpha (annualised) | **+100.6%** | **t ≈ 1.7 — not significant** |
| R² vs SPY | **0.0728** | Only 7.3% of variance is market — CRWD is idiosyncratic |
| Annualised vol | **63.2%** | vs PANW 56.8%, FTNT 54.0%, ZS 76.6% |
| Sharpe | **2.103** | ⚠️ see conflict below |
| Sortino | **3.806** | ⚠️ same caveat |
| Max drawdown | **−25.06%** | Confirmed: $278.86 (6-Oct) → $208.97 |

**⚠️ Data conflict — flagging rather than hiding.** `calculate_sharpe_sortino` reports an annualised return of **+130.7%** and Sharpe 2.10. `calculate_momentum_score` reports **+20.69%** on the same 252-day lookback. These are mathematically irreconcilable: momentum's terminal price (~$257.57 on 23-Oct) divided by a +130% 12-month return implies a ~$91 base, which would make 12-1 momentum ≈ +184%, not +21%. Direct OHLCV confirms the lower figure: CRWD traded ~$194–202 on 3-Aug-2026 and $208.97 now. **I therefore reject the 130.7% return / 2.10 Sharpe as overstated and treat the true 12-month Sharpe as approximately 0.0–0.3.**

**Directly verified price behaviour (my own return calculation):**
- Last **21 trading days: −18.9%** ($257.57 → $208.97)
- Off 6-Oct peak: **−25.1%**
- Since 3-Aug: **+3.2%**
- **23-Nov: −8.9% on 42.1M shares (~4.7x the 20-day average of ~9M)** — a post-earnings (filed 23-Nov) distribution day

**Correlation matrix (252d):** PANW **0.846**, FTNT 0.686, ZS 0.629, MSFT 0.359, **SPY 0.268**. Reassuringly low market correlation, but 0.85 with PANW means CRWD trades as a cybersecurity beta proxy, not a diversifier.

---

## 3. Composite Quant Signal: **NEUTRAL** (near-term bias: cautious)

The two live forces point opposite ways: **estimate revisions and target prices are rising while price is breaking down.** Growth is accelerating (28.3% YoY, 7.7% sequential), accruals are best-in-class, and the sell-side is upgrading — but the stock is 25% off its high, momentum has reversed hard in the last month, and the multiple (35.7x EV/Sales, 160x P/FCF) leaves no valuation cushion if the momentum unwind continues. Positive revisions into a −25% drawdown is historically an ambiguous setup: sometimes an opportunity, often a de-rating that precedes further estimate cuts. **Not enough signal to be long, and the fundamental momentum is too strong to be outright short → Neutral.**

---

## 4. Key Quant Risk Flags

1. **Momentum reversal — confirmed, not merely at risk.** The 12-1 factor (+20.69%) is structurally blind here: by excluding the last 21 trading days it stops measuring at 23-Oct (~$257), and so completely misses the −18.9% collapse that followed. The true momentum state is deteriorating. Distribution on 4.7x volume is a bearish tell.
2. **Alpha is not statistically distinguishable from zero.** R² = 7.3% means the +100.6% "alpha" has a standard error of roughly 60pp (t ≈ 1.7). Any story built on CRWD's market-beating alpha rests on a single 12-month sample and is fragile.
3. **Factor crowding.** 0.846 correlation with PANW and 0.63 with ZS = crowded cybersecurity-long exposure. A sector de-rating hits all three simultaneously; there is no diversification inside the trade.
4. **Valuation compression risk — no floor.** 160x P/FCF and 1,124x EV/EBITDA mean the multiple, not earnings, drives returns. At 62% vol, a 1-sigma year is ±62%.
5. **GAAP vs. adjusted EPS disconnect.** TTM GAAP diluted EPS is **$0.09** (net income $117M on $5,745M revenue, 2.0% margin) against FY27 consensus of $1.254. Valuation ratios derived from the consensus series are approximately 14x more flattering than GAAP reality. Do not compare CRWD's forward P/E to GAAP-based peers without adjustment.
6. **Small-sample caveats.** Earnings-revision signal rests on 5 analysts for an FY2031 period; peer ranking rests on 4 names. Neither supports a high-confidence conclusion.
7. **Liquidity: not a concern** (42M shares traded on a single day; $214B cap) — this is crowding and multiple risk, not liquidity risk.

**Bottom line for the memo:** quality-of-earnings and estimate-revision momentum are real and improving; everything price- and valuation-related is working against the name. Score it **Neutral**, and treat the −25% drawdown plus the 23-Nov volume spike as the single most important datapoint to monitor — a stabilization there would upgrade the signal; another leg down would confirm momentum-driven de-rating regardless of the target-price cluster.
