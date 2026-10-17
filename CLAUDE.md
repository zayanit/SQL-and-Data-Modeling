# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A learning/scratch repo (from Udacity's Full Stack Web Developer Nanodegree) for SQL, psycopg2, and Flask-SQLAlchemy data modeling. There is no test suite, linter, or build step. The only real application is `todoapp/`; the top-level `.py` files are standalone exercises that don't import one another.

## Database

Everything targets a **local PostgreSQL on 127.0.0.1:5432**, not SQLite as the root README claims. Connection strings are hardcoded in each file, with user `zayan`. Each script uses its own database:

| File | Database | What it shows |
|---|---|---|
| `demo.py`, `demo1.py` | `example`, `example2` | Raw psycopg2: DDL, parameterized inserts, fetchone/fetchmany/fetchall |
| `flask_hello_app.py`, `demo2Query.py` | `flaskdemodb` | Flask-SQLAlchemy basics; `demo2Query.py` keeps its REPL query/session-lifecycle notes in comments |
| `driver_vehicle.py` | `example` | One-to-many (`db.relationship` + `backref`) |
| `many-to-many-ex.py` | `todoapp` | Many-to-many through an association `db.Table` |
| `todoapp/app.py` | `todoapp` | Full CRUD app |

Create a database before running a script against it: `createdb <name>`. Several scripts call `db.create_all()` at import time. That works with the pinned Flask-SQLAlchemy 2.4.1, but newer versions would need an app context.

## todoapp

```bash
cd todoapp
python3 -m venv env && source env/bin/activate
pip install -r requirements.txt     # on macOS, psycopg2 may need `brew install libpq` first
python3 app.py                      # http://127.0.0.1:5000, debug mode
```

Unlike the scratch scripts, the todoapp schema is managed with **Flask-Migrate/Alembic** (`migrations/`). Run these from `todoapp/` so that `app.py` is found:

```bash
FLASK_APP=app.py flask db upgrade      # apply migrations
FLASK_APP=app.py flask db migrate      # autogenerate a revision after changing models
```

Everything is in `app.py`:
- Models: `TodoList` (`todolists`) has many `Todo` (`todos`), with backref `todo.list`.
- `/` redirects to `/lists/1`. `GET /lists/<id>` renders `templates/index.html` with all lists, the active list, and that list's todos.
- Mutations are JSON endpoints called with `fetch()` from inline JS in `index.html`: create, delete, and set-completed for both todos and lists. Every handler uses the same pattern: try/commit, rollback on error, close the session in `finally`, then `abort(500)` or return JSON.

### Known inconsistencies

Watch for these when editing:
- The latest migration (`9b3b3bca4f71`) renamed the column `todos.completed` to `complete`. The model attribute is `complete`, but the routes (`/set-completed`), the JSON payload key (`completed`) and the CSS classes still say "completed". Assigning `todo.completed` would set a plain Python attribute and persist nothing.
- `/todos/<id>/set-complete` (`update_todo`) is an unused older duplicate of `/todos/<id>/set-completed`. The template only calls the latter.
- Some handlers use `except():`, which catches nothing, instead of `except:`.
