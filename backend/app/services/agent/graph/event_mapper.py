def map_graph_event(event):

    if "planner" in event:

        return {
            "type": "plan",
            "steps": [
                {
                    "tool": step.tool.value,
                    "reason": step.reason,
                }
                for step in event["planner"]["plan"].steps
            ],
        }

    if "executor" in event:

        return {
            "type": "tool_results",
            "result": event["executor"]["tool_results"],
        }

    if "responder" in event:

        return {
            "type": "complete",
            "answer": event["responder"]["answer"],
        }

    return None