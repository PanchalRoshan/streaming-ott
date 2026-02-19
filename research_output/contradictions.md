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
**Status:** RESOLVED
**Date Identified:** 2026-02-17

**Conflict:**
- Source claims "70-90% of costs at scale = CDN/bandwidth"
- Cost scaling chart shows only 32% of costs are Multi-CDN at 1M users

**Resolution:**
The contradiction is resolved by distinguishing between **raw bandwidth costs** and **CDN management/switching fees**.
1. **Source A (70-90%)** refers to the total cost of video delivery including raw egress bandwidth, which scales linearly with traffic if not optimized.
2. **Source B (32%)** refers to the "Multi-CDN" module/switching service fee, likely excluding the underlying raw bandwidth costs paid to providers like AWS or Akamai.
3. **External Benchmark:** Netflix (G-001) reduced this to a fraction of total costs by building its own CDN (Open Connect), proving that the 70-90% figure is a "worst-case" for unoptimized platforms, while the 32% figure in the chart likely represents a specific service fee rather than total delivery cost.
4. **Conclusion:** Total delivery costs (Bandwidth + CDN) are likely closer to 60-70% for a standard platform, but can be reduced via technology (AV1) and infrastructure (Open Connect).

---

## NEW CONTRADICTIONS

(Add new contradictions below as they are discovered during research)

---

## RESOLVED CONTRADICTIONS

(Move resolved contradictions here with final resolution explanation)
