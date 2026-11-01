# Geo Legal Researcher

- Symbol: GDDY
- Elapsed: 119.7s

---
## GoDaddy Inc. (GDDY) — Geopolitical & Legal Risk Assessment

**Source note:** The SEC EDGAR direct fetch was blocked (HTTP 403) for both the FY2025 10-K and the 2025 Annual Report, and `fetch_filing_text` returned only the SOX certification exhibit for the 10-Q. Geographic/segment figures below are therefore sourced from filing-derived aggregators (BusinessQuant, FY `gddy-20251231`) cross-checked against GoDaddy earnings releases and trade press. Legal items are sourced from FTC releases, court/class-action filings as reported by plaintiff and IP firms, and financial media. Two gaps flagged explicitly: **exact "Legal Proceedings" footnote language and the FY2025 risk-factor section were not retrievable.**

---

### 1. Geographic Risk Map

FY2025 revenue: **$4.95B** (US $3.32B / 67.1%; International $1.63B / 32.9%). International grew **+11.4%** vs US **+6.8%** — non-US is the faster-growing and rising share of the mix. FY2026 guide $5.215–5.255B; Q3'26 revenue ~$1.3B, +6%.

| Geography | Rev exposure | Risk level | Rationale |
|---|---|---|---|
| **United States** | ~67% | Low (geopolitical) / **Medium-High (legal)** | Home market; no country risk, but concentrated litigation + FTC consent order + state privacy patchwork. |
| **India** (Gurugram, Hyderabad, Pune) | Part of intl; material — largest offshore headcount hub | **Medium** | 10-K flags continued expansion of employee base "in India, Bulgaria and Serbia" and regulatory/legal exposure "in India, the UK, and…". Transfer-pricing/PE, data-localisation, employment law, rupee FX. |
| **United Kingdom** (Nottingham/Beeston) | Within intl | Low-Medium | Online Safety Act, UK GDPR/ICO posture, post-Brexit data-transfer friction. |
| **EU (Germany, Netherlands, Spain, Romania-Iași, Bulgaria-Sofia)** | Largest slice of the $1.63B intl base | Medium | DSA (GoDaddy has designated a DSA single point of contact), GDPR, NIS2, AI Act, EU Data Act. |
| **Serbia (Belgrade), Portugal, Mexico, Canada, Australia** | Smaller | Low-Medium | Low political risk; FX and labour-law exposure; Canada/Australia are stable common-law jurisdictions. |
| **Russia / Belarus** | ~0% (exited) | Low, but tail risk | Stopped selling/accepting .ru, .com.ru, .org.ru, .net.ru; ceased serving Russian customers in 2024. Roskomnadzor has blocked GoDaddy properties in Russia — reciprocal regulatory/blocking risk remains. |
| **China / Taiwan / Iran / Syria / NK / Cuba** | De minimis | Low but **compliance-sensitive** | Registrar status creates OFAC/EAR screening duties on domain transactions; no meaningful revenue. |

---

### 2. Top 3 Geopolitical / Legal Risks

**1. Litigation cluster (patent + securities fraud) — HIGH probability, MEDIUM-HIGH impact**
- **Express Mobile v. GoDaddy** (D. Del.): November 2025 jury verdict of **$170M** for willful infringement of two website-construction patents (U.S. 6,546,397; 7,594,168) covering Website Builder and Managed WordPress; $100M through 2019 + $70M for 2019–2022. **Willfulness gives the judge discretion to treble → theoretical exposure >$500M**, materially above the ~$14.8B market cap only at the margin, but ~3x annual net income ($875M FY2025). The 2023 defense win was undone by the Federal Circuit's April 2025 claim-construction reversal. Post-trial motions/appeal pending.
- **Johnson v. GoDaddy Inc., No. 1:26-cv-07144 (S.D.N.Y.)**, filed August 2026: securities fraud class period **Sept 3, 2025 – Feb 24, 2026**. The stock fell **14.28% on Feb 24, 2026** after Q4'25 results, on allegations GoDaddy misrepresented **customer acquisition** trends; lead-plaintiff deadline **Oct 20, 2026**. A second ~16.7% drawdown (Jul 31, 2026) on soft guidance/transition issues, with shares down ~58% from the 52-week high at the trough, raises the likelihood of an expanded or amended complaint. **This is the single most investor-visible legal overhang.**

**2. US data-security / consumer-protection regulatory regime — HIGH probability, MEDIUM impact**
- **FTC consent order finalized May 21, 2025** (Matter No. 2023133) settling charges that GoDaddy misrepresented "award-winning security" and failed to implement standard safeguards for 2019–2022, following the **Managed WordPress (MWP) breach affecting ~1.2 million active/inactive customers**. The order is conduct-based (mandatory information-security program, MFA, third-party assessments, no misleading security claims) — no civil penalty was reported. Crucially it creates **long-duration compliance obligations and an audit trail**, and any breach reopens the company to contempt exposure. Related private data-breach litigation and state AG interest are the incremental risk.

**3. EU/UK digital-regulation tightening — HIGH probability, LOW-MEDIUM impact**
- GoDaddy is a regulated **intermediary and accredited registrar** in the EU/UK: DSA notice-and-action and single-point-of-contact duties (already live), GDPR/UK GDPR, NIS2, the EU AI Act (relevant as "Airo" AI features scale — Airo is now >$100M annualised bookings), and EU Data Act cloud-switching obligations that hit hosting economics.
- Simultaneously, **ICANN's April 2024 Registrar Accreditation Agreement DNS-abuse amendments** raise enforcement/compliance costs across the registrar footprint. Cumulative: modest margin drag and increased regulatory-agency surface, not a solvency issue.

*Deliberately de-emphasised:* US-China decoupling, tariffs, and Russia sanctions are **not** material drivers — minimal China revenue, a modest imported-POS-hardware exposure in GoDaddy Payments, and a completed Russia exit. GoDaddy's beta of 0.94 and lack of manufacturing/supply-chain footprint mean classic geopolitical transmission channels are weak.

---

### 3. Legal & Regulatory Highlights

| Matter | Forum / Regulator | Status | Est. financial exposure |
|---|---|---|---|
| Express Mobile patent (willful) | D. Del. → Fed. Cir. | $170M verdict Nov 2025; willfulness finding; appeal expected | $170M base; up to ~$510M if enhanced |
| Securities class action (Johnson) | S.D.N.Y. 1:26-cv-07144 | Filed Aug 2026; lead plaintiff by Oct 20, 2026 | Unquantified; typically settlement-band of low hundreds of $M for a name this size — reserve not disclosed |
| FTC data-security order | FTC (2023133) | Finalized May 21, 2025 | Conduct remedies; ongoing compliance cost |
| MWP breach follow-on litigation | Various | Consolidated/ongoing | Not disclosed in retrievable sources |

Also standard-course: TCPA/telemarketing class actions (referenced in GoDaddy's own risk language re: "class action lawsuits, including lawsuits alleging violations of the Telephone Consumer Protection Act"), UDRP/domain-name disputes (high-volume, individually immaterial), and payments-related regulatory exposure via GoDaddy Payments (money-transmission licensing, AML program obligations, sponsor-bank oversight).

---

### 4. Compliance Red Flags

1. **Post-order cybersecurity posture (elevated):** A second material hosting breach during the FTC order term would be an existential-trust event for a company monetising "security" claims. Highest-severity governance item.
2. **Payments/AML:** GoDaddy Payments moves it into money-transmission/BSA-AML territory (state licences, KYC on merchant customers). *No enforcement action identified,* but the AML program is now a regulated control surface that did not exist pre-2020.
3. **Sanctions screening at the registrar layer:** OFAC/registrar obligations require blocking or rejecting domain transactions for sanctioned parties — a recurring, low-dollar but high-visibility failure mode (GoDaddy already executed a full Russia exit).
4. **Data privacy / cross-border transfers:** 33% international revenue plus Indian/EU processing centres = SCC/DPF transfer exposure and potential Indian data-localisation friction.
5. **No FCPA red flag identified.** Pakistan/India/Bulgaria/Serbia operations are high-headcount but low-bribery-risk (engineering, not licensed/permitting-heavy sales). No DOJ/SEC FCPA disclosure surfaced.

---

### 5. Overall Geopolitical / Legal Risk Rating: **MEDIUM**

**Composition:** *Geopolitical* risk alone would screen **Low** — ~67% US revenue, no China/Russia/EM manufacturing or commodity exposure, stable-jurisdiction international base, and a completed Russia exit. *Legal/regulatory* risk is the binding constraint at **Medium-to-High** on a standalone basis: a $170M willful-infringement verdict with treble exposure, an active securities-fraud class action tied to the Feb 2026 customer-acquisition disclosure failure, and a live FTC consent order over data security. Blended: **Medium**, tilted to the legal side.

**What would move this to High:** (a) treble damages affirmed or a >$300M judgment, (b) class certification surviving in the securities case combined with a reserve disclosure, (c) evidence of a second material breach during the FTC order term, or (d) an EU/UK enforcement action on DSA/age-verification/AML grounds. **What would move it to Low:** reversal or material reduction of the Express Mobile award plus dismissal of the securities complaint.
