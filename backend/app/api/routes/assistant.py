import json

from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.agent.runtime import AgentRuntime


router = APIRouter(
    prefix="/assistant",
    tags=["Assistant"],
)


class ChatRequest(BaseModel):
    message: str


def sse_event(data: dict) -> str:
    return f"data: {json.dumps(data)}\n\n"


@router.post("/chat")
async def chat(
    payload: ChatRequest,
    db: Session = Depends(get_db),
):

    runtime = AgentRuntime(db)

    async def event_generator():

        async for event in runtime.run(
            prompt=payload.message,
            thread_id="career-copilot",
        ):

            if event is None:
                continue

            yield sse_event(event)

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )