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
# On Linux(debian based)
sudo apt install virtualenv
virtualenv venv
source venv/bin/activate
# OR
python -m venv venv
source venv/bin/activate  # On Linux/Mac
# OR
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

### 6. Create Superuser
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

### Swagger Documentation Access
Access the Swagger API documentation at:
```
http://localhost:8000/api/docs/
```

### Overview
![Swagger API Documentation](project_management_system/images/swagger_api_documentation)

### Authentication Steps

> **Note**: You need to login and get your access token to access the protected endpoints.

#### Public Endpoints (No Token Required):
- GET /api/users/login/
- POST /api/users/register/

#### Login Process
1. Access the login endpoint:
   ```
   http://localhost:8000/api/users/login/
   ```

2. Use these credentials:
   ```json
   {
   "username": "user1",
   "password": "password123"
   }
   ```
   ![Sample User Login Credentials](project_management_system/images/sample_user_login_credentials)

#### Setting Up Authentication
1. Copy the access token from the response:
   ![Copy The Access Token](project_management_system/images/copy_access_token)

2. Authorize in Swagger UI:
   ![Authorize The Access Token](project_management_system/images/authorize_access_token)

3. Paste the access token:
   ![Paste The Access Token](project_management_system/images/paste_access_token)

### Testing API Endpoints
After authentication, you can access all protected endpoints. For example:
Reading all projects from Swagger API documentation:
![Read All The Projects](project_management_system/images/get_all_project_details)

## Authentication

The system uses JWT (JSON Web Token) authentication. To access protected endpoints:
1. Obtain a token by logging in
2. Include the token in the Authorization header: `Bearer <your-token>`
