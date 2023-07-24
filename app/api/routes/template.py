from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from ..models.templates import Template
from ..services.templates import (
    get_all_templates,
    get_template_by_id,
    create_template,
    update_template,
    delete_template,
)

router = APIRouter(tags=['templates'])


@router.get("/templates")
async def get_templates():
    # Get all templates from the database
    templates = await get_all_templates()

    # Return the templates as a JSON response
    return JSONResponse(content=templates)


@router.post("/templates")
async def create_template(request: Request):
    # Get the template data from the request body
    template_data = await request.json()

    # Create a new template from the data
    template = Template(**template_data)

    # Save the template to the database
    created_template = await create_template(template)

    # Return the created template as a JSON response
    return JSONResponse(content=created_template.dict())


@router.put("/templates/{template_id}")
async def update_template(template_id: int, request: Request):
    # Get the template from the database
    template = await get_template_by_id(template_id)

    # Update the template with the data from the request body
    template_data = await request.json()
    template.update(**template_data)

    # Save the template to the database
    updated_template = await update_template(template)

    # Return the updated template as a JSON response
    return JSONResponse(content=updated_template.dict())


@router.delete("/templates/{template_id}")
async def delete_template(template_id: int):
    # Get the template from the database
    template = await get_template_by_id(template_id)

    # Delete the template from the database
    await delete_template(template)

    # Return a JSON response with the status code 204
    return JSONResponse(status_code=204)
