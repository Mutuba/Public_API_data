from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Dog


class DogsSerializer(ModelSerializer):
    class Meta:
        model = Dog
        fields = "__all__"
