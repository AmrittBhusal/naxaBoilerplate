# Django Template in Docker

## Notes before starting

### Place core features of the application in core app and build APIs in the same app's viewsets and serializers files.

### If the application is large divide it into smaller apps (Add according to you need.)

### Pre-commit

We use pre-commit to enforce strict clean code convention.

**Setting up Pre-commit**

**1. Install on your system**

```bash
$ pip install pre-commit
```

**2. After installing on host machine you need to install hooks on your project**

```bash
$ pre-commit install-hooks
$ pre-commit run --all-files --all

```

**3. Updating pre-commit hooks**

```bash
$ pre-commit autoupdate
```

**4. Installing pre-commit hooks on so git uses them**

```bash
$ pre-commit install
```

**5. Steps to validate commit with pre-commit**

```bash
$ git status # review changes
$ git diff # review crucial changes
$ git add . # stage changes
$ pre-commit run --all-files --all ## This will modify files in your code if pre-commit test fails (EX: black fixing code indentions) and you need to stage code again
#=====Optional Steps if pre-commit fails START=====#
$ git status # review changes made by pre-commit
$ git add . # Re stage changes made by pre-commit
#=====Optional Steps if pre-commit fails END=====#
$ git commit
$ git push origin <BRANCH>
```

> _Reference:_ https://wiki.naxa.com.np/en/git/pre-commit \
> **Note** Your project must pass pre-commit hook and it will be validated on github too via Actions.

### Setting up project

You can build the repository according to your needs.

# Setup Process

## Git

Clone this repository

```sh
$ git clone https://github.com/naxa-developers/naxa-backend-template --depth=1
```

If yours is a gis project, that needs playing with large gis data or uses libraries like geoserver, gcc.

```sh
$ cp dependencies/apt_requirements_gis.txt apt_requirements.txt
$ cp dependencies/requirements_gis.txt requirements.txt
```

If yours is a non-gis project. i.e. Does not have whole lot of gis data, or does not use libraries like geoserver, gcc etc.
Even if you need simple gis db fields like PointField from django.contrib.gis.db, you can build this version. This version also includes GDAL.

```sh
$ cp dependencies/apt_requirements_nongis.txt apt_requirements.txt
$ cp dependencies/requirements_nongis.txt requirements.txt
```

## Docker

Install [docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/) in your system.
Create a local copy of `docker-compose.local.yml` on your machine.

```bash
$ cp docker/docker-compose.local.yml docker-compose.yml
```

Also make a copy of `env_sample` to `.env` and use it for setting environment variables for your project.

```bash
$ cp env_sample .env
$ nano .env			    # Edit .env and set environment variables for django project as per requirement
```

If you are using geoserver, create env for the same

```bash
$ cp geoserver_env_sample.txt geoserver_env.txt
$ nano geoserver_env.txt	# Edit geoserver_env.txt and set environment variables for geoserver as per requirement
```

Then start the containers from main compose file

```bash
$ docker compose up -d --build		#  Will create all necessary services
  Starting db ... done
  Starting web   ... done
  .....
  .....
  Starting worker  ... done
```

Go to the postgres database container if you are using one and create database according to credential provided in env file.
You project should be running now

To stop all running containers

```bash
$ docker compose stop			# Will stop all running services
    Stopping db ... done
    Stopping web   ... done
    Stopping worker  ... done
```

## Django

Once you have created all necessary services. You may want to perform some tasks on Django server like `migrations`, `collectstatic` & `createsuperuser`.
Use these commands respectively.

```bash
$ docker exec -it <CONTAINER_NAME> bash		# Get a shell on container from docker
$ docker compose exec web bash		# Get a shell on container from docker compose
root@<container>$ python3 manage.py collectstatic 	# Collecting static files
root@<container>$ python3 manage.py migrate		# Database migrate
root@<container>$ python3 manage.py createsuperuser	# Creating a superuser for login.
```

### Error

**Getting 502 Bad Gateway Error?**

Stop all running containers and recreate the services again using command below:

```bash
$ docker compose up -d --force-recreate
```

OR,

```bash
$ docker compose up -d web --force-recreate
$ docker compose up -d nginx --force-recreate
```

Now you should be able to access your django server on http://django.localhost.

![Django Server](https://private-user-images.githubusercontent.com/58771387/289471900-24f3d35d-521d-449d-8bfb-2c708b8c1455.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDIyODM4NTcsIm5iZiI6MTcwMjI4MzU1NywicGF0aCI6Ii81ODc3MTM4Ny8yODk0NzE5MDAtMjRmM2QzNWQtNTIxZC00NDlkLThiZmItMmM3MDhiOGMxNDU1LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzEyMTElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMjExVDA4MzIzN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTdmZjhmMTc5YmJlZjg2NzY4OGQzM2QzOGFhZWJhMDk1NTVkMzQ3MTRjNzk5YjQ3ODJlNzk5MDViYzEyNjIwYTQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.V0fnkqdaExda6Mos3isiNVIqhW2c_z2gXqIkS11YTxA)

And, django admin panel on http://django.localhost/admim.

![Django Admin](https://private-user-images.githubusercontent.com/58771387/289476414-4c37e6fb-d947-4228-836b-91af145335d1.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDIyODQ4NzYsIm5iZiI6MTcwMjI4NDU3NiwicGF0aCI6Ii81ODc3MTM4Ny8yODk0NzY0MTQtNGMzN2U2ZmItZDk0Ny00MjI4LTgzNmItOTFhZjE0NTMzNWQxLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzEyMTElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMjExVDA4NDkzNlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPThhMTA0OGEwODgwNTcyMTA4MGQ3NTY1MThlMjFlNTE0YzE5ZmQ4MDQ4NGViZDNlYjY4NDZlMzkzNDAxZjc3NjMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.IrW2OqcF8xbeeYwqpcoyBVFkxHnOAQ0d0esGKlIis9M)

## Postgresql

In case if you want to use a local postgresql server instead on running a docker container.
First verify if `postgresql` is installed.

```bash
$ psql -V
psql (PostgreSQL) <PostgreSQL_Version>
```

Edit `postgresql.conf` file to allow listening to other IP address.

```bash
$ sudo nano /etc/postgresql/<PostgreSQL_Version>/main/postgresql.conf
listen_addresses = '*'          # what IP address(es) to listen on;
```

Now you will need to allow authentication to `postgresql` server by editing `pg_hba.conf`.

```bash
$ sudo nano /etc/postgresql/<PostgreSQL_Version>/main/pg_hba.conf
```

Find `host all all 127.0.0.1/32 md5` and change it to `host all all 0.0.0.0/0 md5` \
_It can be `sha` on new version of PostgreSQL_

Restart your postgresql server.

```bash
$ sudo systemctl restart postgresql.service
```

You will now need to set environment `POSTGRES_HOST` your private IP address like following.

```
POSTGRES_HOST=192.168.1.22 				# my local postgresql server ip address
```

For creating a postgresql `role` , `database` & enabling `extensions`.

```bash
$ sudo su - postgres
$ psql
psql> CREATE DATABASE myproject;
psql> CREATE USER myprojectuser WITH PASSWORD 'password';
psql> GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
psql> CREATE EXTENSION postgis;
```

## **MIN**IO for object storage

We are using minio for object storage.
Document Reference: https://github.com/minio/minio/blob/master/docs/orchestration/docker-compose/docker-compose.yaml \
Minio is similar to AWS S3 but we can host it by ourself on our own environment. This makes our web app scalable as it becomes more compatible with AWS.

We have written custom Storage Backend at `project.storage_backends`

> _Note:_ Now we can open `minio.localhost` on browser and login with `username: root` and `password: rootrootroot` on MinIO web UI. Here we need to set permission of public-readonly to `publicuploads` folder so that static files can be retrieved anonymously unsigned.

![Minio Web UI](https://private-user-images.githubusercontent.com/58771387/289463999-b1e9d411-52a1-4948-b732-5e1e9db18d5e.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDIyODI0MjEsIm5iZiI6MTcwMjI4MjEyMSwicGF0aCI6Ii81ODc3MTM4Ny8yODk0NjM5OTktYjFlOWQ0MTEtNTJhMS00OTQ4LWI3MzItNWUxZTlkYjE4ZDVlLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzEyMTElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMjExVDA4MDg0MVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTg4YTc2MjliMzc4NmYxOTJiNDY2MzAzY2RlZTlhOTRiYzNmODBjY2Q1N2MxYzdhNDM2OWI0NTYyN2VlZTMyYTkmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.tNwXpSWo2lppqybiRvbP4U4TXpOP14_fnvGPHP2ym90)

_Now staticfiles is accessible publicly._

## Status and Logs

For viewing status of your docker container.

```bash
    $ docker-compose ps
    Name               Command               State           Ports
    ------------------------------------------------------------------------
    nginx    /docker-entrypoint.sh ngin ...   Up      0.0.0.0:80->80/tcp
    web      sh entrypoint.sh                 Up      0.0.0.0:8001->8001/tcp
    worker   celery -A project worker - ...   Up
```

For viewing logs of your docker services.

```bash
    $ docker-compose logs -f  --tail 1000 web
     Apply all migrations: account, admin, auth, authtoken, contenttypes, core, sessions, sites, socialaccount, user
    Running migrations:
      Applying contenttypes.0001_initial... OK
      Applying contenttypes.0002_remove_content_type_name... OK
      Applying auth.0001_initial... OK
```

## Accessing the web application

> **_Web-Application-Django_** is available at http://django.localhost \
> **_Web-Application-FASTAPI_** is available at http://fastapi.localhost & http://django.localhost/fastapi/ \
> **_ObjectStorageConsole-MinIO_** is available at http://minio.localhost

## Using Custom Model Fields for S3 storage support

```python
from django.db import models
from project.storage_backends import S3PrivateMediaStorage, S3PublicMediaStorage
from django.conf import settings
from django.utils.translation import gettext_lazy as _


# Create your models here.
class UserUploadModel(models.Model):
    upload_files = models.FileField(
        storage=S3PrivateMediaStorage() if settings.OBJECT_STORAGE in ("S3", "MINIO") else None,
        null=True,
        blank=True
    )
    upload_public_files = models.FileField(
        storage=S3PublicMediaStorage() if settings.OBJECT_STORAGE in ("S3", "MINIO") else None,
        null=True,
        blank=True
    )
    name = models.CharField(_("Name"), max_length=50)
```

## How to read files of S3 with libraries that don't support URL as pandas

```python
import boto3
import pandas as pd
s3 = boto3.client('s3', region_name='your_region')
s3.download_file('your_bucket_name', 'path/to/your/file.csv', 'local_file_name.csv')
df = pd.read_csv('local_file_name.csv')
os.remove('local_file_name.csv')
```

> **Warning**
> Don't forget to delete the downloaded file once work is complete. It can cause unwanted storage usage on server.
