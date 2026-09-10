import re

from app.models.knowledge_document import KnowledgeDocument


STOP_WORDS = {
    "what",
    "is",
    "the",
    "a",
    "an",
    "how",
    "why",
    "when",
    "where",
    "which",
    "are",
    "was",
    "were",
    "to",
    "of",
    "in",
    "for",
    "and",
    "or",
}


class ContextCompressionService:

    def compress(
        self,
        query: str,
        documents: list[KnowledgeDocument],
        max_sentences: int = 10,
    ) -> list[dict]:

        query_words = {
            word
            for word in re.findall(
                r"\b\w+\b",
                query.lower(),
            )
            if word not in STOP_WORDS
        }

        scored_sentences = []

        for document in documents:

            sentences = re.split(
                r"(?<=[.!?])\s+",
                document.content or "",
            )

            for sentence in sentences:

                sentence = sentence.strip()

                if not sentence:
                    continue

                sentence_words = set(
                    re.findall(
                        r"\b\w+\b",
                        sentence.lower(),
                    )
                )

                score = len(
                    query_words.intersection(
                        sentence_words
                    )
                )

                if score > 0:

                    scored_sentences.append(
                        {
                            "score": score,
                            "document_id": document.id,
                            "document_type": document.document_type,
                            "source": document.source,
                            "content": sentence,
                        }
                    )

        scored_sentences.sort(
            key=lambda item: item["score"],
            reverse=True,
        )

        return scored_sentences[:max_sentences]