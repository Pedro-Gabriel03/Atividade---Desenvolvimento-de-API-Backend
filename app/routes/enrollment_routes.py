from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.enrollment import (
    EnrollmentCreate,
    EnrollmentResponse
)
from app.services.enrollment_service import EnrollmentService


router = APIRouter(
    prefix="/enrollments",
    tags=["Enrollments"]
)

service = EnrollmentService()


@router.post(
    "",
    response_model=EnrollmentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_enrollment(
    enrollment: EnrollmentCreate,
    db: Session = Depends(get_db)
):
    return service.create_enrollment(
        db,
        enrollment.user_id,
        enrollment.course_id
    )