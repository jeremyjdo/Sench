---
name: sench
description: Competitive intelligence sub-agent for French companies. Analyze any company from name, SIREN, or website. Use when user asks to analyze a company, research competitors, or generate a company report. Scrapes websites with agent-browser, queries API gouv (no API key), returns structured Harmonic-style report.
---

# /sench - Competitive Intelligence

Analyse concurrentielle complete d'une entreprise francaise. Produit un rapport au format Harmonic Scout.

## Workflow Overview

```
Input (name/SIREN/website)
    │
    ▼
Phase 1: Identification ──► Validate with user
    │
    ▼
Phase 2: Collection ──► site-web/, news/, rs/, reviews/, jobs/, employees/
    │
    ▼
Phase 3: Analysis ──► analyse/*.md (12 modules)
    │
    ▼
Phase 4: Report ──► rapport.md (Harmonic format)
```

## Prerequisites

```bash
# Check if agent-browser is installed
which agent-browser || echo "Not installed"

# Install if needed
npm install -g agent-browser
agent-browser install
```

## Rules

1. **Always Phase 1 first** - never collect without validated identification
2. **Always ask user validation** before Phase 2
3. **Never invent data** - use "Non disponible" if missing
4. **Public information only**
5. **All files in .md format**

---

## Phase 1: Identification

Detect input type and find missing information.

### Input Detection

- **9-14 digits** → SIREN/SIRET → fetch from API gouv
- **Contains `.`** → website → WebFetch then API gouv
- **Otherwise** → company name → API gouv + WebSearch

### API Recherche Entreprises (no API key required)

```
WebFetch: https://recherche-entreprises.api.gouv.fr/search?q={query}&page=1&per_page=5
```

See [references/api-gouv.md](references/api-gouv.md) for response fields and examples.

### User Validation

Present company card and ask validation via AskUserQuestion:

```
| Field | Value |
|-------|-------|
| Nom | [raison sociale] |
| SIREN | [numero] |
| Site web | [url] |
| Siege | [adresse] |
| Creation | [date] |
| Effectifs | [tranche] |
| Dirigeants | [liste] |
```

Options: "Oui, c'est la bonne entreprise" / "Non, ce n'est pas la bonne"

---

## Phase 2: Collection

Create folder structure and collect data. See [references/collection.md](references/collection.md) for detailed methods.

### Folder Structure

```
sench_{company}/
├── site-web/
│   ├── arborescence.md
│   ├── pages/*.md
│   └── screenshots/homepage.png
├── news/news.md
├── rs/
│   ├── links.md
│   └── {platform}.md
├── reviews/
│   ├── google.md
│   └── g2.md
├── jobs/
│   ├── linkedin.md
│   └── wttj.md
├── stack/stack.md
├── employees/employees.md
├── analyse/*.md
└── rapport.md
```

### Collection Steps

| Step | Source | Method |
|------|--------|--------|
| 2.1 Site web | Company website | agent-browser or WebFetch |
| 2.2 News | Press, blogs | WebSearch |
| 2.3 Social | LinkedIn, Twitter, Instagram | WebSearch + WebFetch |
| 2.4 Reviews | G2, Google | WebSearch + WebFetch |
| 2.5 Jobs | LinkedIn, WTTJ | WebSearch + WebFetch |
| 2.6 Stack | Jobs, site, StackShare | WebSearch |
| 2.7 Employees | LinkedIn | WebSearch (13+ role searches) |

---

## Phase 3: Analysis

Produce analysis files in `analyse/`. See [references/analysis-modules.md](references/analysis-modules.md) for formats.

| Module | File | Key Sources |
|--------|------|-------------|
| Identity | identity.md | API gouv, INPI |
| Funding | funding.md | Crunchbase, Dealroom, press |
| Team | team.md | LinkedIn, site, employees/ |
| Finance | finance.md | API gouv, Pappers |
| Product | product.md | site-web/, reviews/ |
| Market | market.md | WebSearch market reports |
| Competitors | competitors.md | G2, WebSearch |
| GTM | gtm.md | pricing, jobs/ |
| Marketing | marketing.md | rs/, site-web/ |
| News | news.md | news/ |
| Legal | legal.md | site footer, WebSearch |
| SWOT | swot.md | All modules |

---

## Phase 4: Final Report

Produce `rapport.md` in Harmonic Scout format. See [references/report-template.md](references/report-template.md) for complete template.

### Report Structure

1. **Overview** - 2-3 sentences + 4 insights
2. **Company Card** - Founded, Stage, Funding, Headcount, Founders
3. **Funding** - Investment history timeline
4. **Team** - Narrative profiles (not just tables)
5. **Headcount & Hiring** - Trends and open roles
6. **Product Overview** - Core thesis, ICP, breakdown, moat
7. **Market Analysis** - TAM/SAM/SOM, adjacent markets, trends
8. **Competitors** - Market share estimates, profiles, differences
9. **Traction & News** - Social metrics, recent events
10. **Legal & Compliance** - Certifications, regulations
11. **SWOT** - Summary matrix
12. **Sources** - All sources with URLs

---

## Notes

- If a page is inaccessible (404, anti-bot), skip and note "Non accessible"
- If agent-browser fails, use WebFetch as fallback
- For non-French companies, SIREN/INPI don't apply
- Prioritize data quality over quantity
- Always cite sources
- **Report must be narrative-rich**, not just tables
