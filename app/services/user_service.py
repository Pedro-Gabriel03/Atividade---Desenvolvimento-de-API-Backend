from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import UserRepository


class UserService:

    def __init__(self):
        self.repository = UserRepository()

    def create_user(
        self,
        db: Session,
        name: str,
        email: str
    ):
        existing_user = self.repository.get_by_email(db, email)

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered"
            )

        user = User(
            name=name,
            email=email
        )

        return self.repository.create(db, user)

    def get_users(self, db: Session):
        return self.repository.get_all(db)

    def get_user(self, db: Session, user_id: int):
        user = self.repository.get_by_id(db, user_id)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        return user

    def update_user(
        self,
        db: Session,
        user_id: int,
        name: str,
        email: str
    ):
        user = self.get_user(db, user_id)

        existing_user = self.repository.get_by_email(db, email)

        if existing_user and existing_user.id != user_id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered"
            )

        user.name = name
        user.email = email

        db.commit()
        db.refresh(user)

        return user

    def delete_user(self, db: Session, user_id: int):
        user = self.get_user(db, user_id)

        self.repository.delete(db, user)