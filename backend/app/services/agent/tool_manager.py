class ToolManager:

    def __init__(self):

        self.local_tools = {}

        self.mcp_tools = {}

    def register_local(
        self,
        name,
        tool,
    ):
        self.local_tools[name] = tool

    def register_mcp(
        self,
        name,
        tool,
    ):
        self.mcp_tools[name] = tool

    def get(self, name):

        if name in self.local_tools:
            return self.local_tools[name]

        if name in self.mcp_tools:
            return self.mcp_tools[name]

        raise Exception(f"Unknown tool {name}")