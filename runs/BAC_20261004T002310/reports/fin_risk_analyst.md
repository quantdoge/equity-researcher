# Fin Risk Analyst

- Symbol: BAC
- Elapsed: 32.0s

---
# Financial Risk Assessment — Bank of America Corporation (BAC)

**Sector:** Financial Services / Diversified Banking (US G-SIB) | **Price:** $53.75 | **Mkt Cap:** ~$381B | **FY2025 NI:** $30.5B | As of FY2025 / H1-2026 filings

> **Methodological caveat up front:** BAC is a deposit-funded bank. Corporate-calibrated tools (Altman Z, current ratio, interest-coverage, net-debt/EBITDA) are systematically misleading for banks — a healthy bank *always* shows current ratio < 1, negative net debt-to-EBITDA (huge cash holdings) and low Z-scores because of its liability structure. I flag these rather than treat them as distress signals, and overlay bank-appropriate capital signals (CET1, deposit funding, earnings trajectory).

---

## 1. Credit Risk Assessment — **Investment Grade**

- **Capital is the binding credit metric for a bank, and it is strong:** CET1 ratio ~**11.2% (Standardized)** as of 1Q26 (~$200B CET1), comfortably above the 5.5–6% regulatory minimums and giving CCAR-grade shock absorption. CET1 barely moved (-$1.7B in 1Q26) despite buybacks — capital generation is outpacing distribution.
- **Earnings power is intact and improving:** FY2025 net income $30.5B (EPS $3.88, +19% YoY on $27.1B/2024); H1-2026 momentum is positive ($17.7B in 1H26 vs $15.8B in 1H25) on revenue growth ($97.3B in 1H26). ROE ≈ 10% (30.5/303 book equity).
- **Leverage read in bank terms is benign:** total debt $366B vs $964B cash & short-term instruments; book equity $303B; D/A only 0.11. The corporate "interest coverage 0.48" and "net debt/EBITDA −14.9" are artifacts of deposit funding (FY25 interest expense $78.5B is largely deposit cost, not debt-service stress).
- External ratings (Moody's/S&P/Fitch standalone, typically single-A-high/AA- for BofA) and CDS spreads were **not retrievable** — flagged as a gap, but nothing in fundamentals contradicts investment-grade status.

## 2. Key Financial Risk Metrics

| Metric | FY2025 | Reading |
|---|---|---|
| Debt / Equity | 1.21× | Fine for a bank (incl. deposits-guaranteed debt) |
| Net Debt / EBITDA | −14.9× | Artifact (huge cash); ignore for banks |
| Interest Coverage (EBIT/Int) | 0.48× | **Not applicable** (deposit cost, not debt service) |
| Debt / Assets | 11% | Low |
| CET1 ratio | ~11.2% (std'd) | Strong vs 5.5–6% minimum |
| Current / Quick ratio | 0.42 / 0.42 | Normal for deposit-funded bank, not a red flag |
| Cash / Liabilities | 0.31 | ~$964B liquidity pool > $311B total equity |
| Altman Z-Score | −0.27 (Distress) | **Model misapplication to banks — disregard** |
| Piotroski F-Score | 6/9 (Moderate) | Reasonable; failed on leverage & accrual quality |
| FCF Yield | 3.11% | Modest but positive |
| Payout (FY25) | $9.6B div + $24.1B buyback | $33.7B total, funded from earnings |

## 3. Market Risk Profile

| Metric | Value | Comment |
|---|---|---|
| Annualised Volatility (252d) | 22.7% | Moderate; typical large-cap bank |
| Beta vs SPY (252d) | 0.71 (provider: 1.16) | Below-market sensitivity; provider beta higher — use range 0.7–1.2 |
| Max Drawdown (252d window) | −17.9% | Contained; G-SIB bounce-back capacity |
| Sharpe (approx, 0% Rf) | −0.05 | Flat risk-adjusted return over window |
| Yield curve context | 2Y 4.65% / 10Y 4.99%, spread **+34bp, not inverted** | No inversion signal; 5%+ rates = NIM pressure but no curve stress |

3-year max drawdown and Sortino were not computable from available tool windows (data gap).

## 4. Downside Scenario — Revenue −20% ($38.3B off FY25 base)

| Line | Base FY25 | Stress (−20% rev) |
|---|---|---|
| Revenue | $191.6B | $153.2B |
| Est. Net Income | $30.5B | ~$7–10B (partial cost flexibility; higher credit costs) |
| ROE | ~10% | ~2.5–3.3% — positive, not loss-making |
| CET1 ratio | ~11.2% | Stays well above 5.5% minimum (stress consumed by retained earnings + modest capital actions) |

**Verdict:** A 20% revenue shock is absorbable. BAC survives a severe downturn through CET1 buffer and deposit franchise; credit cost would be the swing factor, not funding. A 2008-type event (the true existential scenario for a G-SIB) is beyond this haircut test and is mitigated by the post-2008 resolution/CCAR regime rather than ratio headroom.

## 5. Overall Financial Risk Rating: **Moderate**

**Credit risk: Low (Investment Grade).** **Market/liquidity risk: Moderate.** The binding risks are market- and rate-side (beta up to ~1.2, 22.7% vol, Sharpe ≈ 0, funding-cost sensitivity), not solvency. For an equity holder, BAC is a low-tail-risk, moderate-return investment; for a creditor, it is investment grade.

## 6. Key Red Flags

1. **Metric-model misfit (read-through risk):** Z-score "Distress," current ratio 0.42 and 0.48× interest coverage are tool artifacts for a bank — a naive reader would badly misprice this name. Treat only CET1, NIM and charge-off data as bank-credit truth.
2. **Rate/NIM compression:** interest expense ($78.5B FY25) is the largest P&L line; any 5%+ / steeper curve environment squeezes NIM, and 26% of liabilities are rate-sensitive wholesale. Not an insolvency risk — an EPS headwind.
3. **Lumpy bank "FCF":** Operating CF swung $44.8B (2023) → −$8.8B (2024) → +$12.6B (2025) with a −$33B working-capital swing; FCF yield 3.1%. For banks this is deposit/loan flow noise, but it makes headline FCF metrics untrustworthy quarter-to-quarter.
4. **Aggressive capital return:** $33.7B returned in FY25 (buybacks 2.7× dividends); CET1 fell slightly in 1Q26. Sustainable today — a first candidate for cutback under stress.
5. **Data gaps:** external credit rating/CDS, LCR/NSFR, debt-maturity schedule, and bank peer multiples (peer tool returned index funds) were unavailable — quality-check before relying on this note alone for rating decisions.

*Assessment basis: FY2021–FY2025 annual + 1H26 quarterly filings, CET1 disclosures (1Q26), and 252-day market data. All dollar figures USD.*
