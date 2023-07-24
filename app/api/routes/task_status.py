from fastapi import APIRouter, Depends, HTTPException
from ..schemas.task_status import TaskStatus
from ..services.task_status import create_task_status, delete_task_status
from ...core.security import get_current_user

router = APIRouter(tags=['task_status'])

@router.post("/tasks/{task_id}/task_statuses")
async def create_task_status(
    task_id: int,
    task_status: TaskStatus,
    current_user=Depends(get_current_user),
):
    return await create_task_status(task_id, task_status, current_user=current_user)

@router.delete("/tasks/{task_id}/task_statuses/{task_status_id}")
async def delete_task_status(
    task_id: int,
    task_status_id: int,
    current_user=Depends(get_current_user),
):
    return await delete_task_status(task_id, task_status_id, current_user=current_user)
