import os

import httpx2
from dotenv import load_dotenv
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

load_dotenv()


class GitHubMCPClient:

    def __init__(self):
        self.url = "https://api.githubcopilot.com/mcp/"
        self.token = os.getenv("GITHUB_TOKEN")

        if not self.token:
            raise RuntimeError(
                "GITHUB_TOKEN is not configured"
            )

    async def call_tool(
    self,
    tool_name: str,
    arguments: dict,
    ):
        print("\n🔥 MCP TOOL CALLED")
        print("Server: GitHub MCP")
        print("Tool:", tool_name)
        print("Arguments:", arguments)
        print("🔥 END MCP CALL\n")
        headers = {
            "Authorization": f"Bearer {self.token}",
        }

        async with httpx2.AsyncClient(
            headers=headers,
            follow_redirects=True,
        ) as http_client:

            async with streamable_http_client(
                self.url,
                http_client=http_client,
            ) as (
                read_stream,
                write_stream,
            ):

                async with ClientSession(
                    read_stream,
                    write_stream,
                ) as session:

                    await session.initialize()

                    result = await session.call_tool(
                        tool_name,
                        arguments,
                    )

                    return result.model_dump()

    async def list_tools(self):
        print("🔥 MCP TOOLS DISCOVERED:")

        headers = {
            "Authorization": f"Bearer {self.token}",
        }

        async with httpx2.AsyncClient(
            headers=headers,
            follow_redirects=True,
        ) as http_client:

            async with streamable_http_client(
                self.url,
                http_client=http_client,
            ) as (
                read_stream,
                write_stream,
            ):

                async with ClientSession(
                    read_stream,
                    write_stream,
                ) as session:

                    await session.initialize()

                    response = await session.list_tools()

                    return response.tools