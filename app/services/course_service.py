from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.course import Course
from app.repositories.course_repository import CourseRepository


class CourseService:

    def __init__(self):
        self.repository = CourseRepository()

    def create_course(
        self,
        db: Session,
        title: str,
        description: str,
        workload: int
    ):
        course = Course(
            title=title,
            description=description,
            workload=workload
        )

        return self.repository.create(db, course)

    def get_courses(self, db: Session):
        return self.repository.get_all(db)

    def get_course(self, db: Session, course_id: int):
        course = self.repository.get_by_id(db, course_id)

        if not course:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Course not found"
            )

        return course

    def update_course(
        self,
        db: Session,
        course_id: int,
        title: str,
        description: str,
        workload: int
    ):
        course = self.get_course(db, course_id)

        course.title = title
        course.description = description
        course.workload = workload

        db.commit()
        db.refresh(course)

        return course

    def delete_course(self, db: Session, course_id: int):
        course = self.get_course(db, course_id)

        self.repository.delete(db, course)