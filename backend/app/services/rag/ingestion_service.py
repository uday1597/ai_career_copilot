from app.models.knowledge_document import KnowledgeDocument

from app.services.ai.embedding_service import EmbeddingService
from app.services.rag.chunking_service import ChunkingService


class IngestionService:

    def __init__(self):

        self.chunker = ChunkingService()

        self.embedding_service = EmbeddingService()

    def ingest(
        self,
        db,
        *,
        title: str,
        source: str,
        document_type: str,
        text: str,
    ):

        chunks = self.chunker.chunk(text)

        documents = []

        for index, chunk in enumerate(chunks):

            embedding = self.embedding_service.create_embedding(
                chunk
            )

            document = KnowledgeDocument(

                title=title,

                source=source,

                document_type=document_type,

                chunk_index=index,

                content=chunk,

                embedding=embedding,

            )

            db.add(document)

            documents.append(document)

        db.commit()

        return documents