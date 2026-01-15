# Ideal Customer Profile Analysis

Determine the company's ideal customer profile based on all available signals.

## Content
```
{scraped_content}
```

## Context
Domain: {domain}

## Instructions

Infer the ICP:
1. **Company characteristics** - Size, industry, stage
2. **Buyer persona** - Title, department, pain points
3. **Use case fit** - Best-fit scenarios
4. **Anti-personas** - Who is NOT a fit
5. **Buying triggers** - What causes them to buy

## Output Schema

```json
{
  "target_company": {
    "size": ["1-10", "11-50", "51-200", "201-1000", "1000+"],
    "stage": ["Startup", "Growth", "Enterprise"],
    "industries": ["string"],
    "geography": ["string"]
  },
  "buyer_persona": {
    "titles": ["string"],
    "departments": ["string"],
    "seniority": "IC | Manager | Director | VP | C-level",
    "pain_points": ["string"]
  },
  "use_case_fit": ["string"],
  "anti_personas": ["string"],
  "buying_triggers": ["string"],
  "confidence_level": "High | Medium | Low"
}
```
