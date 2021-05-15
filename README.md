# Food delivery service
[![Python Version](https://img.shields.io/badge/python-3.8.1-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3.2-brightgreen.svg)](https://djangoproject.com)
[![Django Rest Framework Version](https://img.shields.io/badge/djangorestframework-3.12.4-brightgreen.svg)](https://www.django-rest-framework.org/)
## 
The aim of this web project is to develop a food delivery system. This service will allow people to order food in various restaurants or cafés with delivery. They may choose among different establishments.At each establishment, the customer may choose a food of interest to them., read its description, add to cart .  They can connect their credit card to their account thereby paying for the order or pay in cash when the order is received.
## Getting started
#### Clone the repository:
* `git clone https://github.com/ArystanIgen/DjangoProject.git`
#### Requirements :
* `pip install -r requirements.txt`
#### Create PostgreSQL database:
* https://www.postgresqltutorial.com/postgresql-getting-started/
#### Configure database in settings.py:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'example_name',
        'USER': 'example_user',
        'PASSWORD': 'example_pasword',
        'HOST': 'http://127.0.0.1:8000/',
        'PORT': '5432',
    }
}
```
#### Run database migrations:
* `python manage.py migrate`
#### Create a superuser:
* `python manage.py createsuperuser`
#### Enjoy:
* `python manage.py runserver`
