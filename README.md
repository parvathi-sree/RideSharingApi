# RideSharingApi
basic Ride Sharing API using Django Rest Framework (DRF) with class-based viewsets, including models, serializers, views
## Features

- Create API endpoints for user registration and login using Django Rest Framework (DRF).
- API endpoints for creating a ride request, viewing a ride's details, and listing all rides
- Implement API endpoints for updating the status of a ride
- Unit tests 

##  Setup Instructions
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

## API Endpoints
- POST /api/users/ → Register user
- POST /api/rides/ → Create ride request
- GET /api/rides/ → List rides
- PATCH /api/rides/{id}/update_status/ → Update ride status
