from playwright.async_api import async_playwright

from app.crawlers.base import BaseCrawler


class GreenhouseCrawler(BaseCrawler):

    async def search_jobs(
        self,
        query: str
    ):

        async with async_playwright() as p:

            browser = await p.chromium.launch(
                headless=False
            )

            page = await browser.new_page()

            await page.goto(
                "https://boards.greenhouse.io/openai"
            )

            print(
                await page.title()
            )

            await browser.close()

        return []