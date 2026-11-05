# Nonfin Risk Analyst

- Symbol: LSCC
- Elapsed: 108.0s

---
## NON-FINANCIAL RISK ASSESSMENT — LATTICE SEMICONDUCTOR (LSCC)

**Price $107.25 | Market cap ~$15.2B | Beta 1.89 | 1,174 FTE | Semiconductors (FPGA) | FY26 Q3 ended Oct 3, 2026**

**Scope note / data gaps:** SEC EDGAR and the IR site returned HTTP 403 for the FY25 10-K (filed 02/13/2026), the Q3'26 10-Q, and the 2026 DEF 14A, so I could not verify risk factors, legal proceedings, or compensation tables at source. Findings below are triangulated from Form 4 data, 8-K/8-K-A coverage, rating-agency commentary, and secondary reporting. Items marked **[unverified]** should be confirmed against the filing before publication.

---

### 1. Governance Quality Rating: ADEQUATE (trending positive, with a deal-process asterisk)

**Positives:**
- **Independent Chairman, separate from CEO.** Jeff Richardson is Chairman; Ford Tamer (CEO since Sept 2024) sits as a director. No CEO/Chairman duality — a genuine structural positive versus the sector norm.
- **Board refresh and independence.** On **Oct 21, 2026** the board appointed **John McCool** and **Raejeanne Skillern** as independent directors (8-K, Oct 22), taking the board to nine. Both carry deep semiconductor operating experience. Skillern *rejoined* after serving Sept 2022–May 2024 — useful expertise, but a re-appointment of a recent departure merits a look at why she left.
- **Disclosure hygiene in the deal.** The AMI acquisition was announced with a merger 8-K (May 4, 2026), an S-8 to register 625,967 deal shares (July 28, 2026), and a corrective **8-K/A (Oct 13, 2026)** filing AMI's audited financials. Restating detail is better than burying it.
- **Insider alignment:** see §3 — the CEO bought stock with personal cash.

**Concerns:**
- **Leadership churn at the top.** Both the CEO seat (Sept 2024) and the CFO seat (Lorenzo Flores, appointed early 2025 after an interim CFO) turned over within roughly 12 months. A CFO vacancy filled on an interim basis during a CEO transition is a control-environment watch item.
- **Deal-process litigation overhang [unverified].** Plaintiff firms are soliciting a **securities class action with a class period of roughly April 29, 2026 – October 13, 2026**, and at least one firm is investigating whether executives "were conflicted and acted in their own self-interest when approving the merger." The Oct 13 end-date coincides exactly with the AMI 8-K/A — i.e., the claim likely turns on disclosures made around the $1.65B AMI purchase. **This is a governance signal about the deal process, not a generic nuisance suit.** Docket number not confirmed.
- **Shareholder vote not yet verified** on the 625,967-share issuance; if the stock portion was structured to avoid a vote, dilution scrutiny will follow.

**Rating: Adequate.** Independent chair + fresh independent directors + CEO open-market buying offset the CEO/CFO churn and the deal-process claims. A clean litigation outcome and a stable FY27 CFO tenure would move this to Strong.

---

### 2. Regulatory Risk Summary

- **No active SEC enforcement or DOJ action identified.** EDGAR full-text enforcement search returned zero hits for LSCC. This is a clean result, with the caveat that it only covers SEC actions.
- **Export controls / China — the dominant regulatory exposure.** Geography is the story: **Asia was ~78% of revenue in Q1 2026**, and **distributors were ~94% of revenue that quarter** (84% in FY25, 89% FY24, 87% FY23). A company deriving ~three-quarters of sales from Asia, sold almost entirely through a channel it does not control, sits squarely in the blast radius of US–China chip controls and China's countermeasures (Decree 834, Mar 31, 2026; expanded rare-earth export controls). Lattice's own FY25 10-K flags "increasing restrictions" as a risk **[10-K text not directly retrieved]**.
- **CFIUS history is a live precedent, not ancient history.** The 2016–17 **Canyon Bridge** acquisition collapsed after CFIUS rejection and produced a securities class action over proxy omissions. LSCC is a company with demonstrated national-security sensitivity; any future cross-border transaction, or any Chinese customer concentration, faces elevated scrutiny.
- **Antitrust:** the AMI deal (firmware/BIOS + FPGA) plausibly triggered HSR review; no challenge identified. Post-close, the combined control-plane position is more concentrated — worth monitoring.
- **Privacy/cyber:** no known GDPR/CCPA enforcement. The company is a security vendor (PQC-enabled FPGAs, Sentry stack), so a breach would carry outsized reputational cost.

---

### 3. Insider Activity Analysis (trailing 12 months): **NET SELLING ≈ 6.6:1, BUT THE CEO IS BUYING**

**Open-market purchases (the only buys):**
| Date | Insider | Shares | Price | Value |
|---|---|---|---|---|
| 2026-11-04 | **Ford Tamer, CEO** | 9,790 | $102.52 | **$1,003,689** |

**Open-market sales (all pre-arranged 10b5-1):**
| Date | Insider | Shares | Price | Value |
|---|---|---|---|---|
| 2026-08-17 | E. Elashmawi, SVP Strategy | 15,742 | $134.77 | $2,121,569 |
| 2026-05-20 | P. Desale, SVP R&D | 14,155 | $134.23 | $1,899,994 |
| 2026-06-03 | J. Lederer, **Director** | 6,101 | $153.94 | $939,157 |
| 2026-09-15 | P. Desale | 4,279 | $105.63 | $451,970 |
| 2026-06-04 | T. Feanny, GC | 2,740 | $151.84 | $416,046 |
| 2026-06-12 / 09-14 | P. Desale | 4,078 | ~$127 | $519,374 |
| 2026-08-18 | T. Feanny, GC | 1,880 | $126.43 | $237,688 |
| **Total** | | | | **≈$6.59M** |

**Read-through:**
- The **Oct 13 cluster of six Form 4s were all tax withholding on vesting**, not discretionary sales — do not misread as a bearish signal. The same applies to the July/August/September withholding clusters.
- Discretionary selling was concentrated at **$134–$154** (May–June), i.e., insiders sold into the top decile of the range. **Zero insider purchases occurred during the entire run-up.**
- The lone buyer is the **CEO, buying $1.0M of stock in the open market on Nov 4 — two days after record Q3 results and after a ~32% drawdown from the June peak.** This is the highest-conviction signal in the dataset and materially offsets the SVP selling. Note it is held **indirectly**, so confirm it is not a trust/entity with other purposes.
- **Director sale by Lederer ($939K) is the one to press on** — director selling usually lacks the 10b5-1 "planned diversification" defense that applies to management.

---

### 4. Top Operational Risks

- **AMI integration and impairment risk — the single largest exposure.** Lattice paid **$1.65B ($1.0B cash + ~$650M stock)** for a business that, per the Oct 13 8-K/A, generated **$194.7M of 2025 revenue and a $14.0M net loss**. That is ~8.5x sales for a loss-maker, funded with **$950M of delayed-draw term debt** ($1.15B facility led by Wells Fargo), lifting **S&P-adjusted leverage to ~2.2x** and earning a **'BB'** rating. Q3'26 shows the strain: **revenue +118% YoY to $291M while net profit fell 42.1% QoQ.** Material goodwill/intangible balances now sit against a business with negative GAAP earnings — a pricey setup if AMI's margin ramp disappoints.
- **Channel and geographic concentration.** ~84% distributor-sold, ~78% Asia. This concentrates credit risk in a handful of distributors, complicates revenue-recognition and channel-inventory visibility (a classic FPGA/analog problem — sell-in vs. sell-through), and puts the revenue base inside the US–China policy crossfire.
- **Key-person and organizational stretch.** 1,174 employees absorbing a $1.65B software acquisition, with a CEO (2024) and CFO (2025) both new to their roles and a partially re-built board. Founder risk is absent, but **management-bandwidth risk is high**: the same small executive team is simultaneously integrating AMI, defending the core FPGA franchise against Altera/AMD/Microchip, and managing a leveraged balance sheet.

---

### 5. Reputational Risk Assessment: **MODERATE–ELEVATED**

- **Narrative concentration risk.** The equity story has been re-cast as an "AI data center infrastructure" play (SCMP/OCP workstream with AMI, Arm collaboration, PQC-enabled Sentry stack). Tying the multiple to AI while the acquired AI asset is loss-making invites an **"AI-washing" backlash** if Compute & Communications growth decelerates. The stock's realized volatility — **$157 (June) to $93 (Oct 30), beta 1.89** — shows how violently the market will reprice any disappointment.
- **Shareholder-relations optics.** A 32% drawdown followed by an 8-K/A revealing the acquired company's net loss, then a securities class action, is precisely the sequence that hardens retail and proxy-advisor sentiment.
- **Short interest is moderate, not a red flag:** ~7.03M shares, **5.16% of float** (Oct 15, 2026).
- **ESG:** no material controversy identified; governance is the only meaningful pillar.
- Customer/product reputation is strong (CyberSecurity Breakthrough Award, OCP leadership) — the reputational risk here is **financial-communication and deal-credibility risk, not brand or product-quality risk.**

---

### 6. Overall Non-Financial Risk Rating: **MODERATE** (upper end; the M&A/leverage sub-risk is **HIGH**)

Genuine governance strengths (independent chair, refreshed board, CEO skin-in-the-game) and a clean SEC enforcement record anchor the rating. They are offset by a **transformational, debt-funded, loss-making acquisition**, extreme channel/geographic concentration in the most policy-exposed region in semiconductors, top-team turnover, and active deal-related litigation. Nothing here is existential; several items are compounding.

---

### 7. Red Flags Requiring Escalation

1. **Loss-making acquisition at 8.5x sales with $950M of new debt.** AMI: $194.7M revenue, **–$14.0M net income** (2025, 8-K/A 10/13/26). Combined with a **42.1% QoQ profit decline** on +118% revenue, request the goodwill allocation, intangible amortization schedule, and the covenant cushion under the $200M revolver / $950M term loan. **(Highest priority.)**
2. **Securities class action tied to the AMI disclosure window** (class period ~Apr 29 – Oct 13, 2026) **[unverified — confirm docket]**. A governance/process claim, not a nuisance suit; get outside counsel's view on materiality of the pre-deal disclosures.
3. **Revenue-quality question:** ~94% distributor-sold with Asia at ~78% of revenue. Request distributor inventory weeks, sell-through vs. sell-in, and any change in revenue-recognition terms. Combine with the revenue/earnings divergence in Q3.
4. **Director open-market sale of $939K (Lederer, June)** and **$6.6M of cumulative SVP/GC sales with zero buys until the CEO's Nov 4 purchase** — verify all were 10b5-1 and screen for any adoption date within 90 days of bad news.
5. **Two-year C-suite churn:** CEO (Sept 2024) and CFO (2025, post-interim) both new; board seat re-filled by a 2022–24 alumna. Confirm no unresolved control deficiencies were disclosed in the transition.
6. **Policy single-point-of-failure:** ~78% Asia revenue. Model an export-control/licensing shock and check whether any single distributor or end-customer now exceeds 10% of revenue post-AMI.

**Escalate items 1, 2 and 5 to the investment committee; the remainder to ongoing monitoring.**
