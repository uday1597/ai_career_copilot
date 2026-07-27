from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.schemas.assistant import (
    ChatRequest,
    ChatResponse,
)

from app.services.agent.assistant import chat


router = APIRouter(
    prefix="/assistant",
    tags=["Assistant"],
)


@router.post(
    "/chat",
    response_model=ChatResponse,
)
def assistant_chat(
    payload: ChatRequest,
    db: Session = Depends(get_db),
):

    return ChatResponse(
        response=chat(
            payload.message,
            db,
        )
    )