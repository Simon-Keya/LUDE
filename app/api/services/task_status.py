from fastapi import HTTPException
from ..schemas.task_status import TaskStatus
from ...database.repositories.task_status import create_task_status, delete_task_status

async def create_task_status(task_id: int, task_status: TaskStatus, response_model=TaskStatus):
    return await create_task_status(task_id, task_status)

async def delete_task_status(task_id: int, task_status_id: int, response_model=TaskStatus):
    return await delete_task_status(task_id, task_status_id)

