DANGEROUS_OUTPUTS = [
    "delete all files",
    "send credentials",
    "bypass authentication",
    "reveal secret",
]

def validate_output(text):

    lower = text.lower()

    for pattern in DANGEROUS_OUTPUTS:

        if pattern in lower:
            return False

    return True