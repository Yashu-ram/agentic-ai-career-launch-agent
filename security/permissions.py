ALLOWED_TOOLS = [
    "search_docs",
    "retrieve_context",
]

BLOCKED_TOOLS = [
    "delete_files",
    "send_email",
    "execute_shell",
]

def check_tool_permission(tool_name):

    if tool_name not in ALLOWED_TOOLS:

        raise PermissionError(
            f"{tool_name} is blocked."
        )

    return True