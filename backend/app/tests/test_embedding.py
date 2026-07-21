from app.services.ai.embedding_service import EmbeddingService

service = EmbeddingService()

vector = service.create_embedding(
    "Python FastAPI OpenAI LangGraph"
)

print(len(vector))
print(vector[:5])