from app.services.rag.rag_service import RAGService
from app.services.rag.evaluation.evaluation_dataset import (
    EVALUATION_DATASET,
)


class RAGEvaluationRunner:

    def __init__(self):

        self.rag = RAGService()

    def run(self, db):

        results = []

        for test_case in EVALUATION_DATASET:

            question = test_case["question"]

            expected_sources = set(
                test_case["expected_sources"]
            )

            response = self.rag.ask(
                db=db,
                question=question,
                evaluate=True,
            )

            retrieved_sources = set(
                response.get(
                    "retrieved_sources",
                    [],
                )
            )

            true_positive = (
                expected_sources
                & retrieved_sources
            )

            precision = (
                len(true_positive)
                / len(retrieved_sources)
                if retrieved_sources
                else 0
            )

            recall = (
                len(true_positive)
                / len(expected_sources)
                if expected_sources
                else 0
            )

            f1 = (
                2 * precision * recall
                / (precision + recall)
                if precision + recall
                else 0
            )

            results.append(
                {
                    "id": test_case["id"],
                    "question": question,
                    "expected_sources": list(
                        expected_sources
                    ),
                    "retrieved_sources": list(
                        retrieved_sources
                    ),
                    "precision": precision,
                    "recall": recall,
                    "f1": f1,
                    "judge": response.get(
                        "judge",
                        {},
                    ),
                }
            )

        return results

    def summarize(self, results):

        if not results:
            return {}

        average_precision = (
            sum(
                result["precision"]
                for result in results
            )
            / len(results)
        )

        average_recall = (
            sum(
                result["recall"]
                for result in results
            )
            / len(results)
        )

        average_f1 = (
            sum(
                result["f1"]
                for result in results
            )
            / len(results)
        )

        faithfulness = [
            result["judge"]["faithfulness"]
            for result in results
            if result.get("judge")
            and "faithfulness"
            in result["judge"]
        ]

        answer_relevance = [
            result["judge"]["answer_relevance"]
            for result in results
            if result.get("judge")
            and "answer_relevance"
            in result["judge"]
        ]

        context_relevance = [
            result["judge"]["context_relevance"]
            for result in results
            if result.get("judge")
            and "context_relevance"
            in result["judge"]
        ]

        return {
            "average_precision": average_precision,
            "average_recall": average_recall,
            "average_f1": average_f1,

            "average_faithfulness": (
                sum(faithfulness)
                / len(faithfulness)
                if faithfulness
                else 0
            ),

            "average_answer_relevance": (
                sum(answer_relevance)
                / len(answer_relevance)
                if answer_relevance
                else 0
            ),

            "average_context_relevance": (
                sum(context_relevance)
                / len(context_relevance)
                if context_relevance
                else 0
            ),
        }

    def check_thresholds(summary):

        failures = []

        if summary["average_precision"] < 0.70:
            failures.append("Precision below threshold")

        if summary["average_recall"] < 0.80:
            failures.append("Recall below threshold")

        if summary["average_f1"] < 0.75:
            failures.append("F1 below threshold")

        if summary["average_faithfulness"] < 0.85:
            failures.append(
                "Faithfulness below threshold"
            )

        if summary["average_answer_relevance"] < 0.80:
            failures.append(
                "Answer relevance below threshold"
            )

        if summary["average_context_relevance"] < 0.80:
            failures.append(
                "Context relevance below threshold"
            )

        return {
            "passed": not failures,
            "failures": failures,
        }