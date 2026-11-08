# Nonfin Risk Analyst

- Symbol: FROG
- Elapsed: 63.1s

---
# Non-Financial Risk Assessment — JFrog Ltd. (NASDAQ: FROG)

**Price $100.98 (Nov 6, 2026) | Market cap ~$12.2B | ~1,800 FTE | Israeli-domiciled, Sunnyvale HQ | FY guide $680–682M**
**Risk assessment date: post-Q3 2026 (reported Nov 5, 2026)**

Context that shapes everything below: FROG is up ~110% over 12 months, jumped **+35% on Nov 6** after Q3 revenue of $179.2M (+31% y/y) and a $76M multiyear cloud deal. Non-financial risk is therefore *priced for perfection* — the stock now carries a high multiple into a business whose trust proposition was publicly attacked twice in 2026.

---

## 1. Governance Quality Rating: ADEQUATE (borderline weak)

| Factor | Evidence | Assessment |
|---|---|---|
| CEO/Chairman duality | Shlomi Ben Haim is co-founder, CEO **and Chairman**; the 2025 proxy explicitly asks shareholders to approve his combined service for a three-year term | ❌ Concentration of power |
| Lead independent director | Board designated Mr. Sela as lead independent director (2025 PRE 14A) | ✅ Partial mitigation |
| Founder tenure | CEO since April 2008 (~18.6 yrs) | ⚠️ Entrenchment / key-person |
| Pay alignment | CEO total comp ~$16.8M, **96.3% equity-based** (3.7% salary) | ✅ Aligned, but richly sized |
| Insider alignment | CEO still holds ~4.43M shares post-sales | ✅ Meaningful skin in the game |
| Control failures | No material weakness disclosed; Q3 2026 SOX 302 cert clean (Ben Haim, Nov 6, 2026) | ✅ |
| SEC enforcement | **Zero** actions returned in EDGAR full-text search | ✅ Clean |
| Related-party transactions | None surfaced in available disclosure | ✅ (caveat: proxy text not retrievable) |

**Verdict:** Structurally sound but personality-centric. A founder holding both Chair and CEO for 18 years, at a company where "trust" is the product, means board challenge of management is structurally weaker than ideal. The lead independent director is a real mitigation but not a substitute for an independent chair.

---

## 2. Regulatory Risk Summary: MODERATE

**Active/pending litigation**
- **Securities class action / plaintiff-firm activity.** Multiple firms (Levi & Korsinsky, Howard G. Smith, Rosen, Bronstein Gewirtz) have live FROG actions. The core theory traces to the **Aug 7, 2024 guidance cut**, when management told investors "we now expect cloud revenue growth to slow relative to prior expectations" — FROG fell ~5% and later ~25%+ on follow-through. One solicitation cites a class period of **Feb 7, 2025 – Oct 2, 2025**, indicating litigation risk extends into 2025 disclosure. *Status of consolidation/dismissal/settlement not confirmed — see gaps.*
- No antitrust, IP, product-liability, or FDA/FCC-type approval risk. No GDPR/CCPA enforcement action found.

**Regulatory tailwinds/headwinds:** JFrog is a *beneficiary* of regulation (audit evidence, signed compliance, DevGovOps, supply-chain attestation) — its Oct 2026 product launches are explicitly built around compliance mandates. That partly offsets regulatory risk.

**Note:** The absence of SEC enforcement is a genuine positive and distinguishes FROG from peers with disclosure-controls histories.

---

## 3. Insider Activity Analysis: NET SELLING — ONE-DIRECTIONAL

**Net direction over trailing 12–24 months: heavily negative.** MarketBeat aggregates **~4.14M FROG shares sold over 24 months**, with essentially **no open-market purchases** by officers or directors.

| Insider | Date | Shares | Value | Note |
|---|---|---|---|---|
| CEO Ben Haim | Feb 5, 2026 | 25,000 | ~$1.2M | 10b5-1 plan |
| CEO Ben Haim | May 29, 2026 | 51,237 | **$3.84M** | 10b5-1 |
| CEO Ben Haim | Oct 7, 2026 | 15,000 | **$1.46M** (avg $97.52) | 10b5-1 |
| CTO Landman (co-founder) | Feb 4, 2026 | 15,889 | ~$0.57M @ $36.15 | Sold near 52-wk low |
| CTO Landman | Apr 10, 2026 | 15,000 | $0.64M @ $42.87 | |
| CTO Landman | Aug 13, 2026 | 45,000 | **$4.1M** | 10b5-1 |
| CTO Landman | Oct 5, 2026 | 45,000 | **~$4.0M** | 10b5-1 |
| CRO Tali Notman | Recurring | — | — | Consistent seller |

**Interpretation:** All disclosed sales appear to run through **pre-arranged Rule 10b5-1 plans**, which legally de-risks the trades and explains selling at $36 as well as $97 — evidence of mechanical, calendar-driven programs rather than opportunistic dump-on-news. That is the fair reading.
**However:** the *signal* is still weak. There is no insider buying at any point in the last two years — including the February 2026 drawdown to $34, when insiders were selling rather than stepping in with personal capital. Combined with a ~$12B valuation on ~$700M revenue, "no buyers at the bottom, sellers at the top" is not a management team signalling conviction. **Worth an escalation note, not an accusation.**

---

## 4. Top Operational Risks

1. **Product security failures at the core of the brand (SEVERE — the #1 risk).** CVE-2026-82329, a **CVSS 9.8** authentication bypass in JFrog Access, was disclosed **Aug 28, 2026** and confirmed **exploited in the wild by Sep 1** — attackers minted admin tokens via a "phantom" default join key, enumerating users, groups, credentials and federated access. Self-hosted Artifactory branches required patching (7.111.21 / 7.117.28 / 7.125.20 / 7.133.29 / 7.146.38 / 7.161.20); cloud was mitigated. Fastly reported exploitation "exploded in 72 hours" with mass scanning; California's CAL-CSIC issued a formal cyber advisory. SentinelOne separately catalogs **CVE-2026-65616 and CVE-2026-69107**, additional Artifactory auth-bypass flaws in the same year — i.e., **a pattern, not a one-off**. Admin access to a central artifact repo converts intrusion into **substitution**: build-pipeline tampering and malicious pushes to the customer's own downstream customers. For a company selling supply-chain security, this is existential-brand risk, and it invites customer contractual/SLA claims and regulatory scrutiny.
2. **Geographic and key-person concentration in Israel.** Roughly **950 of ~1,800 employees, including the majority of R&D, are Israel-based** (10-K: R&D primarily Israel and India; HQ Netanya). Regional escalation, mobilization, or travel/logistics disruption hits the engineering core directly. Layered on top: co-founder CEO (18 yrs) + co-founder CTO — thin bench at the top of product and strategy.
3. **Consumption-model revenue instability + vendor/deployment dependency.** Revenue is consumption-based (cloud grew 50% y/y in Q1 2026), which behaves well in upcycles and badly on any optimization pause — precisely the dynamic that produced the **Aug 2024 guidance cut and the litigation that followed**. Customers skew to self-hosted Artifactory (which is where the exploit landed), meaning a large installed base whose security posture JFrog does not fully control. SOC 3 (FY2025) attestation and a published FY2025 sustainability report are genuine control positives.

---

## 5. Reputational Risk Assessment: ELEVATED

**Negative drivers**
- **Trust-brand damage from the CVE.** "Exploited Artifactory bug" headlines in CSO Online, Fastly, SOC Prime and a state cyber advisory are materially worse for JFrog than for a generic SaaS vendor — customers buy FROG *to prevent* this outcome.
- **AI-disruption repricing, twice.** On **Feb 20, 2026** the stock fell **24.6% intraday ($50.29 → $37.75, 15.1M shares — 3x normal volume)** after Anthropic unveiled **Claude Code Security**; a separate Anthropic "Mythos" announcement erased **~$700M of market value in minutes**. The market has repeatedly repriced FROG as an AI casualty, not an AI winner, and will do so again on any similar headline.
- **Multiples amplify everything.** A ~17x sales valuation means any execution wobble or security incident produces an outsized drawdown and a fresh wave of plaintiff-firm solicitations.
- Sell-side is split: "AI tailwinds, massive valuation" (Seeking Alpha sell rating) with direct **GitLab** competition and consumption-model risk cited.

**Positive offsets**
- Strong operator narrative: 451% surge in malicious npm packages in JFrog's own 2026 threat report positions it as the *solution*; new AI-SEC and DevGovOps launches (Oct 21, 2026) are on-message; institutional 13F flows (Perpetual, Gibbs Wealth) are still net adding. Social/press sentiment is currently **net positive** post-Q3, which is precisely why the next incident would be so costly.

---

## 6. Overall Non-Financial Risk Rating: **HIGH**

Rationale: no fraud indicators and a clean SEC enforcement record, but four risks compound rather than offset — (a) a pattern of critical, actively exploited product vulnerabilities in a company whose entire value proposition is supply-chain trust; (b) founder duality plus dual key-person concentration; (c) ~53% of headcount and most R&D in a conflict-exposed geography; (d) live securities litigation and one-directional insider selling, against a valuation with no room for error. Any single item alone would be Moderate. Together, at 17x sales, they warrant **High**.

---

## 7. Red Flags Requiring Escalation

1. **CVE-2026-82329 (CVSS 9.8) exploited within 72 hours of disclosure, plus two further Artifactory auth-bypass CVEs in 2026.** Escalate to: is there evidence of a *material* customer compromise flowing through JFrog, and has JFrog disclosed the customer/revenue impact? An unremediated admin-token backdoor at any marquee customer is a contractual and disclosure event. **Request: JFrog's 8-K/10-Q disclosure language on this incident and any customer notification.**
2. **No insider open-market purchases in 24+ months while ~4.1M shares were sold** — including sales at $36. Not fraudulent, but zero conviction signal from the people with the best information.
3. **CEO simultaneously Chairman for 18 years**, with the board seeking a three-year authorization for the combined role. Weakest governance datum.
4. **Securities class action history is not resolved** — the Aug 2024 cloud-growth guidance cut and a 2025 class period remain live in plaintiff-firm marketing. Confirm whether any case has survived a motion to dismiss; a surviving complaint raises the odds of a restatement-adjacent discovery event.
5. **Concentrated Israel R&D footprint (~950 staff)** — no disclosed business-continuity redundancy for the engineering core.

### Data gaps (disclosed honestly)
- **10-K risk factors were not retrievable** (tool returned "No 10-K found"; the SEC archive URL returned HTTP 403). Board independence ratios, auditor identity, full related-party disclosure, and **customer concentration percentages** are therefore unverified.
- The 2025 DEF 14A could not be fetched directly (SEC 403); governance detail is drawn from search snippets of the 2025 proxy and PRE 14A.
- Litigation **status** (dismissed / consolidated / settled) is unconfirmed; plaintiff-firm pages are marketing and their class-period dates conflict (Aug 8, 2024 vs. Feb 7, 2025 – Oct 2, 2025).
- No cybersecurity-incident-specific 8-K was located for the Artifactory CVE — **absence of a filing here is itself worth verifying**, since a material customer breach could trigger Item 1.05.

### What would change the rating
- **To Critical:** evidence that a named customer was compromised via the Artifactory flaw, or a restatement / adverse internal-control finding.
- **To Moderate:** an independent chairman appointed and the lead-independent structure formalized; a clean vulnerability-disclosure quarter with no repeat CVEs; and any single insider open-market purchase.
