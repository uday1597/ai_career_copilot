from app.services.agent.tools import (
    get_dashboard_tool,
    search_jobs_tool,
    get_resume_match_tool,
    get_learning_roadmap_tool,
    get_assessment_tool,
)

TOOL_REGISTRY = {

    "get_dashboard": get_dashboard_tool,

    "search_jobs": search_jobs_tool,

    "get_resume_match": get_resume_match_tool,

    "get_learning_roadmap": get_learning_roadmap_tool,

    "get_assessment": get_assessment_tool,
}