from rag_agent.main import ask_question

def test_empty_query():

    response = ask_question("")

    assert response["answer"] is not None