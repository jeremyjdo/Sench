"""Screenshot capture using Playwright."""

import asyncio
from datetime import datetime
from pathlib import Path

from playwright.async_api import async_playwright


class ScreenshotTool:
    """Capture screenshots of web pages."""

    def __init__(self, output_dir: Path | None = None):
        """Initialize the screenshot tool.

        Args:
            output_dir: Directory to save screenshots (default: ./screenshots)
        """
        self.output_dir = output_dir or Path("./screenshots")
        self.output_dir.mkdir(parents=True, exist_ok=True)

    async def capture(
        self,
        url: str,
        full_page: bool = True,
        viewport_width: int = 1440,
        viewport_height: int = 900,
        wait_for: str | None = None,
    ) -> Path:
        """Capture a screenshot of the given URL.

        Args:
            url: The URL to capture
            full_page: Whether to capture the full page or just viewport
            viewport_width: Viewport width in pixels
            viewport_height: Viewport height in pixels
            wait_for: Optional CSS selector to wait for before capturing

        Returns:
            Path to the saved screenshot
        """
        # Normalize URL
        if not url.startswith("http"):
            url = f"https://{url}"

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                viewport={"width": viewport_width, "height": viewport_height},
                device_scale_factor=2,  # Retina quality
            )
            page = await context.new_page()

            await page.goto(url, wait_until="networkidle")

            if wait_for:
                try:
                    await page.wait_for_selector(wait_for, timeout=5000)
                except Exception:
                    pass  # Continue even if selector not found

            # Additional wait for lazy-loaded content
            await asyncio.sleep(1)

            # Generate filename
            domain = url.replace("https://", "").replace("http://", "").split("/")[0]
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{domain}_{timestamp}.png"
            filepath = self.output_dir / filename

            await page.screenshot(path=str(filepath), full_page=full_page)
            await browser.close()

            return filepath

    async def capture_multiple(
        self,
        urls: list[str],
        full_page: bool = False,
    ) -> list[Path]:
        """Capture screenshots of multiple URLs.

        Args:
            urls: List of URLs to capture
            full_page: Whether to capture full pages

        Returns:
            List of paths to saved screenshots
        """
        results: list[Path] = []

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)

            for url in urls:
                # Normalize URL
                if not url.startswith("http"):
                    url = f"https://{url}"

                try:
                    context = await browser.new_context(
                        viewport={"width": 1440, "height": 900}
                    )
                    page = await context.new_page()
                    await page.goto(url, wait_until="networkidle")

                    domain = (
                        url.replace("https://", "").replace("http://", "").split("/")[0]
                    )
                    path_part = url.split(domain)[-1].replace("/", "_") or "_home"
                    filename = f"{domain}{path_part}.png"
                    filepath = self.output_dir / filename

                    await page.screenshot(path=str(filepath), full_page=full_page)
                    results.append(filepath)
                    await context.close()
                except Exception:
                    pass  # Skip failed captures

            await browser.close()

        return results


async def main() -> None:
    """Test the screenshot tool."""
    tool = ScreenshotTool()
    path = await tool.capture("stripe.com", full_page=False)
    print(f"Screenshot saved to: {path}")


if __name__ == "__main__":
    asyncio.run(main())
