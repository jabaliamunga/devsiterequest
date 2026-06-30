from rest_framework import serializers
from .models import Inquiry


class Inquiryserializer(serializers.ModelSerializer):
    class Meta:
        model= Inquiry
        fields = '__all__'