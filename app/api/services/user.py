from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..schemas.user import User
from ...database.repositories.users import (
    get_all_users as repository_get_all_users,
    create_user as repository_create_user,
    update_user as repository_update_user,
    delete_user as repository_delete_user,
)
from .authentication import get_current_user

router = APIRouter()

@router.get("/users", response_model=User)
async def get_all_users():
    users = await repository_get_all_users()
    return users

@router.post("/users", response_model=User)
async def create_user(user: User):
    created_user = await repository_create_user(user)
    return created_user

@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: User):
    updated_user = await repository_update_user(user_id, user)
    return updated_user

@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    deleted_user = await repository_delete_user(user_id)
    return deleted_user

@router.get("/user/me", response_model=User)
async def get_current_user():
    return await get_current_user()

