from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import engine
from app.db.base import Base

import app.models
from app.api.v1.resume import router as resume_router
from app.api.v1.job import router as job_router
from app.api.v1.analysis import router as analysis_router
from app.api.v1.job_discovery import router as job_discovery_router
from app.api.v1.roadmap import router as roadmap_router
from app.api.v1.assessment import router as assessment_router
from app.api.v1.dashboard import router as dashboard_router
from app.api.routes.assistant import router as assistant_router
from app.api.rag import router as rag_router
import os


app = FastAPI(
    title="Career Copilot",
    version="0.1.0"
)

origins = [
    "http://localhost:3000",
]

frontend_url = os.getenv("FRONTEND_URL")

if frontend_url:
    origins.append(frontend_url)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(job_discovery_router)
app.include_router(resume_router)
app.include_router(job_router)
app.include_router(analysis_router)
app.include_router(roadmap_router)
app.include_router(assessment_router)
app.include_router(dashboard_router)
app.include_router(assistant_router)
app.include_router(rag_router)


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/")
def root():
    return {
        "app": "Career Copilot API",
        "status": "running",
        "version": "1.0.0"
    }