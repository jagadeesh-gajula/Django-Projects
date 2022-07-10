from urllib.parse import urlparse
from django.urls import URLPattern, path
from .views import get_students,student_details

urlpatterns=[
    path('students/',get_students),
    path('students_details/<int:primarykey>',student_details)
]