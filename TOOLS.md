# TOOLS.md - OTT Research Toolkit

## Research-Specific Tool Notes

### Web Search Patterns That Work

**For Financial Data:**

```
✅ "[Company] 10-Q [Year] [Quarter]"
✅ "[Company] investor relations quarterly results"
✅ "[Metric] [Company] Q4 2024"
❌ "What is Netflix's revenue in the most recent quarter" (too verbose)
```

**For Technology Adoption:**

```
✅ "[Technology] adoption rate 2024 statistics"
✅ "[Codec/Standard] market share forecast"
✅ "[Tech] deployment timeline industry"
❌ "[Technology] future trends" (too vague)
```

**For Market Intelligence:**

```
✅ "[Platform] subscriber count [Month/Quarter] 2024"
✅ "[Industry segment] market size forecast 2030"
✅ "streaming churn rate comparison 2024"
❌ "best streaming platforms" (subjective, not data)
```

### High-Value Source URLs (Direct Access)

**Financial Filings:**

- SEC EDGAR: `https://www.sec.gov/cgi-bin/browse-edgar?company=[NAME]&action=getcompany`
- For Netflix: `https://ir.netflix.net/financials/quarterly-earnings/default.aspx`
- For Disney: `https://thewaltdisneycompany.com/investor-relations/`

**Technology Standards:**

- Codec adoption: `https://www.streamingmedia.com`
- CDN pricing: Direct to provider pricing pages (AWS, Cloudflare, Akamai)

**Market Research (Free Tiers):**

- Statista (limited free): `https://www.statista.com/`
- Government data: FCC, Ofcom, EU publications

### Extraction Scripts (If python_execute available)

**Parse SEC 10-Q for specific metrics:**

```python
# Example: Extract ARPU from Netflix 10-Q
import requests
from bs4 import BeautifulSoup

def extract_metric(filing_url, metric_keyword):
    # Fetch filing HTML
    # Search for tables containing keyword
    # Extract numerical value
    # Return with context
    pass
```

**Scrape pricing pages:**

```python
# Example: Capture CDN pricing tiers
def scrape_pricing(url):
    # Use requests + BeautifulSoup
    # Extract pricing table
    # Save to CSV
    pass
```

### Credibility Red Flags (Learned Signals)

**Low-Credibility Indicators:**

- 🚩 Round numbers without precision (suggests estimate/fabrication)
- 🚩 No methodology disclosed
- 🚩 Marketing language ("revolutionary", "game-changing")
- 🚩 No author attribution
- 🚩 Source is vendor writing about own product (conflict of interest)
- 🚩 Outdated data (>18 months for tech metrics)

**High-Credibility Indicators:**

- ✅ Specific dates and sample sizes
- ✅ Methodology section included
- ✅ Multiple data points (not just headline number)
- ✅ Source links to raw data
- ✅ Known author/institution
- ✅ Peer-reviewed or audited

### Paywall Workarounds (Ethical)

**Strategies:**

1. **Company IR → Instead of news article**
   - News: "Netflix earnings beat expectations" (paywall)
   - Direct: ir.netflix.net (free)
2. **Academic preprints → Instead of journal**
   - Journal: IEEE paper on codec efficiency (paywall)
   - arXiv: Same paper preprint (free)
3. **Government source → Instead of think tank**
   - Think tank: Report on broadband costs (paywall)
   - FCC: Same underlying data (free)

**What NOT to do:**

- ❌ Use bypass tools/archives to access paywalled content without permission
- ❌ Cite sources you couldn't actually read
- ❌ Copy large text blocks from sources

### File Management Conventions

**Naming:**

```
domain1_technology.csv
domain2_business_models.csv
domain3_competitive_intel.csv
domain6_infrastructure_costs.csv
contradictions.md
knowledge_gaps.md
research_log.md
```

**CSV Column Standards:**

```csv
Category,Subcategory,Metric,Value,Unit,Date,Geographic_Scope,Source_URL,Date_Accessed,Credibility_Tier,Notes
```

**Always include:**

- Value WITH unit (25M, not 25)
- Date of data (Q4 2024, not "recent")
- Source URL (exact page, not homepage)
- Date accessed (YYYY-MM-DD)
- Credibility tier (1-4)

---

## Iterative Query Pattern System

When first query fails or returns LOW confidence data,
work through these patterns IN ORDER until HIGH confidence achieved:

### Pattern Ladder: Financial Data

LEVEL 1 (Try first):
→ "[Company] [Metric] [Quarter] [Year]"
→ Example: "Netflix ARPU Q4 2024"

LEVEL 2 (If Level 1 fails):
→ "[Company] investor relations [Year] quarterly results"
→ Go directly to company IR page, not news about it

LEVEL 3 (If Level 2 fails):
→ "SEC EDGAR [Company ticker] 10-Q [Year]"
→ Search directly in SEC filing database

LEVEL 4 (If Level 3 fails):
→ "[Analyst firm] [Company] [Metric] estimate [Year]"
→ Example: "Wedbush Netflix ARPU estimate 2024"
→ Flag result as [ANALYST ESTIMATE]

LEVEL 5 (If Level 4 fails):
→ Use proxy metric
→ Example: Can't find ARPU? → Calculate from Revenue/Subscribers
→ Flag as [DERIVED - methodology: Revenue/Subscribers]

LEVEL 6 (Final attempt):
→ Academic paper or industry report
→ Search: "[Metric] streaming industry [Year] research"
→ Flag source tier carefully

IF ALL 6 LEVELS FAIL:
→ Log to knowledge_gaps.md
→ Move on

---

### Pattern Ladder: Technology Adoption

LEVEL 1: "[Technology] adoption rate [Year]"
LEVEL 2: "[Technology] market share [Year] statistics"
LEVEL 3: "[Technology] deployment data industry report"
LEVEL 4: Academic paper: "[Technology] analysis [Year]"
LEVEL 5: Patent filings as proxy: "[Company] [Technology] patent [Year]"
LEVEL 6: Conference presentation data

---

### Pattern Ladder: Market Size / Forecasts

LEVEL 1: "[Segment] market size [Year]"
LEVEL 2: "[Segment] TAM forecast [Year]"
LEVEL 3: "[Analyst firm] [Segment] report [Year]"
LEVEL 4: Government/regulatory filing mentioning market size
LEVEL 5: Add up component parts (build-up method)
LEVEL 6: Cross-reference 3 analyst estimates, use median

---

### Pattern Ladder: Competitive Data

LEVEL 1: "[Platform] subscribers [Quarter] [Year]"
LEVEL 2: "[Platform] annual report [Year]"
LEVEL 3: Third-party analytics: "Sensor Tower [Platform] downloads [Year]"
LEVEL 4: "[Platform] market share [Region] [Year]"
LEVEL 5: Proxy: "[Platform] content spend [Year]" (signals subscriber ambition)
LEVEL 6: Cross-reference 3 analyst estimates

---

### Self-Learning Rule:

After each domain, update this file:

PATTERNS THAT WORKED THIS SESSION:
→ [Pattern] worked for [data type] → Move to Level 1 next time

PATTERNS THAT FAILED THIS SESSION:
→ [Pattern] failed for [data type] → Move to Level 5/6 next time

This makes the query system smarter every domain.

```

---

## **HOW IT ALL CONNECTS NOW:**
```

Agent searches → Gets data → SOUL.md scores it
↓
HIGH? → Save to CSV → Next data point
↓
MEDIUM? → TOOLS.md Pattern Ladder Level +1
→ Re-score
↓
LOW? → TOOLS.md Pattern Ladder Level +2
→ Re-score
↓
Still LOW after 3 attempts?
→ knowledge_gaps.md
→ MEMORY.md (log failed patterns)
→ Move on
↓
After domain complete → HEARTBEAT.md reviews scores
→ >20% LOW? → Full retry pass
→ MEMORY.md updated with learnings
→ TOOLS.md updated with new patterns

_Add your own discoveries here. This is your research cheat sheet._
