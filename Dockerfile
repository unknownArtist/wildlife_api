FROM python:3.11-slim

WORKDIR /app/

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    POETRY_VERSION=1.7.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s /opt/poetry/bin/poetry /usr/local/bin/poetry \
    && poetry --version

# Upgrade pip and install poetry
RUN python -m pip install --upgrade pip
# Copy poetry configuration files
COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.create false
# Install dependencies
RUN poetry install --no-interaction --no-ansi --no-root

# Copy project
COPY . .

# Install the project
RUN poetry install --no-interaction --no-ansi

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3000"] 