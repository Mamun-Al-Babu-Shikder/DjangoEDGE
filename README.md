# Django CRUD Project - EDGE Program

This is a Django-based CRUD (Create, Read, Update, Delete) project developed for the EDGE Program. The project follows the MVT (Model-View-Template) architecture and provides a RESTful API for CRUD operations using Django REST framework.

## Prerequisites
Make sure you have the following installed on your system:
- Python (>= 3.8)
- pip (Python package manager)
- Virtualenv (recommended for dependency management)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Mamun-Al-Babu-Shikder/DjangoEDGE
cd DjangoProject
```

### 2. Create and Activate a Virtual Environment
```bash
# Install virtualenv if not already installed
pip install virtualenv

# Create a virtual environment
virtualenv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install django djangorestframework
```

### 4. Create a Django Project
```bash
django-admin startproject myproject .
```

### 5. Create a Django App
```bash
python manage.py startapp myapp
```

### 6. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create a Superuser (For Admin Panel)
```bash
python manage.py createsuperuser
```

### 8. Run the Development Server
```bash
python manage.py runserver
```
Access the application at: `http://127.0.0.1:8000/`

## Project Structure
```
myproject/
|-- myapp/       # Application containing models, views, and serializers
|-- myproject/   # Project settings and configurations
|-- manage.py    # Django management script
|-- requirements.txt # List of dependencies
```

## REST API Endpoints
| Method | Endpoint          | Description       |
|--------|------------------|------------------|
| GET    | /api/items/      | Get all items    |
| GET    | /api/items/\<id\>/ | Get single item  |
| POST   | /api/items/      | Create item      |
| PUT    | /api/items/\<id\>/ | Update item      |
| DELETE | /api/items/\<id\>/ | Delete item      |

## Useful Django Commands
```bash
# Collect static files
python manage.py collectstatic

# Run tests
python manage.py test

# Check for issues
python manage.py check

# Show available commands
python manage.py help
```

