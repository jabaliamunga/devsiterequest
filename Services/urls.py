from django.urls import path, include
from .views import ServiceViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'services', ServiceViewSet)

urlpatterns = router.urls