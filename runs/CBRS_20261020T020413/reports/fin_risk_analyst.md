# Fin Risk Analyst

- Symbol: CBRS
- Elapsed: 122.7s

---
# CBRS — Cerebras Systems Inc. | Complete Financial Risk Assessment

**As of 19 Oct 2026 | Price $120.66 | Mkt cap ≈$27.3B (FMP) | Sector: Technology / Semiconductors**

---

## 1. Credit Risk Assessment: **Investment Grade (balance-sheet only) — Unrated**

There is **no credit rating or CDS spread available** (no rated debt; first 10-K not yet filed — audited record stops at FY2025 inside the IPO prospectus). Data gap flagged.

The counterintuitive conclusion: despite a **$(145.9)M operating loss** and a pre-IPO *book equity deficit*, CBRS has **essentially no credit risk today** — because the May 2026 IPO injected ~**$6.2B of net proceeds**:

| Post-IPO (30 Jun 2026) | Value |
|---|---|
| Cash & equivalents | $6.74B |
| Investments | $1.18B |
| **Total liquidity** | **$7.92B** |
| Gross debt | ~$1.18B ($918.2M OpenAI working-capital loan @6% + ~$262M leases) |
| **Net cash** | **≈ +$6.7B** |
| Total equity | $9.15B (from **–$578.7M** deficit at 12/31/25) |
| Undrawn revolver | $850.0M |

**This is not investment grade in the conventional sense — it is equity-funded solvency.** The company cannot fail on debt service; it can only fail on cash consumption. Interest expense is ~$55M/yr against $7.9B of liquidity (~144x liquid coverage). Sole loan matures **no later than 31 Dec 2032** — no refinancing cliff.

⚠️ **Critical caveat:** at 12/31/25 the company was **technically balance-sheet insolvent on a book basis** — liabilities $2.90B vs assets $2.33B, equity **–$578.7M**. The IPO cured this. Pre-IPO, CBRS was a distress credit.

---

## 2. Key Financial Risk Metrics

| Metric | FY2023 | FY2024 | FY2025 | Latest (H1'26 / post-IPO) |
|---|---|---|---|---|
| Revenue | $78.7M | $290.3M | $510.0M | $373.5M (H1, +84%) |
| Revenue growth | — | +268.6% | +75.7% | +74.3% (Q2 YoY) |
| Gross margin | 33.5% | 42.3% | 39.0% | **14.2%** (Q2 GAAP); 41–43% "core" |
| Operating margin | –170.1% | –35.0% | **–28.5%** | –265% GAAP / –55.6% ex-SBC |
| Net income | –$127.2M | –$481.6M | **+$237.8M** ⚠️ | n/m |
| Operating cash flow | –$79.0M | +$452.0M ⚠️ | –$10.1M | –$47.5M |
| Capex | $6.6M | $23.4M | $382.7M | **$548.9M** |
| Free cash flow | –$85.6M | +$428.5M ⚠️ | –$392.8M | **–$596.4M** |
| FCF yield | — | — | **–1.51%** | — |

**Leverage & Coverage**

| Metric | Reading | Interpretation |
|---|---|---|
| Debt/Equity | –0.45 (12/31/25) → **0.13x** post-IPO | Meaningless pre-IPO (neg. equity); 0.13x now = negligible |
| Net debt / EBITDA | **–3.03x** | Net cash. Leverage risk ≈ nil |
| Debt / Assets | 0.11x → ~0.09x | Lease-dominated |
| Interest coverage (EBIT/int.) | **N/A — EBIT negative** | Coverage is 0x on earnings; ~144x on liquidity |
| Current ratio | 2.15x | Strong |
| Quick ratio | 2.06x | Strong (inventory only $63.6M) |
| Cash ratio | 1.54x | Strong |
| Working capital | +$824.1M | Strong |
| **Altman Z-Score** | **0.327 "Distress"** | ⚠️ **Model artifact — see below** |
| **Piotroski F-Score** | **5 / 9 "Moderate"** | ⚠️ Overstated — see below |

### ⚠️ Two model outputs are structurally misleading — must be adjusted

**Altman Z (0.327 → Distress): INVALID.** The model uses *book* equity as x4, and book equity was **–$578.7M** pre-IPO because preferred stock sat at liquidation value. Re-running x4 with the $27.3B market cap (x4 = 9.41) gives:
> **Z ≈ 0.327 + 0.42 × (9.41 – (–0.199)) ≈ 4.36 → SAFE ZONE.**

The "distress" reading is an accounting artifact of IPO structure, not financial reality. Post-IPO book equity of $9.15B confirms this.

**Piotroski F-Score (5): OVERSTATED.** Component detail shows the weakness:
- **F2 = 0** — *negative* operating cash flow (–$10.1M)
- **F4 = 0** — accruals quality fails badly: net income **+$237.8M** vs OCF **–$10.1M**, a **$248M gap**
- **F1 = 1** (positive ROA) is itself driven by the non-operating gain, not operations
- **F8 = 0** — gross margin deteriorated
- **F9 = 0** — asset turnover deteriorated

**On an operating basis, the true F-Score is ~3.** Flagging the reported 5 as generous.

**The FY2025 "profit" is not earnings.** Net income of +$237.8M versus an operating loss of $(145.9)M implies **~$380M of non-operating income**; the prospectus attributes ~$363.3M to a specific item. *Nature not fully verified in this pass — flag as an open diligence item.* Similarly, **FY2024's +$428.5M "FCF" was a working-capital artifact** (+$443.5M WC swing, i.e., customer prepayments/deposits) against a $(481.6)M net loss. **Neither year represents sustainable cash generation.**

---

## 3. Market Risk Profile — **this is where the risk lives**

| Metric | Value | Comment |
|---|---|---|
| Annualised volatility | **114.6%** | Extreme — ~5x a typical large-cap |
| Beta vs SPY | **3.00** | A 10% market drawdown implies ~30% downside |
| Max drawdown | **–61.2%** (close-to-close) | –68.9% intraday (peak $386.34 → low $120.12) |
| Sharpe ratio | **–1.36** | Negative risk-adjusted return since IPO |
| Price vs IPO offer ($185.00) | **–34.8%** | Trading well below issue |
| Price vs first close ($311.07) | **–61.2%** | |
| Recent momentum | –27% in ~12 sessions (10/2 → 10/19) | Deteriorating trend |

⚠️ **Statistical reliability caveat:** vol and beta are computed on only **~110 trading days** (IPO 14 May 2026). A 115% vol estimate on a 5-month window is directionally indicative but imprecise; beta 3.0 reflects a single, high-correlation regime. Treat as order-of-magnitude.

**Near-term catalyst risk:** 180-day lock-up expiry likely falls around **early November 2026** — roughly 226–237M shares versus a thin free float (Class A only ≈ $23.6B of the $49.9B total market value per filings). This is a concrete, dated downside trigger. *Verify exact date.*

**Valuation is the real risk, not solvency:** ~69x annualised Q2 revenue (vs NVDA 14.4x, AMD 16.9x, Intel 7.5x). At that multiple, a modest growth disappointment produces a violent de-rating — exactly what the drawdown already reflects.

---

## 4. Downside Scenario Analysis — Revenue –20%

Base: FY2026 core revenue guidance **$880–890M** (midpoint $885M), core gross margin 41–43%, core operating margin **(17)–(19)%**. Implied core opex ≈ **$540M** (GP $372M + $168M loss).

**Scenario: revenue –20% → $708M**

| Line | Base (guidance) | –20% revenue | Change |
|---|---|---|---|
| Revenue | $885M | $708M | –$177M |
| Gross profit @42% (fixed %) | $372M | $297M | –$75M |
| Core opex (held flat) | $540M | $540M | — |
| **Core operating income** | **–$168M** | **–$243M** | **–$75M** |
| Opex flexed –10% | — | $486M | **–$189M** |
| Capex (2026 run-rate) | ~$1.1B | ~$1.1B | 0 (committed build-out) |
| **FCF (approx.)** | **~–$1.3B** | **~–$1.5B** | worse |

**Verdict: financially survivable, marketwise severe.**
- Liquidity of **$7.92B** against a **~$1.5B** annual burn in the downside = **~5.3 years of runway**, with an $850M revolver undrawn. There is no plausible revenue scenario in the next 3 years that forces a solvency event.
- The damage would be to the **equity**, not the balance sheet: at $885M the market pays ~31x forward sales; a –20% miss with a widening loss plausibly compresses the multiple toward 10–15x → **–50% to –65% equity downside**. Consistent with the observed 69% peak-to-trough.
- **Genuine tail risk is concentration, not the P&L.** MBZUAI was **62% of FY2025 revenue** (34% in Q2'26) and G42 **85% of FY2024** (24% FY2025). Two customers held **76% of receivables**. A *single* contract event — not a market-wide 20% slowdown — is the realistic –50% scenario. Add geopolitical exposure (UAE-linked counterparties).
- A working-capital/related-party wrinkle: the **$918.2M loan is from OpenAI**, which is simultaneously a **customer** ($56.8M in Q2'26, $74.4M in H1). Customer-funded vendor financing cuts both ways.

---

## 5. Overall Financial Risk Rating: **HIGH**

*(Not "Critical" — because Critical should mean solvency risk, and here solvency risk is genuinely low. High reflects extreme market, concentration, and cash-consumption risk.)*

| Risk Dimension | Rating | Rationale |
|---|---|---|
| **Credit / solvency risk** | **Low** | Net cash ~$6.7B, D/E 0.13x, no maturity before 2032, $850M undrawn |
| **Liquidity risk** | **Low** | >6 years runway at current burn; 5+ years even in downside |
| **Market risk** | **Critical** | 115% vol, beta 3.0, –61% drawdown, lock-up pending |
| **Business/concentration risk** | **High** | 2 customers >76% of receivables; UAE concentration |
| **Earnings quality** | **High concern** | Headline profit is non-operating; FCF negative |
| **FCF sustainability** | **High concern** | Capex ~90%+ of revenue; model shifting to capital-intensive cloud |

---

## 6. Key Red Flags

1. **Earnings quality — headline profit is illusory.** FY2025 net income +$237.8M rests on ~$363–384M of non-operating income against a $(145.9)M operating loss. The $248M NI-vs-OCF accrual gap (F4 = 0) confirms this is not cash earnings.
2. **Balance-sheet insolvency pre-IPO.** Equity was **–$578.7M** at 12/31/25; liabilities exceeded assets. Cured solely by $6.2B of IPO proceeds — the balance sheet is an equity-market artifact, not a cash-generation achievement.
3. **Extreme customer concentration.** MBZUAI 62% of FY2025 revenue; G42 85% of FY2024. Two customers = 76% of receivables. This is existential, not a footnote.
4. **Gross margin collapse.** 42.3% (FY24) → 39.0% (FY25) → **14.2%** (Q2'26 GAAP). Management's 41–43% "core" margin excludes $44.3M/quarter of **customer warrant amortisation charged against revenue through Oct 2031** (~$177M/yr structural headwind). Watch whether "core" frames away a real economic cost.
5. **Runaway share-based compensation.** **$377M in Q2'26 alone — ~209% of revenue**, including $273.6M of RSU expense triggered by the IPO liquidity condition. Severe dilution risk and an inflated non-GAAP "ex-SBC" loss.
6. **Capital intensity inflection.** Capex $6.6M → $23.4M → $382.7M → $548.9M (H1'26 alone). Business model is shifting from hardware sales to owned cloud capacity; FCF likely negative for years. FCF yield **–1.51%**.
7. **Auditor change and short audit history.** FY2024 audited by BDO, FY2025 by KPMG; **no 10-K filed yet**. Limited audited operating record.
8. **Market structure risk.** Trading 35% below IPO price, 69% off the high, with a lock-up expiry imminent and beta 3.0. Downside participation is asymmetric.
9. **Data inconsistencies flagged:** (a) net debt reported as –$439.9M on the balance sheet vs –$846.4M in the leverage tool (reconciled: $1,108.2M cash + investments – $261.8M debt = –$846.4M; the former excludes short-term investments); (b) market cap $27.3B (FMP, ~226.5M shares) vs ~$28.7B implied by 237.6M shares across classes per filings; (c) debt/equity of –0.45 is not economically meaningful pre-IPO.

**Mitigants:** $25.4B of remaining performance obligations (22% expected within 24 months), revenue +74% YoY, raised FY26 guidance, zero net debt, and a fully funded multi-year runway. The company will not run out of money. It can, however, run out of multiple.

**Bottom line:** CBRS is a **well-capitalised, cash-consuming, single-customer-concentrated growth story trading at a rich multiple with extreme price volatility.** Judge it as an *equity* risk, not a *credit* risk — the balance sheet is a fortress built from IPO proceeds, and the operating cash flows have never funded it.

---
**Data gaps:** no credit rating/CDS; no 10-K (audited record ends FY2025); vol/beta on ~110 sessions only; nature of the ~$363.3M FY2025 non-operating gain unverified; exact lock-up expiry date unverified; peer multiples drawn from secondary source (sec-api.io, 4 Sep 2026).
