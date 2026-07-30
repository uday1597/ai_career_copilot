import json
from app.models.assessment import Assessment

def get_assessment_tool(db,context,
    previous_results,week: int,):
    
    assessment = (
        db.query(Assessment)
        .filter(
            Assessment.week == week
        )
        .first()
    )

    if assessment is None:

        return json.dumps(
            {
                "status": "NO_ASSESSMENT"
            }
        )
    return json.dumps(
        {
            "week": assessment.week,
            "status": assessment.status,
            "overall_score": assessment.overall_score,
            "feedback": assessment.feedback,
        },
        default=str,
    ) 
