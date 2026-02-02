---
name: sench-valuechain
description: Value chain decomposition and analysis. Map end-to-end market activities, identify where value flows, and surface hidden opportunity areas through a structural lens.
---

# /sench-valuechain - Value Chain Analysis

Systematic decomposition of market activities to identify where value is created, captured, or lost.

## Usage

```
/sench-valuechain {market/industry}           # Default (English)
/sench-valuechain {market/industry} --fr      # French output
/sench-valuechain {market/industry} --en      # English output (explicit)
```

## Objective

Decompose the market into its full activity chain to systematically identify:
- Where value is created, captured, or lost
- Opportunity areas not visible through customer-centric analysis alone
- Structural inefficiencies and friction points

## Workflow

```
Input (market/industry) + optional --fr/--en
    ↓
1. End-to-End Chain Mapping
    ↓
2. Actor Identification per Step
    ↓
3. Dynamics & Trends Analysis
    ↓
4. Friction & Opportunity Detection
    ↓
5. Report → {market}_valuechain.md
```

## Rules

1. **Map full chain first** - complete picture before zooming in
2. **Include all directions** - upstream, core, and downstream activities
3. **Capture handovers** - transitions between steps are often friction sources
4. **Separate facts from assumptions** - clearly label uncertain information
5. **Single output file** - `{market}_valuechain.md`
6. **Sources required** - include URLs for all data

---

## Phase 1: End-to-End Chain Mapping

### Guiding Questions

- What are all the steps from raw input to final delivery?
- Which activities happen before, during, and after the core product/service?
- What supporting activities enable the primary chain?
- Where does the chain start and where does it end for different actors?

### Search Queries

```
# Chain Structure
"{market}" value chain analysis
"{market}" supply chain structure
"{market}" industry workflow
"{market}" process flow

# Actor Discovery
"{market}" key players by segment
"{market}" suppliers distributors
"{market}" intermediaries
"{market}" B2B ecosystem

# Economics
"{market}" margin structure
"{market}" cost breakdown
"{market}" pricing analysis
"{market}" revenue distribution
```

---

## Phase 2: Actor Identification

### For Each Step, Identify:

| Aspect | Questions |
|--------|-----------|
| **Players** | Who operates at this step? Incumbents, challengers, startups? |
| **Concentration** | Is this step fragmented or consolidated? |
| **Margins** | What percentage of total value is captured here? |
| **Barriers** | What prevents entry at this step? |
| **Dependencies** | What upstream/downstream relationships exist? |

### Actor Categories

```
┌─────────────────────────────────────────────────────────────┐
│                    ACTOR MAPPING                              │
├─────────────┬─────────────┬─────────────┬─────────────────────┤
│ Incumbents  │ Challengers │ Startups    │ Adjacent Entrants   │
├─────────────┼─────────────┼─────────────┼─────────────────────┤
│ Market      │ Growing     │ Funded      │ Companies from      │
│ leaders     │ share       │ innovators  │ related markets     │
│ >10% share  │ 2-10%       │ <2%         │ expanding here      │
└─────────────┴─────────────┴─────────────┴─────────────────────┘
```

---

## Phase 3: Dynamics & Trends Analysis

### Per Step Analysis

| Dimension | What to Capture |
|-----------|-----------------|
| **Trends** | What forces are reshaping this step? |
| **Technology** | What tech is enabling/disrupting here? |
| **Regulation** | What rules affect this step? |
| **Behavior** | How are actors/customers changing? |
| **Investment** | Where is capital flowing? |

### Trend Categories

- **Structural shifts** - fundamental changes in how step operates
- **Technology enablers** - new capabilities changing economics
- **Regulatory drivers** - rules creating or removing opportunities
- **Behavioral changes** - evolving expectations and practices

---

## Phase 4: Friction & Opportunity Detection

### Friction Types

| Type | Description | Example |
|------|-------------|---------|
| **Handover friction** | Problems at transitions between steps | Manual data re-entry |
| **Information asymmetry** | Unequal access to data | Opaque pricing |
| **Coordination failure** | Misaligned incentives | Channel conflicts |
| **Capacity mismatch** | Supply/demand imbalance | Seasonal bottlenecks |
| **Quality variance** | Inconsistent outputs | Unreliable service levels |

### Opportunity Signals

- Steps with high margins but low digitization
- Fragmented steps with many small players
- Steps frequently bypassed or disintermediated
- Steps with high customer complaint rates
- Steps where incumbents underinvest
- Steps appearing unattractive today but strategic tomorrow

---

## Phase 5: Report

Output: `{market}_valuechain.md`

### Language Parameter

- Default or `--en`: English output
- `--fr`: French output (use French headers and content)

```markdown
# {Market} - Value Chain Analysis

*{date}*

---

## Executive Summary

{3-4 sentences: chain overview, key findings, primary opportunity areas identified}

---

## Value Chain Overview

### Visual Map

```
{ASCII representation of full chain}

Example:
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│ Step 1   │───▶│ Step 2   │───▶│ Step 3   │───▶│ Step 4   │───▶│ Step 5   │
│ {name}   │    │ {name}   │    │ {name}   │    │ {name}   │    │ {name}   │
└──────────┘    └──────────┘    └──────────┘    └──────────┘    └──────────┘
    │               │               │               │               │
   {X%}           {X%}            {X%}            {X%}            {X%}
  margin          margin          margin          margin          margin
```

### Chain Summary

| Step | Primary Actors | Margin Share | Digitization | Concentration |
|------|----------------|--------------|--------------|---------------|
| {Step 1} | {actors} | {X%} | {Low/Med/High} | {Fragmented/Concentrated} |
| {Step 2} | {actors} | {X%} | {Low/Med/High} | {Fragmented/Concentrated} |

---

## Step-by-Step Analysis

### {Step 1 Name}

**Definition:** {what happens at this step}

| Aspect | Detail |
|--------|--------|
| **Key Players** | {list of companies} |
| **Market Structure** | {fragmented/consolidated, # of players} |
| **Margin Capture** | {X% of total value} |
| **Digitization Level** | {Low/Medium/High} |
| **Entry Barriers** | {capital, regulation, relationships} |

**Trends Shaping This Step:**
- {trend 1} - {impact}
- {trend 2} - {impact}

**Frictions Observed:**
- {friction 1}
- {friction 2}

**Opportunity Signals:**
- {signal 1}
- {signal 2}

{Repeat for each step}

---

## Upstream Dependencies

| Supplier Category | Key Players | Relationship Type | Risk Level |
|-------------------|-------------|-------------------|------------|
| {category 1} | {players} | {contractual/spot/integrated} | {Low/Med/High} |
| {category 2} | {players} | {contractual/spot/integrated} | {Low/Med/High} |

---

## Downstream Channels

| Channel | % of Volume | Key Players | Margin Captured |
|---------|-------------|-------------|-----------------|
| {channel 1} | {X%} | {players} | {X%} |
| {channel 2} | {X%} | {players} | {X%} |

---

## Cross-Chain Dynamics

### Value Flow Analysis

| From Step | To Step | Value Transferred | Friction Level |
|-----------|---------|-------------------|----------------|
| {step A} | {step B} | {description} | {Low/Med/High} |

### Integration Patterns

| Pattern | Players | Rationale |
|---------|---------|-----------|
| Vertical integration | {who} | {why} |
| Horizontal expansion | {who} | {why} |
| Platform plays | {who} | {why} |

---

## Opportunity Matrix

### By Step

| Step | Opportunity Type | Description | Attractiveness |
|------|------------------|-------------|----------------|
| {step} | {unbundling/bundling/digitization/disintermediation} | {description} | {High/Med/Low} |

### Underserved Areas

| Area | Why Underserved | Potential Solution | Size Estimate |
|------|-----------------|-------------------|---------------|
| {area 1} | {reason} | {solution type} | {€Xm} |
| {area 2} | {reason} | {solution type} | {€Xm} |

### Strategic Questions

1. Which step would yield disproportionate returns if improved?
2. Where are incumbents structurally unable to innovate?
3. What adjacent players could enter and reshape the chain?

---

## Assumptions & Limitations

### Explicit Assumptions

1. {Assumption 1}
2. {Assumption 2}

### Data Gaps

- {gap 1} - {impact on analysis}
- {gap 2} - {impact on analysis}

### Recommended Validation

| Topic | Expert Type | Questions |
|-------|-------------|-----------|
| {topic 1} | {operator/investor/regulator} | {questions to validate} |
| {topic 2} | {operator/investor/regulator} | {questions to validate} |

---

## Sources

- {Source 1}: {url}
- {Source 2}: {url}
- {Industry report}: {url}
- {Company disclosure}: {url}
```
