# Nonfin Risk Analyst

- Symbol: FROG
- Elapsed: 211.9s

---
# NON-FINANCIAL RISK ASSESSMENT — JFrog Ltd. (NASDAQ: FROG)

**As of:** October 15, 2026 | **Price:** $94.54 | **Market cap:** ~$10.2B | **Sector:** Technology — Software Application (DevOps / software supply chain security)
**Domicile:** Israel (HQ Sunnyvale, CA) | **IPO:** Sept 2020 | **Employees:** ~1,800 | **Founder-CEO:** Shlomi Ben Haim

---

## 1. Governance Quality Rating: ADEQUATE (with concentration-of-power flags)

**Positives**
- **Single class of ordinary shares — one share, one vote.** No dual-class super-voting structure (charter references Ordinary Shares voting "together as a single class"). This is a genuine differentiator versus most founder-led 2020-vintage software IPOs and means minority holders are not structurally disenfranchised.
- **Committee independence appears intact:** Audit — Luis Visoso, Sigal Zarmi, Barry Zwarenstein; Compensation — Andy Vitus, Yvonne Wassenaar; Nominating/Governance separate. Names suggest a majority-independent ~9-person board with relevant financial/tech expertise (Zwarenstein = former CFO; Zarmi = former CIO).
- **CFO stability:** Ed Grabscheid appointed effective FY2023 year-end, still in seat. No 2026 finance leadership churn, no auditor change or restatement disclosed.

**Negatives**
- **CEO/Chairman duality:** Shlomi Ben Haim is Co-Founder, CEO **and** Chairman. Combines agenda-setting and oversight in one person at a founder-controlled company — weakens board challenge capability, particularly on capital allocation and product-security remediation.
- **Classified (staggered) board:** Class III directors (Yoav Landman, Yossi Sela, Elisa Steele, Luis Visoso) stand at the 2026 AGM. Staggering plus founder/VC-affiliated seats (Landman = co-founder/CTO; Vitus = Scale Venture Partners; Sela = Gemini Israel Ventures) blunts shareholder ability to force change.
- **Insider ownership ~18%** concentrated in founders (Landman ~4.1%), reinforcing entrenchment.

*Net: structurally better than peer founder-led software (no dual class), but operationally over-concentrated in the founder-CEO.*

---

## 2. Regulatory Risk Summary — **Low enforcement risk; rising product-security & compliance burden**

- **SEC/DOJ:** No enforcement actions, subpoenas, or investigations surfaced in EDGAR full-text search for FROG. **Clean.**
- **Securities litigation:** No *filed* class action identified. Bronstein Gewirtz & Grossman maintains an open **investigation solicitation** — but it is tied to the **August 2024 guidance cut** (stock −27.5%), not to 2026 events. Plaintiff-firm advertising risk is elevated after every drawdown, not evidence of misconduct.
- **Product-security regulation — the live exposure:** Three Artifactory auth-bypass flaws (`CVE-2026-42016`, `CVE-2026-42018`, `CVE-2026-82329`) were **added to CISA's Known Exploited Vulnerabilities catalog** in September 2026. Under **BOD 26-04**, US federal agencies were given **two weeks** to patch. Consequences: (a) federal procurement friction / reputational stain in JFrog's most security-sensitive segment, (b) potential congressional or agency inquiry into disclosure timelines, (c) indemnity/contractual exposure to breached customers.
- **Data privacy:** As a SaaS custodian of customer artifacts, binaries and increasingly **AI models**, JFrog carries GDPR/CCPA processor obligations. No breach notification of JFrog's own cloud identified — exploitation observed against **self-hosted** instances (customer-operated), which limits JFrog's direct liability but not its reputational exposure.
- **Regulatory tailwind:** EU **Cyber Resilience Act**-driven compliance demand is a revenue driver (AppTrust positioned as automating audit prep).

---

## 3. Insider Activity Analysis — **NET SELLING, ZERO BUYING (strongly negative signal)**

**Twelve months to Oct 15, 2026:** ~40 Form 4 filings across **~10 distinct insiders**, with **no open-market purchases identified**. Selling is one-way and programmatic.

| Date | Insider | Size | Notes |
|---|---|---|---|
| Feb 5, 2026 | CEO Ben Haim | 25,000 sh | 10b5-1 adopted previously |
| May 29, 2026 | CEO Ben Haim | 51,237 sh (~$3.8M) | Near the $79 local peak |
| Aug 7, 2026 | CEO Ben Haim | 15,000 sh (~$1.46M) | Five tranches, 10b5-1 |
| Oct 7, 2026 | CEO Ben Haim | 15,000 sh (~$1.46M) | 8,330 @ $97.13 wtd avg; retains **4.43M shares** |

**Interpretation:** All sales are under Rule 10b5-1 plans, which mutes the informational signal of any single trade — but the *aggregate* pattern is unambiguous: insiders sold persistently through a **+100% twelve-month rally** ($47 → ~$95–104) and did not buy a single share during the February 2026 crash to $34. Management's own money did not treat the −25% AI-disruption drawdown as an opportunity. CEO retains a large, still-material stake (aligning him with shareholders, but also confirming this is diversification, not loss of conviction).

**Additional flag:** A **$300M buyback** was authorized in February 2026 while the company remains **GAAP-unprofitable** (Q2'26 GAAP EPS −$0.03) and insiders are selling. Corporate cash is being used to absorb equity while executives diversify — a capital-allocation question for the board.

---

## 4. Top Operational Risks

1. **Product security failure at the trust anchor — SEVERE.** Three high/critical Artifactory vulnerabilities exposing **authentication bypass and admin privilege escalation** were chained in the wild between **Aug 15 and Sep 8, 2026**, with attackers minting admin accounts, installing malicious plugins, executing shell commands and exfiltrating cluster keys. **OpenInfra Europe (Linux Foundation Europe) confirmed its self-hosted Artifactory was breached** via CVE-2026-82329 — public for only ~3 days before compromise. All three are in CISA KEV. Critically, this is not an isolated bug: **three separate auth bypasses patched within five weeks (Jul 27, Aug 12, Aug 28)** points to a **systemic weakness in Artifactory's authentication architecture**. Because Artifactory is the system of record for every downstream binary and container, a compromise propagates into customers' entire software supply chains — the maximum-blast-radius failure mode for this business.
2. **Self-hosted install base is an unpatchable long tail.** Cloud is growing +53% y/y but roughly half of revenue remains self-managed, where JFrog **cannot force remediation**. Expect repeat exploitation events, named victim disclosures, and persistent drag on federal/regulated-industry sales.
3. **Key-person and geographic concentration.** Two co-founders (CEO since 2009, CTO Landman) embody product strategy and customer relationships, with no visible succession. Substantial R&D headcount in **Israel** exposes business continuity to regional conflict and military reserve call-ups — an unhedged, uninsurable operational dependency.
4. **AI-driven competitive compression.** Anthropic's **Claude Code Security** launch triggered a **−24.6% single-day decline (Feb 20, 2026)** and a multi-trillion-dollar software selloff. Autonomously-discovered Artifactory exploits (OpenAI agents reportedly found and exploited a JFrog vuln) cut both ways: they validate the security narrative while threatening the value of Xray-style scanning and the artifact-management moat. Competitors: Sonatype, Snyk, Cloudsmith, GitLab/GitHub, plus AI-native entrants.

---

## 5. Reputational Risk Assessment: **ELEVATED**

- **Negative:** Named customer breach at OpenInfra Europe; three CISA KEV listings in one month; a federal two-week patch mandate. For a company whose entire pitch is "trusted software supply chain," being the *attack vector* is the most damaging possible narrative. It also coincides with a ~17% share decline from the Aug 27 high ($104.03) to Sep 8 ($86.73).
- **Mitigants:** Advisories and patches were issued promptly and proactively (Jul 27 / Aug 12 / Aug 28), the company publishes a formal security-advisory channel, it runs an active security research arm, and it partnered with **Wiz** (Sept 2, 2026) to close AI-era threat gaps. JFrog is behaving like a competent security vendor responding to a hard problem — the risk is that the *frequency* of the problem is escalating.
- **Sentiment/valuation risk:** The stock is a high-beta AI-disruption proxy. It moved −10.4% on a *bullish* Q4 print (Feb 12), −24.6% on a competitor's product launch, +24% on Q1 results, +16% on Q2 results, and −7.4% on an unrelated sector selloff (Oct 14). Narrative, not fundamentals, is driving the tape — a standing communications risk.

---

## 6. Overall Non-Financial Risk Rating: **HIGH**

Weighted primarily on **operational/product-security risk** (active in-the-wild exploitation of the flagship product, systemic auth weaknesses, unpatchable self-hosted base) and **insider-selling signal**, partially offset by **adequate governance** (single share class, independent committees, no enforcement history, no fraud indicators) and **genuinely strong fundamentals** (Q2'26 revenue +29%, cloud +53%, FY26 guide $648–652M, EPS beats, ~$142M FCF).

This is **not** a fraud or integrity call — it is a trusted-infrastructure company whose product has become a live attack surface while its own executives sell.

---

## 7. Red Flags Requiring Escalation

1. **Systemic auth architecture weakness in Artifactory.** Three auth-bypass CVEs in five weeks, all exploited, all in CISA KEV, with one confirmed foundation victim. Escalate: how many customer instances compromised; notification and indemnity obligations; whether federal/regulated customers affected; whether JFrog's own cloud was probed; cyber-insurance adequacy. **This is the thesis-level risk.**
2. **CEO/Chairman duality + classified board + founder concentration (~18%).** No independent chair to force remediation urgency on product security. Recommend engagement on splitting the chair role.
3. **Twelve months of one-way insider selling (~10 insiders, ~40 Form 4s) with zero purchases** — including no buying during the 55% drawdown to $34.
4. **$300M buyback while GAAP-unprofitable** and insiders selling — capital-allocation discipline question.
5. **AI-disruption narrative risk** — a competitor's product launch erased a quarter of market value in one session. Position-sizing and expectation-setting issue for the memo.

---

### Data Gaps (disclosed, not inferred)
The filing-text tools returned no 10-K / 10-Q / DEF 14A for FROG and SEC.gov blocked direct fetch (HTTP 403), so the following are **unverified**: executive compensation structure and SBC as % of revenue, exact net dollar retention, customer concentration (top-10 %), precise board independence count, auditor identity, and any disclosed material litigation in Item 3. Findings above are sourced from SEC filing metadata, FORM 4 records, company results releases, CISA/KEV reporting, and press coverage. **Recommend the analyst with EDGAR access verify Artifactory exploitation disclosure language in the Q3 2026 10-Q (due ~Nov 2026) — specifically any loss contingency, customer notification, or indemnification language.**
