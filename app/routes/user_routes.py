from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.core.database import get_db
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

service = UserService()


@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return service.create_user(
        db,
        user.name,
        user.email
    )


@router.get(
    "",
    response_model=list[UserResponse]
)
def get_users(
    db: Session = Depends(get_db)
):
    return service.get_users(db)


@router.get(
    "/{user_id}",
    response_model=UserResponse
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    return service.get_user(db, user_id)


@router.put(
    "/{user_id}",
    response_model=UserResponse
)
def update_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db)
):
    return service.update_user(
        db,
        user_id,
        user.name,
        user.email
    )


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    service.delete_user(db, user_id)

@router.get("/{user_id}/courses")
def get_user_courses(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = service.repository.get_with_courses(
        db,
        user_id
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    courses = [
        enrollment.course
        for enrollment in user.enrollments
    ]

    return {
        "success": True,
        "message": "User courses retrieved successfully",
        "data": {
            "user": {
                "id": user.id,
                "name": user.name,
                "email": user.email
            },
            "courses": [
                {
                    "id": course.id,
                    "title": course.title,
                    "description": course.description,
                    "workload": course.workload
                }
                for course in courses
            ]
        }
    }
    return None