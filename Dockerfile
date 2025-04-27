FROM python:3.11-slim

WORKDIR /app/

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    POETRY_VERSION=1.7.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    # Add Oracle Instant Client path
    LD_LIBRARY_PATH=/opt/oracle/instantclient_21_13

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev curl libaio1 unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# --- Oracle Instant Client Installation ---
RUN mkdir -p /opt/oracle \
    && cd /opt/oracle \
    # Download Instant Client Basic Light and SQL*Plus packages (adjust version if needed)
    && curl -o instantclient-basiclite.zip https://download.oracle.com/otn_software/linux/instantclient/2113000/instantclient-basiclite-linux.x64-21.13.0.0.0dbru.zip \
    && curl -o instantclient-sqlplus.zip https://download.oracle.com/otn_software/linux/instantclient/2113000/instantclient-sqlplus-linux.x64-21.13.0.0.0dbru.zip \
    # Unzip packages
    && unzip instantclient-basiclite.zip \
    && unzip instantclient-sqlplus.zip \
    # Remove zip files
    && rm -f instantclient-basiclite.zip instantclient-sqlplus.zip \
    # Create symbolic link (needed by some applications)
    && cd instantclient_21_13 
    # && ln -s libclntsh.so.21.1 libclntsh.so
# --- End Oracle Instant Client Installation ---

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