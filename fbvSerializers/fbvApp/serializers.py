from dataclasses import field
from rest_framework.serializers import ModelSerializer
from .models import student

class studentSerializer(ModelSerializer):
    class Meta:
        model = student
        fields = ['id','name','score']