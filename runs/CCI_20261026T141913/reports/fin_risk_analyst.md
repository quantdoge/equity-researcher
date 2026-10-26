# Fin Risk Analyst

- Symbol: CCI
- Elapsed: 64.2s

---
## CROWN CASTLE INC. (CCI) — FINANCIAL RISK ASSESSMENT
*As of latest available annual period FY2025 (12/31/2025); market data latest close $88.17, mkt cap ~$38.5B*

### 1. Credit Risk Assessment — **INVESTMENT GRADE (Low BBB), deteriorating**

CCI is an investment-grade issuer, but at the bottom of the band and actively being re-rated downward. Note the critical structural fact from the statements: **FY2025 is already a tower-only P&L** (revenue −35% y/y to $4,265M; D&A −$1.05B to $690M; PP&E −$10.6B to $11.7B), while **all $29.6B of debt remains on the balance sheet**. The fiber/small-cell sale ($8.5B EV, to EQT/Zayo) closed 1 May 2026 — *after* the FY2025 balance sheet — so reported leverage materially overstates the go-forward capital structure.

| Metric | Reported FY2025 | Pro-forma post-close (est.) | Peer context |
|---|---|---|---|
| Total debt | $29,566M | ~$21.5–22.0B | AMT / SBAC |
| Net debt | $29,297M | ~$21.3B | — |
| Net debt / EBITDA | **10.58x** | **~7.7x** | AMT 7.13x / SBAC 7.43x |
| Interest coverage (EBIT/int.) | **2.17x** | ~3.0–3.2x | AMT 4.79x / SBAC 2.93x |
| EBITDA / interest | 2.89x | ~3.9x | — |
| Debt / assets | 94% | ~75% | AMT 71% |
| Total equity | **−$1,635M (negative)** | — | SBAC negative |

*Agency signal: Fitch downgraded CCI's IDR to **BBB** from BBB+ (stable outlook); S&P has CCI on **CreditWatch Negative**, with its ~6.5x covenant-basis leverage translating to ~7.1x on S&P-adjusted terms against a **6.0x downgrade threshold** (S&P regulatory disclosure). A move to BBB−/Baa3-negative is a live risk.*

**Data gap / caveat:** `total_debt` ($29,566M) exceeds short-term + long-term *borrowings* ($2,783M + $21,554M = $24,337M) by ~$5.2B — almost certainly capitalized ground-lease/financing obligations. On borrowings only, net debt/EBITDA is ~8.7x. Both figures are shown because lease treatment changes the multiple by >1 turn.

### 2. Key Financial Risk Metrics

| Metric | Value | Read |
|---|---|---|
| Debt / equity | n.m. (equity negative) | Book equity eroded by $4.4B 2024 impairment + accumulated depreciation (retained earnings −$20,161M) |
| Net debt / EBITDA | 10.58x reported / ~7.7x PF | High end of tower REIT peer range |
| Interest coverage | 2.17x | Weak; ~half of AMT |
| Current ratio | **0.26x** | Structurally low for a REIT, but WC is **−$3,335M** |
| Quick / cash ratio | 0.26x / 0.06x | Cash $269M vs $2,783M of short-dated debt |
| Altman Z-Score | **−0.699 (Distress)** | **Not meaningful for a REIT** — X2 (−0.64) is destroyed by accumulated depreciation, X1 (−0.11) by the negative-WC tower model. Discount heavily. |
| Piotroski F-Score | **4 / 9 (Weak)** | 4/4 on profitability (positive ROA, positive OCF, ROA improvement, clean accruals); **0/5** on leverage, equity issuance, dilution, margin & turnover — distorted by divestiture accounting |
| FCF (FY2025) | $2,875M (67% margin) | Flattered: capex only $182M vs $1,222M in FY2024 — fiber growth capex left with the sold business |
| FCF yield | 7.45% | Strong *if* sustained; normalized (~$300–400M hunt capex) ≈ 6.5–7.0% |

### 3. Market Risk Profile

| Metric | Value | Comment |
|---|---|---|
| Annualised volatility (252d) | **38.2%** | ~2x a typical large-cap REIT; elevated by deal/strategic-review event risk |
| Beta vs SPY (252d) | **0.05** | **Anomalous** — near-zero correlation. Profile beta is 0.96. Treat the 0.05 as a statistical artifact of idiosyncratic M&A tape; do **not** use it for cost of equity or hedging. |
| Max drawdown (trailing) | **−28.2%** | 3-yr peak-to-trough (my price data): **−41.3%**, $124.47 (2-Feb-23) → $73.08 (19-Oct-23) |
| Sharpe (0% rf) | 0.376 | At a ~4.3% risk-free rate, excess return is **negative** |
| Sortino | *not available* | Data gap |
| 3-yr price return | **−24.2%** ($112.86 → $85.53); ~−10% total return with dividends | Negative absolute return for 38% vol = poor risk-adjusted outcome |

**Rate sensitivity is the real market risk:** with the 10Y at 4.99% and 2s10s at +34bp (no inversion), a long-duration, 4.8%-yielding levered REIT is structurally exposed to any back-up in yields — an exposure the SPY beta completely fails to capture.

### 4. Downside Scenario — 20% Revenue Shock (−$853M to $3,412M)

Trigger would be carrier consolidation, Dish/EchoStar distress, or accelerated Sprint-related churn. Tower opex (ground leases, property costs) is largely fixed → severe operating leverage.

| | Base FY2025 | −20% revenue | −20% (pro-forma capital structure) |
|---|---|---|---|
| Revenue | $4,265M | $3,412M | $3,412M |
| EBITDA (margin) | $2,768M (64.9%) | ~$1,765M (51.7%) | ~$1,765M |
| EBIT | $2,078M | ~$1,075M | ~$1,075M |
| Interest expense | $959M | $959M | ~$700M |
| **EBIT / interest** | 2.17x | **1.12x** | ~1.54x |
| **EBITDA / interest** | 2.89x | **1.84x** | ~2.52x |
| Net debt / EBITDA | 10.6x | **16.6x** | ~12.1x |
| FCF | $2,875M | ~$624M | ~$883M |
| Dividend ($1,850M fwd) | 1.55x covered | **0.34x — not covered** | 0.48x — not covered |

**Verdict on the stress case:** EBITDA/interest of 1.84x breaches typical ≥2.0x IG coverage covenants, and net leverage of ~12–17x is far outside any covenant or rating threshold. Management would be forced to **suspend the dividend, draw the revolver, and/or issue equity at a distressed price** (~$2B+ raise). This is a solvency-of-the-distribution, not a solvency-of-the-enterprise, outcome — tower cash flows remain positive throughout, so principal/default risk over a 2–3 year horizon stays low, but equity dilution and a downgrade to sub-investment-grade become probable.

**Refinancing cliffs:** $2,783M due within 12 months vs $269M cash; the $1.75B of June/July 2026 maturities are explicitly covered by sale proceeds (per the company's closing release). Post-close, the maturity wall is manageable — but the cushion was bought with the best growth asset.

### 5. Overall Financial Risk Rating: **HIGH**
*(Bond-holder lens: Moderate. Equity-holder lens: High — negative book equity, 2.2x coverage, dividend dependent on asset-sale deleveraging, negative 3-yr total return.)*

### 6. Key Red Flags
1. **Negative shareholders' equity (−$1.6B)** and retained earnings of −$20.2B — no book-equity buffer; debt/assets 94%.
2. **Interest coverage of 2.17x** is the weakest in the tower peer set (AMT 4.79x, SBAC 2.93x) and fails 1.12x under a 20% revenue shock.
3. **Serial downgrades:** Fitch to BBB (from BBB+), S&P CreditWatch Negative; S&P-adjusted leverage ~7.1x vs a 6.0x threshold.
4. **Asset-sale-dependent balance sheet:** the deleveraging to ~7.7x is *already spent* — the growth engine (fiber/small cells) is gone, leaving a slower-growth pure tower REIT with ~$21B of debt and a shrinking revenue base ($6.99B → $4.27B).
5. **Liquidity mismatch:** current ratio 0.26x, WC −$3.3B, cash 6% of current liabilities.
6. **Piotroski 4/9 and Altman distress zone** — both are structurally biased for REITs (I discount them), but the *direction* (leverage up, equity down, no margin/turnover improvement) is genuine.
7. **Dividend sustainability:** forward ~$4.25/sh (~$1.85B, 4.8% yield) is only ~1.5x FCF-covered at base case, and the payout was already cut from $6.26 to $4.25 annualized in 2025 — a tell.
8. **Estimation risk in my own pro-forma:** net proceeds, exact post-close debt, and the FY2026 covenant EBITDA definition were not retrievable (two 403s on the closing release). Leverage post-close could be 7.3x–8.2x, not exactly 7.7x.

**Explicit data gaps:** FY2026 interim statements (post-close balance sheet), revolving-credit capacity, debt maturity ladder by year, CDS spreads, Sortino ratio, and tenant-concentration disclosure. Peer leverage figures (AMT/SBAC) are tool-derived FY2025 and comparably lease-inclusive.
