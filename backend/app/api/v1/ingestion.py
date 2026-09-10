
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.ingestion import IngestRequest
from app.services.rag.ingestion_service import IngestionService

router = APIRouter(
    prefix="/ingestion",
    tags=["Ingestion"],
)

ingestion_service = IngestionService()


@router.post("/documents")
def ingest_document(
    payload: IngestRequest,
    db: Session = Depends(get_db),
):
    documents = ingestion_service.ingest(
        db=db,
        title=payload.title,
        source=payload.source,
        document_type=payload.document_type,
        text=payload.text,
    )

    return {
        "message": "Document ingested successfully",
        "document_count": len(documents),
        "documents": [
            {
                "id": document.id,
                "title": document.title,
                "source": document.source,
                "document_type": document.document_type,
                "chunk_index": document.chunk_index,
            }
            for document in documents
        ],
    }