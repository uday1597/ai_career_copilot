import json

from app.services.openai_service import client


def analyze_job(description: str):

    prompt = f"""
You are an expert technical recruiter.

Extract all technologies and skills from this job description.

Return ONLY valid JSON.

Schema:

{{
  "technologies": []
}}

Job Description:

{description}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    cleaned = (
        response.output_text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return json.loads(cleaned)