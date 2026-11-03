# Fin Risk Analyst

- Symbol: CRWV
- Elapsed: 42.4s

---
# CRWV — CoreWeave, Inc. | Financial Risk Assessment
**As of:** Nov 2, 2026 (close $50.15, market cap $27.66B) | **Latest financials:** Q2 2026 (Jun 30, 2026, filed Aug 12, 2026); FY2025 10-K filed Mar 2, 2026

---

## 1. Credit Risk Assessment — **DISTRESS (market-priced)**

| Rating source | Rating | Note |
|---|---|---|
| S&P | **B+**, outlook revised to positive | Issuer credit rating; issue-level 'B' |
| Fitch | **BB+** | Senior secured (Jul 16, 2026) |
| Moody's | **A3** | Applied to *CoreWeave Compute Acquisition Co. VIII SPV* — project-finance debt, **not** corporate-level |
| 5Y CDS | **~1,038bp** (intraday >1,140bp) | >1,000bp = conventional distress threshold; +164% YoY |
| 9.75% 2031 bonds | **15.78% YTM** | Bond market pricing ~distressed |

**Critical divergence:** agency ratings (B+/BB+) lag the cash market. CDS at 1,038bp and bonds at 15.8% imply a materially weaker credit than B+. When a company's own unsecured yield is 15.8% and the Fed 5Y is 4.93%, marginal debt cost is ~3x the risk-free rate — this is the signature of a refinancing-constrained borrower.

**Leverage is extreme and rising fast.** Total debt + obligations reached **$51.6B** by Q2 2026 from $29.8B at FY2025 and $10.6B at FY2024 — a **4.9x increase in 18 months**. Book equity is only **$5.0B** against $72.0B liabilities.

---

## 2. Key Financial Risk Metrics

*(TTM = Q3'25→Q2'26, computed from reported quarters; latest balance sheet Jun 30, 2026)*

| Metric | Value | Assessment |
|---|---|---|
| Revenue (TTM) | $7,590M | +296% vs FY2024 |
| EBITDA (TTM) | $3,942M | 51.9% margin |
| **Net debt / EBITDA** | **11.5x** | Severe (FY25: 10.5x) |
| **Gross debt / EBITDA** | **13.1x** | Severe |
| Debt / equity (book) | 10.3x | Severity: equity is 6.5% of assets |
| Debt / assets | 67.0% | — |
| **Interest coverage (EBIT/Int.)** | **-0.03x** | EBIT is *negative* — no coverage |
| EBITDA / interest | 2.10x | Thin; interest = 24.7% of revenue |
| TTM interest expense | $1,874M | Up from $361M (FY24) — 5.2x |
| **Current ratio** | **0.46x** | Impaired |
| Quick ratio | 0.46x | No inventory to liquidate |
| Cash ratio | 0.31x | — |
| Working capital | **-$11,397M** | Structurally negative |
| Cash | $6,412M | vs $72.0B liabilities (8.9%) |
| Altman Z-Score | **-0.14** (book equity) / **~0.08** (at $27.7B market cap) | **Distress zone both ways** (Z<1.81); not a book-equity artifact |
| Piotroski F-Score | **5/9** | Moderate. Failed: positive ROA, no dilution, GM improvement, asset turnover |
| FCF (TTM, est.) | **≈ -$14.8B** | H1'26 alone: **-$10.5B** |
| FCF yield | -33.2% (FY25 basis); **≈ -54%** (TTM est.) | Deeply negative |

**Off-balance-sheet claim — the key gap:** per the 10-Q, drawn debt was **$35.07B** while total "debt and obligations" exceed $51B, and **$35.5B of leases had not yet commenced**. These are committed future obligations not fully reflected in leverage ratios. True total claim is roughly **$70B+**. This is the single largest under-appreciated risk.

---

## 3. Market Risk Profile

| Metric | Value |
|---|---|
| Annualised volatility (252d) | **98.1%** |
| Beta vs SPY (252d) | **3.71** |
| Beta (profile, alt. window) | 7.67 — **discrepancy flagged** |
| Max drawdown (252d) | **-63.65%** |
| Drawdown from ATH ($183.58, Jun 20 2025) | **-72.7%** |
| Sharpe ratio | **-0.41** (negative risk-adjusted return) |
| Sortino | Not computed by tool — **gap**; Sharpe<0 implies negative |

At ~98% vol and beta 3.7, CRWV delivers roughly **3.7x any market drawdown** — a 20% S&P decline implies ~-50% to -70% for CRWV on a beta basis. The October 2026 episode validated this: **-15.5% in a single session (Oct 14)** on 111M shares while the S&P fell 1.1%; **-41% from Oct 6 to Oct 23**. The equity is behaving as a levered credit instrument, not a growth stock.

**Trigger:** Microsoft's CFO (Oct 28) guided CY capex to ~$170B citing delayed third-party capacity deliveries (reported as a cut from $175B). Combined with CDS blowout and rising yields, this crystallized the customer-concentration + funding-dependency thesis.

---

## 4. Downside Scenario — Revenue -20%

Assumes $7,590M → $6,072M (-$1,518M), with ~30% of lost gross profit offset by variable cost flex.

| Line | Base | -20% Revenue | Delta |
|---|---|---|---|
| Revenue | $7,590M | $6,072M | -20% |
| EBITDA | $3,942M | **~$2,700M** | -32% |
| EBIT | -$49M | **~-$1,290M** | Deeply negative |
| Interest expense | $1,874M | $1,874M | Fixed (rises if refinanced at 15%) |
| **Net debt/EBITDA** | 11.5x | **~16.7x** | Covenant-zone |
| **EBITDA/interest** | 2.10x | **~1.44x** | Near breach of 1.5x-type tests |
| **EBIT/interest** | -0.03x | **~-0.69x** | Cannot service from operations |
| FCF | -$14.8B | **worse**, capex committed | — |

**The binding constraint is not earnings — it is the refinancing wall.** At -20% revenue, CRWV cannot service debt from EBIT and must fund interest from new borrowings or equity. With CDS at 1,038bp, the debt market is effectively closed at sane prices; **equity issuance becomes the only viable funding channel**, and shares outstanding already rose **435M → 551M (+27%) in two quarters** — dilution is compounding precisely when the equity is cheapest.

**Liquidity runway:** $6,412M cash ÷ $5,743M quarterly FCF burn = **~1.1 quarters (~3.4 months)**. The company survives only by continuous capital raising — Q2'26 alone added **+$16.5B of debt**. This is a going-concern dependent on capital-market access, not a self-funding business. A closed market is an existential, not a cyclical, event.

**Partial mitigant:** RPO/backlog of **$103.7B** (~14x TTM revenue), excluding >$25B of net new commitments added in early Q3'26. Contracted demand is genuinely large — but concentrated in a handful of hyperscalers whose own capex is being revised downward.

---

## 5. Overall Financial Risk Rating: **CRITICAL**

This is the highest-risk profile in the AI-infrastructure complex on every dimension simultaneously: leverage (13.1x gross), coverage (negative EBIT), liquidity (0.46x current ratio, ~3 months of cash runway), FCF (-$14.8B TTM), and market risk (98% vol, beta 3.7, -73% from high). The business has real gross margins (67%) and a large contracted backlog, so this is **not** a fraud or demand-collapse story — it is a **financing-structure solvency risk**. The equity is a call option on continued access to capital at non-distressed rates.

---

## 6. Key Red Flags

1. **$35.5B of leases not yet commenced** — unbooked obligations larger than all reported debt; disclosed leverage understates the true claim by roughly half.
2. **Terminal funding dependency** — cash covers ~3 months of burn; debt rose $16.5B in one quarter; 2031 bonds at 15.78% imply the market will not refinance on reasonable terms.
3. **CDS at 1,038bp** — the credit market is pricing distress while agencies still rate B+/BB+. Ratings are stale.
4. **Interest = 24.7% of revenue** — the cost of the capital stack is consuming the economics of the business.
5. **Negative EBIT (-$49M TTM) despite 52% EBITDA margin** — the entire EBITDA is consumed by $3,991M of D&A on a $63.3B PP&E base; cash earnings quality is poor.
6. **27% share dilution in two quarters** (435M → 551M) — Piotroski flags no-dilution as failed.
7. **Customer concentration / hyperscaler capex sensitivity** — the October drawdown was triggered by Microsoft's capex guidance; no CoreWeave-specific concentration figure was disclosed in available documents.
8. **Market risk is size-like microcap** — 98% vol, beta 3.7, -15.5% single-day moves on triple-average volume.

---

## Data Gaps (explicitly flagged)
- **Covenant terms and debt maturity schedule** — not available from tools. Given 16.7x leverage in a -20% scenario, whether covenants are maintenance-based (breach trigger) or incurrence-based (no trigger) is the single most decision-relevant unknown. **Must be verified from the 10-Q note on long-term debt.**
- **FCF TTM is derived/estimated** (Q3'25 quarterly cash flow not returned by the tool); H1'26 reported -$10.45B is the hard figure.
- **Sortino ratio** not computed.
- **Beta discrepancy:** 3.71 (252d via tool) vs 7.67 (profile) — using the lower, more conservative figure.
- No peer benchmarking performed (budget); Nebius/Iren cited only qualitatively in press as under similar pressure.
- Q3 2026 results (period ended Sep 30, 2026) not yet available in the dataset — the most recent hard financials are Jun 30, 2026, i.e. **four months stale relative to the October price collapse**.
