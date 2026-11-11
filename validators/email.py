"""Email-format validator for a deliberately defined regular-language subset.

Grammar:
  local  := atom (("." atom) | atom)*
  atom   := one or more letters, digits, _, %, +, -
  domain := label ("." label)+
  label  := alphanumeric (alphanumeric | "-")* alphanumeric
  tld    := 2 or more ASCII letters

The implementation scans characters and maintains finite states/flags.
It is not intended to implement every rule in the full email standards.
"""
import re

LOCAL_ATOM = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_%+-")

def validate_email(value: str) -> tuple[bool, str]:
    if not isinstance(value, str) or not value:
        return False, "Email cannot be empty."
    if any(ch.isspace() for ch in value):
        return False, "Spaces are not allowed."
    if value.count("@") != 1:
        return False, "Email must contain exactly one @ symbol."

    local, domain = value.split("@")
    if not local or len(local) > 64:
        return False, "Local part must contain 1 to 64 characters."
    if local.startswith(".") or local.endswith(".") or ".." in local:
        return False, "Local part cannot start/end with or repeat a dot."
    for ch in local:
        if ch != "." and ch not in LOCAL_ATOM:
            return False, f"Invalid character in local part: {ch}"

    if len(domain) > 253 or "." not in domain:
        return False, "Domain must contain a name and an extension."
    labels = domain.split(".")
    if len(labels) < 2:
        return False, "Domain must contain at least one dot."
    for label in labels:
        if not label or len(label) > 63:
            return False, "Domain labels must contain 1 to 63 characters."
        if not label[0].isalnum() or not label[-1].isalnum():
            return False, "Domain labels must start and end with a letter or digit."
        if not all(ch.isascii() and (ch.isalnum() or ch == "-") for ch in label):
            return False, "Domain labels may contain only letters, digits and hyphens."
    tld = labels[-1]
    if len(tld) < 2 or not tld.isalpha() or not tld.isascii():
        return False, "Extension must contain at least two letters."
    return True, "Email follows the defined format."
