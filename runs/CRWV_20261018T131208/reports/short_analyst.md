# Short Analyst

- Symbol: CRWV
- Elapsed: 162.4s

---
# CoreWeave (CRWV) — Forensic Short-Seller Analysis

**Price $61.39 | Market cap $33.9B | Sector: Software-Infrastructure | IPO Mar-2025 | Beta 7.3**

---

## 1. Earnings Quality Assessment: **LOW** (composite score 0/100)

The feed's composite earnings-quality score is **0 out of 100** — the floor. Cash conversion is **-2.62x** and FCF conversion is deeply negative in substance despite a nominal positive reading. But the more important finding is structural: **CoreWeave's reported "EBITDA profitability" is an artifact of accounting policy, not economics.**

| Metric | FY2024 | FY2025 | Q2 2026 (ann.) |
|---|---|---|---|
| Revenue | $1.915B | $5.131B | $10.30B |
| Gross margin | 74.3% | 71.7% | **65.9%** |
| D&A | $863M | $2.454B | $5.57B |
| Reported EBITDA | $480M | $2.468B | $5.88B |
| Operating income | +$324M | **-$46M** | +$14M |
| Net income | -$863M | -$1.167B | -$2.50B |
| Net margin | -45.1% | -22.7% | **-24.3%** |

**The single most damning statistic:** revenue grew **+112% YoY** in Q2 2026, and net margin was **-24.3%** — versus **-24.0%** in Q2 2025. Two years of hypergrowth, *zero* operating leverage. Every incremental dollar of revenue arrives with an identical proportion of loss attached.

---

## 2. Key Red Flags Found

**R1 — Depreciation deferral (the core forensic finding).** Q2 2026 D&A of $1.393B annualizes to $5.57B against **net PP&E of $63.3B** → implied blended remaining life of **11.4 years**. GPU fleets have 5–6 year economic lives (hyperscalers have *shortened* toward 5). Restating to a 6-year life gives D&A of ~$10.6B/yr — **~$5.0B/yr of under-depreciation, ~39% of annualized revenue.** On that basis true operating income is roughly **-$4.9B/yr**, not the near-breakeven $14M reported.

**R2 — Growth is masking obsolescence.** FY2025 D&A/capex = $2.454B / $10.31B = **23.8%**. In a steady-state fleet D&A ≈ capex. A 24% ratio means the asset base is compounding ~4x annually, hiding the fact that each vintage of silicon is deteriorating. The moment growth decelerates, D&A catches up and EBITDA collapses. This is a *timing* bomb, not a permanent one — which is precisely what a short wants.

**R3 — Gross margin compression of ~970bps.** 75.6% (Q4'24) → 74.2% → 73.0% → 67.6% → 65.5% → **65.9% (Q2'26)**. Directional, sustained margin erosion in a business that claims to be capacity-constrained with demand "outstripping supply." Genuine pricing power does not behave this way — power, rent and depreciation are inflating faster than price.

**R4 — Interest is compounding faster than revenue.** Net interest: $267M → $311M → $388M → $536M → **$640M** (Q2'26), i.e. **+140% in four quarters**. Interest/revenue is *rising* (22.0% → 24.9%) even as revenue doubled. Annualized interest ~$2.56B. **EBIT / interest coverage = 0.12x**; EBITDA-only coverage is 2.3x — and that EBITDA is the fictitious number from R1.

**R5 — Dilution.** Diluted weighted shares: 218M (FY24) → 435M (FY25) → **551M (Q2'26) = +153% in 18 months.** Piotroski F7 = 0. A further $4.2B of 2.875% converts (Sep 2026, due 2033) sit on top. Per-share value creation is structurally impaired.

**R6 — Balance sheet is levered to the eyeballs.** Total debt **$51.608B**, net debt $45.211B, equity only **$5.024B** — equity is **6.5% of $77.07B assets**. Net debt / annualized EBITDA = **7.7x** on the flattering EBITDA, ~45x on restated EBITDA. Working capital is **-$11.4B** (current ratio 0.46x).

**R7 — Cash burn at a scale that requires permanent capital-markets access.** FCF: FY2025 **-$7.25B**; H1 2026 **-$10.45B** (Q1 -$4.71B, Q2 **-$5.74B**). Cumulative burn ~-$17.7B. Q2 2026 capex of $6.42B was **2.5x quarterly revenue**. Implied annual external funding need ≈ $25B/yr.

**R8 — Receivables spike at FY2025 year-end.** DSRI = 2.779. DSO: ~81 days (FY24) → **~225 days (FY25)** as AR jumped 91% in Q4'25 against 15% sequential revenue growth. It has since normalized to ~90 days (AR $2.54B / Q2'26 revenue $2.58B), suggesting a large year-end invoice rather than systemic channel stuffing — **but a 3x DSO swing deserves an explanation we could not obtain.**

---

## 3. Beneish M-Score and Accruals Analysis

**M-Score = +0.003** vs. -1.78 manipulation threshold — a **massive breach**, flagged "HIGH RISK." Components: DSRI 2.779, SGI 2.679, SGAI 2.166, GMI 1.036, DEPI 0.944, LVGI 0.911, **TATA -0.0857**.

**I will not overclaim here.** Beneish is mechanically biased for hypergrowth: SGI 2.679 and SGAI 2.166 are direct consequences of revenue scaling 168%, and DSRI is measured off a tiny FY24 receivables base. The M-Score breach is **not evidence of fraud**. Notably, **TATA is negative (-0.0857)** — accruals are *cash-negative*, i.e. the conservative direction. The manipulation signal that genuinely survives scrutiny is **DEPI 0.944 (declining depreciation rate) and R1's 11.4-year implied life**, which is a legitimate accounting-policy finding rather than a statistical artifact.

**Accruals caveat:** the reported accruals ratio of -0.0857 ("ok") rests on an operating cash flow series I do not trust. FY2023 OCF is shown as **$1.83B against $229M of revenue** — implausible. Treat the accruals metric as unreliable.

**Real OCF quality issue:** Q1 2026 OCF was $2.984B versus NI -$740M + D&A $1.147B + SBC $153M + WC $14M ≈ $574M. That leaves **~$2.4B unexplained** — almost certainly customer prepayments/deferred revenue. Cash today against revenue recognized over years. It flatters the "we generate operating cash" narrative while capex of $7.7B swamps it. This is not fraud; it is a *quality-of-cash mirage* that bulls cite as validation.

**Altman Z = -0.144 (Distress zone).** X1 -0.1816, X2 -0.0536, X3 0.0003, X4 0.0726, X5 0.1041. Using market cap instead of book equity lifts X4 to ~0.47, giving Z ≈ +0.4 — **still deep in distress.** Piotroski F = 5, with F1 (positive ROA), F7 (no dilution), F8 (gross margin) and F9 (asset turnover) all failing.

---

## 4. Competitive Threat Assessment

The credit market has already rendered a verdict: **bonds issued at a 2.875% coupon in September 2026 traded to ~81 cents at a >15% yield within four weeks**, described by Bloomberg as distressed. A 15% cost of debt against a business earning **~0% ROIC on $77B of invested capital** is a value-destruction machine — each dollar of capex now destroys roughly 15 cents of value annually.

Structural threats:
- **Customers are competitors.** Hyperscalers drove 77% of revenue (top two, 2024; Microsoft >60%). They are simultaneously building in-house capacity and passing on take-or-pay options. Your largest customer financing its own substitution is the definition of moat erosion.
- **Gartner forecasts 80% of neocloud providers disappear by 2030** — a direct attack on the category's terminal economics.
- **Vendor circularity.** Nvidia both supplies the GPUs and invests in / backstops the buyer. Supplier-funded demand is a classic Chanos red flag: it works until the supplier's own cycle turns.
- **Funding-market contagion.** A comparable Jane Street-anchored data-center bond struggled to clear in September 2026. CRWV's model requires the ABS/data-center debt market to stay open *at reasonable spreads*. The Fed's September hike tightened precisely the variable the model is most sensitive to.
- **Backlog quality.** $104B backlog against $12.4–13.2B FY26 guidance is only as good as counterparties' balance sheets — and the counterparties are cash-burning AI labs.

---

## 5. Management Red Flags

- **Insider filings:** 30 Form 4s between 26-Aug and 14-Oct-2026, with clusters on **2-Oct (11 filings)** and **14-Oct (2 filings)** — the last of these landing on the day of the 15.5% collapse. The density is characteristic of post-lockup 10b5-1 selling programs. **Caveat: the data feed does not disclose transaction direction or size, so I cannot confirm net selling.** I flag it as a pattern requiring verification, not as proof.
- **CEO response to the selloff** was to blame the market for "acting irrationally" rather than engage with the 15% cost of debt. Promotional deflection in place of capital-structure specificity is a soft red flag.
- **Aggressive non-GAAP framing:** EBITDA as the headline metric in a business where D&A *is* the primary economic cost is the single most misleading presentational choice management makes.
- **Not verified:** auditor changes, related-party transactions, dual-class control structure. SEC filing text retrieval failed (see gaps), so I make no fraud allegation.

---

## 6. Short Thesis Summary — Is There a Credible Bear Case?

**Yes — a rigorous one.** The mechanism is a **refinancing spiral**:

1. The business cannot self-fund: ~$25B/yr capex + $2.6B interest vs $3–4B OCF → permanent capital-markets dependency.
2. Marginal debt now costs **~15%**, up from 2.875% weeks earlier. Each $25B raised adds ~$3.75B/yr of interest.
3. Interest is already compounding at +140%/yr and consuming a *rising* share of revenue (22% → 25%).
4. EBITDA is overstated by ~$5B/yr through an 11.4-year implied GPU life. Reported near-breakeven EBIT becomes ~-$4.9B on normalized depreciation.
5. Growth — the only thing masking obsolescence — has plateaued at ~111% YoY (206% → 134% → 110% → 112% → 112%). **Note: the automated deceleration flag is partly misleading; growth has stabilized, not collapsed. But a plateau at 111% is still insufficient to outrun a debt stack that doubles annually.**
6. Equity is the shock absorber at 6.5% of assets. Any equity raise to delever is massively dilutive at $61 from a $122 April high.

**The bull case, stated fairly and it is not trivial:**
- $104B backlog vs a $33.9B market cap — 3x coverage. JPMorgan initiated Buy (Sep 2026) arguing the shift to shorter contracts *reduces* counterparty risk.
- Revenue is genuinely accelerating in dollars (+$499M QoQ, +23.9% QoQ) with real, scarce physical assets (power, GB200 NVL72 capacity) and a first-mover technical position.
- Much of the debt is secured/project-style against contracted GPU
