# Quant Analyst

- Symbol: AMD
- Elapsed: 43.2s

---
## AMD — Quantitative Factor Report
**Price:** $534.06 (2026‑11‑13) | **Mkt cap:** $875.9B | **Diluted shares:** 1.636B | **Sector:** Technology / Semiconductors

---

### 1. Factor Scores Table

| Factor | Score / Raw Inputs | Sector Rank* | Signal |
|---|---|---|---|
| **Value** | P/E 201.5x · EV/EBITDA 119.3x · P/FCF 129.7x · P/B 13.9x · div yield nil | **4 / 4** (worst on P/E, EV/EBITDA, P/FCF; 2/4 on P/B) | **Strong Sell (deep negative)** |
| **Momentum** | 12‑1 raw price momentum **+127.8%** (11/14/25 $246.81 → 10/15/26 $562.23); tool output +8.07% (see flags) | **1 / 4** (vs NVDA −2.1%) | **Strong Buy** |
| **Quality** | ROE 6.88% · ROIC 5.47% · GP/Assets 0.223 · accruals −4.39% | **4 / 4** on returns; **1 / 4** on accruals | **Neutral–negative** (level weak, trend improving) |
| **Low Vol** | Ann. vol **76.2%** · beta 3.56 vs SPY · max DD 37.7% | **4 / 4** (NVDA 39.9% vol / β1.75) | **Strong Sell (negative)** |
| **Earnings Revision** | +30.5% "upgrade" (see caveat) · PT median **$625** = **+17.0%** implied upside; 8 of 8 recent PTs ≥ $540; Oppenheimer upgrade to Outperform 11/09/26 | **1 / 4** | **Buy (with data caveat)** |

\*Rank vs large‑cap semiconductor comparables NVDA, AVGO, MU (TSM excluded — invalid feed, see flags). n=4 is too small for quintile statistics; treat ranks as directional only.

**Value detail — trailing multiples are on stale FY25 earnings.** The picture changes materially on forward consensus:

| Period | EPS est. | Forward P/E |
|---|---|---|
| FY2025A | $2.65 | 201.5x |
| FY2026E | $8.07 | **66.2x** |
| FY2027E | $17.82 | **30.0x** |
| FY2028E | $26.34 | 20.3x |

FY2026E revenue $52.2B (+50.7% y/y); FY2027E $96.4B (+84.7% y/y). On FY28E EPS the 2‑yr CAGR is ~81%, implying **PEG ≈ 0.8** — statistically "cheap on growth," but the growth estimates are effectively a single-scenario AI datacenter bet.

---

### 2. Price Statistics (252 trading days, vs SPY)

| Metric | Value |
|---|---|
| Annualised return | **159.2%** |
| Annualised volatility | **76.2%** |
| Beta (OLS, 252d) | **3.577** |
| Alpha (annualised) | **+102.9%** |
| R² | 0.447 |
| Sharpe (rf = 0) | **2.067** (≈2.01 at 4% rf) |
| Sortino | **3.431** (implied downside dev. ≈46.4%) |
| Max drawdown | **−37.7%** ($649.42 on 10/06/26 → $404.40 on 11/05/26) |
| Current vs. peak | **−17.8%** |
| YTD 2026 return | +139.0% ($223.47 → $534.06) |
| 5‑yr monthly beta (profile) | 2.49 |

**Statistical significance — critical:** with only ~1 year of daily data, SE(Sharpe) ≈ 1.77 → **t ≈ 1.17, not significant**. SE(alpha) ≈ 56.7% (residual vol) → **t ≈ 1.81, p ≈ 0.07, marginal**. The headline 2.07 Sharpe and 103% alpha are *not* statistically distinguishable from luck/skill at conventional confidence. Treat the point estimates as descriptive, not evidence of durable outperformance.

Piotroski **F‑Score = 8 (Strong)**: all components positive except F5 (leverage increased). This is the strongest single positive in the dataset and corroborates the fundamental improvement trend (ROE 2.41% → 1.53% → 2.85% → 6.88% over FY22–FY25).

---

### 3. Composite Quant Signal: **NEUTRAL**

The factors are in open conflict, and the honest read is a split verdict:

- **Bull case (quantified):** top-ranked momentum (+127.8% 12‑1), F‑Score 8, accelerating fundamentals, negative accruals (earnings cash-backed: OCF $7.71B vs NI $4.34B), unanimous-and-rising sell-side PTs (median +17% upside), PEG < 1.
- **Bear case (quantified):** bottom-ranked value (201x trailing P/E), bottom-ranked low‑vol (76% vol, β 3.6), weak absolute quality (ROIC 5.5%), and a *realised* −37.7% drawdown that shows the de-rating risk is not hypothetical.

Momentum and revision factors say Buy; value, quality level and risk factors say Sell. A quality‑plus‑momentum mandate could justify an overweight; a value, low‑vol, or risk‑parity mandate must exclude AMD outright. Net: **Neutral**, with the caveat that the risk-adjusted statistics are not statistically significant.

---

### 4. Key Quant Risk Flags

1. **Momentum reversal risk — highest priority.** Parabolic profile: +139% YTD 2026 and +128% 12‑1 momentum, but the stock has *already* given back 37.7% peak-to-trough in five weeks (Oct 6 → Nov 5). Buying after a vertical advance of this magnitude with β 3.56 has historically poor risk-adjusted entry characteristics. Price now sits roughly at its ~50‑day mean (~$543) and an estimated mid‑teens percent above its ~200‑day mean — a posture typical of late-stage trends, not early ones.
2. **Estimate-revision figure is an artefact — do not use as-is.** The reported +30.51% "upgrade" compares a **FY2030** estimate ($45.93) to a **FY2029** estimate ($35.19) — different fiscal years, i.e. a roll-forward, *not* a same-period revision. Genuine revision evidence comes from the PT cluster (median $625, 8/8 ≥ $540, one upgrade).
3. **Extreme estimate dispersion.** FY2028E revenue range **$105.9B–$205.7B** (high ≈ 1.94× low) across 39 analysts; FY2030E EPS range $37.54–$59.58. The forward multiple — the entire valuation case — rests on a forecast with ~2x uncertainty. Any FY2027 revenue shortfall vs. the +84.7% consensus collapses the 30x forward P/E.
4. **Factor crowding / beta concentration.** β 3.577 with R² only 0.447 means two-thirds of the 76% vol is idiosyncratic. AMD contributes disproportionate risk to any market or semis-exposed book; it failed the low‑vol screen by the widest margin in the peer set.
5. **Multiple-compression asymmetry.** At 130x P/FCF and 119x EV/EBITDA, a mere 10% earnings miss historically maps to far more than 10% price damage for this name — confirmed by the 37.7% drawdown.
6. **Data integrity issues (disclosed):**
   - **TSM valuation feed invalid** (P/E 1.20, EV/EBITDA 0.0, P/B 0.38 — ADR/local-currency and EV mis-scaling). Excluded from peer ranking; sector n reduced to 4.
   - **Momentum tool output inconsistent with raw prices.** The tool returned +8.07% over a 252‑day lookback, but the underlying price files show +127.8% for the equivalent 12‑1 window and +159.2% for the 252‑day window. The 8.07% figure appears to reflect a much shorter effective lookback (~3.5 months). I used the **verified raw-price momentum**; the tool's *sign and relative ranking* still agree (AMD positive, NVDA negative), so the directional conclusion holds.
   - **Sample size:** 4 peers, 1 year of daily data. No quintile statistics are defensible; ranks are ordinal only.
7. **No liquidity flag.** ~$876B cap, 15–50M shares/day; institutional capacity is not a constraint. No correlation matrix was computed (budget) — β and R² serve as the market-exposure proxy; peer correlations inferred from sector membership only.

**Bottom line:** The numbers do not support a valuation or risk story — they support a *momentum and fundamental-inflection* story. On a factor-balanced basis AMD is expensive, high-risk, and improving; that combination is only investable with a strict momentum/discipline overlay and position sizing consistent with a 77% vol, 3.6-beta instrument.
