from .models import TodoItem
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = "__all__"