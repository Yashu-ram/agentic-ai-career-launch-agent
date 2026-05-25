unsafe_keywords = [

    "medical",
    "diagnosis",
    "treatment",
    "legal",
    "lawsuit",
    "court",
    "confidential",
    "private data",
    "salary leak",
    "passport number"
]


def detect_sensitive_topics(text):

    text = text.lower()

    for word in unsafe_keywords:

        if word in text:

            return True

    return False