from dataclasses import dataclass


@dataclass
class CrawledJob:
    title: str
    company: str
    location: str
    url: str
    description: str | None = None
    department: str | None = None
    job_id: str | None = None