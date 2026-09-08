from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from app.core.database import Base


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    description = Column(Text, nullable=False)
    workload = Column(Integer, nullable=False)

    enrollments = relationship(
        "Enrollment",
        back_populates="course",
        cascade="all, delete-orphan"
    )