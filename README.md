# Sench

Competitive intelligence sub-agent for **Claude Code**, **Codex** & **Cursor**.

Scrape and analyze any company website directly from your AI coding assistant.

## Install

```bash
curl -fsSL https://sench.ai/install | bash
```

Or manually:

```bash
pip install playwright
playwright install chromium
```

## Usage

Use as a sub-agent command in Claude Code, Codex, or Cursor:

```bash
# Full analysis
/sench stripe.com

# Specific modules
/sench stripe.com --gtm
/sench stripe.com --funding --founders

# Skip screenshot
/sench notion.com --no-screenshot
```

Or run directly:

```bash
python -m sench stripe.com
```

## Analysis Modules

| Module | Flag | Description |
|--------|------|-------------|
| Identity | `--identity` | Company basics, tagline, social links |
| Funding | `--funding` | Funding rounds, investors, valuation |
| Founders | `--founders` | Team, leadership, backgrounds |
| Product | `--product` | Products, features, pricing |
| Market | `--market` | Value proposition, positioning |
| Competitors | `--competitors` | Competitive landscape |
| GTM | `--gtm` | Go-to-market strategy |
| Marketing | `--marketing` | Content, social, SEO |
| ICP | `--icp` | Ideal customer profile |
| News | `--news` | Recent updates, press |
| Finance | `--finance` | Financial signals |
| Legal | `--legal` | Compliance, terms |

Run all modules by default, or select specific ones.

## How It Works

1. **Sench scrapes** the target website using Playwright
2. **Returns content + prompts** to the host AI (Claude Code/Codex/Cursor)
3. **Host AI analyzes** the content using its built-in LLM

No API keys required - the analysis is done by your coding assistant.

## Output

Sench returns:
- **Screenshot** of the landing page
- **Social links** (LinkedIn, Twitter, GitHub)
- **Scraped content** in markdown format
- **Analysis prompts** for each requested module

## Project Structure

```
sench/
├── sench/
│   ├── cli.py              # Entry point
│   ├── core/scraper.py     # Playwright scraper
│   ├── modules/base.py     # Module definitions
│   ├── prompts/templates/  # Prompt templates (.md)
│   └── tools/              # Page scraper, screenshot
├── landing/                # Website
├── install.sh              # Installer script
└── pyproject.toml
```

## Development

```bash
# Clone
git clone https://github.com/sench-ai/sench
cd sench

# Install
pip install -e .
playwright install chromium

# Run
python -m sench stripe.com --gtm

# Test
python -m sench --version
```

## License

MIT
