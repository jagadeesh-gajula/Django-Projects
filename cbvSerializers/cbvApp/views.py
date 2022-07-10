from django.shortcuts import render
from .models import student
from .serializers import studentSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404

#required for mixins
from rest_framework import mixins,generics

# Create your views here.
class StudentList(APIView):

    def get(self,request):
        students = student.objects.all()
        serializer = studentSerializer(students,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = studentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class StudentDetail(APIView):
    def get_obj(self,pk):
        try:
            return student.objects.get(pk=pk)
        except student.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        student = self.get_obj(pk)
        serializer = studentSerializer(student)
        return Response(serializer.data)

    def put(self,request,pk):
        student = self.get_obj(pk)
        serializer = studentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_202_ACCEPTED)
        return Response(status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        student = self.get_obj(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    

## mixin classes
class mixin_student_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = student.objects.all()
    serializer_class = studentSerializer

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)

class mixin_student_detail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = student.objects.all()
    serializer_class = studentSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)

    def put(self,request,pk):
        return self.update(request,pk)

    def delete(self, request, pk):
        return self.destroy(request,pk)

# Generics
class generic_student_list(generics.ListCreateAPIView):
    queryset = student.objects.all()
    serializer_class = studentSerializer

class generic_student_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = student.objects.all()
    serializer_class = studentSerializer