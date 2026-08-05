from app.services.agent.context import AgentContext
from app.services.agent.executor import AgentExecutor
from app.services.agent.planner import create_plan
from app.services.agent.responder import stream_response

from .state import AgentState


def planner_node(state: AgentState):

    plan = create_plan(
        prompt=state["prompt"],
        previous_results=state.get(
            "tool_results",
            {},
        ),
    )
    print("=== Planner ===")
    print(state["prompt"])
    return {
        "plan": plan,
    }


def executor_node(state: AgentState):

    executor = AgentExecutor(
        state["db"]
    )

    context = state.get("context")

    if context is None:
        context = AgentContext()

    results = state.get(
        "tool_results",
        {},
    )

    step = state["plan"].steps[0]

    for event in executor.execute_step(
        step,
        context,
        results,
    ):
        pass
    print("=== Executor ===")
    print(state["plan"].steps[0])
    return {
        "tool_results": results,
        "context": context,
    }


def responder_node(state: AgentState):

    answer = ""

    for token in stream_response(
        state["prompt"],
        state.get(
            "tool_results",
            {},
        ),
    ):
        answer += token

    print("=== Responder ===")
    print(answer)
    return {
        "answer": answer,
    }