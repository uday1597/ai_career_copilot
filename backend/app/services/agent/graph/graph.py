from langgraph.graph import StateGraph

from .state import AgentState
from .nodes import planner_node, executor_node, responder_node
from .router import router
from .memory import memory

builder = StateGraph(AgentState)

builder.add_node(
    "planner",
    planner_node
)

builder.add_node(
    "executor",
    executor_node
)

builder.add_node(
    "responder",
    responder_node
)

builder.set_entry_point(
    "planner"
)

builder.add_conditional_edges(
    "planner",
    router,
)

builder.add_edge(
    "executor",
    "planner",
)

builder.set_finish_point(
    "responder"
)

graph = builder.compile()