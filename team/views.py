from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .serializers import MemberSerializer
from .models import Member

class MemberView(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
