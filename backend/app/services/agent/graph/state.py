from typing import Any
from typing_extensions import TypedDict
from langchain_core.messages import BaseMessage
from app.services.agent.models.planner import ExecutionPlan
from app.services.agent.context import AgentContext


class AgentState(TypedDict, total=False):

    prompt: str

    db: Any

    messages: list[BaseMessage]

    context: AgentContext

    plan: ExecutionPlan

    tool_results: dict

    answer: str