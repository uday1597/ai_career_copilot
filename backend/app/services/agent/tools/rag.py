from app.services.rag.rag_service import RAGService


rag_service = RAGService()


def search_knowledge_base_tool(
    db,context,previous_results,
    question: str,
):
    """
    Search Career Copilot's knowledge base
    using the production RAG pipeline.
    """

    return rag_service.ask(
        db=db,
        question=question,
    )