from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from blog import views



def home(request):
    #return HttpResponse("<h1> this is home page </h1>")
    return render(request,'index.html')


def blog(request):
    mes = { "greeting": "hi user this is greeting !"}
    return render(request,'index.html',mes)


def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'signup.html', {'form': form})


