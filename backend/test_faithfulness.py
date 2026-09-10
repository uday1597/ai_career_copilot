from app.services.rag.evaluation.llm_evaluator import (
    LLMEvaluator,
)


def main():

    evaluator = LLMEvaluator()

    context = """
    The candidate has experience with
    React, Node.js and MongoDB.
    """

    answer = """
    The candidate has experience with
    React, Node.js and MongoDB.
    """

    result = evaluator.evaluate_faithfulness(
        question="What technologies does the candidate know?",
        context=context,
        answer=answer,
    )

    print("\n========== FAITHFULNESS ==========")

    print(
        f"\nScore: {result['score']}"
    )

    print(
        f"\nReason: {result['reason']}"
    )

    print(
        "\n==================================\n"
    )


if __name__ == "__main__":
    main()