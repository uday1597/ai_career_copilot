from app.services.ingestion.openai_service import client


class QueryRewriter:

    def rewrite(
        self,
        history,
        question: str,
    ) -> str:

        prompt = f"""
You rewrite follow-up questions into standalone questions.

Conversation:

{history}

Current Question:

{question}

Return ONLY the rewritten question.
"""

        response = client.responses.create(

            model="gpt-5",

            input=prompt,

        )

        return response.output_text.strip()