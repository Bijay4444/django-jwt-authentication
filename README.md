# django-jwt-authentication
This repository was made for task given for me as intern selection 

# Django JWT Authentication API

This project is a Django Rest Framework (DRF) API that allows users to register, login, and logout using JWT Token authentication. The tokens have a short lifespan and expire every 5 minutes.

## Installation

1. Clone the repository:
  git clone https://github.com/your-username/django-jwt-authentication.git

2. Create a virtual environment and install the required packages:
  cd django-jwt-authentication
  python -m venv venv
  source venv/bin/activate # On Windows, use venv\Scripts\activate
  pip install -r requirements.txt

3. Run the Django development server:
   python manage.py runserver

4. Test the API using tests.py
   python manage.py test api
   
## API Endpoints

- `POST /api/register/`: Register a new user.
- `POST /api/login/`: Login and obtain access and refresh tokens.
- `POST /api/logout/`: Logout and invalidate the token.

## API Testing Using curl operations:
- Rgister: curl -X POST http://127.0.0.1:8000/api/register/ -d "name=Bijay&email=bij@gmail.com&phone_number=09230932&password=keytosuce33"
- login : curl -X POST http://127.0.0.1:8000/api/login/ -d "email=bij@gmail.com&password=keytosuce33"
- logout: curl -X POST http://127.0.0.1:8000/api/logout/ -d "refresh_token=<your_refresh_token>"

## To make the test easier I have already made tests.py to carry out the test in api
  python manage.py test api

## Contact

For any questions or feedback, don't hesitate to get in touch with bk006822@gmail.com
