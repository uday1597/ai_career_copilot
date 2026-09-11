from langgraph.runtime import Runtime
from langgraph.config import get_stream_writer

from app.services.agent.context import AgentContext
from app.services.agent.executor import AgentExecutor
from app.services.agent.planner import create_plan
from app.services.agent.responder import stream_response
from app.services.agent.intent import classify_intent

from .runtime_context import AgentRuntimeContext
from .state import AgentState

# ============================================================

# INTENT NODE

# ============================================================

async def intent_node(
state: AgentState,
):
    print("🔥🔥🔥🔥 INTENT NODE HIT")
    print("PROMPT:", state["prompt"])

    intent = classify_intent(
        state["prompt"]
    )

    print(
        "🔥🔥🔥🔥 INTENT RESULT:",
        intent,
    )

    return {
        "intent": intent,
    }


# ============================================================

# PLANNER NODE

# ============================================================

async def planner_node(
state: AgentState,
):
    print("🔥🔥🔥🔥 PLANNER NODE HIT")
    print("PROMPT:", state["prompt"])

    previous_results = state.get(
        "tool_results",
        {},
    )

    print(
        "📦 PREVIOUS TOOL RESULTS:",
        previous_results,
    )

    plan = await create_plan(
        prompt=state["prompt"],
        previous_results=previous_results,
    )

    print(
        "🧠 PLANNER RETURNED:",
        [
            step.tool
            for step in plan.steps
        ],
    )

    return {
        "plan": plan,
    }

# ============================================================

# EXECUTOR NODE

# ============================================================

async def executor_node(
state: AgentState,
runtime: Runtime[AgentRuntimeContext],
):
    print("\n" + "=" * 60)
    print("⚙️ EXECUTOR NODE REACHED")
    print("=" * 60)

    executor = AgentExecutor(
        runtime.context.db
    )

    context = AgentContext()

    # IMPORTANT:
    # Preserve results from previous planner/executor cycles.
    results = state.get(
        "tool_results",
        {},
    ).copy()

    print(
        "📦 EXISTING TOOL RESULTS:",
        results,
    )

    # Execute the current plan.
    async for event in executor.execute(
        state["plan"],
        context,
    ):

        print(
            "⚡ EXECUTOR EVENT:",
            event,
        )

        if event["type"] == "tool_end":

            tool_name = event["tool"]
            tool_result = event["result"]

            results[tool_name] = tool_result

            print(
                f"✅ TOOL COMPLETED: {tool_name}"
            )

    print(
        "📦 UPDATED TOOL RESULTS:",
        results,
    )

    print("=" * 60)
    print("✅ EXECUTOR NODE FINISHED")
    print("=" * 60 + "\n")

    return {
        "tool_results": results,
    }

# ============================================================

# RESPONDER NODE

# ============================================================

def responder_node(
state: AgentState,
):
    print("\n" + "=" * 60)
    print("🚀 RESPONDER NODE REACHED")
    print("=" * 60)

    writer = get_stream_writer()

    answer = ""

    tool_results = state.get(
        "tool_results",
        {},
    )

    print("📦 TOOL RESULTS:")
    print(tool_results)

# ========================================================
# RAG RESULT
# ========================================================
#
# search_knowledge_base already generates a grounded
# answer. Therefore we do NOT call stream_response()
# again, otherwise the answer may be generated twice.
#
# ========================================================

    if isinstance(tool_results, dict):

        rag_result = tool_results.get(
            "search_knowledge_base"
        )

        if rag_result:

            print("\n" + "-" * 60)
            print("🧠 RAG RESULT DETECTED")
            print("✅ SKIPPING stream_response()")
            print("-" * 60)

            print(
                f"📝 RAG Answer:\n{rag_result}"
            )

            answer = rag_result

            writer({
                "type": "token",
                "content": answer,
            })

            writer({
                "type": "complete",
                "answer": answer,
            })

            print(
                "✅ RAG answer streamed directly to client"
            )

            print(
                "=" * 60 + "\n"
            )

            return {
                "answer": answer,
            }

    # ========================================================
    # NORMAL TOOL RESULTS
    # ========================================================

    print("\n" + "-" * 60)
    print("🤖 NO RAG RESULT")
    print("➡️ Calling stream_response()")
    print("-" * 60)

    for token in stream_response(
        state["prompt"],
        tool_results,
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

    print(
        f"📝 Final responder answer:\n{answer}"
    )

    print(
        "✅ Response streamed through stream_response()"
    )

    print(
        "=" * 60 + "\n"
    )

    return {
        "answer": answer,
    }