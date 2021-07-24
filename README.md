## Description
Project for Bachelor's Degree final exam.

This combines the Scrapy framework web crawling spiders with Django ORM to effectively scrape and store information 
found on pre-configured news or other information-rich sites based on some search criteria.

## Technicalities
Developed and tested with:
-  Python 3.8
-  Django 3.2.4
-  Scrapy 2.5.0
-  scrapy-djangoitem 1.1.1

## Development process
- Install required packages
- Create a new Scrapy project:
```angular2html
scrapy startproject game_spiders
```
- Create a new Django project and restructure it to fit with the Scrapy project:
```angular2html
django-admin startproject django_mainframe
```

## How to use
- Install requirements
- Create .env file or set required ENV variables:
```python
# specify to the Django ORM to use a sqlite database, defaults to false; 
# if set to true, this requires the sqlite database to have the jsonb1 update/patch
USE_SQLITE = False 
# Following DB_* settings are required only if USE_SQLITE is set to false
DB_ENGINE = "django.db.backends.postgresql_psycopg2" # for different databases, see https://docs.djangoproject.com/en/3.2/ref/settings/#engine
DB_HOST = '127.0.0.1' 
DB_USER = 'user'
DB_PASSWORD = 'pass'
DB_NAME = 'db_name'
DB_PORT = '5432'
DB_SCHEMA = None # Required only if using a schema-capable database like PostgreSQL, and schema is not public
```