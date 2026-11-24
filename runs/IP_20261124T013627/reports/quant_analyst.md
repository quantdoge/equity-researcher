# Quant Analyst

- Symbol: IP
- Elapsed: 74.4s

---
## IP — International Paper | Quantitative Factor Analysis
**Price $28.98** · Mkt cap $15.35B · EV ≈ $24.96B · Basic Materials / Paper & Packaging · FY end 2025-12-31

**Data-integrity note up front:** IP's FY2025 reporting period contains a −$3.52B net loss (EBITDA −$97M) against operating cash flow of **+$1.70B** and D&A of $2.88B — i.e. the loss is non-cash (impairment/restructuring tied to the DS Smith integration, which also doubled share count 347M → 528M). Trailing multiples (P/E −4.3x, EV/EBITDA −257x, P/FCF −96x) are therefore **not meaningful** and I do not use them for ranking.

### 1. Factor Scores
Scored 0–10 vs. a 3–4 name paper/packaging cross-section (IP, PKG, AMCR, SUZ); 5 = peer median.

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | **7.0** | **1 of 3** (usable) | Bullish — forward only |
| **Momentum** | **1.0** | **4 of 4** | Strongly bearish |
| **Quality** | **3.0** | **3 of 3** | Bearish |
| **Low Vol** | **1.0** | **4 of 4** | Strongly bearish |
| **Earnings Revision** | **2.0** | 3 of 4 | Bearish (tool reading rejected) |

**Value — 7.0 (rank 1).** On trailing metrics IP screens worst; on forward it screens cheapest.
| | IP | PKG | AMCR |
|---|---|---|---|
| EV/2026E EBITDA | **6.8x** | 14.25x | 10.12x |
| EV/2027E EBITDA | **5.5x** | — | — |
| Fwd P/E 2026E / 2027E | 29.2x / **11.3x** | 27.7x | 18.3x |
| P/B | **1.03x** | — | — |
| Div yield | **6.38%** | — | — |

A 35–50% EV/EBITDA discount to peers is the single genuine bull argument. But it is a discount on estimates that are *being cut* (see revisions), and it sits alongside 2.6x net-debt/EBITDA. **SUZ excluded from ranking** — reported P/E 0.87x / EV/EBITDA 2.45x on an $9.25 ADR is a currency/ADR artifact, not a real multiple.

**Momentum — 1.0 (rank 4/4).** 12-1 momentum **−18.0%**; peers PKG −0.04%, AMCR +1.8%, SUZ +8.8%. Returns to 2026-11-23: 1M **−11.5%**, 3M **−29.2%**, 6M −5.0%, 12M **−19.2%**, since 2025-01-02 **−40.4%**. The stock is **at its 52-week low**.

**Quality — 3.0 (rank 3/3).** ROIC has collapsed: 2022 +12.2% → 2023 +8.3% → 2024 +3.4% → **2025 −11.0%**. ROE −23.7% vs PKG +16.7%, AMCR +9.4%. Piotroski **F-score 5/9** (fails positive ROA, ROA improvement, asset-turnover improvement, and **F7 no-dilution** — 52% share issuance). *The one real positive:* gross profit/assets **19.4%**, highest in the group (PKG 17.6%, AMCR 12.6%) — the underlying mill asset base is not structurally broken.

**Low Vol — 1.0 (rank 4/4).** Annualised vol **44.1%** vs PKG 28.6%, SUZ 28.1%, AMCR 32.6%. Beta *looks* benign at 0.88 but that is deceptive: correlation to SPY is only **0.32**, so IP is ~2.5x the market's volatility with almost none of it explained by the market.

**Earnings Revision — 2.0 (tool rejected, real signal bearish).**
⚠️ The tool reports **+30.35% "upgrade"** — this is a **roll-forward artifact, not a revision**. The comparison is 2029E $3.86 vs "prior" $2.96, and $2.96 is *exactly* today's 2028E consensus. The 2029E also rests on **1 analyst**. Sample size is far too small and the periods are mismatched; I discard it.
The *actual* revision tape is negative and recent: **UBS $47 → $35** and **Truist $49 → $39** (Oct 2026), after the July 2026 round of raises. Median recent PT ≈ **$39.50** (+36% vs spot), but the *direction* has flipped hard down.

### 2. Price Statistics (252d, vs SPY)
| Metric | Value |
|---|---|
| Alpha (annualised) | **−60.7%** |
| Alpha t-stat | **≈1.5 — NOT significant** (R²=0.104) |
| Beta | **0.887** (t≈15, highly significant) |
| R² vs SPY | **0.104** |
| Annualised vol | **44.1%** |
| Sharpe | **−0.90** (Sharpe/Sortino tool) / **−1.19** (vol tool) ⚠️ |
| Sortino | **−1.41** |
| Max drawdown | **−39.5%** (52w); **−47.4%** from Jan-2025 peak $55.00 |

⚠️ **Tool inconsistency:** the volatility and Sharpe/Sortino tools disagree for the same window (vol 44.06% vs 44.32%; Sharpe −1.19 vs −0.90), and the −39.84% annualised return implies a start price of ~$48.17 (Jan-2025) rather than 2025-11 (~$35.85). Magnitudes should be treated as approximate; **direction is unambiguous and corroborated** by the raw OHLCV series I recomputed independently.

**The key statistical caveat: R² = 0.10.** Only 10% of IP's variance is market-driven. With ~252 observations, the standard error on annualised alpha is roughly ±42pp, so **the −60.7% alpha is not statistically distinguishable from zero** even though it is directionally damning. Do not present the alpha as a precise estimate.

### 3. Composite Quant Signal: **SELL**
Equal-weighted: (7.0 + 1.0 + 3.0 + 1.0 + 2.0) / 5 = **2.8 / 10**.

One factor of five is positive, and it is the factor most vulnerable to being a value trap — cheap *because* estimates are falling, quality is deteriorating, and the stock is making new lows. Multi-factor ranking does not pay for single-factor extremes. I stop short of Strong Sell only because P/B 1.03, a 6.4% yield, 36% implied PT upside and 19.4% gross-profit/assets preserve a credible contrarian/deep-value case for a **value-tilted mandate with a 24-month horizon**. For a momentum- or quality-tilted mandate this is a clear avoid.

### 4. Key Quant Risk Flags
1. **Downside momentum continuation + violent reversal risk.** At 52-week lows with worst-in-class 12-1 momentum, but realized jump risk is extreme: **+11% on 2026-07-24**, **+14% same-week**, **−16% on 2025-10-30**, **−12% on 2026-04-30**. Position sizing must respect ~44% vol.
2. **Earnings-quality distortion (most important).** The −13.7% accruals ratio and "low accruals" pass are mechanically manufactured by the −$3.52B non-cash charge against +$1.70B operating cash flow. **This is not evidence of accounting quality improvement** and must not be read as such.
3. **Revision metric is spurious.** The +30.35% "upgrade" is a period-roll artifact on a 1-analyst estimate. Anyone quoting it as a bullish signal is reading a bug as a feature.
4. **Dividend coverage.** $1.85/share ≈ $977M vs 2026E EPS $0.99 → **187% EPS payout**; trailing FCF is **negative**. Covered only on forward EBITDA/FCF (~1.7x). A recovery slip puts the 6.4% yield at risk — and the yield is likely part of why the stock is held.
5. **Leverage.** Net debt ≈ $9.66B, **2.6x 2026E EBITDA**, interest $372M. Refinancing cost is a live risk.
6. **Factor crowding: low.** This is a contrarian, out-of-favour name — crowding is a non-issue; the risk is the opposite (persistent de-rating).
7. **Liquidity: not a constraint.** ~12.4M shares/day, $15.3B cap.
8. **Small-sample caveat on ranks.** Ranked against only 3 peers within a "Basic Materials" sector that otherwise contains gold miners and specialty chemicals. Treat sector-rank figures as **indicative, not statistically robust** — a 3-name cross-section cannot produce meaningful quintiles.

**Bottom line:** value is real but early, everything that measures *direction* — momentum, revisions, ROIC trajectory — is negative, and the one "improving" quality metric is an accounting artifact. Numbers win: **Sell**, revisit if 2027E EPS stabilises and revisions turn.
