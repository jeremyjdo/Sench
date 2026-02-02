---
name: sench-competitive-landscape
description: Competitive landscape mapping with dual focus - direct market competition per segment and international benchmarks for inspiration. Identify value gaps and emerging patterns across geographies.
---

# /sench-competitive-landscape - Competitive Landscape Analysis

Comprehensive competitive mapping combining direct segment competition and international benchmarks.

## Usage

```
/sench-competitive-landscape {market/segment}           # Default (English)
/sench-competitive-landscape {market/segment} --fr      # French output
/sench-competitive-landscape {market/segment} --en      # English output (explicit)
```

## Dual Focus

This skill produces two complementary analyses:

### Focus 1: Direct Competition
- Market structure per segment (concentrated/fragmented)
- Key player profiles and positioning
- Competitive intensity mapping
- Value gaps identification

### Focus 2: International Benchmarks
- Advanced market patterns
- Inspirational players by geography
- Funding trajectory signals
- Transferable strategies

## Workflow

```
Input (market/segment) + optional --fr/--en
    ↓
1. Market Structure Analysis
    ↓
2. Direct Competitor Mapping
    ↓
3. International Screening
    ↓
4. Value Gap Synthesis
    ↓
5. Report → {segment}_landscape.md
```

## Rules

1. **Structure before players** - analyze market dynamics before individual profiles
2. **Go beyond features** - include financials, strategy, operating models
3. **Track momentum** - historical evolution reveals trajectories
4. **Facts vs interpretation** - clearly separate observations from analysis
5. **Single output file** - `{segment}_landscape.md`
6. **Sources required** - include URLs for all data

---

## Part 1: Direct Market Competition

### Guiding Questions

- Is the market fragmented, concentrated, or dominated by few players?
- Who are the key incumbents and challengers?
- Where is competition intense vs surprisingly low?
- Which value chain steps are poorly served?
- Which industries, company sizes, or geographies are underserved?
- Are players moving up or down the value chain?
- What does M&A activity reveal?
- Where do clear value gaps exist?

### Search Queries

```
# Market Structure
"{segment}" market share analysis
"{segment}" competitive landscape
"{segment}" market concentration
"{segment}" industry structure

# Player Discovery
"{segment}" leading companies
"{segment}" startups funded
site:crunchbase.com "{segment}"
site:dealroom.co "{segment}"

# Competitive Dynamics
"{segment}" pricing comparison
"{segment}" M&A activity 2024 2025
"{segment}" market consolidation
"{segment}" vertical integration

# Value Gaps
"{segment}" underserved segments
"{segment}" market gaps
"{segment}" unmet needs SMB
"{segment}" emerging players
```

### Market Structure Framework

```
┌─────────────────────────────────────────────────────────────────┐
│                    MARKET STRUCTURE                               │
├─────────────────┬─────────────────┬─────────────────────────────┤
│   Concentrated  │   Oligopoly     │      Fragmented             │
│   (>50% top 3)  │   (30-50%)      │      (<30% top 10)          │
├─────────────────┼─────────────────┼─────────────────────────────┤
│ High barriers   │ Moderate        │ Low barriers                │
│ Price power     │ Competition on  │ Commoditization risk        │
│ Hard to enter   │ differentiation │ Consolidation opportunity   │
└─────────────────┴─────────────────┴─────────────────────────────┘
```

### Competitor Profile Template

For each key player:

| Dimension | What to Capture |
|-----------|-----------------|
| **Positioning** | Target segment, value proposition, brand |
| **Product** | Core offering, features, tech stack |
| **GTM** | Sales model, channels, pricing |
| **Financials** | Revenue, funding, margins (if available) |
| **Trajectory** | Recent moves, M&A, hiring signals |
| **Strengths** | What they do well |
| **Weaknesses** | Where they underperform |

### Value Gap Identification

| Gap Type | Description | Example |
|----------|-------------|---------|
| **Segment gap** | Customer type poorly served | SMBs ignored by enterprise focus |
| **Geographic gap** | Region with weak players | Southern Europe underserved |
| **Feature gap** | Capability missing from market | No mobile-first solution |
| **Price gap** | No offering at certain price point | Nothing between free and enterprise |
| **Integration gap** | Poor connectivity with ecosystem | No ERP integration |

---

## Part 2: International Benchmarks

### Guiding Questions

- Which markets are more advanced for this segment?
- What types of players are emerging there?
- What product, GTM, or positioning patterns repeat?
- Are funding dynamics revealing structural trends?
- What problems are solved elsewhere but not locally?
- What moves could be adapted to local context?

### Search Queries

```
# Geographic Screening
"{segment}" USA startups
"{segment}" UK market leaders
"{segment}" Germany innovation
"{segment}" Asia trends

# Funding Signals
"{segment}" Series A B funding 2024 2025
"{segment}" unicorn
site:techcrunch.com "{segment}" raises

# Pattern Recognition
"{segment}" business model innovation
"{segment}" GTM strategy
"{segment}" product-led growth
"{segment}" vertical SaaS

# Advanced Markets
"{segment}" market maturity comparison
"{segment}" adoption rates by country
"{segment}" digital penetration
```

### Benchmark Framework

```
┌─────────────────────────────────────────────────────────────────┐
│               INTERNATIONAL BENCHMARK MATRIX                     │
├─────────────────┬─────────────────┬─────────────────────────────┤
│     Market      │   Maturity      │    Key Players              │
├─────────────────┼─────────────────┼─────────────────────────────┤
│ USA             │ Most advanced   │ {players}                   │
│ UK              │ Advanced        │ {players}                   │
│ Germany         │ Growing         │ {players}                   │
│ France          │ Emerging        │ {players}                   │
│ Asia            │ Different model │ {players}                   │
└─────────────────┴─────────────────┴─────────────────────────────┘
```

### Pattern Categories

| Pattern Type | What to Look For |
|--------------|------------------|
| **Product** | Feature sets, UX, tech differentiation |
| **GTM** | Sales motion, channel strategy, partnerships |
| **Pricing** | Models, tiers, value metric |
| **Positioning** | Messaging, target persona, brand |
| **Funding** | Round sizes, investor types, valuation signals |

---

## Phase 3: Report

Output: `{segment}_landscape.md`

### Language Parameter

- Default or `--en`: English output
- `--fr`: French output (use French headers and content)

```markdown
# {Segment} - Competitive Landscape

*{date}*

---

## Executive Summary

{4-5 sentences: market structure, competitive dynamics, key value gaps, international signals, entry implications}

---

# Part 1: Direct Market Competition

## Market Structure

### Overview

| Attribute | Detail |
|-----------|--------|
| **Structure Type** | {Concentrated/Oligopoly/Fragmented} |
| **Top 3 Share** | {X%} |
| **# of Significant Players** | {number} |
| **Consolidation Trend** | {Increasing/Stable/Decreasing} |
| **Barrier Level** | {High/Medium/Low} |

### Competitive Intensity by Sub-Segment

| Sub-Segment | Size | Intensity | Key Players | Value Gap |
|-------------|------|-----------|-------------|-----------|
| {segment 1} | {€Xm} | {High/Med/Low} | {players} | {gap or "Crowded"} |
| {segment 2} | {€Xm} | {High/Med/Low} | {players} | {gap or "Crowded"} |

---

## Key Players

### Tier 1: Market Leaders

#### {Player 1 Name}

| Dimension | Detail |
|-----------|--------|
| **Positioning** | {description} |
| **Target Segment** | {customer type} |
| **Revenue** | {€Xm or "Not disclosed"} |
| **Funding** | {total raised} |
| **Founded** | {year} |
| **HQ** | {location} |

**Product & GTM:**
- {product description}
- {sales model}
- {pricing approach}

**Recent Moves:**
- {move 1}
- {move 2}

**Strengths:** {2-3 points}

**Weaknesses:** {2-3 points}

{Repeat for key players}

### Tier 2: Challengers

| Player | Positioning | Funding | Differentiation |
|--------|-------------|---------|-----------------|
| {name} | {position} | {€Xm} | {what makes them different} |

### Tier 3: Emerging Players

| Player | Founded | Funding | Angle |
|--------|---------|---------|-------|
| {name} | {year} | {€Xm} | {approach} |

---

## Competitive Dynamics

### M&A Activity

| Date | Acquirer | Target | Deal Size | Strategic Signal |
|------|----------|--------|-----------|------------------|
| {date} | {company} | {company} | {€Xm} | {what it signals} |

### Vertical Moves

| Player | Direction | Move | Rationale |
|--------|-----------|------|-----------|
| {name} | Upstream/Downstream | {description} | {why} |

### Funding Trends

| Trend | Observation |
|-------|-------------|
| Total invested (last 12mo) | {€Xm} |
| Largest rounds | {list} |
| Investor focus areas | {themes} |

---

## Value Gap Analysis

### Gap Matrix

| Gap Type | Location | Size Estimate | Competition | Entry Opportunity |
|----------|----------|---------------|-------------|-------------------|
| {type} | {where} | {€Xm} | {Low/Med/High} | {assessment} |

### Deep Dive: Top Value Gaps

#### Gap 1: {Name}

**Description:** {what is underserved}

**Why it exists:**
- {reason 1}
- {reason 2}

**Demand signals:**
- {signal 1}
- {signal 2}

**Entry conditions:**
- {condition 1}
- {condition 2}

---

# Part 2: International Benchmarks

## Market Maturity Comparison

| Geography | Maturity | Market Size | Growth | Standout Players |
|-----------|----------|-------------|--------|------------------|
| USA | {Most advanced/Advanced/Emerging} | {$Xb} | {X%} | {players} |
| UK | {level} | {€Xb} | {X%} | {players} |
| Germany | {level} | {€Xb} | {X%} | {players} |
| France | {level} | {€Xb} | {X%} | {players} |
| Asia | {level} | {$Xb} | {X%} | {players} |

---

## Inspirational Players

### {Player 1 - Geography}

| Dimension | Detail |
|-----------|--------|
| **What they do** | {description} |
| **Why inspirational** | {what makes them stand out} |
| **Funding** | {amount, investors} |
| **Key metrics** | {growth, customers, etc.} |

**Transferable lessons:**
- {lesson 1}
- {lesson 2}

**Adaptation considerations:**
- {consideration 1}
- {consideration 2}

{Repeat for 3-5 inspirational players}

---

## Pattern Analysis

### Product Patterns

| Pattern | Where Observed | Implication |
|---------|----------------|-------------|
| {pattern 1} | {geographies/players} | {what it means} |
| {pattern 2} | {geographies/players} | {what it means} |

### GTM Patterns

| Pattern | Where Observed | Implication |
|---------|----------------|-------------|
| {pattern 1} | {geographies/players} | {what it means} |

### Pricing Patterns

| Model | Prevalence | Key Examples |
|-------|------------|--------------|
| {model 1} | {common/emerging/rare} | {players} |
| {model 2} | {common/emerging/rare} | {players} |

---

## Funding Signals

### Investment Thesis Themes

| Theme | Evidence | Signal Strength |
|-------|----------|-----------------|
| {theme 1} | {rounds, amounts} | {Strong/Moderate/Weak} |
| {theme 2} | {rounds, amounts} | {Strong/Moderate/Weak} |

### Notable Rounds (Last 18 Months)

| Company | Round | Amount | Investors | Signal |
|---------|-------|--------|-----------|--------|
| {name} | {type} | {€Xm} | {investors} | {what it indicates} |

---

# Synthesis

## Strategic Implications

### Where to Compete

| Option | Rationale | Risk Level |
|--------|-----------|------------|
| {option 1} | {why} | {High/Med/Low} |
| {option 2} | {why} | {High/Med/Low} |

### Differentiation Paths

| Path | Inspired By | Adaptation Needed |
|------|-------------|-------------------|
| {path 1} | {international example} | {what to change} |
| {path 2} | {international example} | {what to change} |

### Key Success Factors

1. {factor 1}
2. {factor 2}
3. {factor 3}

---

## Assumptions & Limitations

### Explicit Assumptions

1. {Assumption 1}
2. {Assumption 2}

### Data Gaps

- {gap 1}
- {gap 2}

### Recommended Validation

| Topic | Expert Type | Questions |
|-------|-------------|-----------|
| {topic} | {type} | {questions} |

---

## Sources

- {Source 1}: {url}
- {Source 2}: {url}
- {Crunchbase/PitchBook}: {url}
- {Industry report}: {url}
```
