"""Page scraper using Playwright."""

import asyncio
from dataclasses import dataclass, field

from playwright.async_api import Page, async_playwright


@dataclass
class PageContent:
    """Scraped page content."""

    url: str
    title: str
    meta_description: str | None
    main_content: str
    links: list[dict[str, str]] = field(default_factory=list)
    headings: list[dict[str, str]] = field(default_factory=list)
    images_alt: list[str] = field(default_factory=list)


class PageScraper:
    """Extract content from web pages using Playwright."""

    PAGES_TO_SCRAPE = [
        "",  # Homepage
        "/about",
        "/pricing",
        "/product",
        "/products",
        "/features",
        "/customers",
        "/security",
        "/blog",
        "/careers",
        "/jobs",
        "/contact",
        "/legal/privacy",
        "/privacy",
        "/legal/terms",
        "/terms",
    ]

    def __init__(self, max_pages: int = 15, timeout: int = 15000):
        """Initialize the scraper.

        Args:
            max_pages: Maximum number of pages to scrape
            timeout: Request timeout in milliseconds
        """
        self.max_pages = max_pages
        self.timeout = timeout

    async def scrape_site(self, base_url: str) -> list[PageContent]:
        """Scrape multiple pages from a site.

        Args:
            base_url: The base URL of the site to scrape

        Returns:
            List of PageContent objects for successfully scraped pages
        """
        results: list[PageContent] = []
        visited: set[str] = set()

        # Normalize URL
        if not base_url.startswith("http"):
            base_url = f"https://{base_url}"
        base_url = base_url.rstrip("/")

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Sench/1.0"
            )

            for path in self.PAGES_TO_SCRAPE[: self.max_pages]:
                url = f"{base_url}{path}"
                if url in visited:
                    continue
                visited.add(url)

                try:
                    page = await context.new_page()
                    response = await page.goto(
                        url, wait_until="networkidle", timeout=self.timeout
                    )

                    if response and response.status == 200:
                        content = await self._extract_content(page, url)
                        results.append(content)

                    await page.close()
                except Exception:
                    # Skip pages that fail to load
                    pass

            await browser.close()

        return results

    async def _extract_content(self, page: Page, url: str) -> PageContent:
        """Extract structured content from a page."""
        title = await page.title()

        meta_description = await page.evaluate(
            """
            () => {
                const meta = document.querySelector('meta[name="description"]');
                return meta ? meta.getAttribute('content') : null;
            }
        """
        )

        # Extract main content (remove nav, footer, scripts)
        main_content = await page.evaluate(
            """
            () => {
                // Clone the document to avoid modifying the original
                const clone = document.body.cloneNode(true);

                // Remove unwanted elements
                const unwanted = clone.querySelectorAll(
                    'nav, footer, script, style, noscript, iframe, header'
                );
                unwanted.forEach(el => el.remove());

                // Get text content
                const main = clone.querySelector('main') || clone;
                return main.innerText.trim().substring(0, 50000);
            }
        """
        )

        # Extract links
        links = await page.evaluate(
            """
            () => {
                return Array.from(document.querySelectorAll('a[href]'))
                    .slice(0, 100)
                    .map(a => ({
                        text: a.innerText.trim().substring(0, 100),
                        href: a.getAttribute('href')
                    }))
                    .filter(l => l.text && l.href);
            }
        """
        )

        # Extract headings
        headings = await page.evaluate(
            """
            () => {
                return Array.from(document.querySelectorAll('h1, h2, h3'))
                    .map(h => ({
                        level: h.tagName,
                        text: h.innerText.trim().substring(0, 200)
                    }));
            }
        """
        )

        # Extract image alt texts
        images_alt = await page.evaluate(
            """
            () => {
                return Array.from(document.querySelectorAll('img[alt]'))
                    .map(img => img.getAttribute('alt'))
                    .filter(alt => alt && alt.length > 2);
            }
        """
        )

        return PageContent(
            url=url,
            title=title,
            meta_description=meta_description,
            main_content=main_content,
            links=links,
            headings=headings,
            images_alt=images_alt,
        )

    def to_markdown(self, pages: list[PageContent]) -> str:
        """Convert scraped content to markdown for LLM consumption.

        Args:
            pages: List of PageContent objects

        Returns:
            Markdown string with all page content
        """
        sections = []

        for page in pages:
            headings_md = "\n".join(
                f"- [{h['level']}] {h['text']}" for h in page.headings[:20]
            )
            links_md = "\n".join(
                f"- {link['text']}: {link['href']}" for link in page.links[:30]
            )

            section = f"""
## Page: {page.url}
**Title:** {page.title}
**Meta Description:** {page.meta_description or 'N/A'}

### Headings
{headings_md}

### Content
{page.main_content[:10000]}

### Links
{links_md}
"""
            sections.append(section)

        return "\n---\n".join(sections)


async def main() -> None:
    """Test the scraper."""
    scraper = PageScraper(max_pages=3)
    pages = await scraper.scrape_site("stripe.com")
    print(f"Scraped {len(pages)} pages")
    for page in pages:
        print(f"  - {page.url}: {page.title}")


if __name__ == "__main__":
    asyncio.run(main())
