# Django Blog REST API

A Blog REST API built using Django and Django REST Framework.

## Features

- CRUD Operations
- Django REST Framework
- Search
- Filtering
- Ordering
- Pagination
- Authentication
- Permissions

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite

## Installation

```bash
git clone https://github.com/yourusername/django-blog-rest-api.git
cd django-blog-rest-api
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /posts/ | List all posts |
| POST | /posts/ | Create a post |
| GET | /posts/{id}/ | Retrieve a post |
| PUT | /posts/{id}/ | Update a post |
| DELETE | /posts/{id}/ | Delete a post |
