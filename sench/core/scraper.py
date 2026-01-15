"""Main scraper for Sench sub-agent."""

import asyncio
from dataclasses import dataclass
from pathlib import Path

from sench.tools.page_scraper import PageContent, PageScraper
from sench.tools.screenshot import ScreenshotTool
from sench.tools.social_scraper import SocialLinks, SocialScraper


@dataclass
class ScrapeResult:
    """Result from scraping a website."""

    domain: str
    content_markdown: str
    pages: list[PageContent]
    social_links: SocialLinks
    screenshot_path: Path | None = None


class Scraper:
    """Main scraper that combines all tools."""

    def __init__(
        self,
        max_pages: int = 15,
        timeout: int = 15000,
        screenshot_dir: Path | None = None,
    ):
        """Initialize the scraper.

        Args:
            max_pages: Maximum pages to scrape
            timeout: Request timeout in ms
            screenshot_dir: Directory for screenshots
        """
        self.page_scraper = PageScraper(max_pages=max_pages, timeout=timeout)
        self.social_scraper = SocialScraper()
        self.screenshot_tool = ScreenshotTool(screenshot_dir)

    async def scrape(
        self,
        domain: str,
        take_screenshot: bool = True,
    ) -> ScrapeResult:
        """Scrape a website and return structured content.

        Args:
            domain: Domain to scrape (e.g., stripe.com)
            take_screenshot: Whether to capture a screenshot

        Returns:
            ScrapeResult with all scraped content
        """
        # Normalize domain
        if domain.startswith("http"):
            domain = domain.replace("https://", "").replace("http://", "")
        domain = domain.rstrip("/").split("/")[0]

        # Run scraping tasks
        pages = await self.page_scraper.scrape_site(domain)
        social_links = await self.social_scraper.extract_social_links(domain)

        # Screenshot
        screenshot_path = None
        if take_screenshot:
            try:
                screenshot_path = await self.screenshot_tool.capture(
                    domain, full_page=False
                )
            except Exception:
                pass  # Screenshot is optional

        # Convert to markdown
        content_markdown = self.page_scraper.to_markdown(pages)

        return ScrapeResult(
            domain=domain,
            content_markdown=content_markdown,
            pages=pages,
            social_links=social_links,
            screenshot_path=screenshot_path,
        )


def scrape_sync(domain: str, take_screenshot: bool = True) -> ScrapeResult:
    """Synchronous wrapper for scraping.

    Args:
        domain: Domain to scrape
        take_screenshot: Whether to capture screenshot

    Returns:
        ScrapeResult with all scraped content
    """
    scraper = Scraper()
    return asyncio.run(scraper.scrape(domain, take_screenshot))
