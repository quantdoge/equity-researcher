# Fin Risk Analyst

- Symbol: FICO
- Elapsed: 180.5s

---
## FICO (Fair Isaac Corporation) — Financial Risk Assessment
*Data as of latest available: balance sheet/cash flow to 30-Jun-2026 (FQ3 FY26); price to 16-Oct-2026 ($771.19).*

---

### 1. Credit Risk Assessment — **SUB-INVESTMENT GRADE (deteriorating)**

| Agency | Rating | Outlook |
|---|---|---|
| Moody's | **Ba2** CFR & senior unsecured | Stable |
| S&P | **BB+** (issue-level, new notes) | — |

Both agencies place FICO two-to-three notches below investment grade. That is the single most important credit fact: despite a ~52% EBIT margin, FICO is a **junk-rated** borrower because of buyback-driven negative equity and rising leverage.

**Leverage and coverage trajectory (LTM to 30-Jun-26):**
- Gross debt **$5,598m** vs **$3,075m** at FYE Sep-2025 — up **+82% in three quarters**
- Cash **$248m** → net debt **$5,350m**
- LTM EBITDA $1,268m → **net debt/EBITDA 4.22x** (gross 4.42x) vs **3.09x** at FY25
- LTM EBIT $1,251m / interest $186m = **6.7x coverage**; on the FQ3 run-rate interest of $59.9m (~$240m annualised) coverage is already down to **~6.3x**
- Total equity **–$4,097m**; equity/assets **–2.01x**. Debt/equity is not meaningful (n.m.) when equity is negative.

The cause is capital allocation, not operations: **~$4.3bn of buybacks over the last five quarters** ($1.41bn FY25, $0.61bn FQ2 FY26, **$2.27bn in FQ3 FY26 alone**), funded partly by a **$1.0bn 6.25% senior notes issue due Sept-2034 (closed Mar-2026)**.

### 2. Key Financial Risk Metrics

| Metric | Latest (Jun-26 LTM) | FY2025 (Sep-25) | Read |
|---|---|---|---|
| Net debt / EBITDA | **4.22x** | 3.09x | Deteriorating |
| Gross debt / EBITDA | 4.42x | 3.23x | Deteriorating |
| Debt / equity | n.m. (equity –$4.10bn) | n.m. (–$1.75bn) | Negative book equity |
| Debt / assets | 2.75x | 1.65x | Asset-light distortion |
| EBIT / interest | **6.7x** | 7.0x | Adequate but falling |
| Current ratio | **1.18** | 0.83 | Improved |
| Quick ratio | 1.18 | 0.83 | No inventory |
| Cash ratio | 0.33 | 0.16 | Thin |
| Working capital | +$136m | –$144m | Improved |
| Cash / total liabilities | 4.0% | 3.7% | Very thin |
| Altman Z-Score | 5.0 (tool: 5.75, FY25) — "Safe" | 5.75 | **Distorted — see caveat** |
| Piotroski F-Score | 7 (FY25 reported) | 7 | Leverage/equity criteria failing |

**Altman caveat (important):** with total assets of only $2.04bn against $2.39bn revenue, X2 (retained earnings/TA = 2.56), X3 (EBIT/TA = 0.61) and X5 (revenue/TA = 1.18) are inflated by the near-zero asset base, while X4 is negative (book equity/liabilities = –0.67). The Z-score's "safe" reading is mechanically misleading; the negative X4 and the 4.4x gross leverage are the real signals. Similarly, the F-Score's two failing components are precisely leverage (F5) and equity change (F6) — worsening for a third straight year.

**FCF sustainability:**
- LTM FCF **$996m**; FY25 $770m; FY24 $607m → improving trend, FCF/EBITDA ~79%, capex only $5m LTM
- FCF / interest = **5.3x**; FCF yield **~6.0%** on current $16.66bn market cap
- FCF margin ~42% of revenue — best-in-class, but **SBC of ~$52m/quarter (~$209m annualised)** is a real cost not deducted from EBITDA
- *Data note: the FCF-yield tool reported 4.06% using a market cap of $18.94bn; the profile's price/market-cap fields ($771.19 price but $16.66bn cap) are internally inconsistent with the price history. Using the 16-Oct-26 close of $771.19 and ~21.6m shares, cap ≈ $16.7bn and FCF yield ≈ 6.0%.*

### 3. Market Risk Profile — **High / tail-risk event**

| Metric | Value |
|---|---|
| Annualised volatility (3y) | **48.1%** |
| Beta vs SPY (computed) | **0.90** (profile states 1.34 — conflicting feeds) |
| Max drawdown (3y) | **–75.1%** |
| Sharpe ratio | **0.137** (poor risk-adjusted return) |
| Sortino | Not available — **data gap** |

Verified from price data: peak **$2,402.52 (13-Nov-2024)** → trough close **$592.47 (30-Sep-2026)** = **–75.3%**; stock is **–57% since Nov-2025**. Repeated single-day gaps: **–26.5% (29-Sep-26)**, –16.7% (4-Sep-26), –17.0% (30-Jul-26 post-earnings), –8.5% (3-Feb-26). This is not a benign-beta name: the low computed beta is an artefact of idiosyncratic, not market, risk — 48% vol with a 0.14 Sharpe means the price risk is company-specific and highly event-driven.

### 4. Downside Scenario — Revenue –20% (LTM $2,394m → $1,915m)

The realistic transmission channel is the **Scores segment** (roughly half of revenue, majority of profit): FHFA on **8-Jul-2025 authorised VantageScore 4.0** alongside Classic FICO for conforming mortgages, and further competition is under consideration.

| Line | Base (LTM) | –20% revenue, 40% cost flex | –20% revenue, 25% cost flex |
|---|---|---|---|
| Revenue | $2,394m | $1,915m | $1,915m |
| EBITDA | $1,268m | $980m | $909m |
| EBIT | $1,251m | $963m | $892m |
| Interest (run-rate) | $240m | $240m | $240m |
| **EBIT / interest** | 6.3x | **4.0x** | **3.7x** |
| **Net debt / EBITDA** | 4.22x | **5.46x** | **5.89x** |
| FCF (approx.) | $996m | ~$572m | ~$470m |
| FCF / interest | 5.3x | 2.4x | 2.0x |

**Conclusion:** a 20% revenue shock is *survivable* — FCF still covers interest ~2x and debt service — but net leverage moves to **5.5–5.9x**, i.e. deep single-B territory, and would almost certainly trigger a downgrade, a halt to buybacks (the equity story's core), and possible covenant pressure. Growth in FY26 has been strong (FQ2 +, FQ3 revenue $674m, 54% operating margin), so the stress is a *multiple/structural* risk more than an operating one.

### 5. Overall Financial Risk Rating: **HIGH**

Not "Critical": the company generates ~$1bn of FCF, covers interest ~6x, has positive working capital, and has no near-term maturity wall ($300m short-term debt vs $996m LTM FCF). But it is High, not Moderate, because: negative book equity of –$4.1bn, net leverage of 4.2x rising fast, junk ratings, and ~48% vol with a 75% drawdown on a concentrated, politically-exposed business model.

### 6. Key Red Flags
1. **Negative shareholders' equity –$4.10bn** (worsened from –$1.75bn in 12 months). Zero book cushion for creditors; debt/assets 2.75x.
2. **Leverage accelerating to fund buybacks:** debt +82% in three quarters, net leverage 3.1x → 4.2x, interest expense run-rate +50% YoY ($39.9m → $59.9m per quarter).
3. **Sub-investment-grade ratings (Ba2/BB+)** with an equity market already pricing structural impairment: –75% peak-to-trough, including a –26.5% single-day move (29-Sep-2026).
4. **Regulatory/competitive concentration:** FHFA's July-2025 authorisation of VantageScore 4.0 in conforming mortgages — a direct threat to the Scores franchise; event risk is ongoing.
5. **Thin absolute liquidity:** $248m cash (4% of liabilities) against $6.13bn liabilities, current ratio 1.18, cash ratio 0.33. Liquidity depends on FCF and revolver access, not balance-sheet reserves.
6. **Benign-looking screens:** Altman Z 5.0 "Safe" and F-Score 7 mask the deterioration; treat both as unreliable for this asset-light, negative-equity, buyback-heavy company.
7. **SBC ~$209m annualised** flatters EBITDA-based leverage metrics by roughly 0.2x.

### 7. Explicit Data Gaps
- **Covenant terms and the precise debt maturity ladder were not retrieved** (web search for the FY2025 10-K note schedule timed out; only the new $1.0bn 6.25% notes due 2034, the ~$300m short-dated tranche, and ~$2.6bn of legacy senior notes are evidenced). With gross leverage at 4.4x, whether the revolver carries a 4.0x-style incurrence/maintenance test is the key unverified question.
- **Revolver size and availability** unknown.
- **Sortino ratio / CDS spreads** unavailable.
- Beta conflict between feeds (0.90 computed vs 1.34 reported).
- Profile price/market-cap fields stale (~$771 price tagged to a $16.66bn cap that does not reconcile with the $1,806 close in Nov-2025) — all market-cap math here uses the verified 16-Oct-2026 close of $771.19.
