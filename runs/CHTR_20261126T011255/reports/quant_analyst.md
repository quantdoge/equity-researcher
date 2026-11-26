# Quant Analyst

- Symbol: CHTR
- Elapsed: 57.2s

---
## CHTR — Quantitative Factor Report
**Charter Communications, Inc. | Communication Services / Telecommunications Services | Price $147.27**

---

### 1. Factor Scores Table

| Factor | Raw Score | Sector Rank (of 5) | Signal |
|---|---|---|---|
| **Value** | P/E 4.07 · EV/EBITDA 5.51 · P/FCF 4.59 · P/B 0.99 | **1** (best) | **Strong Buy** |
| **Momentum** | −28.96% (12-1m) | **5** (worst) | **Strong Sell** |
| **Quality** | ROE 24.3% · GP/Assets 0.165 · Accruals −7.19% · ROIC 11.3% · F-score 7/9 | **2** | **Neutral / Buy** |
| **Low Vol** | Ann. vol 59.9% · Beta ≈ 0 · MDD −58.2% | **5** (worst) | **Strong Sell** |
| **Earnings Revision** | Tool: +27.6% "upgrade" — **invalid, see flag** · Real PT revisions −20% to −40% | **5** | **Strong Sell** |

**Peer set used for ranks** (Communication Services, closest comparables): VZ, TMUS, T, DIS. Note: GOOGL/META/NFLX share the GICS sector but are not multiple-comparable — I excluded them.

**Value detail — clean sweep, #1 on every metric:**

| Metric | CHTR | T | VZ | TMUS | DIS |
|---|---|---|---|---|---|
| P/E | **4.07** | 7.56 | 11.65 | 17.10 | 22.31 |
| EV/EBITDA | **5.51** | 5.86 | 7.60 | 9.73 | 12.04 |
| P/FCF | **4.59** | 8.48 | 10.17 | 12.19 | 20.90 |

**Quality is better than the tool's "low" label suggests.** ROE 24.3% ranks #1 in the peer set, accruals of −7.19% rank #2 (strongly negative accruals = high earnings quality, cash conversion is excellent: NI $4.99B vs OCF $16.08B). F-score 7/9 with only ROA-improvement and asset-turnover failing. The tool flags "low" purely on gross-profit/assets (0.165, rank #4 of 5) — a structural artifact of capital-intensive cable, not a deterioration. **Caveat: the 24.3% ROE is manufactured by leverage** — ROA is only 3.23% and ROIC 11.34%, down from 11.47% in 2024 and only 11.08% in 2022–23. Three years of essentially flat 11% ROIC on a shrinking equity base.

---

### 2. Price Statistics

| Metric | 252-day | 504-day |
|---|---|---|
| Alpha (ann., vs SPY) | **−42.03%** | **−57.44%** |
| Beta (vs SPY) | −0.052 | 0.139 |
| R² | **0.0002** | **0.0014** |
| Ann. volatility | 60.78% | 51.81% |
| Ann. return (arithmetic) | −43.14% | −53.08% |
| Ann. return (geometric, from price path) | ≈ −25% | ≈ −37% |
| **Sharpe** | **−0.71** | **−1.02** |
| **Sortino** | **−0.89** | **−1.23** |
| Max drawdown | −58.24% | −75.57% |

Observed price path: $366.49 (Nov-2024) → peak $427.25 (May-2025) → $147.27 (25-Nov-2026). Cumulative **−59.8%** from the Nov-2024 mark, **−65.5%** from the May-2025 peak, **−26.6%** over the trailing year. The arithmetic-vs-geometric gap (e.g. −53% vs −37% ann.) is exactly explained by variance drag (~σ²/2), so the series is internally coherent — but **quote the geometric numbers to clients**, arithmetic annualization materially overstates the loss.

Largest single-day dislocations: −18.5% (25-Jul-2025, on 9.6M shares), −25.5% (24-Apr-2026, on 13.3M shares), the 18-Jun-2026 gap on 17.9M shares. Three earnings-driven gaps account for the bulk of realised variance.

---

### 3. Composite Quant Signal

# SELL

**Mechanism:** this is a textbook **value-trap signature** — rank #1 on value, rank #5 on momentum, #5 on low-vol, #5 on revisions. In a cross-sectional factor model, deep value only earns its premium when paired with either positive momentum or positive revisions (both confirming a trough) or with quality/balance-sheet durability (allowing you to wait). CHTR has one of four: value. Zero catalysts confirm the bottom, and the risk profile is the worst in its peer group.

I stop short of Strong Sell for two honest reasons: (1) accruals and F-score confirm the earnings are *real cash*, not accounting, and (2) at 0.99× book and 4.6× FCF, the multiple already discounts severe terminal-value erosion. But neither justifies ownership ahead of a momentum or revision inflection.

---

### 4. Key Quant Risk Flags

1. **⚠️ Earnings-revision reading is a data artifact — do not use it.** The tool reports "+27.55% upgrade" by comparing the **FY2030** EPS estimate ($77.09) against the **FY2029** estimate ($60.44). Those are *different forward periods*, not the same period over time — the "+27.6%" is simply the growth between two years, not a revision. Compounding the error, FY2030 carries only **2 analysts** (n=2, statistically meaningless) and FY2028 has a $29–$86 EPS range across 6 analysts — enormous dispersion. **The genuine revision signal is sharply negative:** in the Jul-2026 cluster, UBS cut $235→$140, Deutsche Bank $215→$150, Wells Fargo $160→$101, Bernstein $150→$120, RBC $160→$150. Median of the 10 most recent targets is **≈$145 vs. spot $147.27 → ~0% implied upside.** Wolfe downgraded to Underperform.

2. **⚠️ Beta and R² are unusable from this feed.** Regression beta of 0.139 (R² = 0.0014) and −0.052 (R² = 0.0002) imply SPY explains 0.02–0.14% of CHTR's variance — implausible for a large-cap telecom. The tell: **every peer also regresses negative on SPY** (VZ −0.29, TMUS −0.27, T −0.31), and SPY's correlation to each is negative. The benchmark series is misaligned. **Use the 5-year monthly beta of 0.731 from the company profile instead.** Practical consequence: with a true beta of ~0.73 but this much idiosyncratic variance, CHTR is a poor hedge and a poor source of market beta — its risk is ~100% company-specific.

3. **Factor crowding: low, but for the wrong reason.** CHTR's correlation to sector peers is modest (VZ 0.36, T 0.35, DIS 0.34, TMUS 0.27) — it is *not* crowded. It has de-coupled from its sector, having fallen while peers fell 10–19%. This is idiosyncratic decay, not a rotation.

4. **Leverage is the real risk, not the multiple.** EV $116.9B vs. market cap $20.3B implies **~$96.6B net debt** on ~$21.2B EBITDA → **~4.6× net debt/EBITDA** and ~4.7× debt/equity. The balance sheet, not the P/E, determines terminal value. Every 100bp of refinancing cost on that stack is ~$1.0B of annual FCF. This is why ROE (24.3%) and ROA (3.2%) diverge by 8×.

5. **Drawdown/momentum-reversal risk cuts both ways.** At −65.5% from peak and below book, a short position carries genuine squeeze risk — three of the last twelve months printed +20% or more off lows. Quantitatively: momentum is confirmed negative, but the stock is now **short-term mean-reverting**, so any short must be sized for 20–30% counter-trend rallies.

6. **Liquidity is adequate.** ~$440M average daily dollar volume (3.0M shares × $147). Not a constraint. However, the ~90% market-cap de-rating raises index-deletion and forced-seller risk that is not captured in any factor score.

**Bottom line:** 1 of 5 factors favourable, and the one that is favourable is the one most prone to value traps. Negative alpha of −42% to −57% annualised, Sharpe −1.0, worst-in-class volatility, negative real revision momentum. **Sell** — the numbers will not support the story until either revisions turn or momentum bases.
