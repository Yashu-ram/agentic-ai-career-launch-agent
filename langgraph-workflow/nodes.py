from state import AgentState


# -----------------------------
# RETRIEVE NODE
# -----------------------------

def retrieve_node(state: AgentState):

    query = state["query"]

    docs = f"Retrieved docs for: {query}"

    print("\n[Retrieve Node]")
    print(docs)

    return {
        "retrieved_docs": docs
    }


# -----------------------------
# REASON NODE
# -----------------------------

def reason_node(state: AgentState):

    query = state["query"]
    docs = state["retrieved_docs"]

    draft = f"Answer generated using: {docs}"

    print("\n[Reason Node]")
    print(draft)

    return {
        "draft_answer": draft
    }


# -----------------------------
# SAFETY NODE
# -----------------------------

def safety_node(state: AgentState):

    query = state["query"].lower()

    risky_keywords = ["medical", "legal"]

    risky = any(word in query for word in risky_keywords)

    print("\n[Safety Node]")

    if risky:
        print("Risky query detected")
        return {
            "safety_flag": "risky"
        }

    print("Safe query")

    return {
        "safety_flag": "safe"
    }


# -----------------------------
# HUMAN REVIEW NODE
# -----------------------------

def review_node(state: AgentState):

    print("\n[Human Review Node]")

    print("Draft Answer:")
    print(state["draft_answer"])

    approval = input("Approve answer? (yes/no): ")

    return {
        "approved": approval.lower() == "yes"
    }


# -----------------------------
# ANSWER NODE
# -----------------------------

def answer_node(state: AgentState):

    print("\n[Answer Node]")

    if state.get("approved") is False:
        print("Answer rejected by reviewer")

    else:
        print("Final Answer:")
        print(state["draft_answer"])

    return {}