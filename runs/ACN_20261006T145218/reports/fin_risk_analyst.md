# Fin Risk Analyst

- Symbol: ACN
- Elapsed: 165.4s

---
# Financial Risk Assessment — ACN (Accenture plc)

**Data basis:** FY2023–FY2026 annual financials (FYE 31-Aug), trailing-1Y price history (252d), 3Y daily prices, yield curve as of 2026-10-06. All balance-sheet metrics as of FY2026-08-31. Market cap ≈ $119B, price ≈ $194.89.

---

## 1. Credit Risk Assessment: **Investment Grade**

Accenture carries a fortress balance sheet. Net debt of just $0.56B against $14.0B EBITDA (net debt/EBITDA **0.04x**) means the company is effectively unlevered on a net basis; cash ($12.8B) alone exceeds total debt ($13.4B). Sources of debt are modest: $0.9B short-term, $10.0B long-term, interest expense $303M.

- The Altman Z of **2.18 ("grey zone") is a model artifact, not a distress signal**: the x4 component uses *book* equity ($33.3B), which severely under-weights an asset-light, high-market-cap services firm (market cap ≈ $119B). A market-value-based Z would sit deep in the safe zone. Flag: treat Z as indicative only.
- Piotroski F-score **6/9 (moderate)**: profitability and accruals quality good; deductions on ROA improvement, rising leverage, and slower asset turnover.

## 2. Key Financial Risk Metrics (FY2026, 8/31/2026)

| Metric | Value | Signal |
|---|---|---|
| Debt/Equity | 0.40x (0.25x FY24 → 0.40x FY26) | Low, but **rising** |
| Net debt/EBITDA | 0.04x | Minimal leverage |
| Interest coverage (EBIT/interest) | **37.6x** | Very strong debt service |
| Current / Quick ratio | 1.43 / 1.43 | Adequate liquidity |
| Cash ratio | 0.58 | Adequate |
| Equity / Assets | 45% | Strong solvency |
| Cash (FYE) | $12.8B | ≈ total debt ($13.4B) |
| Altman Z | 2.18 (grey) | Artifact — see above |
| Piotroski F | 6/9 | Moderate |

## 3. Market Risk Profile — **this is the dominant risk**

| Metric | Value |
|---|---|
| Annualized volatility (252d) | **53.0%** (historically ~15–20% for ACN — regime change) |
| Beta vs SPY (in-sample) | 0.126 — *unreliable*; profile-reported beta 1.10. Data conflict flagged |
| Max drawdown (trailing 1Y, tool) | **−56.5%** |
| Max drawdown (3Y peak-to-trough, price data) | **≈ −68%** ($382 Feb-2025 → $120 Jun-2026) |
| Sharpe (0% rf, trailing 1Y) | **−0.48** |

The price tape shows an acute idiosyncratic shock: a ~23% **single-day gap-down on 2026-06-18** (41.7M shares — 18x normal volume) and a ~50% drawdown in ~6 weeks (mid-June to late-June 2026), consistent with an AI-displacement repricing of IT services. The stock has partially recovered off the ~$120 low but is ~48% below its Feb-2025 high. Downside correlation with the market is low (stock was punished while equity/beta data diverged) — idiosyncratic, not systemic, risk.

## 4. Downside Scenario — Revenue −20% (stress test)

Model: COGS 68% variable, SGA ~80% variable, D&A/capex fixed; interest unchanged.

| Metric | Base FY26 | Stressed (−20% rev) |
|---|---|---|
| Revenue | $74.2B | $59.3B |
| EBIT | $11.7B (15.7% margin) | ≈ $7.1B (~12% margin) |
| Interest coverage | 37.6x | ≈ **23x** |
| Est. net income | $8.4B | ≈ $5.4B |
| Est. FCF | $11.6B (9.7% yield) | ≈ **$7B, still positive** |
| Altman Z (indicative) | 2.18 | ≈ 2.1 — still grey, not distress |
| Cash buffer | $12.8B | Intact (company is a net cash generator) |

**Conclusion: ACN survives a severe demand recession without covenant or solvency stress.** Leverage is so low that even a −30% revenue shock keeps coverage >10x and FCF positive. The real-world lever would be workforce cost reduction (labor ≈ 68% of revenue). Liquidity contagion risk is limited: no inventory, receivables-heavy, $9.5B working capital.

**Macro context:** Yield curve (10/6/26): 2Y 4.65% / 10Y 4.99% / 30Y 5.37%; 2s10s +34bp, **no inversion**. Refinancing the ~$10B LT debt at ~5% would cost ≈ $500M/year — absorbable (coverage ≈ 23x even stressed). No refinancing cliff identifiable from available data.

## 5. Overall Financial Risk Rating: **Moderate**

- Credit risk: **Low** (investment-grade balance sheet by every leverage, coverage, and solvency metric)
- Liquidity risk: **Low** (1.43 current ratio; cash > total debt; positive, improving FCF)
- Market risk: **High** (−57% 1Y drawdown, 53% vol, negative Sharpe, −68% peak-to-trough)
- The blend is Moderate: the company is thoroughly solvent, but the equity carries a severe, idiosyncratic downside narrative (AI disruption of IT services) that has already been repriced — and that is the risk to size.

## 6. Key Red Flags

1. **Equity de-rating event (top flag):** Vertical collapse in June 2026 (−23% single day, ~50% in six weeks). Legitimate thesis risk for a labor-intensive services model; the market has already haircut the stock nearly in half.
2. **Leverage direction:** total debt $4.1B → $13.4B (FY24→FY26) and D/E 0.25 → 0.40; interest expense up 5x ($59M → $303M). Still tiny in absolute terms, but the direction warrants monitoring.
3. **Payout ≈ 99% of FCF:** $11.5B distributions (dividends $4.0B + buybacks $7.5B) vs $11.6B FCF in FY26. Nowhere near distress, but leaves no natural buffer if FCF stalls — buybacks would have to absorb the cut first (they are flexible).
4. **F-score deductions:** ROA and asset turnover deteriorating slightly; F-score slipped on leverage+ROA tests — mild operational efficiency erosion.
5. **Beta/vol data conflict:** tool beta vs SPY (0.13) contradicts profile beta (1.10) — beta is unstable post-shock; do not rely on it for beta-hedging.
6. **Z-score grey zone** is a book-equity artifact — do not misinterpret as distress.

**Data gaps (explicit):** No credit rating/CDS spread data from tools; no debt-maturity schedule available (ST debt only $0.9B, so near-term refinancing exposure is small); no peer-multiple comparison pulled; quarterly trend not examined. None of these gaps changes the overall Moderate conclusion.
