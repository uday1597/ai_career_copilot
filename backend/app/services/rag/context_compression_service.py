import re

from app.models.knowledge_document import KnowledgeDocument


class ContextCompressionService:

    def compress(
        self,
        query: str,
        documents: list[KnowledgeDocument],
    ) -> str:

        query_words = {
            word.lower()
            for word in query.split()
        }

        selected = []

        for document in documents:

            sentences = re.split(
                r"(?<=[.!?])\s+",
                document.content,
            )

            for sentence in sentences:

                words = {
                    word.lower()
                    for word in sentence.split()
                }

                if query_words.intersection(words):

                    selected.append(sentence)

        return "\n".join(selected)