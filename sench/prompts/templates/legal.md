# Legal Context Analysis

Analyze legal and compliance information.

## Content
```
{scraped_content}
```

## Domain: {domain}

## Instructions

Extract:
1. **Legal entity** - Company type, jurisdiction
2. **Compliance** - Certifications, regulations
3. **Privacy** - GDPR, CCPA compliance
4. **Terms of service** - Key provisions
5. **Risk signals** - Lawsuits, regulatory issues

## Output Schema

```json
{
  "legal_entity": {
    "type": "string | null",
    "jurisdiction": "string | null",
    "registration_signals": ["string"]
  },
  "compliance": {
    "certifications": ["SOC 2", "ISO 27001", "HIPAA", "GDPR", "Other"],
    "industry_specific": ["string"]
  },
  "privacy": {
    "gdpr_compliant": "boolean | null",
    "ccpa_compliant": "boolean | null",
    "privacy_policy_url": "string | null",
    "data_processing_signals": ["string"]
  },
  "terms_highlights": ["string"],
  "risk_signals": ["string"],
  "legal_pages_found": ["string"]
}
```
