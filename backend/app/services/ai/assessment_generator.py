import json

from app.services.ingestion.openai_service import client

def generate_assessment(
    skill: str
):
    prompt = f"""
    You are a Senior AI Engineer.

    Create an assessment for:

    {skill}

    Return ONLY JSON.

    {{
        "mcqs":[
            {{
                "question":"",
                "options":[
                    "",
                    "",
                    "",
                    ""
                ],
                "answer":"",
                "explanation":""
            }}
        ],

        "coding":[
            {{
                "question":"",
                "difficulty":""
            }}
        ],

        "scenario":[
            {{
                "question":"",
                "expected_points":[]
            }}
        ]
    }}

    Rules

    Generate

    5 MCQs

    2 Coding Questions

    1 Scenario Question.

    The questions should evaluate real-world industry knowledge.
    """
    response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
    )

    content = (
        response.output_text
        .replace("```json", "")
        .replace("```", "")
    )

    return json.loads(content)