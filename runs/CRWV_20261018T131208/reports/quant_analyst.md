# Quant Analyst

- Symbol: CRWV
- Elapsed: 58.8s

---
# CRWV — Quantitative Factor Analysis

**CoreWeave, Inc. (NASDAQ: CRWV)** | Sector: Technology / Software-Infrastructure (AI cloud compute) | Price: $61.39 | Mkt Cap: ~$26.7B | IPO: 2025-03-28

> ⚠️ **Critical data caveat:** CRWV has traded only since 2025-03-28. All risk statistics below are computed on a **~10-month (~200 trading day) sample**, not a full 252-day year. This is far below the ~3–5 years typically required for stable Sharpe/beta/alpha estimates. **Treat every price statistic as indicative, not statistically significant.**

---

## 1. Factor Scores Table

| Factor | Score | Sector Rank | Signal |
|--------|-------|-------------|--------|
| **Value** | P/E −21.9 (lossmaking), P/B 8.0, EV/EBITDA 21.3, P/FCF −3.7 | Bottom quintile | **Negative** |
| **Momentum** | 12-1 return −9.3% | Bottom quintile | **Negative** |
| **Quality** | ROE −35.0%, GP/Assets 7.5%, Accruals −8.6% (good), F-Score 5/9 | Lower-third | **Weak / Negative** |
| **Low Vol** | Ann. vol 97.7%, beta 3.48 vs SPY, max DD 55.9% | Bottom quintile | **Strongly Negative** |
| **Earnings Revision** | Consensus EPS revised +135.7% (but 2030 period, 6 analysts) | N/A (long-dated) | **Positive (low confidence)** |

**Factor detail:**
- **Value:** Negative earnings and negative FCF make P/E and P/FCF non-comparable. P/B of 8.0x on a $7.67 book value is rich for a capital-intensive hardware-heavy model. EV/EBITDA 21.3x is defensible for hypergrowth but not "cheap." No dividend.
- **Quality:** Trailing ROE of −35% and ROA −2.4% reflect the loss-making, debt-financed GPU buildout. The one genuine bright spot is **accruals ratio −0.086** (negative accruals = cash earnings exceed accounting earnings → high earnings quality, corroborated by $3.06B operating CF vs −$1.17B net income). Piotroski F-Score of **5 (Moderate)** — passes operating cash flow, accruals, leverage reduction, equity change; fails on ROA, dilution, margin, and asset-turnover improvement.
- **Low Vol:** The single worst reading in the factor set — ~98% annualized volatility and a beta of 3.48 (profile lists 7.32 on a longer basis) against SPY. This is a high-octane, high-beta AI-infrastructure name by construction.
- **Earnings Revision:** The +135.7% revision is **not** a clean near-term upgrade signal. The forward period flagged is **FY2030** (consensus $16.87 vs $7.16 prior), covered by only **6 analysts** and with a −$1.61 to +$2.72 range on FY2028. Directionally bullish on the multi-year AI ramp, but the wide dispersion and long horizon make this a weak, low-confidence input.

---

## 2. Price Statistics

| Metric | Value | Note |
|--------|-------|------|
| **Alpha (ann., vs SPY)** | **−38.0%** | Severe underperformance risk-adjusted; R² only 0.22 |
| **Beta (vs SPY)** | **3.50** | Extremely high systematic sensitivity |
| **R²** | 0.221 | Low — beta poorly explains CRWV returns; high idiosyncratic risk |
| **Sharpe ratio** | **−0.13** | Negative risk-adjusted return |
| **Sortino ratio** | **−0.232** | Downside deviation exceeds returns |
| **Annualized return** | −12.67% | Net negative since IPO window |
| **Annualized volatility** | 97.3% | ~4x the market |
| **Max drawdown** | −55.9% | Peak (post-IPO ~$187) to trough (~$69) |
| **Correlation vs peers (180d)** | ORCL 0.61, SPY 0.49, NVDA 0.47, AMD 0.46, MSFT 0.28 | Highest co-movement with cloud-infra (ORCL), not megacap software |

> Minor inconsistency flagged: the volatility module printed an approximate Sharpe of +0.12 while the dedicated Sharpe/Sortino tool returned −0.13. The dedicated tool is used above; the divergence stems from return-basis/window differences and further underscores the instability of metrics on a 10-month sample.

---

## 3. Composite Quant Signal

### **SELL** (low conviction — see qualifiers)

**Rationale:** Four of five factors score negative — bottom-quintile on value, momentum, quality, and low-vol, with only a low-confidence, long-dated positive earnings-revision reading. The risk-adjusted return picture is unambiguous for the period measured: negative Sharpe, negative Sortino, −38% alpha, and a −56% max drawdown at ~98% volatility.

**Important qualifier — the numbers win, but read them in context:** CRWV is a 10-month-old IPO in a capex-heavy, deliberately loss-making AI buildout phase. Traditional value/quality/low-vol factors are structurally biased against *any* early-stage infrastructure buildout (negative FCF, high leverage, no trailing earnings). The composite **Sell** is a faithful reading of the factor data, but it is a statement about *factor-timing risk and drawdown risk*, not a prediction that the AI-infrastructure thesis fails. The positive operating cash flow ($3.06B) against negative net income is a genuine quality offset that a pure factor screen understates.

---

## 4. Key Quant Risk Flags

1. **Small-sample invalidity (primary):** All alpha/beta/Sharpe/Sortino/vol figures rest on ~200 trading days. Beta confidence intervals and Sharpe significance are effectively non-computable at this horizon — the −38% alpha could largely be noise. **Do not size positions off these risk metrics alone.**
2. **Momentum reversal / crash risk:** −9.3% 12-1 momentum combined with 98% vol and a −56% drawdown places CRWV in the high-beta "crash-prone" bucket; further drawdowns of the same magnitude are historically plausible.
3. **Low R² (0.22) / high idiosyncratic risk:** Beta of 3.5 explains <25% of return variance — single-name news (customer concentration, GPU financing, debt) dominates, making hedging with index shorts unreliable.
4. **Factor crowding / AI-theme correlation:** 0.61 correlation to ORCL and ~0.47 to NVDA/AMD → CRWV is effectively a leveraged proxy on the AI-capex trade. It offers little diversification within a tech book and will amplify a sector de-rating.
5. **Dilution & leverage:** F-Score fails on "no dilution" (shares 218M → 435M YoY) and the company carries ~$52.5B enterprise value vs $26.7B market cap — $1.23B annual interest expense on thin EBIT ($14M). Refinancing/rate sensitivity is a material idiosyncratic risk.
6. **Liquidity:** Adequate — $26.7B cap with tens of millions of daily shares traded; not a liquidity concern.

---

**Data gaps:** Precise sector-percentile z-scores require cross-sectional ranking against a defined AI-infrastructure peer set; the available peer group is dominated by profitable mega-caps (NVDA, MSFT, ORCL) that are not factor-comparable to a loss-making neocloud. Ranks above are directional within Technology. Analyst rating fields returned null; price targets (median ~$139, range $88–$250) imply substantial upside but carry wide dispersion consistent with high estimate uncertainty.
