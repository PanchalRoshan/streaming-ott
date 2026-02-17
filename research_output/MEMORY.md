# MEMORY.md - Long-Term Research Intelligence

**Purpose:** This file maintains cumulative research expertise across sessions. Load this file at the start of every session to build on past learnings.

**Last Updated:** 2026-02-17

---

## SOURCE INTELLIGENCE

### Tier 1 Sources Discovered
(Major industry reports, vendor official docs, academic papers)

**Phase 2 Initial Catalog - 107 sources identified across 3 priority domains:**

**Platform Official Sources (TIER 1 - Highest Priority):**
- Netflix: Open Connect docs, Tech Blog, Investor Relations, ISP Speed Index
- Disney+: Investor Relations, AWS re:Invent architecture talks
- Prime Video: Video Direct docs, Amazon 10-K filings
- FAST Platforms: Pluto TV advertiser resources, Tubi partner docs, Xumo platform stats

**Industry Research Firms (TIER 1 - Often Paywalled):**
- Parks Associates (OTT Video Market Tracker)
- Ampere Analysis (SVOD Forecasts)
- Conviva (State of Streaming quarterly reports)
- Sandvine (Global Internet Phenomena Report)
- eMarketer (CTV Advertising Forecasts)

**Academic & Technical:**
- Alliance for Open Media (AV1 codec specifications)
- ACM/IEEE papers on CDN costs, streaming behavior
- WebRTC.org official documentation

**Patterns that work:**
1. **Official platform sources first** - Netflix Tech Blog, earnings calls have hard data
2. **Follow the money** - Investor relations docs must disclose key metrics (subscribers, ARPU)
3. **Vendor case studies** - AWS/Google Cloud case studies reveal architecture patterns
4. **Industry benchmark reports** - Conviva, Sandvine provide comparative data across platforms

### Tier 2 Sources Discovered
(Industry analyst blogs, trade publications, credible tech media)

**Trade Publications Identified:**
- Streaming Media Magazine (deep technical coverage)
- VideoWeek (industry news, FAST focus)
- Broadcasting & Cable / NextTV (traditional media perspective)
- AdExchanger (programmatic CTV, ad tech stack)
- Digiday (CTV advertising trends)

**CDN Vendor Resources:**
- Akamai (video streaming solutions, cost per GB trends)
- Cloudflare (Stream delivery, Workers edge computing)
- Fastly (media delivery, real-time streaming)
- AWS MediaServices case studies
- Google Cloud Media CDN resources

**Subscription Analytics:**
- Antenna (actual churn data - potentially high value)
- ProfitWell (churn benchmarks by industry)
- Recurly (subscription economy reports)

**Streaming Aggregators:**
- Reelgood (content library analytics)
- JustWatch (market share by country)

**Patterns that work:**
1. **Trade pubs often cite Tier 1 sources** - Good for finding paywalled report summaries
2. **Vendor case studies have real numbers** - When they need to prove ROI
3. **Conference proceedings** - NAB, IBC, AWS re:Invent have platform case studies

### Tier 3 Sources Discovered
(General news, opinion pieces, older data)

*Existing research mostly falls here - internal StreamIT strategy docs*

**Tech Media (use selectively):**
- The Verge, Ars Technica, Protocol (good when citing platform announcements with data)

### Source Quality Lessons

**Green Flags to Prioritize:**
- ✅ **Direct platform disclosures** (earnings calls, tech blogs) - highest credibility
- ✅ **"We measured X" statements** - Conviva, Sandvine measure actual traffic
- ✅ **Vendor case studies with customer quotes** - Real implementation data
- ✅ **Academic papers with methodology sections** - Replicable findings
- ✅ **Industry association reports** (IAB, Streaming Video Alliance) - Survey-based data

**Red Flags to Watch For:**
- ⚠️ **"Industry experts estimate"** without attribution - opinion, not data
- ⚠️ **Old data (>2 years)** for fast-moving metrics (codec adoption, CPMs)
- ⚠️ **Single-source claims** without corroboration
- ⚠️ **Vendor whitepapers with no methodology** - marketing, not research

**Best Performing Domains for Sources:**
- **Domain 3 (Competitive):** EXCELLENT - Platforms must disclose subscriber/revenue data in earnings
- **Domain 1 (Technology):** GOOD - Codec consortiums publish specs, vendors share benchmarks
- **Domain 2 (Business Models):** MODERATE - Ad tech industry shares CPM ranges, but FAST specifics harder
- **Domains 4-7:** TBD - Not yet cataloged

---

## SEARCH PATTERNS & STRATEGIES

### What Works (Query Formulations)

**Technology Domain:**
- TBD during Phase 2-3

**Business Models Domain:**
- TBD during Phase 2-3

**Competitive Intelligence:**
- TBD during Phase 2-3

**Infrastructure Costs:**
- TBD during Phase 2-3

**Regional Analysis:**
- TBD during Phase 2-3

### What Doesn't Work (Failed Queries)

- TBD during research

### Search Strategy Evolution

*This section will track how search approaches improve over time*

---

## DOMAIN INSIGHTS (Cross-Cutting Patterns)

### Technology ↔ Business Model Connections
- **Existing insight:** Revenue model evolution (SVOD→AVOD→Hybrid) is driven by subscriber saturation + user tolerance collapse
- **Pattern:** Technology advancements (better ad insertion, personalization) enable new business models

### Competitive Intelligence ↔ Infrastructure Costs
- **Gap identified:** Existing cost models lack validation against actual Netflix/Prime operational data
- **Hypothesis:** If we find Netflix CDN costs, can validate or refute "70-90% CDN" claim (C-001 contradiction)

### Regional Trends ↔ Technology Adoption
- **Existing data:** Asia = highest growth region (index 100)
- **Research opportunity:** Do regional players use different tech stacks due to bandwidth constraints?

### User Behavior ↔ Content Strategy
- **Existing insight:** User patience collapse (5 sec → 2 sec start time tolerance from 2015-2024)
- **Implication:** Content delivery quality becoming more important than content quantity?

---

## METHODOLOGY LEARNINGS

### What's Working
- **Structured CSV templates:** 12-column format should capture all needed metadata
- **Contradiction tracking:** Logging C-001 early prevents compounding bad assumptions
- **Daily memory files:** Ensures no research context is lost between sessions

### What Needs Adjustment
- TBD based on Phase 3 research velocity

### Research Velocity Insights
- **Target:** 25-40 data points per hour
- **Actual:** TBD during Phase 3 deep research

### Quality Control Lessons
- **Confidence scoring:** Need to be strict - only mark HIGH confidence if multiple Tier 1/2 sources agree
- **Retry loop:** Max 3 attempts per data point with different search patterns before marking as gap
- **Stopping conditions:** TBD based on Phase 3 experience

---

## CRITICAL FAILURES & RECOVERIES

### Web Access Limitations (GitHub Actions Environment)

**Critical Blocker Discovered:** 2026-02-17 Session 4

The GitHub Actions environment has severe web access restrictions (ERR_BLOCKED_BY_CLIENT errors) that block:

**BLOCKED Categories:**
- ✗ Commercial vendor pricing pages (AWS, Google Cloud, Stripe, etc.)
- ✗ Streaming platform websites (Netflix, Disney+, etc.)
- ✗ Industry organization websites (Alliance for Open Media, DASH-IF)
- ✗ Most CDN vendor sites
- ✗ Many commercial news/trade publication sites

**ACCESSIBLE Sources:**
- ✓ GitHub repositories (code search, file content)
- ✓ Some academic repositories (needs testing: arXiv, IEEE, etc.)
- ✓ Some open standards documents (if hosted on accessible domains)

**Workarounds Attempted:**
1. Direct navigation to vendor pricing → FAILED (ERR_BLOCKED_BY_CLIENT)
2. Accessing platform official sites → FAILED (ERR_BLOCKED_BY_CLIENT)
3. GitHub code search → SUCCESS
4. GitHub file content retrieval → SUCCESS
5. GitHub MCP Server for earnings transcripts → SUCCESS (Netflix Q1 2024 data extracted)

**Impact on Research:**
- ~80% of cataloged sources in Phase 2 are inaccessible
- Original Phase 3 plan (direct web research) is NOT viable in current environment
- Requires handoff to web-capable environment for full execution

**Resolution Strategy - Handoff Created:**
- ✅ Created HANDOFF_TO_WEB_AGENT.md (565 lines) - Complete handoff documentation
- ✅ Documented all 350 sources for web-capable agent to access
- ✅ Provided systematic workflow and priority order
- ✅ Specified CSV format, confidence scoring, quality standards
- ✅ Mapped 10 knowledge gaps to specific sources
- ✅ Demonstrated GitHub MCP alternative (Netflix financial data)

**Value Preserved:**
- All Phase 0-2 work (3,900+ lines) ready for continuation
- Clear path forward for 700+ data point extraction
- Complete research infrastructure documented

### Paywall Encounters
*Track which critical sources are paywalled and what workarounds were attempted*

**Known Paywalled Sources (from Phase 2):**
- Parks Associates (OTT Video Market Tracker)
- Ampere Analysis (SVOD Forecasts)
- eMarketer (CTV Advertising Reports)

**Status:** Not yet attempted (web access blocked first)

### Data Quality Issues
*Track sources that initially seemed good but turned out unreliable*

- TBD during research

### Research Dead Ends
*Track topics that consumed time but yielded no usable data*

- Phase 3 Initial Attempt: Discovered environment access restrictions after attempting 5+ sources

---

## EXISTING RESEARCH INTEGRATION

### Data Points Already Validated (From Phase 0 Audit)

**HIGH Confidence (from existing research):**
1. OTT market size 2015: $70B, 2024: $320B, 2030: $600B+ (consistent across sources)
2. Revenue model shift: 2019 (85% SVOD) → 2030 (45% SVOD, 40% Hybrid, 15% AVOD)
3. User start time tolerance: 2015 (5 sec) → 2024 (2 sec) - 60% decrease
4. Infrastructure cost formula: 1 hour viewing ≈ 1.8GB at 4Mbps
5. Cost scaling: Stage 1 (1K users) = $1K-$3K/mo, Stage 3 (1M users) = $400K-$2.5M/mo

**MEDIUM Confidence:**
1. Regional growth: Asia index 100 (highest), LATAM 54, Africa 44, Middle East 34
2. Module costs at 1M users: Multi-CDN $30K, Retention $25K, Rec Engine $15K

**LOW Confidence (needs validation):**
1. "70-90% of costs = CDN" (contradicted by cost chart showing 32%)
2. StreamIT pricing tiers ($15K-$30K Launch tier) - not market-tested

### Gaps to Fill (From Phase 0 Audit)

**TIER 1 CRITICAL:**
1. Competitive operational benchmarks (Netflix/Disney+/Prime CDN costs, ARPU, churn)
2. FAST channel economics (CPM rates, ad fill rates, SSAI costs)
3. Emerging tech ROI analysis (AV1 codec savings, edge computing cost-benefit)

**TIER 2 HIGH:**
4. Regional OTT player strategies (Hotstar, Viu, Globoplay monetization models)
5. DRM implementation costs (Widevine/FairPlay licensing, multi-DRM orchestration)
6. Churn prediction playbook (prediction signals, retention tactics, benchmark rates)

*(See existing_research_audit.md for full gap analysis)*

---

## TOOLS & TECHNIQUES

### Research Tools Preferences
- **Web search:** TBD which search engines work best for OTT industry queries
- **Web browse:** TBD best extraction strategies for long reports
- **File operations:** CSV append workflow should prevent data loss

### Data Extraction Scripts
*Any reusable patterns for extracting data from common source types*

- TBD during research

### Source Bookmarks
*URLs that repeatedly provide high-quality data*

- TBD during research

---

## SESSION PATTERNS

### Most Productive Times
- TBD after multiple sessions

### Common Blockers
- **Large PDFs:** "0. Future OTT Industry Report 2026" (966KB) required bash extraction in Phase 0
- **Paywalls:** TBD during research

### Session Length Optimization
- **Target:** 2-hour focused research blocks with heartbeat checks every 30 min
- **Actual:** TBD based on velocity tracking

---

## EVOLUTION TRACKING

### Version History
- **v1.0 (2026-02-17):** Initial MEMORY.md structure created during Phase 1 workspace initialization
- Future versions will track major methodology shifts and insight breakthroughs

### Major Breakthroughs
*Reserved for significant cross-domain insights that change research direction*

- TBD during research

---

## INSTRUCTIONS FOR FUTURE SELF

When you wake up in a new session:

1. **Read this file first** - It contains everything you've learned about finding good sources
2. **Read yesterday's daily log** (`memory/YYYY-MM-DD.md`) - Picks up where you left off
3. **Check research_log.md** - See domain completion status
4. **Review contradictions.md** - Don't propagate known conflicts

**Don't reinvent the wheel** - If a search pattern worked before, use it again.
**Update this file** - When you discover a great source or learn a lesson, add it here immediately.
**Quality over quantity** - Tier 1/2 sources with HIGH confidence > many Tier 3 sources with LOW confidence.

---

*This file grows with your research expertise. Treat it as your evolving research brain.*
