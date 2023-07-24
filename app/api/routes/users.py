from fastapi import APIRouter, Depends, HTTPException
from ..schemas.user import User
from ..services.user import get_all_users, create_user, update_user, delete_user
from .authentication import get_current_user

router = APIRouter(tags=['users'])

@router.get("/users")
async def get_all_users():
    return await get_all_users()

@router.post("/users")
async def create_user(
    user: User,
    current_user: User = Depends(get_current_user),
):
    if current_user.is_admin:
        return await create_user(user, current_user=current_user)

    raise HTTPException(status_code=403, detail="Only admins can create users")

@router.put("/users/{user_id}")
async def update_user(
    user_id: int,
    user: User,
    current_user: User = Depends(get_current_user),
):
    if current_user.id == user_id or current_user.is_admin:
        return await update_user(user_id, user, current_user=current_user)

    raise HTTPException(status_code=403, detail="Only users can update their own profiles")

@router.delete("/users/{user_id}")
async def delete_user(
    user_id: int,
    current_user: User = Depends(get_current_user),
):
    if current_user.id == user_id or current_user.is_admin:
        return await delete_user(user_id, current_user=current_user)

    raise HTTPException(status_code=403, detail="Only users can delete their own profiles")
