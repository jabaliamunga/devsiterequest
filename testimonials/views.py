from django.shortcuts import render

from .serializers import TestimonialSerializer
from .models import Testimonial
from rest_framework.viewsets import ModelViewSet

class TestimonialView(ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
