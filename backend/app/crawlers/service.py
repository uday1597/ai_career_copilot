from app.crawlers.greenhouse import GreenhouseCrawler


class JobCrawlerService:

    def __init__(self):
        self.greenhouse = GreenhouseCrawler()

    async def search(
        self,
        query: str
    ):
        return await self.greenhouse.search_jobs(query)