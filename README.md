# Wildlife BOT 

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
   cd wild_life_api
   ```

2. Start the application with Docker Compose:
   ```bash
   docker-compose up -d
   ```

3. Create a migrations
   ```bash
   docker compose api alembic revision --autogenerate -m "table create" 
   ```

4. Run a migration
   ```bash
   docker compose exec api alembic upgrade head
   ```

5. Check the logs of the containers
   ```bash
   docker compose logs -f
   ```
6. To create a new migration:

   ```bash
   alembic revision --autogenerate -m "Description of the migration"
   ```

   To apply migrations:

   ```bash
   alembic upgrade head
   ```

3. The API will be available at http://localhost:3000

4. API documentation is available at:
   - Swagger UI: http://localhost:3000/docs
   - ReDoc: http://localhost:3000/redoc



## Project Structure

```
├── Dockerfile
├── README.md
├── alembic.ini
├── app
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py
│   │   └── api_v1
│   │       ├── __init__.py
│   │       ├── api.py
│   │       └── endpoints
│   │           ├── __init__.py
│   │           ├── auth.py
│   │           ├── users.py
│   │           └── wildlife.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── logging.py
│   ├── db
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── base_class.py
│   │   └── session.py
│   ├── dependencies.py
│   ├── main.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── wildlife.py
│   ├── repositories
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── wildlife.py
│   ├── schemas
│   │   ├── __init__.py
│   │   ├── token.py
│   │   ├── user.py
│   │   └── wildlife.py
│   ├── services
│   │   └── __init__.py
│   └── utils
│       ├── __init__.py
│       └── security.py
├── app.log
├── docker-compose.yml
├── env.example
├── migrations
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       ├── 2b4a1e2b4ec5_table_updated.py
│       ├── 5141a9d237c7_table_updated.py
│       └── bd154bb1b29d_table_updated.py
├── my.log
├── poetry.lock
└── pyproject.toml
```
