# /sench-valuechain

Value chain decomposition and analysis for venture design.

## What It Does

Maps the full end-to-end activity chain of a market to identify where value is created, captured, or lost. Surfaces opportunity areas that may not emerge through customer-centric analysis alone.

## Usage

```
/sench-valuechain carbon credits
/sench-valuechain luxury resale
/sench-valuechain clinical trials --fr
```

## Output

Single markdown file: `{market}_valuechain.md`

Includes:
- Visual chain mapping
- Step-by-step actor analysis
- Margin distribution
- Trends and dynamics per step
- Friction and handover points
- Opportunity matrix
- Upstream/downstream dependencies
- Integration patterns
- Strategic questions

## Key Questions Answered

- Who are all the actors involved at each step?
- What trends or dynamics are shaping each step today?
- Where is value created, captured, or lost?
- Where do frictions, delays, or inefficiencies occur?
- Which steps are structurally underserved or over-fragmented?
- What parts are typically ignored by incumbents?
- Are there steps that look unattractive today but could become strategic?

## Requirements

- WebSearch
- WebFetch

No API keys required.
