import models
from fastapi import FastAPI, Depends, Request
from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi_pagination import Page, add_pagination, paginate
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class Events(BaseModel):
    original_id: str
    talent_id: Optional[str]
    talent_name: Optional[str]
    talent_grade: Optional[str]
    booking_grade: Optional[str]
    operating_unit: str
    office_city: Optional[str]
    office_postal_code: str
    job_manager_name: Optional[str]
    job_manager_id: Optional[str]
    total_hours: float
    start_date: datetime
    end_date: datetime
    client_name: Optional[str]
    client_id: str
    industry: Optional[str]
    required_skills: Optional[str]
    optional_skills: Optional[str]
    is_unassigned: Optional[bool]
    class Config:
        orm_mode = True


@app.get("/", response_model=Page[Events])
def list_records(
    request: Request, db: Session = Depends(get_db),
    search_term: Optional[str] = None,
    sort_by_date: Optional[str] = None
    ):
    if search_term:
        filters = {"operating_unit": search_term}
        if sort_by_date:
            events = db.query(models.Events).filter_by(**filters).order_by(models.Events.start_date).all()
        else:
            events = db.query(models.Events).filter_by(**filters).all()
    else:
        if sort_by_date:
            events = db.query(models.Events).order_by(models.Events.start_date).all()
        else:
            events = db.query(models.Events).all()

    if not events:
        message = "No events found!"
        return templates.TemplateResponse("index.html", {"request": request, "events": [], "message": message})

    return templates.TemplateResponse("index.html", {"request": request, "events": paginate(events)})


add_pagination(app)
