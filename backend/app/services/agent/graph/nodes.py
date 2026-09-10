from langgraph.runtime import Runtime

from app.services.agent.context import AgentContext
from app.services.agent.executor import AgentExecutor
from app.services.agent.planner import create_plan
from app.services.agent.responder import stream_response

from .runtime_context import AgentRuntimeContext
from .state import AgentState

from langgraph.config import get_stream_writer
from app.services.agent.intent import classify_intent

async def intent_node(state: AgentState):
    print("🔥🔥🔥🔥 INTENT NODE HIT")
    print("PROMPT:", state["prompt"])
    intent = classify_intent(
        state["prompt"]
    )

    print("🔥🔥🔥🔥 INTENT RESULT:", intent)

    return {
        "intent": intent
    }
async def planner_node(
    state: AgentState,
):
    print("🔥🔥🔥🔥 PLANNER NODE HIT")
    print("PROMPT:", state["prompt"])
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

    results = state.get(
        "tool_results",
        {},
    ).copy()

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

    print("\n" + "=" * 60)
    print("🚀 RESPONDER NODE REACHED")
    print("=" * 60)

    writer = get_stream_writer()

    answer = ""

    tool_results = state.get("tool_results", {})

    print("📦 Tool results:")
    print(tool_results)

    # -------------------------------------------------
    # RAG already generated the final grounded answer
    # -------------------------------------------------

    if isinstance(tool_results, dict):

        rag_result = tool_results.get(
            "search_knowledge_base"
        )

        if rag_result:

            print("\n" + "-" * 60)
            print("🧠 RAG RESULT DETECTED")
            print("✅ Skipping stream_response()")
            print("-" * 60)

            print(f"📝 RAG Answer:\n{rag_result}")

            answer = rag_result

            writer({
                "type": "token",
                "content": answer,
            })

            writer({
                "type": "complete",
                "answer": answer,
            })

            print("✅ RAG answer streamed directly to client")
            print("=" * 60 + "\n")

            return {
                "answer": answer,
            }

    # -------------------------------------------------
    # Normal tools → responder LLM
    # -------------------------------------------------

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

    print(f"📝 Final responder answer:\n{answer}")
    print("✅ Response streamed through stream_response()")
    print("=" * 60 + "\n")

    return {
        "answer": answer,
    }