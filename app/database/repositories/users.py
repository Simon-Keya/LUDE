# app/db/repositories/users.py
from fastapi import HTTPException
from ...api.models.user import User
from sqlalchemy.orm import Session

async def get_all_users(db: Session):
    return db.query(User).all()

async def create_user(user: User, db: Session):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    return db_user

async def update_user(user_id: int, user: User, db: Session):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    db_user.email = user.email
    db_user.password = user.password
    db_user.is_admin = user.is_admin

    db.commit()
    return db_user

async def delete_user(user_id: int, db: Session):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(db_user)
    db.commit()

