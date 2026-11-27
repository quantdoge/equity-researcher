# Fin Risk Analyst

- Symbol: ORCL
- Elapsed: 50.6s

---
## ORACLE CORPORATION (ORCL) — Financial Risk Assessment
*Price $103.88 | Market cap ~$314bn | FY2026 (May-end) financials | Risk data as of late Nov 2026*

---

### 1. Credit Risk Assessment — **SUB-INVESTMENT GRADE (Crossover / Fallen-Angel Risk)**

Oracle is nominally investment grade but sits at the bottom rung, and the trajectory is clearly toward high yield.

| Rating agency | Rating | Outlook |
|---|---|---|
| Moody's | Baa2 | **Negative** (negative outlook re-affirmed Feb and Nov) |
| S&P | **BBB−** (cut from BBB in July 2026) | Stable |

The crucial signal is market-priced, not agency-priced: **ORCL 5Y CDS hit a record ~356bp** and its bonds trade at **~9% yields** — roughly 390bp+ over the 5.13% 10Y UST. That is a high-yield spread in all but label. Equity has fallen **~70% from the 2025 peak** (−47% YTD 2026), and bankruptcy speculation is now in mainstream coverage. Moody's explicitly treats Oracle's massive lease obligations as debt-like, which means headline leverage **understates** true obligations.

The core credit story: Oracle is funding an AI datacenter buildout ($55.7bn capex in FY26, up 162% YoY) with debt while free cash flow is deeply negative. **PP&E ballooned from $43.5bn to $129.6bn in one year (+198%)** and total debt rose from $104.1bn to $156.2bn. This is a leveraged infrastructure bet, not a software cash machine.

---

### 2. Key Financial Risk Metrics

| Metric | FY2026 | FY2025 | FY2024 | Assessment |
|---|---|---|---|---|
| **Debt / Equity** | **3.63x** | 4.96x | 10.2x | Very high (equity base thin) |
| **Net debt / EBITDA** | **3.72x** | 3.90x | 3.93x | Stretched for BBB− |
| **Interest coverage (EBIT/int)** | **5.25x** | 4.96x | 4.34x | Adequate but interest +28.6% YoY |
| **Interest coverage (tool)** | 4.48x | — | — | Tool uses gross/capitalised interest |
| **Debt / Assets** | 0.60x | 0.62x | 0.67x | High |
| **Equity / Assets** | **16.4%** | 12.5% | 6.6% | Thin cushion |
| **Current ratio** | **1.12x** | 0.75x | 0.72x | Weak, improved via debt-funded cash raise |
| **Quick ratio** | 1.12x | — | — | No inventory (pure software) |
| **Cash ratio** | 0.76x | — | — | OK |
| **Working capital** | +$4.80bn | −$8.06bn | −$8.99bn | Thin positive |
| **Altman Z-Score** | **0.679 (Distress)** | — | — | Severe |
| **Piotroski F-Score** | **5 / 9 (Moderate)** | — | — | Mediocre |
| **FCF** | **−$23.69bn** | −$0.39bn | +$11.81bn | Deteriorating to deeply negative |
| **FCF yield** | **−7.82%** | — | — | Cash-consumptive |
| **Retained earnings** | **−$4.31bn** | −$15.48bn | −$22.63bn | Accumulated deficit persists |

**On the Z-Score:** the standard calc uses *book* equity (x4 = 0.197). Re-running x4 on market cap ($314bn / $218.7bn liabilities = 1.436) lifts the score only to **~1.42 — still inside the distress zone (<1.81)**. This is not a book-value artifact; Oracle fails on earnings retention (x2 negative), turnover (x5 = 0.26), and leverage simultaneously.

**Margin deterioration is the quietest red flag.** Gross margin fell from 71.4% → 70.5% → **65.8%** in two years (−470bp) while cost of revenue grew **36.0%** vs revenue growth of 17.3%. Revenue growth is accelerating (6.0% → 8.4% → 17.3%) precisely because Oracle is selling lower-margin OCI/AI infrastructure. Growth quality is degrading as it scales. Piotroski confirms (F8 gross-margin improvement = 0, F9 asset turnover improvement = 0, F3 ROA improvement = 0).

---

### 3. Market Risk Profile — **Extreme**

| Metric | Value | Interpretation |
|---|---|---|
| Annualised volatility | **59.1%** | ~3x market; worse than most high-yield equities |
| Beta vs SPY | **1.74** | Amplifies market drawdowns ~1.7x |
| Max drawdown (3yr) | **−68.7%** | Full-blown bear market |
| Sharpe ratio | **−0.074** | Negative risk-adjusted return |
| 30-day move (reported) | −17.6% | Acute, ongoing volatility |

A 59% vol stock with a 1.74 beta and a Sharpe below zero is a **de-risking candidate for any risk-budgeted mandate**. Realised drawdown of nearly 70% has already exceeded typical "stress test" assumptions. Downside beta is likely higher than measured beta given the leverage — equity is behaving as a levered call option on the AI datacenter buildout.

---

### 4. Downside Scenario Analysis — Revenue −20%

Assume FY27 revenue falls 20% (AI contract delays, cloud digestion), gross margin held at 65.8%, SG&A flat, D&A +15% as new assets enter service, interest expense rising to $5.5bn on incremental issuance.

| Metric | Base FY26 | **Scenario A: −20% rev** | **Scenario B: −20% rev + GM to 55%** |
|---|---|---|---|
| Revenue | $67.36bn | $53.89bn | $53.89bn |
| Gross margin | 65.8% | 65.8% | 55.0% |
| Operating income | $20.61bn | $14.81bn | $9.00bn |
| EBITDA | $33.45bn | $25.50bn | $19.69bn |
| EBIT / interest | 5.25x | **2.69x** | **1.64x** |
| Net income | $17.09bn | $7.64bn | $2.87bn |
| Operating cash flow | $31.98bn | ~$23.1bn | ~$18.4bn |
| Capex | $55.66bn | $45.0bn | $55.6bn (committed) |
| **Free cash flow** | −$23.69bn | **−$21.9bn** | **−$37.3bn** |
| Net debt | $124.9bn | **$146.8bn** | **$162.2bn** |
| **Net debt / EBITDA** | 3.72x | **5.76x** | **8.24x** |
| Altman Z | 0.68 | ~0.5 | <0.3 |

**Interpretation:** A 20% revenue decline is not survivable on the current capital structure without decisive action. Coverage falls to ~2.7x (and 1.6x under margin compression), leverage blows through 5.5–8.0x — **well past any plausible BBB− covenant threshold and squarely in single-B territory**. At 8.2x net leverage the equity is effectively option value.

**Mitigants:** (a) capex is the lever — cutting to maintenance levels (~$15bn) would restore FCF to roughly breakeven; (b) the $31.9bn cash pile covers 5.4 quarters of current FCF burn and 4.4x short-term debt ($7.2bn); (c) operating cash flow remains solidly positive at $32bn, so this is a *solvency/leverage* problem, not an immediate *default* problem. Oracle retains capital-markets access — but at ~9% marginal cost, each new dollar of debt imports ~$900mn of annual interest per $10bn raised.

**Liquidity / refinancing:** Near-term maturities are modest (ST debt $7.2bn vs cash $31.9bn), so there is **no imminent refinancing cliff** — but $26.6bn of total debt sits outside reported short/long-term lines (leases and finance obligations), and the true obligation profile including AI compute commitments is not visible in the standard statements. Management paid **$5.79bn of dividends and $0.21bn of buybacks while FCF was −$23.7bn** — shareholder returns funded entirely by borrowing. That is a reversal candidate and a governance flag.

---

### 5. Overall Financial Risk Rating: **HIGH** (trending toward Critical)

Not yet Critical, because operating cash flow is positive, cash is ample, near-term maturities are light, and revenue is genuinely growing 17%. But leverage, coverage, free cash flow, the Z-score, and the market-implied credit signal all point the same direction, and the rating agencies have already begun moving.

---

### 6. Key Red Flags
1. **Negative FCF at scale** — −$23.7bn, from +$11.8bn two years ago; capex up 162% YoY and largely committed/contractual.
2. **Fallen-angel trajectory** — S&P cut to BBB− (July 2026); Moody's Baa2 negative; CDS at record 356bp; bonds at ~9%.
3. **Altman Z of 0.68 in the distress zone even on market-cap equity (~1.42).**
4. **Gross margin −470bp in two years** as revenue mix shifts to low-margin OCI — growth is diluting, not compounding, profitability.
5. **Depreciation overhang** — $129.6bn of PP&E will drive D&A well above today's $9.3bn, structurally compressing EBIT and coverage regardless of revenue.
6. **Borrowing to pay dividends** — $5.8bn of dividends on negative FCF.
7. **Dilution** — share count 2.744bn → 2.860bn (+4.2% in two years); Piotroski F7 = 0; equity rose ~$22bn vs $17bn net income less $5.8bn dividends, implying roughly **$6bn+ of equity issuance/OCI gains** beyond earnings.
8. **Extreme equity risk** — 59% vol, 1.74 beta, −69% drawdown, negative Sharpe, 59% annualised swing in a single year.
9. **Macro backdrop hostile** — 10Y at 5.13%, 2s10s +39bp (no inversion, higher-for-longer); refinancing $156bn of debt into a 9% market is a multi-billion annual EPS headwind.

### Data Gaps (explicitly flagged)
- **Debt maturity schedule / covenant terms unavailable** — cannot confirm specific leverage or coverage maintenance covenants; the $26.6bn gap between reported total debt and ST+LT lines (leases/finance obligations) is unresolved.
- **Off-balance-sheet AI compute and lease commitments** (Stargate/OpenAI-related) not quantified in available statements — Moody's treats these as debt-like, which would raise adjusted leverage materially above 3.72x.
- **No peer/industry comparative multiples** pulled; Oracle's leverage is high in absolute terms but I have not benchmarked it against infrastructure-software peers.
- **Interest coverage discrepancy**: tool reports 4.48x vs 5.25x on reported EBIT/interest — likely a gross-vs-net or capitalised-interest definitional difference; both are disclosed above.
- Rating actions and CDS levels are sourced from press coverage, not a live credit feed; verify against agency releases before relying on them.

**Bottom line:** ORCL is a leveraged infrastructure build-out wearing a software company's income statement. It survives a downturn on liquidity but not on credit quality — a 20% revenue decline takes net leverage to ~5.8x and coverage under 3x, triggering downgrade to junk. Position sizing should reflect a ~1.7 beta, 59%-vol equity that has already demonstrated a 69% drawdown.
