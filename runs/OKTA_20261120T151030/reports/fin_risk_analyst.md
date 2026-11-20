# Fin Risk Analyst

- Symbol: OKTA
- Elapsed: 59.9s

---
# OKTA — Financial Risk Assessment

**Price basis:** $201.82 (20-Nov-2026); market cap ~$33.7B (~167M shares). *Note: an earlier price pull through 10-Mar-2026 showed $79.61 — the stock has re-rated +154% since; all ratios below use the current cap.*

---

## 1. Credit Risk Assessment

**Rating: Investment Grade (in substance) — net-cash, effectively debt-free issuer**

Okta is one of the least levered mid-cap software issuers in the market. Debt has been retired almost entirely:

| | FY2024 | FY2025 | FY2026 | Q2 FY2027 |
|---|---|---|---|---|
| Total debt | $1,297M | $952M | $422M | **$53M** |
| Cash & ST inv. | $2,202M | $2,523M | $2,553M | $2,299M |
| Net cash | $905M | $1,571M | **$2,131M** | **$2,246M** |

The legacy 0.375% June-2026 convertibles and the 2028 notes have been settled (long-term debt = $0 in the latest quarter). **The refinancing cliff has been eliminated** — the entire remaining $53M appears to be short-term/lease-type obligations. Debt/equity 0.06, debt/assets 0.04, net debt/EBITDA **−6.0x** (net cash). Interest coverage **37.3x** (tool; on reported EBIT $259M / interest $4M it is ~65x — I use the more conservative tool figure). With no material funded debt, there are no maintenance covenants exposed to a revenue shock.

*Caveat:* no public rating was retrievable for the residual debt, and no CDS exists — data gap, but economically irrelevant at this leverage.

**Altman Z-Score: 1.681 — "Distress" zone, but a false positive.** The score is dragged down by x2 = −0.2644 (retained earnings/total assets, i.e. the $2.38B accumulated deficit created by years of SBC-funded losses) and thin x3 (0.0267). Recomputing x4 on market rather than book equity ($33.7B ÷ $2.711B liabilities = 12.4x instead of 2.58x) lifts Z to **≈7.6 — deep in the safe zone.** For an asset-light software issuer with net cash, the book-equity Z-score is structurally misleading.

**Piotroski F-Score: 8/9 — Strong.** Only miss is F7 (no dilution) — see red flags.

---

## 2. Key Financial Risk Metrics

| Metric | Value | Read |
|---|---|---|
| Debt / equity | 0.06 | Very low |
| Net debt / EBITDA | −6.0x | Net cash |
| Interest coverage | 37.3x | Trivial debt service |
| Altman Z (book) / (market-equiv.) | 1.68 / ~7.6 | Distress / Safe |
| Piotroski F | 8 / 9 | Strong |
| Current ratio | 1.36 | Adequate* |
| Quick ratio | 1.36 | No inventory |
| Cash ratio | 1.00 | Cash ≥ all current liabilities ex-deferred rev. |
| Working capital | $919M | Positive |
| Assets / liabilities | 3.58x | Conservative |
| Equity / assets | 0.72 | Solid |
| FCF (FY26) | $863M | 29.6% margin |
| FCF yield | 2.39% (tool) / 2.56% (current cap) | Low-ish vs. history |
| Cash runway | N/A — FCF positive | ~4.5 yrs of opex on cash even at zero revenue |

\*Current liabilities ($2.554B) are dominated by **deferred revenue**, which is settled in service, not cash — true liquidity is materially better than 1.36x implies.

**FCF sustainability — good, but quality is the issue.** FCF rose $63M → $488M → $730M → $863M (FY23–FY26); margin 3.4% → 21.6% → 28.0% → **29.6%**. Latest quarter: FCF $233M (28.9% margin). *However*, FY26 FCF embeds a **$544M SBC add-back = 18.6% of revenue**: SBC-adjusted FCF is only **~$319M (10.9% margin, ~0.95% yield)**. Cash generation is real and improving, but roughly 63% of it is compensation expense paid in stock.

---

## 3. Market Risk Profile

| Metric | Value |
|---|---|
| Annualised volatility (756d) | **58.65%** |
| Beta vs SPY (computed) | **1.241** |
| Max drawdown (3y) | **−50.57%** |
| Sharpe (0% rf) | 1.068 |
| Sharpe at ~4.7% rf | ~0.99 |
| 1-day 95% VaR (parametric) | ~6.1% |
| 1-day 99% VaR | ~8.6% |

**High-beta, high-vol equity.** Realised vol of ~59% is ~3.5x the index; beta 1.24 means a 20% market drawdown plausibly costs ~25–30%. Documented single-session gaps: −15% (28-May-25), −12% (20-Feb-26), −8% (29-Aug-24); upside gaps +9.4% (19-Nov-26) and +7% (5-Mar-26). Earnings-gap risk of 7–15% is structural — the equity, not the balance sheet, is where OKTA's risk lives.

*Sortino ratio unavailable from tools (gap); beta conflict flagged — vendor profile shows 0.733 vs 1.241 computed. I rely on the computed 1.241, which is more consistent with observed gap behaviour.*

**Rate backdrop:** 2Y 4.74% / 10Y 5.13%, 2s10s +39bp (no inversion). A 5%+ long end is a persistent multiple headwind for a ~60x earnings, 10%-growth asset — the dominant driver of the 3-year 50% drawdown.

---

## 4. Downside Scenario: Revenue −20%

Base: FY26 revenue $2,919M, gross margin 77.4%, opex $2,109M, cash $2,299M, debt $53M.

| Line | Base FY26 | Stress (−20% rev, opex −12%) | Severe (−20% rev, opex flat) |
|---|---|---|---|
| Revenue | $2,919M | $2,335M | $2,335M |
| Gross profit (77.4%) | $2,258M | $1,807M | $1,807M |
| Opex | $2,109M | $1,856M | $2,109M |
| EBIT | $149M | **−$49M** | **−$302M** |
| EBITDA | $355M | ~$47M | ~−$206M |
| Net cash | $2,246M | $2,246M | $2,246M |
| Net debt/EBITDA | net cash | net cash | net cash |
| FCF (est.) | $863M | ~$270M | ~$150M |
| Interest coverage | 37x | ~15x (interest income offsets) | ~5x |

**Conclusion: the company survives a 20% revenue decline without any financing need.** Even the severe case leaves net cash intact, coverage above 5x, and no covenant exposure. The real stress transmission is not solvency — it is (a) **goodwill impairment**: $5,567M of goodwill/intangibles (61% of assets, 80% of equity, largely Auth0), which a −20% revenue trajectory would likely write down, hitting book equity though not cash; and (b) **deferred-revenue unwind**: a 20% billings decline could drain $300–400M of working capital in one year — absorbed by a $2.3B cash pile. Downside to the *equity* on this scenario, at ~60x earnings, is plausibly **−50% to −60%** — consistent with the observed 3-year drawdown.

---

## 5. Overall Financial Risk Rating: **MODERATE**

- **Balance-sheet / credit risk: LOW** (net cash 6.7% of market cap, 37x coverage, no maturities, no covenants)
- **Liquidity risk: LOW** (cash ratio 1.0, $919M WC, FCF positive every year since FY23)
- **Business / earnings risk: MODERATE–HIGH** (growth 28% → 18% → 11.8% → guided 10–11%)
- **Equity / market risk: HIGH** (59% vol, beta 1.24, −50.6% drawdown, earnings gap risk)

OKTA cannot be meaningfully impaired by its capital structure; it can be impaired by a growth stall. Composite: **Moderate**.

---

## 6. Key Red Flags

1. **Goodwill concentration** — $5.57B (61% of assets, 80% of equity) from the Auth0 deal; impairment risk material if growth settles into high single digits.
2. **FCF quality** — SBC $544M (18.6% of revenue) is 63% of reported FCF; true cash economics are ~$319M, ~0.95% adjusted yield.
3. **Dilution history** — shares 158.0M → 175.9M (FY23–FY26), +3.7%/yr; F7 of Piotroski fails. Buybacks ($445M in H1 FY27) now offset this, and were executed at low prices — a positive.
4. **Growth deceleration** — +28.4% → +18.1% → +11.8% → guide +10–11%; a 20% shock is plausible in a security-software budget cut.
5. **Altman Z = 1.68 "distress"** — analytically misleading here (negative retained earnings, book-equity x4), but it will trip mechanical screens.
6. **Accumulated deficit −$2.38B** — no dividend/buyback capacity from retained earnings; all returns are balance-sheet-cash funded.
7. **Receivables/DSO** — $687M, ~86 days, stable but a collections indicator to monitor in a downturn.

**Data gaps:** Sortino ratio not computed; no public credit rating or CDS on residual debt; revolver capacity and the exact composition/maturity of the $53M residual obligation not disclosed by the tools; peer benchmarking unavailable (sector screen returned only mega-caps — MSFT/AAPL/NVDA — not identity-software comparables); beta conflict between vendor profile (0.733) and computed (1.241).
