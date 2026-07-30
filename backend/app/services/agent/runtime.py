from app.services.agent.planner import create_plan
from app.services.agent.executor import AgentExecutor
from app.services.agent.context import AgentContext
from app.services.agent.responder import stream_response


class AgentRuntime:

    def __init__(self, db):
        self.db = db

    def run(self, prompt: str):

        yield {
            "type": "status",
            "message": "Planning...",
        }

        context = AgentContext()

        plan = create_plan(prompt)

        yield {
            "type": "plan",
            "steps": [
                {
                    "tool": step.tool.value,
                    "reason": step.reason,
                }
                for step in plan.steps
            ],
        }

        executor = AgentExecutor(self.db)

        results = {}

        for event in executor.execute(
            plan,
            context,
        ):

            yield event

            if event["type"] == "tool_end":
                results[event["tool"]] = event["result"]

        yield {
            "type": "status",
            "message": "Generating response...",
        }

        answer = ""

        for token in stream_response(
            prompt,
            results,
        ):

            answer += token

            yield {
                "type": "token",
                "content": token,
            }

        yield {
            "type": "complete",
            "answer": answer,
        }