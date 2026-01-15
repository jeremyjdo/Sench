"""Social media link scraper."""

import re
from dataclasses import dataclass, field

from playwright.async_api import async_playwright


@dataclass
class SocialLinks:
    """Social media links found on a site."""

    linkedin: str | None = None
    twitter: str | None = None
    github: str | None = None
    youtube: str | None = None
    instagram: str | None = None
    facebook: str | None = None
    discord: str | None = None
    slack: str | None = None
    other: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, str | list[str] | None]:
        """Convert to dictionary."""
        return {
            "linkedin": self.linkedin,
            "twitter": self.twitter,
            "github": self.github,
            "youtube": self.youtube,
            "instagram": self.instagram,
            "facebook": self.facebook,
            "discord": self.discord,
            "slack": self.slack,
            "other": self.other,
        }


class SocialScraper:
    """Extract social media links from websites."""

    SOCIAL_PATTERNS: dict[str, str] = {
        "linkedin": r"linkedin\.com/(company|in)/[\w-]+",
        "twitter": r"(twitter|x)\.com/[\w-]+",
        "github": r"github\.com/[\w-]+",
        "youtube": r"youtube\.com/(c|channel|user)/[\w-]+",
        "instagram": r"instagram\.com/[\w-]+",
        "facebook": r"facebook\.com/[\w-]+",
        "discord": r"discord\.(gg|com/invite)/[\w-]+",
        "slack": r"[\w-]+\.slack\.com",
    }

    async def extract_social_links(self, url: str) -> SocialLinks:
        """Extract social media links from a website.

        Args:
            url: The website URL to extract links from

        Returns:
            SocialLinks object with found social media links
        """
        if not url.startswith("http"):
            url = f"https://{url}"

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()

            try:
                await page.goto(url, wait_until="networkidle", timeout=15000)

                # Get all links on the page
                links = await page.evaluate(
                    """
                    () => Array.from(document.querySelectorAll('a[href]'))
                        .map(a => a.href)
                        .filter(href => href)
                """
                )

                # Also check footer specifically
                footer_links = await page.evaluate(
                    """
                    () => {
                        const footer = document.querySelector('footer');
                        if (!footer) return [];
                        return Array.from(footer.querySelectorAll('a[href]'))
                            .map(a => a.href);
                    }
                """
                )

                all_links = list(set(links + footer_links))

            except Exception:
                all_links = []
            finally:
                await browser.close()

        return self._parse_social_links(all_links)

    def _parse_social_links(self, links: list[str]) -> SocialLinks:
        """Parse social links from a list of URLs.

        Args:
            links: List of URLs to parse

        Returns:
            SocialLinks object with categorized links
        """
        result = SocialLinks()

        for link in links:
            for platform, pattern in self.SOCIAL_PATTERNS.items():
                if re.search(pattern, link, re.IGNORECASE):
                    current = getattr(result, platform)
                    if current is None:
                        setattr(result, platform, link)
                    break

        return result


async def main() -> None:
    """Test the social scraper."""
    scraper = SocialScraper()
    links = await scraper.extract_social_links("stripe.com")
    print("Social links found:")
    for platform, url in links.to_dict().items():
        if url:
            print(f"  {platform}: {url}")


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
