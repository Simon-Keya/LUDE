# app/utils/helpers.py

import os
import random
import string


def generate_random_string(length: int) -> str:
    """Generates a random string of a given length."""
    characters = string.ascii_lowercase + string.digits
    return "".join(random.choice(characters) for _ in range(length))

