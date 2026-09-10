from app.services.rag.evaluation.llm_evaluator import (
    LLMEvaluator,
)


def main():

    evaluator = LLMEvaluator()

    question = """
    What skills is the candidate missing
    for the target AI Engineer job?
    """

    context = """
The candidate enjoys watching movies.

The candidate owns several plants.

The frontend uses Tailwind CSS.

The candidate prefers dark mode.
"""

    result = evaluator.evaluate_context_relevance(
        question=question,
        context=context,
    )

    print(
        "\n========== CONTEXT RELEVANCE =========="
    )

    print(
        f"\nScore: {result['score']}"
    )

    print(
        f"\nReason: {result['reason']}"
    )

    print(
        "\n========================================\n"
    )


if __name__ == "__main__":
    main()