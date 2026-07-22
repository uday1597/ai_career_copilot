from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.resume import Resume
from app.schemas.resume import ResumeResponse
from app.services.ai.resume_analyzer import analyze_resume
from app.extractors.extractor_service import extract_resume

router = APIRouter(
    prefix="/resume",
    tags=["resume"]
)

@router.get("/")
def get_resumes(
    db: Session = Depends(get_db)
):
    rows = db.query(
    Resume.id,
    Resume.filename,
    Resume.technologies,
    Resume.summary,
    Resume.extraction_method,
    Resume.page_count,
    ).all()

    return [
        {
            "id": row.id,
            "filename": row.filename,
            "technologies": row.technologies,
            "summary": row.summary,
            "extraction_method": row.extraction_method,
            "page_count": row.page_count,
        }
        for row in rows
    ]
@router.post(
    "/upload",
    response_model=ResumeResponse
)
async def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    file_bytes = await file.read()

    extracted_text = extract_resume(
        file_bytes
    )
    print("=" * 100)
    print(extracted_text)
    print("=" * 100)
    analysis,embedding = analyze_resume(
    extracted_text
    )
    print(type(analysis))
    print(analysis)
    print(type(analysis["technologies"]))
    try:
        resume = Resume(
            filename=file.filename,
            extracted_text=extracted_text["text"],
            technologies=analysis["technologies"],
            summary=analysis["summary"],
            extraction_method=extracted_text["extraction_method"],
            page_count=extracted_text["page_count"],
            embedding=embedding
        )

        db.add(resume)
        db.commit()
        db.refresh(resume)

        return resume

    except Exception as e:
        print("ERROR:", repr(e))
        raise