import json

from app.services.ingestion.openai_service import client
from app.services.ai.embedding_service import EmbeddingService

def analyze_resume(text: str) -> dict:

    prompt = f"""
You are an expert technical recruiter.

Extract all technologies, tools, programming languages,
frameworks, cloud platforms, databases, AI tools,
libraries, and platforms mentioned in the resume.

Return ONLY valid JSON.

Schema:

{{
  "summary": "professional summary",
  "technologies": []
}}

Resume:

{text}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )
    print(response.output_text)
    result = response.output_text
    embedding_service = EmbeddingService()
    embedding = embedding_service.create_embedding(result)
    print(embedding)
    return json.loads(result), embedding