from app.db.database import SessionLocal

from app.services.rag.evaluation.retrieval_evaluator import (
    RetrievalEvaluator,
)


def main():

    db = SessionLocal()

    try:

        evaluator = RetrievalEvaluator()

        result = evaluator.evaluate(
            db=db,
            question="What skills are missing for the target job?",
            expected_sources=[
                "resume",
                "job",
            ],
            top_k=5,
        )

        print("\n========== RAG RETRIEVAL EVALUATION ==========")

        print(
            f"\nQuestion:\n"
            f"{result['question']}"
        )

        print(
            f"\nExpected sources:\n"
            f"{result['expected_sources']}"
        )

        print(
            f"\nRetrieved sources:\n"
            f"{result['retrieved_sources']}"
        )

        print(
            f"\nPrecision: "
            f"{result['precision']:.2f}"
        )

        print(
            f"Recall: "
            f"{result['recall']:.2f}"
        )
        print(
            f"F1 Score: "
            f"{result['f1']:.2f}"
        )

        print(
            "\n===============================================\n"
        )

    finally:

        db.close()


if __name__ == "__main__":
    main()