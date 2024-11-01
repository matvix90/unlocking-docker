# Docker Compose with Django
A simple guide to using Docker Compose for deploying and managing Django applications in development and production environments.

## Table of Contents
- [Requirements](#requirements)
- [Development](#development)
- [Production](#production)

## Requirements

Before you begin, ensure you have the following installed on your host:
- [Docker](https://docs.docker.com/get-docker/)

## Development
To set up your Django application in a development environment, run the following command:

### Start Containers
Run the following command to start your development containers:

```
docker compose -f compose.dev.yaml -p django-dev up --build -d
```

### Start Tailwind
Run the following command to start Tailwind:

```
docker compose -f compose.prod.yaml -p django-dev exec app sh -c "cd tailwind && npm run build"
```

## Production
To set up your Django application in a production environment, run the following command:

### Start Containers
Run the following command to start your development containers:

```
docker compose -f compose.prod.yaml -p django-project up --build -d
```

### View Running Containers
To see the list of currently running containers, use:

```
docker compose -f compose.prod.yaml -p django-project ps
```
### Prepare the Django Application
Make your Django app ready by running the following commands:

```
docker compose -f compose.prod.yaml -p django-project exec app sh -c "python manage.py migrate"

docker compose -f compose.prod.yaml -p django-project exec app sh -c "python manage.py collectstatic --clear"
```
