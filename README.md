# Technical Assessment - Chemify. Quick summary:
Write a REST API which will manage tasks, each task is assigned to a user. Each user is only able to see their own tasks. A task can only have one status at a time.
* Tasks.
    * Tasks have status:
        * Pending.
        * Doing.
        * Blocked.
        * Done.
    * Tasks can be deleted (archived).
* Users.
    * Users have private tasks.

# Requirements:
* Python 3.9 and 3.10 support.
* Formatting, use Black.
* Type annotations (Pydantic).
* Light-weight framework (FastAPI).
* DB (SQLite).
* DB managed by code with migrations (SQLAlchemy, Alembic).
## Bonus:
* Sub-tasks
* Un-deleting
* Due dates
* Labels
* Documentation illustrating the design and thought process for the implemented solution
# Implementation:
## What was implemented:
* Base requirements
* Labels
* Documentation illustrating the design and thought process for the implemented solution
## Not implemented:
* Sub-tasks
* Un-deleting
* Due dates
## Tech:
* Poetry
* FastAPI
* Pydantic
* SQLAlchemy
* Alembic
* SQLite
* Black
* Pytest
## Models:
* User
* Task
* Label
## Bare bones approach. REST API implementation:
* /tasks/
    * PUT to create tasks.
    * DELETE to delete tasks.
    * GET to get tasks that belong to you (check for due date).
    * PATCH /status/ to move tasks along status.
    * PATCH /restore/ to un-delete tasks.
* /users/
    * PUT to create User.
    * POST to get a user authentication token.
## Future considerations:
* User authentication. Was initially in-scope, but dropped due to time constraints.
* Write comprehensive tests.
* Production WSGI server. Gunicorn.
* Production SQL database. PostgreSQL.
* Email confirmation for new users. SMTP server.
* Hash passwords. 
* Async to not block on db operations. Asyncio.
# Getting started:
## Prerequisites:
* Python ^3.9.
* Poetry.
## Running the application
* Run
    * ```python3 -m poetry run fastapi dev tech_assessment/main.py```
* Test
    * ```python3 -m poetry run pytest```
* Lint
    * ```python3 -m poetry run black .```
* Make db migrations:
    * ```python3 -m poetry run alembic revision --autogenerate -m "Migration message"```
* Apply db migrations:
    * ```python3 -m poetry run alembic upgrade head```
## Using the application
* Start the application (Using run as above).
* Go to calhost:8000/docs (or whatever is otherwise specified by the server console).
* Use API as documented.
    * Ideally:
        * Create a User (or two)
        * Create Labels
        * Create Tasks
        * Perform operations on Tasks
