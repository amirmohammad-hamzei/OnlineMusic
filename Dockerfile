# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip



# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files (INCLUDING manage.py)
COPY . .

# Run migrations and collect static files
RUN python manage.py migrate --noinput && \
    python manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8000

# Start the gunicorn server
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]