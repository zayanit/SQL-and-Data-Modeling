# Repository Guidelines

## Project Structure & Module Organization

The root Python files are independent data-modeling exercises: `demo.py` and `demo1.py` use psycopg2, while `demo2Query.py`, `driver_vehicle.py`, and `many-to-many-ex.py` demonstrate Flask-SQLAlchemy queries and relationships. `flask_hello_app.py` is a small Flask example. The working Todo application lives in `todoapp/`: routes and models are in `app.py`, the page and its JavaScript are in `templates/index.html`, and schema revisions are in `migrations/versions/`. Dependencies are listed in `todoapp/requirements.txt`. There is currently no test directory or shared asset pipeline.

## Setup, Run, and Migration Commands

Run these from `todoapp/` unless stated otherwise:

```bash
python3 -m venv env
source env/bin/activate
python -m pip install -r requirements.txt
createdb todoapp
FLASK_APP=app.py flask db upgrade
python app.py
```

The app expects a local PostgreSQL server at `127.0.0.1:5432` and connects as user `zayan`; adjust the connection string in `app.py` for your local setup. `flask db upgrade` applies committed schema revisions. After changing models, use `FLASK_APP=app.py flask db migrate` to generate a revision, inspect it, then run `flask db upgrade`. Root examples use their own hard-coded PostgreSQL databases, so create the database named in a script before running it. There is no build command.

## Coding Style & Naming Conventions

Use `snake_case` for Python modules, functions, and variables; use `PascalCase` for ORM models. Use four spaces in new Python code. Existing `todoapp/app.py` functions use tabs, so preserve their local indentation when making narrow edits. Keep model table names and foreign keys consistent with the migrations. No formatter or linter is configured.

## Testing Guidelines

No automated test framework or coverage target is configured. For changes to Todo behavior, start the app and manually verify the affected route and page interaction, including database persistence. For schema changes, apply the migration to a local disposable database and check the resulting tables. If adding tests, place them under `tests/` with `test_*.py` names and document how to run them.

## Commit & Pull Request Guidelines

Recent commits use short, descriptive subjects such as `Revise README for clarity and detail` and `Bump werkzeug from ...`. Keep commits focused and state the change in the subject. In pull requests, describe the behavior changed, database or migration impact, and checks performed; link a relevant issue and include screenshots when the Todo page changes. Do not commit local database credentials or generated environment files.
