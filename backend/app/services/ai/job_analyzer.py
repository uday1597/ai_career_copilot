import json

from app.services.ingestion.openai_service import client
from app.services.ai.embedding_service import EmbeddingService


def analyze_job(job_text: str):

    prompt = f"""
You are an expert technical recruiter.

Extract all technologies and technical skills from the following job description.

Return ONLY valid JSON.

Schema:

{{
    "technologies": []
}}

Job Details:

{job_text}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
    )

    cleaned = (
        response.output_text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    analysis = json.loads(cleaned)

    embedding = EmbeddingService().create_embedding(
        cleaned
    )

    return analysis, embedding