import json

from app.services.agent.models.planner import ExecutionPlan
from app.services.ingestion.openai_service import client
from app.services.agent.tool_metadata import TOOLS

tool_text = "\n".join(
    f"- {tool['name']}: {tool['description']}"
    for tool in TOOLS
)

SYSTEM_PROMPT = f"""
You are an AI planner.

Your job is to decide which tools should be executed.

Available tools:

{tool_text}

Return ONLY JSON.

{{
    "steps":[
        {{
            "tool":"",
            "reason":""
        }}
    ]
}}
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