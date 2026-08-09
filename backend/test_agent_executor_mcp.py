import asyncio

from app.services.agent.executor import AgentExecutor
from app.services.agent.planner.models import (
    ExecutionPlan,
    PlanStep,
)


async def main():

    plan = ExecutionPlan(
        steps=[
            PlanStep(
                tool="search_repositories",
                source="mcp",
                reason="Find FastAPI projects",
                arguments={
                    "query": "python fastapi"
                },
            )
        ]
    )

    print("PLAN:")
    print(plan)

    # We don't have a DB requirement for this MCP-only test.
    executor = AgentExecutor(db=None)

    context = {}

    print("\nEXECUTING...\n")

    async for event in executor.execute(
        plan,
        context,
    ):
        print(event)


if __name__ == "__main__":
    asyncio.run(main())