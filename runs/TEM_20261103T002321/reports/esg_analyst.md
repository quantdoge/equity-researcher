# Esg Analyst

- Symbol: TEM
- Elapsed: 94.1s

---
## ESG Analysis — Tempus AI, Inc. (NASDAQ: TEM)

**Snapshot:** Healthcare / Medical-Healthcare Information Services · US (Chicago) · Market cap ~$13.9B · 3,800 FTE · IPO June 2024 · Beta 3.61 · Q3'26 revenue $411.5M (+23% y/y), Data & Applications +33% at >71% gross margin, first positive adjusted EBITDA quarter.

**Framing note:** Tempus is not an industrial or energy business, so the ESG debate is *not* about carbon. It is about two things: **(1) whether the company's core asset — 45M de-identified patient records, monetised through data licensing — was lawfully assembled and can be lawfully licensed**, and **(2) whether a founder-controlled, dual-class, serial-acquirer governance structure is aligned with minority shareholders.** Both are live, litigated, and material to cash flows. Environmental factors are immaterial here and I will not inflate them.

---

### 1. ESG Materiality Map

| Factor | Materiality | Why it hits cash flow / cost of capital |
|---|---|---|
| **Data privacy & genetic-data consent (S)** | **Critical** | Directly attacks the Insights/Data licensing revenue line (>71% GM). Statutory-damages class action; injunctive relief could restrict the data estate itself. |
| **Governance: dual-class control, related-party dealings, board quality (G)** | **Critical** | ~60% voting control on <25% economic ownership; related-party deals (Pathos AI, AstraZeneca pass-through, SoftBank JV) are the specific subject of a securities fraud class action. Drives cost of equity and any governance discount. |
| **Business ethics / billing & reimbursement practices (S/G)** | **High** | Ambry alleged "aggressive and potentially unethical" billing; payer and False Claims Act tail risk in the diagnostics segment. |
| **Product safety & clinical validity of AI diagnostics (S)** | **High** | FDA/CLIA license to operate; algorithm performance and bias claims underpin both reimbursement and the AI narrative. |
| **Human capital (S)** | **Medium** | Lab/pathology and ML talent retention; four integrations in 18 months (Ambry, Paige, Deep 6 AI, Personalis). |
| **Anti-corruption / global expansion (G)** | **Low–Medium** | Japan JV, EU/UK expansion; no disclosed FCPA issues. |
| **Environmental: Scope 1–2, compute energy, Scope 3 reagents (E)** | **Low** | No manufacturing footprint. Sequencing + AI training is energy-intensive but immaterial to enterprise value. Real issue is a *disclosure gap*, not emissions. |

**Peer-mapping caveat:** the sector tool returned mega-cap pharma (LLY, JNJ, ABBV) — not meaningful comps. True comparables are Doximity, IQVIA, Natera, Exact Sciences, Veracyte, Recursion; peer ESG scoring was not retrievable within budget.

---

### 2. Environmental Risk Assessment: **LOW**

- No manufacturing, no significant Scope 1 combustion, no water-stress or stranded-asset exposure. Carbon intensity per revenue dollar is structurally low and falling as high-margin software/data revenue scales.
- Genuine but sub-material issues: energy for NGS compute and AI model training; Scope 3 single-use plastics and reagents (Illumina is a disclosed partner/supplier); biohazardous and regulated medical waste handling across CLIA labs.
- **Disclosure gap is the real E issue.** Tempus does not appear to publish a sustainability/TCFD-aligned report with GHG inventory. A shareholder proposal requesting GHG emissions and climate-risk reporting reportedly drew **~70.4% support** in the 2025 proxy season (per third-party proxy-season analyses; I could not verify the tally directly — SEC pages returned 403). If accurate, that is a strong majority protest vote against the board's recommendation — a *governance* problem more than an environmental one.
- No EU CBAM exposure of consequence; CSRD likely out of scope at current EU revenue.

**Verdict: Low.** Do not pay for E risk here; do flag the missing disclosure as a symptom of weak shareholder responsiveness.

---

### 3. Social Risk Assessment: **HIGH**

**The dominant issue: genetic data privacy.** In February 2025 Tempus acquired Ambry Genetics for ~$600M and, as a condition, absorbed a database containing genetic information of hundreds of thousands of individuals, which it used to train AI models and licensed onward to 70+ counterparties including AstraZeneca, BMS, Pfizer, GSK, Incyte and Servier. Multiple class actions were **consolidated on 15 April 2026 as *Farrier et al v. Tempus AI, Inc.* (N.D. Ill.)**, alleging violations of the **Illinois Genetic Information Privacy Act (GIPA)** and other state statutes — specifically that Tempus compelled Ambry to disclose data and then re-disclosed it without written consent, in deals the complaint values at **~$1.1 billion**.

This is the single most important ESG fact about the company, because:
- GIPA carries **statutory damages of $2,500 (negligent) to $15,000 (intentional/reckless) per violation**. On a several-hundred-thousand-person class, theoretical exposure is in the **billions** ($1.25B–$7.5B). Realistic settlements discount that by an order of magnitude, but the asymmetry is real and the tail is fat.
- More important than damages is **injunctive/business-model risk**: a ruling that de-identified genetic data is inherently identifiable — the plaintiffs' core theory — would undercut the legal premise of the entire Insights licensing model and the "de-identified" representation in customer contracts.
- It sits atop an already-damaged credibility base: Ambry had a prior HIPAA matter with HHS/OCR (reported settlement), and the securities complaint alleges Ambry's model rested on "aggressive and potentially unethical business practices" — i.e. billing. That implies **payer/FCA tail risk** in Diagnostics, the larger revenue segment.

**Mitigants (genuine):** product-safety and clinical governance look comparatively strong. The FDA granted a **tumor-only indication for xT CDx (May 2026)**, making Tempus the first lab with CDx approval for both tumor-only and tumor-normal comprehensive genomic profiling; PRISM2 validation published in *Nature Medicine*. Regulatory-grade validation is the best defence against AI-washing claims. No disclosed workforce-safety controversies, no disclosed breach of the 45M-record data estate (a breach would be catastrophic — treat as a latent, unquantified risk).

**Verdict: High.** Not because of labour or community issues, but because the consent basis of the core data asset is under legal attack.

---

### 4. Governance Quality Score: **3 / 10**

| Item | Assessment |
|---|---|
| **Dual-class structure** | **Severe.** Class B carries **30 votes/share**; CEO/Founder/Chairman Eric Lefkofsky controls roughly **~60% of voting power on <25% of economic interest**. Tempus is a controlled company; minority shareholders cannot effect change. |
| **CEO/Chairman duality** | **No independent chair.** Combined with dual-class, there is no meaningful check on executive authority. |
| **Related-party transactions** | **The central red flag.** Pathos AI is Lefkofsky-affiliated and holds collaborations with Tempus; the AstraZeneca relationship is alleged to have been restructured via a Pathos "pass-through payment" that reduced AZ's commitment; the SoftBank Japan JV is alleged to resemble **round-tripping of capital** to manufacture revenue and income. These are exactly the transactions that a strong independent board would police — and this board cannot. |
| **Board quality** | Multiple directors/executives reportedly previously associated with companies that **restated financial results**. Board independence count could not be verified (proxy inaccessible), but controlled-company status means independence is structurally compromised regardless of headcount. |
| **Compensation alignment** | Not verifiable within budget. Offsetting signal: insider ownership is high (aligned in theory), but see below. |
| **Insider selling** | **Poor optics.** CEO-related entities sold ~$9.6M; Lefkofsky sold **250,000 shares for ~$17.6M at $70.36 on 27 Oct 2026**, leaving ~50,000 directly held; 775K+ shares sold under 10b5-1 plans. Heavy selling into strength by a 60%-control founder undercuts the "founder alignment" defence. |
| **Capital allocation / shareholder rights** | Serial stock-funded M&A — **Personalis at $1.5B (100% stock, up to 50% cash election)** pending, Paige $101.5M, Ambry $600M, Deep 6 AI — creating dilution and integration risk with no shareholder vote possible. No poison pill identified. |
| **Shareholder responsiveness** | The reported ~70.4% support for a GHG-reporting proposal against board recommendation signals a board out of step with its own shareholders. |
| **Positives** | No disclosed DOJ/FCPA/anti-corruption matters; robust FDA/quality-systems discipline; meaningful founder economic ownership. |

**Score: 3/10.** The structure is legal but value-relevant: it caps the achievable governance score no matter how the committees are composed, because control is not contestable and the related-party risk is concentrated in the controlling shareholder.

---

### 5. ESG Controversies (with financial impact estimates)

| # | Controversy | Status | Estimated financial impact |
|---|---|---|---|
| 1 | ***Farrier v. Tempus AI*** — GIPA/state genetic-privacy class action (consolidated 15 Apr 2026, N.D. Ill.) | Active | **$50–300M probability-weighted settlement**; theoretical statutory exposure $1B+. Plus unquantified **business-model/injunctive risk** to Insights revenue. *Largest single ESG liability.* |
| 2 | **Securities class action** (10b-5/20a; filed 12 Jun 2025; class period 6 Aug 2024–27 May 2025) alleging inflated contract values with related parties, SoftBank round-tripping, Ambry practices, AZ pass-through | Active | **$15–60M** typical settlement range, largely D&O-insured; reputational cost higher than cash cost |
| 3 | **Spruce Point short report** (28 May 2025) — accounting, related parties, "2% of revenue from AI" | Published | **~20% single-day share decline (~$2B+ market cap)**; triggered #2 and permanent governance discount |
| 4 | **AI-washing allegations** (overstated AI capabilities) | Litigation + SEC-wide thematic scrutiny | Reputational; constrains future "AI premium" in multiple |
| 5 | **Ambry prior HIPAA/OCR matter** and alleged billing practices | Resolved/under scrutiny | Modest direct cost; signals compliance culture weakness at acquired entity |

---

### 6. Regulatory ESG Exposure

- **US federal:** HIPAA/HITECH Privacy & Security Rules; **CLIA**; **FDA** LDT oversight and companion-diagnostic labelling (active, and a *strength* — xT CDx approvals); FTC Health Breach Notification Rule; SEC climate-disclosure rule (stayed, immaterial).
- **US state — the acute zone:** **Illinois GIPA** (private right of action, statutory damages — the live litigation), **Texas CUBI**, **Washington My Health My Data**, California CMIA/GINA, plus ~20 comprehensive state privacy laws. Genetic data is the most heavily protected category and Tempus operates a national lab footprint.
- **EU/UK:** **GDPR Art. 9** special-category genetic data and international transfer rules; **EU AI Act** — medical AI (Algos, Next, PRISM2-class models) likely **high-risk**, with conformity-assessment obligations phasing in 2026–2027; **EU IVDR** for any EU-marketed diagnostics. This is a rising compliance-cost line if Tempus scales in Europe.
- **ESG-linked debt covenants:** **None identified.** Capital structure is convertible notes/equity, not sustainability-linked loans. No CBAM exposure.
- **Reimbursement (quasi-regulatory):** CMS/PAMA coverage decisions and private-payer medical-necessity policies are the real "licence to operate" gate for Diagnostics — more financially binding than any ESG rule.

---

### 7. Overall ESG Rating: **ESG RISK**

Tempus is an **environmental non-issue, a social risk, and a governance laggard.** It cannot be rated "Average" because (a) a consolidated class action challenges the lawful basis of the company's principal high-margin asset, and (b) a founder holds ~60% of votes on <25% of economics, chairs his own board, and transacts with entities he is affiliated with — the precise fact pattern the securities suit targets. On the conventional E-and-S-policy axis it would score far better (strong FDA/clinical validation, real patient-benefit mission, no labour or safety controversies). The rating is driven by **governance and data-ethics tail risk, not by ideology.**

---

### 8. ESG Investment Implication: **NEGATIVE (risk-overlay)**

**This is not a thesis-killer, but it is a discount-rate and position-sizing issue — and the market is currently pricing none of it.**

1. **Cost of equity, not revenue, is where ESG bites here.** A beta of 3.6 plus non-contestable control plus unresolved genetic-privacy litigation argues for a governance/legal risk premium. At ~$13.9B market cap on ~$1.6B annualised revenue and only ~$65M FY26 adjusted EBITDA, the valuation rests on terminal data-licensing economics — the exact cash flows the GIPA suit imperils. **A single adverse ruling on "de-identified" genetic data would compress the multiple, not just the earnings.**
2. **Watch three specific catalysts:** (i) class certification and any *Farrier* motion-to-dismiss ruling — the key binary; (ii) whether any pharma counterparty (AZ, BMS, GSK, Pfizer) renegotiates or pauses data licences citing consent risk (a customer-behaviour tell that would be far more damaging than the lawsuit itself); (iii) the 2026 proxy — board composition, related-party disclosure expansion, and whether the GHG proposal returns with majority support.
3. **Governance is a permanent haircut, not an event.** With ~60% voting control, no independent chair, and a founder selling into strength, there is no activist path and no takeover premium. Minority holders are permanent passengers. Related-party optics (Pathos AI) will recur as long as the founder incubates adjacent ventures.
4. **Genuine positives to weigh against this:** FDA CDx leadership and *Nature Medicine*-grade validation are the strongest possible rebuttal to AI-washing claims; Data & Applications growth of 33% at >71% GM is real, not narrative; the shift to positive adjusted EBITDA reduces going-concern/dilution pressure.

**Recommendation:** Treat ESG as a **material risk overlay — underweight-capable, not disqualified.** Size the position for a plausible $50–300M litigation hit *and* a scenario in which the Insights data-licensing model requires re-papering with consent. Any long thesis should explicitly underwrite the GIPA outcome rather than assume it away; any short thesis should respect the FDA/CDx franchise and the 33% data-segment growth. I would not initiate or add ahead of a ruling on the motion to dismiss.

---

**Data gaps (disclosed honestly):** 10-K and DEF 14A could not be retrieved (tool returned "none found"; SEC direct fetches returned HTTP 403), so board-independence counts, exact compensation metrics, and verified vote tallies are unconfirmed. No GHG inventory, no third-party ESG score (MSCI/Sustainalytics), and no sustainability-linked debt were found. The ~70.4% GHG-proposal figure is sourced to a third-party proxy-season analysis and is unverified. Environmental conclusions rest on business-model inference (no manufacturing footprint) rather than reported data.
