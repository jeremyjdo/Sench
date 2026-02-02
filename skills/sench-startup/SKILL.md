---
name: sench-startup
description: Competitive intelligence for startups. Analyze any company from name, SIREN, or website. Returns funding, team, product, market, and competitor analysis. No external tools required.
---

# /sench-startup - Competitive Intelligence

Full competitive intelligence report on any startup.

## Usage

```
/sench-startup {company}           # Default language (English)
/sench-startup {company} --fr      # French output
/sench-startup {company} --en      # English output (explicit)
```

## Workflow

```
Input (name/SIREN/website) + optional --fr/--en
    ↓
1. Identification (API gouv + WebSearch)
    ↓
2. User validation
    ↓
3. Data collection (WebSearch + WebFetch)
    ↓
4. Report → {company}_analysis.md
```

## Rules

1. **Always identify first** - validate with user before analysis
2. **Never invent data** - use "Not available" (or "Non disponible" if --fr) if missing
3. **Single output file** - `{company}_analysis.md`
4. **Exact counts** - always report exact numbers found, not ranges
5. **Sources required** - always include LinkedIn URL + website in Sources section

---

## Phase 1: Identification

### Input Detection

- **9-14 digits** → SIREN/SIRET
- **Contains `.`** → website
- **Otherwise** → company name

### API Recherche Entreprises (no API key)

```
WebFetch: https://recherche-entreprises.api.gouv.fr/search?q={query}&page=1&per_page=5
```

Key fields in `results[]`:
- `siren`, `nom_complet`, `date_creation`
- `siege.adresse`, `siege.code_postal`, `siege.commune`
- `tranche_effectif_salarie`, `activite_principale`
- `dirigeants[]` (nom, prenoms, qualite)

### User Validation

Present company card via AskUserQuestion:

| Field | Value |
|-------|-------|
| Name | {company name} |
| SIREN | {number} |
| Website | {url} |
| HQ | {address} |
| Headcount | {range} |

Options: "Yes, correct" / "No"

---

## Phase 2: Data Collection

Use WebSearch and WebFetch only.

### Research Sources

| Source | What to Find | Method |
|--------|--------------|--------|
| **Website** | Messaging, features, pricing | WebFetch: {url}, /pricing, /about |
| **API gouv** | Legal info, headcount, executives | WebFetch: API endpoint |
| **G2/Capterra** | Reviews, ratings, complaints | WebSearch: site:g2.com |
| **LinkedIn** | Company page, employees, posts | WebSearch: site:linkedin.com/company |
| **Crunchbase** | Funding rounds, investors, news | WebSearch: site:crunchbase.com |
| **Dealroom** | Funding, valuation | WebSearch: site:dealroom.co |
| **Twitter/X** | Announcements, sentiment | WebSearch: site:twitter.com |
| **Job postings** | Where they invest, tech stack | WebSearch: site:welcometothejungle.com |
| **Blog/Changelog** | Product direction, roadmap | WebFetch: {url}/blog |
| **Press** | News, partnerships, acquisitions | WebSearch: "{company}" news 2025 |

### Search Queries

```
# Funding & Investors
"{company}" funding round series
"{company}" site:crunchbase.com
"{company}" site:dealroom.co

# Team & Leadership
"{company}" CEO founder site:linkedin.com/in
"{company}" CTO site:linkedin.com/in
"{company}" leadership team

# Product & Reviews
"{company}" site:g2.com
"{company}" site:capterra.com
"{company}" reviews

# Competitors & Market
"{company}" competitors alternatives
"{company}" vs
"{sector}" market size TAM

# Hiring & Investment Areas
"{company}" site:welcometothejungle.com
"{company}" careers jobs

# News & Traction
"{company}" news 2025
"{company}" partnership
```

---

## Phase 3: Report

Output: `{company}_analysis.md`

### Language Parameter

- Default or `--en`: English output
- `--fr`: French output (use French headers and content)

```markdown
# {Company} - Scout Report

*{date}*

---

## Overview

{2-3 sentences: business, target, value proposition}

| | |
|---|---|
| **Founded** | {year} |
| **Stage** | {Seed/Series A/B/Bootstrapped} |
| **Funding** | {total} |
| **Headcount** | {exact number} |
| **HQ** | {city} |

[Website]({url}) · [LinkedIn]({url})

---

## Insights

- {Insight 1}
- {Insight 2}
- {Insight 3}

---

## Funding

| Round | Amount | Date | Lead |
|-------|--------|------|------|
| {type} | {amount} | {date} | {investor} |

---

## Team

### {Name} - {Title}
{Bio 2-3 sentences}
LinkedIn: {url}

---

## Product

### Core Product Overview

{2-3 sentences describing what the product does, how it works, and what problem it solves}

### Major Product Components

1. **{Component 1}:** {Description of feature and value}
2. **{Component 2}:** {Description of feature and value}
3. **{Component 3}:** {Description of feature and value}

### Pricing

| Product | Price | Notes |
|---------|-------|-------|
| {tier} | {price} | {context} |

*Source: [{website}]({url}) - {date}*

### Ideal Customer Profile (ICP)

#### Primary ICP: {Persona Name}

| Attribute | Detail |
|-----------|--------|
| **Age** | {range} |
| **Status** | {job/life status} |
| **Location** | {geography} |
| **Budget** | {spending capacity} |
| **Pain Points** | {main problems} |
| **Motivation** | {why they buy} |

#### Secondary ICP: {Persona Name}
{Similar table structure}

### Key Differentiators

- **{Category}:** {Specific advantage}
- **{Category}:** {Specific advantage}

---

## Reviews

| Source | Rating | Reviews | Key Feedback |
|--------|--------|---------|--------------|
| G2 | {X}/5 | {count} reviews | {main pros/cons} |
| Capterra | {X}/5 | {count} reviews | {main pros/cons} |
| Trustpilot | {X}/5 | {count} reviews | {main pros/cons} |

**Common Praise:** {what users love}
**Common Complaints:** {recurring issues}

*Sources: [G2]({url}), [Capterra]({url}), [Trustpilot]({url})*

---

## Market

### Market Segments

```
{Industry}
├── {Segment 1}
│   ├── {Sub-segment} ← {Company position}
│   └── {Sub-segment}
└── {Segment 2}
    └── {Sub-segment}
```

### Market Sizing

| Level | Segment | Size | Source |
|-------|---------|------|--------|
| **TAM** | {broad market} | {X}B | {source} |
| **SAM** | {addressable} | {X}B | {source} |
| **SOM** | {obtainable} | {X}M | {source} |

### Market Trends

| Trend | Impact |
|-------|--------|
| {Trend 1} | {Tailwind/Headwind - explanation} |
| {Trend 2} | {Tailwind/Headwind - explanation} |

**Trends:** {key trends}

---

## Competitors

| Name | Positioning | Funding |
|------|-------------|---------|
| {competitor} | {positioning} | {amount} |

**{Company} leads in:** {area}
**Competitors lead in:** {area}

---

## Hiring

| Department | Open Roles | Level | Source |
|------------|------------|-------|--------|
| {Engineering} | {X} positions | {Junior/Senior/Lead} | [WTTJ]({url}) |
| {Sales} | {X} positions | {level} | [Careers]({url}) |

**Investment Focus:** {where the company is hiring most - engineering, sales, ops}

**Tech Stack:** {technologies mentioned in job postings}

*Sources: [Welcome to the Jungle]({url}), [Careers page]({url})*

---

## News

- {date}: {event} ([source]({url}))

---

## SWOT

| Strengths | Weaknesses |
|-----------|------------|
| {item} | {item} |

| Opportunities | Threats |
|---------------|---------|
| {item} | {item} |

---

## Sources

- LinkedIn: {url}
- Website: {url}
- {other sources with URLs}
```
