from sqlalchemy import select

from app.models.knowledge_document import KnowledgeDocument
from app.services.ai.embedding_service import EmbeddingService
from sqlalchemy import select
from sqlalchemy import or_
from app.services.rag.reranker_service import (
    ReRankerService,
)

class RetrievalService:

    def __init__(self):

        self.embedding_service = EmbeddingService()
        self.reranker = ReRankerService()

    def vector_search(
        self,
        db,
        query: str,
        top_k: int = 5,
        document_type: str | None = None,
    ) -> list[KnowledgeDocument]:

        query_embedding = (
            self.embedding_service.create_embedding(
                query
            )
        )

        statement = select(KnowledgeDocument)

        if document_type:

            statement = statement.where(
                KnowledgeDocument.document_type == document_type
            )

        statement = (
            statement
            .order_by(
                KnowledgeDocument.embedding.cosine_distance(
                    query_embedding
                )
            )
            .limit(top_k)
        )

        return (
            db.execute(statement)
            .scalars()
            .all()
        )

    def keyword_search(
        self,
        db,
        query: str,
        limit: int = 5,
        document_type: str | None = None,
    ):

        words = [
            word
            for word in query.split()
            if len(word) > 2
        ]

        if not words:
            return []

        conditions = []

        for word in words:

            conditions.append(
                KnowledgeDocument.content.ilike(
                    f"%{word}%"
                )
            )

        statement = (
            select(KnowledgeDocument)
            .where(or_(*conditions))
            .limit(limit)
        )
        if document_type:

            statement = statement.where(
                KnowledgeDocument.document_type == document_type
            )

        return (
            db.execute(statement)
            .scalars()
            .all()
        )

    def hybrid_search(
        self,
        db,
        query,
        top_k=5,
        document_type=None,
    ):

        vector_results = self.vector_search(
            db,
            query,
            top_k,
            document_type=document_type
        )

        keyword_results = self.keyword_search(
            db,
            query,
            top_k,
            document_type=document_type
        )

        merged = {}

        for document in vector_results:

            merged[document.id] = document

        for document in keyword_results:

            merged[document.id] = document

        return list(
            merged.values()
        )[:top_k]