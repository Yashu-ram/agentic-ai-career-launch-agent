from rag_agent.main import ask_question

def test_response_schema():

    response = ask_question(
        "What is refund policy?"
    )

    required_keys = [
        "answer",
        "citations",
        "human_review"
    ]

    for key in required_keys:
        assert key in response