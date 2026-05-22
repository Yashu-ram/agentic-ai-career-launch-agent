HIGH_RISK_TOPICS = [
    "medical",
    "legal",
    "financial",
]

def requires_human_review(text):

    lower = text.lower()

    for topic in HIGH_RISK_TOPICS:

        if topic in lower:
            return True

    return False