# app/utils/validation.py

from fastapi import HTTPException
from ..models.user import User


def validate_email(email: str) -> bool:
    """Validates an email address."""
    if not email:
        return False

    if not "@" in email or not "." in email:
        return False

    return True


def validate_username(username: str) -> bool:
    """Validates a username."""
    if not username:
        return False

    if len(username) < 4:
        return False

    if len(username) > 20:
        return False

    return True


def validate_user(user: User) -> bool:
    """Validates a user object."""
    if not user.email:
        raise HTTPException(status_code=400, detail="Email is required")

    if not validate_email(user.email):
        raise HTTPException(status_code=400, detail="Invalid email address")

    if not user.username:
        raise HTTPException(status_code=400, detail="Username is required")

    if not validate_username(user.username):
        raise HTTPException(status_code=400, detail="Invalid username")

    return True

