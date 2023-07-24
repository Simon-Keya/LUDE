# projects.py
from typing import List

from ..models.projects import Project


def get_all_projects() -> List[Project]:
    return Project.query.all()


def get_project_by_id(project_id: int) -> Project:
    return Project.query.get(project_id)


def create_project(project_data: dict) -> Project:
    project = Project(**project_data)
    project.save()
    return project


def update_project(project_id: int, project_data: dict) -> Project:
    project = Project.query.get(project_id)
    project.update(**project_data)
    project.save()
    return project


def delete_project(project_id: int) -> None:
    project = Project.query.get(project_id)
    project.delete()