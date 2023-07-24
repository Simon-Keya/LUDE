from fastapi import APIRouter, Depends, HTTPException
from ..schemas.task_assignment import TaskAssignment
from ..services.task_assignments import create_task_assignment, delete_task_assignment
from ...core.security import get_current_user

router = APIRouter(tags=['task_assignment']
)

@router.post("/tasks/{task_id}/task_assignments")
async def create_task_assignment(
    task_id: int,
    task_assignment: TaskAssignment,
    current_user=Depends(get_current_user),
):
    return await create_task_assignment(task_id, task_assignment, current_user=current_user)

@router.delete("/tasks/{task_id}/task_assignments/{task_assignment_id}")
async def delete_task_assignment(
    task_id: int,
    task_assignment_id: int,
    current_user=Depends(get_current_user),
):
    return await delete_task_assignment(task_id, task_assignment_id, current_user=current_user)
