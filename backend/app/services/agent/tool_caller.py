from app.services.agent.tools.registry import TOOL_REGISTRY


class ToolCaller:

    def __init__(self, db, context):
        self.db = db
        self.context = context

    def call(
        self,
        name: str,
        arguments: dict,
    ):

        tool = TOOL_REGISTRY.get(name)

        if tool is None:
            raise Exception(f"Unknown tool {name}")

        return tool(
            db=self.db,
            context=self.context,
            previous_results={},
            **arguments,
        )