import json
from enum import Enum

class EventType(str, Enum):
    STATUS = "status"
    PROGRESS = "progress"
    TOOL_START = "tool_start"
    TOOL_END = "tool_end"
    TOKEN = "token"
    COMPLETE = "complete"
    ERROR = "error"


class StreamEvent:

    @staticmethod
    def create(event_type: EventType, **payload):
        return (
            f"data: {json.dumps({'type': event_type, **payload})}\n\n"
        )

    @staticmethod
    def status(message: str):
        return StreamEvent.create(
            EventType.STATUS,
            message=message,
        )

    @staticmethod
    def progress(value: int):
        return StreamEvent.create(
            EventType.PROGRESS,
            value=value,
        )

    @staticmethod
    def tool_start(tool: str):
        return StreamEvent.create(
            EventType.TOOL_START,
            tool=tool,
        )

    @staticmethod
    def tool_end(tool: str):
        return StreamEvent.create(
            EventType.TOOL_END,
            tool=tool,
        )

    @staticmethod
    def token(content: str):
        return StreamEvent.create(
            EventType.TOKEN,
            content=content,
        )

    @staticmethod
    def complete(data):
        return StreamEvent.create(
            EventType.COMPLETE,
            data=data,
        )

    @staticmethod
    def error(message: str):
        return StreamEvent.create(
            EventType.ERROR,
            message=message,
        )