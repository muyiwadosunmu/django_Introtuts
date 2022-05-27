from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Vehicle
from .serializers import VehicleSerializer
# Create your views here.

class VehicleView(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer 