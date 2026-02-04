# Analysis Modules

Formats for Phase 3 analysis files in `analyse/`.

---

## 3.1 - Identity (`identity.md`)

**Sources**: API gouv, INPI, annuaire-entreprises

```markdown
# Identity

## Legal Information

| Field | Value |
|-------|-------|
| Raison sociale | ... |
| SIREN | ... |
| SIRET (siege) | ... |
| Forme juridique | ... |
| Capital social | ... |
| Date creation | ... |
| Code NAF | ... |
| Siege social | ... |

## Directors

| Name | Role | Since |
|------|------|-------|

## Beneficial Owners (if available)

...

## History

- [Date]: [Event]
```

---

## 3.2 - Funding (`funding.md`)

**Sources**: Crunchbase, Dealroom, press

**WebSearch queries**:
```
"{company}" funding rounds investors
"{company}" levee de fonds investisseurs
"{company}" site:crunchbase.com
"{company}" site:dealroom.co
```

```markdown
# Funding

## Investment History

**Series B · 30M EUR** (June 2024)
Lead: **Accel**
Participants: Index Ventures, BPI

**Series A · 10M EUR** (January 2023)
Lead: **Serena**
Participants: Alven

**Seed · 2M EUR** (March 2022)
Lead: **Kima Ventures**

---
**Total raised**: 42M EUR
**Last valuation**: ~200M EUR (estimated)
```

---

## 3.3 - Team (`team.md`)

**IMPORTANT**: Key section. Must be detailed with narrative paragraphs.

**Sources**: LinkedIn, website, employees/

```markdown
# Team

[2-3 sentence intro about team composition]

## [First Last] - [Title] (since [date])

[First Last], [Title] since [date]. [3-4 sentence narrative about background, achievements, expertise].

- **LinkedIn**: [url]
- **Education**: [school, degree]
- **Previous**: [companies and roles with results if known]
- **Key expertise**: [domain]

## [Next Person] - [Title]
...

## Talent Flow

### Recent Hires
| Name | Role | Date | From |
|------|------|------|------|

### Recent Departures
| Name | Former Role | Date | To |
|------|-------------|------|-----|

## Talent Sources

Where employees come from (companies, schools).
```

---

## 3.4 - Finance (`finance.md`)

**Sources**: API gouv (`finances`), Pappers, societe.com

```markdown
# Finance

| Year | Revenue | Net Result | Employees | Source |
|------|---------|------------|-----------|--------|
| 2024 | ... | ... | ... | Pappers |
| 2023 | ... | ... | ... | API gouv |

## Analysis

[Commentary on financial trends, profitability, growth]
```

---

## 3.5 - Product (`product.md`)

**Sources**: site-web/, pricing, reviews/

```markdown
# Product Overview

## Core Product Thesis

For [target persona], the main challenge is [problem].
[Company] provides [solution type] that [value proposition] - [concrete benefits].

## Ideal Customer Profile

**User Persona**
- [Persona 1]: [description]
- [Persona 2]: [description]

**Economic Buyer**
- [Who makes purchase decision and why]

## Product Breakdown

- **[Module 1]** - [Technical description of what it does, how it works]
- **[Module 2]** - [Technical description]
- **[Module 3]** - [Technical description]
- **API & Integrations** - [List of integrations, available APIs]

## User Journey & Delivery Model

1. **[Step 1]**: [Description]
2. **[Step 2]**: [Description]
3. **[Step 3]**: [Description]

**Delivery Model**: [SaaS / On-premise / Hybrid], [description]

## Pricing

| Tier | Price | Includes |
|------|-------|----------|
| Starter | X EUR/month | ... |
| Pro | Y EUR/month | ... |
| Enterprise | Custom | ... |

## Differentiation & Moat

**What differentiates [Company]**:
- [Differentiator 1]: [explanation]
- [Differentiator 2]: [explanation]

**Primary Moat**: [Description - proprietary tech, network effects, switching costs, etc.]
```

---

## 3.6 - Market (`market.md`)

**Sources**: WebSearch market reports, site, news

**WebSearch queries**:
```
"{sector}" market size 2025 2026 forecast
"{sector}" market analysis report
"{sector}" TAM SAM SOM
"{sector}" industry trends 2025
```

```markdown
# Market Analysis

## Market Segmentation

### Primary Segment (TAM)
- **Segment**: [e.g., PLM Software]
- **Size**: [XX]B USD (source: [source])
- **CAGR**: [X]% (2024-2030)
- **Description**: [description]

### Sub-Segment (SAM)
- **Segment**: [e.g., PLM for Process Industries]
- **Size**: [X]B USD
- **CAGR**: [X]%
- **Description**: [why different]

### Niche (SOM)
- **Segment**: [e.g., PLM for Cosmetics R&D]
- **Size**: [X]M USD
- **CAGR**: [X]%
- **Description**: [company's specific niche]

## Adjacent Markets

| Market | Size | Link to Core | Potential |
|--------|------|--------------|-----------|
| [e.g., Pharma PLM] | [X]B USD | [Similar formulation] | High/Medium/Low |
| [e.g., Food PLM] | [X]B USD | [Process manufacturing] | High/Medium/Low |

## Market Dynamics

### Key Trends
1. **[Trend 1]**: [description and impact]
2. **[Trend 2]**: [description and impact]
3. **[Trend 3]**: [description and impact]

### Growth Drivers
- [Driver 1]
- [Driver 2]

### Market Barriers
- [Barrier 1]
- [Barrier 2]

## Positioning

**Tagline**: "[site tagline]"

- **Vertical/Horizontal**: [Specialized vertical / Multi-industry horizontal]
- **Price segment**: [Premium / Mid-market / Low-cost]
- **Target**: [Enterprise / Mid-market / SMB / Startup]
- **Approach**: [Best-of-breed specialist / Integrated suite]

## Recent Market Activity

| Date | Event | Impact |
|------|-------|--------|
| [date] | [Acquisition/Funding/Launch] by [actor] | [market impact] |

## Sources
- [Report 1](url)
- [Report 2](url)
```

---

## 3.7 - Competitors (`competitors.md`)

**Sources**: G2 alternatives, WebSearch

**WebSearch queries**:
```
"{competitor}" market share revenue
"{sector}" market share analysis 2025
"{competitor}" annual revenue ARR
```

```markdown
# Key Competitors

## Landscape Overview

[3-4 sentence synthesis: number of players, types (specialized vs generic), trends]

## Market Share Estimates

| Competitor | Type | Est. Revenue | Market Share | Positioning |
|------------|------|--------------|--------------|-------------|
| [Competitor 1] | Direct | ~XXM EUR | ~X% | [short desc] |
| [Competitor 2] | Direct | ~XXM EUR | ~X% | [short desc] |
| [Competitor 3] | Indirect | ~XXXM EUR | ~X% | [short desc] |
| [Company] | - | ~XXM EUR | ~X% | [short desc] |

*Note: Estimates based on [sources: headcount, funding, public clients, etc.]*

## Competitor Profiles

### [Competitor 1]
- **Site**: [url]
- **Stage**: [Seed/Series A/Exited/Bootstrapped]
- **Funding**: [total raised]
- **Headcount**: [number]
- **Est. Revenue**: [amount] (source: [source])
- **Clients**: [examples if known]
- **Primary focus**: [main focus]
- **Key differentiators**: [what sets them apart]
- **Strengths**: [list]
- **Weaknesses**: [list]

### [Competitor 2]
...

## Key Competitive Differences

**Competitors lead:**
- **[Competitor X]** excels in [domain] - [detailed explanation]
- **[Competitor Y]** leads in [domain] - [detailed explanation]

**Areas where [Company] leads:**
- **[Advantage 1]**: [detailed explanation]
- **[Advantage 2]**: [detailed explanation]

## Competitive Moat Analysis

[Analysis of company's moat vs competitors: switching costs, network effects, proprietary tech, etc.]
```

---

## 3.8 - GTM (`gtm.md`)

**Sources**: site, pricing, jobs/, news

```markdown
# Go-to-Market

## Sales Model
- **Type**: [Self-serve / Sales-led / PLG / Hybrid]
- **Channels**: [site, demo request, marketplace, partners]

## Pricing Strategy
- **Model**: [Freemium / Free trial / Quote-based]
- **Entry point**: [price]
- **Upsell path**: [description]

## Sales Team (from jobs/ and LinkedIn)
- Sales headcount: [X]
- Regions covered: [list]
- Key roles hiring: [list]

## Partners & Channels
- [Partner type 1]: [examples]
- [Partner type 2]: [examples]
```

---

## 3.9 - Marketing (`marketing.md`)

**Sources**: rs/, site-web/, news/, reviews/

```markdown
# Marketing Analysis

## Synthesis

[3-4 sentence summary: main channels, tone, strengths and weaknesses]

## Digital Presence

### Website
- **URL**: [url]
- **Languages**: [list]
- **Blog**: [Yes/No] - [frequency] - [main themes]
- **SEO**: [quick analysis - meta, structure, performance]

### Social Media

| Platform | URL | Followers | Engagement | Frequency |
|----------|-----|-----------|------------|-----------|
| LinkedIn | [url] | [number] | [active/inactive] | [X posts/week] |
| Twitter/X | [url] | [number] | [active/inactive] | [X posts/week] |
| YouTube | [url] | [number] | [active/inactive] | [X videos/month] |
| Instagram | [url or N/A] | [number or N/A] | ... | ... |

**Recent LinkedIn posts** (examples):
- [Date]: "[Title/Summary]" - [engagement]
- [Date]: "[Title/Summary]" - [engagement]

## Reviews & Reputation

| Platform | URL | Rating | Reviews |
|----------|-----|--------|---------|
| G2 | [url or N/A] | [X/5] | [number] |
| Capterra | [url or N/A] | [X/5] | [number] |
| Trustpilot | [url or N/A] | [X/5] | [number] |

**Analysis**: [Commentary on presence/absence of reviews and impact]

## Events & Conferences

| Event | Date | Type | Location |
|-------|------|------|----------|
| [Conference name] | [date] | Exhibitor/Sponsor | [city] |

## Communication Tone
[Description: corporate, startup, technical, casual, etc.]
```

---

## 3.10 - News (`news.md`)

```markdown
# Traction & Recent News

## Web and Social Media Traction

[2-3 sentence description of web and social traction]

| Platform | Metric | Value | Trend |
|----------|--------|-------|-------|
| Website | Est. traffic | [X visits/month] | [+X%] |
| LinkedIn | Followers | [X] | [+X%] |
| Twitter | Followers | [X] | [+X%] |

## Company News

- **[Date]**: [Event]. [Source](url)
- **[Date]**: [Event]. [Source](url)
```

---

## 3.11 - Legal (`legal.md`)

**Sources**: site footer, legal pages, WebSearch

```markdown
# Legal & Compliance

## Company Compliance

| Criteria | Status |
|----------|--------|
| Legal mentions | Present/Absent |
| Terms & Conditions | ... |
| GDPR/DPO | ... |

## Certifications

| Certification | Expected | Status |
|--------------|----------|--------|
| ISO 27001 | Yes (EU enterprise) | Not displayed |
| SOC 2 Type 2 | Yes (US enterprise) | Not displayed |
| 21 CFR Part 11 | [If applicable] | ... |

## Industry Regulations

[Industry-specific regulations and how product addresses them]

## Gap Analysis
- **Strengths**: ...
- **Gaps**: ...
```

---

## 3.12 - SWOT (`swot.md`)

```markdown
# SWOT Analysis

| | Positive | Negative |
|---|----------|----------|
| **Internal** | **Strengths:** [...] | **Weaknesses:** [...] |
| **External** | **Opportunities:** [...] | **Threats:** [...] |

## Detailed Analysis

### Strengths
- [Strength 1]: [explanation]
- [Strength 2]: [explanation]

### Weaknesses
- [Weakness 1]: [explanation]
- [Weakness 2]: [explanation]

### Opportunities
- [Opportunity 1]: [explanation]
- [Opportunity 2]: [explanation]

### Threats
- [Threat 1]: [explanation]
- [Threat 2]: [explanation]
```
