# Project Management System

A robust Django-based project management system that allows efficient management of projects, tasks, and team collaboration.



## Guidelines

### 1. Clone the Repository
```bash
git clone https://github.com/centaurusgod/django_rest_project_management_api.git
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
python manage.py makemigrations
python manage.py migrate
```

### 5. Populate Database with Dummy Data
```bash
python techforing_pms/populate_db.py
```

### 5. Create Superuser
```bash
python manage.py createsuperuser
```
Use the following credentials:
- Username: your_username
- Email: your_email@example.com
- Password: Password123!


### 7. Run Development Server
```bash
python manage.py runserver
```

## API Documentation

Access the Swagger API documentation at:
```
http://localhost:8000/api/docs/
```
![Swagger API Documentation](project_management_system/images/swagger_api_documentation.png)


## 🔒 Authentication

The system uses JWT (JSON Web Token) authentication. To access protected endpoints:
1. Obtain a token by logging in
2. Include the token in the Authorization header: `Bearer <your-token>`

