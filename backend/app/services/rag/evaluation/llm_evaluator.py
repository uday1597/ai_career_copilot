import json

from app.services.ingestion.openai_service import client


class LLMEvaluator:

    def evaluate_faithfulness(
        self,
        question: str,
        context: str,
        answer: str,
    ) -> dict:

        prompt = f"""
You are evaluating the faithfulness of an AI-generated
answer in a Retrieval-Augmented Generation system.

Question:
{question}

Retrieved Context:
{context}

Generated Answer:
{answer}

Determine whether the answer is supported by the
retrieved context.

Return ONLY valid JSON:

{{
    "score": 0,
    "reason": ""
}}

Scoring:

0 = Answer is not supported by the context.

0.5 = Answer is partially supported.

1 = Answer is fully supported.

Do not use outside knowledge.
Judge ONLY based on the supplied context.
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

    def evaluate_context_relevance(
        self,
        question: str,
        context: str,
    ) -> dict:

        prompt = f"""
    You are evaluating the relevance of retrieved context
    in a Retrieval-Augmented Generation system.

    Question:
    {question}

    Retrieved Context:
    {context}

    Determine how relevant the retrieved context is
    for answering the question.

    Return ONLY valid JSON:

    {{
        "score": 0,
        "reason": ""
    }}

    Scoring:

    0 = Context is completely irrelevant.

    0.5 = Context is partially relevant.

    1 = Context is highly relevant and useful.

    Judge ONLY whether the context is relevant to the
    question.

    Do not judge whether the context is factually correct.
    Do not use outside knowledge.
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

    def evaluate_answer_relevance(
        self,
        question: str,
        answer: str,
    ) -> dict:

        prompt = f"""
    You are evaluating the relevance of an AI-generated
    answer in a Retrieval-Augmented Generation system.

    Question:
    {question}

    Generated Answer:
    {answer}

    Determine whether the answer directly addresses
    the user's question.

    Return ONLY valid JSON:

    {{
        "score": 0,
        "reason": ""
    }}

    Scoring:

    0 = Answer does not address the question.

    0.5 = Answer partially addresses the question.

    1 = Answer directly and completely addresses
    the question.

    Judge ONLY answer relevance.

    Do not judge whether the answer is factually correct.
    Do not use outside knowledge.
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