from abc import ABC, abstractmethod

from app.models.knowledge_document import KnowledgeDocument


class BaseReRanker(ABC):

    @abstractmethod
    def rerank(
        self,
        query: str,
        documents: list[KnowledgeDocument],
        top_k: int = 5,
    ) -> list[KnowledgeDocument]:
        pass