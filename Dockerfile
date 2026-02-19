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

# Environment setup
ENV PYTHONUNBUFFERED=1
ENV PATH="/app/.venv/bin:$PATH"

# Copy project files
COPY . .

# Now collectstatic will find Django in the virtual environment
RUN python manage.py collectstatic --noinput

# Copy and prepare the entrypoint script
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

# Run command
CMD ["./entrypoint.sh"]
