from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render

from .models import Blog

# Create your views here.
def blog(request):
    posts = Blog.objects.all()
    return render(request, 'blogs.html', {'posts': posts})