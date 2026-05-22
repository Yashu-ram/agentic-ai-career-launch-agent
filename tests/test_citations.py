from rag_agent.main import ask_question

def test_citations_exist():

    response = ask_question(
        "Refund policy?"
    )

    assert "citations" in response
    assert len(response["citations"]) > 0