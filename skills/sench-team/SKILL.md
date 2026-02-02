---
name: sench-team
description: Analyze a company's team structure and founders. Returns employee list by department with LinkedIn URLs, founder backgrounds, and team composition analysis. No external tools required.
---

# /sench-team - Team & Founders Analysis

Deep dive on a company's team structure and founder backgrounds.

## Usage

```
/sench-team {company}           # Default language (English)
/sench-team {company} --fr      # French output
/sench-team {company} --en      # English output (explicit)
```

## Workflow

```
Input (company name) + optional --fr/--en
    ↓
1. Find LinkedIn company page
    ↓
2. Collect employees by department
    ↓
3. Deep dive on founders
    ↓
4. Report → {company}_team.md
```

## Rules

1. **Never invent data** - use "Not found" (or "Non trouvé" if --fr) if missing
2. **Always include LinkedIn URLs** when found
3. **Single output file** - `{company}_team.md`
4. **Exact counts** - always report exact number of employees found, not ranges
5. **Sources required** - always include LinkedIn URL + website in Sources section

---

## Phase 1: Find Company

### Search for LinkedIn

```
WebSearch: "{company}" site:linkedin.com/company
```

Note the company LinkedIn URL and employee count displayed.

### Get Website

```
WebSearch: "{company}" official website
WebFetch: {website}/about OR {website}/team
```

---

## Phase 2: Collect Employees

### Search by Role (do ALL searches)

```
# Leadership
"{company}" CEO founder site:linkedin.com/in
"{company}" CTO "chief technology" site:linkedin.com/in
"{company}" CFO "chief financial" site:linkedin.com/in
"{company}" COO "chief operating" site:linkedin.com/in
"{company}" CPO "chief product" site:linkedin.com/in

# Department Heads
"{company}" VP "vice president" site:linkedin.com/in
"{company}" director site:linkedin.com/in
"{company}" head of site:linkedin.com/in

# Engineering
"{company}" engineer developer site:linkedin.com/in
"{company}" tech lead site:linkedin.com/in

# Product & Design
"{company}" product manager site:linkedin.com/in
"{company}" designer UX site:linkedin.com/in

# Sales & Marketing
"{company}" sales site:linkedin.com/in
"{company}" marketing site:linkedin.com/in
"{company}" growth site:linkedin.com/in

# Operations & Compliance
"{company}" operations site:linkedin.com/in
"{company}" HR "people" site:linkedin.com/in
"{company}" finance site:linkedin.com/in
"{company}" compliance legal site:linkedin.com/in
```

### Alternative Sources

```
"{company}" team site:welcometothejungle.com
"{company}" team about
WebFetch: {website}/about OR {website}/team
```

---

## Phase 3: Founder Deep Dive

For each founder/CEO:

```
"{founder_name}" background career
"{founder_name}" education
"{founder_name}" previous company
"{founder_name}" interview
```

Collect:
- Education (school, degree, year)
- Previous companies and roles
- Notable achievements
- Time at current company

---

## Phase 4: Report

Output: `{company}_team.md`

### Language Parameter

- Default or `--en`: English output
- `--fr`: French output (use French headers and content)

```markdown
# {Company} - Team Analysis

*{date}*

---

## Summary

{3-4 sentences: team size, composition, key points about founders, strengths/weaknesses}

| | |
|---|---|
| **Headcount** | {exact number} (LinkedIn) |
| **Founded** | {year} |
| **Founders** | {names} |
| **LinkedIn** | [{company}]({url}) |

---

## Founders

### {Name} - {Title}

**Background:**
{Narrative paragraph 3-4 sentences: career path, education, previous experience, expertise}

| | |
|---|---|
| **LinkedIn** | [{name}]({url}) |
| **Education** | {school}, {degree} ({year}) |
| **Previous** | {company} - {role} ({years}) |
| **At {company} since** | {year} |

### {Name 2} - {Title}
...

---

## Team by Department

### Leadership ({count})

| Name | Role | LinkedIn |
|------|------|----------|
| {name} | CEO | [{profile}]({url}) |
| {name} | CTO | [{profile}]({url}) |

### Engineering ({count})

| Name | Role | LinkedIn |
|------|------|----------|
| {name} | {title} | [{profile}]({url}) |

### Product & Design ({count})

| Name | Role | LinkedIn |
|------|------|----------|
| {name} | {title} | [{profile}]({url}) |

### Sales & Marketing ({count})

| Name | Role | LinkedIn |
|------|------|----------|
| {name} | {title} | [{profile}]({url}) |

### Operations & Support ({count})

| Name | Role | LinkedIn |
|------|------|----------|
| {name} | {title} | [{profile}]({url}) |

---

## Analysis

### Composition

- **Total identified:** {X} on LinkedIn
- **Tech/Business ratio:** {X}% / {Y}%
- **Leadership:** {observations}

### Strengths

- {strength 1}
- {strength 2}

### Areas of Concern

- {concern 1}
- {concern 2}

### Hiring Signals

{Observations based on job postings: where are they investing?}

---

## Sources

- LinkedIn: {url}
- Website: {url}
- {other sources with URLs}
```
