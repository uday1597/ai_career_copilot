from app.services.ingestion.openai_service import client


def should_continue(
    user_prompt: str,
    tool_results: dict,
):

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"""
You are evaluating whether the agent has enough information.

User Request:
{user_prompt}

Tool Results:
{tool_results}

Return ONLY JSON.

{{
    "continue": true,
    "reason": "",
    "next_tool": ""
}}
"""
    )

    return response.output_text