import json

from app.services.openai_service import client


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

    return json.loads(result)