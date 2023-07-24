# app/db/repositories/task_assignment.py

from fastapi import HTTPException
from ...api.models.task_assignment import TaskAssignment
from sqlalchemy.orm import Session

async def get_all_task_assignments(db: Session):
    return db.query(TaskAssignment).all()

async def create_task_assignment(task_id: int, task_assignment: TaskAssignment, db: Session):
    db_task_assignment = TaskAssignment(
        task_id=task_id, user_id=task_assignment.user_id
    )
    db.add(db_task_assignment)
    db.commit()
    return db_task_assignment

async def delete_task_assignment(task_id: int, task_assignment_id: int, db: Session):
    db_task_assignment = db.query(TaskAssignment).filter(
        TaskAssignment.task_id == task_id, TaskAssignment.id == task_assignment_id
    ).first()
    if not db_task_assignment:
        raise HTTPException(status_code=404, detail="Task assignment not found")

    db.delete(db_task_assignment)
    db.commit()

