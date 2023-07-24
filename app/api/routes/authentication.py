from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from ...core.security import create_access_token, get_user_by_email, get_current_user
from .users import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/token")

router = APIRouter(tags=['authentication'])


@router.post("/token")
async def login(email: str, password: str, depends_on=Depends(oauth2_scheme)):
    """Logs in a user and returns an access token."""
    user = await get_user_by_email(email)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect email or password")

    if not user.check_password(password):
        raise HTTPException(status_code=401, detail="Incorrect email or password")

    token = create_access_token(user.id)

    return {"access_token": token}


@router.get("/me")
async def get_current_user(current_user: User = Depends(get_current_user)):
    """Returns the currently logged in user."""
    return current_user

