# Base Image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/
RUN rm /app/requirements.txt

# Run Django server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "docker.wsgi:application"]
