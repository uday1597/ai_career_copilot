from openai import OpenAI

from app.core.config import settings
from app.services.ingestion.openai_service import client

class EmbeddingService:

    def __init__(self):


        self.model = settings.openai_embedding_model

    def create_embedding(
        self,
        text: str
    ) -> list[float]:

        response = client.embeddings.create(
            model=self.model,
            input=text
        )

        return response.data[0].embedding