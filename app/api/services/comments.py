from fastapi import HTTPException
from ..models.comment import Comment
from ...database.repositories.comments import create_comment, delete_comment

async def create_comment(task_id: int, comment: Comment):
    return await create_comment(task_id, comment)

async def delete_comment(task_id: int, comment_id: int):
    return await delete_comment(task_id, comment_id)

