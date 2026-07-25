import json

from app.services.ingestion.openai_service import client


def evaluate_assessment(
    assessment,
    mcq_score,
    coding_answers,
    scenario_answer,
):

    prompt = f"""
You are a Senior Software Engineering Interviewer.

Candidate completed an assessment.

MCQ Score

{mcq_score}/5

Coding Questions

{coding_answers}

Scenario Answer

{scenario_answer}

Return ONLY JSON.

{{
    "coding_score": 0,
    "scenario_score": 0,
    "overall_score": 0,

    "strengths":[
        ""
    ],

    "weaknesses":[
        ""
    ],

    "recommendations":[
        ""
    ],

    "summary":"",

    "next_action":""
}}

Rules

Coding score out of 100.

Scenario score out of 100.

Overall score should combine

MCQ

Coding

Scenario

Do not explain outside JSON.
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
    )

    return json.loads(
        response.output_text
        .replace("```json", "")
        .replace("```", "")
    )