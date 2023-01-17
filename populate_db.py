import json
from models import Events
from fastapi import Depends
from database import SessionLocal
from sqlalchemy.orm import Session
from datetime import datetime


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def save_rec(model, db: Session = next(get_db()), **kwargs):
    try:
        db.add(model)
        db.commit()
    except:
        pass


f = open('planning.json')
data = json.load(f)
ctr = 0
for event in data:

    event_model = Events()
    # event_model.parse_obj(event)
    event_model.original_id = event["originalId"]
    event_model.talent_id = event["talentId"]
    event_model.talent_name = event["talentName"]
    event_model.talent_grade = event["talentGrade"]
    event_model.booking_grade = event["bookingGrade"]
    event_model.operating_unit = event["operatingUnit"]
    event_model.office_city = event["officeCity"]
    event_model.office_postal_code = event["officePostalCode"]
    event_model.job_manager_name = event["jobManagerName"]
    event_model.job_manager_id = event["jobManagerId"]
    event_model.total_hours = event["totalHours"]
    start_date = datetime.strptime(event["startDate"], '%m/%d/%Y %I:%M %p')
    end_date = datetime.strptime(event["endDate"], '%m/%d/%Y %I:%M %p')
    event_model.start_date = start_date
    event_model.end_date = end_date
    event_model.client_name = event["clientName"]
    event_model.client_id = event["clientId"]
    event_model.industry = event["industry"]

    reqs = ""
    for skill in event["requiredSkills"]:
        reqs += str(skill) + "; "
    event_model.required_skills = reqs

    optionals = ""
    for skill in event["optionalSkills"]:
        optionals += str(skill) + "; "
    event_model.optional_skills = optionals

    event_model.is_unassigned = event["isUnassigned"]

    save_rec(model=event_model)
    ctr += 1

print(str(ctr) + " records processed.")
