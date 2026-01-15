# Market & Value Proposition Analysis

Analyze the company's market positioning and value proposition.

## Content
```
{scraped_content}
```

## Domain: {domain}

## Instructions

Analyze:
1. **Value proposition** - Core value offered
2. **Target market** - Who they serve
3. **Market category** - Which market they compete in
4. **Positioning** - How they differentiate
5. **Use cases** - Specific use cases mentioned
6. **Social proof** - Testimonials, logos, case studies

## Output Schema

```json
{
  "value_proposition": "string",
  "tagline": "string | null",
  "target_market": {
    "segment": "B2B | B2C | B2B2C | Mixed",
    "company_size": ["Startup", "SMB", "Mid-Market", "Enterprise"],
    "industries": ["string"],
    "personas": ["string"]
  },
  "market_category": "string",
  "positioning_statement": "string",
  "key_differentiators": ["string"],
  "use_cases": ["string"],
  "social_proof": {
    "customer_logos": ["string"],
    "testimonials_count": "number",
    "case_studies_count": "number",
    "metrics_claims": ["string"]
  }
}
```
