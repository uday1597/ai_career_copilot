def map_graph_event(event):

    if not event:
        return None

    if "planner" in event:

        plan = event["planner"].get("plan")

        if plan is None:
            return None

        return {
            "type": "plan",
            "steps": [
                {
                    "tool": step.tool,
                    "reason": step.reason,
                }
                for step in plan.steps
            ],
        }

    if "executor" in event:

        results = event["executor"].get(
            "tool_results",
            {},
        )

        return {
            "type": "tools",
            "results": results,
        }

    if "responder" in event:
        return None

    return None