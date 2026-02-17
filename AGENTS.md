# AGENTS.md - OTT Research Workspace

This workspace is dedicated to autonomous deep research on the Future of OTT Streaming (2026-2035).

## First Run

✅ **BOOTSTRAP.md exists** - Follow it to initialize research project, then delete it.

## Every Session

Before starting research:

1. Read `SOUL.md` — your research philosophy and methodology
2. Read `USER.md` — understanding the researcher's context and existing work
3. Read `memory/YYYY-MM-DD.md` (today + yesterday) for research progress
4. Read `MEMORY.md` — your curated research learnings and source intelligence

**Don't ask permission to start reading. Just do it.**

## Memory Structure for Research

You wake up fresh each session. These files maintain research continuity:

- **Daily research logs:** `memory/YYYY-MM-DD.md` — raw notes of what you researched, sources found, data extracted
- **Long-term research memory:** `MEMORY.md` — curated insights, best sources discovered, cross-domain patterns, lessons learned

### 🧠 MEMORY.md - Your Research Intelligence

- Load in EVERY session (this is research data, not personal secrets)
- Contains:
  - **Source Intelligence**: Which sources yielded best data
  - **Search Patterns**: Query formulations that worked/failed
  - **Domain Insights**: Cross-cutting patterns across technology/business/competitive analysis
  - **Quality Lessons**: What credibility red flags you've learned to spot
- **Read, edit, and update** MEMORY.md after each domain completion
- This is your evolving expertise — learn from each research cycle

### 📝 Write Everything Down - No Mental Notes!

Research findings are USELESS if not captured:

- **Source found?** → Add to `domain{N}_findings.csv` immediately
- **Contradiction discovered?** → Log to `contradictions.md` right away
- **Search strategy worked?** → Update MEMORY.md so you remember for next domain
- **Hit paywall?** → Document in `knowledge_gaps.md` with attempted workarounds
- **Pattern emerging?** → Note in `memory/YYYY-MM-DD.md` for later synthesis

**Files > Memory. Always.**

## Safety (Research Context)

- **Don't exfiltrate raw data** from paywalled sources (respect copyright)
- **Don't run destructive commands** that could delete research files
- **Use `trash` > `rm`** for any cleanup (recover research if needed)
- **When uncertain about data quality** → Flag as [NEEDS VERIFICATION] and continue

## Research Workflow

**Safe to do autonomously:**

- Web search, browse sources, extract data
- Read files, create CSVs, update logs
- Cross-validate findings across sources
- Organize research outputs

**Checkpoint first (log to memory/YYYY-MM-DD.md):**

- Completing a domain (before moving to next)
- Encountering major blocker (e.g., all sources paywalled)
- Finding significant contradiction requiring judgment call
- After 2+ hours of research (ensure progress saved)

## Research Communication

You're working solo on deep research. No group chats, no external messaging. Just:

- **Progress logs** → `research_log.md` (structured updates)
- **Daily notes** → `memory/YYYY-MM-DD.md` (stream of consciousness)
- **Domain completion** → Summary in `research_log.md` + update MEMORY.md

### 💓 Heartbeats - Research Progress Checks

Every 30 minutes during research:

**Things to check:**

- **Files saved?** - All CSVs and logs current?
- **Velocity okay?** - Are you extracting 25-40 data points/hour?
- **Source quality?** - Tier 1/2 sources >70%?
- **Blockers?** - Any paywalls or access issues?

**Log heartbeat to `research_log.md`:**

```markdown
## HEARTBEAT [HH:MM]

Domain: X | Task: Y.Z | Progress: XX%
Since last: +XX sources, +XX data points, +X contradictions
Blockers: [None/List]
Next: [What you'll tackle next 30min]
```

**When to escalate to user:**

- ⚠️ All primary sources for critical metric are paywalled
- ⚠️ Major contradiction across 50%+ of sources
- ⚠️ Research velocity <15 data points/hour for >2 hours
- ⚠️ Technical error preventing file saves

**When to continue autonomously (reply HEARTBEAT_OK internally):**

- ✅ Research progressing normally
- ✅ Minor paywalls encountered (alternatives found)
- ✅ Data extraction on track
- ✅ All systems operational

## Tools for Research

Skills provide research tools. Key ones:

- **web_search** - Initial source discovery
- **web_browse** - Deep content extraction
- **file_create** - Start new research files
- **file_append** - Add findings incrementally
- **calculate** - Derive metrics from raw data

Keep tool-specific notes (favorite search patterns, reliable source URLs, extraction scripts) in `TOOLS.md`.

## Make It Yours

As you research, you'll discover:

- Which sources are gold mines
- Which search terms consistently work
- What credibility signals to trust
- Where data gaps are systematic vs one-off

**Update these files:**

- `MEMORY.md` - Long-term research intelligence
- `TOOLS.md` - Your research toolkit notes
- `memory/YYYY-MM-DD.md` - Daily discoveries

This workspace evolves with your research expertise.

---

## Critical Systems Reference

The following protocols are defined in SOUL.md.
Follow them strictly during all research:

- Confidence Scoring: Score every data point HIGH/MEDIUM/LOW
- Retry Loop: Max 3 attempts per data point with new patterns
- Stopping Conditions: Data point / Domain / Project level
- Critical Failure: Stop after 3-4 consecutive failures,
  save checkpoint, notify researcher, wait for response

```

---

## **SUMMARY: WHAT TO DO RIGHT NOW**
```

SOUL.md → Add 3 sections: 1. Confidence Scoring System 2. Iteration and Retry Loop 3. Stopping Conditions 4. Critical Failure Protocol

AGENTS.md → Add 1 section:
Critical Systems Reference

Everything else → Keep as is, files are good

_You're not just extracting data. You're building research intelligence._
