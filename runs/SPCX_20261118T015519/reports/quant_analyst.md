# Quant Analyst

- Symbol: SPCX
- Elapsed: 42.2s

---
## SPCX — Quantitative Factor & Risk Report

**SpaceX ($SPCX) · Industrials / Aerospace & Defense · Price $141.70 · IPO 2026-06-12**

⚠️ **Data integrity flag before anything else:** Two figures conflict badly. `calculate_valuation_ratios` implies a market cap of **$414.6B** ($141.70 × 2.926B diluted shares), while `get_company_profile` reports **$1.867T** (implying ~13.2B total shares incl. non-public classes). All multiples below use the $414.6B basis; on the $1.867T basis **every valuation multiple rises ~4.5x** (EV/EBITDA ~435x). Do not act on either number without reconciling the share count.

---

### 1. Factor Scores Table

Peer set = GE, RTX, LMT, BA (A&D comparables; n=5, so "rank" is coarse — quintiles of 5 are fragile).

| Factor | Score (0–100) | Sector Rank | Signal |
|--------|---------------|-------------|--------|
| Value | **5** | 5 / 5 | Strongly negative |
| Momentum (12-1) | **75** | 1 / 5 | Positive (low confidence) |
| Quality | **32** | 5 / 5 | Negative |
| Low Vol | **4** | 5 / 5 | Strongly negative |
| Earnings Revision | **62** | n/a | Upgrade (low confidence) |

**Value (worst in class).** EV/EBITDA **96.2x** vs peer median ~20.4x (LMT 17.7, RTX 20.1, BA 20.4, GE 29.5) — 4.7x the median. P/B 10.04x (3rd of 5). P/E **−83.9x** and P/FCF **−29.7x** are unusable — negative earnings make the value composite a distortion-prone proxy here. Note 49.4% gross margin and strong cash conversion make EV/EBITDA on *trailing* EBITDA (FY25 $4.29B) a harsh read on a business inflecting to profitability.

**Momentum (best in class — but the comparison is invalid).** Reported +6.52% vs GE −18.1%, RTX −13.5%, LMT −8.5%, BA −18.2%. SPCX ranks 1/5. **However**, peers' figures span a true 252-day window while SPCX's spans only ~110 days post-IPO — this is an apples-to-oranges ranking. My own recomputation from the raw price file: **−11.96% since inception** (160.95 → 141.70) and **−8.07%** IPO-to-21-days-ago. The genuine reading is *modestly negative absolute momentum*, currently recovering (+30.9% off the 8/5 low). The "1/5" rank is really a statement that peers are in deeper downtrends.

**Quality (worst in class).** ROIC **−4.03%** vs LMT 27.2%, GE 22.3%, RTX 8.7%, BA 7.2%. ROE −11.95%. ROIC has deteriorated from +1.18% (FY24) to −4.03% (FY25). Piotroski F-Score **5/9** (moderate) — fails on negative ROA, worsening leverage (interest expense $1.58B→$1.95B), and no asset-turnover improvement. **The one genuinely high-quality datum:** accruals ratio **−0.127**, i.e. operating CF $6.79B against net income −$4.94B. Earnings are *understated* by GAAP, not overstated — D&A of $6.70B is the driver, and cash conversion is real. Gross margin improved 41.2% → 42.9% → 49.4% (FY23–25), revenue +33.2% YoY.

**Low Vol (worst in class).** 78.9% annualised vol vs peer median ~32% (RTX 26.7, LMT 31.4, GE 35.0, BA 36.0) — **2.2x** the peer median. Beta 2.42 vs SPY. Max drawdown 46.4%. This is the single most damning factor score.

**Earnings Revision (flagged, not trusted).** Tool reports FY2028 consensus EPS $9.90 vs $4.21 prior, **+135%**, signal "upgrade." Two material caveats: (a) the "prior" value of 4.21 is *identical* to the current FY2027 consensus, suggesting a period-mismatch rather than a true same-period revision; (b) analyst dispersion is absurd — FY2028 EPS range **$0.37 to $48.77** across 30 analysts (a 132x spread). Consensus on this name carries almost no information. FY2025 did beat: actual EPS −$1.69 vs −$2.94 estimated.

---

### 2. Price Statistics

| Metric | Value | Reliability |
|---|---|---|
| Annualised return (tool) | +1.16% | ⚠️ conflicts with −11.96% actual price change |
| Realised return since IPO | **−11.96%** | Hard fact (160.95 → 141.70) |
| Annualised volatility | 78.92% | Directional only |
| Beta vs SPY | **2.442** | Significant (t≈5.2) |
| R² vs SPY | **0.197** | — |
| Alpha (annualised) | +2.92% | **Not significant (t≈0.03)** |
| Sharpe ratio | **0.015** | **Not significant** |
| Sortino ratio | **0.024** | **Not significant** |
| Max drawdown | **−46.35%** | Close-to-close, 6/16 high 201.80 → 8/5 low 108.27 |

**Statistical power warning.** The entire return series is **110 trading days ≈ 0.44 years**. Standard errors at this sample size: SE(beta) ≈ 0.47; SE(annualised alpha) ≈ 107%; SE(annualised Sharpe) ≈ 1.5. Therefore:
- Beta 2.44 is statistically real, but explains only **19.7%** of variance — ~80% of SPCX risk is idiosyncratic. It offers essentially no diversification benefit against a market or A&D sleeve.
- **Alpha of +2.92% is indistinguishable from zero.** Sharpe 0.015 and Sortino 0.024 are likewise statistically meaningless — both are within one SE of a coin flip. Do not cite these as evidence of risk-adjusted outperformance.

---

### 3. Composite Quant Signal: **NEUTRAL** (composite 41/100, negative tilt)

Weights: momentum 30%, quality 25%, value 20%, revisions 15%, low-vol 10% → 0.30(75) + 0.25(32) + 0.20(5) + 0.15(62) + 0.10(4) = **41.2**.

The name splits cleanly in two. Positive: peer-relative momentum, reported upward revisions, improving gross margin, strong cash conversion, 33% revenue growth. Negative: worst-in-class valuation, profitability, and volatility. **Three of five factors sit in the bottom quintile.** The two supportive factors (momentum, revisions) are precisely the two whose data I trust least. I would not size a position on this composite — a 110-day sample cannot support a factor conclusion.

---

### 4. Key Quant Risk Flags

1. **Sample-size failure (primary).** 110 trading days. Sharpe, Sortino, and alpha are statistically void. Any backtest-style inference from this history is unreliable.
2. **IPO lockup expiry imminent.** IPO 2026-06-12 + standard 180-day lockup ≈ **early December 2026** — within weeks of the current data date. Substantial supply overhang; historically the highest-risk window for post-IPO volatility and drawdown.
3. **Post-IPO momentum decay in progress.** −46.4% drawdown inside the first three months (201.80 → 108.27), only partially recovered. Classic post-IPO price-discovery pattern; reversal risk runs both directions.
4. **Market-cap model risk.** $414.6B vs $1.87T is a 4.5x discrepancy. Every valuation conclusion scales with it. **Unresolved.**
5. **Idiosyncratic/single-name risk.** R² 0.197 → 80% diversifiable-in-theory but undiversified-in-practice exposure. Peer correlation matrix not computed (budget) — **gap**.
6. **Valuation is entirely back-loaded.** At $414.6B: 96x trailing EV/EBITDA → 28x on 2026E → 6.6x on 2027E → 2.2x on 2028E. The thesis requires revenue to compound 19.3B → 48.2B → 165.0B → 337.5B over three years (CAGR ~160%) **and** EBITDA margin to reach 55.7%. Any slippage collapses the multiple support.
7. **Consensus is uninformative.** FY2028 EPS dispersion 0.37–48.77; FY2026 range −0.73 to +0.95. Do not treat the revision "upgrade" as signal.
8. **Not a liquidity flag.** Dollar volume is exceptional (~$12B/day at recent volumes). Exit capacity is not a constraint.

**Bottom line:** A high-beta, high-volatility, richly-valued growth name with best-in-class cash conversion but worst-in-class profitability and valuation, entering a lockup window, on a return history too short to support statistical inference. Quantitatively: **Neutral, avoid on risk grounds until the sample lengthens and the share count is reconciled.**
