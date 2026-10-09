# Homework 2 - Movie Theater Booking Application

## Overview

This project is a Movie Theater Booking Application built with Python, Django, and Django REST Framework.

The application allows users to:

- View movie listings
- View seat availability
- Book seats
- View booking history
- Access movie, seat, and booking data through REST API endpoints

The application also includes a Bootstrap-based web interface, automated testing, Behavior-Driven Development testing with Behave, and deployment through Render.

## Features

- Movie listing page
- Seat availability page
- Booking history page
- REST API for movies
- REST API for seats
- REST API for bookings
- Automatic seat status updates when a booking is created
- Prevention of booking an already-booked seat
- Bootstrap responsive interface
- Unit testing
- API integration testing
- Behave BDD testing
- Render deployment

## Technologies Used

- Python
- Django
- Django REST Framework
- Bootstrap
- SQLite
- PostgreSQL
- Gunicorn
- WhiteNoise
- Behave
- behave-django
- Git
- GitHub
- Render

## Project Structure

    homework2/
    ├── README.md
    │
    └── movie_theater_booking/
        ├── bookings/
        │   ├── migrations/
        │   ├── templates/
        │   │   └── bookings/
        │   │       ├── base.html
        │   │       ├── movie_list.html
        │   │       ├── seat_booking.html
        │   │       └── booking_history.html
        │   ├── admin.py
        │   ├── apps.py
        │   ├── models.py
        │   ├── serializers.py
        │   ├── tests.py
        │   ├── urls.py
        │   └── views.py
        │
        ├── features/
        │   ├── booking.feature
        │   └── steps/
        │       └── booking_steps.py
        │
        ├── movie_theater_booking/
        │   ├── settings.py
        │   ├── urls.py
        │   ├── asgi.py
        │   └── wsgi.py
        │
        ├── build.sh
        ├── manage.py
        └── requirements.txt

## Setup Instructions

### 1. Navigate to the Homework 2 directory

    cd CS4300/homework2

### 2. Create a virtual environment

    python3 -m venv myenv --system-site-packages

### 3. Activate the virtual environment

    source myenv/bin/activate

### 4. Navigate to the Django project

    cd movie_theater_booking

### 5. Install the required dependencies

    pip install -r requirements.txt

### 6. Apply database migrations

    python3 manage.py migrate

## Running the Application Locally

From the directory containing `manage.py`, run:

    python3 manage.py runserver 0.0.0.0:3000

When running inside DevEdu, open the application using the App button.

The main pages are:

- `/` - Movie listings
- `/seats/` - Seat availability
- `/history/` - Booking history
- `/api/` - REST API root


## Deployment

The application is deployed using Render.

The deployed application uses:

- Gunicorn
- PostgreSQL
- WhiteNoise
- Django migrations
- Static-file collection
- Environment variables for production configuration

### Render Build Command

    ./build.sh

### Render Start Command

    gunicorn movie_theater_booking.wsgi:application

## Render URL

Live application:

https://cs4300-oxn4.onrender.com

API root:

https://cs4300-oxn4.onrender.com/api/

Movie API:

https://cs4300-oxn4.onrender.com/api/movies/

Seat API:

https://cs4300-oxn4.onrender.com/api/seats/

Booking API:

https://cs4300-oxn4.onrender.com/api/bookings/

## GitHub Repository

https://github.com/nhinebaugh/CS4300

## AI Usage Disclosure

ChatGPT was used as a learning, development, and troubleshooting assistant during this assignment.

ChatGPT was used to assist with:

- Understanding Django project structure
- Understanding Django models, views, and templates
- Understanding database migrations
- Understanding Django REST Framework serializers and viewsets
- Creating and understanding REST API routing
- Creating Bootstrap-based templates
- Writing and understanding unit and integration tests
- Creating Behave BDD tests
- Debugging Django errors
- Troubleshooting Render deployment
- Assisting with README documentation

AI-generated suggestions and code were reviewed, tested, and incorporated into the project where appropriate.
The final application was tested locally using DevEdu, Django's automated test system, Behave, and the deployed Render application.
