from fastapi import APIRouter, Depends, HTTPException
from ..schemas.user import UserCreate, UserUpdate, User, AdminBase, AdminCreate, AdminShow
from ..services.user import get_all_users, create_user, update_user, delete_user
from .authentication import get_current_user
from fastapi import APIRouter

router = APIRouter()

@router.get("/users", response_model=list[User])
async def get_all_users(current_user: User = Depends(get_current_user)):
    return await get_all_users()

@router.post("/users", response_model=User)
async def create_user(
    user_create: UserCreate,
    current_user: User = Depends(get_current_user),
):
    if current_user.role == "admin":
        return await create_user(user_create)

    raise HTTPException(status_code=403, detail="Only admins can create users")

@router.put("/users/{user_id}", response_model=User)
async def update_user(
    user_id: int,
    user_update: UserUpdate,
    current_user: User = Depends(get_current_user),
):
    if current_user.id == user_id or current_user.role == "admin":
        return await update_user(user_id, user_update)

    raise HTTPException(status_code=403, detail="Only users can update their own profiles")

@router.delete("/users/{user_id}", response_model=User)
async def delete_user(
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
    if current_user.role == "admin":
        return await create_user(admin_create, user_type="admin")

    raise HTTPException(status_code=403, detail="Only admins can create admins")

@router.get("/users/admins", response_model=list[AdminShow])
async def get_admins(
    current_user: User = Depends(get_current_user),
):
    if current_user.role == "admin":
        return await get_all_users(user_type="admin")

    raise HTTPException(status_code=403, detail="Only admins can view admins")
