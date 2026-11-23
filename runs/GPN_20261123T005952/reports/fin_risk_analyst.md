# Fin Risk Analyst

- Symbol: GPN
- Elapsed: 90.1s

---
## GPN — Financial Risk Assessment

**Critical framing note:** Global Payments closed the $24.25B Worldpay acquisition and the $13.5B Issuer Solutions sale to FIS during this window. **FY2025 annual figures are a pre-deal, ex-Issuer stub and are not representative.** The live risk profile must be read off the Q3 2026 balance sheet and TTM P&L, which I have reconstructed below. Where the two diverge sharply, I flag it — the divergence is itself the story.

---

### 1. Credit Risk Assessment — **Investment Grade (low BBB tier), but deteriorating**

S&P affirmed **BBB / stable** (April 2025) on the Issuer Solutions disposal, and rated GPN's new senior unsecured notes **BBB-** — the bottom rung of IG. Management explicitly targets maintaining IG and returning to **3.0x adjusted net leverage within 18–24 months**. That commitment is credible but currently unmet, and the cushion to a downgrade is thin.

The core credit problem: **GAAP EBIT coverage has collapsed below 1.0x.** TTM EBIT is ~$976M against ~$1.0–1.1B of annualized interest. The company services debt entirely on the back of a $3.5B/yr D&A add-back — which is overwhelmingly amortization of acquired intangibles, not maintenance capex. Interest is genuinely covered on a cash basis (~3.6x), but there is no earnings-based coverage left. Any impairment or margin shock transmits straight to the equity.

### 2. Key Financial Risk Metrics

| Metric | FY2025 (pre-deal) | Q3'26 TTM (post-deal) | Assessment |
|---|---|---|---|
| Total debt | $21.87B | $23.70B | ↑ |
| Cash | $8.34B | $5.57B | ↓ (deal funding) |
| Net debt | $13.53B | $18.13B | **+$4.6B** |
| Net debt / EBITDA | 3.93x | **4.56x** (3.9x on annualized Q3) | Elevated; target 3.0x |
| EBITDA / interest | 5.3x | **3.6x** | Adequate |
| EBIT / interest | 3.12x | **~0.9x** | **Fails** |
| Debt / equity | 0.92x | 0.99x | Stable |
| Debt / assets | 0.41x | 0.38x | OK |
| Current ratio | 1.69x | **0.82x** | **Breach of conventional liquidity test** |
| Cash ratio | 1.12x | 0.41x | Weak |
| Working capital | +$5.15B | **–$2.47B** | Reversed |
| Altman Z-Score | 1.02 (Distress) | **~0.5 (est.)** | Indicative only |
| Piotroski F-Score | 6 / 9 (Moderate) | n/a | Leverage & turnover flags |
| Goodwill+intangibles | 40% of assets | **73% of assets** ($45.6B) | Impairment exposure |
| Tangible book equity | — | **≈ –$21.6B** | Negative |

**Z-Score caveat:** Altman is structurally hostile to acquisition-heavy payment processors (X4 uses book equity, X5 penalizes asset-heavy roll-ups). Treat the 1.02 and my ~0.5 pro-forma estimate as a *direction*, not a calibrated default probability. The F-Score's two failures are exactly the ones that matter: **F5 (leverage increased)** and **F9 (asset turnover deteriorated)**.

**Liquidity caveat:** the 0.82 current ratio overstates stress because a large slice of current liabilities is merchant settlement float, matched by settlement assets. But it also means reported cash is not freely available — the $5.57B is not a deleveraging war chest.

### 3. Market Risk Profile — **high vol for a payments name, no risk-adjusted compensation**

- **Annualized volatility (3Y): 38.7%** — well above what a BBB-rated, fee-based processor should carry.
- **Beta: 1.005 vs SPY (3Y)**, but the company profile shows **0.816 (5Y)**. Sensitivity is *rising*, not stable — the market is repricing GPN as a levered financial rather than a defensive tech name.
- **Max drawdown (3Y): –53.95%** — roughly double a typical broad-market drawdown. This is a stock that loses more than the market in a selloff despite a beta near 1.
- **Sharpe ratio (3Y, rf=0): 0.103** — effectively zero risk-adjusted return. Investors have been paid nothing for 39% volatility.
- Beta/vol sourced from `calculate_price_volatility` (1095-day window, SPY benchmark); the 5Y beta is from the company profile — the two are not reconciled and the gap is itself informative.

### 4. Downside Scenario Analysis — Revenue –20%

TTM revenue $11.49B, TTM EBITDA $3.98B (34.6% margin), net debt $18.13B, annualized cash interest $1.10B, capex ~$0.94B/yr.

A 20% revenue decline (–$2.30B) on a net-revenue payments model carries high decremental margins (40–55%), since interchange pass-through flexes but the technology and sales base does not:

| Decremental margin | EBITDA | Net debt/EBITDA | EBITDA/interest |
|---|---|---|---|
| 35% | $3.17B | 5.7x | 2.9x |
| 45% (base) | $2.94B | **6.2x** | 2.7x |
| 55% | $2.71B | 6.7x | 2.5x |

**Consequences:** free cash flow falls to roughly $1.0B pre-working-capital — enough to cover the ~$266M dividend but not the ~$1.2B+/yr buyback program that has been running. Deleveraging stalls outright, net leverage sits at 5.7–6.7x for the duration of the downturn, and a **downgrade to BB+/sub-investment grade becomes the base case**, raising refinancing costs precisely when the maturity wall bites. The equity, already carrying –$21.6B of tangible book, absorbs the full impact; a further goodwill impairment (73% of assets) is highly likely under this scenario, and Q1 2026 already produced a **–$1.80B net loss** in a single quarter from exactly this mechanism.

### 5. Overall Financial Risk Rating — **HIGH**

Not Critical: the business generates real cash, interest is covered on a cash basis, ratings are IG, and the maturity ladder is reasonably distributed (1.200% notes due Mar-2026 already refinanced in March 2026 with $1.0B of new BBB- notes; $750M 2.150% due 2027; $2.0B 1.500% convertibles due 2031). But leverage is 4.56x *before* any stress, GAAP coverage is below 1x, liquidity has inverted, and 9M 2026 free cash flow was **negative $516M** while the company repurchased $1.24B of stock. That is balance-sheet-funded.

### 6. Key Red Flags

1. **Negative FCF through 9M 2026 (–$516M)** against $1.24B of buybacks and $200M of dividends. Q3 alone burned $393M on a –$1.37B working capital swing. Partly settlement-timing noise, but the direction is wrong.
2. **Tangible book equity of –$21.6B.** Equity is 100% goodwill and intangibles. There is no tangible solvency buffer.
3. **GAAP EBIT/interest ≈ 0.9x.** Debt service depends on a non-cash D&A add-back.
4. **Leverage 4.56x vs. 3.0x target** — requires ~$1.5B of net debt reduction, but FCF is currently negative.
5. **Q1 2026 net loss of –$1.80B**, retained earnings fell from $5.94B to $4.23B. Recurring impairment risk on a 73%-intangible balance sheet.
6. **Sharp liquidity reversal:** working capital +$5.15B → –$2.47B; current ratio 1.69x → 0.82x; short-term debt rose from $925M (Jun-26) to $2.62B (Sep-26).
7. **Stock down 54% peak-to-trough with zero Sharpe** — the market has already voted on the deal's risk, and the 5Y→3Y beta migration (0.816→1.005) confirms de-rating.

### Data Gaps (explicitly flagged)

- **Covenant levels and headroom** — not available from the tools. GPN's revolver carries a leverage test (typically 3.5–4.0x for IG issuers); at 4.56x reported / ~3.5x adjusted, headroom is thin and unquantified.
- **Full debt maturity ladder by year and the revolver capacity** — only individual note issues confirmed via filings search; no complete schedule.
- **Moody's rating and CDS spreads** — not retrieved.
- **Peer benchmarking** — not run (budget); no relative leverage/coverage context.
- **FY2025 interest expense ($649.6M) looks understated** relative to ~$19B average debt (implies 3.4%); Q3 2026's $276M quarter (≈4.9%) is the more realistic run-rate, and I used that.
- **Reported EBIT and operating income disagree** in the source data (FY2025: $2.03B vs $1.47B), so tool-computed interest coverage of 2.27x differs from my figure; I have used both and disclosed the range.
- Quarterly gross profit less SG&A does not reconcile to reported operating income, implying unallocated charges; downside sensitivities are therefore modeled off EBITDA margin, not line-item build-up.

**Bottom line:** GPN is an IG credit with sub-IG *characteristics* post-Worldpay — the rating rests on management's deleveraging promise, not on current metrics. The single most important thing to monitor is whether reported (not adjusted) net leverage breaks below 4.0x over the next four quarters. If it does not, the downside case is a downgrade, a buyback suspension, and further multiple compression.
