# Funding Analysis

Analyze the following content to extract funding information.

## Content
```
{scraped_content}
```

## Company Context
Domain: {domain}

## Instructions

Search for and extract:
1. **Total funding raised** - Sum of all rounds
2. **Funding rounds** - Each round with date, amount, type, investors
3. **Key investors** - Notable VCs, angels, strategics
4. **Last round details** - Most recent funding event
5. **Valuation** - If disclosed or estimated

If no funding information is found, indicate this clearly.

## Output Schema

```json
{
  "total_raised_usd": "number | null",
  "funding_stage": "Pre-Seed | Seed | Series A | Series B | Series C+ | Bootstrapped | Unknown",
  "last_round": {
    "date": "YYYY-MM-DD | null",
    "amount_usd": "number | null",
    "round_type": "string | null",
    "lead_investor": "string | null"
  },
  "funding_rounds": [
    {
      "date": "YYYY-MM-DD",
      "amount_usd": "number",
      "round_type": "string",
      "investors": ["string"]
    }
  ],
  "notable_investors": ["string"],
  "estimated_valuation": "string | null",
  "funding_sources_found": ["string"]
}
```
