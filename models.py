from database import Base
from typing import Any
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, \
                       Table, ForeignKey, ARRAY
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy.orm import relationship


@as_declarative()
class Base():
    id: Any
    __name__: str

    class Config:
        orm_mode = True

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class Events(Base):
    id = Column(Integer, primary_key=True, index=True)
    original_id = Column(String, unique=True, nullable=False)
    talent_id = Column(String)
    talent_name = Column(String)
    talent_grade = Column(String)
    booking_grade = Column(String)
    operating_unit = Column(String, nullable=False)
    office_city = Column(String)
    office_postal_code = Column(String, nullable=False)
    job_manager_name = Column(String)
    job_manager_id = Column(String)
    total_hours = Column(Float, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    client_name = Column(String)
    client_id = Column(String, nullable=False)
    industry = Column(String)
    required_skills = Column(String)
    optional_skills = Column(String)
    is_unassigned = Column(Boolean)
