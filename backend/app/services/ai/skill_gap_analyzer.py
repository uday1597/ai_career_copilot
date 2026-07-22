import json

from openai import OpenAI

from app.core.config import settings
from app.services.ingestion.openai_service import client

def analyze_skill_gap(
    resume_summary: str,
    resume_technologies: list,
    job_title: str,
    job_description: str,
    job_technologies: list,
):
    prompt = f"""
    You are an experienced AI career coach.

    Compare the candidate's resume with the job.

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

    Return ONLY valid JSON.

    {{
        "priority_skills": [
            {{
                "skill": "",
                "reason": "",
                "difficulty": "",
                "estimated_learning_time": ""
            }}
        ],

        "nice_to_have": [
            {{
                "skill": "",
                "reason": ""
            }}
        ],

        "learning_order": [
            "Skill 1",
            "Skill 2",
            "Skill 3"
        ]
    }}

    Rules:
    - Recommend only skills missing from the resume.
    - Prioritize the most impactful skills first.
    - estimated_learning_time should be realistic (e.g. "3 days", "2 weeks", "1 month").
    - difficulty should be Easy, Medium, or Hard.
    """
    response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt,
    )
    content = response.output_text.strip()

    content = content.replace("```json", "")
    content = content.replace("```", "")

    return json.loads(content)