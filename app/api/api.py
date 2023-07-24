from fastapi import FastAPI

from app.api.routes.authentication import router as auth_router
from app.api.routes.tasks import router as tasks_router
from app.api.routes.users import router as users_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(tasks_router, prefix="/tasks", tags=["Tasks"])
app.include_router(users_router, prefix="/users", tags=["Users"])
