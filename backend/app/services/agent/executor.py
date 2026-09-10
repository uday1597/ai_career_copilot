from app.services.agent.mcp.github import GitHubMCPClient
from app.services.agent.tools.registery import TOOL_REGISTRY


class AgentExecutor:

    def __init__(self, db):
        self.db = db
        self.github_mcp = GitHubMCPClient()

    async def execute_step(
        self,
        step,
        context,
        previous_results,
    ):
        print("\n===== EXECUTOR =====")
        print("Tool:", step.tool)
        print("Source:", step.source)
        print("Arguments:", step.arguments)
        print("====================\n")
        yield {
            "type": "tool_start",
            "tool": step.tool,
            "reason": step.reason,
        }

        # --------------------------------
        # INTERNAL TOOL
        # --------------------------------

        if step.source == "internal":

            tool = TOOL_REGISTRY.get(step.tool)

            if tool is None:
                raise Exception(
                    f"Unknown internal tool: {step.tool}"
                )

            result = tool(
                db=self.db,
                context=context,
                previous_results=previous_results,
                **step.arguments,
            )

        # --------------------------------
        # MCP TOOL
        # --------------------------------

        elif step.source == "mcp":

            result = await self.github_mcp.call_tool(
                step.tool,
                step.arguments,
            )

        else:

            raise Exception(
                f"Unknown tool source: {step.source}"
            )

        # --------------------------------
        # SAVE RESULT
        # --------------------------------

        context.put(
            step.tool,
            result,
        )

        previous_results[step.tool] = result

        yield {
            "type": "tool_end",
            "tool": step.tool,
            "result": result,
        }

    async def execute(
        self,
        plan,
        context,
    ):

        results = {}

        for step in plan.steps:

            async for event in self.execute_step(
                step,
                context,
                results,
            ):
                yield event