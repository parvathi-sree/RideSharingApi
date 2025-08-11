from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Ride


class RideAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="test123"
        )
        self.client.login(username="testuser", password="test123")

        self.ride = Ride.objects.create(
            rider=self.user,
            status="started"
        )

    def test_create_ride_authenticated(self):
        url = reverse("ride-list")
        data = {
            "status": "started",
            "pickup_location": "edapally",
            "dropoff_location": "kaloor",
            "rider":1
        }
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ride.objects.count(), 2)

    def test_create_ride_unauthenticated(self):
        self.client.logout()
        url = reverse("ride-list")
        data = {"status": "started"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_ride_status(self):
        url = reverse("ride-update-status", args=[self.ride.id])
        data = {"status": "completed"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.ride.refresh_from_db()
        self.assertEqual(self.ride.status, "completed")


class UserAPITestCase(APITestCase):
    def test_create_user(self):
        url = reverse("user-list")
        data = {"username": "user1", "password": "user123"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
