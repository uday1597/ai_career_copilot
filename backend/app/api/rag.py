from typing import Optional
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.services.rag.retrieval_service import RetrievalService
from app.services.rag.rag_service import RAGService

router = APIRouter(
    prefix="/rag",
    tags=["RAG"],
)


@router.get("/search")

def search(
    query: str,
    db: Session = Depends(get_db),
):

    service = RetrievalService()

    docs = service.retrieve(
        db,
        query,
    )

    return [
        {
            "title": d.title,
            "chunk": d.chunk_index,
            "content": d.content,
        }
        for d in docs
    ]

@router.get("/ask")
def ask(
    question: str,
    document_type: Optional[str] = None,
    history: Optional[str] = None,
    top_k: int = 5,
    db: Session = Depends(get_db),
):
    service = RAGService()

    answer = service.ask(
        db=db,
        question=question,
        top_k=top_k,
        document_type=document_type,
        history=history,
    )

    return {
        "answer": answer
    }