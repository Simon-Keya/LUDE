from fastapi import APIRouter, Depends, HTTPException
from ..schemas.user import UserCreate, UserUpdate, User, AdminCreate, AdminShow
from ..services.user import (
    get_all_users, create_user, update_user, delete_user, create_admin, get_admins,
)
from .authentication import get_current_user

router = APIRouter(tags=['users'])

@router.get("/users", response_model=list[User])
async def get_all_users(current_user: User = Depends(get_current_user)):
    return await get_all_users()

@router.post("/users", response_model=User)
async def create_normal_user(
    user: UserCreate,
    current_user: User = Depends(get_current_user),
):
    if current_user.role == "admin":
        return await create_user(user)

    raise HTTPException(status_code=403, detail="Only admins can create users")

@router.post("/admins", response_model=AdminShow)
async def create_admin_user(
    admin: AdminCreate,
    current_user: User = Depends(get_current_user),
):
    # Check if there are any users in the database
    users = await get_all_users()
    if not users:
        # If no users, allow admin creation without authentication
        return await create_admin(admin)

    if current_user.role == "admin":
        return await create_admin(admin)

    raise HTTPException(status_code=403, detail="Only admins can create admins")

@router.put("/users/{user_id}", response_model=User)
async def update_user_info(
    user_id: int,
    user: UserUpdate,
    current_user: User = Depends(get_current_user),
):
    if current_user.id == user_id or current_user.role == "admin":
        return await update_user(user_id, user)

    raise HTTPException(status_code=403, detail="Only users can update their own profiles")

@router.delete("/users/{user_id}", response_model=User)
async def delete_user_info(
    user_id: int,
    current_user: User = Depends(get_current_user),
):
    if current_user.id == user_id or current_user.role == "admin":
        return await delete_user(user_id)

    raise HTTPException(status_code=403, detail="Only users can delete their own profiles")

@router.post("/users/admin", response_model=AdminShow)
async def create_admin(
    admin_create: AdminCreate,
    current_user: User = Depends(get_current_user),
):
    """Creates a new Admin user."""

    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Only Admin users can create new Admin users")

    admins = await get_admins()

    if not admins:
        admin = await create_admin(admin_create)
        return admin

    admin = await create_admin(admin_create)  # Corrected this line
    return admin

@router.get("/users/admins", response_model=list[AdminShow])
async def get_all_admins(
    current_user: User = Depends(get_current_user),
):
    if current_user.role == "admin":
        return await get_admins()

    raise HTTPException(status_code=403, detail="Only admins can view admins")
