from django.urls import path, include
from .views import MemberView
from rest_framework import routers
router = routers.DefaultRouter()

router.register(r"members", MemberView)

urlpatterns = [
    path("", include("router.urls"))
]
