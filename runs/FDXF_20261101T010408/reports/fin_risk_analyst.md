# Fin Risk Analyst

- Symbol: FDXF
- Elapsed: 54.3s

---
## FDXF — FedEx Freight Holding Company | Financial Risk Assessment

**Company:** LTL freight carrier, spun off from FedEx Corp. effective June 1, 2026 (NYSE: FDXF). Revenue $8.8bn, 40,000 employees. Price $126.04, market cap $18.84bn. Note: fiscal year changed from May 31 to Dec 31 at separation; FY2026 (ended 5/31/26) is presented on a **carve-out/segment basis**, not a standalone basis — this distorts most ratios below.

---

## 1. Credit Risk Assessment

**Rating: Investment Grade — but at the lowest rung (BBB−)**

S&P assigned a **'BBB−' issue-level rating to the $3.7bn senior unsecured notes** (Feb 2026). Capital structure confirmed from filings:

| Instrument | Amount | Tenor |
|---|---|---|
| Senior unsecured notes | $3,700m | Priced Feb 2026 |
| Term Loan Facility | $600m | Drawn in full 27 May 2026 |
| 5-yr revolving credit facility | $1,200m | Jan 2026, **undrawn** |
| Operating/finance leases (implied) | ~$1,840m | — |
| **Total debt per balance sheet** | **$6,365m** | ST only $43m |

Proceeds funded a **~$4.1bn cash dividend to FedEx** — this is a deliberately levered recapitalization, not distress-driven borrowing.

**Critical split:** reported "total debt" of $6,365m includes ~$1.84bn of lease liabilities. **Financial (non-lease) debt is ~$4,527m**; financial net debt **$4,276m** vs. reported net debt $6,114m. Leverage looks materially better on a debt-only basis — I show both throughout.

**Key adjustment (most important item in this report):** FY2026 interest expense of **$57m is not a run-rate number**. It reflects only a partial period, as the notes and term loan were issued/drawn at the very end of FY2026 (notes Feb, TL drawn 27 May 2026). On ~$4.3bn of financial debt at ~5.2–5.4%, **pro-forma run-rate interest is ~$300–320m annually**, roughly 5.5x the reported figure. Interest coverage computed off the reported $57m (9.47x) **overstates debt-service capacity by ~5x**.

---

## 2. Key Financial Risk Metrics

| Metric | Reported | Adjusted / Pro-forma | Assessment |
|---|---|---|---|
| Debt / equity | −12.81x | n.m. | **Meaningless — equity is negative** |
| Debt / assets | 0.92x | 0.66x (financial debt) | High but lease-inflated |
| Net debt / EBITDA | 4.40x | 3.9x (adj. EBITDA); **2.8x** financial-debt only | Elevated; consistent with BBB− |
| Interest coverage (EBIT) | 9.47x (on $57m) | **~2.0x–3.0x** on ~$310m run-rate | Thin |
| Interest coverage (EBITDA) | — | ~4.5x–5.0x | Adequate |
| Current ratio | 1.52x | — | Adequate |
| Quick ratio | 1.52x | — | Adequate (no inventory) |
| Cash ratio | 0.25x | — | **Thin** |
| Cash | $251m | — | Very low for a standalone issuer |
| Working capital | $513m | — | Positive |
| Total equity | **−$497m** | — | Negative book equity |
| Altman Z-Score | **1.674 (Distress)** | **~3.25 (Safe)** on market-cap x4 | **See caveat** |
| Piotroski F-Score | **3 / 9 (Weak)** | — | Genuine deterioration |
| FCF (FY26) | **−$212m** | ~+$790m normalized | Transitional WC distortion |
| FCF yield | **−1.13%** | ~+4.2% normalized | — |

**Altman Z caveat (important):** The tool flags "Distress," but the score uses *book* equity in x4, which is −$497m post-dividend. Swapping in market capitalization ($18.84bn ÷ $7,381m liabilities = 2.55) raises Z from 1.674 to **~3.25 — the safe zone**. The "distress" reading is largely an artifact of the engineered negative equity, not operating insolvency. I weight Z lightly here.

**Piotroski:** 3/9, but four of the six failures (F5 lower leverage, F6 positive equity change, F7 no dilution, F3 ROA improvement) are separation artifacts. The genuine signals are F4 accruals quality (net income $655m vs. OCF $167m — poor conversion) and the ROA decline.

**Debt maturity / refinancing cliff: none near-term.** All facilities are 5-year (revolver with a one-year extension option), notes are long-dated, short-term debt is only $43m. **No maturity wall before ~2031.** This is the single strongest mitigant in the credit.

---

## 3. Market Risk Profile

| Metric | Value | Note |
|---|---|---|
| Annualised volatility | **64.79%** | Only ~107 trading sessions of history |
| Beta vs SPY | **−0.197** (profile: −7.34) | **Statistically meaningless** |
| Max drawdown | **−42.72%** | $188.46 (9 Jun) → $107.95 (21 Oct) |
| Sharpe ratio | **−0.336** | Negative |
| Sortino ratio | Not available | Negative Sharpe ⇒ negative Sortino |
| Price vs. peak | −33.1% | Peak close $188.46 |
| Price vs. first close | −15.7% | IPO $149.53 |

**Major data gap:** FDXF has traded only since June 1, 2026 (~5 months). Beta, volatility, and Sharpe are computed on an insufficient sample and the negative beta is a small-sample artifact — it should **not** be used for cost-of-equity or hedging decisions. Volatility is nonetheless directionally real: this is a newly independent, event-driven, high-operating-leverage equity in post-IPO price discovery, down 43% peak-to-trough in five months.

---

## 4. Downside Scenario: Revenue −20%

Base FY2026: revenue $8,795m; EBITDA $1,390m (15.8% margin); adj. EBITDA ~$1,550m; run-rate interest ~$310m; D&A $449m.

**Central case** (variable costs = 55% of revenue; −$1,759m revenue, +$967m cost relief):

| Item | Base | Revenue −20% |
|---|---|---|
| Revenue | $8,795m | $7,036m |
| EBITDA | $1,390m | **$598m** (6.5% margin) |
| EBIT | $941m | **~$149m** |
| Interest | ~$310m | ~$310m |
| EBIT interest coverage | ~3.0x | **~0.5x — breach** |
| EBITDA coverage | ~4.5x | ~1.9x |
| Net debt / EBITDA (lease-incl.) | 4.4x | **10.2x** |
| Net debt / EBITDA (financial only) | 2.8x | 7.2x |
| Net income | +$655m | **negative ~$120m** |
| FCF | −$212m | **−$400m to −$500m** |

**Severe case** (decremental margin at FY2026's *realized* rate — the company turned a **1.1% revenue decline into a 58.6% operating income decline**, implying decremental margins >100%): a 20% revenue loss drives EBITDA to **zero or materially negative (−$700m to −$1,200m)**, i.e. equity wipeout and restructuring.

**Liquidity through the downside:** $251m cash + $1.2bn undrawn revolver = **~$1.45bn total liquidity** vs. a $400–500m annual burn → ~3 years of runway. **But covenant tests on the revolver (likely a net-leverage maintenance test in the 4.0–4.5x range) would bind long before cash ran out**, at roughly a 12–15% revenue decline. Exact covenant thresholds are **not disclosed in available data — flagged as a gap.**

**Conclusion:** the balance sheet survives a 10% decline; a 20% decline breaches covenants and forces a waiver or equity raise. The company has essentially **no capacity to self-fund through a full freight recession.**

---

## 5. Overall Financial Risk Rating: **HIGH**

Static leverage (2.8x financial / 4.4x lease-inclusive net debt, ~4.5x EBITDA coverage, no maturities before 2031, $1.2bn undrawn revolver, BBB−) is genuinely **moderate**. What drives the rating to High is **the sensitivity of that structure to volume**, evidenced rather than hypothetical:

- Revenue −1.1% → GAAP operating income **−58.6%** ($1,348m → $616m segment basis; $540m carve-out).
- Adjusted operating income −25.6% on flat revenue.
- Operating margin compressed 16.7% → 7.0% (adjusted 12.6%).
- Negative book equity of −$497m, negative reported FCF, $251m cash.
- Equity down 43% peak-to-trough in five months.

The business is a high-fixed-cost LTL network with a thin equity cushion — precisely the profile that fails in a prolonged downturn, even though it is investment grade today.

---

## 6. Key Red Flags

1. **Extreme operating leverage** — a 1% revenue miss costs ~50% of operating income. This is the dominant risk.
2. **Negative shareholders' equity (−$497m)** from the $4.1bn debt-funded dividend to FedEx; retained earnings −$509m. Debt/assets 0.92x.
3. **Interest coverage overstated ~5x** if the reported $57m expense is taken at face value; run-rate ~$300–320m.
4. **Negative FCF (−$212m; yield −1.13%)** and OCF of only $167m against net income of $655m — weak accruals quality.
5. **Thin cash ($251m; cash ratio 0.25)** for a newly independent issuer with no FedEx cash-pooling backstop.
6. **Dis-synergy / stranded cost risk** — Transition Services Agreement with FedEx runs only up to 2 years; company is still absorbing separation costs (Q4 FY26 GAAP operating income fell 66.9% vs. adjusted −23.9%). Margin may deteriorate further as TSA support rolls off.
7. **Piotroski 3/9**; Altman Z 1.674 as computed.
8. **Equity event risk** — 42.7% max drawdown, 65% vol, volatile post-spin float; FedEx retains **up to 19.9%**, an overhang.
9. **Valuation cushion is thin** — EV ~$25.0bn = ~16x adjusted EBITDA and ~18x reported EBITDA, leaving room for further de-rating if volumes soften.

## 7. Mitigants

- **BBB− investment grade** with $3.7bn notes + $600m term loan; **$1.2bn undrawn revolver**; **no maturities before ~2031** — no refinancing cliff.
- **Q1 FY2027 (qtr ended 8/31/26) showed recovery**: operating income $253m, margin **10.4%** (vs. 12.8% prior year), EPS $1.49 vs. $1.38 consensus — a clear sequential improvement from FY2026's 7.0%.
- Q4 FY2026 revenue +4.8%; revenue per shipment +11.5%, yield +8.2% — pricing discipline intact.
- Normalized FCF is likely **~$790m** once the ~$1.0bn non-recurring working-capital build is excluded (net receivables jumped $132m → $1,172m as the company began carrying its own AR), implying a **~4.2% FCF yield** and ~7.6 years of FCF to retire net debt.

---

## Data Gaps & Caveats (explicit)

- **Balance sheet internal inconsistency:** FY2026 shows **PP&E net = $0** (vs. $4,132m prior year) while total assets are $6,884m, and **total liabilities ($7,381m) exceed total assets**. A 40,000-employee national LTL network cannot have zero PP&E — this is a carve-out/restatement artifact. All ratios derived from this balance sheet (Z-score, debt/assets, equity/assets) are **indicative only**.
- **EBIT ($941m) ≠ operating income ($540m)** in the same filing, a ~$401m unexplained non-operating gap; net income ($655m) exceeds operating income. Adjusted EBITDA (~$1,550m) is my derivation, not a reported figure.
- **No covenant thresholds, maturity-by-year schedule, or CDS spreads available.** Credit ratings sourced from S&P commentary, not a primary ratings report.
- **True LTL peer comparables unavailable** — the peer tool returned unrelated Industrials mega-caps (SpaceX, GE, CAT, RTX, UNP). ODFL/XPO/SAIA/ArcBest multiples could not be obtained, so no peer-relative leverage or valuation benchmark is offered.
- **Market-risk statistics rest on ~107 trading days**; beta and Sharpe are not decision-grade.
- Sortino ratio not provided by tools.
