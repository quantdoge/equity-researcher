# Fin Risk Analyst

- Symbol: GDDY
- Elapsed: 57.8s

---
# GoDaddy Inc. (GDDY) — Financial Risk Assessment

**Sector:** Technology / Software – Infrastructure | **Rating date:** latest data vintage (FY2025 10-K filed 2026‑02‑25; price series through 2026‑02‑27)

---

## 1. Credit Risk Assessment: **Sub‑Investment Grade (strong BB‑type high yield)**

Solvency is **not** the risk here — cash generation is elite and leverage is modest. The balance sheet's *appearance* of fragility (17.96x debt/equity, 0.61 current ratio, 0.44 Altman Z) is almost entirely an artefact of aggressive buybacks and customer prepayment accounting, not operating distress.

| Metric | FY2025 | FY2024 | FY2023 | Read |
|---|---|---|---|---|
| Total debt | $3,862.6M | $3,894.7M | $3,935.7M | Flat/declining |
| Cash & ST inv. | $1,080.9M | $1,089.0M | $498.8M | Rebuilt |
| **Net debt** | **$2,781.7M** | $2,805.7M | $3,476.9M | Improving |
| **Net debt / EBITDA** | **2.22x** | 2.65x | 4.61x | ✅ Deleveraging |
| **EBIT / interest** | **7.5x** | 5.8x | 3.3x | ✅ Strong |
| EBITDA / interest | 8.3x | 6.7x | 4.2x | ✅ |
| FCF / interest | 10.4x | 8.0x | 5.4x | ✅ |
| EBITDA | $1,255.0M | $1,059.0M | $754.1M | +18.5% YoY |

**Covenant / refinancing structure (verified via filings search):** the $1.2B revolver was upsized and extended to **July 31, 2031**, carrying a **springing** first‑lien net leverage covenant of ≤ **5.75:1.00**, tested only when ≥40% of commitments are utilized. Outstanding notes: **$600M 5.25% due 2027** and **$800M 3.50% due 2029**, plus 2029 term loans. No maturity wall until 2029; the only near‑term obligation is the $600M 2027 note, covered **3.8x** by cash ($1.08B) + undrawn revolver ($1.2B) alone, before any FCF.

**Coverage of the covenant is the decisive point:** to breach 5.75x first‑lien leverage, EBITDA would need to fall ~61% to ~$484M. That is a catastrophic, not a cyclical, outcome.

---

## 2. Key Financial Risk Metrics

| Metric | Value | Assessment |
|---|---|---|
| Debt / equity (book) | **17.96x** | ⚠️ Not meaningful — equity is $215.1M after $2.79B cumulative buybacks |
| Debt / assets | 48% | Moderate |
| Net debt / EBITDA | 2.22x | ✅ Low |
| Interest coverage (EBIT) | 7.47x | ✅ Healthy |
| Current ratio / quick ratio | **0.61x / 0.61x** | ⚠️ Structurally <1 — see below |
| Cash ratio | 0.36x | Adequate |
| Working capital | **−$1,154.6M** | ⚠️ Negative |
| **Altman Z (book equity)** | **0.442 — Distress** | ⚠️ Mis-specified, see note |
| **Altman Z (market-cap x4)** | **~1.46 — Grey/Distress** | ⚠️ Recut; still weak |
| **Piotroski F‑Score** | **5 / 9 — Moderate** | Neutral |
| Goodwill + intangibles | $4,619.6M (57.5% of assets) | ⚠️ Tangible equity **−$4,404.5M** |
| FCF | $1,575.5M (31.8% margin) | ✅ Excellent |
| FCF yield | **9.56%** | ✅ Very strong |
| SBC | $317.8M (6.4% of rev; 20% of FCF) | ⚠️ Real dilution offset |

**Why the current ratio and Z‑score are misleading (important):** GoDaddy collects cash *up front* for subscriptions, booking the obligation as current deferred revenue. That liability is settled with **service, not cash** — it is a balance-sheet strength masquerading as a liquidity weakness. Adding the undrawn $1.2B revolver to current assets lifts the adjusted current ratio to ~1.0x; excluding deferred revenue it is comfortably above 1.5x *(exact deferred-revenue split not available from tools — flagged gap)*. Likewise, Altman's X1 (−0.144) and X2 (−0.347) are both driven by the buyback-induced retained deficit, not by operating losses. I recut the score with market capitalisation (x4 = 1.90 instead of 0.03): Z rises to ~1.46 — still grey zone, but a genuinely different picture. **I would not treat either Z reading as a bankruptcy signal for this business model.** The F‑score components that fail (F5 lower leverage, F6 positive equity change, F8 margin improvement) are all buyback/accounting artefacts; the cash-based tests (F2 positive OCF, F4 accruals quality) pass.

---

## 3. Market Risk Profile: **High**

| Metric | Value | Comment |
|---|---|---|
| Annualised volatility (756d) | **41.7%** | ~2.3x a typical large-cap software name |
| Beta vs SPY (trailing 3y) | **0.56** | vs profile 5y beta 0.94 — divergence is the tell |
| **Max drawdown** | **−65.0%** | Peak ~$214–216 (Jan 2025) → ~$73 intraday (Feb 2026) |
| Sharpe (0% RF) | **−0.06** | Negative risk-adjusted return |
| Price 2026-02-27 | $87.16 | −58% from 52-week high |

**Interpretation — this is the single most important risk finding:** trailing beta (0.56) is *far below* the long-run beta (0.94). That is not diversification; it is a signature of an **idiosyncratic de-rating that decoupled from the market**. Two single-session shocks dominate the record: **−11% on 2025‑08‑08** and **−14.3% on 2026‑02‑25**, when Q4 2025 EPS of $1.80 *beat* ($1.58 est.) and revenue of $1.27B met, but **2026 guidance and bookings growth disappointed** — Barclays, Morgan Stanley, RBC and UBS all cut targets. A stock that falls 14% on an EPS beat has **guidance/durability risk priced into it**, and the market risk is event-driven, not market-driven. For portfolio construction this behaves like a high-beta name during GDDY-specific news and a low-beta name during market drawdowns — the worst of both.

---

## 4. Downside Scenario: Revenue −20% (−$990M, to $3,961M)

Modelled with 61.6% gross margin (200bp compression) and 20% variable opex on $2,022M of total operating cost:

| Line item | FY2025 actual | −20% revenue | Change |
|---|---|---|---|
| Revenue | $4,951M | $3,961M | −20.0% |
| Gross profit | $3,150M | $2,440M | −22.5% |
| Operating expense | $2,022M | $1,941M | −4.0% |
| **EBIT** | **$1,138M** | **$499M** | **−56%** |
| EBITDA | $1,255M | ~$615M | −51% |
| Interest expense | $151M | $151M | — |
| **Interest coverage** | 7.5x | **3.3x** | Still >1x |
| **Net debt / EBITDA** | 2.22x | **4.52x** | Under 5.75x covenant |
| FCF (est.) | $1,576M | **~$715M** | +ve, 4.8% yield |

**Conclusion:** a 20% revenue decline is survivable **without equity issuance, without covenant breach, and with FCF still covering interest 4.7x**. The binding constraint is not solvency but **capital return** — the $1.6B FY2025 buyback already consumed ~102% of FCF; under this scenario buybacks would have to be cut ~55%, which is exactly the kind of discretionary lever that makes the credit resilient.

**Tail case (−35% revenue):** EBITDA ~$290M → net leverage ~9.6x → **covenant breach** and coverage near 1.9x. Probability low: revenue grew through 2020, and ~two-thirds of revenue is subscription/domains with high renewal rates. This is a "loss of the SMB franchise" scenario, not a normal recession.

---

## 5. Overall Financial Risk Rating: **MODERATE**

Split verdict, and the split is the whole point:

- **Credit/liquidity risk: LOW.** 2.22x net leverage, 7.5x interest coverage, 10x FCF/interest, 31.8% FCF margins, no maturities until 2029, springing covenant only at 5.75x, $2.3B of liquidity.
- **Market/equity risk: HIGH.** 41.7% vol, −65% drawdown, negative Sharpe, event-driven 11–14% single-day gaps.
- **Business-durability risk: MODERATE and rising.** Revenue growth is decelerating (2025 +8.3% → 9M 2026 +6.2%), and the market explicitly rejected 2026 guidance.

**Net: MODERATE** — a high-yield-quality credit with an equity security that is currently priced as a melting-ice-cube despite healthy cash generation. The FCF yield of 9.6% against a 2.2x-levered balance sheet is a wide spread, and the disconnect is the investment debate.

---

## 6. Key Red Flags

1. **Growth deceleration / guidance rejection.** Revenue growth 8.3% (2025) → 6.2% (9M 2026); −14.3% single-day reaction to *2026 guidance*, not to the quarter. Bookings growth is the leading indicator to monitor.
2. **Negative tangible equity of −$4.4B**, with $4.62B of goodwill/intangibles (57.5% of assets). Any impairment or write-down hits a $215M equity base and would be optically violent, though non-cash.
3. **Buybacks exceed FCF** ($1,602M repurchased vs $1,576M generated in FY2025). Capital returns are being run at 102% of free cash flow — zero margin for error, and the mechanism by which book equity has been driven to near zero. This is a *capital-allocation* red flag for credit holders.
4. **Structural current ratio of 0.61x** — benign given deferred revenue, but it means **no balance-sheet cushion if the revolver were ever unavailable**. Liquidity is facility-dependent, not asset-dependent.
5. **SBC at 6.4% of revenue / 20% of FCF** — real economic cost that flatters EBITDA and FCF optics; buybacks are partly funding dilution repair rather than returning capital.
6. **Floating-rate exposure unquantified.** Interest expense of $151M on $3.86B implies ~3.9% average cost. If a majority of the ~$2.45B term loans are SOFR-based, **each +100bp costs ~$25M (+16% interest expense)**, cutting coverage from 7.5x to 6.5x. *(Term-loan fixed/floating split not available from tools — flagged gap.)*
7. **Negative risk-adjusted return over 3 years** (Sharpe −0.06) — shareholders have been paid volatility, not return.

---

## Data Gaps (explicitly flagged)

- **No credit rating or CDS data available** from tools. The BB-category characterisation is *inferred* from coupon levels (5.25%/3.50%), covenant structure and leverage — not verified.
- **`fetch_yield_curve` failed** (parameter validation error); refi-cost backdrop unassessed.
- **No quarterly balance-sheet data**, so covenant compliance cannot be tracked intra-year.
- **Deferred-revenue current/non-current split unavailable** — limits the precision of adjusted liquidity ratios.
- **Price/market-cap inconsistency across feeds:** company profile quotes $117.24 / $14.85B market cap, the price series ends at $87.16 (2026‑02‑27), and `calculate_fcf_yield` used a $16.49B cap. All yield figures should be treated as a **range: 9.6% (on $16.5B) to 10.6% (on $14.85B)**. The drawdown, volatility and beta statistics are computed off the price series and are internally consistent.
- **No peer-multiple benchmarking** — the tool's "sector peers" returned mega-caps (AAPL, NVDA, MSFT) that are not meaningful operating comparables for a 5,800-employee SMB web-services vendor.
