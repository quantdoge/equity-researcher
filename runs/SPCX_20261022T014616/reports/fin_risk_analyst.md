# Fin Risk Analyst

- Symbol: SPCX
- Elapsed: 478.6s

---
## SPCX — Financial Risk Assessment
**Space Exploration Technologies Corp. (SpaceX) | Industrials – Aerospace & Defense | FY end 12/31/2025**

⚠️ **Data integrity notes up front:** (1) Profile `market_cap` ($2.10T) is inconsistent with price × shares ($159.31 × 2.926B = **~$466B**, which matches the FCF-yield engine); I use $466B. (2) SPCX listed 2026-06-12 — only **13 trading sessions** of price history exist, so vol/beta are statistically fragile. (3) No quarterly statements, debt maturity schedule, covenant terms, or credit rating/CDS data available. (4) Treasury yield-curve feed failed twice — rate-environment context is a gap. (5) Balance sheet predates the June 2026 IPO, so post-IPO cash is *understated* by an unknown amount.

---

### 1. Credit Risk Assessment — **Sub-Investment Grade (speculative, ~BB-/BB band, "liquidity-secured")**
Leverage is genuinely conservative: total debt $22.90B against **$24.75B cash → net cash of $1.85B** (net debt/EBITDA **−0.43x**), debt/assets 0.25x, D/E 0.55x. This is *not* a leverage story. The problem is **debt-service capacity out of earnings**: FY25 EBIT was **−$2.41B**, so GAAP interest coverage is **−1.33x** and only **2.21x on EBITDA** ($4.29B / $1.95B) — well below GE (10.4x) and RTX (5.1x), and only modestly above Boeing (1.54x, which carries 3.4x net leverage vs SPCX's net cash). Implied cost of debt ≈ **8.5%** ($1.945B / $22.9B), consistent with high-yield/unsecured-plus-convertible financing. Interest expense rose 23% YoY while debt rose 66%. The credit is funded by capital markets and equity, not by cash generation.

### 2. Key Financial Risk Metrics Table

| Metric | FY2025 | FY2024 | Assessment |
|---|---|---|---|
| Revenue | $18.67B (+33.2%) | $14.02B (+34.9%) | Strong top line; 2-yr CAGR ~34% |
| Gross margin | 49.4% | 42.9% | Improving |
| Operating margin | **−13.9%** | +3.3% | Deteriorated |
| EBITDA / EBIT | $4.29B / **−$2.41B** | $3.31B / −$0.52B | EBITDA positive, EBIT negative |
| Net income | **−$4.94B** | +$0.79B | Loss |
| Total debt | $22.90B | $13.79B | +66% YoY |
| Net debt / EBITDA | **−0.43x** (net cash) | 0.73x | Strength |
| Debt / equity · Debt / assets | 0.55x · 0.25x | 0.53x · 0.24x | Low |
| Interest coverage (EBIT) | **−1.33x** | −0.33x | Failure |
| Interest coverage (EBITDA) | 2.21x | 2.09x | Thin |
| Current / quick / cash ratio | 1.45 / 1.33 / 1.16 | — | Adequate |
| Working capital | $9.55B | $4.32B | Positive |
| Altman Z-Score (book equity) | **0.166 — Distress** | — | Accumulated deficit −$37.0B |
| Altman Z-Score (market equity ≈$466B) | **≈5.2 — Safe** | — | Market values solvency |
| Piotroski F-Score | **5/9 — Moderate** | — | +OCF, +accruals, +GM; −ROA, −turnover, −leverage |
| FCF / FCF yield | **−$13.95B / −2.99%** | −$5.39B | Burn widening 2.6x |
| Capex / revenue · Capex / OCF | 111% · 3.06x | 80% · 1.93x | Growth investment heavy |

The Z-score split is the single most important nuance in this file: on book equity SPCX screens as bankrupt; on its actual market equity it screens as a fortress. The truth is in between — **solvent, but only because the equity market keeps funding it.**

### 3. Market Risk Profile
- **Annualised volatility: 80.6%** (vs ~15–20% for large-cap industrials) — top-decile single-stock risk.
- **Beta vs SPY: 3.09** — a 10% index drawdown implies ~31% SPCX downside; note profile beta field reads `0` (placeholder) and the 3.09 is estimated on 13 sessions only.
- **Max drawdown: −46.4%** (visible tape peak $225.64 on 6/16 → $147.11 on 6/23 = −34.8% intraday, so the 46.35% figure likely uses a wider/synthetic window — directionally confirmed: the stock halved from its post-IPO high in eight sessions).
- **Sharpe ≈ 0.36** at a 0% risk-free assumption; on a ~4–4.5% T-bill alternative the ratio is **negative** — investors are not being compensated for the volatility on a risk-adjusted basis.
- **Valuation fragility:** ~24.9x sales, **~108x EV/EBITDA**, −3.0% FCF yield, ~16.7x tangible book. This multiple is a discount-rate and sentiment instrument; it is the dominant driver of equity risk, not the balance sheet.

### 4. Downside Scenario Analysis (revenue −20% → $14.94B)

| | Base FY25 | −20% Revenue, capex flexed | −20% Revenue, capex held | Severe −35%, capex held |
|---|---|---|---|---|
| Gross profit (49.4% GM) | $9.22B | $7.38B | $7.38B | $6.00B |
| Opex (cut 10%/15%) | $11.81B | $10.63B | $10.63B | $10.04B |
| Operating income | −$2.59B | −$3.25B | −$3.25B | −$4.04B |
| EBITDA | $4.29B | $3.45B | $3.45B | $2.66B |
| EBITDA / interest | 2.21x | **1.77x** | 1.77x | **1.37x** |
| Operating cash flow | $6.79B | ~$4.94B | ~$4.94B | ~$3.56B |
| Capex | $20.74B | $12.0B | $20.74B | $20.74B |
| FCF | −$13.95B | ~−$7.1B | **~−$15.8B** | **~−$17.2B** |
| Cash runway (ex-IPO proceeds) | 7.1 qtrs | ~3.5 yrs | **~1.5 yrs** | **~1.4 yrs** |

**Key insight:** the burn is **discretionary growth capex**, not an operating cash deficit — OCF is +$6.79B. Management can halve capex and survive a 20% revenue shock for 3+ years. The genuine tripwire is **coverage, not liquidity**: EBITDA would need to fall below ~$3.9B (≈−9% revenue with flat opex) to breach a typical 2.0x interest-coverage covenant, and below ~$2.9B for 1.5x. That is reachable in a −20% to −25% scenario with capex held — which is exactly when flexibility is least likely. Absent covenant documentation, this is an inference, not a confirmed term.

### 5. Overall Financial Risk Rating: **HIGH**
Decomposed: **credit/solvency = Moderate** (net cash, no near-term maturity cliff — only $928M, 4.1% of debt, matures within a year, covered 26x by cash); **liquidity/cash-flow = High** (−$13.95B FCF, ~7 quarters of runway pre-IPO); **market/valuation = High-to-Critical** (80.6% vol, 3.09 beta, −46% drawdown, 25x sales). The "High" verdict is driven by **cash-consumption intensity and valuation**, not by leverage — an unusual and important distinction for the investment committee.

### 6. Key Red Flags
1. **Negative EBIT and negative GAAP interest coverage (−1.33x)**; cash coverage only 2.2x and deteriorating as debt grows 66%/yr.
2. **FCF burn widening 2.6x YoY** (−$13.95B); capex at 111% of revenue and 3.06x operating cash flow — a capital-markets-dependent model.
3. **Altman Z 0.166 in the distress zone** on book equity; retained earnings deficit −$37.0B.
4. **Massive dilution overhang:** FY24 diluted share count 9.956B vs basic 2.848B — ~250% potential dilution from converts/preferred; a fresh IPO adds further supply.
5. **Extreme valuation fragility:** ~25x sales, ~108x EV/EBITDA with negative FCF — highly sensitive to rates and risk appetite.
6. **Data gaps:** no maturity ladder, no covenant terms, no rating/CDS, no quarterly trend, inconsistent market-cap field, and 13-session price history that makes the 80.6% vol / 3.09 beta estimates unreliable in magnitude (though not in direction).

**Bottom line:** SPCX will not fail on its balance sheet — $24.75B cash, net cash position, and discretionary capex give it real staying power. It can fail *as an equity* through dilution and multiple compression. Monitor EBITDA/interest monthly (2.2x, covenant tripwire ~2.0x), quarterly FCF vs. capex plan, and any convertible issuance or secondary offering.
