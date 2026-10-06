# Quant Analyst

- Symbol: IBM
- Elapsed: 292.0s

---
All data gathered. I have everything needed for the full quant assessment.

---

# IBM (International Business Machines Corp.) — Quant Factor Report
*IT Services / Technology | Price $222.76 | Mkt Cap ~$210B | Data as-of latest close*

## 1. Factor Scores Table

| Factor | Score | Sector Rank* | Signal |
|--------|-------|-------------|--------|
| **Value** | P/E 19.9, EV/EBITDA 15.3, P/FCF 17.5, Div Yld 3.03% | ~20th / 25 mega-cap (bottom quintile) | **Neutral** |
| **Momentum** | 12-1m return **-13.95%** | Bottom 5 / 25 | **Strong Sell** |
| **Quality** | ROE 32.4%, ROIC 12.5%, GP/Assets 0.259, Accruals -0.017, F-Score **7/9** | Mid (outside top-20 / 25) | **Positive** |
| **Low Vol** | Ann. vol **53.7%**, beta 0.85 vs SPY, Max DD **-37.5%** | Bottom decile | **Strong Sell** |
| **Earnings Revision** | Fwd EPS est cut **-9.7%** (12.56 vs 13.91 prior) | Weak | **Sell** |

*\*Rankings are approximate: computed against the 25-name mega-cap universe returned by the ranker. Direct IT-services comps (ACN, INFY, etc.) are not in that universe — multiple-based sector rank is a partial gap.*

**Supporting detail:**
- **Value:** Cheapest mega-cap tech on P/E (NVDA ~50x, MSFT ~35x) but not top-quintile composite — P/B 6.45 is elevated for the group and FCF yield (~5.7%) is only mid-pack. Dividend yield 3.0% provides support.
- **Momentum:** Negative over 3, 6 and 12-month windows; stock has decoupled from a rising market (SPY momentum +5.0% over same window).
- **Quality (the one bright spot):** ROIC stable 10.8%→12.5% over 4 years; accruals negative every year 2022–25 (high earnings quality); Piotroski 7/9 — fails only on share dilution and asset-turnover improvement.
- **Revisions:** Far-dated estimates (FY28–FY30) carry only **2–3 analysts** — revision signal is directionally reliable (multiple July-2026 target cuts: GS $335→$270, BMO $270→$230, MS $293→$190; Susquehanna recently raised to $235) but **statistically low-confidence**.

## 2. Price Statistics (252-day window, benchmark SPY)

| Metric | Value |
|---|---|
| Alpha (annualised) | **-39.3%** ⚠️ |
| Beta | 0.86 |
| R² of market regression | **4.4%** (very weak fit) |
| Sharpe / Sortino | **-0.38 / -0.41** |
| Annualised return / vol | -20.4% / 54.3% |
| Max drawdown | -37.5% |
| Corr with SPY / MSFT / AAPL | 0.21 / 0.28 / 0.15 |

**Interpretation:** The large negative alpha is *not* a market-beta story — R² = 4.4% means the market factor explains essentially none of IBM's moves. The stock is trading on idiosyncratic news flow, and its realized volatility (54%) and drawdown (-37.5%) are inconsistent with its 0.71 fundamental beta. **Treat alpha/beta estimates as low-reliability** given the weak regression fit.

## 3. Composite Quant Signal: **SELL**

Weighting: Momentum (negative trend) × Earnings Revision (downgrades) × Risk-adjusted stats (Sharpe -0.38, Sortino -0.41 — bottom-quintile risk efficiency) dominate. Quality is genuinely good and value is neutral-to-supportive (3% yield), which prevents a Strong Sell: there is real earnings quality and a valuation floor here, but the price trend, estimate trajectory and risk ratios all point the same way.

## 4. Key Quant Risk Flags

1. **Trend/momentum breakdown** — 12-1 return -14% in an up market; no momentum support at current levels. Reversal risk cuts both ways: a beaten-down high-quality name *can* mean-revert, but there is no bottoming signal in the data.
2. **Factor crowding** — Low market correlation (0.21) means IBM is *not* hiding in index beta; any selloff in AI software names (the narrative driver) hits it directly.
3. **Volatility regime** — 54% realized vol and a 37.5% drawdown for a name with 0.71 fundamental beta = factor instability; position sizing should assume fat tails.
4. **Estimate coverage thin** — FY29/FY30 consensus rests on 2–3 analysts; the -9.7% revision is directionally consistent with July target cuts but should not be over-weighted.
5. **Regression non-significance** — Alpha of -39% is the residual of an R²=4.4% model; do not quote it as standalone evidence.

**Data caveats:** Sector ranking is approximate (top-25 mega-cap universe, no direct IT-services comps available); forward-year estimate sample sizes are small; low-vol factor is computed on a 252-day window that captures the recent drawdown, so it likely overstates the structural vol versus IBM's history.
