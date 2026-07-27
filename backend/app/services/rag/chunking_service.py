import re


class ChunkingService:

    def __init__(
        self,
        chunk_size: int = 800,
        overlap: int = 150,
    ):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(
        self,
        text: str,
    ) -> list[str]:

        text = self._clean(text)

        paragraphs = [
            p.strip()
            for p in text.split("\n\n")
            if p.strip()
        ]

        chunks = []

        current = ""

        for paragraph in paragraphs:

            if len(current) + len(paragraph) <= self.chunk_size:

                if current:
                    current += "\n\n"

                current += paragraph

            else:

                if current:
                    chunks.append(current)

                overlap_text = current[-self.overlap :] if current else ""

                current = overlap_text + "\n\n" + paragraph

        if current:

            chunks.append(current)

        return chunks

    def _clean(
        self,
        text: str,
    ) -> str:

        text = text.replace("\r", "")

        text = re.sub(
            r"\n{3,}",
            "\n\n",
            text,
        )

        text = re.sub(
            r"[ \t]+",
            " ",
            text,
        )

        return text.strip()