# Fin Risk Analyst

- Symbol: DDOG
- Elapsed: 438.7s

---
# DDOG (Datadog, Inc.) — Financial Risk Assessment

**Sector:** Technology / Software—Application (SaaS observability) · **Mkt cap:** ~$93.5B · **Net cash position**

> ⚠️ **Data caveats upfront:** (1) The reported spot price ($260.36) is inconsistent with the provided daily price series (last close $115.66, 2026‑02‑20); market cap (~$93.5B) and the price history cannot both be right. I use the **reported market cap** for valuation metrics (FCF yield) and the tool's own returns series for volatility/drawdown. (2) Peer comparison not pulled within budget — noted as gap. (3) FY2025 figures are the latest full annual period available.

---

## 1. Credit Risk Assessment — **Investment Grade (fortress balance sheet; unrated)**

Datadog carries **net cash of ~$2.94B** (cash & ST investments $4.47B vs. total debt $1.54B). Leverage is trivial in absolute terms, D/E of 0.41 is inflated by convertible debt that is fully covered by liquid assets, and there is no refinancing cliff of consequence. This is an **Investment-Grade-quality credit profile** — arguably A-/BBB+ if it carried a public rating (SaaS convertibles often go unrated). The only "weakness" is accounting optics: FY2025 operating income was slightly negative (−$44M), so an operating-income-based interest coverage reads negative — but the company is a large **net interest income** earner on its cash pile, so true debt service capacity is effectively unlimited.

---

## 2. Key Financial Risk Metrics

| Metric | Value | Read |
|---|---|---|
| Debt / Equity | 0.41x | Low; convertible notes |
| Debt / Assets | 0.23x | Low |
| **Net Debt / EBITDA** | **−15.2x (net cash $2.94B)** | Net cash — no leverage |
| Interest coverage (EBIT basis) | ~12.5x | Strong |
| Interest coverage (op-income basis, tool) | −4.0x | Negative only because GAAP op income ≈ 0; net interest income is positive |
| Current ratio | 3.38x | Fortress liquidity |
| Quick / Cash ratio | 3.38x / 2.81x | Extremely liquid |
| Working capital | $3.79B | Strong |
| **Altman Z-Score** | **2.07 (Grey)** | Understated — tool uses *book* equity for X4; using $93.5B market cap the score is far into the safe zone |
| **Piotroski F-Score** | **6 / 9 (Moderate)** | Lost pts: ROA improvement, no-dilution, gross-margin improvement |
| FCF (FY2025) | $1,000.6M | FCF margin 29.2% |
| FCF yield | 1.06% | Thin — a *valuation* signal, not a cash-generation weakness |
| Cash runway | Effectively infinite | FCF-positive; $4.5B cash |

**Trend (annual):** Revenue $2,128M → $2,684M → $3,427M (+26% → +28%). FCF $632M → $836M → $1,001M. Gross margin 80.7% → 80.8% → **79.9%** (slight compression). SBC steady at ~22% of revenue. Retained earnings finally turned positive (+$138M) in FY2025.

**Debt maturity structure:** LT debt $1.24B, ST debt $39M; cash of $4.47B covers all maturities many times over — **no refinancing risk**.

---

## 3. Market Risk Profile

| Metric | Value | Read |
|---|---|---|
| Annualised volatility (3y) | **54.4%** | Very high — typical high-beta SaaS |
| Beta vs SPY (tool) | 1.32 (profile: 1.51) | Amplifies market drawdowns |
| Max drawdown (3y) | **−48.6%** | Deep peak-to-trough pain |
| Sharpe (approx, rf=0) | 0.91 | Decent return per unit vol, but swing-heavy |

Market risk is the **dominant risk for equity holders**, not credit. The stock has repeatedly drawn down ~50% and trades on growth/multiple sentiment. A 1.3–1.5 beta means a 20% SPY drawdown plausibly produces a 30%+ DDOG decline.

---

## 4. Downside Scenario — Revenue −20%

Approximate FY2025 pro-forma (revenue ~$2,742M vs. $3,427M):

| Line | Base | −20% (cost cuts 15%) | −20% (no cuts) |
|---|---|---|---|
| Revenue | 3,427 | 2,742 | 2,742 |
| Gross profit (80%) | 2,740 | 2,191 | 2,191 |
| Opex | 2,784 | 2,366 | 2,784 |
| Operating income | −44 | **−175** | **−593** |
| EBITDA (≈ +D&A) | 194 | −119 | −537 |
| Net interest income | ~+150 | ~+150 | ~+150 |
| **FCF (SBC-addback ~$750M)** | 1,001 | **positive ~$450–600M** | **positive ~$350–500M** |

**Conclusion:** Even a severe 20% revenue shock leaves DDOG **FCF-positive** because the cost base is heavily stock-compensated (non-cash) and gross margins are ~80%. With $2.94B net cash and no meaningful debt service, **there is no solvency, covenant, or liquidity stress in this scenario** — only earnings/multiple compression. The realistic downside is equity-price, not balance-sheet.

---

## 5. Overall Financial Risk Rating

- **Credit / solvency risk: LOW** (net cash fortress, negligible leverage)
- **Liquidity risk: LOW** (current ratio 3.4x, $4.5B cash)
- **Market / equity risk: MODERATE–HIGH** (54% vol, 1.3–1.5 beta, −49% max drawdown, 1% FCF yield)

**Composite: LOW–MODERATE** — a fundamentally very safe *balance sheet* attached to a high-volatility *equity*. Survives downturns comfortably; the stock price is the volatile variable, not the business's solvency.

---

## 6. Key Red Flags

1. **Stock-based compensation = 22% of revenue ($751M).** FCF is SBC-boosted; economic dilution is real. Share count rises ~3–4%/yr — Piotroski explicitly penalises dilution (F7 = 0). GAAP FCF overstates true owner earnings by roughly the dilution drag.
2. **GAAP operating margin is negative (−1.3% in FY2025)** despite 28% revenue growth — profitability is thin at the operating line; the positive net income ($108M) is largely *interest income on the cash pile*, not operations.
3. **Gross margin compression** (80.8% → 79.9%) — worth monitoring if it persists (Piotroski F8 = 0).
4. **Very thin FCF yield (~1.1%)** — the equity embeds high growth expectations; any growth deceleration drives multiple compression (consistent with the −49% historical drawdown).
5. **Working-capital volatility** — recent quarter showed a −$152M WC drag (Q2‑2026), a reminder that reported FCF can swing.
6. **Data integrity gap** — spot price vs. market-cap inconsistency must be reconciled before quoting per-share risk metrics.

**Bottom line:** Datadog is a **low credit risk, high market risk** name. Balance-sheet stress-testing passes with wide margins under a 20% revenue decline; the risk that matters to an equity investor is valuation and volatility, not financial distress.
