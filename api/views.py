
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Ride
from .serializers import UserSerializer, RideSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(rider=self.request.user)

    @action(detail=True, methods=["patch"])
    def update_status(self, request, pk=None):
        ride = self.get_object()
        ride.status = request.data.get("status", ride.status)
        ride.save()
        return Response(RideSerializer(ride).data)

