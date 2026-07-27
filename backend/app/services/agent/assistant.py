import json

from app.services.ingestion.openai_service import client

from app.services.agent.prompts import SYSTEM_PROMPT
from app.services.agent.tools import TOOLS
from app.services.agent.tool_registry import TOOL_REGISTRY


def chat(
    message: str,
    db,
):

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": message,
            },
        ],
        tools=TOOLS,
    )

    while True:

        tool_calls = [
            item
            for item in response.output
            if item.type == "function_call"
        ]

        if not tool_calls:
            return response.output_text

        tool_outputs = []

        for tool_call in tool_calls:

            tool = TOOL_REGISTRY.get(tool_call.name)

            if tool is None:
                raise Exception(
                    f"Tool '{tool_call.name}' not registered."
                )

            arguments = json.loads(
                tool_call.arguments or "{}"
            )

            output = tool(
                db=db,
                **arguments,
            )

            tool_outputs.append(
                {
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": output,
                }
            )

        response = client.responses.create(
            model="gpt-4.1-mini",
            previous_response_id=response.id,
            input=tool_outputs,
        )