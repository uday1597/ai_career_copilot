from app.services.ingestion.openai_service import client

from app.services.rag.retrieval_service import RetrievalService
from app.services.rag.context_compression_service import (
    ContextCompressionService,
)
from app.services.rag.query_analyzer import QueryAnalyzer
from app.services.rag.query_rewriter import QueryRewriter
from app.services.rag.reranker_service import ReRankerService
from app.services.rag.context_builder import ContextBuilder
from app.services.rag.evaluation.rag_evaluator import (
    RAGEvaluator,
)
from app.services.rag.evaluation.llm_judge import (
    LLMJudge,
)

class RAGService:

    def __init__(self):

        self.retriever = RetrievalService()

        self.compressor = (
            ContextCompressionService()
        )

        self.query_analyzer = QueryAnalyzer()

        self.rewriter = QueryRewriter()

        self.reranker = ReRankerService()

        self.context_builder = ContextBuilder()

        self.evaluator = RAGEvaluator()
        self.judge = LLMJudge()
    def ask(
        self,
        db,
        question: str,
        top_k: int = 5,
        document_type: str | None = None,
        history: str | None = None,
        evaluate: bool = False,
    ) -> str | dict:

        print("\n" + "=" * 60)
        print("🚀 RAGService.ask() CALLED")
        print(f"❓ Question: {question}")
        print("=" * 60)

        # -------------------------------------------------
        # 1. Rewrite question
        # -------------------------------------------------

        rewritten_question = self.rewriter.rewrite(
            history,
            question,
        )
        print("✅ Step 1: Query rewritten")
        print(f"   Rewritten: {rewritten_question}")
        # -------------------------------------------------
        # 2. Detect document type
        # -------------------------------------------------

        detected_document_type = (
            document_type
            or self.query_analyzer.detect_document_type(
                rewritten_question
            )
        )

        # -------------------------------------------------
        # 3. Hybrid retrieval
        # -------------------------------------------------

        documents = self.retriever.hybrid_search(
            db,
            rewritten_question,
            top_k * 3,
            document_type=detected_document_type,
        )
        print(f"✅ Step 3: Retrieved {len(documents)} documents")
        # -------------------------------------------------
        # 4. Reranking
        # -------------------------------------------------

        documents = self.reranker.rerank(
            rewritten_question,
            documents,
            top_k,
        )
        print(f"✅ Step 4: Reranked documents: {len(documents)}")
        retrieved_sources = [
            document.source
            for document in documents
        ]

        # -------------------------------------------------
        # 5. No documents
        # -------------------------------------------------

        if not documents:

            answer = (
                "I couldn't find relevant information "
                "in the knowledge base."
            )

            if not evaluate:
                return answer

            return {
                "answer": answer,
                "evaluation": {},
                "judge": {},
                "rewritten_question": rewritten_question,
                "document_type": detected_document_type,
                "retrieved_sources": [],
            }

        # -------------------------------------------------
        # 6. Context compression
        # -------------------------------------------------

        compressed_documents = self.compressor.compress(
            rewritten_question,
            documents,
        )
        print(
            f"✅ Step 6: Compressed documents: "
            f"{len(compressed_documents)}"
        )
        # -------------------------------------------------
        # 7. Compression failure
        # -------------------------------------------------

        if not compressed_documents:

            answer = (
                "I couldn't find relevant information "
                "in the retrieved documents."
            )

            if not evaluate:
                return answer

            return {
                "answer": answer,
                "evaluation": {},
                "judge": {},
                "rewritten_question": rewritten_question,
                "document_type": detected_document_type,
                "retrieved_sources": retrieved_sources,
            }

        # -------------------------------------------------
        # 8. Build context
        # -------------------------------------------------

        context = self.context_builder.build(
            compressed_documents
        )

        # -------------------------------------------------
        # 9. Grounded prompt
        # -------------------------------------------------

        prompt = f"""
    You are Career Copilot, an AI career assistant.

    Answer the user's question using ONLY the
    provided context.

    IMPORTANT RULES:

    1. Do not invent information.

    2. If the answer is not supported by the
    supplied context, say:

    "I couldn't find that information
    in the knowledge base."

    3. Cite factual claims using the source number.

    Example:

    The candidate has experience with React.
    [SOURCE 1]

    4. Do not create citations that do not exist.

    5. If multiple sources support a claim,
    cite all relevant sources.

    6. Keep the answer concise and useful.

    ---

    CONTEXT

    {context}

    ---

    USER QUESTION

    {rewritten_question}

    ---

    ANSWER
    """

        # -------------------------------------------------
        # 10. Generate answer
        # -------------------------------------------------
        print("🤖 Sending grounded context to GPT-5...")
        response = client.responses.create(
            model="gpt-5",
            input=prompt,
        )

        answer = response.output_text
        print("✅ GPT-5 response received")
        print(f"📝 Answer: {answer[:200]}...")
        # -------------------------------------------------
        # 11. Normal response
        # -------------------------------------------------

        if not evaluate:
            return answer

        # -------------------------------------------------
        # 12. RAG evaluation
        # -------------------------------------------------

        evaluation = self.evaluator.evaluate(
            question=question,
            context=context,
            answer=answer,
        )

        # -------------------------------------------------
        # 13. LLM Judge
        # -------------------------------------------------

        judge_evaluation = self.judge.evaluate(
            question=question,
            context=context,
            answer=answer,
        )

        # -------------------------------------------------
        # 14. Evaluation response
        # -------------------------------------------------

        return {
            "answer": answer,

            "evaluation": evaluation,

            "judge": judge_evaluation,

            "rewritten_question": rewritten_question,

            "document_type": detected_document_type,

            "retrieved_sources": retrieved_sources,
        }