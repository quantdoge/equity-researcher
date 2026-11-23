# Quant Analyst

- Symbol: CLS
- Elapsed: 27.2s

---
## CLS — Celestica Inc. | Quantitative Factor Report

**Snapshot:** Price $201.63 (2026-11-20) · Mkt cap $25.4B · Technology / Hardware, Equipment & Parts (EMS) · Canada-domiciled, USD reporting

*Peer set:* The sector feed returns only megacaps (AAPL, MSFT, NVDA), which are not valid comps for an EMS provider. I substituted the true industry peer group — **FLEX, JBL, SANM, PLXS** — for all cross-sectional ranks (n=5; ranks 1=best, 5=worst).

### 1. Factor Scores

| Factor | Score / Raw Values | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E 27.7x · EV/EBITDA 19.6x · P/FCF 51.1x | **5 / 5** | Negative — most expensive in group on all three multiples |
| **Momentum** | 12-1 return **−25.2%** | **3 / 5** | Negative absolute, mid-pack (PLXS −17.8, SANM −24.6, JBL −26.0, FLEX −38.4) |
| **Quality** | ROE 37.6% · ROIC 34.2% · GP/Assets 20.8% · Accruals 0.024 · F-Score 7/9 | **2 / 5** | Positive — ROIC/ROE best-in-class ex-JBL |
| **Low Vol** | 81.7% ann. vol · β 3.06 · Max DD 57.3% | **4 / 5** | Negative — only FLEX (83.0%) is worse |
| **Earnings Revision** | +20.95% (tool) — **artifact, see below** | n/a | Unreliable; near-term trajectory genuinely upward |

**Value (detail):** CLS trades at a premium to peer medians on every metric — EV/EBITDA 19.6x vs peer median 13.9x (+41%), P/FCF 51.1x vs median 17.6x (+190%), P/E 27.7x vs median 24.4x. There is no value support here.

**Quality:** The factor engine stamps this "low," which I believe mis-scores the input. ROIC has compounded from 11.7% (2022) → 13.2% → 22.3% → **34.2% (2025)**, with ROE 37.6%. Piotroski 7/9 loses points only on accruals quality (F4) and leverage (F5) — both consistent with a working-capital-heavy, growth-funded EMS balance sheet, not deterioration. This is the one genuinely strong pillar.

**⚠ Earnings Revision — do not use as printed.** The engine compared the **FY2030** EPS estimate ($46.63) against the **FY2029** estimate ($38.55) and labeled the +20.95% gap a "revision." That is a fiscal-year comparison, not a revision of the same forward period — a data artifact. Coverage at those horizons is only 2–4 analysts, so ranges are meaningless. The defensible read: the FY2026 consensus (12 analysts, $11.31) sits **+89%** above FY2025 ($5.98), and implied TTM EPS from the P/E ratio (~$7.29) already exceeds the stale FY2025 consensus snapshot — consistent with *upward* revision pressure. FY2027 $21.74 and FY2028 $31.26 imply a doubling-then-doubling curve that the market is now visibly discounting.

### 2. Price Statistics

| Metric | Value |
|---|---|
| Alpha (ann., vs SPY, 252d) | **−22.96%** |
| Beta (vs SPY, 252d) | **3.06** (R² 0.325) |
| Realized vol (ann.) | **81.7%** |
| Sharpe (0% RF) | **−0.206** |
| Sortino | **−0.297** |
| Ann. return | −17.04% |
| Max drawdown | **−57.3%** |
| 12-mo price return | −28.6% ($282.28 → $201.63) |
| 6-mo / 3-mo / 1-mo | −41.8% / −33.2% / **−32.7%** |
| YTD 2026 | −31.8% |
| Drawdown required to recover | **+134%** |

**Data integrity check — passed.** I verified the −57.3% max drawdown against raw OHLC: close high $472.40 (2026-06-02) → $201.63 (2026-11-20) = −57.3%. Exact match. The drawdown is real, not a split artifact.

**⚠ Statistical significance flags (important):**
- **Alpha is NOT significant.** With residual vol of ~68% annualized, the standard error on the annualized alpha is roughly **±68pp** (t ≈ −0.3). The −23% point estimate is directionally informative but statistically indistinguishable from zero.
- **Sharpe/Sortino are NOT significant** over a single 252-day window at 82% vol (SE on Sharpe ≈ 0.6; t ≈ −0.3). A one-year Sharpe at this volatility level has essentially no inferential power.
- **Beta IS significant:** se(β) ≈ 0.28, t ≈ 11. Treat *sensitivity* as reliable; treat *alpha* as noise-plus-signal.
- **Beta conflict:** the profile lists β 1.345 (long-window monthly) vs 3.06 (trailing daily). R² of only 0.325 means ~68% of CLS's variance is idiosyncratic — this is an AI-hardware sentiment vehicle, not a market proxy.
- The feed's "annualized return" (−17.04%) differs from the compounded 12-month price change (−28.6%); the gap is volatility drag plus methodology, not an error in the drawdown.

### 3. Composite Quant Signal

# NEUTRAL — with a distinct negative tilt

**Score: −1 of ±2.** Four of five measurable factors are neutral-to-negative on a relative basis; only Quality is positive.

Working through the evidence honestly:
- **Bear side:** worst-in-group valuation, −25% momentum inside a −57% drawdown, β 3.06, and negative risk-adjusted returns across every measure. Additionally, **the most recent 21 trading days delivered −32.7%** — and because standard 12-1 momentum *excludes* that window, the reported −25.2% **understates** the current deterioration. The momentum factor is flattered by construction.
- **Bull side:** Quality — ROIC 34.2%, ROE 37.6%, F-Score 7, accruals 0.024 (well below the 0.05 concern threshold), and rising ROIC four years running. Plus forward valuation optionality: on FY2026E $11.31 the stock is **17.8x**; on FY2027E $21.74 it is **9.3x**. If estimates hold, this is not expensive.
- **Why not Sell:** a −1 score, not −2, because the quality pillar is real, unbroken, and improving, and forward multiples are reasonable *if* the AI-infrastructure estimate curve survives. **Why not Buy:** you cannot underwrite a 3.06-beta, 82%-vol name on 9.3x FY2027E when the market has de-rated it 57% — that multiple is the market pricing estimate risk, not a discount.

**Screen logic:** a standard multi-factor model weighting value and momentum equally would classify CLS **Sell** (bottom-quintile value, below-median momentum, bottom-quintile low-vol). Only a quality-overlay mandate would hold it. Hence Neutral with negative tilt.

### 4. Key Quant Risk Flags

1. **Momentum reversal risk — realized, not prospective.** The stock is already in a violent downtrend (−57.3% from peak, −32.7% in one month, on above-average volume: 5.3M shares on 2026-11-20 vs ~2.4M 12-month average). Elevated down-volume = distribution, not capitulation.
2. **Factor crowding — highest in the peer group.** CLS ranks 5/5 on value and 4/5 on low-vol. It is a crowded, expensive, high-beta AI-hardware trade. Every EMS peer is down double digits, so this is a **sector-wide unwind**: diversification within the industry provides zero protection.
3. **Volatility regime.** 81.7% annualized vol is roughly 3x the historical norm for a $25B contract manufacturer. Position sizing must reflect the vol, not the market cap.
4. **Event/gap risk is severe.** Single-day moves of −14.4% (2026-04-28) and −13.3% (2026-08-06) occurred with no orderly trend. Earnings gaps, not drift, drive this name.
5. **Estimate-revision data gap.** The revision factor is unusable as computed (FY2030 vs FY2029 mislabeled as a revision). I could not obtain a true same-period revision history. Coverage thins to 2–4 analysts beyond FY2027, so the forward curve that "justifies" the multiple is thinly supported.
6. **Liquidity — NOT a concern.** ~$600M daily dollar volume; institutional-size entry/exit is feasible.
7. **Alpha/Sharpe non-significance** (per above) — do not build a thesis on the −23% alpha point estimate alone. This is a risk-management decision, not an alpha decision.

**Bottom line:** the numbers support a *quality asset in a broken price trend at a premium valuation*. Hold-and-monitor with strict risk limits; do not add on the basis of these factor scores. Re-underwrite the FY2027 EPS estimate — that single input is worth ~$0 vs ~$200/share of terminal value.
