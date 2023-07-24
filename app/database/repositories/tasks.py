# app/db/repositories/task.py

from fastapi import HTTPException
from ...api.models.task import Task
from sqlalchemy.orm import Session

async def get_all_tasks(db: Session):
    return db.query(Task).all()

async def create_task(task: Task, db: Session):
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    return db_task

async def update_task(task_id: int, task: Task, db: Session):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    db_task.title = task.title
    db_task.description = task.description
    db_task.due_date = task.due_date
    db_task.status = task.status

    db.commit()
    return db_task

async def delete_task(task_id: int, db: Session):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(db_task)
    db.commit()

