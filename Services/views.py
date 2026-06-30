from django.shortcuts import render
from rest_framework import viewsets
from .models import Services
from .serializers import serviceserializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = serviceserializer
# Create your views here.


# Create your views here.
