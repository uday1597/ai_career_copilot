from app.services.rag.retrieval_service import (
    RetrievalService,
)

from app.services.rag.evaluation.metrics import (
    calculate_precision,
    calculate_recall,
    calculate_f1,
)


class RetrievalEvaluator:

    def __init__(self):

        self.retriever = RetrievalService()

    def evaluate(
        self,
        db,
        question: str,
        expected_sources: list[str],
        top_k: int = 5,
    ) -> dict:

        documents = (
            self.retriever.hybrid_search(
                db,
                question,
                top_k,
            )
        )

        retrieved_sources = [
            document.document_type
            for document in documents
        ]

        precision = calculate_precision(
            retrieved_sources,
            expected_sources,
        )

        recall = calculate_recall(
            retrieved_sources,
            expected_sources,
        )
        f1 = calculate_f1(
            precision,
            recall,
        )
        return {
            "question": question,
            "expected_sources": expected_sources,
            "retrieved_sources": retrieved_sources,
            "precision": precision,
            "recall": recall,
            "f1":f1,
        }