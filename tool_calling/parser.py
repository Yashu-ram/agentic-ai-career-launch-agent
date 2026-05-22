import re


def parse_response(text):

    thought = re.search(r"THOUGHT:(.*)", text)
    action = re.search(r"ACTION:(.*)", text)
    tool_input = re.search(r"INPUT:(.*)", text)

    return (

        thought.group(1).strip() if thought else None,

        action.group(1).strip() if action else None,

        tool_input.group(1).strip() if tool_input else None
    )