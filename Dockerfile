# Python 3.12 (uv compatible)
FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
  libpq-dev gcc \
  && rm -rf /var/lib/apt/lists/*

# Install uv from official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Set work directory
WORKDIR /app

# Copy dependency files first (caching layer)
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-install-project

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Environment setup
ENV PYTHONUNBUFFERED=1
ENV PATH="/app/.venv/bin:$PATH"

# Run command (Port 8080 is default for Cloud Run)
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8080"]
