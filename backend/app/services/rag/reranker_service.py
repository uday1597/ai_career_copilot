import re

from app.models.knowledge_document import KnowledgeDocument
from app.services.rag.base_reranker import BaseReRanker


class ReRankerService(BaseReRanker):

    def rerank(
        self,
        query: str,
        documents: list[KnowledgeDocument],
        top_k: int = 5,
    ) -> list[KnowledgeDocument]:

        query_words = set(
            re.findall(
                r"\b\w+\b",
                query.lower(),
            )
        )

        scored = []

        for document in documents:

            content_words = set(
                re.findall(
                    r"\b\w+\b",
                    document.content.lower(),
                )
            )

            score = len(
                query_words.intersection(
                    content_words
                )
            )

            scored.append(
                (
                    score,
                    document,
                )
            )

        scored.sort(
            key=lambda item: item[0],
            reverse=True,
        )

        return [
            document
            for _, document in scored[:top_k]
        ]