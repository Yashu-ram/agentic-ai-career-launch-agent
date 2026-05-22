SUSPICIOUS_PATTERNS = [
    "ignore previous instructions",
    "reveal system prompt",
    "show hidden memory",
    "bypass security",
    "act as admin",
]

def detect_prompt_injection(text):

    lower = text.lower()

    for pattern in SUSPICIOUS_PATTERNS:

        if pattern in lower:
            return True

    return False