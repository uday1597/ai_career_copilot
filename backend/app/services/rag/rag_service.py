from app.services.ingestion.openai_service import client
from app.services.rag.retrieval_service import RetrievalService
from app.services.rag.context_compression_service import (
    ContextCompressionService,
)
from app.services.rag.query_analyzer import QueryAnalyzer
from app.services.rag.query_rewriter import QueryRewriter
from app.services.rag.reranker_service import ReRankerService

class RAGService:

    def __init__(self):

        self.retriever = RetrievalService()
        self.compressor = ContextCompressionService()
        self.query_analyzer = QueryAnalyzer()
        self.rewriter = QueryRewriter()
        self.reranker = ReRankerService()

    def ask(
        self,
        db,
        question: str,
        top_k: int = 5,
        document_type: str | None = None,
        history: str | None = None,
    ) -> str:

        rewritten = self.rewriter.rewrite(
            history,
            question,
        )

        documents = self.retriever.hybrid_search(
            db,
            question,
            top_k * 3,
            document_type=document_type,
        )

        documents = self.reranker.rerank(
            question,
            documents,
            top_k,
        )

        if not documents:

            return "No relevant information found."

        context = self.compressor.compress(
            question,
            documents,
        )

        prompt = f"""
            You are an AI assistant.

            Answer ONLY using the supplied context.

            If the answer is not contained in the context,
            reply:

            "I couldn't find that information."

            ----------------------

            Context

            {context}

            ----------------------

            Question

            {question}
            """

        response = client.responses.create(

            model="gpt-5",

            input=prompt,

        )

        return response.output_text