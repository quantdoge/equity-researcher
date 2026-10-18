# Quant Analyst

- Symbol: BSP
- Elapsed: 57.7s

---
## BSP — Quantitative Factor & Risk Report
**Bending Spoons S.p.A.** · Technology / Software-Application · Italy · Mkt cap ≈ $29.9B
Data as of 2026-10-15. **Critical caveat up front: BSP IPO'd 2026-07-01 — only ~74 trading days (~3.5 months) of price history exist.** Every "252-day" statistic below is therefore computed on ~74 observations, not a year. Alpha, beta, Sharpe and Sortino are mechanically annualized from a 3-month sample and are **not statistically reliable**. Read the factor table, but discount the risk metrics heavily (details in §4).

---

### 1. Factor Scores Table

| Factor | Score (0–100 pctile) | Sector Rank | Signal |
|--------|----------------------|-------------|--------|
| **Value** | ~5 | Bottom decile | **Strongly negative** — EV/EBITDA 73.6x, P/FCF 97.2x, P/B 28.4x, P/E ~n/a (2025 net income −$0.14M, i.e. loss). Priced for perfection. |
| **Momentum** | ~65 | Upper third (raw price) | **Positive but fragile** — +10.96% "12-1" return, but measured on ~2.5 months, not 12. Notably *excludes* the +47% two-day spike (Oct 14–15), which falls in the skipped 21-day window. |
| **Quality** | ~30 | Bottom third | **Weak** — ROE −0.01% (2025), Piotroski F-score 4/9, GP/Assets 0.18. Offsets: negative accruals (−0.061, high earnings quality on cash basis) and positive operating CF ($291M). |
| **Low Vol** | ~2 | Bottom 2% | **Strongly negative** — 121.3% annualised vol (~5–6× market), max drawdown 40.1%. Un-investable on a low-vol/long-only-risk mandate. |
| **Earnings Revision** | ~90 | Top decile | **Strongly positive** — forward EPS raised +79.4% (2027e $2.44 vs. prior $1.36). Only 5 analysts — thin, high-dispersion coverage (range $1.95–$2.93). |

**Note on sector rank:** peer/ranking infrastructure is mega-cap-biased — the sector-peer tool returns semiconductors (NVDA, TSM, MU…) and the 25-name ranking universe does **not include BSP**. Ranks above are qualitative placements versus that mega-cap universe, not a true Software-Application peer set. Treat as directional.

---

### 2. Price Statistics (252-day window = ~74 actual observations)

| Metric | Value | Reliability |
|--------|-------|-------------|
| Annualised alpha vs SPY | **+114.8%** | ⚠️ Not usable — R² = 0.0003 |
| Beta vs SPY | **0.178** | ⚠️ Meaningless at R²≈0; profile beta = 1.48 → true beta unknown |
| R-squared | 0.0003 | Market explains 0.03% of BSP variance |
| Annualised volatility | **121.3%** | High but directionally credible (short window overstates) |
| Sharpe ratio | **0.96** | Annualised from ~74 days — upward-biased |
| Sortino ratio | **1.93** | Same caveat; small downside sample |
| Max drawdown | **−40.1%** (peak close $53.44 → $32.03) | Consistent with price history |
| Cumulative return (Jul 1 → Oct 15) | **+37.7%** ($40.50 → $55.77) | First-to-last close |
| Latest close / snapshot price | **$55.77** vs. ratios model **$47.07** | Valuation multiples understated ~18.5% at $55.77 |

**Reading the alpha:** A +114.8% "alpha" with R² of 0.0003 is the textbook signature of annualizing a short, low-correlation price path. The regression has essentially zero explanatory power and near-zero degrees of freedom; the t-stat on alpha is not meaningful. Do not cite this as genuine market-neutral outperformance.

---

### 3. Composite Quant Signal: **NEUTRAL (low conviction)**

- **Bearish:** Value bottom-decile, Quality bottom-third (negative ROE, F-score 4), Low-Vol bottom-2%, EV/EBITDA 73.6x on a loss-making base. The core value/quality/low-vol triplet — the classic robust composite — is uniformly poor.
- **Bullish:** Earnings-revision momentum top-decile (+79%), strong operating cash flow ($291M, positive and rising), and a violent recent price uptrend (+47% in two sessions).
- **Net:** One strong factor (revisions) offsets four weak ones, and every risk statistic is unreliable on 3 months of post-IPO data. **Composite = Neutral, statistically low confidence.** A momentum/revision trader can justify a speculative long; a factor-disciplined, risk-budgeted mandate gets no clean signal here.

---

### 4. Key Quant Risk Flags

1. **Sample-size failure (the dominant risk).** ~74 trading days since IPO. Alpha, beta, Sharpe, Sortino, and "12-1" momentum are all computed on far less than their stated windows. **Do not rely on the beta of 0.178 or alpha of 114.8%.** The profile's beta (1.48) contradicts the regression — real market sensitivity is unknown.
2. **Factor crowding / event risk.** Oct 14 traded 19.6M shares (+41% day) and Oct 15 hit $55.77 — an event-driven spike (news/catalyst). Classic post-IPO **lockup-expiry overhang** likely ~Jan 2027; supply shock risk.
3. **Extreme volatility / position sizing.** 121% annualised vol and 40% peak-to-trough drawdown → any position needs <½ normal weight to hold risk constant. Tail risk high.
4. **Valuation asymmetry.** EV/EBITDA 73.6x, P/FCF 97x, P/B 28x with a 2025 net loss → negative P/E. Multiples are ~18.5% *higher* at the current $55.77 than the $47.07 used in the ratio model. No valuation cushion.
5. **Liquidity & data integrity.** Average volume ~1–2.5M shares with episodic 7–20M spikes; pre-lockup float may be thin. Price feed shows an $47.07 snapshot vs. $55.77 last trade — flag model/price mismatch to the desk.
6. **Thin, dispersed analyst coverage.** Revisions rest on 5 EPS analysts and 7 revenue analysts; 2027 EPS range $1.95–$2.93 (±25%). The +79% upgrade is real but rests on a base that appears to conflate the 2026 estimate ($1.36) with the 2027 period — treat the magnitude with caution.

**Bottom line:** The data tell a clear story — BSP is an expensive, low-quality, high-volatility recent IPO with genuinely strong estimate-revision momentum. The revision signal is the only quantitatively clean positive, and even the risk metrics purporting to describe it are untrustworthy on 3.5 months of history. Signal: **Neutral / speculative; re-run the full panel after 6–12 months of trading history.**
