from typing import List, Optional
from ..models.task import Task


def search_tasks(
    q: str, completed: Optional[bool] = None, tags: Optional[List[str]] = None
) -> List[Task]:
    """Search for tasks.

    Args:
        q: The search query.
        completed: Whether to only return completed tasks.
        tags: A list of tags to filter by.

    Returns:
        A list of tasks.
    """

    tasks = []

    if q:
        tasks = Task.query.filter(Task.title.contains(q)).all()

    if completed is not None:
        tasks = [task for task in tasks if task.completed == completed]

    if tags is not None:
        for tag in tags:
            tasks = [task for task in tasks if tag in task.tags]

    return tasks

