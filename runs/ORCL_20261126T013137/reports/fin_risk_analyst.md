# Fin Risk Analyst

- Symbol: ORCL
- Elapsed: 71.7s

---
## ORACLE CORPORATION (ORCL) — Financial Risk Assessment
*Data as of FY2026 (ended 5/31/26), Q1 FY2027 (ended 8/31/26), and market data through the latest quote ($103.88).*

---

### 1. Credit Risk Assessment — **SUB-INVESTMENT GRADE (cusp)**

| Rating agency | Rating | Outlook |
|---|---|---|
| S&P Global | **BBB-** (downgraded from BBB, July 2026) | Stable |
| Moody's | **Baa2** | **Negative** |
| Fitch | BBB | Stable |
| **Market-implied (CDS)** | **~356bp — record wide** | Implies **BB / high-yield** |

Oracle sits at the **bottom rung of investment grade with negative momentum**. The most important signal is the divergence: a BBB- issuer should trade near 80–150bp CDS; ORCL trades at **356bp**, roughly 2.5–4x the IG median. The bond market is already pricing a downgrade to high yield.

**Why credit is deteriorating — the numbers tell one story:**

| Metric | FY2024 | FY2025 | FY2026 | Q1 FY27 / TTM |
|---|---|---|---|---|
| Revenue ($M) | 52,961 | 57,399 | **67,357** | 78,477 (TTM est.) |
| EBITDA ($M) | 21,394 | 23,912 | 33,447 | 37,719 (TTM) |
| Total debt ($M) | 94,469 | 104,104 | **156,189** | 155,931 |
| Net debt ($M) | 84,015 | 93,318 | 124,295 | 119,562 |
| Interest expense ($M) | 3,514 | 3,578 | **4,599** | 5,104 (TTM) |
| Interest coverage (EBIT/int) | 4.37x | 4.94x | **4.48x ↓** | 4.52x |
| Net debt / EBITDA | 3.93x | 3.90x | 3.72x | 3.17x |
| Total equity ($M) | 9,239 | 20,969 | 43,056 | 67,196 |
| Equity / Assets | 6.6% | 12.5% | 16.4% | 22.2% |

Oracle added **$52.1B of debt in a single year (+50%)** and $61.8B over two years. Coverage has now *rolled over* (4.94x → 4.48x) despite 17% revenue growth — interest expense is compounding faster than EBIT. Debt funded 100% of a $55.7B capex program that generated no revenue in the period.

**Capitalized-interest illusion:** Oracle capitalizes interest on construction. Reported $4.6B interest expense understates true economic interest cost; as datacenters are placed in service, that capitalized interest converts to P&L expense, creating a mechanical step-up in future interest expense beyond the 24% yoy growth already visible.

---

### 2. Key Financial Risk Metrics

| Metric | Value | Assessment |
|---|---|---|
| Debt / Equity | 3.63x | **High** — 2.5x+ typical for IG software |
| Debt / Assets | 59.7% | High |
| Net Debt / EBITDA | 3.72x (FY26) / 3.17x (TTM Q1) | Elevated but not covenant-threatening *today* |
| Interest coverage | 4.48x | Adequate now; **declining trend**; thin after depreciation ramp |
| **Altman Z-Score** | **0.679 — DISTRESS** | Book-equity basis |
| Altman Z (market-cap adjusted, X4 = 1.44) | **≈1.42 — still distress zone** | Fails even on the generous basis |
| **Piotroski F-Score** | **5 / 9 — Moderate** | See below |
| Current ratio | 1.12x (1.17x Q1 FY27) | **Thin** for an IG credit |
| Quick ratio | 1.12x (no inventory) | Thin |
| Cash ratio | 0.76x | Adequate |
| Working capital | +$4,803M | Positive but modest vs. $218.7B liabilities |
| Cash & ST investments | $31.9B → $37.1B (Q1 FY27) | Meaningful absolute buffer |
| **FCF (FY26)** | **–$23,686M** | Severe negative |
| FCF yield | **–7.82%** | Negative |
| FCF margin | **–35.2%** | Deteriorating from +22.3% (FY24) |
| Capex / revenue | **82.6%** | Extreme |
| Capex / operating cash flow | 174% | Capex exceeds all internal cash generation |

**Altman Z caveat:** the tool's 0.679 uses *book* equity, which is punitive given $43B book equity vs $314B market cap. Recomputing with market capitalization (X4 = 314.1/218.7 = 1.44) yields **Z ≈ 1.42** — still firmly below the 1.81 distress threshold. Even a 7x book-to-market rescue cannot lift ORCL out of the distress zone, which is itself the finding: leverage and fixed-asset intensity are now structurally incompatible with a conventional software credit profile.

**Piotroski detail (5/9):** Positives = positive ROA, positive operating cash flow, accruals quality, book leverage reduction (from the equity raise), positive equity change. **Failures = declining ROA, share dilution (+3% diluted shares), declining gross margin (65.8% vs 70.5% FY25 vs 71.4% FY24), declining asset turnover (0.257x vs 0.341x).** The margin and turnover deterioration is the OCI mix shift — Oracle is trading a 70%-gross-margin software business for a ~30–40%-gross-margin compute business.

---

### 3. Market Risk Profile — **EXTREME**

| Metric | Value |
|---|---|
| Annualized volatility (2yr) | **59.1%** (vs ~30% for large-cap software) |
| Beta vs SPY | **1.74** (company-reported beta 1.78) |
| Max drawdown (3yr) | **–68.7%** |
| Sharpe ratio (0% rf) | **–0.071** — negative risk-adjusted return |
| Peak close | $323.43 (9/10/2025); intraday high $340.56 |
| Latest quote | **$103.88 → –67.9% from peak** |
| Additional decline since 10/1/26 | –24.5% ($137.56 → $103.88) |

This is a **single-name event-risk profile masquerading as a mega-cap**. Realized single-day moves: **+36%** (9/10/25), **–11%** (12/11/25), **–8.4%** (6/11/26), **–7%** (2/5/26). Beta of 1.74 means a 20% SPY drawdown implies a ~35% ORCL drawdown on beta alone; the observed behavior (68.7% peak-to-trough on no broad-market crash) suggests **downside beta materially exceeds regression beta**. In a genuine risk-off event, this equity has no defensive characteristics.

A negative Sharpe of –0.071 over two years means holders were paid nothing for 59% volatility — the definition of uncompensated risk.

---

### 4. Downside Scenario Analysis: Revenue –20%

Base: FY26 revenue $67,357M, EBITDA $33,447M, gross margin 65.8%, opex $23.7B. A 20% decline takes revenue to **$53,886M (–$13,471M)**. Because 60%+ of cost of revenue is fixed cloud infrastructure (depreciation, power, leases), decremental margins on the way down are severe.

| Line item | Base FY26 | Scenario A: Managed (–30% decremental) | Scenario B: Severe (–50% decremental) |
|---|---|---|---|
| Revenue | 67,357 | 53,886 | 53,886 |
| EBITDA | 33,447 | **29,406** | **26,711** |
| Net debt / EBITDA | 3.72x | **4.07x** | **4.48x** |
| Forward D&A (see note) | 9,294 | ~17,000 | ~17,000 |
| EBIT | 24,153 | **12,406** | **9,711** |
| Interest (FY27 run-rate) | 4,599 | 5,700 | 5,700 |
| **Interest coverage** | 4.48x | **2.18x** | **1.70x** |
| FCF | –23,686 | deeply negative | deeply negative |

**Both scenarios land ORCL in high-yield credit territory.** At 1.7x coverage, a BB rating and re-pricing of the entire $156B debt stack follow immediately.

**The depreciation cliff is the underappreciated risk.** PP&E went $43.5B → $129.6B → **$161.8B** in twelve months. FY26 D&A of just $9.3B greatly understates steady-state depreciation on that asset base. At a ~6-year average life, D&A trends toward $20–27B/yr. Holding FY26 EBITDA constant, EBIT would fall from $24.2B to roughly **$6–13B — coverage of 1.1x–2.3x**. EBITDA-based leverage metrics mask this entirely; EBIT-based coverage does not. **This is why management and rating agencies focus on EBITDA while the equity and CDS markets focus on free cash flow — and why the two are diverging.**

**Mitigants (fairly stated):** RPO/backlog of **$664B** (up from $523B) is contractually committed and materially larger than the revenue base; a 20% revenue decline requires contract cancellation or counterparty failure, not merely weak demand. Customer-reimbursed capex of $20–25B in FY27 reduces net cash outflow. Q1 FY27 was operationally strong: revenue +30%, OCI +121%, record $23B operating cash flow (+184%).

**Unmitigated:** FY27 capex guidance of **$90–95B** against operating cash flow of ~$50B implies a **~$35–45B annual funding gap** that must be met with new debt or equity — at a moment when CDS is at record wides. This is reflexive: wider spreads raise the cost of the very financing the plan depends on.

---

### 5. Overall Financial Risk Rating: **HIGH** (approaching Critical)

| Dimension | Rating |
|---|---|
| Credit risk | **High** — BBB-/Baa2 negative, CDS pricing BB, Z-score in distress |
| Liquidity risk | **Moderate–High** — 1.12x current ratio is thin; model is market-access dependent |
| Market risk | **Critical** — 59% vol, 1.74 beta, 68.7% drawdown, negative Sharpe |
| FCF sustainability | **Critical** — negative FCF yield, capex at 83% of revenue, negative FCF margin |

**Cash runway:** FY26 negative FCF of $23.7B plus $6.0B of dividends and buybacks = **~$29.7B annual cash consumption** against $37.1B cash = **~1.25 years of runway without capital markets access**. Oracle is not liquidity-constrained *if* markets stay open; it is highly vulnerable if they close. That is a confidence-sensitive, not a balance-sheet-insolvent, credit — and confidence-sensitive credits reprice violently.

---

### 6. Key Red Flags

1. **Debt up 50% in one year ($104B → $156B) to fund zero-revenue-generating capex.** Capex of $55.7B in FY26 flips to $90–95B in FY27 guidance.
2. **FCF collapsed from +$11.8B (FY24) to –$23.7B (FY26).** FCF margin –35.2%; FCF yield –7.82%.
3. **Altman Z of 0.679 (0.68) — distress zone — and still ~1.42 even using market cap instead of book equity.**
4. **Interest coverage peaked in FY25 (4.94x) and is now declining (4.48x) despite 17% revenue growth.** Interest expense +24% yoy; capitalized interest will compound this as assets enter service.
5. **CDS at a record 356bp against a BBB- rating — a ~250bp mispricing that historically resolves in favor of the market.**
6. **Shareholder returns ($6.0B dividends + buybacks) funded entirely by debt while FCF is negative**, and now equity is being issued ($20B common+debt filing; diluted shares 2.914B → 3.000B) — paying dividends with borrowed money while simultaneously diluting.
7. **Gross margin erosion: 71.4% → 70.5% → 65.8%.** The business is structurally mixing toward lower-margin compute.
8. **Negative retained earnings (–$4.3B FY26, –$1.1B Q1 FY27)** — constrains dividend capacity under corporate law tests.
9. **Thin liquidity for the rating tier:** current ratio 1.12x, negative working-capital cushion relative to $156B debt.
10. **Customer concentration:** $664B RPO is a strength only if counterparties perform; a single AI-lab default converts a "backlog" story into a receivable and stranded-asset story.

---

### Data Gaps (explicitly flagged)

- **Debt maturity schedule unavailable** — only the ST/LT split (95% long-term, $7.6B current) is retrievable. The refinancing-cliff risk is therefore **unquantified** and is the single most important missing input.
- **Revolver size and covenant terms not disclosed** in available data — cannot test headroom against leverage covenants (likely EBITDA-based at 4.0–5.0x, which would be breached in Scenario B).
- **Sortino ratio** not computed by the tool; **CDS spread (356bp)** and rating actions sourced from press, not primary feeds.
- **FY26 total debt ($156,189M) does not reconcile to ST+LT borrowings ($129,541M)** — a ~$26.6B gap, likely data-center lease/finance obligations. The Q1 FY27 balance sheet reconciles exactly at $155,931M, so the discrepancy appears to be a classification issue, not an error in the debt level.
- **No segment-level margin disclosure** (OCI vs. SaaS) available to test the concentration and margin-mix thesis directly.
- Peer/sector multiple comparison not run; large-cap software peers (MSFT, GOOGL) hold net cash and are not valid leverage comparables.

**Bottom line:** Oracle is a **structurally sound franchise with a structurally broken financing model**. The operating business is growing 17–30% with a $664B backlog, but it is consuming $30–45B of external capital annually to do so. Coverage is thin, liquidity is thin, the Z-score is in distress, and the market is pricing the credit as high yield while agencies hold it one notch above. The equity reflects this: –68% from peak, 59% volatility, 1.74 beta, negative Sharpe. **Risk rating: HIGH.**
