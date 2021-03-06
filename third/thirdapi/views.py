from functools import partial
import json
from django.shortcuts import render
import requests
import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def student_api(request):
    if request.method =='GET':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data= JSONParser().parse(stream)
        id=python_data.get('id', None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer= StudentSerializer(stu)
            json_data=JSONRenderer().render(serializer.data)

            return HttpResponse(json_data, content_type='application/json')
        
    
        stu=Student.objects.all()
        serializer= StudentSerializer(stu,many=True)
        json_data=JSONRenderer().render(serializer.data)

        return HttpResponse(json_data, content_type='application/json')


    if request.method =='POST':
        json_data=request.body
        print(json_data)
        stream=io.BytesIO(json_data)
        python_data= JSONParser().parse(stream)
        serializer=StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Saved'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')


    if request.method =='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data= JSONParser().parse(stream)
        id=python_data.get('id')
        stu=Student.objects.get(id=id)
        print("stsdfadu",stu)
        serializer=StudentSerializer(stu,data=python_data)
        print("serializerdsfasfdaAAAA",serializer)
        
        if serializer.is_valid():
            print("serializer",serializer.validated_data)
            serializer.save()
            res={'msg':'Updated'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')

        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')    

    if request.method =='DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data= JSONParser().parse(stream)
        id=python_data.get('id')
        stu=Student.objects.get(id=id)
        print("stsdfadu",stu)
        stu.delete()
        res={'msg':'Deleted'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
        
       