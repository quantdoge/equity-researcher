# Fin Risk Analyst

- Symbol: GS
- Elapsed: 121.3s

---
I now have sufficient data to complete the assessment. The sector-peers call returned index funds (not useful comparables), and the rating search yielded no usable content — I'll flag those gaps and rely on domain knowledge for the credit rating and regulatory capital metrics.

---

# Goldman Sachs Group (GS) — Financial Risk Assessment
**Sector:** Financial Services / Capital Markets (global investment bank + G-SIB) | **Market cap:** ~$266B | **Price:** $902.56 | **Report date:** data through FY2025 (period end 2025-12-31)

**Important framework note up front:** GS is a global systemically important bank (G-SIB). Several of the standard tools (Altman Z, Piotroski F, interest coverage, FCF yield, current ratio) are calibrated for industrial companies and produce misleading readings for a regulated bank whose balance sheet is funding-driven. I flag each of these explicitly below rather than reporting them as literal signals. The binding solvency metrics for GS are regulatory capital ratios (CET1, SLR) and liquidity ratios (LCR/NSFR), which are not in the tool set — noted as data gaps.

---

## 1. Credit Risk Assessment

**Rating: Investment Grade (Strong)**

- Agency ratings (domain knowledge, not tool-verified — see gaps): **Moody's A2 / S&P A+ / Fitch A+**, all stable. Goldman Sachs International: A+/A-1 (S&P). This is high-quality investment-grade, one of the strongest in the banking universe.
- FY2025 earnings: **Net income $17.2B** (EPS $51.95), up from $8.5B in 2023 — a strong recovery cycle. Estimated **ROE ≈ 13.8%** on ~$125B book equity.
- Leverage looks extreme by industrial standards (D/E 4.88, equity/assets 7%) but is *by design* for a G-SIB dealer — the relevant metric is the regulatory capital stack, which is well above minimums (CET1 ≈ 14–15% area; SLR ≈ 5.5–6%) after a multi-year earnings retention and buyback program.
- Net cash position at headline level: cash & ST investments $624.5B vs total debt $609.5B → **net debt ≈ −$15.0B**.

## 2. Key Financial Risk Metrics Table

| Metric | Value (FY2025) | Interpretation |
|---|---|---|
| Debt / Equity | 4.88× | High, but normal for a dealer bank; equity/assets 7% is a buffer, not a defect |
| Net debt / EBITDA | −0.62× | Net cash; headline-only (bank EBITDA is not a meaningful construct) |
| Interest coverage (EBIT/interest) | 0.33× | **Not meaningful for banks** — $66.8B interest expense includes trading-book funding & deposits; binding test is net interest margin + capital ratios |
| Current ratio / Quick ratio | 0.83 / 0.83 | Below 1 by design (liability-funded); binding tests are LCR/NSFR (not available) |
| Working capital | −$208.2B | Normal for a bank; not a liquidity signal |
| Cash & ST investments | $624.5B (34.5% of assets) | Deep liquidity pool incl. client-segregated funds |
| Altman Z-Score | 0.143 → "Distress" | **Model inapplicable to banks** — uses book equity in x4 and ignores bank funding structure; disregard as a solvency signal |
| Piotroski F-Score | 5/9 (Moderate) | Understates strength: scores 0 on operating cash flow (negative, normal for banks) and leverage reduction |
| FCF yield | −16.5% (FCF −$47.2B) | **Not meaningful for banks** — cash flow swings with balance-sheet/trading activity, not cash burn |

## 3. Market Risk Profile (3-year window, vs SPY)

| Metric | Value |
|---|---|
| Annualised volatility | **32.2%** |
| Beta vs S&P 500 | **1.44** |
| Max drawdown (3Y) | **−30.9%** |
| Sharpe (0% Rf) | 1.11 |

GS is a **high-beta, high-vol equity** (beta 1.44, ~1.6× market vol). The 30.9% max drawdown reflects the 2022 bear market and the March 2023 regional-bank stress. Risk-adjusted returns over the window are constructive (Sharpe 1.11), but in a market drawdown GS typically falls 1.4–1.5× the index — tail-risk sensitive for equity holders even though the balance sheet is sound. The stock's embedded volatility is a *market* risk, not a *credit* risk.

## 4. Downside Scenario Analysis — Revenue −20%

Basis: FY2025 revenue $125.1B, operating income $21.85B, net income $17.2B, equity $125.0B. Simulating a severe downturn (20% revenue hit, e.g., markets shock + deal-flow freeze, higher credit provisions):

| Line | Base (FY2025) | Scenario (−20% rev) |
|---|---|---|
| Revenue | $125.1B | $100.1B |
| Operating income | $21.85B | $7–12B (40–60% flow-through; comp partially variable) |
| Provision for credit losses | (embedded) | +$2–4B (cyclical uptick) |
| **Net income** | **$17.2B** | **~$4–8B** |
| Implied ROE | ~13.8% | ~3.5–6.5% |
| Common equity | $125.0B | ~$125B (retained, less reduced dividends/buybacks) |
| CET1 / SLR | Well above minimums | Still above minimums; buffers absorb |

**Conclusion: no solvency threat.** Even in a severe 20% revenue shock GS remains profitable and adequately capitalized; the realistic consequences are a sharp ROE step-down, suspension of buybacks (currently $12.4B/yr), wider funding spreads, and ~40%+ equity drawdown given beta 1.4. Liquidity impact would be contained by the >$600B cash/ST book and LCR buffer — this is a *capital-returns and equity-volatility* event, not a credit event. Historical precedent: GS absorbed a 2022–2023 earnings recession (net income $21.6B → $8.5B, −61%) without capital stress.

## 5. Overall Financial Risk Rating: **Moderate**

- **Credit risk: Low.** A-rated G-SIB, net cash headline, strong capital generation, regulatory buffers comfortably above minimums.
- **Liquidity risk: Low.** Deep cash/inventory pool; standard commercial paper/repo roll ($311B short-term debt) is stress-managed via LCR regulation.
- **Market/earnings risk: High.** Beta 1.44, 32% vol, cyclical IB/global-markets revenue mix — earnings can halve in a downturn, and the equity is highly rate- and sentiment-sensitive.

Netting out: solid balance sheet, elevated equity risk. **Moderate** overall.

## 6. Key Red Flags & Data Gaps

**Red flags:**
1. **Three consecutive years of negative operating cash flow** (2023: −$12.6B; 2024: −$13.2B; 2025: −$45.2B). Largely balance-sheet-driven (asset growth/working capital), not cash-burn — but the 2025 swing (+$34B deterioration vs 2024) warrants monitoring; it coincided with the cash book contracting from $921.8B to $624.5B.
2. **Elevated absolute funding costs** — interest expense $66.8B at a 2Y yield of 4.65%/10Y 4.99% (curve normalized, no inversion). Rate-sensitive; margin compression if the Fed cuts with a floored deposit book.
3. **~$311B short-term debt (51% of total debt)** — continuous rollover dependency on CP/repo; a standard dealer-bank funding model, but a genuine stress transmission channel (as seen March 2023 for peers).
4. **Earnings cyclicality** — IB + Global Markets revenue swings (2022–2023 net income −61% peak-to-trough); consumer/private-credit legacy exposures add tail risk.
5. **Tool outputs that are artifacts, not risks:** Altman "Distress" (0.143) and FCF yield (−16.5%) must be ignored for a bank — they are structural false positives.

**Data gaps (not tool-verified):**
- Agency ratings (A2/A+/A+) and CET1/LCR/SLR ratios are from domain knowledge; web search returned no usable confirmation and the fundamentals API does not expose them. **Flagged as unverified.**
- Debt maturity schedule / refinancing cliff detail — not available.
- CDS spreads — not available.
- Peer multiples — sector-peers tool returned index funds rather than comparable banks; no valid comp set available.

**Bottom line:** GS is a strongly capitalized, investment-grade institution with low credit and liquidity risk and materially higher market/earnings risk. Equity holders should underwrite ~1.4× market beta and 30%+ drawdowns in stress; debt holders' exposure is well cushioned by ~$125B of equity and regulatory buffers.
