import json

from app.services.ingestion.dashboard_service import build_dashboard
from app.models.job import Job
from app.models.resume_match import ResumeMatch
from app.models.learning_roadmap import LearningRoadmap
from app.models.assessment import Assessment

def get_dashboard_tool(db,context,previous_results,):

    dashboard = build_dashboard(db)

    return json.dumps(
        dashboard.model_dump(),
        default=str,
    )

def search_jobs_tool(db,context,previous_results,keyword: str | None = None,):

    jobs = (
        db.query(Job)
        .limit(10)
        .all()
    )

    results = []

    for job in jobs:

        results.append(
            {
                "id": str(job.id),
                "title": job.title,
                "company": job.company,
                "location": job.location,
                "technologies": job.technologies,
            }
        )

    return json.dumps(results, default=str)

def get_resume_match_tool(db,context,
    previous_results,):

    match = (
        db.query(ResumeMatch)
        .order_by(
            ResumeMatch.created_at.desc()
        )
        .first()
    )

    if match is None:

        return json.dumps(
            {
                "status": "NO_MATCH"
            }
        )

    return json.dumps(
        {
            "match_score": match.match_score,
            "matching_technologies": match.matching_technologies,
            "missing_technologies": match.missing_technologies,
        },
        default=str,
    )

def get_learning_roadmap_tool(db,context,
    previous_results,):

    roadmap = (
        db.query(LearningRoadmap)
        .order_by(
            LearningRoadmap.created_at.desc()
        )
        .first()
    )

    if roadmap is None:

        return json.dumps(
            {
                "status": "NO_ROADMAP"
            }
        )

    return json.dumps(
        roadmap.roadmap,
        default=str,
    )
    
def get_assessment_tool(db,context,
    previous_results,week: int,):
    
    assessment = (
        db.query(Assessment)
        .filter(
            Assessment.week == week
        )
        .first()
    )

    if assessment is None:

        return json.dumps(
            {
                "status": "NO_ASSESSMENT"
            }
        )
    return json.dumps(
        {
            "week": assessment.week,
            "status": assessment.status,
            "overall_score": assessment.overall_score,
            "feedback": assessment.feedback,
        },
        default=str,
    ) 

TOOLS = [

    {
        "type": "function",
        "name": "get_dashboard",
        "description": "Returns the user's dashboard.",
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },

    {
        "type": "function",
        "name": "search_jobs",
        "description": "Returns available jobs from the Career Copilot database.",
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },

    {
        "type": "function",
        "name": "get_resume_match",
        "description": "Returns the latest resume match analysis including score, matching skills and missing skills.",
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },

    {
        "type": "function",
        "name": "get_learning_roadmap",
        "description": "Returns the user's complete learning roadmap including weeks, topics, focus areas, resources and mini projects.",
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },

    {
        "type": "function",
        "name": "get_assessment",
        "description": "Returns assessment results for a specific roadmap week.",
        "parameters": {
            "type": "object",
            "properties": {
                "week": {
                    "type": "integer",
                    "description": "Roadmap week number"
                }
            },
            "required": ["week"]
        }
    }
]