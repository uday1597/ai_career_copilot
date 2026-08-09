from .state import AgentState


def route_after_planner(state: AgentState):

    plan = state["plan"]

    if plan.steps:
        return "executor"

    return "responder"


def route_after_intent(
    state: AgentState,
):

    intent = state.get(
        "intent",
        "GENERAL",
    )

    if intent == "TOOL":
        return "planner"

    return "responder"