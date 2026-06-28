def calculate_match(
    resume_technologies: list,
    job_technologies: list
):

    resume_set = {
        tech.lower()
        for tech in resume_technologies
    }

    job_set = {
        tech.lower()
        for tech in job_technologies
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