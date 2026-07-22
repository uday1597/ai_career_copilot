from sqlalchemy.orm import Session

from app.models.resume import Resume
from app.models.job import Job
from app.services.ai.match_explainer import explain_match
from app.services.ai.skill_gap_analyzer import analyze_skill_gap
from app.services.ai.learning_roadmap import generate_learning_roadmap

def match_resume_to_jobs(
    db: Session,
    resume_id: str,
    limit: int = 10
):
    resume = db.get(Resume, resume_id)

    if not resume:
        raise ValueError("Resume not found")

    if not resume.embedding:
        raise ValueError("Resume has no embedding")

    resume_tech = {
        tech.lower().strip()
        for tech in (resume.technologies or [])
    }

    jobs = (
        db.query(
            Job,
            (
                1 - Job.embedding.cosine_distance(
                    resume.embedding
                )
            ).label("similarity")
        )
        .order_by(
            Job.embedding.cosine_distance(
                resume.embedding
            )
        )
        .limit(limit)
        .all()
    )

    results = []

    for job, similarity in jobs:

        job_tech = {
            tech.lower().strip()
            for tech in (job.technologies or [])
        }

        matching = sorted(resume_tech & job_tech)
        missing = sorted(job_tech - resume_tech)
        explanation = explain_match(
            resume_summary=resume.summary,
            resume_technologies=resume.technologies,
            job_title=job.title,
            job_description=job.description,
            job_technologies=job.technologies,
            match_score=round(float(similarity) * 100),
        )
        skill_gap = analyze_skill_gap(
            resume_summary=resume.summary,
            resume_technologies=resume.technologies,
            job_title=job.title,
            job_description=job.description,
            job_technologies=job.technologies,
        )
        learning_roadmap = generate_learning_roadmap(
            resume_summary=resume.summary,
            resume_technologies=resume.technologies,
            job_title=job.title,
            job_description=job.description,
            job_technologies=job.technologies,
        )
        results.append(
            {
                "job_id": job.id,
                "title": job.title,
                "similarity": round(float(similarity), 4),
                "match_score": round(float(similarity) * 100),
                "matching_technologies": matching,
                "missing_technologies": missing,
                "explanation": explanation,
                "skill_gap": skill_gap,
                "learning_roadmap": learning_roadmap,
            }
        )

    return results