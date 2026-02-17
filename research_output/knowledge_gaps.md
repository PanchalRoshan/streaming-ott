# KNOWLEDGE GAPS TRACKER

This file tracks data points that could not be found or verified during research.

## Purpose
- Document systematic data gaps (missing across all sources)
- Track paywall encounters and attempted workarounds
- Identify areas where OTT industry lacks transparency
- Guide future research priorities

---

## FORMAT

Each gap entry should include:
- **Gap ID:** Unique identifier (G-001, G-002, etc.)
- **Domain:** Which research domain this affects
- **Data Point Needed:** Specific metric or finding sought
- **Search Attempts:** What queries/sources were tried (max 3 before logging)
- **Blockers:** Why data couldn't be obtained (paywall, proprietary, non-existent)
- **Impact:** How critical this gap is (HIGH/MEDIUM/LOW)
- **Workarounds Attempted:** Alternative approaches tried
- **Status:** OPEN / ALTERNATIVE_FOUND / ACCEPTED_GAP

---

## GAPS FROM PHASE 0 AUDIT (Pre-Identified)

### G-001: Netflix CDN Bandwidth Consumption
**Domain:** Domain 3 (Competitive Intelligence)
**Status:** RESOLVED
**Priority:** HIGH

**Data Point Needed:**
- Netflix total CDN bandwidth consumption (PB/month or PB/year)
- Netflix CDN cost per subscriber per month
- Netflix CDN vendor mix (% on Open Connect vs commercial CDNs)

**Resolution:**
- **Bandwidth:** Netflix accounts for ~15% of global internet traffic (Statista 2025).
- **Vendor Mix:** ~95% of traffic is served via **Open Connect** (proprietary CDN), with the remaining 5% on commercial CDNs for backup/edge cases.
- **Cost Impact:** By building its own CDN and embedding appliances in ISPs, Netflix has decoupled bandwidth growth from linear cost increases, effectively refuting the "70-90% cost" claim for mature platforms.

---

### G-002: Disney+ Churn Rates by Region
**Domain:** Domain 3 (Competitive Intelligence)
**Status:** OPEN
**Priority:** HIGH

**Data Point Needed:**
- Disney+ monthly/annual churn rate (overall)
- Disney+ churn rate by region (US, Europe, Asia, LATAM)
- Comparative churn rates: Disney+ vs Netflix vs Prime Video

**Why This Matters:**
Retention is identified as most expensive module at scale ($25K/month at 1M users). Need benchmarks to define "acceptable churn" and validate retention investment ROI.

**Search Attempts:** None yet (identified in Phase 0 audit)

**Workarounds to Try:**
1. Disney earnings call transcripts
2. Industry analyst reports (Parks Associates, Ampere Analysis)
3. Subscriber growth vs total subscriber disclosures (infer churn)
4. Regional regulatory filings (EU may require disclosure)

---

### G-003: FAST Channel CPM Rates
**Domain:** Domain 2 (Business Models)
**Status:** RESOLVED
**Priority:** HIGH

**Data Point Needed:**
- FAST channel CPM rates by genre (news, entertainment, sports)
- FAST CPM trends 2020-2024
- FAST vs traditional TV CPM comparison
- Ad fill rate benchmarks for FAST channels

**Resolution:**
- **CPM Rates:** FAST channel CPMs typically range from **$4 to $15** (NewscastStudio 2025). Live content (sports/news) commands higher CPMs ($15+) compared to general entertainment ($4-$6).
- **Ad Load:** FAST channels carry 4-10 minutes of ads per hour (Pluto TV ~10 min, Tubi ~4-6 min).
- **Fill Rates:** SSAI/SGAI implementations have increased fill rates by up to 132%, significantly improving monetization efficiency.

---

### G-004: AV1 Codec ROI Analysis
**Domain:** Domain 1 (Technology Disruption)
**Status:** RESOLVED
**Priority:** HIGH

**Data Point Needed:**
- AV1 bandwidth savings vs H.264/H.265 (% reduction at same quality)
- AV1 encoding cost (compute resources) vs H.265
- AV1 adoption timeline 2024-2030 (% of OTT platforms)
- Device support for AV1 (% of streaming devices with hardware decode)

**Resolution:**
- **Efficiency:** AV1 provides ~30% better efficiency than HEVC/VP9.
- **Adoption:** Netflix reached 30% viewing share on AV1 by Dec 2025.
- **Device Support:** Most mid-to-high end Smart TVs and mobile devices (Android/iOS) now support hardware AV1 decoding.
- **ROI:** Bandwidth savings (30%) outweigh the higher initial encoding compute costs at scale.

---

### G-005: DRM Licensing Costs
**Domain:** Domain 6 (Infrastructure Costs)
**Status:** RESOLVED
**Priority:** MEDIUM-HIGH

**Data Point Needed:**
- Widevine licensing fees (per-stream vs per-user model)
- FairPlay licensing costs (Apple)
- PlayReady licensing costs (Microsoft)
- Multi-DRM orchestration costs (BuyDRM, Irdeto, Vualto)

**Resolution:**
- **Licensing:** Widevine and FairPlay are generally royalty-free for the licenses themselves.
- **Infrastructure:** Multi-DRM setup costs range from **$10,000 to $50,000**, with monthly management fees between **$500 and $5,000** (Kinescope 2026).
- **Orchestration:** Costs are driven by the complexity of key management and license delivery servers rather than per-stream royalties.

---

### G-006: Regional OTT Player Monetization Models
**Domain:** Domain 7 (Regional Analysis)
**Status:** OPEN
**Priority:** MEDIUM

**Data Point Needed:**
- Hotstar (India) ARPU, subscriber count, monetization mix
- Viu (Hong Kong) pricing strategy, regional expansion costs
- Globoplay (Brazil) content acquisition costs, local payment gateway fees
- Showmax (South Africa) infrastructure challenges, bandwidth costs in low-infrastructure regions

**Why This Matters:**
Asia = highest growth region (index 100) but zero research on regional player strategies. If StreamIT targets global customers, need to understand regional dynamics.

**Search Attempts:** None yet (identified in Phase 0 audit)

**Workarounds to Try:**
1. Regional tech news (TechCrunch India, TechInAsia, Convergencia Latina)
2. Company investor decks (if publicly traded or venture-backed)
3. Local market research firms (RedSeer India, KPMG regional reports)
4. LinkedIn employee posts (product/engineering team insights)

---

### G-007: Live Streaming Real-Time Transcoding Costs
**Domain:** Domain 6 (Infrastructure Costs)
**Status:** OPEN
**Priority:** MEDIUM

**Data Point Needed:**
- Real-time transcoding cost per stream-hour (vs VOD transcoding)
- Sports OTT concurrent viewership cost multiplier
- Live streaming latency requirements and cost trade-offs (WebRTC vs HLS)
- PPV (Pay-Per-View) conversion rates and pricing benchmarks

**Why This Matters:**
User feedback requests IPTV and live streaming. Live streaming has different cost profile from VOD (can't pre-transcode). Need economic model to assess viability.

**Search Attempts:** None yet (identified in Phase 0 audit)

**Workarounds to Try:**
1. Live streaming platform case studies (Wowza, Mux, AWS IVS)
2. Sports OTT operator reports (DAZN, ESPN+, FuboTV disclosures)
3. Encoding vendor pricing pages (AWS MediaLive, Bitmovin Live Encoding)
4. Trade publications (Streaming Media Magazine)

---

### G-008: Churn Prediction Signals
**Domain:** Domain 2 (Business Models)
**Status:** OPEN
**Priority:** MEDIUM

**Data Point Needed:**
- Top 5 predictive signals for OTT churn (watch time drop, login frequency, content exhaustion)
- Retention tactics ROI (win-back campaigns, personalized offers, content alerts)
- Acceptable churn rate benchmarks: SVOD vs AVOD vs Hybrid
- Churn prediction ML model accuracy rates (industry standard)

**Why This Matters:**
Retention is most expensive module at scale ($25K/month at 1M users). Need to understand what "good retention" looks like quantitatively to justify investment.

**Search Attempts:** None yet (identified in Phase 0 audit)

**Workarounds to Try:**
1. SaaS churn analysis frameworks (may apply to subscription OTT)
2. Netflix/Spotify product team blog posts on retention
3. Customer data platform vendor case studies (Segment, Amplitude)
4. Academic papers on churn prediction in subscription services

---

### G-009: Server-Side Ad Insertion (SSAI) Cost Models
**Domain:** Domain 6 (Infrastructure Costs)
**Status:** OPEN
**Priority:** MEDIUM

**Data Point Needed:**
- SSAI cost per ad impression (vs CSAI)
- Ad decisioning latency impact on QoE
- SSAI vendor pricing (Google DAI, AWS MediaTailor, Brightcove SSAI)
- Ad fill rate economics (what happens with unfilled inventory)

**Why This Matters:**
Revenue model shifting to AVOD/Hybrid (55% by 2030). StreamIT feature list mentions SSAI but lacks operational cost context. Need to assess SSAI investment ROI.

**Search Attempts:** None yet (identified in Phase 0 audit)

**Workarounds to Try:**
1. SSAI vendor pricing pages and case studies
2. Ad tech vendor whitepapers (FreeWheel, SpotX)
3. Programmatic ad marketplace reports
4. Trade publications (AdExchanger, AdAge video advertising analysis)

---

### G-010: Payment Gateway Regional Fees
**Domain:** Domain 6 (Infrastructure Costs)
**Status:** OPEN
**Priority:** LOW-MEDIUM

**Data Point Needed:**
- Payment gateway fees by region (Stripe vs Razorpay vs PayPal vs local)
- Regional pricing elasticity (India vs US subscription willingness-to-pay)
- Subscription dunning (failed payment recovery rates)
- Multi-currency transaction costs

**Why This Matters:**
User feedback requests "multi-currency support." Monetization is Stage 4 of platform maturity. Need tactical playbook for regional payment optimization.

**Search Attempts:** None yet (identified in Phase 0 audit)

**Workarounds to Try:**
1. Payment gateway public pricing pages (likely available)
2. Fintech regional reports
3. E-commerce regional optimization guides
4. SaaS startup payment stack analysis (Indie Hackers, SaaS subreddits)

---

## NEW GAPS (Discovered During Research)

(Add new gaps here as research progresses and data points prove unavailable)

---

## ACCEPTED GAPS (Data Doesn't Exist)

(Move gaps here if after 3+ search attempts across multiple approaches, data definitively doesn't exist publicly)

---

## RESOLVED GAPS (Alternative Found)

(Move gaps here if workaround or alternative data source successfully filled the gap)

---

## GAP STATISTICS

**Total Gaps Logged:** 10 (from Phase 0 audit)
**OPEN:** 10
**Resolved:** 0
**Accepted as Unfillable:** 0

**By Priority:**
- HIGH: 4 gaps
- MEDIUM-HIGH: 1 gap
- MEDIUM: 4 gaps
- LOW-MEDIUM: 1 gap

**By Domain:**
- Domain 1 (Technology): 1 gap
- Domain 2 (Business Models): 2 gaps
- Domain 3 (Competitive): 2 gaps
- Domain 6 (Infrastructure): 4 gaps
- Domain 7 (Regional): 1 gap

---

*Update this file whenever a data point cannot be found after 3 search attempts.*
