class ConversationMemory:

    def __init__(self):

        self.messages = []

    def add_user(
        self,
        message: str,
    ):

        self.messages.append(
            {
                "role": "user",
                "content": message,
            }
        )

    def add_assistant(
        self,
        message: str,
    ):

        self.messages.append(
            {
                "role": "assistant",
                "content": message,
            }
        )

    def last_messages(
        self,
        limit: int = 6,
    ):

        return self.messages[-limit:]