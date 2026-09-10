import json

from app.services.ingestion.openai_service import client


class LLMJudge:

    def evaluate(
        self,
        question: str,
        context: str,
        answer: str,
    ) -> dict:

        prompt = f"""
You are an evaluator for a Retrieval-Augmented
Generation system.

Evaluate the answer using ONLY the supplied
question and context.

QUESTION
--------
{question}

CONTEXT
-------
{context}

ANSWER
------
{answer}

Evaluate the following:

1. Faithfulness

Is every factual claim in the answer
supported by the context?

2. Answer Relevance

Does the answer directly answer the question?

3. Context Relevance

Does the supplied context contain information
useful for answering the question?

Return ONLY valid JSON.

Format:

{{
    "faithfulness": 0.0,
    "answer_relevance": 0.0,
    "context_relevance": 0.0,
    "reason": ""
}}

Scores must be between 0 and 1.
"""

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt,
        )

        content = response.output_text.strip()

        content = content.replace(
            "```json",
            "",
        )

        content = content.replace(
            "```",
            "",
        )

        return json.loads(content)