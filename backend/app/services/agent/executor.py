from app.services.agent.tool_registry import TOOL_REGISTRY


class AgentExecutor:

    def __init__(self, db):
        self.db = db

    def execute(self, plan, context):

        results = {}

        for step in plan.steps:

            tool = TOOL_REGISTRY.get(step.tool.value)

            if tool is None:
                raise Exception(f"Unknown tool {step.tool}")

            yield {
                "type": "tool_start",
                "tool": step.tool.value,
                "reason": step.reason,
            }

            result = tool(
                db=self.db,
                context=context,
                previous_results=results,
            )

            context.put(
                step.tool.value,
                result,
            )

            results[step.tool.value] = result

            yield {
                "type": "tool_end",
                "tool": step.tool.value,
                "result": result,
            }

        return results