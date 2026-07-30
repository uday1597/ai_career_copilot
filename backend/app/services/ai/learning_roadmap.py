import json

from app.services.ingestion.openai_service import client


def generate_learning_roadmap(
    match_score: int,
    matching_technologies: list,
    missing_technologies: list,
    ai_explanation: dict,
):
    prompt = f"""
    You are an experienced AI career mentor.

    A candidate has already been evaluated against a job.

    Match Score:
    {match_score}%

    Matching Technologies:
    {", ".join(matching_technologies)}

    Missing Technologies:
    {", ".join(missing_technologies)}

    AI Match Summary:
    {ai_explanation.get("summary", "")}

    Candidate Strengths:
    {chr(10).join("- " + s for s in ai_explanation.get("strengths", []))}

    Missing Skills:
    {chr(10).join("- " + s for s in ai_explanation.get("missing_skills", []))}

    Career Recommendations:
    {chr(10).join("- " + r for r in ai_explanation.get("recommendations", []))}

    Create a practical personalized roadmap.

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
    - Focus ONLY on the missing skills.
    - Do NOT include technologies the candidate already knows.
    - Order topics from beginner to advanced.
    - Every week must contain a practical mini project.
    - Resources should be high-quality free documentation such as Microsoft Learn, OpenAI Docs, LangChain Docs, FastAPI Docs, Azure Learn, Kubernetes Docs, etc.
    - The roadmap should directly improve the candidate's match score.
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
    )

    content = response.output_text.strip()
    content = content.replace("```json", "")
    content = content.replace("```", "")

    return json.loads(content)

def generate_learning_roadmap_stream(
    match_score: int,
    matching_technologies: list,
    missing_technologies: list,
    ai_explanation: dict,
):
    prompt = f"""
    You are an experienced AI career mentor.

    A candidate has already been evaluated against a job.

    Match Score:
    {match_score}%

    Matching Technologies:
    {", ".join(matching_technologies)}

    Missing Technologies:
    {", ".join(missing_technologies)}

    AI Match Summary:
    {ai_explanation.get("summary", "")}

    Candidate Strengths:
    {chr(10).join("- " + s for s in ai_explanation.get("strengths", []))}

    Missing Skills:
    {chr(10).join("- " + s for s in ai_explanation.get("missing_skills", []))}

    Career Recommendations:
    {chr(10).join("- " + r for r in ai_explanation.get("recommendations", []))}

    Create a practical personalized roadmap.

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
    - Focus ONLY on the missing skills.
    - Do NOT include technologies the candidate already knows.
    - Order topics from beginner to advanced.
    - Every week must contain a practical mini project.
    - Resources should be high-quality free documentation.
    - The roadmap should directly improve the candidate's match score.
    """

    full_text = ""

    with client.responses.stream(
        model="gpt-4.1-mini",
        input=prompt,
    ) as stream:

        for event in stream:

            if event.type == "response.output_text.delta":

                full_text += event.delta

                yield {
                    "type": "token",
                    "content": event.delta,
                }

        stream.until_done()

    yield {
        "type": "complete",
        "content": full_text,
    }