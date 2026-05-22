from langgraph.graph import StateGraph, END

from state import AgentState

from nodes import (
    retrieve_node,
    reason_node,
    safety_node,
    review_node,
    answer_node
)


# -----------------------------
# CONDITIONAL ROUTING
# -----------------------------

def route_safety(state: AgentState):

    if state["safety_flag"] == "risky":
        return "review"

    return "answer"


# -----------------------------
# BUILD GRAPH
# -----------------------------

graph = StateGraph(AgentState)

# Add nodes
graph.add_node("retrieve", retrieve_node)
graph.add_node("reason", reason_node)
graph.add_node("safety", safety_node)
graph.add_node("review", review_node)
graph.add_node("answer", answer_node)

# Entry point
graph.set_entry_point("retrieve")

# Edges
graph.add_edge("retrieve", "reason")
graph.add_edge("reason", "safety")

# Conditional edge
graph.add_conditional_edges(
    "safety",
    route_safety,
    {
        "review": "review",
        "answer": "answer"
    }
)

# Final flow
graph.add_edge("review", "answer")
graph.add_edge("answer", END)

# Compile graph
app = graph.compile()