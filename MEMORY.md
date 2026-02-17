# MEMORY.md - Research Intelligence Bank

_This is your accumulated research expertise. Update after each domain._

## Source Intelligence

### Best Sources Discovered (By Category)

**Financial Data (ARPU, Revenue, Subscribers):**

- **SEC EDGAR** (sec.gov) - Tier 1, most reliable for public US companies
- **Company IR pages** - Tier 1/2, varies by company transparency
- **Analyst presentations** (Wedbush, MoffettNathanson) - Tier 2, sometimes ahead of filings

**Technology Adoption Metrics:**

- **StreamingMedia.com** - Tier 2, good for codec adoption
- **Academic preprints** (arXiv) - Tier 1, cutting-edge tech
- **AWS/Google/Azure documentation** - Tier 2, infrastructure trends

**Market Intelligence:**

- **App analytics** (Sensor Tower, App Annie) - Tier 2 when free tier available
- **Trade associations** (MPAA, CTA) - Tier 2, industry-wide data
- **Government regulators** (FCC, Ofcom) - Tier 1, but often lagging

**Cost Data:**

- **Provider pricing pages** (AWS, Cloudflare) - Tier 2, but keep URLs as they change
- **TeleGeography** - Tier 2 for bandwidth/cable data

### Sources That Disappointed

- ❌ **Generic tech news** (TechCrunch, The Verge) - Often cite no sources, mix estimates with facts
- ❌ **Statista free tier** - Too many paywalls, limited value
- ❌ **Company blog posts** - Pure marketing, use only for feature announcements

## Search Query Patterns

### What Worked

**For financial metrics:**

```
✅ "[Company] 10-Q [Quarter] [Year]"
✅ "[Company] investor relations"
✅ "[Platform] ARPU Q[X] [Year]"
```

**For adoption rates:**

```
✅ "[Technology] adoption statistics [Year]"
✅ "[Standard] market share [Year]"
✅ "[Tech] deployment data"
```

**For market size:**

```
✅ "[Segment] market forecast [Year]"
✅ "[Category] TAM [Year]" (Total Addressable Market)
```

### What Failed

```
❌ "Best [technology]" (subjective, yields listicles)
❌ "Future of [industry]" (vague, yields opinion pieces)
❌ Questions in search ("How many subscribers does X have?")
```

## Cross-Domain Patterns Identified

### Pattern 1: AI as Ubiquitous Driver

**Observation:** "AI/ML" mentioned as critical capability across all 4 domains

- Domain 1 (Tech): Recommendation engines, content personalization
- Domain 2 (Business): Churn prediction, pricing optimization
- Domain 3 (Competitive): Differentiator in platform strategies
- Domain 6 (Infrastructure): Transcoding efficiency, CDN optimization

**Implication:** AI is not a feature, it's infrastructure. Platforms without ML capabilities are at fundamental disadvantage.

### Pattern 2: Data Disclosure Asymmetry

**Observation:** Netflix/Disney disclose detailed metrics; Apple/Amazon don't

- Netflix: ARPU, churn, engagement by title
- Apple TV+: Subscriber count NOT disclosed
- Amazon Prime Video: Revenue NOT broken out from Prime

**Implication:** Creates systematic knowledge gaps. For undisclosed platforms, rely on:

- Third-party estimates (but flag as [ESTIMATE])
- Inverse indicators (e.g., content spend suggests subscriber ambition)

### Pattern 3: [Add as patterns emerge]

## Credibility Lessons Learned

### Red Flags Encountered

**Example 1: TechCrunch Netflix ARPU article**

- **Issue:** Cited $29.85 vs SEC filing's $31.43
- **Lesson:** Tech news often miscalculates or uses non-standard methodology
- **Action:** Always check primary source for financial data

**Example 2: "Blockchain will revolutionize streaming" claims**

- **Issue:** Web3 streaming articles heavy on hype, light on deployment data
- **Lesson:** Distinguish between potential use cases and actual implementations
- **Action:** For emerging tech, require: active users, transaction volumes, technical documentation

### Trust Signals Validated

- ✅ **Specific dates/sample sizes** → Correlated with higher accuracy
- ✅ **Methodology section** → Almost always Tier 1 or 2 source
- ✅ **Multiple metrics** → More reliable than single headline number

## Paywall Workarounds That Worked

### Workaround 1: Company IR → News

**Situation:** WSJ article on Disney earnings (paywalled)  
**Solution:** Went to thewaltdisneycompany.com/investor-relations → Found earnings transcript (free)  
**Result:** Got same data + more detail

### Workaround 2: Preprint → Journal

**Situation:** IEEE paper on codec efficiency (paywalled)  
**Solution:** Searched arXiv for author name → Found preprint version  
**Result:** Same content, free access

### Workaround 3: [Add as discovered]

## Research Efficiency Metrics

Track to improve over time:

```
Domain 1 (Technology):
- Duration: X.X hours
- Data points/hour: XX
- Sources/hour: XX
- Cross-validation rate: XX%
- Paywall hit rate: XX%

Domain 2 (Business Models):
- [Same metrics]

[Update after each domain]
```

**Target improvements:**

- Increase data points/hour (better source identification)
- Increase cross-validation rate (more thorough verification)
- Decrease paywall hit rate (better free source finding)

## Domain-Specific Insights

### Domain 2: Business Models

**Key Learning:** ARPU varies wildly by region

- US Netflix ARPU: ~$17/month
- India Netflix ARPU: ~$2/month
- Global blended: ~$10/month

**Implication:** Always specify geography when citing ARPU

### Domain 3: Competitive Intelligence

**Key Learning:** [Fill in after completing domain]

### Domain 1: Technology

**Key Learning:** [Fill in after completing domain]

### Domain 6: Infrastructure Costs

**Key Learning:** [Fill in after completing domain]

## Mistakes Made & Lessons

### Mistake 1: [Example]

**What happened:** [Describe error]  
**Why it happened:** [Root cause]  
**How to prevent:** [Lesson learned]  
**Updated file:** [Which config file updated to prevent recurrence]

### Mistake 2: [Add as they occur]

## OTT Domain Glossary

Living terminology reference:

- **ARPU:** Average Revenue Per User (monthly or annual)
- **SVOD:** Subscription Video On Demand (e.g., Netflix basic plan)
- **AVOD:** Ad-supported Video On Demand (e.g., Hulu with ads)
- **FAST:** Free Ad-Supported Streaming Television (e.g., Pluto TV)
- **CDN:** Content Delivery Network (Akamai, Cloudflare, etc.)
- **Churn:** Monthly subscriber cancellation rate
- **MAU:** Monthly Active Users
- **ARPU vs ARPDAU:** ARPU = revenue per subscriber; ARPDAU = revenue per daily active (engagement-weighted)
- **Transcode:** Convert video into multiple bitrates/resolutions/codecs
- **ABR:** Adaptive Bitrate streaming (adjusts quality to bandwidth)

[Expand as new terms encountered]

## Research Philosophy Refinements

### Evolution 1: [Example]

**Initial approach:** [How I started]  
**What I learned:** [Discovery that changed approach]  
**New approach:** [Updated methodology]

## User Preferences Observed

**Researcher values:**

- Precision over speed (would rather wait for 3-source validation)
- Transparency about gaps (prefers honest "unknown" over weak estimate)
- Raw data over summaries (wants CSV, not prose)

**Researcher dislikes:**

- Speculation without [ESTIMATE] flags
- Vague sourcing ("according to reports")
- Over-formatting (wants analyst notes, not deck)

## Future Research Vectors

Ideas for follow-up research (beyond current scope):

1. **Deep dive on regional platforms** (Hotstar, iQIYI, Viu) - could be valuable
2. **Patent analysis** - What are platforms filing for? (signals future strategy)
3. **Executive compensation correlation** - Does CEO pay tie to metrics that predict success?
4. **Content ROI analysis** - Which original content drives highest subscriber growth vs cost?

[Add as possibilities emerge during research]

---

_This file is your research brain. Update it religiously. It makes you smarter every session._

```

---

## **🚀 DEPLOYMENT INSTRUCTIONS**

### **Files to Upload to OpenClaw:**

1. ✅ **AGENTS.md** (replace default)
2. ✅ **SOUL.md** (replace default)
3. ✅ **TOOLS.md** (replace default)
4. ✅ **IDENTITY.md** (replace default)
5. ✅ **USER.md** (replace default)
6. ✅ **HEARTBEAT.md** (replace default)
7. ✅ **BOOTSTRAP.md** (replace default)
8. ✅ **MEMORY.md** (create new - this one's missing in default)

### **First Launch Test:**

Give OpenClaw this command:
```

Initialize research workspace. Read BOOTSTRAP.md and follow initialization protocol. Confirm ready status when workspace setup complete.

```

### **Full Research Launch:**

After bootstrap complete:
```

Begin autonomous research on Domain 2 (Business Models). Execute all sub-tasks per AGENTS.md configuration. Log progress via heartbeat protocol. Run until domain completion or 3-hour timeout, whichever comes first.

## Source Tracking Log

Agent must update this section in real-time during research.
Every URL attempted must be logged here immediately.

---

### SUCCESSFULLY FETCHED

| #   | URL | Type | Domain | Data Extracted | Date |
| --- | --- | ---- | ------ | -------------- | ---- |

---

### FAILED TO FETCH

| #   | URL | Reason | Alternative Tried | Domain | Date |
| --- | --- | ------ | ----------------- | ------ | ---- |

---

### PARTIALLY FETCHED

| #   | URL | What Accessible | What Blocked | Domain | Date |
| --- | --- | --------------- | ------------ | ------ | ---- |

---

### Source Stats

Total Attempted: 0
Successfully Fetched: 0
Failed: 0
Partially Fetched: 0
Success Rate: 0%

Failure Reason Labels:

- PAYWALL: Content behind payment
- 404: Page not found
- BLOCKED: Access denied
- TIMEOUT: Page too slow
- LOGIN_REQUIRED: Needs account
- PDF_LOCKED: PDF protected
- JAVASCRIPT: Needs JS rendering
- EMPTY: Loaded but no useful data

Rules:

- Log EVERY URL before attempting
- Update status immediately after attempt
- Always try alternative if fetch fails
- Update stats every 10 fetches
- No exceptions - failed attempts must be logged too

```

---

## **UPDATE MASTER PROMPT**

Find this line in master prompt:
```

### MASTER RULES (Apply Throughout All Phases)

```

Add this block:
```

### Source Tracking Rule:

EVERY URL attempted must be logged to
the Source Tracking Log section in MEMORY.md

Before accessing: add URL with status [ATTEMPTING]
After success: move to Successfully Fetched table
After failure: move to Failed table with exact reason
After partial: move to Partially Fetched table
Update summary stats every 10 fetches
NO EXCEPTIONS - every attempt gets logged

## Checkpoint Log

Record of all research stop points and resumes.

---

### Active Checkpoint

Status: [NONE / STOPPED_AT_CHECKPOINT]
Checkpoint ID: [TIMESTAMP or NONE]
Stop Reason: [Description or NONE]
Resume Command: [Command researcher should use or NONE]

---

### Checkpoint History

| #                              | Timestamp | Phase | Domain | Stop Reason | Status |
| ------------------------------ | --------- | ----- | ------ | ----------- | ------ |
| [Auto-filled when stop occurs] |

---

### Resume Protocol

When researcher says "Resume research from checkpoint [TIMESTAMP]":

STEP 1: Read checkpoint from archive folder
STEP 2: Read all saved CSV files to understand current state
STEP 3: Read MEMORY.md to understand what failed
STEP 4: Confirm with researcher:
"Resuming from checkpoint [TIMESTAMP]
Completed: [X] data points across [X] domains
Resuming at: [Exact sub-task]
Issue resolved: [Ask researcher to confirm fix]
Starting in 10 seconds..."
STEP 5: Continue from exact stop point
STEP 6: Update Checkpoint Log status to RESUMED

```

---

## **3. UPDATE MASTER PROMPT**

Find this in master prompt:
```

### MASTER RULES (Apply Throughout All Phases)

```

Add this block:
```

### Critical Failure Rule:

If ANY of these happen consecutively:

- 3 failed URL fetches in a row
- 3 LOW confidence results with no recovery
- 3 failed searches returning nothing useful
- 4 paywall blocks on same topic

IMMEDIATELY:

1. STOP all research
2. SAVE all files to archive/checkpoint\_[TIMESTAMP]/
3. Log stop details to MEMORY.md
4. Notify researcher with exact stop reason and fix suggestion
5. WAIT for researcher response before continuing

DO NOT:

- Try to work around the failure silently
- Skip the failed section and continue
- Fabricate data to fill the gap
- Continue without notifying researcher

Resume ONLY when researcher says:
"Resume research from checkpoint [TIMESTAMP]"

```

---

## **HOW IT WORKS END TO END:**
```

Research running normally
↓
Failure occurs (paywall/404/no data)
↓
Failure 2 occurs
↓
Failure 3 occurs
↓
THRESHOLD HIT → STOP EVERYTHING
↓
Save all files to archive/checkpoint
↓
Log stop reason to MEMORY.md
↓
Notify you with exact details:
"Stopped at Domain 2, Sub-task 2.3
Failed 3 times on churn rate data
Root cause: All sources paywalled
Fix: Try Antenna.com free tier or
Parks Associates press release"
↓
WAIT for your response
↓
You fix the issue
↓
You say: "Resume from checkpoint [TIMESTAMP]"
↓
Agent reads checkpoint
↓
Confirms what it completed
↓
Continues from exact stop point
↓
Nothing lost
