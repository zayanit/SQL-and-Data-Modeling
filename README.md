# SQL and Data Modeling

A collection of Python examples demonstrating SQLAlchemy ORM, relational database modeling, and Flask integration. This repository was created for learning and experimenting with different database design concepts, relationships, and CRUD operations.

## Features

* SQLAlchemy ORM fundamentals
* Database modeling best practices
* One-to-One relationships
* One-to-Many relationships
* Many-to-Many relationships
* Querying with SQLAlchemy
* Flask integration
* Simple Todo application example

## Project Structure

```
.
├── todoapp/                  # Flask Todo application
├── demo.py                   # SQLAlchemy basics
├── demo1.py                  # Additional ORM examples
├── demo2Query.py             # Query examples
├── driver_vehicle.py         # Driver & Vehicle relationship model
├── many-to-many-ex.py        # Many-to-Many relationship example
├── flask_hello_app.py        # Basic Flask application
└── README.md
```

## Technologies Used

* Python
* SQLAlchemy
* Flask
* SQLite
* HTML
* Mako Templates

## Getting Started

### Clone the repository

```bash
git clone https://github.com/zayanit/SQL-and-Data-Modeling.git
cd SQL-and-Data-Modeling
```

### Create a virtual environment

Linux/macOS

```bash
python -m venv venv
source venv/bin/activate
```

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

> If a `requirements.txt` file is not available, install the required packages manually:

```bash
pip install flask sqlalchemy
```

## Learning Topics

This repository demonstrates:

* Creating database models using SQLAlchemy
* Defining primary and foreign keys
* Working with ORM relationships
* Executing CRUD operations
* Writing SQLAlchemy queries
* Integrating SQLAlchemy with Flask applications

## Future Improvements

* Add comprehensive documentation
* Add unit tests
* Add Docker support
* Add Alembic migrations
* Improve project organization
* Expand Flask application features

## License

This project is intended for educational purposes. Feel free to use the code as a learning resource.


