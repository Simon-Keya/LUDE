from dotenv import load_dotenv
load_dotenv()  # Load variables from .env file

from fastapi import FastAPI
from .api.routes import tasks, task_assignments, task_status, users,authentication, comments,notifications, projects, template, tags, search
from app.core.config import Settings


settings = Settings()

def create_app() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME, debug=settings.DEBUG)

    # Include API routes
    app.include_router(authentication.router, prefix="/api")
    app.include_router(users.router, prefix="/api")
    app.include_router(tasks.router, prefix="/api")
    app.include_router(task_assignments.router, prefix="/api")
    app.include_router(task_status.router, prefix="/api")
    app.include_router(comments.router, prefix="/api")
    app.include_router(notifications.router, prefix="/api")
    app.include_router(projects.router, prefix="/api")
    app.include_router(template.router, prefix="/api")
    app.include_router(tags.router, prefix="/api")
    app.include_router(search.router, prefix="/api")

    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
