from fastapi import HTTPException
from ...api.models.comment import Comment
from sqlalchemy.orm import Session

async def get_all_comments(db: Session):
    return db.query(Comment).all()

async def create_comment(task_id: int, comment: Comment, db: Session):
    db_comment = Comment(task_id=task_id, user_id=comment.user_id, text=comment.text)
    db.add(db_comment)
    db.commit()
    return db_comment

async def delete_comment(task_id: int, comment_id: int, db: Session):
    db_comment = db.query(Comment).filter(
        Comment.task_id == task_id, Comment.id == comment_id
    ).first()
    if not db_comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    db.delete(db_comment)
    db.commit()

