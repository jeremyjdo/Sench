# Collection Methods

Detailed methods for Phase 2 data collection.

## 2.1 - Website Scraping

### With agent-browser

```bash
# Screenshot homepage
agent-browser open "https://URL" && agent-browser screenshot "./sench_{name}/site-web/screenshots/homepage.png"

# Get page content (accessibility tree)
agent-browser snapshot
```

### Pages to scrape (priority order)

1. Homepage
2. About / A propos
3. Pricing / Tarifs
4. Product / Features
5. Customers / Use cases
6. Team / Equipe
7. Blog (first page)
8. Contact

### Output files

- `arborescence.md` - All discovered URLs
- `pages/homepage.md` - Homepage content
- `pages/about.md`, `pages/pricing.md`, etc.

### Fallback

If agent-browser fails, use WebFetch on key pages.

---

## 2.2 - News

### WebSearch queries

```
"{company}" actualite 2025 OR 2026
"{company}" news 2025 OR 2026
"{company}" levee de fonds OR funding
"{company}" partenariat OR partnership OR acquisition
```

### Output format (`news/news.md`)

```markdown
## [Article Title]
- **Date**: ...
- **Source**: [name](url)
- **Summary**: ...
```

---

## 2.3 - Social Media

### Find accounts

```
WebSearch: "{company}" site:linkedin.com/company
WebSearch: "{company}" site:twitter.com OR site:x.com
WebSearch: "{company}" site:instagram.com
```

### Output

- `rs/links.md` - All social URLs found
- `rs/linkedin.md` - Recent posts
- `rs/twitter.md` - Recent tweets
- `rs/instagram.md` - Recent posts

---

## 2.4 - Reviews

### WebSearch queries

```
"{company}" avis google
"{company}" site:g2.com
"{company}" site:capterra.com
"{company}" site:trustpilot.com
```

### Output format

- `reviews/google.md` - Google reviews summary
- `reviews/g2.md` - G2 rating, pros/cons, review excerpts

---

## 2.5 - Jobs

### WebSearch queries

```
"{company}" offres emploi site:linkedin.com/jobs
"{company}" site:welcometothejungle.com
"{company}" careers jobs
```

### Output format (`jobs/linkedin.md`, `jobs/wttj.md`)

```markdown
## [Job Title]
- **Location**: ...
- **Type**: CDI/CDD/Stage/Freelance
- **Remote**: yes/no/hybrid
- **Stack/Skills**: ...
- **URL**: ...
```

---

## 2.6 - Tech Stack

### Sources

- Job postings (jobs/)
- Website source (headers, meta, scripts)
- WebSearch queries:

```
"{company}" stack technique OR tech stack
"{company}" site:stackshare.io
"{company}" engineering blog
```

### Output (`stack/stack.md`)

```markdown
# Tech Stack

## Frontend
- [Tech 1] (source: job posting)

## Backend
- [Tech 2] (source: stackshare)

## Infrastructure
- [Tech 3] (source: website)
```

---

## 2.7 - Employees

### Goal

Find at least 50% of LinkedIn employee count.

### Step 1: Get total count

Note LinkedIn company page employee count (e.g., "58 employees on LinkedIn")

### Step 2: Role-based searches (do ALL)

```
"{company}" CEO OR founder site:linkedin.com/in
"{company}" CTO OR "chief technology" site:linkedin.com/in
"{company}" CFO OR "chief financial" site:linkedin.com/in
"{company}" CPO OR "chief product" site:linkedin.com/in
"{company}" CRO OR "chief revenue" site:linkedin.com/in
"{company}" VP OR "vice president" site:linkedin.com/in
"{company}" director site:linkedin.com/in
"{company}" manager site:linkedin.com/in
"{company}" engineer OR developer site:linkedin.com/in
"{company}" sales site:linkedin.com/in
"{company}" customer success site:linkedin.com/in
"{company}" marketing site:linkedin.com/in
"{company}" product site:linkedin.com/in
```

### Step 3: Geographic searches (if multi-country)

```
"{company}" employees france site:linkedin.com/in
"{company}" employees USA site:linkedin.com/in
"{company}" employees asia site:linkedin.com/in
```

### Step 4: Alternative sources

- Team page from website (already scraped)
- `"{company}" employees site:rocketreach.co`
- `"{company}" employees site:zoominfo.com`

### Output format (`employees/employees.md`)

```markdown
# Employees - [Company]

**Sources**: LinkedIn, website, [others]
**Total**: ~[X] (LinkedIn) / [Y] (WTTJ)

## Direction / C-Level

| Name | Role | LinkedIn | Location |
|------|------|----------|----------|
| ... | CEO | https://linkedin.com/in/... | Paris |

## Tech & Product

| Name | Role | LinkedIn |
|------|------|----------|

## Sales & Business Development

| Name | Role | LinkedIn | Region |
|------|------|----------|--------|

## Customer Success

| Name | Role | LinkedIn |
|------|------|----------|

## Marketing & Communication

| Name | Role | LinkedIn |
|------|------|----------|

## Operations & Support

| Name | Role | LinkedIn |
|------|------|----------|

## Former Executives (if relevant)
- **[Name]**: [former role] → [new role/departure]
```
