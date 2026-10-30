# Fin Risk Analyst

- Symbol: GEN
- Elapsed: 72.1s

---
## GEN (Gen Digital Inc.) — Financial Risk Assessment

**Snapshot (latest available):** Consumer cyber-safety subscription software (Norton, LifeLock, Avast, Avira, MoneyLion). Price ~$28.20, market cap ~$16.8bn, ~596M diluted shares. Latest balance sheet 2026-10-02; TTM = four quarters through 2026-10-02.

---

### 1. Credit Risk Assessment: **SUB-INVESTMENT GRADE (Crossover BB)**

| Item | Data |
|---|---|
| Fitch IDR | **BB+**, outlook revised to **Stable** (11-Feb-2026) |
| S&P ICR | **BB**; TLB rated BB (recovery '3'), senior unsecured **BB-** |
| Net debt / TTM EBITDA | **3.1x** ($7,527M / $2,431M) |
| Net debt / FY26 "as-reported" EBITDA | 5.5x — **see data caveat** |

GEN is a leveraged, acquisition-built subscription software company with stable but sub-investment-grade credit. The Feb-2026 Fitch outlook revision to Stable (from Negative) is a genuine positive — it reflects deleveraging, cost savings from the Avast integration, and steady FCF. But the company sits two notches below investment grade, and the rating now hinges on the **~$4.4bn of debt maturing in 2027** being refinanced on acceptable terms.

**Critical data caveat (flagged):** the annual FY2026 record shows `ebitda` = $1,435M and `ebit` = $942M, which is *internally inconsistent* with `operating_income` = $2,155M and with the quarterly series (Q4 FY26 EBITDA $658M, Q3 $572M, Q2 $504M; Q4 FY26 FCF $449M reported). Summed quarterly TTM EBITDA = $2,431M and TTM operating income = $2,207M. **I use the quarterly-derived TTM figures as primary**; the single-row annual EBITDA field appears mis-scaled and should not be used for leverage math. Likewise the tool-reported "interest coverage" of 3.79x uses operating income, while the Z-score tool uses the low EBIT — hence a wide 1.7x–4.3x reported range. My best estimate of true coverage is **3.5–4.3x EBITDA/interest**, consistent with a BB+ credit.

---

### 2. Key Financial Risk Metrics

| Metric | Value | Read |
|---|---|---|
| Total debt | $8,116M | vs. equity $2,741M |
| Debt / equity (book) | **2.96–3.16x** | High, but stable since FY24 (3.16x) |
| Debt / assets | 0.53 | Over half the balance sheet |
| Net debt / EBITDA (TTM) | **3.1x** | Acceptable for BB+; ~4x is the downgrade trigger zone |
| Interest coverage (EBITDA/interest) | **4.7x** | TTM interest $514M |
| Interest coverage (EBIT/interest) | ~3.5x (normalised) | Adequate but not cushion-rich |
| Implied cost of debt | ~6.3% | Reflects 2023-vintage issuance |
| Current ratio / quick ratio | **0.40 / 0.40** | Structurally weak (deferred revenue) |
| Cash & ST investments | $589M | **~5%** of assets; ~1.1 quarters of FCF |
| Working capital | **–$2.2bn** (Q2 FY27) | Negative by design (subscription billings) |
| Altman Z-Score | **0.54 — "Distress" zone** | Largely a **false signal** (see below) |
| Piotroski F-Score | **8 / 9 — "Strong"** | Profitability & deleveraging all clean |
| FY26 dividends + buybacks | $312M + $634M = **$946M** | 62% of FCF |
| FCF (FY26) / FCF margin | $1,523M / **30.5%** | Excellent |
| FCF yield | **~8.7–9.0%** | High — market pricing credit/refi risk |

**On the Z-Score (0.54, "Distress"):** I do **not** treat this as a bankruptcy signal. It is mechanically broken for this business model: (a) goodwill + intangibles are **$12.9bn = 83% of total assets**, crushing the asset-turnover and retained-earnings terms; (b) X1 is negative purely because deferred revenue exceeds current assets; (c) X4 uses *book* equity ($2.7bn) instead of market equity (~$16.8bn), which alone would lift the score massively. The F-Score of 8 and 4.7x interest coverage directly contradict a distress reading. **Gap noted:** I could not obtain a market-cap-based Z or Altman Z'' for the EM-score variant.

---

### 3. Market Risk Profile

| Metric | Value | Note |
|---|---|---|
| Annualised volatility (252d) | **47.2%** | Very high; ~2x large-cap software median |
| Beta vs SPY (252d, computed) | **0.81** | Defensive-ish on this window |
| Beta (vendor, longer window) | **1.257** | **Divergence flagged** — I'd trust ~1.1–1.2 for forward risk |
| Max drawdown (252d, tool) | –33.6% | |
| Peak-to-trough (Aug-2025 → Apr-2026) | **–43.6%** ($31.42 → $17.72) | My own calculation from price history |
| Sharpe (0% rf, 252d) | 0.579 | Respectable, but UST 2Y–10Y available; true excess-return Sharpe lower |
| Price recovery | Trough $17.72 → ~$28.20 = **+59%** | FY27 guide raised to $5.465–5.515bn |

The 47% volatility and the –44% drawdown are **event-driven, not structural**: the stock de-rated through the FY26 print (Jan-2026 gap down, further decline into the March–April 2026 low) and then round-tripped on raised FY27 guidance and better-than-expected revenue growth. Investors in GEN are accepting equity volatility that behaves like a high-yield credit — the equity is effectively a levered call on the refinancing outcome. Note the price history feed ends 2026-04-30 while statements run to 2026-10-02, so the volatility/beta windows do **not** include the last six months of recovery; true trailing vol is likely somewhat lower than 47%.

---

### 4. Downside Scenario Analysis (−20% revenue)

Base: TTM revenue $5,228M, TTM EBITDA $2,431M (46.5% margin), 78% gross margin, SG&A ~$1.15bn TTM (ex one-off), D&A ~$490M, interest $514M, capex ~$25M.

| | Base | **–20% revenue** | **–30% severe** |
|---|---|---|---|
| Revenue | $5,228M | $4,182M | $3,660M |
| Gross profit (78%) | $4,078M | $3,262M | $2,855M |
| Opex (cut 10% / 15%) | ($1,647M) | ($1,482M) | ($1,400M) |
| **EBITDA** | **$2,431M** | **$1,616M** | **$1,208M** |
| EBITDA margin | 46.5% | 38.6% | 33.0% |
| EBIT (post D&A) | $1,941M | $1,126M | $718M |
| Interest expense | $514M | $514M (or higher on refi) | $560M |
| **EBIT / interest** | 3.8x | **2.2x** | **1.3x** |
| **EBITDA / interest** | 4.7x | **3.1x** | **2.2x** |
| Net debt / EBITDA | 3.1x | **4.7x** | **6.2x** |
| FCF (post interest, tax, capex) | ~$1,350M | **~$780M** | **~$450M** |
| Dividend ($312M) coverage | 4.3x | 2.5x | **1.4x** |

**Interpretation.** A 20% revenue shock is a severe stress for a subscription business with high renewal rates, and GEN survives it without covenant collapse: FCF stays comfortably positive (~$780M), the dividend is still 2.5x covered, and no maturity wall is breached on liquidity alone. But **net leverage would push to ~4.7x — through the level at which Fitch/S&P would almost certainly move to negative outlook or downgrade to BB/BB-**, precisely as the 2027 maturities come due. In that world GEN refinances into a *worse* spread environment: each +150bp on $8.1bn of debt costs ~$120M of annual interest, taking EBITDA/interest toward 2.6x and FCF toward ~$660M. The severe case (6.2x, 2.2x coverage) is a genuine restructuring-risk scenario — but it requires revenue to shrink 30%, which is well outside the observed behaviour (FY27 revenue growth is guided *up* ~10%).

---

### 5. Overall Financial Risk Rating: **MODERATE** (upper end of band)

**Why not "High":** genuinely strong cash generation (30% FCF margin, ~9% FCF yield), 78% gross margin, an 8/9 F-Score, four consecutive years of book-equity growth, positive and growing net income (TTM $1,206M), a Stable rating outlook as of Feb-2026, and 4.7x EBITDA interest coverage. Deleveraging is happening (net debt $7,527M today vs. $7,809M two years ago) even while paying $946M/yr to shareholders.

**Why not "Low":** the company is structurally levered at ~3x, sub-investment-grade, holds only ~5% of assets in cash with a 0.40 current ratio, and is dependent on capital markets to roll a 2027 maturity cohort. That is a refinancing-risk profile, not a fortress.

### 6. Key Red Flags

1. **2027 refinancing cliff (~$4.4bn).** Fitch flagged ~$4.4bn of debt due in 2027. Confirming evidence in the data: short-term debt jumped from **$181M (Jul-2026) to $1,080M (Oct-2026)** — debt being reclassified to current as the maturity approaches. This is the single largest risk in the name.
2. **Thin absolute liquidity.** Cash $589M vs. current liabilities $3,481M. Cash/liabilities = **0.03**. Coverage of interest alone is ~4.6 quarters of cash. Revolver capacity was **not disclosed in my data** — a material gap; without a confirmed undrawn revolver, liquidity is one bad quarter from tight.
3. **Goodwill & intangibles = 83% of assets.** Tangible book equity is deeply negative. Any impairment (Avast, MoneyLion) would hit book equity directly and could pressure leverage covenants measured on GAAP equity. This is also why the Z-Score reads "distress."
4. **Shareholder returns compete with deleveraging.** $946M returned in FY26 against $1,523M FCF, while $8.1bn of debt needs rolling in 2027. Buybacks should be (and probably will be) the first thing suspended in a downturn — but the current policy reduces the deleveraging buffer.
5. **Growth is partly inorganic.** Revenue +27% YoY in Q4 FY26 with goodwill adding ~$600M — organic growth is materially below headline. Acquisition-driven roll-ups carry integration and impairment risk.
6. **Equity risk is credit risk.** –43.6% drawdown, 47% realised vol, and a beta that the two sources disagree on (0.81 vs. 1.26). A credit event at refinancing transmits directly to equity.
7. **Data-quality flags (explicit gaps):** FY2026 annual EBITDA/EBIT fields are internally inconsistent and were discarded in favour of quarterly-derived TTM; Q4 FY26 SG&A ($36M) and operating income ($813M) look like one-off distortions, so my coverage ratios are normalised; no covenant detail, no revolver commitment size, no CDS spreads, no peer multiple context available.

**Bottom line:** GEN is a cash-generative, moderately levered BB credit whose financial risk is *concentrated and dated* — 2027 refinancing, funded by an FCF stream that is robust even under a 20% revenue decline. Investment-grade-quality cash flow, sub-investment-grade balance sheet. Watch the 2027 maturity roll and buyback pace as the two leading indicators.
