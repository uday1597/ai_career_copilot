import json

from app.services.ingestion.openai_service import client

from app.services.agent.prompts import SYSTEM_PROMPT
from app.services.agent.tool_metadata import TOOLS
from app.services.agent.tools.registery import TOOL_REGISTRY
from app.services.agent.context import AgentContext
from app.services.ingestion.openai_service import client



def chat(
    message: str,
    db,
):
    """
    Existing non-streaming assistant.
    """

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

            tool = TOOL_REGISTRY.get(
                tool_call.name
            )

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

def chat_stream(
    message: str,
    db,
):
    """
    Streaming assistant with function/tool calling.

    Text is streamed to the frontend as it is generated.
    Tool calls are executed and the model continues
    generating the final response.
    """

    # ==================================================
    # AGENT CONTEXT
    # ==================================================

    context = AgentContext()

    previous_results = {}

    # ==================================================
    # FIRST MODEL RESPONSE
    # ==================================================

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

        stream=True,
    )

    function_calls = []
    completed_response = None

    # ==================================================
    # STREAM FIRST MODEL RESPONSE
    # ==================================================

    for event in response:

        # ------------------------------
        # Normal text
        # ------------------------------

        if event.type == "response.output_text.delta":

            yield event.delta

        # ------------------------------
        # Response completed
        # ------------------------------

        elif event.type == "response.completed":

            completed_response = event.response

            break

    # ==================================================
    # NO RESPONSE
    # ==================================================

    if completed_response is None:
        return

    # ==================================================
    # FIND FUNCTION CALLS
    # ==================================================

    for item in completed_response.output:

        if item.type == "function_call":

            function_calls.append(item)

    # ==================================================
    # NO TOOL CALL
    # ==================================================

    if not function_calls:
        return

    # ==================================================
    # EXECUTE TOOLS
    # ==================================================

    tool_outputs = []

    for tool_call in function_calls:

        tool_name = tool_call.name

        call_id = tool_call.call_id

        arguments = json.loads(
            tool_call.arguments or "{}"
        )

        # ------------------------------
        # Find registered tool
        # ------------------------------

        tool = TOOL_REGISTRY.get(
            tool_name
        )

        if tool is None:

            raise Exception(
                f"Tool '{tool_name}' not registered."
            )

        # ------------------------------
        # Execute tool
        # ------------------------------

        output = tool(
            db=db,
            context=context,
            previous_results=previous_results,
            **arguments,
        )

        # ------------------------------
        # Store result
        # ------------------------------

        previous_results[tool_name] = output

        context.put(
            tool_name,
            output,
        )

        # ------------------------------
        # Send result back to model
        # ------------------------------

        tool_outputs.append(
            {
                "type": "function_call_output",

                "call_id": call_id,

                "output": json.dumps(
                    output,
                    default=str,
                ),
            }
        )

    # ==================================================
    # CONTINUE MODEL AFTER TOOLS
    # ==================================================

    second_response = client.responses.create(
        model="gpt-4.1-mini",

        previous_response_id=completed_response.id,

        input=tool_outputs,

        stream=True,
    )

    # ==================================================
    # STREAM FINAL ANSWER
    # ==================================================

    for event in second_response:

        if event.type == "response.output_text.delta":

            yield event.delta

        elif event.type == "response.completed":

            break