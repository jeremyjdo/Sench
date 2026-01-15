"""Sench CLI - Entry point for sub-agent."""

import argparse
import asyncio
import sys
from pathlib import Path

from sench import __version__
from sench.core.scraper import Scraper
from sench.modules import (
    DEFAULT_MODULE_ORDER,
    MODULE_FLAGS,
    MODULE_INFO,
    ModuleKey,
    get_prompt,
    get_system_prompt,
)


def parse_modules(args: argparse.Namespace) -> list[ModuleKey]:
    """Parse which modules to run from args."""
    modules = []

    if args.identity:
        modules.append(ModuleKey.IDENTITY)
    if args.funding:
        modules.append(ModuleKey.FUNDING)
    if args.founders:
        modules.append(ModuleKey.FOUNDERS)
    if args.finance:
        modules.append(ModuleKey.FINANCE)
    if args.icp:
        modules.append(ModuleKey.ICP)
    if args.product:
        modules.append(ModuleKey.PRODUCT_BREAKDOWN)
    if args.market:
        modules.append(ModuleKey.MARKET_VALUE_PROP)
    if args.competitors:
        modules.append(ModuleKey.COMPETITORS)
    if args.gtm:
        modules.append(ModuleKey.GTM)
    if args.marketing:
        modules.append(ModuleKey.MARKETING)
    if args.news:
        modules.append(ModuleKey.NEWS)
    if args.legal:
        modules.append(ModuleKey.LEGAL)

    # If no modules specified, use all
    if not modules:
        modules = DEFAULT_MODULE_ORDER

    return modules


async def run_sench(domain: str, modules: list[ModuleKey], screenshot: bool = True) -> str:
    """Run Sench analysis.

    Args:
        domain: Domain to analyze
        modules: List of modules to run
        screenshot: Whether to take screenshot

    Returns:
        Formatted output with scraped content and prompts
    """
    # Scrape the site
    scraper = Scraper()
    result = await scraper.scrape(domain, take_screenshot=screenshot)

    # Build output
    output_parts = []

    # Header
    output_parts.append(f"# Sench Analysis: {domain}\n")

    # Screenshot info
    if result.screenshot_path:
        output_parts.append(f"Screenshot saved: {result.screenshot_path}\n")

    # Social links
    social = result.social_links
    social_items = []
    if social.linkedin:
        social_items.append(f"LinkedIn: {social.linkedin}")
    if social.twitter:
        social_items.append(f"Twitter: {social.twitter}")
    if social.github:
        social_items.append(f"GitHub: {social.github}")

    if social_items:
        output_parts.append("## Social Links")
        output_parts.append("\n".join(f"- {item}" for item in social_items))
        output_parts.append("")

    # Pages scraped
    output_parts.append(f"## Pages Scraped: {len(result.pages)}")
    for page in result.pages:
        output_parts.append(f"- {page.url}: {page.title}")
    output_parts.append("")

    # System prompt
    output_parts.append("## System Prompt")
    output_parts.append("```")
    output_parts.append(get_system_prompt())
    output_parts.append("```\n")

    # Module prompts
    output_parts.append("## Analysis Prompts\n")
    output_parts.append("Analyze the following website content for each requested module.\n")

    # Website content
    output_parts.append("### Scraped Content\n")
    output_parts.append("<website_content>")
    # Truncate if too long
    content = result.content_markdown
    if len(content) > 50000:
        content = content[:50000] + "\n\n[Content truncated...]"
    output_parts.append(content)
    output_parts.append("</website_content>\n")

    # Module-specific prompts
    for module_key in modules:
        info = MODULE_INFO[module_key]
        output_parts.append(f"### {info['name']} Analysis")
        output_parts.append(f"*{info['description']}*\n")

        prompt = get_prompt(module_key, "[See website_content above]", domain)
        # Remove the scraped_content part since it's above
        prompt = prompt.replace(
            "```\n[See website_content above]\n```",
            "[See scraped content above]"
        ).replace(
            "```\n{scraped_content}\n```",
            "[See scraped content above]"
        )
        output_parts.append(prompt)
        output_parts.append("")

    return "\n".join(output_parts)


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        prog="sench",
        description="Competitive intelligence sub-agent for Claude Code, Codex & Cursor",
    )
    parser.add_argument(
        "domain",
        nargs="?",
        help="Domain to analyze (e.g., stripe.com)",
    )
    parser.add_argument(
        "--version", "-v",
        action="store_true",
        help="Show version",
    )
    parser.add_argument(
        "--no-screenshot",
        action="store_true",
        help="Skip screenshot capture",
    )

    # Module flags
    parser.add_argument("--identity", action="store_true", help="Company identity")
    parser.add_argument("--funding", action="store_true", help="Funding history")
    parser.add_argument("--founders", action="store_true", help="Founders & team")
    parser.add_argument("--finance", action="store_true", help="Financial signals")
    parser.add_argument("--icp", action="store_true", help="Ideal customer profile")
    parser.add_argument("--product", action="store_true", help="Product breakdown")
    parser.add_argument("--market", action="store_true", help="Market & value prop")
    parser.add_argument("--competitors", action="store_true", help="Competitors")
    parser.add_argument("--gtm", action="store_true", help="Go-to-market")
    parser.add_argument("--marketing", action="store_true", help="Marketing")
    parser.add_argument("--news", action="store_true", help="Recent news")
    parser.add_argument("--legal", action="store_true", help="Legal context")

    args = parser.parse_args()

    if args.version:
        print(f"sench {__version__}")
        return

    if not args.domain:
        parser.print_help()
        return

    # Parse modules
    modules = parse_modules(args)

    # Run analysis
    try:
        output = asyncio.run(run_sench(
            args.domain,
            modules,
            screenshot=not args.no_screenshot,
        ))
        print(output)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
