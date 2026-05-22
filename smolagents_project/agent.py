from smolagents import tool, CodeAgent, LiteLLMModel


@tool
def document_search(query: str) -> str:
    """
    Searches internal documents.

    Args:
        query: The search query from the user.
    """

    documents = {
        "python": "Python is used for AI and backend.",
        "power bi": "Power BI is used for dashboards.",
        "sql": "SQL is used for querying databases."
    }

    query = query.lower()

    for key, value in documents.items():
        if key in query:
            return value

    return "No document found."


model = LiteLLMModel(
    model_id="ollama/qwen2.5:3b",
    api_base="http://localhost:11434"
)

agent = CodeAgent(
    tools=[document_search],
    model=model
)

response = agent.run(
    "What is Power BI used for?"
)

print("\nFinal Answer:")
print(response)