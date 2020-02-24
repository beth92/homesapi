# Django API For Modeling Home Data

Basic API for querying real estate data using Django and Django Rest Framework.
Built with Python 3.8.1.

## Setup

Create virtual env and install dependencies: 
```bash
$ python -m venv env
$ . env/bin/activate
$ pip install -r requirements.txt
```

Set up sqlite database: 
```bash
$ python manage.py migrate
```

To seed the DB with the sample data:
```bash
$ python manage.py ingestcsv
```
Can also accept a file name parameter (relative to this directory)

## Run API Server

```bash
$ python manage.py runserver
```

## View API Docs

Docs are auto-generated via [drf-yasg](https://github.com/axnsan12/drf-yasg)
with SwaggerUI. With server running, visit http://localhost:8000/docs to view
and try out some requests. 


## Run Tests

Run unit tests with:
```bash
$ python manage.py test rest_api.tests
```
