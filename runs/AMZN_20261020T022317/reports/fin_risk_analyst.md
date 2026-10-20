# Fin Risk Analyst

- Symbol: AMZN
- Elapsed: 171.9s

---
I have what I need. Here is the assessment.

---

# AMZN — Financial Risk Assessment
**Data as of:** FY2025 10-K (filed 2026-02-06) + Q2'26 (filed 2026-07-31). Price data through 2026-02-20.

## 1. Credit Risk Assessment: **INVESTMENT GRADE** (strong, but deteriorating trajectory)

Amazon's balance sheet remains fortress-grade: **net debt/EBITDA 0.18x** on the Dec'25 basis, **interest coverage 35–44x**. Even after six months of aggressive debt issuance, net debt/EBITDA is under 1.0x. Default risk over any realistic horizon is negligible.

The caveat is *direction*, not *level*. Total debt rose **$223.2B vs $153.0B** in six months (+46%), with long-term debt nearly doubling from $65.6B to $128.9B, and Amazon priced **$24.9B of senior unsecured notes in July 2026**. This is deliberate debt-funding of a ~$200B AI capex program — an IG credit levering up to invest, not a distressed borrower. *(Agency ratings not verifiable from tool data — external search returned issuance news but no Moody's/S&P action. Flagged as a data gap; the metrics support a high-IG profile.)*

## 2. Key Financial Risk Metrics

| Metric | Value | Read |
|---|---|---|
| Debt / Equity | 0.37x (Dec'25) → **0.40x** (Jun'26) | Low |
| Debt / Assets | 0.19x → **0.20x** | Low |
| Net Debt / EBITDA | 0.18x (tool, Dec'25); **0.59–0.86x** (Jun'26, $100.2B net debt / $168.9B TTM op-EBITDA) | Low but rising fast |
| Gross Debt / EBITDA | 0.93x (Dec'25) → **1.32x** (Jun'26) | Low |
| Interest Coverage (EBIT/int.) | **35.2x** (tool); 43.8x on FY25 EBIT $99.6B/$2.27B | Very strong |
| Current Ratio | 1.05x → **1.03x** (Jun'26) | Thin |
| Quick Ratio | 0.88x | Thin |
| Cash & ST Investments | $123.0B (**flat** for 6 months despite negative FCF) | Adequate |
| Working Capital | $11.1B → **$8.0B** on a $1.1T balance sheet | Very thin |
| Equity / Assets | 0.50 | Adequate |
| Altman Z-Score | **2.33 (Grey)** as reported — see note | **~4.0–4.6 (Safe)** on market equity |
| Piotroski F-Score | **7 / 9 (Moderate)** | Fails F7 (dilution), F9 (asset turnover) |
| FCF Yield | **0.27%** (FY25); **negative** on TTM | Weak/deteriorating |

**Altman Z note — material:** the tool's x4 uses *book* equity (x4 = 1.01), which mechanically penalises a company trading at ~7x book. Restating with market equity ($2.83T / $544.1B liabilities = 5.20) and Jun'26 balance-sheet inputs gives **Z ≈ 4.6** (≈4.0 at the Feb-20 close of $210.11). Bankruptcy risk is not a live concern; the grey-zone reading is an artifact.

**F-Score detail:** the two failures are exactly the right ones to watch — **F7 = 0** (diluted shares 10.19B in 2022 → 10.90B in Q2'26, ~2%/yr creep, plus **$19.3B TTM SBC**); **F9 = 0** (PP&E $538.8B is now 49% of assets and compounding faster than revenue — asset turnover is falling).

## 3. Market Risk Profile

| Measure | Value |
|---|---|
| Annualised Volatility (504d) | **32.85%** |
| Beta vs SPY | **1.49** (profile: 1.456) |
| Max Drawdown (504d) | **-21.74%** |
| Sharpe (0% rf) | **0.879** |
| Sortino | *Not available — data gap* |

Realised drawdown path: peak close **$254.00 (2025-11-03) → $199.60 (2026-02-12), -21.4%**. The damage was event-driven: **-10% across 2026-02-05/06** around the FY25 print on 179M shares (~3x normal), then a further leg down. A -20% S&P move implies roughly **-30%** for AMZN at 1.49 beta; a 2-sigma month (9.5% monthly vol) implies a **-19%** tail. Note the 504-day window starts ~Feb 2024 and therefore **excludes AMZN's ~-50% 2022 drawdown** — true tail risk is understated by the reported max drawdown.

## 4. Downside Scenario: Revenue -20%

Baseline **TTM (Q3'25–Q2'26): revenue $775.7B, operating income $93.7B (12.1%), D&A $75.2B, op-EBITDA $168.9B, interest $3.33B, capex $173.0B, FCF -$11.6B.**

| | Base | Revenue -20% | -20% + 250bp GM compression | -30% tail |
|---|---|---|---|---|
| Revenue | $775.7B | $620.6B | $620.6B | $543.0B |
| Operating income | $93.7B | **$48.9B** | **$33.3B** | **$26.4B** |
| Operating margin | 12.1% | 7.9% | 5.4% | 4.9% |
| Interest coverage | 28.1x | **14.7x** | **10.0x** | **7.9x** |
| Op-EBITDA | $168.9B | $124.1B | $108.5B | $101.6B |
| Net debt/EBITDA | 0.59x | **0.81x** | 0.92x | 0.99x |

*Assumes COGS fully variable, cash opex 75% variable, D&A fixed.*

**Conclusion: the P&L survives easily; the cash flow does not — but capex is the release valve.** At $200B capex against a 20%-lower OCF (~$129B), FCF would be **-~$71B**, requiring another ~$70B of debt and pushing net debt toward $170B (~1.4x EBITDA) — still IG. Critically, capex is **discretionary**: throttling to maintenance (~$40B) on depressed OCF flips FCF to **+~$89B** instantly. Liquidity is therefore not a constraint in a downturn; the current ratio of 1.03 is thin, but $123B of liquid assets plus total discretion over a $200B budget is a far better defence than the headline ratio suggests.

## 5. Overall Financial Risk Rating: **MODERATE**

Split assessment: **Credit risk = LOW** (IG, sub-1x net leverage, 10–44x coverage across all stress cases). **Market/equity risk = HIGH** (33% vol, 1.49 beta, drawdown history understated by the window). **FCF/liquidity risk = MODERATE and rising** (negative TTM FCF, debt-funded capex, thin working capital).

## 6. Key Red Flags

1. **FCF has gone negative:** TTM FCF **-$11.6B** (vs +$32.9B in FY24, +$32.2B in FY23). TTM capex $173.0B exceeded OCF $161.4B. Q2'26 alone: capex $54.2B, FCF **-$8.8B**. FY2026 FCF is likely deeply negative.
2. **Debt-funded build-out:** total debt +$70.2B in 6 months; net debt $30B → $100B; cash *flat* at $123B while burning cash — every dollar of the deficit is borrowed. Interest expense annualising ~$5.3B vs $2.27B in FY25 — coverage is very high but the *rate of change* is steep.
3. **Earnings quality is distorted:** Q2'26 net income **$62.6B vs operating income $27.5B** — roughly **$55B of non-operating gains** (tool "EBIT" of $82.2B exceeds operating income by the same margin). TTM net income $135.3B vs ~$77B core. The ~21x reported P/E flatters; on core earnings it is nearer 35x+.
4. **Haircut to reported profitability:** $19.3B TTM SBC (~2.5% of revenue) and 2%/yr dilution mean GAAP earnings overstate distributable value; no dividend or buyback exists to offset it.
5. **Working capital now a drag, not a source:** -$24.4B in Q1'26 and -$7.6B in Q2'26. Working capital of $8.0B against $241.3B of current liabilities is a very thin buffer.
6. **Asset intensity inflecting:** PP&E $443.1B → $538.8B in two quarters. D&A will ramp hard, mechanically compressing margins and making the 12% operating margin harder to hold.

## 7. Explicit Data Gaps

- **Debt maturity schedule / refinancing ladder unavailable.** This is the single most important missing input for a credit assessment of a company adding $70B of debt semi-annually. *(Mitigant: $123B cash and market access demonstrated by the July 2026 $24.9B deal.)*
- **Segment data unavailable** (North America / International / AWS). AWS historically carries the majority of operating income; a 20% retail-revenue decline and a 20% AWS decline are not remotely equivalent risks. The scenario above is consolidated only.
- **Agency ratings and CDS spreads not verified** — web search returned the July 2026 issuance but no Moody's/S&P/Fitch action.
- **Sortino ratio unavailable.**
- **Price/market-cap inconsistency:** profile shows $262.45 / $2.83T, but the last observed close in the price history (2026-02-20) is **$210.11** (≈$2.29T). Market-based ratios (FCF yield, market-equity Z) carry ~20% uncertainty on this basis.
- Max drawdown window (504 days) **excludes the 2022 bear market**; genuine 3-year tail risk is worse than -21.7%.

**Bottom line:** AMZN is not a solvency story — it is an **FCF and earnings-quality story**. The credit can absorb a 20–30% revenue shock without breaching any plausible covenant, and management retains enormous optionality via capex discipline. But the company has crossed from self-funding to debt-funding its growth, reported earnings are materially inflated by non-operating gains, and the equity carries 1.5x market beta with 33% volatility and no shareholder-return cushion. The watch item for the next four quarters is the **capex/OCF gap and the debt trajectory** — not leverage levels.
