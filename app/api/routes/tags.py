from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from ..models.tags import Tag
from ..services.tags import (
    get_all_tags,
    get_tag_by_id,
    create_tag,
    update_tag,
    delete_tag,
)

router = APIRouter(tags=['tags'])


@router.get("/tags")
async def get_tags():
    # Get all tags from the database
    tags = await get_all_tags()

    # Return the tags as a JSON response
    return JSONResponse(content=tags)


@router.post("/tags")
async def create_tag(request: Request):
    # Get the tag data from the request body
    tag_data = await request.json()

    # Create a new tag from the data
    tag = Tag(**tag_data)

    # Save the tag to the database
    created_tag = await create_tag(tag)

    # Return the created tag as a JSON response
    return JSONResponse(content=created_tag.dict())


@router.put("/tags/{tag_id}")
async def update_tag(tag_id: int, request: Request):
    # Get the tag from the database
    tag = await get_tag_by_id(tag_id)

    # Update the tag with the data from the request body
    tag_data = await request.json()
    tag.update(**tag_data)

    # Save the tag to the database
    updated_tag = await update_tag(tag)

    # Return the updated tag as a JSON response
    return JSONResponse(content=updated_tag.dict())


@router.delete("/tags/{tag_id}")
async def delete_tag(tag_id: int):
    # Get the tag from the database
    tag = await get_tag_by_id(tag_id)

    # Delete the tag from the database
    await delete_tag(tag)

    # Return a JSON response with the status code 204
    return JSONResponse(status_code=204)
