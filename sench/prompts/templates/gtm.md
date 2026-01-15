# Go-to-Market Strategy Analysis

Analyze the company's go-to-market strategy based on website signals.

## Content
```
{scraped_content}
```

## Domain: {domain}

## Instructions

Analyze GTM signals:
1. **Sales model** - Self-serve, sales-led, PLG, hybrid
2. **Acquisition channels** - How they acquire customers
3. **Conversion path** - CTA flow (trial, demo, contact)
4. **Onboarding** - Self-serve or guided
5. **Pricing strategy** - Transparent vs hidden
6. **Enterprise signals** - Security, compliance pages

## Output Schema

```json
{
  "sales_model": "Self-serve | Sales-led | PLG | Hybrid | Unknown",
  "primary_cta": "string",
  "conversion_path": ["string"],
  "acquisition_channels": {
    "seo_signals": ["string"],
    "content_marketing": "boolean",
    "paid_ads_signals": ["string"],
    "partnerships": ["string"],
    "integrations_as_channel": "boolean"
  },
  "pricing_transparency": "Transparent | Partial | Hidden",
  "enterprise_ready": {
    "security_page": "boolean",
    "compliance_certifications": ["string"],
    "sla_mentioned": "boolean",
    "dedicated_enterprise_page": "boolean"
  },
  "expansion_signals": {
    "multi_product": "boolean",
    "upsell_paths": ["string"],
    "usage_based_component": "boolean"
  }
}
```
