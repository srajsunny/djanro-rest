from .models import Student
from rest_framework import serializers


class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=50)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
