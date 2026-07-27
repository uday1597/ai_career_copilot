from app.models.knowledge_document import KnowledgeDocument


class ReRankerService:

    def rerank(
        self,
        query: str,
        documents: list[KnowledgeDocument],
        top_k: int = 5,
    ) -> list[KnowledgeDocument]:

        query_words = {
            word.lower()
            for word in query.split()
        }

        scored = []

        for document in documents:

            content_words = {
                word.lower()
                for word in document.content.split()
            }

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