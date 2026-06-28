import asyncio

from app.crawlers.greenhouse import GreenhouseCrawler


async def main():
    crawler = GreenhouseCrawler()

    jobs = await crawler.search_jobs("AI")

    print(jobs)


if __name__ == "__main__":
    asyncio.run(main())