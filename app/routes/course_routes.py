from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.course import (
    CourseCreate,
    CourseResponse,
    CourseUpdate
)
from app.services.course_service import CourseService


router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)

service = CourseService()


@router.post(
    "",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED
)
def create_course(
    course: CourseCreate,
    db: Session = Depends(get_db)
):
    return service.create_course(
        db,
        course.title,
        course.description,
        course.workload
    )


@router.get(
    "",
    response_model=list[CourseResponse]
)
def get_courses(
    db: Session = Depends(get_db)
):
    return service.get_courses(db)


@router.get(
    "/{course_id}",
    response_model=CourseResponse
)
def get_course(
    course_id: int,
    db: Session = Depends(get_db)
):
    return service.get_course(db, course_id)


@router.put(
    "/{course_id}",
    response_model=CourseResponse
)
def update_course(
    course_id: int,
    course: CourseUpdate,
    db: Session = Depends(get_db)
):
    return service.update_course(
        db,
        course_id,
        course.title,
        course.description,
        course.workload
    )


@router.delete(
    "/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_course(
    course_id: int,
    db: Session = Depends(get_db)
):
    service.delete_course(db, course_id)

    return None