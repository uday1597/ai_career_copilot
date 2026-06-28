from abc import ABC, abstractmethod

from app.job_discovery.models import CrawledJob


class BaseProvider(ABC):

    @abstractmethod
    async def search(
        self,
        query: str
    ) -> list[CrawledJob]:
        pass