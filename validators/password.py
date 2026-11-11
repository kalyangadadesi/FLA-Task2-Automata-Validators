"""Password validator using finite-state summaries.

Rule: 8-16 characters, at least one uppercase, lowercase, digit and
one allowed special character. Whitespace and unsupported characters fail.
"""
SPECIAL = set("!@#$%^&*()-_+=")

def validate_password(value: str) -> tuple[bool, str]:
    if not isinstance(value, str):
        return False, "Input must be text."

    # DFA state summary: length (0..17+), four category flags, dead state.
    length = 0
    upper = lower = digit = special = False

    for ch in value:
        length += 1
        if ch.isspace():
            return False, "Spaces are not allowed."
        if "A" <= ch <= "Z":
            upper = True
        elif "a" <= ch <= "z":
            lower = True
        elif "0" <= ch <= "9":
            digit = True
        elif ch in SPECIAL:
            special = True
        else:
            return False, f"Unsupported character: {ch}"

        if length > 16:
            return False, "Password must not exceed 16 characters."

    if length < 8:
        return False, "Password must contain at least 8 characters."
    if not upper:
        return False, "Add at least one uppercase letter."
    if not lower:
        return False, "Add at least one lowercase letter."
    if not digit:
        return False, "Add at least one digit."
    if not special:
        return False, "Add at least one allowed special character."
    return True, "Password satisfies all defined rules."
