from app.db.database import SessionLocal

from app.services.rag.evaluation.evaluation_runner import (
    RAGEvaluationRunner,
)


def main():

    db = SessionLocal()

    try:

        runner = RAGEvaluationRunner()

        results = runner.run(db)

        summary = runner.summarize(results)

        print("\n==============================")
        print("RAG REGRESSION TEST")
        print("==============================")

        for result in results:

            print("\n------------------------------")

            print(
                f"Test: {result['id']}"
            )

            print(
                f"Question: {result['question']}"
            )

            print(
                f"Expected: "
                f"{result['expected_sources']}"
            )

            print(
                f"Retrieved: "
                f"{result['retrieved_sources']}"
            )

            print(
                f"Precision: "
                f"{result['precision']:.2f}"
            )

            print(
                f"Recall: "
                f"{result['recall']:.2f}"
            )

            print(
                f"F1: "
                f"{result['f1']:.2f}"
            )

            print(
                f"Judge: "
                f"{result['judge']}"
            )

        print("\n==============================")
        print("SUMMARY")
        print("==============================")

        for key, value in summary.items():

            print(
                f"{key}: {value:.2f}"
            )


    finally:

        db.close()


if __name__ == "__main__":
    main()