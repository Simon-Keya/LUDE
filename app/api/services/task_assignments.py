from fastapi import HTTPException
from ..models.task_assignment import TaskAssignment
from ...database.repositories.task_assignments import create_task_assignment, delete_task_assignment

async def create_task_assignment(task_id: int, task_assignment: TaskAssignment):
    return await create_task_assignment(task_id, task_assignment)

async def delete_task_assignment(task_id: int, task_assignment_id: int):
    return await delete_task_assignment(task_id, task_assignment_id)

