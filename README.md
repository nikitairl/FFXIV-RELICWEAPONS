# FFXIV-RELICWEAPONS
# How to get a Zodiac Weapon for every job in FFXIV using Django, Docker, Nginx, Gunicorn and Postgres

## [relicweapons.com](http://relicweapons.com/) - the site should work, but may be abandoned



If you are a fan of Final Fantasy XIV, you might have heard of the Zodiac Weapons, a series of powerful and customizable weapons that can be obtained through a long and challenging questline. Each job in the game has its own Zodiac Weapon, and they are considered one of the ultimate goals for endgame players.

How do you know which materials you need, which dungeons you have to run, which trials you have to complete, and which NPCs you have to talk to?

That's where this project comes in. I have created a web application using Django, Docker, Nginx, Gunicorn and Postgres that will help you get your Zodiac Weapons faster and easier.

In this blog post, I will show you how to set up and run the project on your own Linux server using Docker Compose. You will need some basic knowledge of Linux commands, Docker, Nginx and Postgres to follow along. If you are not familiar with these technologies, don't worry, I will provide some links and resources to help you get started.

## Prerequisites

Before we begin, you will need to have the following installed on your Linux server:

- Docker: A tool that allows you to create and run containers that isolate your applications from the host system. You can install Docker following the official instructions here: https://docs.docker.com/engine/install/
- Docker Compose: A tool that allows you to define and run multiple containers using a YAML file. You can install Docker Compose following the official instructions here: https://docs.docker.com/compose/install/
- Git: A version control system that allows you to clone and update the project code from GitHub. You can install Git following the official instructions here: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

## Clone the project code

The first step is to clone the project code from GitHub to your server. You can do this by running the following command in your terminal:

This will create a directory called `ffxiv-zodiac-weapon-guide` in your current working directory. You can change the name of the directory if you want, but make sure to use the same name throughout this tutorial.

## Configure the environment variables

The next step is to configure some environment variables that will be used by the project. These variables include:

- `SECRET_KEY`: A secret key that is used by Django for security purposes. You can generate a random secret key using this tool: https://djecrety.ir/
- `DEBUG`: A boolean value that determines whether Django runs in debug mode or not. Debug mode is useful for development and testing, but should be set to `False` for production.
- `ALLOWED_HOSTS`: A list of hostnames or IP addresses that are allowed to access the web application. You should include your server's hostname or IP address here, as well as any domain names that point to it.
- `DATABASE_URL`: A URL that specifies the connection details for the Postgres database. The format of the URL is: `postgres://user:password@host:port/database`
- `FFXIV_API_KEY`: An API key that is used to access the FFXIV API, a third-party service that provides data about the game. You can obtain an API key by registering here: https://xivapi.com/account

To set these variables, you need to create a file called `.env.dev` and `.env.db` in the root directory of the project (the same directory where the `docker-compose.yml` file is located). The file should look something like this:
```
.env.dev exam
DEBUG='0 or 1'
SECRET_KEY='you'r django key'
ALLOWED_HOSTS=localhost 127.0.0.1 example.com 111.111.111.111:example-ip www.example.com [::1]
POSTGRES_ENGINE=django.db.backends.postgresql
POSTGRES_DB=postgresdb
POSTGRES_USER=postgresuser
POSTGRES_PASSWORD=postgrespassword
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

```
.env.db example
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
```

### Docker-compose
To start the composing process:
```
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec web python manage.py loaddata data.json
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --noinput
```