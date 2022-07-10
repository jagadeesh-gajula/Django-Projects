from urllib import response
from django.shortcuts import render
from django.http import JsonResponse
from .models import employee
from rest_framework.decorators import api_view
from .serializer import employeeSerializer
from rest_framework.response import Response


# Create your views here.
def employeeview(request):
    emp = {"name":"jagadeesh","id":230}

    data = employee.objects.all()
    response = {"employees":list(data.values())}

    return JsonResponse(response)


@api_view(['GET'])
def get_emp(request):
    employees = employee.objects.all()
    employees = employeeSerializer(employees,many=True)
    return Response(employees.data)


