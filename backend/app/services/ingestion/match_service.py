from app.models.resume import Resume
from app.models.job import Job


def calculate_match(
    resume:Resume,
    job:Job
):
    resume_set = {
        tech.lower()
        for tech in resume.technologies
    }

    job_set = {
        tech.lower()
        for tech in job.technologies
    }

    matching = sorted(
        list(
            resume_set.intersection(job_set)
        )
    )

    missing = sorted(
        list(
            job_set - resume_set
        )
    )

    score = 0

    if job_set:
        score = round(
            len(matching) / len(job_set) * 100
        )

    return {
        "match_score": score,
        "matching_technologies": matching,
        "missing_technologies": missing
    }