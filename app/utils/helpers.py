# utils/helpers.py
import re

def validate_code_snippet(code: str, language: str) -> bool:
    """
    Validates a code snippet based on language-specific patterns.
    """
    validation_patterns = {
        "python": [r"def\s+\w+\(.*\):", r"import\s+\w+"],
        "javascript": [r"function\s+\w+\(.*\)\s*\{", r"const\s+\w+\s*="],
        # Add more languages and patterns as needed
    }

    if language not in validation_patterns:
        return True  # No specific validation for this language

    for pattern in validation_patterns[language]:
        if not re.search(pattern, code):
            return False
    return True
