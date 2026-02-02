# CLAUDE.md - Sench Project Guidelines

## Project Overview

Sench provides competitive intelligence skills for AI agents (Claude Code, Codex, Cursor).

## Skills

- `/sench-startup` - Full competitive intelligence report
- `/sench-team` - Team structure and founder analysis

## Skill Improvement Guidelines

When user feedback indicates issues with skill output, always update the SKILL.md accordingly:

### Data Quality
- **Exact counts**: Always report exact numbers found (e.g., "19 employees" not "10-49")
- **Sources required**: Every report must include LinkedIn URL + website in Sources section
- **Never invent**: Use "Not found" / "Non trouvé" for missing data

### Output Format
- **Language parameter**: Support `--fr` and `--en` flags for output language
- **Default language**: English
- **Single file**: One markdown report per analysis

### Research Thoroughness
- Search multiple LinkedIn queries to maximize employee discovery
- Cross-reference company page count with found profiles
- Include compliance/legal roles in team searches

## Folder Structure

```
skills/
  sench-startup/
    SKILL.md
    README.md
  sench-team/
    SKILL.md
    README.md
examples/
  ornikar_analysis.md
  1point6_team.md
landing-page/
  index.html
  sench-startup.html
  sench-team.html
```

## Common Issues & Fixes

| Issue | Fix |
|-------|-----|
| Employee count shows range instead of exact | Count all unique profiles found |
| Missing sources | Always add LinkedIn + Website to Sources |
| Output in wrong language | Check for --fr/--en flag, default to English |
| Incomplete team list | Run ALL search queries in Phase 2 |

## Report Quality Guidelines

### Product Section
- Include **Core Product Overview** with narrative description
- List **Major Product Components** (numbered list with descriptions)
- **Pricing** must include source URL and date
- **ICP** should be detailed with tables: Age, Status, Location, Budget, Pain Points, Motivation
- Include both **Primary** and **Secondary** ICPs

### Market Section
- Start with **Market Segments** tree diagram showing company position
- **Market Sizing** table must include Source column
- Add **Key Market Data** with specific numbers
- **Market Trends** should indicate Tailwind/Headwind impact

## Documentation Maintenance

**IMPORTANT:** Always update README.md when making changes to:
- Skill names or commands
- Output format or sections
- Language options (--fr, --en)
- Installation instructions
- Example files

Keep README.md in sync with actual skill capabilities.
