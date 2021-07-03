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