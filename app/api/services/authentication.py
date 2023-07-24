from datetime import datetime, timedelta
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from passlib.context import CryptContext
from .. import schemas
from ..schemas.user import User
from fastapi import APIRouter, Depends
from ...core.config import Settings

settings = Settings()


SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/token")

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

def create_access_token(user: User):
    expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": str(user.id), "exp": datetime.utcnow() + expires_delta}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def authenticate_user(username: str, password: str):
    # Retrieve user from database or other data source based on username
    # For demonstration purposes, let's assume we have a list of users
    # stored in memory.
    users = [
        {"id": 1, "username": "admin", "password": get_password_hash("admin")},
        {"id": 2, "username": "user", "password": get_password_hash("user")},
    ]

    # Find the user with the matching username
    user = next((user for user in users if user["username"] == username), None)

    if user is None:
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    # Verify the provided password against the hashed password stored for the user
    if not verify_password(password, user["password"]):
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    # Create and return the access token for the authenticated user
    user_obj = User(**user)  # Create a User object from the user data
    token = create_access_token(user_obj)
    return token

def get_user_by_id(user_id: int) -> User:
    """Gets the user by ID."""
    # Replace this implementation with your database query to retrieve the user
    users = [
        {"id": 1, "username": "admin", "password": get_password_hash("admin")},
        {"id": 2, "username": "user", "password": get_password_hash("user")},
    ]
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return User(**user)

router = APIRouter()

@router.get("/users/me")
async def get_current_user(
    token: str = Depends(oauth2_scheme),
) -> User:
    """Gets the current user."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = int(payload["sub"])
        user = get_user_by_id(user_id)
        return user
    except jwt.JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
