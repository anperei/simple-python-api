# Simple Django API

This is a minimal Django project providing a simple REST API endpoint.

## Features

- Django 5.x project structure
- REST API endpoint using Django REST Framework
- Example endpoint: `/api/hello/<name>/` returns a greeting

## Installation

1. **Clone the repository**

2. **Install dependencies**
   ```sh
   pip install django djangorestframework
   ```

3. **Apply migrations**
   ```sh
   python manage.py migrate
   ```

4. **Run the development server**
   ```sh
   python manage.py runserver
   ```

## API Usage

- **Hello endpoint:**  
  `GET /api/hello/<name>/`  
  Returns:  
  ```json
  {"message": "Hello, <name>!"}
  ```


