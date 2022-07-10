from django.urls import path
from . import views


urlpatterns = [
    path('',views.getData),
    path('add/',views.addItem),
    path('getblog',views.getblog),
    path('addblog',views.addblog),
    path('getmessage',views.getmessage),
    path('postmessage',views.postmessage),
]