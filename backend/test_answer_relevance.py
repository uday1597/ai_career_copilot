from app.services.rag.evaluation.llm_evaluator import (
    LLMEvaluator,
)


def main():

    evaluator = LLMEvaluator()

    question = """
    What skills is the candidate missing
    for the target AI Engineer job?
    """

    answer = """
The candidate has 7 years of experience
building React applications.
"""

    result = evaluator.evaluate_answer_relevance(
        question=question,
        answer=answer,
    )

    print(
        "\n========== ANSWER RELEVANCE =========="
    )

    print(
        f"\nScore: {result['score']}"
    )

    print(
        f"\nReason: {result['reason']}"
    )

    print(
        "\n=======================================\n"
    )


if __name__ == "__main__":
    main()