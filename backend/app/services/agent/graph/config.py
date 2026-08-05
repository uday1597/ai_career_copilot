from langchain_core.runnables import RunnableConfig


def get_graph_config(thread_id: str) -> RunnableConfig:
    return {
        "configurable": {
            "thread_id": thread_id,
        }
    }