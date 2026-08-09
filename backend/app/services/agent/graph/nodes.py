from langgraph.runtime import Runtime

from app.services.agent.context import AgentContext
from app.services.agent.executor import AgentExecutor
from app.services.agent.planner import create_plan
from app.services.agent.responder import stream_response

from .runtime_context import AgentRuntimeContext
from .state import AgentState

from langgraph.config import get_stream_writer
from app.services.agent.intent import classify_intent

def intent_node(state: AgentState):

    intent = classify_intent(
        state["prompt"]
    )

    return {
        "intent": intent,
    }

async def planner_node(
    state: AgentState,
):
    plan = await create_plan(
        prompt=state["prompt"],
        previous_results=state.get(
            "tool_results",
            {},
        ),
    )

    return {
        "plan": plan,
    }

async def executor_node(
    state: AgentState,
    runtime: Runtime[AgentRuntimeContext],
):

    executor = AgentExecutor(
        runtime.context.db
    )

    context = AgentContext()

    results = {}

    async for event in executor.execute(
        state["plan"],
        context,
    ):

        if event["type"] == "tool_end":

            results[event["tool"]] = event["result"]

    return {
        "tool_results": results,
    }

def responder_node(state: AgentState):

    writer = get_stream_writer()

    answer = ""

    for token in stream_response(
        state["prompt"],
        state.get("tool_results", {}),
    ):

        answer += token

        writer({
            "type": "token",
            "content": token,
        })

    writer({
        "type": "complete",
        "answer": answer,
    })

    return {
        "answer": answer,
    }