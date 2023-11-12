from fastapi import APIRouter, Depends, HTTPException
from typing import List, Union
from ..schemas.task import Task, TaskCreate, TaskUpdate
from ..services.task import get_all_tasks, create_task, update_task, delete_task
from ...core.security import get_current_user

router = APIRouter(tags=['tasks'])

@router.get("/tasks", response_model= List[Task])
async def get_all_tasks():
    return await get_all_tasks()

@router.post("/tasks", response_model= TaskCreate)
async def create_task(
    task: TaskCreate,
    current_user=Depends(get_current_user),
):
    return await create_task(task, current_user=current_user)

@router.put("/tasks/{task_id}", response_model=TaskUpdate)
async def update_task(
    task_id: int,
    task: TaskUpdate,
    current_user=Depends(get_current_user),
):
    return await update_task(task_id, task, current_user=current_user)

@router.delete("/tasks/{task_id}", response_model=Task)
async def delete_task(
    task_id: int,
    current_user=Depends(get_current_user),
):
    return await delete_task(task_id, current_user=current_user)
