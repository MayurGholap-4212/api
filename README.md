Features
**Django REST Framework Book API**

Create, Read, Update, and Delete (CRUD) operations for books.

Uses Django REST Framework for API development.

Includes model validation for book details.

Provides a unique ISBN field for book identification.

Installation

Prerequisites

Python 3.x

Django 3.x or later

Django REST Framework

Setup

Clone the repository

git clone <repository_url>
cd <project_directory>

Create a virtual environment and activate it

python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

Install dependencies

pip install -r requirements.txt

Run database migrations

python manage.py migrate

Create a superuser (optional, for admin panel access)

python manage.py createsuperuser

Run the server
python manage.py runserver

API Endpoints

Method

Endpoint

Description

GET

/api/books/

Retrieve a list of all books

POST

/api/books/

Create a new book

GET

/api/books/{id}/

Retrieve details of a specific book

PUT

/api/books/{id}/

Update details of a book

DELETE

/api/books/{id}/

Delete a book
