from django.shortcuts import render
from .serializers import Inquiryserializer
from rest_framework import viewsets
from .models import Inquiry



class Inquiryviewset(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = Inquiryserializer

# Create your views here.


# Create your views here.
