# Quant Analyst

- Symbol: GS
- Elapsed: 197.3s

---
## GS — Goldman Sachs Group — Quant Factor Report

**Data as of latest close: $902.56 | Mkt cap $266.3B | Sector: Financial Services (Capital Markets)**
Benchmark for all market stats: SPY, 252-day window. Cross-sectional ranks built against a hand-curated 7-name large-cap financial peer set (JPM, MS, C, BAC, WFC, BX, BLK) — the `rank_universe_by_factor` tool's universe resolved to a 25-symbol fund-heavy list that excludes GS, so official quintile ranks are **not available** (data gap, flag below).

---

### 1. Factor Scores Table

| Factor | Score | Sector Rank (of 7 peers) | Signal |
|--------|-------|--------------------------|--------|
| **Value** | P/E 17.6, P/B 2.29, EV/EBITDA 11.3, DivYld 1.99% | #4/7 (mid) | Neutral |
| **Momentum** | 12-1 mo. return **−3.2%** | Bottom half (inferred; peers not computed) | **Negative** |
| **Quality** | ROE 13.7%, ROIC ~3.0%, GP/Assets 3.3%, Accruals 3.4%, F-Score 5/9 | Mid | Moderate / Low |
| **Low Vol** | β 1.72 vs SPY, ann. vol 34.0% | Bottom (highest-beta major bank) | **Negative** |
| **Earnings Revision** | Forward EPS est. +2.0% vs 3-mo ago (2029E: $78.69 vs $77.16) | Positive | **Upgrade** |

**Value detail:** GS trades at a P/E below Morgan Stanley (18.7), Citi (18.4) and BX (28.8) but at a premium to JPM (16.6), BAC (14.1), WFC (12.7). P/B of 2.29 sits mid-pack (JPM 2.56, MS 2.69, C 1.12, BAC 1.34, WFC 1.41). P/FCF is negative (−6.1×) — an accounting artifact of bank working-capital treatment, not a real signal; ignore it for banks. **Value is fair-to-slightly-rich, not a standout.**

**Quality detail:** ROE has compounded upward sharply: 7.3% (FY23) → 9.6% (FY22 reported series) → 11.7% (FY24) → **13.7% (FY25)**. Accruals ratio 3.4% is "ok" but has roughly doubled since FY23 (1.3%) — mild earnings-quality erosion. Piotroski F-Score = 5 (moderate): profitability improving, but operating-cash-flow and leverage subcomponents negative.

**Revision detail:** Consensus EPS trajectory is cleanly upward — FY26E $68.35 → FY27E $72.44 → FY28E $77.16 → FY29E $78.69 (+6.0% FY25-26 CAGR). The +2.0% 3-month revision is a genuine upgrade. **Caveat:** the revision comparator is the *2029* estimate, covered by only 4 analysts — small sample, treat as directional only.

---

### 2. Price Statistics (1-year, vs SPY)

| Metric | Value |
|---|---|
| Alpha (annualised) | **−20.9%** |
| Beta | 1.73 (1-yr OLS; 1.28 per profile, longer-horizon) |
| R² vs SPY | 0.44 |
| Sharpe ratio | **0.03** |
| Sortino ratio | **0.04** |
| Annualised return | +0.95% |
| Annualised volatility | 33.8–34.0% |
| Max drawdown | **−21.8%** |
| Peer correlation | MS 0.86 · C 0.66 · JPM 0.63 · BAC 0.57 · BLK 0.54 · BX 0.45 · WFC 0.44 |

The stock produced essentially **zero absolute return at roughly 1.7× market beta** over the past year — that is a strongly negative alpha profile. It has retraced from ~$1,150 (Jul 2026) to $902, a ~21% drawdown. Recent sell-side targets cluster $995–$1,300 (Evercore cut to $1,000 in Oct 2026; BofA $1,300, Citi $1,200, UBS $1,150); the market price sits ~10% below the lowest.

---

### 3. Composite Quant Signal: **NEUTRAL (Hold)**

| Factor | Weighting contribution |
|---|---|
| Momentum | − |
| Low Vol | − |
| Alpha/Beta profile | − |
| Earnings revisions | + |
| Quality trend (ROE) | + |
| Valuation | 0 |

**Scorecard: 2 negative, 2 positive, 1 neutral.** The positives (estimate revisions, ROE improvement, moderate valuation) are real, but the price structure (negative 12-1 momentum, −20.9% alpha at 1.73 beta, 34% vol) does not yet confirm them. Revisions are a leading indicator, so a Buy would require momentum/price confirmation — not present. **Neutral, tilted constructive on fundamentals, technically weak.**

---

### 4. Key Quant Risk Flags

1. **Momentum reversal / trend risk (HIGH):** −3.2% 12-1 momentum, −20.9% alpha, price 21% off highs; the 200-day trend is down while the sector/SPY is positive (~+5%). Short-term mean-reversion risk is elevated; a continuation leg lower is the base case until momentum inflects.
2. **Factor crowding / beta risk (HIGH):** Correlations of 0.86 (MS) and 0.66 (C/JPM) mean GS is a concentrated bet on the large-cap bank complex; a financials drawdown would hit all positions together. β≈1.7 amplifies this ~70% above market.
3. **Low liquidity: N/A** — $266B mega-cap, deep two-sided flow; not a liquidity concern. Flag: the recent **negative free cash flow** reading is a banks-standard artifact and should not feed P/FCF screens.
4. **Data/sample caveats:** (a) official cross-sectional factor ranks unavailable — `rank_universe_by_factor` returned a 25-name fund-heavy universe excluding GS; sector ranks above are hand-built from 7 peers. (b) The +2.0% revision signal relies on the FY2029 consensus (n=4 analysts); FY26-28 series (n=11–17) is better populated and consistent, so the signal direction is credible but magnitude is uncertain. (c) Sortino/Sharpe assume 0% risk-free and a single 252-day window — Sharpe 0.03 is effectively indistinguishable from zero; do not read it as precise.

**Bottom line:** A high-beta, low-alpha momentum laggard with genuinely improving fundamentals and positive estimate revisions. Quant composite is **Neutral** — wait for price confirmation (12-1 momentum turning positive and a break back above the prior downtrend) before upgrading to a Buy, or for a sharper multiple de-rating (P/E <15) to make the value case compelling.
