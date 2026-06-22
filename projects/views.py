from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .serializers import ProjectSerializer
from .models import Project

class ProjectView(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    