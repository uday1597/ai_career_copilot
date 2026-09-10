class ContextBuilder:

    def build(
        self,
        compressed_documents: list[dict],
    ) -> str:

        sections = []

        for index, document in enumerate(
            compressed_documents,
            start=1,
        ):

            sections.append(
                f"""
SOURCE {index}

Document ID:
{document["document_id"]}

Document Type:
{document["document_type"]}

Source:
{document["source"]}

Content:
{document["content"]}
""".strip()
            )

        return "\n\n---\n\n".join(
            sections
        )