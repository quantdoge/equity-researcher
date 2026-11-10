# Quant Analyst

- Symbol: BABA
- Elapsed: 98.0s

---
## BABA — Quantitative Factor Report (spot ≈ $105.38; data through ~Nov 2026)

### ⚠️ Data integrity note (read first)
Two feeds are broken and I will not build conclusions on them:
1. **All valuation multiples are currency-mixed and unusable as printed.** BABA files financials in **RMB**, while market cap/price are in **USD**. The tool printed P/E 2.4, P/B 0.23, EV/EBITDA 0.83, P/FCF −5.0 — these are arithmetic artifacts, not a 2x-earnings stock. I re-derive below.
2. **Earnings-revision feed is a null-value artifact** (−100% = current estimate 0.0 vs prior 73.47 on the FY2031 row where only 10 analysts cover). Not a downgrade signal — a missing-data signal.
3. Price history in my first pull ended 2026-07-31 ($122.25); price-target timestamps (latest 2026-11-09 at $109.45) confirm "now" is ~Nov 2026 and the $105.38 quote is live. Return statistics below are reconciled to that.

---

### 1. Factor Scores

| Factor | Score | Sector Rank (of 5) | Signal |
|---|---|---|---|
| **Value** | Corrected P/E **17.4x** FY26 (13.8x FY25); P/B **1.60x**; EV/EBITDA **≈5.5x** (est.); div yield 2.89% | **1 / 5** (cheapest) | **Attractive** |
| **Momentum** | −9.38% (12-1, official) / **≈−30%** realized trailing yr; −43.8% from Oct-25 peak | **2 / 5** (official) → **5 / 5** on realized basis | **Negative** |
| **Quality** | ROE 9.23%, GP/Assets 0.214, accruals +0.014; **ROIC 4.32%**; F-Score **4/9** | **5 / 5** (worst) | **Weak** |
| **Low Vol** | Vol 40.24% ann., β 0.92, R² 0.11 | **5 / 5** (highest vol); 2/5 on β | **Unfavourable** |
| **Earnings Revision** | *Not computable* — feed broken. Proxy: FY30 EPS est. 73.47 **below** FY29 78.65; FY29 est. dispersion 46.9–162.4 (3.5x) | n/a | **Neutral→Negative, low confidence** |

**Peer cross-section (value / quality / momentum / vol):** AMZN 37.2x / high / −4.4% / 36.2%; HD 24.8x / high / −11.8% / 28.5%; TJX 28.3x / high / −9.5% / 24.4%; MCD 23.6x / low / −12.3% / 21.9%. BABA is the **only name in the peer set in the top quintile on value and the bottom quintile on quality, momentum and volatility simultaneously.** That combination is not a "rare triple-win" — it is the canonical value-trap signature.

### 2. Price Statistics
| Metric | Value |
|---|---|
| Alpha (ann., vs SPY, 252d) | **−63.0%** — but see caveat |
| Beta (252d vs SPY) | **0.925** (5Y monthly profile β: 0.401) |
| R² vs SPY | **0.110** → 89% idiosyncratic |
| Sharpe | **−1.247** |
| Sortino | **−2.115** |
| Ann. return / vol | −50.5% (tool) / 40.5% |
| Max drawdown | **−43.2%** (peak $187.62 on 2025-10-02 → $94.81 low 2026-06-26 = −49.5% peak-to-trough) |

**Caveat on alpha/Sharpe:** with R² = 0.11 the "alpha" is almost entirely unexplained residual, not factor alpha; its standard error is enormous and the −63% magnitude is not reproducible from the OHLCV series (which shows roughly −30% over the trailing year). **Direction is reliable (materially negative risk-adjusted performance); magnitude is not.** Cross-checked Sharpe using realized −30% return on 40% vol ≈ −0.75 — still clearly poor, roughly half the reported figure.

### 3. Composite Quant Signal: **NEUTRAL (sell-leaning / underweight on risk-adjusted basis)**
Value is genuinely cheap, but the model requires top-quintile scores on value **AND** momentum **AND** quality. BABA scores 1/5, 5/5, 5/5. One of three conditions is not a buy.

**The deterioration is measured, coordinated, and recent (FY2026 vs FY2025):**
- Operating cash flow **−53.8%** (RMB 164.8B → 76.2B) while net income fell only −20.4%
- Accruals ratio swung **+9.4pp** (−1.92% → +1.44%) — earnings quality deteriorating every year for four years
- ROIC **10.51% → 4.32%** — now below any reasonable cost of capital
- Piotroski F-Score 4/9, with zero credit on accruals, leverage, margins, or turnover

Consensus targets ($160–$200, median ~$186, ~+75% upside) are the bull case, but note they were **serially cut** through H1-2026 ($225 → $186 → $175 → $170) before two recent raises. Targets are a lagging indicator; OCF and ROIC are not.

### 4. Key Quant Risk Flags
1. **Value-trap risk (highest conviction):** cheap multiple + collapsing ROIC + negative momentum + rising accruals. The market is pricing the earnings stream as impaired, and the cash-flow line supports that read.
2. **Momentum reversal / trend risk:** −43.8% from the Oct-2025 peak, trading below the 2026 recovery highs; 12-1 momentum negative on every measurement basis I computed.
3. **Idiosyncratic risk dominates:** R² 0.11 and β instability (0.40 five-year vs 0.92 one-year) mean SPY hedging will not protect this position. High vol (40%) with a −43% drawdown is not a low-vol holding.
4. **Sample/statistical limits:** 5-name peer set (thin for quintile ranking — treat ranks as indicative, not statistically robust); 252-day window only; FY2026 financials are 8 months old; **revision factor unavailable** and the FY2030 consensus EPS curve actually slopes *down* from FY2029.
5. **FX/dual-listing:** USD-quoted ADS over RMB-reporting China assets adds CNY translation risk not captured in any factor above.

**Bottom line for the memo:** BABA screens as an extreme deep-value / extreme low-quality split. Until OCF stabilises and ROIC re-crosses ~8%, the quantitative case is **not** "buy the cheapness" — it is "wait for the cash-flow inflections to confirm the valuation."
