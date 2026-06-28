from abc import ABC, abstractmethod

from app.crawlers.models import CrawledJob


class BaseCrawler(ABC):

    @abstractmethod
    async def search_jobs(
        self,
        query: str
    ) -> list[CrawledJob]:
        pass