from app.services.ingestion.openai_service import client


def stream_response(
    user_prompt: str,
    tool_results: dict,
):

    with client.responses.stream(
        model="gpt-4.1-mini",
        input=f"""
User Request

{user_prompt}

Tool Results

{tool_results}

Respond naturally.
Never mention tool names.
Use the available information.
"""
    ) as stream:

        for event in stream:

            if event.type == "response.output_text.delta":

                yield event.delta

        stream.until_done()