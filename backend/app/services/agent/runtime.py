from app.services.agent.graph.config import get_graph_config
from app.services.agent.graph.graph import graph
from app.services.agent.graph.event_mapper import map_graph_event
from app.services.agent.graph.runtime_context import AgentRuntimeContext


class AgentRuntime:

    def __init__(self, db):
        self.db = db

    async def run(
        self,
        prompt: str,
        thread_id: str,
    ):

        state = {
            "prompt": prompt,
        }

        runtime_context = AgentRuntimeContext(
            db=self.db,
        )

        config = {
            **get_graph_config(thread_id),
            "recursion_limit": 20,
        }

        async for event in graph.astream(
            state,
            config=config,
            context=runtime_context,
            stream_mode=["updates", "custom"],
        ):

            mode, data = event

            # -----------------------------
            # Custom responder token
            # -----------------------------

            if mode == "custom":

                yield data

                continue

            # -----------------------------
            # Normal graph update
            # -----------------------------

            if mode == "updates":

                mapped_event = map_graph_event(data)

                if mapped_event:

                    yield mapped_event