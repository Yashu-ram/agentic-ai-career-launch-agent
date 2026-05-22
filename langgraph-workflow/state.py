from typing import TypedDict


class AgentState(TypedDict):
    query: str
    retrieved_docs: str
    draft_answer: str
    safety_flag: str
    approved: bool