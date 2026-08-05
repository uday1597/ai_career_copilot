from app.services.agent.tools.registery import TOOL_REGISTRY


class AgentExecutor:

    def __init__(self, db):
        self.db = db

    def execute_step(
        self,
        step,
        context,
        previous_results,
    ):

        tool = TOOL_REGISTRY.get(step.tool.value)

        if tool is None:
            raise Exception(
                f"Unknown tool {step.tool}"
            )

        yield {
            "type": "tool_start",
            "tool": step.tool.value,
            "reason": step.reason,
        }

        result = tool(
            db=self.db,
            context=context,
            previous_results=previous_results,
        )

        context.put(
            step.tool.value,
            result,
        )

        previous_results[step.tool.value] = result

        yield {
            "type": "tool_end",
            "tool": step.tool.value,
            "result": result,
        }

    def execute(
        self,
        plan,
        context,
    ):

        results = {}

        for step in plan.steps:

            yield from self.execute_step(
                step,
                context,
                results,
            )

        return results