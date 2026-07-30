from uuid import UUID
from fastapi import APIRouter, HTTPException
from fastapi import UploadFile
from fastapi import File
from fastapi import Depends
from pathlib import Path
import shutil
from fastapi.responses import FileResponse
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
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@router.get("")
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

@router.get("/{resume_id}/preview")
def preview_resume(
    resume_id: UUID,
    db: Session = Depends(get_db)
):

    resume = (
        db.query(Resume)
        .filter(Resume.id == resume_id)
        .first()
    )

    if not resume:
        raise HTTPException(
            status_code=404,
            detail="Resume not found"
        )

    return FileResponse(
        path=resume.file_path,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f"inline; filename={resume.filename}"
        }
    )
    
@router.post(
    "/upload",
    response_model=ResumeResponse
)
async def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    file_path = UPLOAD_DIR / file.filename

    # Save PDF
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    # Read for processing
    file_bytes = file_path.read_bytes()
    
    extracted_text = extract_resume(file_bytes)

    analysis, embedding = analyze_resume(
        extracted_text
    )
    print("LLM Result:")
    print(repr(analysis))
    resume = Resume(
        filename=file.filename,
        file_path=str(file_path),
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