import json
from app.models.learning_roadmap import LearningRoadmap

def get_learning_roadmap_tool(db,context,
    previous_results,):

    roadmap = (
        db.query(LearningRoadmap)
        .order_by(
            LearningRoadmap.created_at.desc()
        )
        .first()
    )

    if roadmap is None:

        return json.dumps(
            {
                "status": "NO_ROADMAP"
            }
        )

    return json.dumps(
        roadmap.roadmap,
        default=str,
    )
    