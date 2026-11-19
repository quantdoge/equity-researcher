# Quant Analyst

- Symbol: CBRS
- Elapsed: 23.3s

---
## CBRS — Cerebras Systems Inc. | Quantitative Factor Report

### ⚠️ Data Integrity Flags (read before the tables)

Three material defects in the raw feed, quantified:

1. **Unreliable risk statistics — 32 trading days of history.** IPO date **2026-05-14**; price history begins that day. Every "252-day" metric below is therefore computed on **n=32 trading days**, then annualized. Required n for significance at these vol levels is ~250. **All vol/beta/alpha/Sharpe/Sortino/max-DD figures are statistically void** — treat as descriptive of one post-IPO episode, not as risk estimates.
2. **Price discrepancy.** Profile quote **$94.15** vs. last close **$221.00** (2026-06-30), a **2.35x** gap. The valuation multiples were computed at $94.15 — confirmed by back-out (229.63 × $0.41 = $94.15). At the last actual close, **trailing P/E ≈ 539x and EV/EBITDA ≈ 167x**, not 230x/69.5x. Multiples below are shown as-reported with the corrected figure.
3. **The +198% "upgrade" is an artifact.** The revision tool compared the **FY2028** consensus ($5.754) against $1.930 — which is *exactly* the current **FY2027** consensus. That is a **period mismatch, not a revision**. 5.754 / 1.930 = 2.981 → the reported +198.1%. Genuine estimate-revision momentum cannot be measured with this output.

Also inconsistent internally: reported diluted EPS $0.41 vs. net income $237.8M ÷ 215.2M shares = **$1.10**.

---

### 1. Factor Scores Table

| Factor | Score | Sector Rank | Signal |
|--------|-------|-------------|--------|
| **Value** | P/E 229.6x → **~539x** adj.; EV/EBITDA 69.5x → **~167x**; P/FCF **−51.6x** (negative FCF) | **5 / 5** (worst) | **Very Bearish** |
| **Momentum** | −49.7% (12-1 tool); **−28.96%** since IPO close ($311.07→$221.00); **−45.8%** peak-to-trough; **+31.1%** off 6/25 low | **5 / 5** (worst) | **Bearish** (inflecting?) |
| **Quality** | ROE **−41.1%**; gross profit/assets **8.56%**; accruals **+10.66%** (>5% = poor); F-Score **5/9** | **5 / 5** (worst) | **Bearish** |
| **Low Vol** | Vol **113.7%**, beta **2.79** vs SPY, max DD **−45.8%** (32d) | **5 / 5** (worst) | **Strongly Bearish** |
| **Earnings Revision** | +198.1% reported → **spurious (period mismatch)**. Real picture: FY26 **−$0.16**, FY27 **$1.93**, FY28 **$5.75**; 4–6 analysts; FY27 range **$1.00–$2.83** (±47% dispersion) | **n/a — not measurable** | **Neutral / Uninformative** |

**Peer value context (semis):** MU 9.5x, NVDA 30.8x, AVGO 74.2x, AMD 200.1x, **CBRS 539x**. CBRS is the only name in the group with **negative** FCF and negative ROE.

---

### 2. Price Statistics

| Metric | Reported (252d window) | Reality |
|---|---|---|
| Alpha (ann.) | **−159.77%** | Artifact — arithmetic of a −29% move over 32 days |
| Beta vs SPY | **2.815** | t ≈ 2.1, but on 32 obs. **Not reliable** |
| R² | **0.126** | Only **12.6%** of variance is market-explained → **87% idiosyncratic** |
| Sharpe | **−1.473** | n=32, not significant |
| Sortino | **−2.901** | n=32, not significant |
| Ann. Vol | **113.65%** | vs semis peers ~40–55% → **2–3x group vol** |
| Max Drawdown | 73.73% (unverified, doesn't reconcile) | **−45.8%** close-to-close, verified |
| Return since IPO | — | **−28.96%** |
| Correlation vs SPY | — | **0.353** |
| Correlation vs NVDA/AMD/AVGO/MU | — | **0.38 / 0.38 / 0.31 / 0.40** |

The **low peer correlation (0.31–0.40)** for a semiconductor is itself a red flag: returns are driven by lockup/float mechanics and single-name sentiment, not sector fundamentals. Beta of 2.79 with R² of 0.13 is an unstable estimate you should not hedge with.

---

### 3. Composite Quant Signal

## **SELL** (factor composite = **Strong Sell**; conviction tempered only by sample-size void)

Every measurable factor lands in the **bottom quintile of its sector**. There is no factor support at any horizon. The sole positive signal in the data — the "+198% upgrade" — is a **demonstrable computational artifact**, and removing it leaves the composite with zero bullish inputs. What prevents an unqualified "Strong Sell" is not valuation (which is the single most extreme reading in the dataset) but the honest fact that **32 days is not a sample**.

**The one genuine positive:** +31.1% off the 6/25 low on rising volume, and fundamentals that are *directionally* improving — revenue $78.7M → $290.3M → $510.0M (+650% over two years), gross profit turning from $26.4M to $199.1M, and consensus FY28 EPS of $5.75 implying a **~38x 2028 P/E** at the last close. That is a real optionality story. It is not a quant signal.

---

### 4. Key Quant Risk Flags

- **🔴 Sample size (critical):** n=32 trading days. No vol, beta, alpha, Sharpe, or Sortino figure here reaches statistical significance. Do not size a position using these.
- **🔴 Valuation-tail risk:** ~539x trailing P/E, ~167x EV/EBITDA, negative FCF. Most expensive name in the semi peer set by a wide margin on every multiple.
- **🔴 Momentum reversal risk (two-sided):** Down 45.8% from peak but up 31.1% in four sessions. At 113% annualized vol, a single day's ±15% move is ~1 standard deviation. Position sizing must assume fat tails.
- **🔴 Factor crowding — the opposite risk:** At 0.31–0.40 correlation to semis, CBRS provides **less** sector-beta diversification than its industry label implies. It is an idiosyncratic bet, not a semi exposure.
- **🟠 Liquidity:** IPO-float dynamics. Volume spiked to 21.4M and 18.4M shares on 6/24–6/25 selloff days vs. 3.8–5.8M typical. Lockup expiry is an unmodeled, unhedgeable event risk.
- **🟠 Earnings quality:** Accruals ratio +10.66% (2x the 5% warning threshold); F-Score components F2 (positive operating CF), F4 (accruals), F8 (gross margin trend), F9 (asset turnover) all **fail**. F-Score of 5 is entirely carried by leverage and dilution items.
- **🟠 Estimate dispersion:** FY27 EPS range $1.00–$2.83 across 6 analysts (±47%); FY28 range $5.14–$6.31 on only 4 analysts. Consensus is thin and unstable — consensus-EPS-based valuation is unreliable here.

**Bottom line:** A bottom-quintile-on-everything stock with an unreliable data feed and 32 days of price history. The quant verdict is **SELL**, but the honest read is that *CBRS is not yet quantifiable* — recommend re-running the full factor stack once ≥120 trading days exist and one full estimate-revision cycle has printed. Until then this is a fundamental/qualitative position, not a factor position.
