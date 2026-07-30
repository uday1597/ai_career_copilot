
import json
from app.services.ingestion.dashboard_service import build_dashboard


def get_dashboard_tool(db,context,previous_results,):

    dashboard = build_dashboard(db)

    return json.dumps(
        dashboard.model_dump(),
        default=str,
    )
