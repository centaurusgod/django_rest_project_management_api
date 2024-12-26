# Project Management System

A robust Django-based project management system that allows efficient management of projects, tasks, and team collaboration.



## ⚡️ Quick Start Guide

### 1. Clone the Repository
```bash
git clone <repository-url>
cd project_management_system
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
# or
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
```bash
python manage.py migrate
```

### 5. Create Superuser
```bash
python manage.py createsuperuser
```
Use the following credentials:
- Username: ozone
- Email: ozonewagle998@gmail.com
- Password: ozone12345

### 6. Populate Database
```bash
python techforing_pms/populate_db.py
```

### 7. Run Development Server
```bash
python manage.py runserver
```

## 🔗 API Documentation

Access the Swagger API documentation at:
```
http://localhost:8000/api/schema/swagger-ui/
```
![Swagger API Documentation](images/swagger_api_documentation.png)

## 🚀 Tech Stack

- Python 3.12.3
- Django 5.1.4
- Django REST Framework
- JWT Authentication
- SQLite3 Database
- Swagger/OpenAPI Documentation

## 🔒 Authentication

The system uses JWT (JSON Web Token) authentication. To access protected endpoints:
1. Obtain a token by logging in
2. Include the token in the Authorization header: `Bearer <your-token>`

