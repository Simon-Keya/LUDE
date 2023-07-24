from fastapi import APIRouter, Depends, HTTPException
from ..schemas.task import Task
from ..services.user import get_current_user
from ..models.user import User


router = APIRouter()

@router.get("/tasks", response_model=Task)
async def get_all_tasks():
    tasks = await get_all_tasks()
    return tasks

@router.post("/tasks", response_model=Task)
async def create_task(
    task: Task,
    current_user: User = Depends(get_current_user),
):
    if current_user.is_admin:
        return await create_task(task, current_user=current_user)

    raise HTTPException(status_code=403, detail="Only admins can create tasks")

@router.put("/tasks/{task_id}", response_model=Task)
async def update_task(
    task_id: int,
    task: Task,
    current_user: User = Depends(get_current_user),
):
    if current_user.is_admin:
        # Implement update task logic here
        return {"message": "Task updated successfully"}

    raise HTTPException(status_code=403, detail="Only admins can update tasks")

@router.delete("/tasks/{task_id}")
async def delete_task(
    task_id: int,
    current_user: User = Depends(get_current_user),
):
    if current_user.is_admin:
        # Implement delete task logic here
        return {"message": "Task deleted successfully"}

    raise HTTPException(status_code=403, detail="Only admins can delete tasks")
