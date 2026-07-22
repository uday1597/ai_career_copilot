import json

from openai import OpenAI

from app.core.config import settings
from app.services.ingestion.openai_service import client


def explain_match(
    resume_summary: str,
    resume_technologies: list,
    job_title: str,
    job_description: str,
    job_technologies: list,
    match_score: int,
):
    prompt = f"""
    You are an experienced AI technical recruiter.

    Analyze the following resume and job.

    Resume Summary:
    {resume_summary}

    Resume Technologies:
    {", ".join(resume_technologies)}

    Job Title:
    {job_title}

    Job Description:
    {job_description}

    Job Technologies:
    {", ".join(job_technologies)}

    Semantic Match Score:
    {match_score}%

    Return ONLY valid JSON.

    {{
        "summary": "...",

        "strengths": [
            "...",
            "..."
        ],

        "missing_skills": [
            "...",
            "..."
        ],

        "recommendations": [
            "...",
            "..."
        ]
    }}
    """
    response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt,
    )
    content = response.output_text.strip()

    content = content.replace("```json", "")
    content = content.replace("```", "")

    return json.loads(content)