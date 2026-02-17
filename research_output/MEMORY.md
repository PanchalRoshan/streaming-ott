# MEMORY.md - Long-Term Research Intelligence

**Purpose:** This file maintains cumulative research expertise across sessions. Load this file at the start of every session to build on past learnings.

**Last Updated:** 2026-02-17

---

## SOURCE INTELLIGENCE

### Tier 1 Sources Discovered
(Major industry reports, vendor official docs, academic papers)

*None discovered yet - Phase 2 will populate this*

**Patterns that work:**
- TBD based on Phase 2-3 research

### Tier 2 Sources Discovered
(Industry analyst blogs, trade publications, credible tech media)

*None discovered yet - Phase 2 will populate this*

**Patterns that work:**
- TBD based on Phase 2-3 research

### Tier 3 Sources Discovered
(General news, opinion pieces, older data)

*Existing research mostly falls here - internal StreamIT strategy docs*

### Source Quality Lessons

**Red Flags Learned:**
- TBD during research

**Green Flags to Prioritize:**
- TBD during research

**Best Performing Domains for Sources:**
- TBD after Phase 2 source discovery

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

### Paywall Encounters
*Track which critical sources are paywalled and what workarounds were attempted*

- TBD during research

### Data Quality Issues
*Track sources that initially seemed good but turned out unreliable*

- TBD during research

### Research Dead Ends
*Track topics that consumed time but yielded no usable data*

- TBD during research

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
