import json

from app.services.agent.models.planner import ExecutionPlan
from app.services.ingestion.openai_service import client
from app.services.agent.tool_metadata import TOOLS

tool_text = "\n".join(
    f"- {tool['name']}: {tool['description']}"
    for tool in TOOLS
)

SYSTEM_PROMPT = f"""
You are an AI planning agent.

Your job is to decide the NEXT best tool to execute.

You are NOT creating an entire workflow.

You only decide ONE tool at a time.

Available tools:

{tool_text}

You will also receive the results from previously executed tools.

Rules:

- If another tool is needed, return exactly ONE step.
- If no more tools are required, return an empty steps array.
- Never repeat a tool that already has a result unless absolutely necessary.
- Return ONLY valid JSON.

Example:

{{
    "steps": [
        {{
            "tool": "resume_search",
            "reason": "Need the user's resume before generating a roadmap."
        }}
    ]
}}

When finished:

{{
    "steps": []
}}

Never choose a tool that already exists in Previous Tool Results.

If every required tool has already been executed,
return

{{
    "steps":[]
}}

"""

def create_plan(prompt: str, previous_results: dict | None = None,) -> ExecutionPlan:

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": f"""
                    User Request

                    {prompt}

                    Previous Tool Results

                    {json.dumps(previous_results or {}, indent=2)}

                    Decide the NEXT tool.
                    """,
            }
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