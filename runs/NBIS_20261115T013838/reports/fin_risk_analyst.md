# Fin Risk Analyst

- Symbol: NBIS
- Elapsed: 53.2s

---
## NBIS — Nebius Group N.V. | Financial Risk Assessment
*Data as of Q3 2026 (quarter ended 2026-09-30). Price $115.88.*

---

### 1. Credit Risk Assessment — **Sub-Investment Grade (CCC-equivalent profile)**

| Signal | Reading |
|---|---|
| Unsecured, **unrated** convertible stack | No agency rating found; CDS unavailable (**data gap**) |
| Trailing net debt / EBITDA (operating) | **13.9x** |
| Reported net debt/EBITDA (2.63x) | **Not a valid leverage measure** — see below |
| Interest coverage (op. EBIT basis) | **−1.6x** TTM; **−9.95x** on FY25 (tool) |
| Altman Z (Q3'26, book equity) | **0.83 — Distress** |

**The single most important correction to the headline data:** the source EBITDA of $493.2M for FY25 does not reconcile to operating income + D&A (−$611.7M + $417.9M = **−$193.8M**). The reported figure only reconciles if ~$687M of **non-operating gains** are included. FY25 net income was **+$82.5M against operating income of −$611.7M**; Q1'26 net income of +$621.2M came with operating income of −$128.0M. **Profitability is revaluation-driven, not operating.** The tool's 2.63x net-debt/EBITDA and the 8/9 Piotroski F-score both inherit this distortion. On genuine operating EBITDA, TTM leverage is **13.9x**.

**Mitigants that keep this out of outright "Distress":**
- **No refinancing cliff.** Earliest maturity is **Jun 2029 ($588M)**. Ladder: $1.8B Sep-2030, $3.1B Mar-2031, $613M Jun-2031, $1.8B Sep-2032, $2.1B Mar-2033, plus ~$5.75B Aug-2026 notes (2030/2034) and a $775M secured GPU facility (SOFR+250, Jul-2026). Short-term debt is only **$187.5M**.
- Cash interest is subsidised (1.00%–4.50% coupons), but notes **accrete to 110%–125%**, so the true economic cost is ~4%–6%, not the coupon.
- **Every convertible is out of the money.** Conversion prices run ~$138.75–$183.22 (2029–2033) and ~$313/$325 (2026 vintage) versus a $115.88 spot. The convert structure has stopped being latent equity and is now **debt that must be repaid or refinanced in cash**.

---

### 2. Key Financial Risk Metrics

| Metric | Value | Source/Note |
|---|---|---|
| Revenue (TTM) | $2,189.8M | Q4'25–Q3'26; Q3 alone $980.8M |
| Revenue growth | ~4.1x YoY (FY25 $529.8M → Q3 run-rate $3.92B) | — |
| Operating income (TTM) | **−$503.5M** | Q3'26 first positive quarter (+$50.4M) |
| Adj. EBITDA (TTM, op. basis) | **$612.9M** | constructed: op. inc. + D&A $1,116.4M |
| EBITDA run-rate (Q3'26 ×4) | ~$1,883M | implies 4.5x net lev. *if sustained* |
| Total debt | **$15,959.6M** | vs. ST+LT $14,189M → **~$1.77B unexplained (leases?)** |
| Cash & ST investments | $7,425.6M | — |
| Net debt | $8,534M | 0.5x equity |
| Net debt / EBITDA | **13.9x TTM** / 4.5x Q3 run-rate | ranges 3x–14x depending on denominator |
| EBITDA / interest | **1.96x** (TTM: $612.9M / $313.2M) | interest expense up 4.9x YoY |
| Debt / equity | 1.08x (FY25) → **1.30x** (Q3'26) | trend deteriorating |
| Debt / assets | 40% → **41.2%** | — |
| Current ratio | **5.31x** (Q3'26) | cash ratio 3.0x |
| Working capital | **$10,680M** | — |
| Altman Z | 0.83 book / **1.37 market-cap basis** | both <1.81 |
| Piotroski F | 8/9 *reported* — **not credit-credible** (F1/F3 driven by non-op. gains; F5 = 0) | — |
| FCF (TTM) | **−$12,421M** | OCF +$5,065M − capex $17,487M |
| FCF yield | **−44.7%** (tool: −12.83% on stale FY25 FCF) | — |
| Capex (Q3'26 alone) | **$7,300M** | 2026 guidance raised to **~$27B** |

**Model caveat:** Altman Z was not built for a pre-scale, asset-heavy GPU infrastructure company — X5 (asset turnover) is only 0.057 and mechanically crushes the score. I flag it because it is directionally consistent with the leverage and coverage data, not because 0.83 is a literal bankruptcy probability.

---

### 3. Market Risk Profile

| Metric | Value | Interpretation |
|---|---|---|
| Annualised volatility (756d) | **114.6%** | daily 1σ ≈ 7.2%; **99% 1-day VaR ≈ 16.8%** |
| Beta vs SPY | **2.93x** (tool) vs 1.56 (profile) | use 2.93 — two independent sources disagree (**gap**) |
| Max drawdown (3y) | **−59.6%** | equity down despite debt +3.2x |
| Sharpe ratio | 1.31 | backward-looking, flattered by the 2025 melt-up |
| Sortino | not available | **data gap** |

Vol of 114.6% with a 2.93 beta means a garden-variety market drawdown becomes an equity impairment event, which in turn closes the capital-markets window the funding model depends on. **That correlation is the core market risk, not price volatility per se.**

---

### 4. Downside Scenario: Revenue −20%

Base (Q3'26 ×4): revenue $3,920M, gross margin 41.4%, but note **D&A $1,681M annualised sits inside cost of revenue** — cash gross margin is ~84%. Contribution margin is therefore very high and depreciation is fixed.

| | Base (run-rate) | Revenue −20% |
|---|---|---|
| Revenue | $3,920M | $3,136M |
| EBITDA | $1,883M | **~$1,224M** |
| Interest expense | ~$450–600M | ~$450–600M |
| EBITDA / interest | ~3.1–4.2x | **~2.0–2.7x** |
| Net debt / EBITDA | 4.5x | **7.0x** |
| FCF | ≈ −$14B (at $27B capex) | ≈ **−$15B** |
| Cash runway | ~1.3 quarters | **~1 quarter** |

**If they cut capex** to defend liquidity, FCF improves sharply but they breach capacity-delivery obligations and forfeit prepayments — the mechanism that currently funds >100% of Q3 capex. **If they hold capex**, they must raise equity at $115.88 (already ~60% below peak) into a 114%-vol tape — i.e., a heavily dilutive rescue. Short-term debt is negligible, so this is a **liquidity-and-dilution event, not a 2026 default event**.

---

### 5. Overall Financial Risk Rating: **HIGH**

*(Not Critical: no near-term maturity wall, $7.4B cash, $38.7B RPO, and prepayments covering >100% of associated capex. Not Moderate: negative operating profitability, 13.9x trailing leverage, −$12.4B TTM FCF, 70% customer concentration.)*

---

### 6. Key Red Flags

1. **Earnings quality / non-operating profits.** Operating income −$611.7M (FY25) and −$503.5M (TTM) against positive net income. Z-score x3, EBITDA, and F-score are all contaminated. Any model taking the $493.2M EBITDA at face value overstates solvency by ~$690M.
2. **Receivables explosion.** Q3'26 receivables **$4,202M vs $288.6M in Q2** (DSO 45 → **128 days**), with **one customer holding 75% of receivables (~$3.1B)**. Single-counterparty collection risk of ~11% of total assets, unexplained in the reported data.
3. **Customer concentration: 33% / 22% / 15% — three unnamed customers = ~70% of Q3 revenue.**
4. **Cash flow flattered by prepayments.** Q1'26 OCF of +$2,258M included a +$2,121M working-capital inflow; Q2 OCF was a near-identical +$2,246M. Prepaid contract liabilities are an **obligation to deliver capacity**, not free cash. Q1 and Q2 OCF values are suspiciously identical — possible feed duplication.
5. **Converts are all OTM** ($138.75–$183.22 vs $115.88 spot): refinancing risk has replaced dilution risk, and conversion is unavailable as a de-leveraging mechanism.
6. **Unsecured debt structure against rapidly depreciating collateral.** Only the $775M GPU facility is secured; everything else sits on GPU/DC assets with a multi-year obsolescence curve.
7. **Beta dispute** (2.93 computed vs 1.56 disclosed) and **market-cap dispute** ($27.8B tool / $34.5B implied at 298M diluted shares / ">$50B" third-party Oct-2026) — reconciling the share count is required before sizing equity risk.

**Data gaps:** no credit rating, no CDS, no Sortino, no usable peer set (sector screen returned AAPL/NVDA/MSFT/TSM/AVGO/SKHY — mega-cap semis, **not valid neocloud comparables**), debt maturity schedule reconstructed from third-party aggregation rather than filings, and a **$1.77B gap between total debt and ST+LT debt** plus a FY25 net-income conflict ($82.5M IS vs $101.7M CF) that should be resolved against the 20-F before relying on any leverage figure.
