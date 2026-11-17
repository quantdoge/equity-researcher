# Fin Risk Analyst

- Symbol: ASTS
- Elapsed: 54.6s

---
## AST SpaceMobile, Inc. (ASTS) — Financial Risk Assessment
*As of latest data: balance sheet 30-Sep-2026; price $28.58 (16-Nov-2026 close)*

**Business context:** pre-scale satellite-direct-to-cell operator. TTM revenue $142.9M, TTM net loss $628.3M. This is a **capital-funding risk story, not a demand story** — the entire risk assessment turns on whether ASTS can fund a ~$2B/yr satellite build before revenues scale.

---

## 1. Credit Risk Assessment

**Rating: SUB-INVESTMENT GRADE (speculative), borderline CCC/B- on trajectory.** No public issuer rating or CDS spread was retrievable — **data gap**; rating is inferred from credit metrics.

The tension: the **income statement is distress-grade, the maturity wall is not.** Debt ballooned from $2.24B (Dec-25) to $4.12B (Sep-26) via convertible notes. But $4,083.7M sits in long-term debt and only $8.8M is short-term — the new converts mature in 2032/2034. **There is no refinancing cliff before 2032.** That single fact is what keeps this out of "Critical."

| Credit metric (TTM to Q3'26) | Value | Read |
|---|---|---|
| Revenue | $142.9M | Inflecting but immaterial vs. cash burn |
| EBIT / EBITDA | **-$734.5M / -$655.4M** | Deeply negative |
| Interest expense (TTM) | $83.3M (Q3'26 annualised ~$121M) | **11x increase** from Q4'25 ($2.7M) |
| Interest coverage (EBIT/int.) | **-8.8x** | Fails, structurally |
| Net debt / EBITDA | **n.m.** (both negative) | *Tool returned 0.26 — a sign artifact; disregard* |
| Net debt / TTM revenue | **9.2x** | Gross debt / revenue 28.8x |
| Debt / equity | **1.90x** (0.94x at FY25) | Leverage roughly doubled in 9 months |

**Distress scorecard:**
- **Altman Z-Score: 0.605 → Distress zone.** Critically, I re-ran x4 on market equity ($8.58B basic): Z ≈ **1.17** — still deep in distress. Even at the profile's $11.67B fully-diluted cap, Z ≈ 1.58, below the 1.81 floor. *The distress conclusion is not an artifact of using book equity.*
- **Piotroski F-Score: 5/9 ("Moderate") — but this overstates quality.** The 5 points come almost entirely from accounting-trend items (ROA improvement, accruals, gross margin, asset turnover) that are flattered by revenue growing from a near-zero base. The four *diagnostic* tests all fail: **F1 positive ROA = 0, F2 positive operating CF = 0, F5 lower leverage = 0, F7 no dilution = 0.** A company with negative ROA, negative OCF, rising leverage and 17% annual dilution is not a "moderate" credit.

---

## 2. Key Financial Risk Metrics Table

| Metric | Value | Assessment |
|---|---|---|
| **Leverage** | | |
| Total debt | $4,118.7M | +84% since Dec-25 |
| Net debt | $1,319.8M | Positive net debt from zero 9 months ago |
| Debt / equity | 1.90x | Elevated & rising |
| Debt / assets | 0.61x | Half the balance sheet is debt |
| **Coverage** | | |
| Interest coverage | -8.8x | Not serviceable from EBIT |
| Cash interest cover | Negative | Funded from cash pile |
| **Liquidity** | | |
| Cash + ST investments | **$2,798.9M** ($3.2B incl. restricted per mgmt) | Genuinely strong |
| Current ratio / quick ratio | **13.65x / 13.26x** | Anomalously high — cash-heavy, not operating strength |
| Working capital | $2,851M | Asset is cash, not receivables |
| Cash / total liabilities | 0.61x | Adequate near-term |
| **Cash runway (TTM FCF -$1,799.4M)** | **~1.6 years (~6.2 qtrs)** | Exhaustion ~H1-2028, *before* new financing |
| **Runway at Q4'26 guided run-rate (~$550M/qtr)** | **~5.1 quarters (~Q1-2028)** | Deteriorating, not stable |
| **Solvency** | | |
| Altman Z | **0.605 (Distress)**; 1.17 market-adjusted | Distress on any basis |
| Piotroski F | 5/9 (diagnostics all fail) | Overstated |
| Retained earnings | -$1,385.9M | Accumulated deficit widening $550M+/yr |
| Equity / assets | 31.9% (47.7% at FY25) | **Falling despite raising capital** |

**FCF sustainability — the core problem:**

| | FY2023 | FY2024 | FY2025 | TTM Q3'26 |
|---|---|---|---|---|
| Operating CF | -$148.9M | -$126.1M | -$71.5M | -$249.5M |
| Capex | -$118.8M | -$174.1M | -$1,064.7M | **-$1,549.9M** |
| **FCF** | **-$267.7M** | **-$300.3M** | **-$1,136.3M** | **-$1,799.4M** |
| Capex / revenue | n.m. | 39x | 15x | **10.8x** |

**FCF yield: -21.0%** on basic market cap ($8.58B); tool reports **-15.53%** on a $7.32B cap. *(Market cap is inconsistent across sources — see gaps.)* Cash burn has **accelerated 6.7x in two years** and is driven by capex, not opex: operating cash burn is only $250M TTM while capex is $1.55B. Management guides Q4'26 capex of **$400–500M** and adj. opex of $130–140M, implying continued ~$550M/quarter outflow.

---

## 3. Market Risk Profile

| Metric | Value | Interpretation |
|---|---|---|
| Annualised volatility (3y) | **101.8%** | Extreme; ~4x market |
| Beta vs SPY | **2.65** (profile: 2.85) | A 20% market drawdown implies ~55% |
| Max drawdown (3y) | **-78.5%** | Full-scale de-rating already occurred once |
| Sharpe (0% rf) | 0.535 | On a realistic ~4.75% rf (2Y), excess Sharpe ≈ **0.48** — mediocre |
| Recent drawdown | **-56.8%** in 10 weeks ($66.12 → $28.58) | Ongoing, not historical |

The stock is **in an active drawdown right now**, not a recovered one: -10.0% on 9-Oct, -15.4% on 5-Nov, with 34M and 22M share volume spikes. At $28.58, the equity sits **64% below the $79.57 conversion price** of the $1.0B 2034 converts and **36% below the $44.98 capped-call strike**. Translation: **the convertible equity-hedge has failed.** The converts behave as straight debt, and the dilution that was supposed to be avoided is now the *more expensive* path.

---

## 4. Downside Scenario Analysis

**Scenario A — Revenue -20% (standard stress). Largely immaterial.** A 20% hit to $142.9M revenue = -$28.6M of gross cash. Against a $1.8B annual burn, revenue variance is **statistically irrelevant** to solvency. This is the key analytical point: *for ASTS, revenue risk ≠ financial risk. Funding risk is the risk.* I therefore stress the funding channel instead.

**Scenario B — Capital markets close / equity stays below $45 for 4 quarters.**
- Convertible access is impaired (already deep out-of-the-money), leaving straight debt at 10Y ~5.13% + high-yield spread ≈ **8–9% all-in**, or equity at $28.58.
- To fund 2027's ~$2.0B burn, an equity raise at $28.58 requires **~70M shares (+23% dilution)**. A raise at $15 (a further -48%) requires **~133M shares (+44%)**. This is a **reflexive death-spiral**: lower price → more shares → lower price.
- Interest expense, already annualising ~$121M and up 11x in three quarters, would compound: each $1B of converts at 4.25% adds ~$43M/yr of cash interest, pushing interest coverage further negative.

**Scenario C — Satellite deployment slips one year** (the operational risk that matters). Cash of $2.80B at ~$550M/quarter exhausts by **~Q1-2028**. Any slip beyond that forces a raise into a distressed tape, or asset-level/joint-venture financing at punitive cost. **No covenant headroom data is available — data gap** — so I cannot rule out an acceleration trigger inside the convert indentures, though converts typically carry no maintenance covenants.

**Scenario D — Forced conversion / cash repayment.** Maturities in 2032/2034 mean **no near-term cliff**, but also that ~$4.1B of principal must eventually be repaid in *cash* unless the stock recovers above $79.57. That's a ~$4B refinancing against a business that must be generating >$500M EBITDA by then. Plausible only on successful execution.

---

## 5. Overall Financial Risk Rating: **HIGH**

Not Critical, because: (a) $2.80B of cash and a 13.7x current ratio fund ~5–6 quarters of operations; (b) **zero maturities before 2032** — no refinancing cliff; (c) revenue is inflecting ($4.4M FY24 → $70.9M FY25 → $150–200M FY26E) and gross margin turned positive (+40.2% in Q3'26).

But firmly High, because every credit metric is deteriorating simultaneously: leverage doubled, interest expense up 11x, FCF burn at -$1.8B and accelerating, Altman Z in distress on any equity basis, equity down 19% in 2026 *despite* raising ~$1.1B, and 17.2% share count growth in three quarters.

**Upgrade to Moderate requires:** positive operating cash flow, or capex guided below ~$1B/yr, or the stock recovering above the $44.98 capped-call strike.
**Downgrade to Critical if:** cash falls below ~$1.2B without committed financing, the Q4 capex guide is exceeded, or deployment slips a full year.

---

## 6. Key Red Flags

1. **Leverage tripled in three quarters** — debt $2.24B → $4.12B; interest expense $2.7M → $30.3M/quarter. Growth is being financed with debt at escalating cost.
2. **Systematic dilution** — shares 256.0M (Q4'25) → 290.7M → 299.1M → 300.1M. **+17.2% in nine months**, and F-Score F7 = 0. Per-share value is being structurally eroded.
3. **Cash burn accelerating, not moderating** — FCF -$268M → -$300M → -$1,136M → -$1,799M. Capex at **10.8x revenue.** Q4'26 capex guided *up* to $400–500M.
4. **Altman Z of 0.605, and only 1.17 market-adjusted** — distress isn't a book-equity artifact.
5. **Convertible note equity hedge is dead** — stock at $28.58 vs. $44.98 cap-call and $79.57 conversion prices. Converts now function as expensive straight debt with a $4B bullet in 2032/2034.
6. **Shareholders' equity falling while raising capital** — $2.66B → $2.16B during 2026; retained deficit -$1.39B. Losses are outrunning capital raised.
7. **Extreme market risk** — 101.8% vol, beta 2.65, -78.5% max drawdown, and -56.8% in the last 10 weeks. A 20% market drawdown plausibly costs shareholders >50%.

---

## Data Gaps & Caveats (explicitly flagged)

- **Market cap is inconsistent across sources:** $7.32B (FCF-yield tool), $8.58B (300.1M basic shares × $28.58), $11.67B (company profile, implying ~408M shares — likely fully diluted/as-converted). FCF yield therefore ranges **-15.4% to -21.0%**. I have used basic where a single figure was required and shown the range.
- **No credit rating or CDS spread** retrievable — credit rating assigned by inference.
- **Cash differs by source:** $2,798.9M (balance sheet, cash + ST investments) vs. **$3.2B** cited by management (includes restricted cash). Runway math above uses the conservative $2.80B.
- **Debt maturity schedule by tranche and covenant package not disclosed** in available data. Maturities of 2032 (4.25% converts, $400M) and 2034 (1.625% converts, $1.0B) come from press reports; a 2.25% series was also priced but its size/maturity could not be verified (SEC filing returned HTTP 403). Note total debt of $4.12B exceeds the identified tranches, so **~$1.5B+ of the stack is uncharacterised.**
- **FY2025 net debt/EBITDA of 0.26 (tool output) is a mathematical artifact** of negative net debt and negative EBITDA — not a usable leverage reading.
- **Interest coverage discrepancy:** tool reports -7.98x on FY25 (EBIT -$421.0M vs. interest $36.1M computes to -11.7x). I report the TTM figure (-8.8x) computed directly and flag the inconsistency.
- **No peer benchmarking performed.** ASTS is classified under "Communication Services / Telecommunications Services," which maps to AT&T/Verizon — a meaningless comparison for a pre-scale satellite venture. Peer multiples unavailable and, in my judgement, not informative.
