from .state import AgentState


def router(state: AgentState):

    if len(state["plan"].steps):

        return "executor"

    return "responder"