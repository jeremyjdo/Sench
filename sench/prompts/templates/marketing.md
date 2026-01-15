# Marketing Analysis

Analyze the company's marketing approach and content strategy.

## Content
```
{scraped_content}
```

## Domain: {domain}

## Instructions

Analyze:
1. **Content strategy** - Blog, resources, guides
2. **Social presence** - Active channels
3. **Brand voice** - Tone and messaging style
4. **SEO signals** - Target keywords, structure
5. **Lead magnets** - Gated content, tools
6. **Community** - Discord, Slack, forums

## Output Schema

```json
{
  "content_strategy": {
    "has_blog": "boolean",
    "blog_frequency": "string | null",
    "content_types": ["Blog", "Podcast", "Video", "Webinar", "Ebook", "Newsletter"],
    "topics": ["string"]
  },
  "social_presence": {
    "primary_channel": "string | null",
    "channels": [
      {
        "platform": "string",
        "url": "string",
        "follower_signals": "string | null"
      }
    ]
  },
  "brand_voice": "Professional | Casual | Technical | Playful | Unknown",
  "seo_signals": {
    "target_keywords": ["string"],
    "meta_description": "string | null"
  },
  "lead_magnets": ["string"],
  "community": {
    "has_community": "boolean",
    "platforms": ["string"]
  },
  "newsletter": "boolean"
}
```
