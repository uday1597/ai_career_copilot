import json

from app.services.ingestion.openai_service import client


def generate_assessment(week):

    prompt = f"""
    You are a Senior Software Engineer and Technical Interviewer.

    Generate an assessment based on the learning roadmap below.

    Week:
    {week["week"]}

    Focus:
    {week["focus"]}

    Topics:
    {", ".join(week["topics"])}

    Mini Project:
    {week["mini_project"]}

    Return ONLY valid JSON.

    {{
        "title": "",
        "estimated_duration": "",
        "difficulty": "",

        "mcqs": [
            {{
                "id": 1,
                "question": "",
                "options": [
                    "",
                    "",
                    "",
                    ""
                ],
                "answer": 0,
                "explanation": ""
            }}
        ],

        "coding": [
            {{
                "id": 1,
                "title": "",
                "question": "",
                "difficulty": "",
                "expected_skills": [],
                "hints": []
            }}
        ],

        "scenario": [
            {{
                "id": 1,
                "question": "",
                "expected_points": [],
                "sample_answer": ""
            }}
        ]
    }}

    Rules

    1. Generate exactly

    - 5 MCQs
    - 2 Coding Questions
    - 1 Scenario Question

    2. Questions must evaluate practical industry knowledge.

    3. MCQs should include realistic distractors.

    4. Coding questions should resemble interview questions asked by Microsoft, Amazon, Google, Atlassian, Thoughtworks, etc.

    5. Coding questions must not include complete solutions.

    6. Scenario questions should assess architectural thinking and problem solving.

    7. Explanations should be concise.

    8. Output ONLY JSON.
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
    )

    content = (
        response.output_text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return json.loads(content)