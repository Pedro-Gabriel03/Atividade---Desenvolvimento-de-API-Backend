from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.enrollment import Enrollment
from app.repositories.course_repository import CourseRepository
from app.repositories.enrollment_repository import EnrollmentRepository
from app.repositories.user_repository import UserRepository


class EnrollmentService:

    def __init__(self):
        self.enrollment_repository = EnrollmentRepository()
        self.user_repository = UserRepository()
        self.course_repository = CourseRepository()

    def create_enrollment(
        self,
        db: Session,
        user_id: int,
        course_id: int
    ):
        user = self.user_repository.get_by_id(db, user_id)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        course = self.course_repository.get_by_id(
            db,
            course_id
        )

        if not course:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Course not found"
            )

        existing_enrollment = (
            self.enrollment_repository
            .get_by_user_and_course(
                db,
                user_id,
                course_id
            )
        )

        if existing_enrollment:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User is already enrolled in this course"
            )

        enrollment = Enrollment(
            user_id=user_id,
            course_id=course_id
        )

        return self.enrollment_repository.create(
            db,
            enrollment
        )