from dataclasses import dataclass


@dataclass
class CrawledJob:

    title: str

    company: str

    location: str

    url: str

    job_id: str

    description: str | None = None

    department: str | None = None

    employment_type: str | None = None

    posted_date: str | None = None