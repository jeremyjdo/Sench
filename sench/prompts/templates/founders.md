# Founders & Leadership Analysis

Analyze the following content to identify founders and key leadership.

## Content
```
{scraped_content}
```

## Company Context
Domain: {domain}

## Instructions

Identify and extract:
1. **Founders** - Names, roles, backgrounds
2. **C-level executives** - CEO, CTO, CFO, etc.
3. **Advisory board** - Notable advisors if mentioned
4. **LinkedIn profiles** - If available
5. **Background** - Previous companies, education

## Output Schema

```json
{
  "founders": [
    {
      "name": "string",
      "title": "string",
      "linkedin_url": "string | null",
      "background": "string | null",
      "previous_companies": ["string"],
      "is_technical": "boolean"
    }
  ],
  "executives": [
    {
      "name": "string",
      "title": "string",
      "linkedin_url": "string | null"
    }
  ],
  "advisors": ["string"],
  "team_size_signals": "string | null",
  "hiring_signals": ["string"]
}
```
