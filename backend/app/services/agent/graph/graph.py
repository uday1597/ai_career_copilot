from langgraph.graph import END, START, StateGraph

from .state import AgentState

from .nodes import (
    intent_node,
    planner_node,
    executor_node,
    responder_node,
)

from .router import (
    route_after_intent,
    route_after_planner,
)


builder = StateGraph(AgentState)


# ============================================================
# NODES
# ============================================================

builder.add_node(
    "intent",
    intent_node,
)

builder.add_node(
    "planner",
    planner_node,
)

builder.add_node(
    "executor",
    executor_node,
)

builder.add_node(
    "responder",
    responder_node,
)


# ============================================================
# START
# ============================================================

builder.add_edge(
    START,
    "intent",
)


# ============================================================
# INTENT
# ============================================================

builder.add_conditional_edges(
    "intent",

    route_after_intent,

    {
        "planner": "planner",
        "responder": "responder",
    },
)


# ============================================================
# PLANNER
#
# If plan has steps:
#
#     planner → executor
#
# If plan is empty:
#
#     planner → responder
# ============================================================

builder.add_conditional_edges(
    "planner",

    route_after_planner,

    {
        "executor": "executor",
        "responder": "responder",
    },
)


# ============================================================
# EXECUTOR
#
# After executing a tool:
#
#     executor → planner
#
# Planner sees previous tool results and decides
# whether another tool is required.
# ============================================================

builder.add_edge(
    "executor",
    "planner",
)


# ============================================================
# RESPONDER
# ============================================================

builder.add_edge(
    "responder",
    END,
)


# ============================================================
# COMPILE
# ============================================================

graph = builder.compile()