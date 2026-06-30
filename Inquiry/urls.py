from django.urls import path, include
from .views import Inquiryviewset
from rest_framework.routers import DefaultRouter

inquiries = DefaultRouter()
inquiries.register(r'inquiries', Inquiryviewset)

urlpatterns = inquiries.urls