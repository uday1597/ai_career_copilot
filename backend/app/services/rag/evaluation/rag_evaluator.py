from app.services.rag.evaluation.llm_evaluator import (
    LLMEvaluator,
)


class RAGEvaluator:

    def __init__(self):

        self.llm_evaluator = LLMEvaluator()

    def evaluate(
        self,
        question: str,
        context: str,
        answer: str,
    ) -> dict:

        context_relevance = (
            self.llm_evaluator
            .evaluate_context_relevance(
                question=question,
                context=context,
            )
        )

        faithfulness = (
            self.llm_evaluator
            .evaluate_faithfulness(
                question=question,
                context=context,
                answer=answer,
            )
        )

        answer_relevance = (
            self.llm_evaluator
            .evaluate_answer_relevance(
                question=question,
                answer=answer,
            )
        )

        evaluation = {
            "context_relevance": context_relevance,
            "faithfulness": faithfulness,
            "answer_relevance": answer_relevance,
        }

        evaluation["overall_score"] = (
            self.calculate_overall_score(
                evaluation
            )
        )

        return evaluation
    def calculate_overall_score(
        self,
        evaluation: dict,
    ) -> float:

        context_score = (
            evaluation[
                "context_relevance"
            ]["score"]
        )

        faithfulness_score = (
            evaluation[
                "faithfulness"
            ]["score"]
        )

        answer_score = (
            evaluation[
                "answer_relevance"
            ]["score"]
        )

        return (
            context_score
            + faithfulness_score
            + answer_score
        ) / 3