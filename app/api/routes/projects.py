from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from ..models.projects import Project
from ..services.projects import (
    get_all_projects,
    get_project_by_id,
    create_project,
    update_project,
    delete_project,
)


router = APIRouter(tags=['projects'])

@router.get("/projects")
async def get_projects():
    # Get all projects from the database
    projects = await get_all_projects()

    # Return the projects as a JSON response
    return JSONResponse(content=projects)

@router.post("/projects")
async def create_project(request: Request):
    # Get the project data from the request body
    project_data = await request.json()

    # Create a new project from the data
    project = Project(**project_data)

    # Save the project to the database
    await project.save()

    # Return the created project as a JSON response
    return JSONResponse(content=project.dict())

# Other route operations

@router.put("/projects/{project_id}")
async def update_project(request: Request, project_id: int):
    # Get the project from the database
    project = await get_project_by_id(project_id)

    # Update the project with the data from the request body
    project.update(**await request.json())

    # Save the project to the database
    await project.save()

    # Return the updated project as a JSON response
    return JSONResponse(content=project.dict())

@router.delete("/projects/{project_id}")
async def delete_project(project_id: int):
    # Get the project from the database
    project = await get_project_by_id(project_id)

    # Delete the project from the database
    await project.delete()

    # Return a JSON response with the status code 204
    return JSONResponse(status_code=204)
