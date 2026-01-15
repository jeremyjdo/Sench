"""Base module definitions for Sench sub-agent."""

from enum import Enum

from sench.prompts import load_template


class ModuleKey(str, Enum):
    """Available analysis modules."""

    IDENTITY = "identity"
    FUNDING = "funding"
    FOUNDERS = "founders"
    FINANCE = "finance"
    ICP = "icp"
    PRODUCT_BREAKDOWN = "product_breakdown"
    MARKET_VALUE_PROP = "market_value_prop"
    COMPETITORS = "competitors"
    GTM = "gtm"
    MARKETING = "marketing"
    NEWS = "news"
    LEGAL = "legal"


# Mapping of short flags to module keys
MODULE_FLAGS: dict[str, ModuleKey] = {
    "identity": ModuleKey.IDENTITY,
    "funding": ModuleKey.FUNDING,
    "founders": ModuleKey.FOUNDERS,
    "finance": ModuleKey.FINANCE,
    "icp": ModuleKey.ICP,
    "product": ModuleKey.PRODUCT_BREAKDOWN,
    "market": ModuleKey.MARKET_VALUE_PROP,
    "competitors": ModuleKey.COMPETITORS,
    "gtm": ModuleKey.GTM,
    "marketing": ModuleKey.MARKETING,
    "news": ModuleKey.NEWS,
    "legal": ModuleKey.LEGAL,
}


# Module metadata
MODULE_INFO: dict[ModuleKey, dict[str, str]] = {
    ModuleKey.IDENTITY: {
        "name": "Identity",
        "description": "Company basics, tagline, industry, social links",
    },
    ModuleKey.FUNDING: {
        "name": "Funding",
        "description": "Funding rounds, investors, valuation",
    },
    ModuleKey.FOUNDERS: {
        "name": "Founders",
        "description": "Founders, executives, team signals",
    },
    ModuleKey.FINANCE: {
        "name": "Finance",
        "description": "Financial signals and estimates",
    },
    ModuleKey.ICP: {
        "name": "ICP",
        "description": "Ideal customer profile",
    },
    ModuleKey.PRODUCT_BREAKDOWN: {
        "name": "Product",
        "description": "Products, features, pricing",
    },
    ModuleKey.MARKET_VALUE_PROP: {
        "name": "Market",
        "description": "Value proposition, positioning",
    },
    ModuleKey.COMPETITORS: {
        "name": "Competitors",
        "description": "Competitive landscape",
    },
    ModuleKey.GTM: {
        "name": "GTM",
        "description": "Go-to-market strategy",
    },
    ModuleKey.MARKETING: {
        "name": "Marketing",
        "description": "Content, social, SEO",
    },
    ModuleKey.NEWS: {
        "name": "News",
        "description": "Recent news and updates",
    },
    ModuleKey.LEGAL: {
        "name": "Legal",
        "description": "Compliance, privacy, terms",
    },
}


# Default execution order
DEFAULT_MODULE_ORDER: list[ModuleKey] = [
    ModuleKey.IDENTITY,
    ModuleKey.PRODUCT_BREAKDOWN,
    ModuleKey.MARKET_VALUE_PROP,
    ModuleKey.COMPETITORS,
    ModuleKey.GTM,
    ModuleKey.ICP,
    ModuleKey.FUNDING,
    ModuleKey.FOUNDERS,
    ModuleKey.MARKETING,
    ModuleKey.NEWS,
    ModuleKey.FINANCE,
    ModuleKey.LEGAL,
]


def get_prompt(module_key: ModuleKey, scraped_content: str, domain: str) -> str:
    """Get the analysis prompt for a module.

    Args:
        module_key: The module to get prompt for
        scraped_content: Scraped website content in markdown
        domain: The domain being analyzed

    Returns:
        Formatted prompt string for the AI to analyze
    """
    template = load_template(module_key.value)

    # Replace placeholders
    prompt = template.replace("{scraped_content}", scraped_content)
    prompt = prompt.replace("{domain}", domain)

    return prompt


def get_system_prompt() -> str:
    """Get the system prompt for analysis."""
    return """You are Sench, an expert competitive intelligence analyst. Analyze companies based on their website content.

## Guidelines
1. **Accuracy**: Only report facts from the provided content
2. **Confidence**: Use "appears to", "suggests that" for uncertain info
3. **Structure**: Follow the exact output schema
4. **Completeness**: State "Not found" if info unavailable

## Output
Return valid JSON matching the requested schema. No markdown code blocks."""
