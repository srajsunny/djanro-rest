from .models import Student
from rest_framework import serializers


class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=50)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print("instance",instance.name)
        instance.name= validated_data.get('name', instance.name)
        print("instance",instance.name)
        instance.roll= validated_data.get('roll', instance.roll)
        instance.city= validated_data.get('city', instance.city)    
        instance.save()
        print("instance",instance.name)
        return instance