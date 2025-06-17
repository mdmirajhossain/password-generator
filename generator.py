import random
import string


def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    if not any([use_upper, use_lower, use_digits, use_symbols]):
        raise ValueError("At least one character type must be selected.")

    chars = ""
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password
