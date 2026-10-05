# Geo Legal Researcher

- Symbol: AMD
- Elapsed: 246.7s

---
I have enough to compile the report. Direct 10-K retrieval failed (tool limitation), but I sourced the key filing data via secondary pages that quote the AMD 10-K, 8-K, and earnings calls.

---

# AMD — Geopolitical & Legal Risk Assessment
**Advanced Micro Devices, Inc. (NASDAQ: AMD)** | Santa Clara, CA | Semiconductors | FY2025 revenue: **$34.6B** (2024: $25.8B; 2023: $22.7B) | Market cap: ~$1.03T

---

## 1. Geographic Risk Map (FY2025, AMD 10-K billing-location basis)

| Country/Region | Revenue Exposure | Est. % of Revenue | Risk Level | Notes |
|---|---|---|---|---|
| **United States** | ~$11.4B | ~33% | Low–Med | HQ, largest market; procurement priorities (DoD/cloud) are tailwinds; regulatory base |
| **China & Hong Kong** | $7.8B (2024: $6.2B; 2023: $3.4B) | **22.4%** (2024: 24.2%) | **Very High** | Second-largest billing region; direct target of U.S. export controls; also exposed to Beijing import-approval/retaliation risk |
| **Taiwan** | ~$5.2B | ~15% | **High** | Large billed-revenue region AND the manufacturing choke point (nearly all leading-edge wafers from TSMC) |
| **Singapore** | ~$4.3B | ~12% | Med | Major ODM/distribution hub; transshipment risk for controlled parts |
| **Rest of World** (Japan, Germany, Korea, etc.) | ~$5.9B | ~17% | Med | No disclosed single-country concentration beyond the above |

*International sales ≈ 67% of total (US 33%); ~65–66% in 2022–2023 per prior 10-Ks.* Customer concentration: a small number of OEMs/cloud hyperscalers/ODMs drive a large share of revenue (five customers historically >40–50% in segments), amplifying any single-market shock.

**Supply-side geography:** AMD is a fabless designer — essentially all advanced (≤5nm) wafers are produced by TSMC in **Taiwan**, with GlobalFoundries (US/Dresden) for some mature nodes and packaging/assembly across Taiwan, Malaysia, China and Singapore. This inverts the usual country-risk picture: ~15% of revenue is billed in Taiwan, but *the entire product portfolio depends on Taiwanese fabrication.*

---

## 2. Top 3 Geopolitical Risks

**Risk 1 — U.S.-China export controls on AI accelerators: revenue truncation, confirmed and recurring**
- **Probability: ~High (already materialized, policy direction intensifying)** | **Impact: High**
- April 2025: BIS license requirement for MI308-class Instinct GPUs to China triggered an **up to ~$800M charge** (8-K); AMD ultimately booked ~$440M net charge in 2025 after reversing ~$360M when Q4 license sales (~$390M to China) materialized.
- Full-year 2025 revenue hit estimated at **~$1.5B** from tightened curbs per company guidance (The Register / Astute).
- Jan 2026: new rule covering **MI325**; limited licenses granted Feb 2026; management explicitly guided **no China revenue beyond Q1 2026**; Q1 2026 China revenue was "not material." CEOs note the licensing regime is "very dynamic."
- If this regime broadens (e.g., to less-advanced SKUs) it would hit the full $7.8B China billing line, not just data-center AI GPUs.

**Risk 2 — Taiwan Strait escalation / TSMC single-point manufacturing concentration**
- **Probability: Low–Moderate** | **Impact: Severe (existential to supply)** | Timeframe: sustained
- AMD's entire leading-edge wafer supply sits in Taiwan (TSMC). A blockade or conflict would halt production with no short-term substitute; recovery measured in quarters-to-years even under the most benign scenario. US/EU "friend-shoring" (TSMC Arizona, Japan, Germany) is diversifying the industry, not AMD's near-term output.
- Any Taiwan shock would also erase $5.2B of billed revenue and destabilize the global AI-chip customer base simultaneously.

**Risk 3 — Beijing's countermeasures (dual-direction exposure)**
- **Probability: Medium** | **Impact: Medium–High**
- China's new Anti-Sanctions Law enables retaliation and compensation claims against foreign firms that comply with US controls; MOFCOM has blacklisted US firms and banned trade with six US companies; export controls on drones/rare materials (gallium, germanium — inputs to chip manufacturing) are live escalation tools.
- Even chips Washington licenses may not clear Beijing's import approval (AMD disclosed it "did not yet know" whether MI325 imports would be permitted). AMD also holds stakes in China-based JVs (x86/Hygon lineage), which raises dual-use licensing and forced-transfer sensitivities.

---

## 3. Legal & Regulatory Highlights

**Export-control regime (primary regulatory exposure):** BIS license requirements (Apr 2025 MI308; Jan 2026 MI325); AMD has an active license pipeline and recurring inventory/purchase-commitment write-down risk. Political dimension: Republicans in Congress have proposed moving export-control enforcement out of Commerce — authority churn adds compliance uncertainty.

**Active litigation:**
- **Adeia v. AMD** — patent-infringement suit over 3D V-Cache/X3D die-stacking technology (ten patents); ongoing, with parallel ITC/PTAB proceedings. Legacy peer Xilinx IP litigation (e.g., Sentient Sensors appeal) also runs under the AMD umbrella.
- **"Llano" securities class action** — long-running investor suit alleging misleading statements on the 2011 Llano processor defects; class status granted, litigation continues.
- **Consumer/competition matters** — historically settled (Intel/AMD antitrust 2009, FTC), but routine warranty/consumer claims persist at immaterial levels.

**Regulatory posture:** SEC oversight routine; no active SEC/FTC enforcement disclosed in our window. Key *political* regulatory lever is the export-control apparatus itself (see above) plus tariffs — the 2025–26 tariff cycle adds cost and supply-chain volatility for a fabless firm reliant on cross-border wafer/logistics flows.

**Litigation risk assessment:** monetary exposures currently look manageable (patent damages, not existential), but the **export-control charge cycle is the true earnings-risk item** — it has already cost ~$0.4–0.8B in a single year.

---

## 4. Compliance Red Flags

1. **Third-party diversion of restricted parts (elevated).** In 2026 a leading semiconductor analyst called on the US government to investigate AMD after restricted-class Instinct chips were found in China; AMD attributed this to a customer/hyper-distributor. Although alleged conduit liability sits with intermediaries, BIS enforcement frequently reaches the manufacturer's end-user vetting and red-flag controls. Expect scrutiny of AMD's distributor and ODM due-diligence programs.
2. **China JV / dual-use licensing exposure.** AMD's equity stakes in Chinese x86 ventures sit squarely at the intersection of US export controls and China's Anti-Sanctions Law — a classic "damned if you comply, damned if you don't" compliance posture (US enforcement vs. Chinese retaliation claims).
3. **High-velocity rule changes.** Two new China-control rule sets inside 12 months (Apr 2025, Jan 2026) plus proposed enforcement-restructuring means AMD's compliance architecture must be continuously re-engineered; slippage risk is real in this environment.
4. **No FCPA/AML red flags surfaced** in the review window.

---

## 5. Overall Geopolitical/Legal Risk Rating: **HIGH**

**Rationale:** This is a rare case where the *largest geopolitical risk has already materialized and is ongoing* — AMD has taken ~$440M net charges, lost guidance visibility on its #2 market (~22% of revenue), and management itself is forecasting near-zero China AI-revenue. Layer on TSMC/Taiwan single-point manufacturing risk and escalating Beijing countermeasures, and the risk matrix is dominated by left-tail, correlated events. Offsetting factors: US/Japan/Europe demand strength, mandatory license flows (not an outright ban), and asset-light fabless model; litigation and FCPA exposure are comparatively modest.

*Data caveat: the 10-K text-retrieval tool failed for AMD; geographic and charge figures are sourced from the AMD 10-K/8-K/earnings-call data as reported through BloFin analysis, Investing.com, The Register, and Astute Group. Peer-comparison of export-control exposure (NVDA, TSM) is available but not priced in this note.*
