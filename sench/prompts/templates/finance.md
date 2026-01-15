# Financial Signals Analysis

Analyze financial signals and estimates (with appropriate caveats).

## Content
```
{scraped_content}
```

## Context
Domain: {domain}

## Instructions

IMPORTANT: Financial estimates are inherently uncertain. Flag all inferences clearly.

Analyze:
1. **Revenue signals** - Pricing * users estimates
2. **Growth signals** - Hiring, expansion
3. **Burn rate indicators** - Team size, funding
4. **Business model health** - Unit economics signals
5. **Runway estimates** - If funding and team known

## Output Schema

```json
{
  "revenue_signals": {
    "model": "string",
    "signals": ["string"],
    "estimate_range": "string | null",
    "confidence": "Low | Very Low"
  },
  "growth_signals": {
    "hiring_activity": "Active | Moderate | Low | Unknown",
    "expansion_signals": ["string"],
    "growth_trajectory": "string | null"
  },
  "cost_signals": {
    "team_size_estimate": "string | null",
    "infrastructure_signals": ["string"],
    "burn_rate_estimate": "string | null"
  },
  "business_health_indicators": ["string"],
  "caveats": ["string"]
}
```
