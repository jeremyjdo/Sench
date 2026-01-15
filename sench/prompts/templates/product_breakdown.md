# Product Breakdown Analysis

Analyze the product offering based on website content.

## Content
```
{scraped_content}
```

## Domain: {domain}

## Instructions

Extract detailed product information:
1. **Core product(s)** - Main offerings
2. **Features** - Key features per product
3. **Pricing model** - Free, freemium, subscription, usage-based
4. **Pricing tiers** - If visible
5. **Integrations** - Third-party integrations
6. **Platform** - Web, mobile, desktop, API
7. **Technology signals** - Tech stack if visible

## Output Schema

```json
{
  "products": [
    {
      "name": "string",
      "description": "string",
      "target_user": "string",
      "key_features": ["string"],
      "differentiators": ["string"]
    }
  ],
  "pricing_model": "Free | Freemium | Subscription | Usage-based | Enterprise | Unknown",
  "pricing_tiers": [
    {
      "name": "string",
      "price": "string",
      "features": ["string"]
    }
  ],
  "has_free_trial": "boolean",
  "integrations": ["string"],
  "platforms": ["Web", "iOS", "Android", "Desktop", "API"],
  "technology_signals": ["string"]
}
```
