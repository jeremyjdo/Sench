# Competitor Analysis

Identify competitors based on website content and market positioning.

## Content
```
{scraped_content}
```

## Domain: {domain}

## Instructions

Identify:
1. **Direct competitors** - Same product, same market
2. **Indirect competitors** - Different product, same problem
3. **Alternatives** - What customers used before
4. **Competitive advantages** - How company positions vs competition
5. **Comparison pages** - If they have "vs" pages

## Output Schema

```json
{
  "direct_competitors": [
    {
      "name": "string",
      "domain": "string | null",
      "why_competitor": "string",
      "differentiation": "string"
    }
  ],
  "indirect_competitors": [
    {
      "name": "string",
      "domain": "string | null",
      "overlap": "string"
    }
  ],
  "alternatives": ["string"],
  "competitive_positioning": "string",
  "claimed_advantages": ["string"],
  "comparison_pages_found": ["string"]
}
```
