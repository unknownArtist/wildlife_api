# Crypto BOT 

A modular FastAPI application with SQLAlchemy, Alembic, and PostgreSQL, all containerized with Docker.

## Features

- FastAPI for API development
- SQLAlchemy for ORM
- Alembic for database migrations
- PostgreSQL as the database
- Docker and Docker Compose for containerization
- Poetry for dependency management

## Requirements

- Docker and Docker Compose
- Python 3.11+
- Poetry (optional for local development)

## Getting Started

### Using Docker (Recommended)

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd crypto
   ```

2. Start the application with Docker Compose:
   ```bash
   docker-compose up -d
   ```

3. The API will be available at http://localhost:8000

4. API documentation is available at:
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

### Local Development with Poetry

1. Install Poetry (if not already installed):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Run the setup script:
   ```bash
   ./setup_dev.sh
   ```

3. Activate the Poetry shell:
   ```bash
   poetry shell
   ```

4. Run database migrations:
   ```bash
   alembic upgrade head
   ```

5. Start the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

## Project Structure

```
.
├── alembic.ini                  # Alembic configuration
├── app                          # Application package
│   ├── api                      # API endpoints
│   │   └── api_v1               # API v1 endpoints
│   │       ├── api.py           # API router
│   │       └── endpoints        # API endpoint modules
│   │           ├── items.py     # Items endpoints
│   │           └── users.py     # Users endpoints
│   ├── core                     # Core modules
│   │   └── config.py            # Configuration settings
│   ├── db                       # Database modules
│   │   ├── base.py              # Base for models
│   │   ├── base_class.py        # Base class for models
│   │   └── session.py           # Database session
│   ├── main.py                  # Main application
│   ├── models                   # SQLAlchemy models
│   │   ├── item.py              # Item model
│   │   └── user.py              # User model
│   └── schemas                  # Pydantic schemas
│       ├── item.py              # Item schemas
│       └── user.py              # User schemas
├── config                       # Configuration files
│   ├── .env                     # Environment variables
│   └── .env.example             # Example environment variables
├── docker-compose.yml           # Docker Compose configuration
├── Dockerfile                   # Docker configuration
├── migrations                   # Alembic migrations
│   ├── env.py                   # Alembic environment
│   ├── script.py.mako           # Alembic script template
│   └── versions                 # Migration versions
├── pyproject.toml               # Python project configuration
├── requirements.txt             # Python dependencies
├── setup.py                     # Setup script
└── setup_dev.sh                 # Development setup script
```

## Database Migrations

To create a new migration:

```bash
alembic revision --autogenerate -m "Description of the migration"
```

To apply migrations:

```bash
alembic upgrade head
```

## Using Poetry for Dependency Management

Poetry is a fast Python package installer and resolver. Here are some common commands:

- Install a package:
  ```bash
  poetry add <package-name>
  ```

- Install all dependencies:
  ```bash
  poetry install
  ```

- Create a virtual environment:
  ```bash
  poetry env use python3.11
  ```

- Install the project in development mode:
  ```bash
  poetry install --extras "dev"
  ``` 