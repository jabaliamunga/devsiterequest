from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import TestimonialView

router = DefaultRouter()

router.register(r"testimonials", TestimonialView, basename="Testimonials")

urlpatterns = [
    path("", include(router.urls))
]
