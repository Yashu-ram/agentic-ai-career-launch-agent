from pydantic import BaseModel
from typing import List


class CareerResponse(BaseModel):
    answer: str
    fit_score: int
    matching_skills: List[str]
    missing_skills: List[str]
    seven_day_plan: List[str] = [
        "Day 1 task",
        "Day 2 task"
    ]
    citations: List[str] = [
        "[SOURCE: filename.pdf]"
    ]
    human_review_flag: bool

    """Response schema for career recommendations.

    seven_day_plan MUST be a JSON array.
    citations MUST be a JSON array.
    Do NOT return plain text for arrays.
    Return ONLY valid JSON.
    No markdown.
    No explanations.
    """