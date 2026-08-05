from app.services.agent.graph.graph import graph
from app.services.agent.graph.config import get_graph_config
from app.services.agent.graph.event_mapper import map_graph_event


class AgentRuntime:

    def __init__(self, db):
        self.db = db

    def run(self, prompt: str):

        state = {
            "prompt": prompt,
            "db": self.db,
        }

        for event in graph.stream(
            state,
            config={**get_graph_config("career-copilot"),"recursion_limit": 20,}
        ):
            event = map_graph_event(event)

            if event:
                yield event