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
)


# ============================================================
# GRAPH BUILDER
# ============================================================

builder = StateGraph(
    AgentState
)


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
# INTENT ROUTING
#
# CASUAL / GENERAL
#       ↓
#   responder
#
# TOOL
#       ↓
#   planner
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
# TOOL PIPELINE
#
# planner
#    ↓
# executor
#    ↓
# responder
# ============================================================

builder.add_edge(
    "planner",
    "executor",
)

builder.add_edge(
    "executor",
    "responder",
)


# ============================================================
# END
# ============================================================

builder.add_edge(
    "responder",
    END,
)

# ============================================================ 
# COMPILE GRAPH 
# ============================================================ 
graph = builder.compile()