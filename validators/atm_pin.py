"""Four-digit ATM PIN validator implemented as a length-counting DFA."""

def validate_pin(value: str) -> tuple[bool, str]:
    if not isinstance(value, str):
        return False, "PIN must be text."
    # States q0..q4 count digits; any non-digit or fifth digit enters dead state.
    state = 0
    for ch in value:
        if ch < "0" or ch > "9":
            return False, "Only digits 0-9 are allowed."
        state += 1
        if state > 4:
            return False, "PIN must contain exactly four digits."
    if state == 4:
        return True, "Valid four-digit PIN."
    return False, "PIN must contain exactly four digits."
