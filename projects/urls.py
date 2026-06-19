from .views import ProjectView
from rest_framework import routers
router = routers.DefaultRouter()
from django.urls import include, path

router.register(r"projects", ProjectView, basename="project")

urlpatterns = [
    path("", include(router.urls))
]
