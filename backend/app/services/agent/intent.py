from app.services.ingestion.openai_service import client


def classify_intent(
    prompt: str,
) -> str:

    response = client.responses.create(

        model="gpt-4.1-mini",

        input=f"""
Classify the user's message into exactly ONE category.

Categories:

CASUAL
- greetings
- hello
- hi
- thanks
- goodbye
- small talk

GENERAL
- general questions
- technical explanations
- conceptual questions
- questions that do not require Career Copilot user data

TOOL
- questions requiring the user's Career Copilot data
- resume information
- dashboard information
- job match information
- roadmap information
- assessment information
- personalized career information

Examples:

User: hi
Category: CASUAL

User: hello
Category: CASUAL

User: thanks
Category: CASUAL

User: what is RAG?
Category: GENERAL

User: explain LangGraph
Category: GENERAL

User: what is my dashboard status?
Category: TOOL

User: what skills am I missing?
Category: TOOL

User: show my learning roadmap
Category: TOOL

Return ONLY the category.

User message:

{prompt}
""",
    )

    result = (
        response.output_text
        .strip()
        .upper()
    )

    if result not in {
        "CASUAL",
        "GENERAL",
        "TOOL",
    }:

        return "GENERAL"

    return result