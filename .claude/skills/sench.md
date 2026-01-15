# /sench - Competitive Intelligence

Analyze any company from their website using web scraping and AI analysis.

## Usage

```
/sench <domain>
/sench <domain> --module <module_name>
/sench <domain> --all
```

## Examples

```
/sench stripe.com
/sench notion.com --module gtm
/sench linear.app --all
```

## How it works

1. **Scrape** the target website using Playwright (landing page, about, pricing, etc.)
2. **Analyze** the scraped content using the available modules
3. **Output** structured competitive intelligence

## Available Modules

| Module | Description |
|--------|-------------|
| `identity` | Company basics: name, tagline, industry, founded year, HQ, team size, social links |
| `funding` | Funding rounds, investors, valuation, total raised |
| `founders` | Founders and leadership team, backgrounds, LinkedIn profiles |
| `finance` | Financial signals: revenue estimates, growth indicators, burn rate signals |
| `icp` | Ideal Customer Profile: target segments, company size, industries, use cases |
| `product` | Product breakdown: features, pricing tiers, integrations, tech stack |
| `market` | Market positioning: value proposition, differentiators, target market |
| `competitors` | Competitive landscape: direct/indirect competitors, positioning |
| `gtm` | Go-to-market: sales model, acquisition channels, pricing strategy |
| `marketing` | Marketing strategy: content, social presence, SEO, ads |
| `news` | Recent news: press releases, announcements, media coverage |
| `legal` | Legal context: compliance, certifications, terms, privacy |

## Scraping Instructions

Use Playwright to scrape these pages (when available):

```python
pages_to_scrape = [
    "/",
    "/about",
    "/about-us",
    "/pricing",
    "/product",
    "/features",
    "/customers",
    "/case-studies",
    "/security",
    "/blog",
    "/careers",
    "/jobs",
    "/contact",
    "/privacy",
    "/terms",
]
```

For each page, extract:
- Page title
- Meta description
- Main text content
- Headings (h1, h2, h3)
- Links (internal and external)
- Images with alt text

## Analysis Prompts

### identity

Extract company identity information:
- Company name
- Tagline/slogan
- Industry/sector
- Founded year
- Headquarters location
- Team size (if mentioned)
- Social links (LinkedIn, Twitter, GitHub, etc.)

### funding

Analyze funding information:
- Funding rounds (seed, series A, B, C, etc.)
- Investors (VCs, angels)
- Total amount raised
- Latest valuation (if available)
- Funding timeline

### founders

Extract founder and leadership information:
- Founder names and roles
- Co-founders
- C-level executives
- Board members
- Professional backgrounds
- LinkedIn profiles

### finance

Identify financial signals:
- Revenue indicators (ARR, MRR mentions)
- Growth metrics
- Customer count
- Employee growth
- Profitability signals

### icp

Determine Ideal Customer Profile:
- Target customer segments
- Company size (SMB, mid-market, enterprise)
- Industries served
- Geographic focus
- Use cases highlighted
- Customer testimonials analysis

### product

Break down the product:
- Core features
- Product tiers/plans
- Pricing structure
- Integrations
- API availability
- Tech stack (if visible)
- Mobile/desktop availability

### market

Analyze market positioning:
- Value proposition
- Key differentiators
- Target market
- Problem being solved
- Unique selling points

### competitors

Map competitive landscape:
- Direct competitors mentioned
- Indirect competitors
- Comparison pages
- Competitive advantages claimed
- Market category

### gtm

Analyze go-to-market strategy:
- Sales model (self-serve, sales-led, PLG)
- Acquisition channels
- Pricing transparency
- Free trial/freemium
- Demo availability
- Partner program

### marketing

Evaluate marketing strategy:
- Content marketing (blog frequency, topics)
- Social media presence
- SEO indicators
- Paid advertising signals
- Email marketing
- Community building

### news

Gather recent news:
- Press releases
- Product announcements
- Partnerships
- Awards/recognition
- Media coverage
- Blog announcements

### legal

Review legal context:
- Compliance certifications (SOC2, GDPR, HIPAA)
- Security practices
- Terms of service highlights
- Privacy policy highlights
- Data handling

## Output Format

Return analysis as structured markdown:

```markdown
# Company Analysis: [Company Name]

## Summary
Brief overview of the company based on analysis.

## [Module Name]
Detailed findings for each analyzed module.

### Key Findings
- Finding 1
- Finding 2

### Data Points
| Metric | Value |
|--------|-------|
| ... | ... |

## Sources
- [Page Title](url) - what was extracted
```

## Notes

- If a page returns 404 or is inaccessible, skip it
- Respect rate limits and add delays between requests
- Focus on publicly available information only
- Confidence levels: High (explicit data), Medium (inferred), Low (estimated)
