# Company Identity Analysis

Analyze the following website content to extract the company's identity information.

## Website Content
```
{scraped_content}
```

## Instructions

Extract the following information:
1. **Official company name** - The legal/official name
2. **Brand name** - If different from official name
3. **Tagline/Slogan** - The company's main tagline
4. **Description** - A 2-3 sentence description of what the company does
5. **Industry** - Primary industry (SaaS, FinTech, HealthTech, etc.)
6. **Founded year** - When the company was founded
7. **Headquarters** - City, Country
8. **Company size** - Approximate number of employees if mentioned
9. **Website URL** - Main domain
10. **Social links** - LinkedIn, Twitter/X, etc.

## Output Schema

```json
{
  "official_name": "string",
  "brand_name": "string | null",
  "tagline": "string | null",
  "description": "string",
  "industry": "string",
  "sub_industries": ["string"],
  "founded_year": "number | null",
  "headquarters": {
    "city": "string | null",
    "country": "string | null"
  },
  "employee_count": "string | null",
  "website_url": "string",
  "social_links": {
    "linkedin": "string | null",
    "twitter": "string | null",
    "github": "string | null",
    "other": ["string"]
  }
}
```
