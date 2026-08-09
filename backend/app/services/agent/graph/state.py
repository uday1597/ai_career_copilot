from typing_extensions import TypedDict

from langchain_core.messages import BaseMessage

from app.services.agent.models.planner import ExecutionPlan


class AgentState(TypedDict, total=False):

    prompt: str

    messages: list[BaseMessage]

    plan: ExecutionPlan

    tool_results: dict

    answer: str

    intent: str