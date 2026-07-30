class AgentContext:

    def __init__(self):
        self.data = {}

    def put(self, key: str, value):
        self.data[key] = value

    def get(self, key: str):
        return self.data.get(key)

    def all(self):
        return self.data