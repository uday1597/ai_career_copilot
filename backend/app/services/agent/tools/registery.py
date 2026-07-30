from app.services.agent.tools.dashboard import get_dashboard_tool
from app.services.agent.tools.jobs import search_jobs_tool
from app.services.agent.tools.resume import get_resume_match_tool
from app.services.agent.tools.roadmap import get_learning_roadmap_tool
from app.services.agent.tools.assessment import get_assessment_tool

TOOL_REGISTRY = {
    "get_dashboard": get_dashboard_tool,
    "search_jobs": search_jobs_tool,
    "get_resume_match": get_resume_match_tool,
    "get_learning_roadmap": get_learning_roadmap_tool,
    "get_assessment": get_assessment_tool,
}