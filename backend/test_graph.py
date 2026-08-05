from app.db.database import SessionLocal

from app.services.agent.graph.graph import graph
from app.services.agent.graph.config import get_graph_config
from app.services.agent.runtime import AgentRuntime


def main():

    db = SessionLocal()

    runtime = AgentRuntime(db)

    for event in runtime.run(
        "Generate roadmap"
    ):
        print(event)
    # db = SessionLocal()

    # state = {
    #     "prompt": "Generate a learning roadmap for becoming a Python AI Engineer.",
    #     "db": db,
    # }

    # for event in graph.stream(
    #     state,
    #     config=get_graph_config("test-thread"),
    # ):
    #     print(event)

    # print("\n===== PLAN =====")
    # print(result["plan"])

    # print("\n===== TOOL RESULTS =====")
    # print(result["tool_results"])

    # print("\n===== ANSWER =====")
    # print(result["answer"])

    db.close()


if __name__ == "__main__":
    main()