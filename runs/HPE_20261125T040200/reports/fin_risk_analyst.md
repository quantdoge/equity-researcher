# Fin Risk Analyst

- Symbol: HPE
- Elapsed: 97.0s

---
## HPE — Financial Risk Assessment
**Hewlett Packard Enterprise Co.** | Technology / Computer Hardware | FYE 31-Oct | Latest annual: FY2026 (period ended 2026-10-31, filed 2026-11-23) | Price $40.18, market cap ≈$53.3B

---

### 1. Credit Risk Assessment — **INVESTMENT GRADE (low-BBB tier, stable)**

| Agency | Rating | Outlook |
|---|---|---|
| S&P | BBB | Stable |
| Moody's | Baa2 senior unsecured | Stable |
| Fitch | BBB+ / F2 short-term | Stable |

Leverage is genuinely investment-grade on a flow basis: net debt/EBITDA **1.54x**, debt/assets **0.21**, debt/equity **0.68**, and EBITDA of $8.36B covers $18.65B of gross debt comfortably. Headline interest coverage of **20.4x** (EBIT $4.90B / interest $224M) looks fortress-like — but see the red flag on that number below; I do not accept it at face value.

The **Altman Z-Score of 1.011 ("Distress Zone")** is the main contradiction. I view it as structurally distorted rather than predictive here: X2 (retained earnings/assets) is 0.0023 because HPE has run a negative accumulated-earnings position for years via buybacks (FY2025 retained earnings −$2.81B, FY2026 only +$0.20B), and X4 uses *book* equity ($27.6B) rather than the $53.3B market value. Substituting market cap lifts X4 from 0.45 to 0.88 and pulls Z toward the ~1.3–1.4 area — still grey/distress, still a warning about thin book cushion relative to $60.9B of liabilities, but not a bankruptcy signal for a company generating $3.9B of FCF. **Piotroski F-Score 7/9** (moderate-strong) is the better read on momentum; the two misses are exactly leverage increase (F5) and dilution (F7, diluted shares +9% YoY — Juniper consideration), both one-off deal artifacts.

**Verdict:** the balance sheet can survive a prolonged downturn, but the cushion is thinner than the rating implies, and it is a *flow* cushion (cash generation), not a *stock* cushion (equity/assets 0.31).

---

### 2. Key Financial Risk Metrics

| Metric | FY2026 | FY2025 | FY2024 | Assessment |
|---|---|---|---|---|
| Revenue | $46.74B | $34.30B | $30.07B | +36% YoY, largely inorganic |
| Gross margin | 37.8% | 28.8% | 31.8% | Strong recovery |
| Operating margin | 9.76% | 4.79% | 8.10% | Volatile |
| EBITDA | $8.36B | $2.63B | $5.56B | |
| **Net debt / EBITDA** | **1.54x** | 6.97x | 0.89x | IG-consistent now |
| **Debt / equity** | **0.68x** | 0.97x | 0.80x | Improving |
| Debt / assets | 0.21x | 0.32x | 0.28x | |
| **Interest coverage (reported)** | **20.4x** | negative (EBIT −$110M) | 25.6x | *See caveat* |
| Interest expense | $224M | $175M | $117M | +28% / +91% over 2 yrs |
| Current ratio | **1.05x** | 1.01x | 1.29x | Thin |
| Quick ratio | **0.66x** | 0.76x | 0.95x | Weak |
| Cash ratio | 0.16x | 0.23x | 0.57x | Declining |
| Working capital | $1.81B | $0.35B | $7.48B | Collapsed vs FY24 |
| Cash & ST inv. | $5.75B | $5.77B | $14.85B | |
| **Altman Z** | **1.01 — Distress** | — | — | Artifact-adjusted ~1.3–1.4 |
| **Piotroski F** | **7 / 9** | — | — | Moderate-strong |
| Goodwill + intangibles | **$29.21B** | $30.14B | $18.60B | 106% of equity, 33% of assets |
| FCF | $3.86B | $0.63B | $1.97B | |
| **FCF yield** | **6.65%** | — | — | (7.2% on $53.3B mcap) |
| FCF margin | 8.3% | 1.8% | 6.6% | Improving |

**Debt structure / refinancing:** $3.65B current portion (19.6% of $18.65B) + $15.0B long-term. Known notes include $900M 4.05% due Sep-2027, $300M FRN due Sep-2028, $1.75B 4.55% due Oct-2029, plus new 2028–2033 senior unsecured issued at 4.50%/4.60%/5.25%. The $3.65B near-term wall is coverable ~1.6x by cash alone — no refinancing cliff. *Full maturity ladder by year was not retrievable (10-K PDF not parsed); flagged as a data gap.*

**Rate backdrop (as of 2026-11-25):** 2Y 4.74%, 5Y 4.93%, 10Y 5.13%, 30Y 5.47%, 2s10s **+39bp (not inverted)**. Curve is steep and rates are high — every refinancing reprices upward, which is why interest expense has compounded +91% in two years.

---

### 3. Market Risk Profile

| Metric | Value | Read |
|---|---|---|
| Annualised volatility (3y, 756d) | **55.9%** | Very high for hardware (~2x large-cap tech) |
| Beta vs SPY (computed) | **1.88** | Amplifies market drawdowns ~2x |
| Beta (reported, company profile) | 1.47 | Discrepancy flagged |
| Max drawdown (3y) | **−48.3%** | Halved at worst point |
| Sharpe (0% rf) | 0.88 | Adequate return/vol; but rf≈4.7% means **excess-return Sharpe is near zero** |

This is the weakest part of the profile. A 55.9% vol / 1.88 beta combination means HPE trades like a cyclical rather than a stable IG hardware name — consistent with AI-server order lumpiness and the Juniper integration. With the 2Y risk-free rate at 4.74%, a 0.88 Sharpe on a 0% risk-free assumption implies roughly **flat risk-adjusted excess return over the trailing three years**. Sortino/non-annualised tail statistics were not available from the toolset.

---

### 4. Downside Scenario Analysis — Revenue −20%

Base FY2026: EBITDA $8.36B, EBIT $4.90B, FCF $3.86B, net debt $12.89B.

| | **Base** | **Downside (−20% rev, GM held)** | **Severe (−20% rev, GM→34%)** |
|---|---|---|---|
| Revenue | $46.74B | $37.39B | $37.39B |
| Gross profit | $17.67B | $14.13B | $12.71B |
| Opex actions | — | −$1.2B | −$1.2B |
| EBITDA | $8.36B | ~$5.69B | ~$3.87B |
| **Net debt/EBITDA** | **1.54x** | **~2.27x** | **~3.33x** |
| Interest coverage (reported 224M) | 20.4x | ~10x | ~1.8x |
| Interest coverage (gross ~2x basis) | ~10x | ~5x | **<1x — breach risk** |
| FCF | $3.86B | ~$2.0B | **~$0.2–0.5B** |
| Dividend ($873M) covered? | 4.4x | ~2.3x | **Marginal / at risk** |
| Goodwill −20% write-down → equity | $27.6B | $21.8B | $21.8B (equity/assets → 0.26) |

**Read:** a 20% revenue shock is *survivable* — leverage stays under 2.3x, FCF stays positive, and the dividend is still covered. It is the **severe** case (volume loss *plus* margin compression, i.e. an AI-server pricing war) that matters: leverage ~3.3x, coverage below 1x on a gross basis, goodwill impairment pushing equity down ~21%, and a live downgrade path from BBB toward BBB−/Ba1. Critically, **FY2025 already showed this movie**: EBIT of −$110M, net income $57M, FCF of just $627M — the trough is demonstrated, not hypothetical. The difference is that FY2026's buffer is thinner on liquidity (quick ratio 0.66 vs 0.95 in FY2024).

---

### 5. Overall Financial Risk Rating: **MODERATE**

Supported by IG ratings across all three agencies with stable outlooks, 1.54x net leverage, $3.86B FCF, 6.65–7.2% FCF yield, and a 7/9 F-score. Constrained by thin liquidity, goodwill-heavy equity, high market risk, and proven trough-level margin fragility. It is not High only because cash generation and the absence of a refinancing cliff give real time to adjust.

---

### 6. Key Red Flags

1. **Interest coverage is overstated.** $224M interest on $18.65B of debt implies a ~1.2% effective rate — implausible in a 4.7–5.5% market. This almost certainly nets captive-finance interest income (HPE Financial Services). Gross coverage is more likely **5–10x**, not 20x. Treat 20.4x as a ceiling, not a base case.
2. **Goodwill = 106% of equity.** $29.2B of goodwill/intangibles (up from $18.6B pre-Juniper) means book equity is largely acquisition accounting. A 20% write-down erases 21% of equity; a 40% write-down erases 42%. This is the single largest asset-side risk and the direct cause of the Z-score distress reading.
3. **Liquidity is thin for the size of the book.** Current ratio 1.05, quick 0.66, cash ratio 0.16, working capital down from $7.48B (FY24) to $1.81B. Current liabilities of $36.0B sit against $37.8B of current assets.
4. **Inventory +122% YoY** ($6.35B → $14.09B) — either AI-server pre-build or channel stuffing; if demand slips, this is a writedown and cash-burn vector.
5. **Working capital consumed $2.30B of cash** in FY2026 (vs $0.69B in FY24) — FCF quality depends on reversing this.
6. **Growth is inorganic; organic growth unproven.** Revenue +36% with diluted shares +9% and debt-funded goodwill — integration and cross-sell risk sits on top of an already cyclical base.
7. **Shareholder returns exceed comfortable limits in a downturn:** $0.87B dividends + $1.24B buyback = $2.11B, 55% of FCF, and leverage rose in FY2026 despite record FCF.
8. **Market risk is high:** 55.9% vol, beta 1.88, −48.3% max drawdown, and a Sharpe of 0.88 that is roughly zero on an excess-return basis at current rates.

**Data gaps flagged:** (a) debt maturity ladder by year — 10-K not parseable; (b) rating agency rationale pages returned 403/empty, so covenant specifics and agency-adjusted leverage thresholds are unavailable; (c) Sortino and peer-multiple comparison not computed; (d) beta conflict (1.47 profile vs 1.88 computed) unresolved; (e) market-cap inconsistency between `calculate_fcf_yield` ($58.07B) and company profile ($53.34B) — I used the profile figure and show both yields.
