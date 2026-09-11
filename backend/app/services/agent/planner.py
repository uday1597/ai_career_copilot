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
- Only select a tool that is appropriate for the user's request.

RAG TOOL:

- Use "search_knowledge_base" when the answer requires
  information from Career Copilot's stored knowledge base.

- The knowledge base may contain:
  resume, target job, assessment, roadmap, and other
  ingested career documents.

- Examples:
  "What skills are missing for my target job?"
  "What technologies are missing from my resume?"
  "What are my weaknesses?"
  "Compare my resume with the target job."
  "What did my assessment say?"
  "What should I learn next?"

- When selecting "search_knowledge_base", pass the user's
  question as the "question" argument.

- Do not use RAG merely because the question is career-related.
  Use it only when information from the stored knowledge base
  is required.

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

Example RAG tool:

{{
    "steps": [
        {{
            "tool": "search_knowledge_base",
            "source": "internal",
            "reason": "Need information from the user's stored career documents.",
            "arguments": {{
                "question": "What skills are missing for my target job?"
            }}
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
    # Previous tool results
    # ---------------------------------------

    previous_results = previous_results or {}

    executed_tools = set(
        previous_results.keys()
    )

    print("EXECUTED TOOLS:", executed_tools)

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
User Request:

{prompt}

--------------------------------

ALREADY EXECUTED TOOLS:

{json.dumps(
    list(executed_tools),
    indent=2,
)}

--------------------------------

PREVIOUS TOOL RESULTS:

{json.dumps(
    previous_results,
    indent=2,
)}

--------------------------------

AVAILABLE MCP TOOLS:

{json.dumps(
    mcp_tool_definitions,
    indent=2,
)}

--------------------------------

PLANNING RULE:

Select exactly ONE tool that has NOT already
been executed.

If all required information is already available,
return:

{{
    "steps": []
}}

Do NOT select any tool listed under
ALREADY EXECUTED TOOLS.

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

    # ---------------------------------------
    # SAFETY:
    # Never execute the same tool twice
    # ---------------------------------------

    original_steps = plan.steps

    plan.steps = [
        step
        for step in plan.steps
        if step.tool not in executed_tools
    ]

    # ---------------------------------------
    # Debug
    # ---------------------------------------

    print("\n===== PLANNER =====")

    print(
        "LLM PLAN:",
        [
            step.tool
            for step in original_steps
        ],
    )

    print(
        "EXECUTED:",
        list(executed_tools),
    )

    print(
        "FINAL PLAN:",
        [
            step.tool
            for step in plan.steps
        ],
    )

    print("===================\n")

    return plan