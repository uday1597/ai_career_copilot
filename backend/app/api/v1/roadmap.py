import json
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from uuid import UUID
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.resume import Resume
from app.models.job import Job
from app.models.learning_roadmap import LearningRoadmap

from app.schemas.roadmap import RoadmapGenerateRequest
from app.schemas.roadmap import RoadmapResponse

from app.services.ai.learning_roadmap import generate_learning_roadmap, generate_learning_roadmap_stream
from app.models.resume_match import ResumeMatch
from app.core.streaming import StreamEvent
from app.core.sse import sse_response
from app.services.agent.runtime import AgentRuntime
from fastapi.responses import StreamingResponse

from app.services.agent.stream import sse

router = APIRouter(
    prefix="/roadmap",
    tags=["Roadmap"]
)

@router.post("/test")
def test_agent(
    payload: RoadmapGenerateRequest,
    db: Session = Depends(get_db),
):

    runtime = AgentRuntime(db)

    def generate():

        for event in runtime.run(
            "Generate a learning roadmap",
        ):
            yield sse(event)

    return StreamingResponse(
        generate(),
        media_type="text/event-stream",
    )
    
@router.post("/generate-stream")
def generate_stream(
    payload: RoadmapGenerateRequest,
    db: Session = Depends(get_db),
):

    def event_generator():

        yield StreamEvent.status("Loading match...")

        match = db.get(
            ResumeMatch,
            payload.match_id,
        )

        if not match:
            yield StreamEvent.error("Match not found")
            return

        yield StreamEvent.progress(20)

        yield StreamEvent.status("Checking existing roadmap...")

        existing = (
            db.query(LearningRoadmap)
            .filter(
                LearningRoadmap.match_id == payload.match_id
            )
            .first()
        )

        if existing:
            yield StreamEvent.complete({
                "existing": True,
                "roadmap": existing.roadmap,
            })
            return

        yield StreamEvent.progress(40)

        yield StreamEvent.status("Generating AI roadmap...")

        roadmap_text = ""

        for event in generate_learning_roadmap_stream(
            match.match_score,
            match.matching_technologies,
            match.missing_technologies,
            match.ai_explanation,
        ):

            if event["type"] == "token":

                roadmap_text += event["content"]

                yield StreamEvent.token(event["content"])

            elif event["type"] == "complete":

                roadmap_text = event["content"]

        roadmap_text = (
            roadmap_text
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        roadmap = json.loads(roadmap_text)

        yield StreamEvent.progress(80)

        yield StreamEvent.status("Saving roadmap...")

        record = LearningRoadmap(
            match_id=match.id,
            roadmap=roadmap,
        )

        db.add(record)
        db.commit()
        db.refresh(record)

        yield StreamEvent.progress(100)

        yield StreamEvent.complete({
            "existing": False,
            "id": str(record.id),
            "roadmap": record.roadmap,
        })

    return sse_response(event_generator())

@router.post(
    "/generate",
    response_model=RoadmapResponse,
)
def generate(
    payload: RoadmapGenerateRequest,
    db: Session = Depends(get_db),
):

    match = db.get(
        ResumeMatch,
        payload.match_id,
    )

    if not match:
        raise HTTPException(
            status_code=404,
            detail="Match not found",
        )

    existing = (
        db.query(LearningRoadmap)
        .filter(
            LearningRoadmap.match_id == payload.match_id
        )
        .first()
    )

    if existing:
        return existing

    roadmap = generate_learning_roadmap(
        match.match_score,
        match.matching_technologies,
        match.missing_technologies,
        match.ai_explanation,
    )

    record = LearningRoadmap(
        match_id=match.id,
        roadmap=roadmap,
    )

    db.add(record)

    db.commit()

    db.refresh(record)

    return record

@router.get(
    "/{match_id}",
    response_model=RoadmapResponse,
)
def get_roadmap(
    match_id: UUID,
    db: Session = Depends(get_db),
):

    roadmap = (
        db.query(LearningRoadmap)
        .filter(
            LearningRoadmap.match_id == match_id
        )
        .first()
    )

    if not roadmap:
        raise HTTPException(
            status_code=404,
            detail="Roadmap not found",
        )

    return roadmap