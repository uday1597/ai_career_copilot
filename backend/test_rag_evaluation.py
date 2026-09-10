from pprint import pprint

from app.services.rag.evaluation.rag_evaluator import (
    RAGEvaluator,
)


def main():

    evaluator = RAGEvaluator()

    question = """
    What skills is the candidate missing
    for the target AI Engineer job?
    """

    context = """
    The candidate has strong React and Node.js skills.

    The target job requires LangGraph,
    MCP and RAG evaluation.

    The candidate has limited experience
    with Kubernetes.
    """

    answer = """
    The candidate is missing experience with
    MCP and RAG evaluation.
    """

    result = evaluator.evaluate(
        question=question,
        context=context,
        answer=answer,
    )

    print(
        "\n========== RAG EVALUATION ==========\n"
    )

    pprint(result)

    print(
        "\n====================================\n"
    )


if __name__ == "__main__":
    main()