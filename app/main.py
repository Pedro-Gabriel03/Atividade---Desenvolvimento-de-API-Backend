from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException

from app.core.database import Base, engine
from app.core.exceptions import (
    http_exception_handler,
    validation_exception_handler
)
from app.models import User, Course, Enrollment
from app.routes.user_routes import router as user_router
from app.routes.course_routes import router as course_router
from app.routes.enrollment_routes import router as enrollment_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="StudyManager API",
    description="API RESTful para gerenciamento de usuários, cursos e matrículas",
    version="1.0.0"
)


app.add_exception_handler(
    HTTPException,
    http_exception_handler
)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)


app.include_router(user_router)
app.include_router(course_router)
app.include_router(enrollment_router)


@app.get("/")
def root():
    return {
        "success": True,
        "message": "StudyManager API is running",
        "data": None
    }