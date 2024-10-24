# Multi-container-app

## Mount Volume (Persistent Data Storage)

```
docker run -dp 127.0.0.1:8000:8000 --name django-app --mount type=volume,source=django_db,target=/app django
```

### Step-by-Step Breakdown:

- type=volume: This specifies that the mount is a Docker volume.

- source=django_db: defines the name of the volume you want to use or create.

- target= specifies the location inside the container where you want the source to be mounted.

- django= the name of the Docker image that you're running.

## Mount Bind (Development)

```
docker run -dp 127.0.0.1:8000:8000 --name django-app --mount type=bind,source="$(pwd)",target=/app django
```

### Step-by-Step Breakdown:

- type=bind: This defines the type of mount. There are different types, but in this case, bind means you are binding a directory or file from the host (your local machine) to a directory or file inside the container.

- source=$(pwd): specifies the path on your host machine that you want to bind, $(pwd) is a shell command that returns the present working directory.

- target= specifies the location inside the container where you want the source to be mounted.

- django= the name of the Docker image that you're running.

## Create a network

```
docker network create django-network
```

## Create a postgres database and connect to the custom network

```
$ docker run -d \
	--name django-postgres \
  --network django-network --network-alias postgres \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=admin \
  -e POSTGRES_DB=djangodata \
  -v django-data-volume:/var/lib/postgresql/data \
	postgres
```

### How to manage psql:

```
-- enter in psql

psql -U admin -d djangodata

-- show list of database

\l

-- show list of tables

\dt

-- show table's row

SELECT * FROM docker_tag;

-- exit

\q
```

## Create an app container and connect to the custom network

```
docker run -dp 127.0.0.1:8000:8000 \
  --name django-app \
  -w /app -v "$(pwd):/app" \
  --network django-network \
  django
```

## Create nginx container

```
docker run -dp 80:80 \
  --name nginx-cont \
  --network django-network \
  nginx
```
