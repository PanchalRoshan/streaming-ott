# HEARTBEAT.md - Research Progress Checks

## Auto-Check Every 30 Minutes

During active research, I automatically assess and log progress.

### Standard Heartbeat Tasks

**1. Progress Assessment:**

- Current domain and sub-task
- Sources consulted (since last heartbeat + cumulative)
- Data points extracted (since last heartbeat + cumulative)
- Contradictions found (new + total)
- Knowledge gaps identified (new + total)
- Estimated time to domain completion

**2. Quality Check:**

```
✅ Source quality: Tier 1/2 ratio >70%?
✅ Cross-validation: Key claims have 3+ sources?
✅ Data completeness: >90% of requested metrics found?
✅ Velocity: 25-40 data points/hour sustained?
✅ Blockers: Any paywalls or access issues?
```

**3. File Checkpoint:**

Ensure all files saved and current:

- Domain CSV files updated
- research_log.md current
- contradictions.md includes latest
- knowledge_gaps.md updated
- memory/YYYY-MM-DD.md has session notes

**4. Self-Correction Check:**

```
IF velocity <20 data points/hour:
    → Diagnose: Sparse sources? Dense sources? Distracted?
    → Action: Adjust search strategy

IF cross-validation rate <50%:
    → Action: Require 3+ sources for next 5 data points

IF Tier 3/4 sources >40%:
    → Action: Prioritize financial filings, academic papers

IF knowledge gaps >10%:
    → Action: Review gaps, try alternative search angles
```

### Heartbeat Output Format

Log to `research_log.md`:

```markdown
## HEARTBEAT [YYYY-MM-DD HH:MM]

**Current Task:** Domain X, Sub-task Y.Z  
**Progress:** XX% of Domain X complete  
**Velocity:** XX data points/hour (target: 30-40)

**Since Last Heartbeat (30 min):**

- Sources: +XX
- Data Points: +XX
- Contradictions: +X
- Gaps: +X

**Quality Metrics:**

- Tier 1/2 Sources: XX% (target: >70%)
- Cross-Validation Rate: XX% (target: >60%)
- Data Completeness: XX% (target: >95%)

**Blockers:** [None | List any issues]

**Next Steps:** [What I'll tackle in next 30 min]

**ETA:** X.X hours to domain completion
```

### When to Escalate to User

🚨 **Stop and notify researcher if:**

- All primary sources for critical metric are paywalled
- Major contradiction across 50%+ of credible sources
- Research velocity <15 data points/hour for >2 hours (indicates stuck)
- Technical error preventing file saves/access
- Discovered user's existing research contains significant error

### When to Continue Autonomously

✅ **Keep working (internal HEARTBEAT_OK) if:**

- Research progressing normally
- Minor paywalls (alternatives exist)
- Data extraction on track
- Quality metrics within acceptable range
- No critical blockers

### Domain Completion Heartbeat

Extended check when finishing a domain:

```markdown
## DOMAIN X COMPLETION REPORT

**Duration:** X.X hours  
**Sources:** XXX consulted  
**Data Points:** XXX extracted  
**Contradictions:** XX documented  
**Gaps:** XX identified

**Quality Score:**

- Source Credibility: [Score]/100
- Data Completeness: [Score]/100
- Cross-Validation: [Score]/100
- Documentation: [Score]/100
- **OVERALL:** [Score]/100

**Top 5 Findings:**

1. [Most significant data point + source]
2. [Most significant data point + source]
3. [Most significant data point + source]
4. [Most significant data point + source]
5. [Most significant data point + source]

**Major Contradictions:**

1. [Issue requiring deeper investigation]

**Critical Gaps:**

1. [Data that proved impossible to find + why]

**Lessons Learned:**

- [What search strategies worked]
- [What sources were most valuable]
- [What to improve for next domain]

**Ready for Domain [X+1]:** [Yes/No]
```

### Proactive Background Work (During Heartbeats)

Between research tasks, I can:

- Review and organize memory files
- Update MEMORY.md with new source intelligence
- Clean up CSV files (standardize formatting)
- Commit progress to version control (if git available)
- Analyze cross-domain patterns in accumulated data

### Emergency Heartbeat

If encountering critical blocker:

```markdown
## 🚨 EMERGENCY HEARTBEAT

**Issue:** [Specific problem]  
**Impact:** [How this affects research]  
**Attempted Solutions:**

1. [What I tried]
2. [What I tried]
3. [What I tried]

**Options:**  
A. [Option 1 - pros/cons]  
B. [Option 2 - pros/cons]  
C. Escalate to researcher for guidance

**Recommendation:** [My suggested path]

**Status:** Waiting for user input before proceeding
```

---

_Heartbeats maintain research momentum and catch issues early._
