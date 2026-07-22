import json

from app.services.ingestion.openai_service import client

def generate_learning_roadmap(
    resume_summary: str,
    resume_technologies: list,
    job_title: str,
    job_description: str,
    job_technologies: list,
):
    prompt = f"""
    You are an experienced AI career mentor.

    Create a personalized learning roadmap.

    Candidate Resume Summary:
    {resume_summary}

    Candidate Technologies:
    {", ".join(resume_technologies)}

    Target Job:
    {job_title}

    Job Description:
    {job_description}

    Target Technologies:
    {", ".join(job_technologies)}

    Return ONLY valid JSON.

    {{
        "estimated_completion": "",
        "weeks": [
            {{
                "week": 1,
                "focus": "",
                "topics": [],
                "mini_project": "",
                "resources": []
            }}
        ]
    }}

    Rules:
    - Maximum 6 weeks.
    - Focus only on missing skills.
    - Order topics from beginner to advanced.
    - Each week should include a practical mini project.
    - Resources should be generic names (Microsoft Learn, LangChain Docs, OpenAI Docs, FastAPI Docs, etc.).
    """
    response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt,
    )
    content = response.output_text.strip()

    content = content.replace("```json", "")
    content = content.replace("```", "")

    return json.loads(content)