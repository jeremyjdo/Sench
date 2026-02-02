# Sench

Competitive intelligence skills for AI agents (Claude Code, Codex, Cursor).

## Skills

### /sench-startup

Full competitive intelligence report on any startup.

```bash
npx skills add https://github.com/jeremyjdo/Sench --skill sench-startup
```

```
/sench-startup ornikar
/sench-startup ornikar --fr
/sench-startup 443061841
/sench-startup qonto.com
```

**Output:** `{company}_analysis.md` with funding, team, product (ICP, pricing), reviews, market, competitors, hiring, SWOT.

### /sench-team

Team structure and founder background analysis.

```bash
npx skills add https://github.com/jeremyjdo/Sench --skill sench-team
```

```
/sench-team 1point6
/sench-team 1point6 --fr
/sench-team pennylane
```

**Output:** `{company}_team.md` with employee list by department, founder deep dives, hiring signals.

### /sench-market

Market definition & opportunity mapping for venture design.

```bash
npx skills add https://github.com/jeremyjdo/Sench --skill sench-market
```

```
/sench-market pet insurance
/sench-market vertical farming
/sench-market regulatory reporting --fr
```

**Output:** `{market}_opportunity_map.md` with value chain, opportunity grid, segments, adjacent markets, competitive landscape, international benchmarks.

## Language

Default output is English. Add `--fr` for French output.

## Features

- Works inside Claude Code, Codex, Cursor, Mistral CLI
- No external tools or API keys required
- French company data via API gouv.fr
- Single markdown report output
- Detailed ICP and market segment analysis
- Sources included with URLs

## Examples

See [examples/](examples/) for sample outputs:
- [ornikar_analysis.md](examples/ornikar_analysis.md)
- [1point6_team.md](examples/1point6_team.md)
- [regulatory_reporting_opportunity_map.md](examples/regulatory_reporting_opportunity_map.md)

## License

MIT
