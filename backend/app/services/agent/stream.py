import json


def sse(event: dict):

    return f"data: {json.dumps(event)}\n\n"