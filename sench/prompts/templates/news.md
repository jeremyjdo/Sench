# News & Updates Analysis

Analyze recent news and updates about the company.

## Content
```
{scraped_content}
```

## Domain: {domain}

## Instructions

Extract:
1. **Recent news** - Press releases, announcements
2. **Product updates** - New features, launches
3. **Company milestones** - Achievements, awards
4. **Media coverage** - Press mentions
5. **Sentiment** - Overall tone of coverage

## Output Schema

```json
{
  "recent_news": [
    {
      "date": "YYYY-MM-DD | null",
      "title": "string",
      "summary": "string",
      "source": "string | null",
      "type": "Product Launch | Funding | Partnership | Award | Hiring | Other"
    }
  ],
  "press_coverage": ["string"],
  "awards_recognition": ["string"],
  "product_updates": ["string"],
  "overall_sentiment": "Positive | Neutral | Negative | Mixed",
  "news_recency": "Active (< 3 months) | Moderate (3-12 months) | Stale (> 12 months) | No news found"
}
```
