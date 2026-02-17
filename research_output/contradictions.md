# CONTRADICTIONS TRACKER

This file tracks contradictions discovered during OTT streaming research (2026-2035).

## Purpose
When multiple sources provide conflicting data points, log them here for investigation and resolution.

## Format
Each contradiction entry should include:
- **ID:** Unique identifier (C-001, C-002, etc.)
- **Domain:** Which research domain this affects
- **Conflict:** What data points are conflicting
- **Source A:** First source with details
- **Source B:** Conflicting source with details
- **Impact:** Why this matters for the research
- **Status:** OPEN / INVESTIGATING / RESOLVED
- **Resolution:** How the contradiction was resolved (if applicable)

---

## EXISTING CONTRADICTIONS (From Phase 0 Audit)

### C-001: Infrastructure CDN Cost Percentage
**Domain:** Domain 6 (Infrastructure Costs)
**Status:** OPEN
**Date Identified:** 2026-02-17

**Conflict:**
- Source claims "70-90% of costs at scale = CDN/bandwidth"
- Cost scaling chart shows only 32% of costs are Multi-CDN at 1M users

**Source A:**
- File: `streaming_ott_research/Streaming - A to Z & Infrastructure Cost.md`
- Claim: "70-90% of cost at scale = video delivery (CDN/Bandwidth)"
- Tier: Internal document (assumed Tier 2)

**Source B:**
- File: `streaming_ott_research/13. Cost Scaling Log.png`
- Data: At 1M users: Multi-CDN ~$30K, Rec Engine ~$15K, Retention ~$25K, Transcoding ~$7K, AI Analytics ~$17K
- Total: ~$94K/month
- Multi-CDN percentage: $30K / $94K = 32%
- Tier: Internal document (assumed Tier 2)

**Impact:**
This discrepancy affects infrastructure cost planning and recommendations. If CDN is truly 70-90% at scale, then cost projections are significantly underestimated in the chart.

**Investigation Needed:**
1. Check if chart is missing bandwidth costs separate from multi-CDN module costs
2. Verify if "video delivery" includes origin storage, transcoding bandwidth, and edge caching beyond CDN switching
3. Validate against external benchmarks (Netflix, YouTube bandwidth cost disclosures)

**Resolution:** TBD

---

## NEW CONTRADICTIONS

(Add new contradictions below as they are discovered during research)

---

## RESOLVED CONTRADICTIONS

(Move resolved contradictions here with final resolution explanation)
