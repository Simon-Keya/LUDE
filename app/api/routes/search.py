from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List

from ...database.session import get_db
from ...database.repositories.tasks import Task
from ...core.security import get_current_user
from ..schemas.task import Task, TaskCreate, TaskUpdate
from ..schemas.user import User

router = APIRouter()

@router.get("/tasks/", response_model=List[Task])
def search_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    q: str = Query(None, min_length=3, max_length=50),
):
    """
    Search for tasks that match the query 'q' in the title or description.
    """
    return Task.search_tasks(db, current_user.id, q)


@router.get("/users/", response_model=List[User])
def search_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    q: str = Query(None, min_length=3, max_length=50),
):
    """
    Search for users that match the query 'q' in their username or email.
    """
    return Task.search_users(db, current_user.id, q)
