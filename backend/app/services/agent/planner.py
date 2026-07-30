import json

from app.services.agent.planner_models import ExecutionPlan
from app.services.ingestion.openai_service import client


SYSTEM_PROMPT = """
You are an AI planner.

Your only job is to decide which tools should be executed.

Available tools:

get_dashboard
search_jobs
get_resume_match
get_learning_roadmap
get_assessment

Return ONLY JSON.

{
  "steps":[
    {
      "tool":"",
      "reason":""
    }
  ]
}
"""


def create_plan(user_prompt: str) -> ExecutionPlan:

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
    )

    text = (
        response.output_text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return ExecutionPlan.model_validate(
        json.loads(text)
    )