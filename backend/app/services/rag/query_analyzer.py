class QueryAnalyzer:

    def detect_document_type(
        self,
        question: str,
    ) -> str | None:

        question = question.lower()

        if "resume" in question:

            return "resume"

        if "roadmap" in question:

            return "roadmap"

        if "assessment" in question:

            return "assessment"

        if "pdf" in question:

            return "pdf"

        return None