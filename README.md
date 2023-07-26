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

   
## API Endpoints

- `POST /api/register/`: Register a new user.
- `POST /api/login/`: Login and obtain access and refresh tokens.
- `POST /api/logout/`: Logout and invalidate the token.


## Contact

For any questions or feedback, please contact bk006822@gmail.com