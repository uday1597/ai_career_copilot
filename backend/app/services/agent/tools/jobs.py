import json
from app.models.job import Job


def search_jobs_tool(db,context,previous_results,keyword: str | None = None,):

    jobs = (
        db.query(Job)
        .limit(10)
        .all()
    )

    results = []

    for job in jobs:

        results.append(
            {
                "id": str(job.id),
                "title": job.title,
                "company": job.company,
                "location": job.location,
                "technologies": job.technologies,
            }
        )

    return json.dumps(results, default=str)
