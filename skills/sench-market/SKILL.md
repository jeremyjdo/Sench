---
name: sench-market
description: Market definition & opportunity mapping. Define the broadest possible market perimeter, explore value chains, and create comprehensive opportunity maps. Exhaustive scoping before prioritization.
---

# /sench-market - Market Definition & Scoping

Comprehensive market opportunity mapping for venture design. Think wide before thinking right.

## Usage

```
/sench-market {market/industry}           # Default (English)
/sench-market {market/industry} --fr      # French output
/sench-market {market/industry} --en      # English output (explicit)
```

## Philosophy

**Think wide before thinking right.**

- Favor exhaustiveness over precision
- Avoid early judgments on attractiveness or feasibility
- Structure exploration using value chains
- Make assumptions explicit
- Delay convergence deliberately

## Workflow

```
Input (market/industry) + optional --fr/--en
    ↓
1. Market Perimeter Definition
    ↓
2. Value Chain Mapping
    ↓
3. Opportunity Exploration
    ↓
4. Adjacent Market Discovery
    ↓
5. Report → {market}_opportunity_map.md
```

## Rules

1. **Exhaustiveness first** - capture everything, filter later
2. **No premature filtering** - avoid attractiveness judgments
3. **Single output file** - `{market}_opportunity_map.md`
4. **Sources required** - include URLs for all market data
5. **Make assumptions explicit** - state what you assumed

---

## Phase 1: Market Perimeter Definition

### Guiding Questions

- What could reasonably belong to the market we are exploring?
- What problems, jobs, or use cases might exist even if they are not obvious today?
- What adjacent or emerging spaces could be relevant?
- Is there anything happening in other countries that doesn't exist locally but could be interesting?
- What parts of the value chain are often overlooked?
- What would we regret not having explored later?

### Search Queries

```
# Core Market Understanding
"{market}" market size TAM SAM
"{market}" industry overview 2025
"{market}" value chain analysis
"{market}" market segments

# Value Chain Exploration
"{market}" supply chain
"{market}" distribution channels
"{market}" B2B vs B2C
"{market}" upstream downstream

# Adjacent Markets
"{market}" adjacent markets
"{market}" convergence with
"{market}" emerging trends
"{market}" disruption

# International Benchmarks
"{market}" USA startups
"{market}" Europe trends
"{market}" Asia innovation
"{market}" emerging markets

# Jobs To Be Done
"{market}" customer pain points
"{market}" unmet needs
"{market}" user research
"{market}" jobs to be done

# Regulations & Barriers
"{market}" regulations France
"{market}" barriers to entry
"{market}" compliance requirements
```

---

## Phase 2: Value Chain Mapping

### Value Chain Framework

```
Raw Materials → Components → Assembly → Distribution → Retail → End User → After-Sales
     ↓              ↓           ↓           ↓          ↓         ↓           ↓
  [Players]    [Players]   [Players]   [Players]  [Players] [Players]   [Players]
```

### For Each Stage, Identify:

1. **Key players** - incumbents, challengers, startups
2. **Margin structure** - who captures value
3. **Pain points** - inefficiencies, friction
4. **Innovation opportunities** - what could be improved
5. **Digital penetration** - how digitized is this stage

---

## Phase 3: Opportunity Exploration

### Opportunity Categories

| Category | Description | Examples |
|----------|-------------|----------|
| **Underserved segments** | Customer groups poorly served | SMBs, rural areas, specific demographics |
| **Friction points** | Process inefficiencies | Manual processes, long wait times |
| **Unbundling opportunities** | Breaking apart integrated offers | Vertical SaaS carve-outs |
| **Bundling opportunities** | Combining fragmented services | Platform plays |
| **Regulatory arbitrage** | New rules enabling innovation | Open banking, data portability |
| **Technology shifts** | New tech enabling new models | AI, blockchain, IoT |
| **Behavior changes** | Post-COVID, generational shifts | Remote work, sustainability |

### Research Sources

| Source | What to Find | Method |
|--------|--------------|--------|
| **Market reports** | TAM/SAM/SOM, trends | WebSearch: "{market}" market report 2025 |
| **Crunchbase/Dealroom** | Funded startups in space | WebSearch: site:crunchbase.com "{market}" |
| **CB Insights** | Market maps, landscapes | WebSearch: site:cbinsights.com "{market}" |
| **McKinsey/BCG/Bain** | Strategy insights | WebSearch: site:mckinsey.com "{market}" |
| **Trade publications** | Industry news | WebSearch: "{market}" industry publication |
| **Regulatory bodies** | Rules, compliance | WebSearch: "{market}" regulation France |
| **Reddit/Forums** | User pain points | WebSearch: site:reddit.com "{market}" problems |
| **ProductHunt** | New entrants | WebSearch: site:producthunt.com "{market}" |

---

## Phase 4: Adjacent Market Discovery

### Adjacency Framework

```
         ┌─────────────────────────────────────────┐
         │           ADJACENT MARKETS              │
         │                                         │
    ┌────┼────┐         CORE MARKET          ┌────┼────┐
    │ Up- │    │                              │Down-│    │
    │stream│    │    ┌─────────────────┐     │stream│    │
    │      │    │    │  {YOUR MARKET}  │     │      │    │
    └──────┘    │    └─────────────────┘     └──────┘    │
         │                                         │
         │    ┌──────────┐    ┌──────────┐        │
         │    │Substitute│    │Complement│        │
         │    │ Markets  │    │ Markets  │        │
         │    └──────────┘    └──────────┘        │
         │                                         │
         └─────────────────────────────────────────┘
```

### Adjacency Types

1. **Upstream** - Suppliers, raw materials, inputs
2. **Downstream** - Customers, distribution, end-users
3. **Substitutes** - Alternative solutions to same problem
4. **Complements** - Products used together with core market
5. **Geographic** - Same market in other regions
6. **Demographic** - Same need, different customer segment

---

## Phase 5: Report

Output: `{market}_opportunity_map.md`

### Language Parameter

- Default or `--en`: English output
- `--fr`: French output (use French headers and content)

```markdown
# {Market} - Opportunity Map

*{date}*

---

## Executive Summary

{3-4 sentences: market definition, size, key opportunities identified, recommended exploration areas}

---

## Market Definition

### Core Market

{Clear definition of the market perimeter. What is IN scope, what is OUT of scope.}

| Attribute | Detail |
|-----------|--------|
| **Definition** | {clear market definition} |
| **TAM** | {total addressable market} |
| **SAM** | {serviceable addressable market} |
| **SOM** | {serviceable obtainable market} |
| **Growth Rate** | {CAGR %} |
| **Key Geographies** | {main markets} |

*Sources: [{source}]({url})*

### Market Boundaries

**Included:**
- {segment 1}
- {segment 2}

**Excluded:**
- {segment 1} (reason)
- {segment 2} (reason)

**Assumptions:**
- {assumption 1}
- {assumption 2}

---

## Value Chain

```
{Visual ASCII representation of value chain}

Example:
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│ Raw Mat. │───▶│ Manufact.│───▶│ Distrib. │───▶│  Retail  │───▶│ End User │
└──────────┘    └──────────┘    └──────────┘    └──────────┘    └──────────┘
    │               │               │               │               │
   5%              20%             15%             40%             20%
  margin          margin          margin          margin          spend
```

### Value Chain Stages

#### 1. {Stage Name}

| Aspect | Detail |
|--------|--------|
| **Key Players** | {list of companies} |
| **Margin Structure** | {X%} |
| **Pain Points** | {inefficiencies} |
| **Digitization Level** | {Low/Medium/High} |
| **Opportunity Potential** | {assessment} |

{Repeat for each stage}

---

## Opportunity Map

### Category View

```
{Visual opportunity map - can use ASCII grid or table}

Example:
┌─────────────────────────────────────────────────────────────────────┐
│                        OPPORTUNITY MAP                               │
├─────────────┬─────────────┬─────────────┬─────────────┬─────────────┤
│  Segment A  │  Segment B  │  Segment C  │  Segment D  │  Segment E  │
├─────────────┼─────────────┼─────────────┼─────────────┼─────────────┤
│ Opp 1       │ Opp 4       │ Opp 7       │ Opp 10      │ Opp 13      │
│ Opp 2       │ Opp 5       │ Opp 8       │ Opp 11      │ Opp 14      │
│ Opp 3       │ Opp 6       │ Opp 9       │ Opp 12      │ Opp 15      │
└─────────────┴─────────────┴─────────────┴─────────────┴─────────────┘
```

### Detailed Opportunities

#### {Opportunity Category 1}

| Opportunity | Description | Target Segment | Existing Players | White Space |
|-------------|-------------|----------------|------------------|-------------|
| {Opp 1} | {description} | {segment} | {players or "None"} | {High/Med/Low} |
| {Opp 2} | {description} | {segment} | {players or "None"} | {High/Med/Low} |

#### {Opportunity Category 2}

{Same table structure}

---

## Market Segments

### Segment Breakdown

| Segment | Size | Growth | Penetration | Key Players | Opportunity |
|---------|------|--------|-------------|-------------|-------------|
| {Segment 1} | {€Xm} | {X%} | {X%} | {players} | {assessment} |
| {Segment 2} | {€Xm} | {X%} | {X%} | {players} | {assessment} |

### Segment Deep Dives

#### {Segment 1 Name}

**Definition:** {what this segment includes}

**Customer Profile:**
- {characteristic 1}
- {characteristic 2}

**Jobs To Be Done:**
- {job 1}
- {job 2}

**Current Solutions:**
- {solution 1} - {provider}
- {solution 2} - {provider}

**Unmet Needs:**
- {need 1}
- {need 2}

{Repeat for key segments}

---

## Adjacent Markets

### Adjacency Map

```
                    ┌─────────────────┐
                    │   UPSTREAM      │
                    │ {list markets}  │
                    └────────┬────────┘
                             │
┌─────────────┐    ┌────────▼────────┐    ┌─────────────┐
│ SUBSTITUTES │◀───│  CORE MARKET    │───▶│ COMPLEMENTS │
│ {markets}   │    │   {market}      │    │ {markets}   │
└─────────────┘    └────────┬────────┘    └─────────────┘
                             │
                    ┌────────▼────────┐
                    │  DOWNSTREAM     │
                    │ {list markets}  │
                    └─────────────────┘
```

### Adjacent Market Analysis

| Adjacent Market | Relationship | Size | Convergence Potential | Notes |
|-----------------|--------------|------|----------------------|-------|
| {market 1} | Upstream | {€Xb} | {High/Med/Low} | {notes} |
| {market 2} | Downstream | {€Xb} | {High/Med/Low} | {notes} |
| {market 3} | Substitute | {€Xb} | {High/Med/Low} | {notes} |
| {market 4} | Complement | {€Xb} | {High/Med/Low} | {notes} |

---

## Competitive Landscape

### Market Map

| Category | Players | Funding | Notes |
|----------|---------|---------|-------|
| **Incumbents** | {list} | N/A | {market position} |
| **Challengers** | {list} | {amounts} | {differentiation} |
| **Startups** | {list} | {amounts} | {innovation angle} |
| **Adjacent entrants** | {list} | {amounts} | {why entering} |

### Recent Funding Activity

| Company | Round | Amount | Date | Investors | Signal |
|---------|-------|--------|------|-----------|--------|
| {company} | {type} | {€Xm} | {date} | {investors} | {what it signals} |

---

## International Benchmarks

### What Exists Elsewhere

| Country | Innovation | Description | Local Equivalent | Gap |
|---------|------------|-------------|------------------|-----|
| USA | {company/model} | {description} | {local or "None"} | {opportunity} |
| UK | {company/model} | {description} | {local or "None"} | {opportunity} |
| Germany | {company/model} | {description} | {local or "None"} | {opportunity} |
| Asia | {company/model} | {description} | {local or "None"} | {opportunity} |

---

## Trends & Drivers

### Macro Trends

| Trend | Description | Impact on Market | Timeframe |
|-------|-------------|------------------|-----------|
| {Trend 1} | {description} | {Tailwind/Headwind} | {Short/Med/Long term} |
| {Trend 2} | {description} | {Tailwind/Headwind} | {Short/Med/Long term} |

### Technology Shifts

| Technology | Current State | Potential Impact | Adoption Timeline |
|------------|---------------|------------------|-------------------|
| {Tech 1} | {maturity} | {impact description} | {timeline} |
| {Tech 2} | {maturity} | {impact description} | {timeline} |

### Regulatory Environment

| Regulation | Status | Impact | Opportunity/Threat |
|------------|--------|--------|-------------------|
| {Reg 1} | {active/upcoming} | {description} | {assessment} |
| {Reg 2} | {active/upcoming} | {description} | {assessment} |

---

## Customer Insights

### Jobs To Be Done (JTBD)

| Job | Current Solution | Pain Level | Frequency |
|-----|------------------|------------|-----------|
| {job 1} | {how solved today} | {High/Med/Low} | {daily/weekly/monthly} |
| {job 2} | {how solved today} | {High/Med/Low} | {daily/weekly/monthly} |

### Unmet Needs

| Need | Customer Segment | Why Unmet | Opportunity Size |
|------|------------------|-----------|------------------|
| {need 1} | {segment} | {reason} | {assessment} |
| {need 2} | {segment} | {reason} | {assessment} |

---

## Key Questions for Further Exploration

### Unanswered Questions

1. {Question 1}
2. {Question 2}
3. {Question 3}

### Recommended Expert Interviews

| Expert Type | Questions to Explore | Potential Sources |
|-------------|---------------------|-------------------|
| {type 1} | {questions} | {where to find} |
| {type 2} | {questions} | {where to find} |

---

## Assumptions & Limitations

### Explicit Assumptions

1. {Assumption 1}
2. {Assumption 2}
3. {Assumption 3}

### Data Limitations

- {limitation 1}
- {limitation 2}

### What We Did NOT Explore (Yet)

- {area 1} - {why deprioritized for now}
- {area 2} - {why deprioritized for now}

---

## Sources

- {Source 1}: {url}
- {Source 2}: {url}
- {Market report}: {url}
- {Industry publication}: {url}
```
