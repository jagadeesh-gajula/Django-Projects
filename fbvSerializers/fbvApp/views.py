import re
from select import select
from django.shortcuts import render
from .models import student
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import studentSerializer
from fbvApp import serializers
from rest_framework import status

# Create your views here.
@api_view(['GET','POST'])
def get_students(request):

    if request.method == 'GET':
        students = student.objects.all()
        students = studentSerializer(students,many=True)
        return Response(students.data)

    if request.method == 'POST':
        serializer = studentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET','PUT','DELETE'])
def student_details(request,primarykey):
    try:
        stud = student.objects.get(pk = primarykey)
    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        stud = studentSerializer(stud)
        return Response(stud.data)

    elif request.method == 'PUT':
        serializer = studentSerializer(stud,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        stud.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
