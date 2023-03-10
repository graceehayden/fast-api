## Trying out FastAPI

A simple backend application that provides an API for a dashboard which
allows a planner to get insights into client and planning information.
Includes examples of pagination, sorting, filtering.

Test data in `planning.json`. Imported with 'populate_db.py'.

## Stack: 
* Python 3.11
* FastAPI
* SQLAlchemy (sqlite)

##### NOTES #####
Steps to run this implementation:
 - start up virtual environment  (python3 -m venv venv; source venv/bin/activate)
 - run “pip install -r requirements.txt”
 - run "python3 -m uvicorn events:app --reload"
 - visit the home page so the tables will be created (127.0.0.1:8000/)
 - stop server and run "python3 populate_db.py" to populate the DB (records processed message will display when it's done)
 - restart server and visit the refreshed home page
