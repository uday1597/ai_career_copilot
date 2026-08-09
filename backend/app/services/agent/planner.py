import json

from app.services.agent.models.planner import ExecutionPlan
from app.services.ingestion.openai_service import client
from app.services.agent.tool_metadata import TOOLS
from app.services.agent.mcp.github import GitHubMCPClient

tool_text = "\n".join(
    f"- {tool['name']}: {tool['description']}"
    for tool in TOOLS
)

SYSTEM_PROMPT = f"""
You are an AI planning agent.

Your job is to decide the NEXT best tool to execute.

You are NOT creating an entire workflow.

You only decide ONE tool at a time.

INTERNAL CAREER COPILOT TOOLS:

{tool_text}

MCP TOOLS:

The MCP tools available to you will be provided in the user message.

Rules:

- If another tool is needed, return exactly ONE step.
- If no more tools are required, return an empty steps array.
- Never repeat a tool that already has a result unless absolutely necessary.
- For internal tools, use source="internal".
- For MCP tools, use source="mcp".
- When selecting an MCP tool, provide the required arguments according to its input schema.
- Only select an MCP tool if it is appropriate for the user's request.
- Return ONLY valid JSON.

Example internal tool:

{{
    "steps": [
        {{
            "tool": "get_resume_match",
            "source": "internal",
            "reason": "Need the user's resume information.",
            "arguments": {{}}
        }}
    ]
}}

Example MCP tool:

{{
    "steps": [
        {{
            "tool": "search_repositories",
            "source": "mcp",
            "reason": "Find GitHub repositories relevant to the user's request.",
            "arguments": {{
                "query": "python fastapi"
            }}
        }}
    ]
}}

When finished:

{{
    "steps": []
}}

Never choose a tool that already exists in Previous Tool Results.

If every required tool has already been executed,
return:

{{
    "steps": []
}}
"""
async def create_plan(
    prompt: str,
    previous_results: dict | None = None,
) -> ExecutionPlan:
    print("🔥 CREATE PLAN CALLED")
    print("PROMPT:", prompt)
    # ---------------------------------------
    # Discover MCP tools
    # ---------------------------------------

    mcp_client = GitHubMCPClient()

    mcp_tools = await mcp_client.list_tools()

    mcp_tool_definitions = [
        {
            "name": tool.name,
            "description": tool.description,
            "input_schema": tool.input_schema,
        }
        for tool in mcp_tools
    ]
    # ---------------------------------------
    # Ask planner
    # ---------------------------------------

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

                            {json.dumps(
                                previous_results or {},
                                indent=2,
                            )}

                            Available MCP Tools

                            {json.dumps(
                                mcp_tool_definitions,
                                indent=2,
                            )}

                            Decide the NEXT tool.
                            """,
            },
        ],
    )

    # ---------------------------------------
    # Parse response
    # ---------------------------------------

    text = (
        response.output_text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    plan = ExecutionPlan.model_validate(
        json.loads(text)
    )

    print("\n===== PLANNER PLAN =====")
    print(plan.model_dump_json(indent=2))
    print("========================\n")

    return plan