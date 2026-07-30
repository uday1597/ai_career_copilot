import json
from app.models.resume_match import ResumeMatch

def get_resume_match_tool(db,context,
    previous_results,):

    match = (
        db.query(ResumeMatch)
        .order_by(
            ResumeMatch.created_at.desc()
        )
        .first()
    )

    if match is None:

        return json.dumps(
            {
                "status": "NO_MATCH"
            }
        )

    return json.dumps(
        {
            "match_score": match.match_score,
            "matching_technologies": match.matching_technologies,
            "missing_technologies": match.missing_technologies,
        },
        default=str,
    )
