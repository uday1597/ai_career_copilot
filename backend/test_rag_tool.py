from app.db.database import SessionLocal

from app.services.agent.tools.rag import (
    search_knowledge_base_tool,
)


def main():

    db = SessionLocal()

    try:

        result = search_knowledge_base_tool(
            db=db,
            question="What skills are missing for the target job?",
        )

        print("\n==============================")
        print("RAG TOOL RESULT")
        print("==============================")

        print(result)

    finally:

        db.close()


if __name__ == "__main__":
    main()