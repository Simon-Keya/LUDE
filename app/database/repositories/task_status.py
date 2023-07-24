# app/db/repositories/task_status.py

from fastapi import HTTPException
from ...api.models.task_status import TaskStatus
from sqlalchemy.orm import Session

async def get_all_task_statuses(db: Session):
    return db.query(TaskStatus).all()

async def create_task_status(task_id: int, task_status: TaskStatus, db: Session):
    db_task_status = TaskStatus(task_id=task_id, status=task_status.status)
    db.add(db_task_status)
    db.commit()
    return db_task_status

async def delete_task_status(task_id: int, task_status_id: int, db: Session):
    db_task_status = db.query(TaskStatus).filter(
        TaskStatus.task_id == task_id, TaskStatus.id == task_status_id
    ).first()
    if not db_task_status:
        raise HTTPException(status_code=404, detail="Task status not found")

    db.delete(db_task_status)
    db.commit()

