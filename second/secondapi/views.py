from django.shortcuts import render
from requests.api import post
import io
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from .serializers import StudentSerializer
from .models import Student
from rest_framework.parsers import JSONParser
import json

# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer= StudentSerializer(data=python_data)
        if serializer.is_valid():
            print("VAlidatinggGGGGGGGGGGGG")
            
            serializer.save()
            #print("serialize.data", serializer.data)
            res={'msg': 'Data Created'}
            json_data= JSONRenderer().render(res)
            #print(res['msg'])
            print("HAHAHAHAHA")
            return HttpResponse(json_data, content_type='application/json')

        
        json_data= JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')


